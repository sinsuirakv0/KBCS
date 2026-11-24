# v16.0.0 → v16.0.1 · 最優先の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-253706eac635914c5cc7f5db3c494165"></a>

### [`00545a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a50.md) → [`00545a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545a90.md) FUN_00545a90

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
      "definition_site": "00545a98",
      "incomplete_value": false,
      "site": "00545a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545a58",
      "incomplete_value": false,
      "site": "00545a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00545a9c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545a9c",
      "DATA",
      [
        "storage",
        "00c6a630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a50.md#insn-00545a58)
- 新版 [`00545a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545a90.md#insn-00545a98)

~~~diff
- 00545a58 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00545a58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00545a58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00545a58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545a98 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00545a98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545a98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545a98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00545a58 bytes 29c10891
+ 00545a98 bytes 29c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97209569968e988d49d394bbe8b1d0c"></a>

### [`00545a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a70.md) → [`00545ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545ab0.md) FUN_00545ab0

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
      "definition_site": "00545ab8",
      "incomplete_value": false,
      "site": "00545abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545a78",
      "incomplete_value": false,
      "site": "00545a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00545abc",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545abc",
      "DATA",
      [
        "storage",
        "00c6a630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a70.md#insn-00545a78) · [`00545a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a70.md#insn-00545a9c)
- 新版 [`00545ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545ab0.md#insn-00545ab8) · [`00545adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545ab0.md#insn-00545adc)

~~~diff
- 00545a78 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00545a78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00545a78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00545a78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545ab8 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00545ab8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545ab8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545ab8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00545a78 bytes 29c10891
+ 00545ab8 bytes 29c11891
- 00545a9c ["INT_ADD", "register:40f0:8", ["const:545a9c:8", "const:4:8"]]
- 00545a9c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00545adc ["INT_ADD", "register:40f0:8", ["const:545adc:8", "const:4:8"]]
+ 00545adc ["CALL", null, ["callee:00c57eb0:8"]]
- 00545a9c bytes 05481c94
+ 00545adc bytes f5481c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86af52fa9d04b9fbfb5a0f6eb1b74af8"></a>

### [`00545ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md) → [`00545af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545af0.md) FUN_00545af0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004ee534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00545b1c",
      "incomplete_value": false,
      "site": "00545b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545adc",
      "incomplete_value": false,
      "site": "00545adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00545b1c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545b1c",
      "DATA",
      [
        "storage",
        "00c6a630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md#insn-00545ac4) · [`00545ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md#insn-00545ad4) · [`00545afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md#insn-00545afc)
- 新版 [`00545b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545af0.md#insn-00545b04) · [`00545b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545af0.md#insn-00545b14) · [`00545b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545af0.md#insn-00545b3c)

~~~diff
- 00545ac4 ["INT_ADD", "register:40f0:8", ["const:545ac4:8", "const:4:8"]]
- 00545ac4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00545b04 ["INT_ADD", "register:40f0:8", ["const:545b04:8", "const:4:8"]]
+ 00545b04 ["CALL", null, ["callee:00c57e90:8"]]
- 00545ac4 bytes f3471c94
+ 00545b04 bytes e3481c94
- 00545ad4 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00545ad4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00545ad4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00545ad4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00545b14 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00545b14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00545b14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00545b14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00545ad4 bytes 4ac10891
+ 00545b14 bytes 4ac11891
- 00545afc ["INT_ADD", "register:40f0:8", ["const:545afc:8", "const:4:8"]]
- 00545afc ["CALL", null, ["callee:0043bb20:8"]]
+ 00545b3c ["INT_ADD", "register:40f0:8", ["const:545b3c:8", "const:4:8"]]
+ 00545b3c ["CALL", null, ["callee:0043bb20:8"]]
- 00545afc bytes f9d7fb97
+ 00545b3c bytes f9d7fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4c831b2bd29c235d3cc835d7fb79e08"></a>

### [`00545b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b24.md) → [`00545b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545b64.md) FUN_00545b64

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
      "definition_site": "00545b6c",
      "incomplete_value": false,
      "site": "00545b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545b2c",
      "incomplete_value": false,
      "site": "00545b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00545b6c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545b6c",
      "DATA",
      [
        "storage",
        "00c6a630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b24.md#insn-00545b28)
- 新版 [`00545b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545b64.md#insn-00545b68)

~~~diff
- 00545b28 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00545b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00545b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00545b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00545b68 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00545b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00545b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00545b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00545b28 bytes 08c10891
+ 00545b68 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-712c29d16f9873d4896fb93a58816411"></a>

### [`00547adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547adc.md) → [`00547b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b1c.md) FUN_00547b1c

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
      "definition_site": "00547b3c",
      "incomplete_value": false,
      "site": "00547b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547afc",
      "incomplete_value": false,
      "site": "00547b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00547b40",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00547b40",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547adc.md#insn-00547af0) · [`00547afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547adc.md#insn-00547afc)
- 新版 [`00547b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b1c.md#insn-00547b30) · [`00547b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b1c.md#insn-00547b3c)

~~~diff
- 00547af0 ["INT_ADD", "register:40f0:8", ["const:547af0:8", "const:4:8"]]
- 00547af0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00547b30 ["INT_ADD", "register:40f0:8", ["const:547b30:8", "const:4:8"]]
+ 00547b30 ["CALL", null, ["callee:00c57e90:8"]]
- 00547af0 bytes e83f1c94
+ 00547b30 bytes d8401c94
- 00547afc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00547afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00547afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00547afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00547b3c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00547b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00547b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00547b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00547afc bytes 08c10a91
+ 00547b3c bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90509592ebe68fdf79ef1f74ed307d08"></a>

### [`00547b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b14.md) → [`00547b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b54.md) FUN_00547b54

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
      "definition_site": "00547b5c",
      "incomplete_value": false,
      "site": "00547b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547b1c",
      "incomplete_value": false,
      "site": "00547b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00547b60",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00547b60",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b14.md#insn-00547b1c)
- 新版 [`00547b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b54.md#insn-00547b5c)

~~~diff
- 00547b1c ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00547b1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00547b1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00547b1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00547b5c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00547b5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00547b5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00547b5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00547b1c bytes 29c10a91
+ 00547b5c bytes 29c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84a155dbbeb5de507d8c6cc41772065"></a>

### [`00547d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md) → [`00547dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md) FUN_00547dc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547e00",
      "incomplete_value": true,
      "site": "00547e00",
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
      "definition_site": "00547dc0",
      "incomplete_value": true,
      "site": "00547dc0",
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
      "00547dec",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00547e00",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00547e08",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00547dec",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00547e00",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00547e08",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md#insn-00547da0) · [`00547dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md#insn-00547dac) · [`00547dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547d84.md#insn-00547dc8)
- 新版 [`00547de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md#insn-00547de0) · [`00547dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md#insn-00547dec) · [`00547e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547dc4.md#insn-00547e08)

~~~diff
- 00547da0 ["INT_ADD", "register:40f0:8", ["const:547da0:8", "const:4:8"]]
- 00547da0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00547de0 ["INT_ADD", "register:40f0:8", ["const:547de0:8", "const:4:8"]]
+ 00547de0 ["CALL", null, ["callee:00c57e90:8"]]
- 00547da0 bytes 3c3f1c94
+ 00547de0 bytes 2c401c94
- 00547dac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 00547dac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00547dec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 00547dec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00547dac bytes 29a144f9
+ 00547dec bytes 29a146f9
- 00547dc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 00547dc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00547e08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db8:8"]]
+ 00547e08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00547dc8 bytes 29dd44f9
+ 00547e08 bytes 29dd46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ef4780122b99fdb0d4b7d7d54e7f6b"></a>

### [`00547eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md) → [`00547f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md) FUN_00547f2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547f68",
      "incomplete_value": true,
      "site": "00547f6c",
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
      "definition_site": "00547f28",
      "incomplete_value": true,
      "site": "00547f2c",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00547fc0",
      "incomplete_value": true,
      "site": "00547fc0",
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
      "definition_site": "00547f80",
      "incomplete_value": true,
      "site": "00547f80",
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
      "00547f58",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00547f6c",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00547fb0",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00547f58",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00547f6c",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00547fb0",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md#insn-00547f40) · [`00547f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md#insn-00547f18) · [`00547f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547eec.md#insn-00547f58)
- 新版 [`00547f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md#insn-00547f80) · [`00547f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md#insn-00547f58) · [`00547f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547f2c.md#insn-00547f98)

~~~diff
- 00547f40 ["INT_ADD", "register:40f0:8", ["const:547f40:8", "const:4:8"]]
- 00547f40 ["CALL", null, ["callee:00c57e90:8"]]
+ 00547f80 ["INT_ADD", "register:40f0:8", ["const:547f80:8", "const:4:8"]]
+ 00547f80 ["CALL", null, ["callee:00c57e90:8"]]
- 00547f40 bytes d43e1c94
+ 00547f80 bytes c43f1c94
- 00547f18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 00547f18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00547f58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 00547f58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00547f18 bytes 08a144f9
+ 00547f58 bytes 08a146f9
- 00547f58 ["INT_ADD", "register:40f0:8", ["const:547f58:8", "const:4:8"]]
- 00547f58 ["CALL", null, ["callee:00c58000:8"]]
+ 00547f98 ["INT_ADD", "register:40f0:8", ["const:547f98:8", "const:4:8"]]
+ 00547f98 ["CALL", null, ["callee:00c58000:8"]]
- 00547f58 bytes 2a3f1c94
+ 00547f98 bytes 1a401c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c29c64f6d8d0bd018f4a6cd3eee0d66c"></a>

### [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) → [`00548584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md) FUN_00548584

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 8件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md) [`0052cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052cdf0.md) [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00548590",
      "incomplete_value": false,
      "site": "00548594",
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
      "definition_site": "00548550",
      "incomplete_value": false,
      "site": "00548554",
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
      "00548590",
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
      "00548590",
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

- 旧版 [`00548554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md#insn-00548554) · [`00548550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md#insn-00548550)
- 新版 [`00548594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md#insn-00548594) · [`00548590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548584.md#insn-00548590)

~~~diff
- 00548554 ["INT_ADD", "register:40f0:8", ["const:548554:8", "const:4:8"]]
- 00548554 ["CALL", null, ["callee:0043b778:8"]]
+ 00548594 ["INT_ADD", "register:40f0:8", ["const:548594:8", "const:4:8"]]
+ 00548594 ["CALL", null, ["callee:0043b778:8"]]
- 00548554 bytes 79ccfb97
+ 00548594 bytes 79ccfb97
- 00548550 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00548550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00548550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00548550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00548590 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00548590 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00548590 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00548590 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00548550 bytes 00303c91
+ 00548590 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9f9d45dd1fd8448c439f8ac8173a991"></a>

### [`00548a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md) → [`00548a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a6c.md) FUN_00548a6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00548a78",
      "incomplete_value": false,
      "site": "00548a7c",
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
      "definition_site": "00548a38",
      "incomplete_value": false,
      "site": "00548a3c",
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
      "00548a78",
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
      "00548a78",
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

- 旧版 [`00548a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md#insn-00548a3c) · [`00548a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md#insn-00548a38)
- 新版 [`00548a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a6c.md#insn-00548a7c) · [`00548a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a6c.md#insn-00548a78)

~~~diff
- 00548a3c ["INT_ADD", "register:40f0:8", ["const:548a3c:8", "const:4:8"]]
- 00548a3c ["CALL", null, ["callee:0043b778:8"]]
+ 00548a7c ["INT_ADD", "register:40f0:8", ["const:548a7c:8", "const:4:8"]]
+ 00548a7c ["CALL", null, ["callee:0043b778:8"]]
- 00548a3c bytes 3fcbfb97
+ 00548a7c bytes 3fcbfb97
- 00548a38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00548a38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00548a38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00548a38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00548a78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00548a78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00548a78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00548a78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00548a38 bytes 00303c91
+ 00548a78 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52fe8465231b7c23e6f1dfbf6ac561d6"></a>

### [`00548a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a54.md) → [`00548a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a94.md) FUN_00548a94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00548aac",
      "incomplete_value": true,
      "site": "00548ab0",
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
      "definition_site": "00548a6c",
      "incomplete_value": true,
      "site": "00548a70",
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
      "00548aa8",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00548ab0",
      "DATA",
      [
        "storage",
        "00c6a390",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00548aa8",
      "READ",
      [
        "storage",
        "00c9b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "00548ab0",
      "DATA",
      [
        "storage",
        "00c6a790",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a54.md#insn-00548a60) · [`00548a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a54.md#insn-00548a68) · [`00548a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a54.md#insn-00548a74)
- 新版 [`00548aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a94.md#insn-00548aa0) · [`00548aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a94.md#insn-00548aa8) · [`00548ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548a94.md#insn-00548ab4)

~~~diff
- 00548a60 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00548aa0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00548a60 bytes 883a00d0
+ 00548aa0 bytes 883a00f0
- 00548a68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
- 00548a68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00548aa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
+ 00548aa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00548a68 bytes 087546f9
+ 00548aa8 bytes 087540f9
- 00548a74 ["INT_ADD", "register:40f0:8", ["const:548a74:8", "const:4:8"]]
- 00548a74 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00548ab4 ["INT_ADD", "register:40f0:8", ["const:548ab4:8", "const:4:8"]]
+ 00548ab4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00548a74 bytes 0b3c1c94
+ 00548ab4 bytes fb3c1c94
~~~


<a id="compare-b5c34ba5209e6d23843d8736e1e2809c"></a>

### [`00548d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d04.md) → [`00548d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d44.md) FUN_00548d44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00548d5c",
      "incomplete_value": true,
      "site": "00548d60",
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
      "definition_site": "00548d1c",
      "incomplete_value": true,
      "site": "00548d20",
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
      "00548d58",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00548d60",
      "DATA",
      [
        "storage",
        "00c6a3e0",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00548d58",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ],
    [
      "00548d60",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d04.md#insn-00548d10) · [`00548d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d04.md#insn-00548d18) · [`00548d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d04.md#insn-00548d24)
- 新版 [`00548d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d44.md#insn-00548d50) · [`00548d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d44.md#insn-00548d58) · [`00548d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d44.md#insn-00548d64)

~~~diff
- 00548d10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00548d50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00548d10 bytes 883a00d0
+ 00548d50 bytes 883a00f0
- 00548d18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
- 00548d18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00548d58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00548d58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00548d18 bytes 088146f9
+ 00548d58 bytes 088140f9
- 00548d24 ["INT_ADD", "register:40f0:8", ["const:548d24:8", "const:4:8"]]
- 00548d24 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00548d64 ["INT_ADD", "register:40f0:8", ["const:548d64:8", "const:4:8"]]
+ 00548d64 ["CALL", null, ["callee:00c57ea0:8"]]
- 00548d24 bytes 5f3b1c94
+ 00548d64 bytes 4f3c1c94
~~~


<a id="compare-431394943beed66944ae5283c6365c05"></a>

### [`005491d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491d8.md) → [`00549218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549218.md) FUN_00549218

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
      "definition_site": "0054922c",
      "incomplete_value": false,
      "site": "00549230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005491ec",
      "incomplete_value": false,
      "site": "005491f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "00549230",
      "DATA",
      [
        "storage",
        "00c6a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00549230",
      "DATA",
      [
        "storage",
        "00c6a880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005491e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491d8.md#insn-005491e4) · [`005491ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491d8.md#insn-005491ec)
- 新版 [`00549224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549218.md#insn-00549224) · [`0054922c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549218.md#insn-0054922c)

~~~diff
- 005491e4 ["INT_ADD", "register:40f0:8", ["const:5491e4:8", "const:4:8"]]
- 005491e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00549224 ["INT_ADD", "register:40f0:8", ["const:549224:8", "const:4:8"]]
+ 00549224 ["CALL", null, ["callee:00c57e90:8"]]
- 005491e4 bytes 2b3a1c94
+ 00549224 bytes 1b3b1c94
- 005491ec ["COPY", "tmp:0:8", ["const:480:8"]]
- 005491ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005491ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005491ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054922c ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0054922c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054922c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054922c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005491ec bytes 08011291
+ 0054922c bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a92cd68d09108141d28d8e6fb0c6a0"></a>

### [`005492e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005492e0.md) → [`00549320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549320.md) FUN_00549320

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
      "definition_site": "00549334",
      "incomplete_value": false,
      "site": "00549338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005492f4",
      "incomplete_value": false,
      "site": "005492f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
      "00549338",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00549338",
      "DATA",
      [
        "storage",
        "00c6a910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005492ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005492e0.md#insn-005492ec) · [`005492f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005492e0.md#insn-005492f4)
- 新版 [`0054932c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549320.md#insn-0054932c) · [`00549334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549320.md#insn-00549334)

~~~diff
- 005492ec ["INT_ADD", "register:40f0:8", ["const:5492ec:8", "const:4:8"]]
- 005492ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0054932c ["INT_ADD", "register:40f0:8", ["const:54932c:8", "const:4:8"]]
+ 0054932c ["CALL", null, ["callee:00c57e90:8"]]
- 005492ec bytes e9391c94
+ 0054932c bytes d93a1c94
- 005492f4 ["COPY", "tmp:0:8", ["const:510:8"]]
- 005492f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005492f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005492f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00549334 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00549334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00549334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00549334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005492f4 bytes 08411491
+ 00549334 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d9a7d981b27c35ff492d5d8bc2aeeec"></a>

### [`00549304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549304.md) → [`00549344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549344.md) FUN_00549344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00549348",
      "incomplete_value": true,
      "site": "0054934c",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00549308",
      "incomplete_value": true,
      "site": "0054930c",
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
            "const:510:8"
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
      "0054934c",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054934c",
      "DATA",
      [
        "storage",
        "00c6a910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00549308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549304.md#insn-00549308)
- 新版 [`00549348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549344.md#insn-00549348)

~~~diff
- 00549308 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00549308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00549308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00549308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00549348 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00549348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00549348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00549348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00549308 bytes 08411491
+ 00549348 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822ac5bd11e8643222cc186b830f984a"></a>

### [`00549848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) → [`00549888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md) FUN_00549888

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md) [`00549a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) [`00549b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549b90.md) [`00549d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md)
- 新版 呼出元 1件 [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0054063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054063c.md) [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) [`00549bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549bd0.md) [`00549dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dbc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005499a8",
      "incomplete_value": true,
      "site": "005499a8",
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
      "definition_site": "00549968",
      "incomplete_value": true,
      "site": "00549968",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005499a4",
      "incomplete_value": true,
      "site": "005499bc",
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
      "definition_site": "00549964",
      "incomplete_value": true,
      "site": "0054997c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054995c",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      "00549978",
      "DATA",
      [
        "storage",
        "00c69680",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00549998",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054995c",
      "READ",
      [
        "storage",
        "00c9b160",
        null,
        "pointer"
      ]
    ],
    [
      "00549978",
      "DATA",
      [
        "storage",
        "00c69a80",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00549998",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00549900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md#insn-00549900) · [`00549914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md#insn-00549914) · [`0054991c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md#insn-0054991c)
- 新版 [`00549940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md#insn-00549940) · [`00549954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md#insn-00549954) · [`0054995c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md#insn-0054995c)

~~~diff
- 00549900 ["INT_ADD", "register:40f0:8", ["const:549900:8", "const:4:8"]]
- 00549900 ["CALL", null, ["callee:00c57e90:8"]]
+ 00549940 ["INT_ADD", "register:40f0:8", ["const:549940:8", "const:4:8"]]
+ 00549940 ["CALL", null, ["callee:00c57e90:8"]]
- 00549900 bytes 64381c94
+ 00549940 bytes 54391c94
- 00549914 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00549954 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00549914 bytes 893a00b0
+ 00549954 bytes 893a00d0
- 0054991c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d60:8"]]
- 0054991c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054995c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:160:8"]]
+ 0054995c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0054991c bytes 29b146f9
+ 0054995c bytes 29b140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a24e4353ff4c8ab945b009b55596b4b"></a>

### [`00549a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) → [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) FUN_00549a8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) [`00549848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) [`00549b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549b90.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00536674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536674.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md)
- 新版 呼出元 3件 [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) [`00549888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md) [`00549bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549bd0.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`005366b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005366b4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00549ac0",
      "incomplete_value": true,
      "site": "00549ac0",
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
      "definition_site": "00549a80",
      "incomplete_value": true,
      "site": "00549a80",
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
      "00549ab0",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "00549ac0",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00549ab0",
      "READ",
      [
        "storage",
        "00c9b168",
        null,
        "pointer"
      ]
    ],
    [
      "00549ac0",
      "DATA",
      [
        "storage",
        "00c67818",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00549a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md#insn-00549a64) · [`00549a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md#insn-00549a70) · [`00549a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md#insn-00549a74)
- 新版 [`00549aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md#insn-00549aa4) · [`00549ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md#insn-00549ab0)

~~~diff
- 00549a64 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00549aa4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00549a64 bytes 883a00b0
+ 00549aa4 bytes 883a00d0
- 00549a70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d68:8"]]
- 00549a70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00549ab0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:168:8"]]
+ 00549ab0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00549a70 bytes 08b546f9
+ 00549ab0 bytes 08b540f9
- 00549a74 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00549a74 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dea573ba5a67da04e48a369dee0b916"></a>

### [`00549d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md) → [`00549dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dbc.md) FUN_00549dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00549848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00549888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00549dc8",
      "incomplete_value": false,
      "site": "00549dcc",
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
      "definition_site": "00549d88",
      "incomplete_value": false,
      "site": "00549d8c",
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
      "00549dc8",
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
      "00549dc8",
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

- 旧版 [`00549d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md#insn-00549d8c) · [`00549d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d7c.md#insn-00549d88)
- 新版 [`00549dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dbc.md#insn-00549dcc) · [`00549dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549dbc.md#insn-00549dc8)

~~~diff
- 00549d8c ["INT_ADD", "register:40f0:8", ["const:549d8c:8", "const:4:8"]]
- 00549d8c ["CALL", null, ["callee:0043b778:8"]]
+ 00549dcc ["INT_ADD", "register:40f0:8", ["const:549dcc:8", "const:4:8"]]
+ 00549dcc ["CALL", null, ["callee:0043b778:8"]]
- 00549d8c bytes 6bc6fb97
+ 00549dcc bytes 6bc6fb97
- 00549d88 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00549d88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00549d88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00549d88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00549dc8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00549dc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00549dc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00549dc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00549d88 bytes 00303c91
+ 00549dc8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70e7d1625063c3d945ea0f1d01e35d49"></a>

### [`0054b02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md) → [`0054b06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md) FUN_0054b06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00508acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00508b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508b0c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b0bc",
      "incomplete_value": true,
      "site": "0054b0bc",
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
      "definition_site": "0054b07c",
      "incomplete_value": true,
      "site": "0054b07c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054b0a4",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054b0bc",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054b0a4",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0054b0bc",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054b048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md#insn-0054b048) · [`0054b064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md#insn-0054b064) · [`0054b138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b02c.md#insn-0054b138)
- 新版 [`0054b088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md#insn-0054b088) · [`0054b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md#insn-0054b0a4) · [`0054b178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b06c.md#insn-0054b178)

~~~diff
- 0054b048 ["INT_ADD", "register:40f0:8", ["const:54b048:8", "const:4:8"]]
- 0054b048 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054b088 ["INT_ADD", "register:40f0:8", ["const:54b088:8", "const:4:8"]]
+ 0054b088 ["CALL", null, ["callee:00c57e90:8"]]
- 0054b048 bytes 92321c94
+ 0054b088 bytes 82331c94
- 0054b064 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 0054b064 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054b0a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 0054b0a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0054b064 bytes 29a144f9
+ 0054b0a4 bytes 29a146f9
- 0054b138 ["INT_ADD", "register:40f0:8", ["const:54b138:8", "const:4:8"]]
- 0054b138 ["CALL", null, ["callee:0043bba4:8"]]
+ 0054b178 ["INT_ADD", "register:40f0:8", ["const:54b178:8", "const:4:8"]]
+ 0054b178 ["CALL", null, ["callee:0043bba4:8"]]
- 0054b138 bytes 8bc2fb97
+ 0054b178 bytes 8bc2fb97
~~~


<a id="compare-ebb12c69cd1fa4873fff0a355b49b528"></a>

### [`0054b790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md) → [`0054b7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md) FUN_0054b7d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) · 呼出先 6件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0054b868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b868.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005154b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md) · 呼出先 6件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0054b8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b8a8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b814",
      "incomplete_value": true,
      "site": "0054b820",
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
      "definition_site": "0054b7d4",
      "incomplete_value": true,
      "site": "0054b7e0",
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
      "0054b804",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054b820",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054b804",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0054b820",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054b7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md#insn-0054b7b4) · [`0054b7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md#insn-0054b7c4) · [`0054b7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b790.md#insn-0054b7f4)
- 新版 [`0054b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md#insn-0054b7f4) · [`0054b804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md#insn-0054b804) · [`0054b834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b7d0.md#insn-0054b834)

~~~diff
- 0054b7b4 ["INT_ADD", "register:40f0:8", ["const:54b7b4:8", "const:4:8"]]
- 0054b7b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054b7f4 ["INT_ADD", "register:40f0:8", ["const:54b7f4:8", "const:4:8"]]
+ 0054b7f4 ["CALL", null, ["callee:00c57e90:8"]]
- 0054b7b4 bytes b7301c94
+ 0054b7f4 bytes a7311c94
- 0054b7c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 0054b7c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054b804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 0054b804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0054b7c4 bytes 08a144f9
+ 0054b804 bytes 08a146f9
- 0054b7f4 ["INT_ADD", "register:40f0:8", ["const:54b7f4:8", "const:4:8"]]
- 0054b7f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054b834 ["INT_ADD", "register:40f0:8", ["const:54b834:8", "const:4:8"]]
+ 0054b834 ["CALL", null, ["callee:00c57e90:8"]]
- 0054b7f4 bytes a7301c94
+ 0054b834 bytes 97311c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1419129ba7b7ff61222a4417a6a39a96"></a>

### [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) → [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) FUN_0054b944

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) [`00519dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519dc0.md) [`0051c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`0054bb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 6件 [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) [`00519e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519e00.md) [`0051c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`0054bb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bb8c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054b9fc",
      "incomplete_value": true,
      "site": "0054ba04",
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
      "definition_site": "0054b9bc",
      "incomplete_value": true,
      "site": "0054b9c4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054b9ec",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054ba04",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0054ba60",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054b9ec",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0054ba04",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0054ba60",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md#insn-0054b990) · [`0054b9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md#insn-0054b9ac) · [`0054b9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md#insn-0054b9e4)
- 新版 [`0054b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md#insn-0054b9d0) · [`0054b9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md#insn-0054b9ec) · [`0054ba24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md#insn-0054ba24)

~~~diff
- 0054b990 ["INT_ADD", "register:40f0:8", ["const:54b990:8", "const:4:8"]]
- 0054b990 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054b9d0 ["INT_ADD", "register:40f0:8", ["const:54b9d0:8", "const:4:8"]]
+ 0054b9d0 ["CALL", null, ["callee:00c57e90:8"]]
- 0054b990 bytes 40301c94
+ 0054b9d0 bytes 30311c94
- 0054b9ac ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:940:8"]]
- 0054b9ac ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054b9ec ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d40:8"]]
+ 0054b9ec ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0054b9ac bytes 39a344f9
+ 0054b9ec bytes 39a346f9
- 0054b9e4 ["INT_ADD", "register:40f0:8", ["const:54b9e4:8", "const:4:8"]]
- 0054b9e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054ba24 ["INT_ADD", "register:40f0:8", ["const:54ba24:8", "const:4:8"]]
+ 0054ba24 ["CALL", null, ["callee:00c57e90:8"]]
- 0054b9e4 bytes 2b301c94
+ 0054ba24 bytes 1b311c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3fd50e178d85e5a657a39cc322d3f0b"></a>

### [`0054c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md) → [`0054c224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c224.md) FUN_0054c224

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054c0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0054c0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054c230",
      "incomplete_value": false,
      "site": "0054c234",
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
      "definition_site": "0054c1f0",
      "incomplete_value": false,
      "site": "0054c1f4",
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
      "0054c230",
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
      "0054c230",
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

- 旧版 [`0054c1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md#insn-0054c1f4) · [`0054c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md#insn-0054c1f0)
- 新版 [`0054c234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c224.md#insn-0054c234) · [`0054c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c224.md#insn-0054c230)

~~~diff
- 0054c1f4 ["INT_ADD", "register:40f0:8", ["const:54c1f4:8", "const:4:8"]]
- 0054c1f4 ["CALL", null, ["callee:0043b778:8"]]
+ 0054c234 ["INT_ADD", "register:40f0:8", ["const:54c234:8", "const:4:8"]]
+ 0054c234 ["CALL", null, ["callee:0043b778:8"]]
- 0054c1f4 bytes 51bdfb97
+ 0054c234 bytes 51bdfb97
- 0054c1f0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054c1f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054c1f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054c1f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054c230 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054c230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054c230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054c230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054c1f0 bytes 00303c91
+ 0054c230 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a07a88904f22ea5817e07c9f603a991"></a>

### [`0054c6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md) → [`0054c730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c730.md) FUN_0054c730

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054c524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c524.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0054c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c564.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054c76c",
      "incomplete_value": true,
      "site": "0054c770",
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
      "definition_site": "0054c72c",
      "incomplete_value": true,
      "site": "0054c730",
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
      "0054c75c",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054c770",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054c75c",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0054c770",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054c71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md#insn-0054c71c) · [`0054c744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md#insn-0054c744) · [`0054c75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c6f0.md#insn-0054c75c)
- 新版 [`0054c75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c730.md#insn-0054c75c) · [`0054c784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c730.md#insn-0054c784) · [`0054c79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c730.md#insn-0054c79c)

~~~diff
- 0054c71c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 0054c71c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054c75c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 0054c75c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0054c71c bytes 08a144f9
+ 0054c75c bytes 08a146f9
- 0054c744 ["INT_ADD", "register:40f0:8", ["const:54c744:8", "const:4:8"]]
- 0054c744 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054c784 ["INT_ADD", "register:40f0:8", ["const:54c784:8", "const:4:8"]]
+ 0054c784 ["CALL", null, ["callee:00c57e90:8"]]
- 0054c744 bytes d32c1c94
+ 0054c784 bytes c32d1c94
- 0054c75c ["INT_ADD", "register:40f0:8", ["const:54c75c:8", "const:4:8"]]
- 0054c75c ["CALL", null, ["callee:00c58000:8"]]
+ 0054c79c ["INT_ADD", "register:40f0:8", ["const:54c79c:8", "const:4:8"]]
+ 0054c79c ["CALL", null, ["callee:00c58000:8"]]
- 0054c75c bytes 292d1c94
+ 0054c79c bytes 192e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3972c3c96183252493f98a424666fb37"></a>

### [`0054c83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md) → [`0054c87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c87c.md) FUN_0054c87c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0051a73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a73c.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0051a77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a77c.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0053d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d7f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054c954",
      "incomplete_value": true,
      "site": "0054c954",
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
      "definition_site": "0054c914",
      "incomplete_value": true,
      "site": "0054c914",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054c954",
      "incomplete_value": true,
      "site": "0054c954",
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
      "definition_site": "0054c914",
      "incomplete_value": true,
      "site": "0054c914",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054c93c",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "0054c940",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0054c954",
      "DATA",
      [
        "storage",
        "00c67d18",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054c93c",
      "READ",
      [
        "storage",
        "00c9b150",
        null,
        "pointer"
      ]
    ],
    [
      "0054c940",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "0054c954",
      "DATA",
      [
        "storage",
        "00c68118",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054c8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md#insn-0054c8e0) · [`0054c8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md#insn-0054c8f0) · [`0054c8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md#insn-0054c8f4)
- 新版 [`0054c920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c87c.md#insn-0054c920) · [`0054c930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c87c.md#insn-0054c930) · [`0054c934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c87c.md#insn-0054c934)

~~~diff
- 0054c8e0 ["INT_ADD", "register:40f0:8", ["const:54c8e0:8", "const:4:8"]]
- 0054c8e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0054c920 ["INT_ADD", "register:40f0:8", ["const:54c920:8", "const:4:8"]]
+ 0054c920 ["CALL", null, ["callee:00c57e90:8"]]
- 0054c8e0 bytes 6c2c1c94
+ 0054c920 bytes 5c2d1c94
- 0054c8f0 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 0054c930 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 0054c8f0 bytes 793a00d0
+ 0054c930 bytes 793a00f0
- 0054c8f4 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 0054c934 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 0054c8f4 bytes 7a3a00d0
+ 0054c934 bytes 7a3a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f77c1edc6064b5e5296893a8618d1738"></a>

### [`0054cb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md) → [`0054cb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb9c.md) FUN_0054cb9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0051b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`0051b11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md) [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) [`005283a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0054cba8",
      "incomplete_value": true,
      "site": "0054cbac",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054cb68",
      "incomplete_value": true,
      "site": "0054cb6c",
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
      "0054cba8",
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
      "0054cba8",
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

- 旧版 [`0054cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md#insn-0054cb6c) · [`0054cb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md#insn-0054cb68)
- 新版 [`0054cbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb9c.md#insn-0054cbac) · [`0054cba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb9c.md#insn-0054cba8)

~~~diff
- 0054cb6c ["INT_ADD", "register:40f0:8", ["const:54cb6c:8", "const:4:8"]]
- 0054cb6c ["CALL", null, ["callee:00442930:8"]]
+ 0054cbac ["INT_ADD", "register:40f0:8", ["const:54cbac:8", "const:4:8"]]
+ 0054cbac ["CALL", null, ["callee:00442930:8"]]
- 0054cb6c bytes 61d7fb97
+ 0054cbac bytes 61d7fb97
- 0054cb68 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054cb68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054cb68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054cb68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054cba8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054cba8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cba8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cba8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054cb68 bytes 00303c91
+ 0054cba8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91975d334b0aae9b07b1bbe5046319b3"></a>

### [`0054cbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md) → [`0054cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc20.md) FUN_0054cc20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0051baa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md) [`0051c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`0051bae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md) [`0051c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054cc2c",
      "incomplete_value": true,
      "site": "0054cc30",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054cbec",
      "incomplete_value": true,
      "site": "0054cbf0",
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
      "0054cc2c",
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
      "0054cc2c",
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

- 旧版 [`0054cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md#insn-0054cbf0) · [`0054cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md#insn-0054cbec)
- 新版 [`0054cc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc20.md#insn-0054cc30) · [`0054cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc20.md#insn-0054cc2c)

~~~diff
- 0054cbf0 ["INT_ADD", "register:40f0:8", ["const:54cbf0:8", "const:4:8"]]
- 0054cbf0 ["CALL", null, ["callee:0043b778:8"]]
+ 0054cc30 ["INT_ADD", "register:40f0:8", ["const:54cc30:8", "const:4:8"]]
+ 0054cc30 ["CALL", null, ["callee:0043b778:8"]]
- 0054cbf0 bytes d2bafb97
+ 0054cc30 bytes d2bafb97
- 0054cbec ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054cbec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054cbec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054cbec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054cc2c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054cc2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cc2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cc2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054cbec bytes 00303c91
+ 0054cc2c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efdf1e7f9210eb3085b078497f15a4ab"></a>

### [`0054d0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md) → [`0054d13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d13c.md) FUN_0054d13c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`0053fc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc60.md)
- 新版 呼出元 1件 [`0051e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c940.md) [`0053fca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053fca0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054d1e8",
      "incomplete_value": true,
      "site": "0054d1e8",
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
      "definition_site": "0054d1a8",
      "incomplete_value": true,
      "site": "0054d1a8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054d1d4",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "0054d1e8",
      "DATA",
      [
        "storage",
        "00c68a28",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0054d1d4",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "0054d1e8",
      "DATA",
      [
        "storage",
        "00c68e28",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md#insn-0054d17c) · [`0054d18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md#insn-0054d18c) · [`0054d194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md#insn-0054d194)
- 新版 [`0054d1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d13c.md#insn-0054d1bc) · [`0054d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d13c.md#insn-0054d1cc) · [`0054d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d13c.md#insn-0054d1d4)

~~~diff
- 0054d17c ["INT_ADD", "register:40f0:8", ["const:54d17c:8", "const:4:8"]]
- 0054d17c ["CALL", null, ["callee:00c57e90:8"]]
+ 0054d1bc ["INT_ADD", "register:40f0:8", ["const:54d1bc:8", "const:4:8"]]
+ 0054d1bc ["CALL", null, ["callee:00c57e90:8"]]
- 0054d17c bytes 452a1c94
+ 0054d1bc bytes 352b1c94
- 0054d18c ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0054d1cc ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0054d18c bytes 6a3a00b0
+ 0054d1cc bytes 6a3a00d0
- 0054d194 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:de8:8"]]
- 0054d194 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054d1d4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1e8:8"]]
+ 0054d1d4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0054d194 bytes 4af546f9
+ 0054d1d4 bytes 4af540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1920b054bb7622e28377f3aa0098fe51"></a>

### [`0054d9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md) → [`0054da18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da18.md) FUN_0054da18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0054da24",
      "incomplete_value": false,
      "site": "0054da28",
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
      "definition_site": "0054d9e4",
      "incomplete_value": false,
      "site": "0054d9e8",
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
      "0054da24",
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
      "0054da24",
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

- 旧版 [`0054d9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md#insn-0054d9e8) · [`0054d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md#insn-0054d9e4)
- 新版 [`0054da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da18.md#insn-0054da28) · [`0054da24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054da18.md#insn-0054da24)

~~~diff
- 0054d9e8 ["INT_ADD", "register:40f0:8", ["const:54d9e8:8", "const:4:8"]]
- 0054d9e8 ["CALL", null, ["callee:00442930:8"]]
+ 0054da28 ["INT_ADD", "register:40f0:8", ["const:54da28:8", "const:4:8"]]
+ 0054da28 ["CALL", null, ["callee:00442930:8"]]
- 0054d9e8 bytes c2d3fb97
+ 0054da28 bytes c2d3fb97
- 0054d9e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054d9e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054d9e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054d9e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054da24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054da24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054da24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054da24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054d9e4 bytes 00303c91
+ 0054da24 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137e4eecfa2888d2f6c9aa8214d51dc3"></a>

### [`0054db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md) → [`0054db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054db94.md) FUN_0054db94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0054e740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e740.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054dba0",
      "incomplete_value": false,
      "site": "0054dba4",
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
      "definition_site": "0054db60",
      "incomplete_value": false,
      "site": "0054db64",
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
      "0054dba0",
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
      "0054dba0",
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

- 旧版 [`0054db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md#insn-0054db64) · [`0054db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md#insn-0054db60)
- 新版 [`0054dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054db94.md#insn-0054dba4) · [`0054dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054db94.md#insn-0054dba0)

~~~diff
- 0054db64 ["INT_ADD", "register:40f0:8", ["const:54db64:8", "const:4:8"]]
- 0054db64 ["CALL", null, ["callee:0043b778:8"]]
+ 0054dba4 ["INT_ADD", "register:40f0:8", ["const:54dba4:8", "const:4:8"]]
+ 0054dba4 ["CALL", null, ["callee:0043b778:8"]]
- 0054db64 bytes f5b6fb97
+ 0054dba4 bytes f5b6fb97
- 0054db60 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054db60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054db60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054db60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054dba0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054dba0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dba0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dba0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054db60 bytes 00303c91
+ 0054dba0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291586f024aadf3403ca41c25c540cd0"></a>

### [`0054dd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md) → [`0054dd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd54.md) FUN_0054dd54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054dd60",
      "incomplete_value": false,
      "site": "0054dd64",
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
      "definition_site": "0054dd20",
      "incomplete_value": false,
      "site": "0054dd24",
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
      "0054dd60",
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
      "0054dd60",
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

- 旧版 [`0054dd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md#insn-0054dd24) · [`0054dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md#insn-0054dd20)
- 新版 [`0054dd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd54.md#insn-0054dd64) · [`0054dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd54.md#insn-0054dd60)

~~~diff
- 0054dd24 ["INT_ADD", "register:40f0:8", ["const:54dd24:8", "const:4:8"]]
- 0054dd24 ["CALL", null, ["callee:0043b778:8"]]
+ 0054dd64 ["INT_ADD", "register:40f0:8", ["const:54dd64:8", "const:4:8"]]
+ 0054dd64 ["CALL", null, ["callee:0043b778:8"]]
- 0054dd24 bytes 85b6fb97
+ 0054dd64 bytes 85b6fb97
- 0054dd20 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054dd20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054dd20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054dd20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054dd60 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054dd60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dd60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dd60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054dd20 bytes 00303c91
+ 0054dd60 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8670fbdd40694e3cc4267a448a945923"></a>

### [`0054e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md) → [`0054e220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e220.md) FUN_0054e220

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0054dd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054dd68.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054e22c",
      "incomplete_value": false,
      "site": "0054e230",
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
      "definition_site": "0054e1ec",
      "incomplete_value": false,
      "site": "0054e1f0",
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
      "0054e22c",
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
      "0054e22c",
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

- 旧版 [`0054e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md#insn-0054e1f0) · [`0054e1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md#insn-0054e1ec)
- 新版 [`0054e230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e220.md#insn-0054e230) · [`0054e22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054e220.md#insn-0054e22c)

~~~diff
- 0054e1f0 ["INT_ADD", "register:40f0:8", ["const:54e1f0:8", "const:4:8"]]
- 0054e1f0 ["CALL", null, ["callee:0043b778:8"]]
+ 0054e230 ["INT_ADD", "register:40f0:8", ["const:54e230:8", "const:4:8"]]
+ 0054e230 ["CALL", null, ["callee:0043b778:8"]]
- 0054e1f0 bytes 52b5fb97
+ 0054e230 bytes 52b5fb97
- 0054e1ec ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054e1ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054e1ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054e1ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054e22c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054e22c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e22c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e22c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054e1ec bytes 00303c91
+ 0054e22c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af7ee976ed5450a7ea022077e26c9c0"></a>

### [`0054eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md) → [`0054eefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eefc.md) FUN_0054eefc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0054ed04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054ed04.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0054ef08",
      "incomplete_value": false,
      "site": "0054ef0c",
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
      "definition_site": "0054eec8",
      "incomplete_value": false,
      "site": "0054eecc",
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
      "0054ef08",
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
      "0054ef08",
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

- 旧版 [`0054eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md#insn-0054eecc) · [`0054eec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md#insn-0054eec8)
- 新版 [`0054ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eefc.md#insn-0054ef0c) · [`0054ef08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054e/0054eefc.md#insn-0054ef08)

~~~diff
- 0054eecc ["INT_ADD", "register:40f0:8", ["const:54eecc:8", "const:4:8"]]
- 0054eecc ["CALL", null, ["callee:0043b778:8"]]
+ 0054ef0c ["INT_ADD", "register:40f0:8", ["const:54ef0c:8", "const:4:8"]]
+ 0054ef0c ["CALL", null, ["callee:0043b778:8"]]
- 0054eecc bytes 1bb2fb97
+ 0054ef0c bytes 1bb2fb97
- 0054eec8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0054eec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054eec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054eec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054ef08 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0054ef08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054ef08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054ef08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054eec8 bytes 00303c91
+ 0054ef08 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c6cb0bc6cfc8e9a451d209b1975b68"></a>

### [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) → [`0054f430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md) _INIT_25

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) [`004e75fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e75fc.md) [`00515474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) [`00515590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515590.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004e7494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7494.md) [`004e763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e763c.md) [`005154b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005154b4.md) [`005155d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005155d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054f754",
      "incomplete_value": false,
      "site": "0054f768",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f714",
      "incomplete_value": false,
      "site": "0054f728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa44",
      "incomplete_value": false,
      "site": "0054fa58",
      "value": [
        "leaf",
        "const:4e763c:8"
      ]
    },
    "old": {
      "definition_site": "0054fa04",
      "incomplete_value": false,
      "site": "0054fa18",
      "value": [
        "leaf",
        "const:4e75fc:8"
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa4c",
      "incomplete_value": false,
      "site": "0054fa58",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fa0c",
      "incomplete_value": false,
      "site": "0054fa18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "0054f4bc",
      "DATA",
      [
        "storage",
        "00415344",
        null,
        "dword"
      ]
    ],
    [
      "0054f738",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      "0054f754",
      "PARAM",
      [
        "storage",
        "00ca4e68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054f4bc",
      "DATA",
      [
        "storage",
        "00415344",
        "fde_00415344",
        "dword"
      ]
    ],
    [
      "0054f738",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "dword"
      ]
    ],
    [
      "0054f754",
      "PARAM",
      [
        "storage",
        "00ca5268",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054f728) · [`0054fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054fa18) · [`0054feb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054feb8)
- 新版 [`0054f768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md#insn-0054f768) · [`0054fa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md#insn-0054fa58) · [`0054fef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054f/0054f430.md#insn-0054fef8)

~~~diff
- 0054f728 ["INT_ADD", "register:40f0:8", ["const:54f728:8", "const:4:8"]]
- 0054f728 ["CALL", null, ["callee:004e7494:8"]]
+ 0054f768 ["INT_ADD", "register:40f0:8", ["const:54f768:8", "const:4:8"]]
+ 0054f768 ["CALL", null, ["callee:004e7494:8"]]
- 0054f728 bytes 4b5ffe97
+ 0054f768 bytes 4b5ffe97
- 0054fa18 ["INT_ADD", "register:40f0:8", ["const:54fa18:8", "const:4:8"]]
- 0054fa18 ["CALL", null, ["callee:00c57e30:8"]]
+ 0054fa58 ["INT_ADD", "register:40f0:8", ["const:54fa58:8", "const:4:8"]]
+ 0054fa58 ["CALL", null, ["callee:00c57e30:8"]]
- 0054fa18 bytes 06201c94
+ 0054fa58 bytes f6201c94
- 0054feb8 ["INT_ADD", "register:40f0:8", ["const:54feb8:8", "const:4:8"]]
- 0054feb8 ["CALL", null, ["callee:005154b4:8"]]
+ 0054fef8 ["INT_ADD", "register:40f0:8", ["const:54fef8:8", "const:4:8"]]
+ 0054fef8 ["CALL", null, ["callee:005154b4:8"]]
- 0054feb8 bytes 6f15ff97
+ 0054fef8 bytes 6f15ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beac8033de0cf209128825fe255d015e"></a>

### [`0055098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) → [`005509cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509cc.md) FUN_005509cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00727120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md) [`00727560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727560.md) · 呼出先 1件 [`00576400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md)
- 新版 呼出元 2件 [`00727160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727160.md) [`007275a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275a0.md) · 呼出先 1件 [`00576440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576440.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509e8",
      "incomplete_value": true,
      "site": "005509e8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509a8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509e8",
      "incomplete_value": true,
      "site": "005509ec",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509ac",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005509e4",
      "READ",
      [
        "storage",
        "002c3c48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005509e4",
      "READ",
      [
        "storage",
        "002c3c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005509a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md#insn-005509a4)
- 新版 [`005509e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509cc.md#insn-005509e4)

~~~diff
- 005509a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
- 005509a4 ["LOAD", "register:5060:8", ["const:1b1:8", "tmp:0:8"]]
- 005509a4 ["COPY", "register:5068:8", ["const:0:8"]]
- 005509a4 ["COPY", "register:5070:8", ["const:0:8"]]
+ 005509e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c88:8"]]
+ 005509e4 ["LOAD", "register:5060:8", ["const:1b1:8", "tmp:0:8"]]
+ 005509e4 ["COPY", "register:5068:8", ["const:0:8"]]
+ 005509e4 ["COPY", "register:5070:8", ["const:0:8"]]
- 005509a4 bytes 032546fd
+ 005509e4 bytes 034546fd
~~~


<a id="compare-d98d63efda2a383758c053f51b9a0b6f"></a>

### [`005509ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509ec.md) → [`00550a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a2c.md) FUN_00550a2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00550a44",
      "incomplete_value": true,
      "site": "00550a48",
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
      "definition_site": "00550a04",
      "incomplete_value": true,
      "site": "00550a08",
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
      "00550a40",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00550a48",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00550a40",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00550a48",
      "DATA",
      [
        "storage",
        "00c6ab40",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005509f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509ec.md#insn-005509f8) · [`00550a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509ec.md#insn-00550a00) · [`00550a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509ec.md#insn-00550a0c)
- 新版 [`00550a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a2c.md#insn-00550a38) · [`00550a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a2c.md#insn-00550a40) · [`00550a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a2c.md#insn-00550a4c)

~~~diff
- 005509f8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00550a38 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005509f8 bytes 483a00d0
+ 00550a38 bytes 483a00f0
- 00550a00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
- 00550a00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00550a40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00550a40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00550a00 bytes 081547f9
+ 00550a40 bytes 081541f9
- 00550a0c ["INT_ADD", "register:40f0:8", ["const:550a0c:8", "const:4:8"]]
- 00550a0c ["CALL", null, ["callee:00c57ea0:8"]]
+ 00550a4c ["INT_ADD", "register:40f0:8", ["const:550a4c:8", "const:4:8"]]
+ 00550a4c ["CALL", null, ["callee:00c57ea0:8"]]
- 00550a0c bytes 251c1c94
+ 00550a4c bytes 151d1c94
~~~


<a id="compare-2e35e37f585f358d7255b178d6cdf039"></a>

### [`00550a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md) → [`00550a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a6c.md) FUN_00550a6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a20.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00550a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a60.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00550b10",
      "incomplete_value": true,
      "site": "00550b14",
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
      "definition_site": "00550ad0",
      "incomplete_value": true,
      "site": "00550ad4",
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
      "definition_site": "00550aec",
      "incomplete_value": true,
      "site": "00550af4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00550aac",
      "incomplete_value": true,
      "site": "00550ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00550ae8",
      "incomplete_value": false,
      "site": "00550af4",
      "value": [
        "leaf",
        "const:45a6c8:8"
      ]
    },
    "old": {
      "definition_site": "00550aa8",
      "incomplete_value": false,
      "site": "00550ab4",
      "value": [
        "leaf",
        "const:45a688:8"
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
      "00550ae8",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "00550aec",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ],
    [
      "00550aec",
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
      "00550ae8",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "00550aec",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "00550aec",
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

- 旧版 [`00550a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550a94) · [`00550ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550ab4) · [`00550a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550a6c)
- 新版 [`00550ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a6c.md#insn-00550ad4) · [`00550af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a6c.md#insn-00550af4) · [`00550aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a6c.md#insn-00550aac)

~~~diff
- 00550a94 ["INT_ADD", "register:40f0:8", ["const:550a94:8", "const:4:8"]]
- 00550a94 ["CALL", null, ["callee:00c58320:8"]]
+ 00550ad4 ["INT_ADD", "register:40f0:8", ["const:550ad4:8", "const:4:8"]]
+ 00550ad4 ["CALL", null, ["callee:00c58320:8"]]
- 00550a94 bytes 231d1c94
+ 00550ad4 bytes 131e1c94
- 00550ab4 ["INT_ADD", "register:40f0:8", ["const:550ab4:8", "const:4:8"]]
- 00550ab4 ["CALL", null, ["callee:00c58330:8"]]
+ 00550af4 ["INT_ADD", "register:40f0:8", ["const:550af4:8", "const:4:8"]]
+ 00550af4 ["CALL", null, ["callee:00c58330:8"]]
- 00550ab4 bytes 1f1d1c94
+ 00550af4 bytes 0f1e1c94
- 00550a6c ["INT_ADD", "register:40f0:8", ["const:550a6c:8", "const:4:8"]]
- 00550a6c ["CALL", null, ["callee:00c582f0:8"]]
+ 00550aac ["INT_ADD", "register:40f0:8", ["const:550aac:8", "const:4:8"]]
+ 00550aac ["CALL", null, ["callee:00c582f0:8"]]
- 00550a6c bytes 211d1c94
+ 00550aac bytes 111e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a8e4a0dc0e28a0a4fc70ef6ed11ce9"></a>

### [`00550ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md) → [`00550f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550f34.md) FUN_00550f34

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) · 呼出先 5件 [`0055e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e500.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005550b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md) · 呼出先 5件 [`0055e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e540.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00550f78",
      "incomplete_value": false,
      "site": "00550f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00550f38",
      "incomplete_value": false,
      "site": "00550f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "00550f7c",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f98",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ],
    [
      "00550fb4",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00550f7c",
      "DATA",
      [
        "storage",
        "00c6abe0",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f98",
      "DATA",
      [
        "storage",
        "00c6ac48",
        null,
        "undefined *"
      ]
    ],
    [
      "00550fb4",
      "READ",
      [
        "storage",
        "00c9b240",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00550f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f2c) · [`00550f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f38) · [`00550f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f50)
- 新版 [`00550f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550f34.md#insn-00550f6c) · [`00550f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550f34.md#insn-00550f78) · [`00550f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550f34.md#insn-00550f90)

~~~diff
- 00550f2c ["INT_ADD", "register:40f0:8", ["const:550f2c:8", "const:4:8"]]
- 00550f2c ["CALL", null, ["callee:0055e540:8"]]
+ 00550f6c ["INT_ADD", "register:40f0:8", ["const:550f6c:8", "const:4:8"]]
+ 00550f6c ["CALL", null, ["callee:0055e540:8"]]
- 00550f2c bytes 75350094
+ 00550f6c bytes 75350094
- 00550f38 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00550f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00550f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00550f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00550f78 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00550f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00550f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00550f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00550f38 bytes 08811f91
+ 00550f78 bytes 08812f91
- 00550f50 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 00550f90 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 00550f50 bytes 593a00d0
+ 00550f90 bytes 593a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66813b26fc97911c0a3c7490c2aea4b4"></a>

### [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) → [`00551274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md) FUN_00551274

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) · 呼出先 6件 [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`008aac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008aa/008aac28.md) [`008abcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008abcf8.md) [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) · 呼出先 6件 [`00551ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md) [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005512cc",
      "incomplete_value": true,
      "site": "005512d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055128c",
      "incomplete_value": true,
      "site": "00551294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
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
      "definition_site": "005512c8",
      "incomplete_value": true,
      "site": "005512d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a3:8"
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
      "definition_site": "005512c8",
      "incomplete_value": true,
      "site": "005512d8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
      "value": [
        "LOAD",
        "16",
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
      "005512c8",
      "READ",
      [
        "storage",
        "002a31a3",
        null,
        "string"
      ]
    ],
    [
      "005512c8",
      "READ",
      [
        "storage",
        "002a31b3",
        null,
        "string"
      ]
    ],
    [
      "005512cc",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005512c8",
      "READ",
      [
        "storage",
        "002a3270",
        null,
        "string"
      ]
    ],
    [
      "005512c8",
      "READ",
      [
        "storage",
        "002a3280",
        null,
        "string"
      ]
    ],
    [
      "005512cc",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005512d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-005512d8) · [`005512e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-005512e8) · [`00551278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-00551278)
- 新版 [`00551318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md#insn-00551318) · [`00551328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md#insn-00551328) · [`005512b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md#insn-005512b8)

~~~diff
- 005512d8 ["INT_ADD", "register:40f0:8", ["const:5512d8:8", "const:4:8"]]
- 005512d8 ["CALL", null, ["callee:00597ecc:8"]]
+ 00551318 ["INT_ADD", "register:40f0:8", ["const:551318:8", "const:4:8"]]
+ 00551318 ["CALL", null, ["callee:00597ecc:8"]]
- 005512d8 bytes ed1a0194
+ 00551318 bytes ed1a0194
- 005512e8 ["INT_ADD", "register:40f0:8", ["const:5512e8:8", "const:4:8"]]
- 005512e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00551328 ["INT_ADD", "register:40f0:8", ["const:551328:8", "const:4:8"]]
+ 00551328 ["CALL", null, ["callee:00c57eb0:8"]]
- 005512e8 bytes f2191c94
+ 00551328 bytes e21a1c94
- 00551278 ["INT_ADD", "register:40f0:8", ["const:551278:8", "const:4:8"]]
- 00551278 ["CALL", null, ["callee:00c57e90:8"]]
+ 005512b8 ["INT_ADD", "register:40f0:8", ["const:5512b8:8", "const:4:8"]]
+ 005512b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00551278 bytes 061a1c94
+ 005512b8 bytes f61a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dec892d8fd54a4d4e40acb8adcbceed"></a>

### [`00551d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md) → [`00551dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551dc0.md) FUN_00551dc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00551e10",
      "incomplete_value": true,
      "site": "00551e10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00551dd0",
      "incomplete_value": true,
      "site": "00551dd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00551e00",
      "incomplete_value": true,
      "site": "00551e10",
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
      "definition_site": "00551dc0",
      "incomplete_value": true,
      "site": "00551dd0",
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
      "00551df8",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00551e00",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00551df8",
      "READ",
      [
        "storage",
        "00c9b240",
        null,
        "pointer"
      ]
    ],
    [
      "00551e00",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551dd0) · [`00551da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551da4) · [`00551dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551dac)
- 新版 [`00551e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551dc0.md#insn-00551e10) · [`00551de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551dc0.md#insn-00551de4) · [`00551dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551dc0.md#insn-00551dec)

~~~diff
- 00551dd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00551dd0 ["INT_ADD", "register:40f0:8", ["const:551dd0:8", "const:4:8"]]
- 00551dd0 ["CALLIND", null, ["register:0:8"]]
+ 00551e10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00551e10 ["INT_ADD", "register:40f0:8", ["const:551e10:8", "const:4:8"]]
+ 00551e10 ["CALLIND", null, ["register:0:8"]]
- 00551dd0 bytes 20013fd6
+ 00551e10 bytes 20013fd6
- 00551da4 ["INT_ADD", "register:40f0:8", ["const:551da4:8", "const:4:8"]]
- 00551da4 ["CALL", null, ["callee:0055e624:8"]]
+ 00551de4 ["INT_ADD", "register:40f0:8", ["const:551de4:8", "const:4:8"]]
+ 00551de4 ["CALL", null, ["callee:0055e624:8"]]
- 00551da4 bytes 10320094
+ 00551de4 bytes 10320094
- 00551dac ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00551dec ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00551dac bytes 483a00b0
+ 00551dec bytes 483a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a969e8544e548562a08b1a274473000"></a>

### [`00551ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md) → [`00551f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f0c.md) FUN_00551f0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551f1c",
      "incomplete_value": true,
      "site": "00551f28",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551edc",
      "incomplete_value": true,
      "site": "00551ee8",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551f2c",
      "incomplete_value": true,
      "site": "00551f30",
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
                "const:be0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551eec",
      "incomplete_value": true,
      "site": "00551ef0",
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
                "const:7e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00551f28",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551f30",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551f28",
      "DATA",
      [
        "storage",
        "00c6abe0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551f30",
      "DATA",
      [
        "storage",
        "00c6ac48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551f28) · [`00551edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551edc) · [`00551f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551f00)
- 新版 [`00551f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f0c.md#insn-00551f68) · [`00551f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f0c.md#insn-00551f1c) · [`00551f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f0c.md#insn-00551f40)

~~~diff
- 00551f28 ["INT_ADD", "register:40f0:8", ["const:551f28:8", "const:4:8"]]
- 00551f28 ["CALL", null, ["callee:00c57e80:8"]]
+ 00551f68 ["INT_ADD", "register:40f0:8", ["const:551f68:8", "const:4:8"]]
+ 00551f68 ["CALL", null, ["callee:00c57e80:8"]]
- 00551f28 bytes d6161c94
+ 00551f68 bytes c6171c94
- 00551edc ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00551edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551f1c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00551f1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551edc bytes 08811f91
+ 00551f1c bytes 08812f91
- 00551f00 ["INT_ADD", "register:40f0:8", ["const:551f00:8", "const:4:8"]]
- 00551f00 ["CALL", null, ["callee:00c53d00:8"]]
+ 00551f40 ["INT_ADD", "register:40f0:8", ["const:551f40:8", "const:4:8"]]
+ 00551f40 ["CALL", null, ["callee:00c53d00:8"]]
- 00551f00 bytes 78061c94
+ 00551f40 bytes 70071c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e015f0dc09940532403ca14ef760b82c"></a>

### [`00551f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md) → [`00551f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f7c.md) FUN_00551f7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00551f8c",
      "incomplete_value": false,
      "site": "00551f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551f4c",
      "incomplete_value": false,
      "site": "00551f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00551f9c",
      "incomplete_value": false,
      "site": "00551fa0",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551f5c",
      "incomplete_value": false,
      "site": "00551f60",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00551f98",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551fa0",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551f98",
      "DATA",
      [
        "storage",
        "00c6abe0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551fa0",
      "DATA",
      [
        "storage",
        "00c6ac48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551f98) · [`00551fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551fa0) · [`00551f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551f4c)
- 新版 [`00551fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f7c.md#insn-00551fd8) · [`00551fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f7c.md#insn-00551fe0) · [`00551f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f7c.md#insn-00551f8c)

~~~diff
- 00551f98 ["INT_ADD", "register:40f0:8", ["const:551f98:8", "const:4:8"]]
- 00551f98 ["CALL", null, ["callee:00c57e80:8"]]
+ 00551fd8 ["INT_ADD", "register:40f0:8", ["const:551fd8:8", "const:4:8"]]
+ 00551fd8 ["CALL", null, ["callee:00c57e80:8"]]
- 00551f98 bytes ba161c94
+ 00551fd8 bytes aa171c94
- 00551fa0 ["INT_ADD", "register:40f0:8", ["const:551fa0:8", "const:4:8"]]
- 00551fa0 ["CALL", null, ["callee:0055e5ac:8"]]
+ 00551fe0 ["INT_ADD", "register:40f0:8", ["const:551fe0:8", "const:4:8"]]
+ 00551fe0 ["CALL", null, ["callee:0055e5ac:8"]]
- 00551fa0 bytes 73310094
+ 00551fe0 bytes 73310094
- 00551f4c ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00551f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551f8c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00551f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551f4c bytes 08811f91
+ 00551f8c bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39257706b0a7fd84b5d1af4c0fde778b"></a>

### [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) → [`00551ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md) FUN_00551ff4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00551274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md) [`00551ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055215c",
      "incomplete_value": false,
      "site": "00552164",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055211c",
      "incomplete_value": false,
      "site": "00552124",
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
            "const:f13:8"
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
      "definition_site": "005522bc",
      "incomplete_value": false,
      "site": "005522c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055227c",
      "incomplete_value": false,
      "site": "00552284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "definition_site": "005522d4",
      "incomplete_value": false,
      "site": "005522e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552294",
      "incomplete_value": false,
      "site": "005522a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "0055215c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00552180",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "005522bc",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055215c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00552180",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "005522bc",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-00552124) · [`00552284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-00552284) · [`005522a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-005522a0)
- 新版 [`00552164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md#insn-00552164) · [`005522c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md#insn-005522c4) · [`005522e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md#insn-005522e0)

~~~diff
- 00552124 ["INT_ADD", "register:40f0:8", ["const:552124:8", "const:4:8"]]
- 00552124 ["CALL", null, ["callee:00441e94:8"]]
+ 00552164 ["INT_ADD", "register:40f0:8", ["const:552164:8", "const:4:8"]]
+ 00552164 ["CALL", null, ["callee:00441e94:8"]]
- 00552124 bytes 4cbffb97
+ 00552164 bytes 4cbffb97
- 00552284 ["INT_ADD", "register:40f0:8", ["const:552284:8", "const:4:8"]]
- 00552284 ["CALL", null, ["callee:00441e94:8"]]
+ 005522c4 ["INT_ADD", "register:40f0:8", ["const:5522c4:8", "const:4:8"]]
+ 005522c4 ["CALL", null, ["callee:00441e94:8"]]
- 00552284 bytes f4befb97
+ 005522c4 bytes f4befb97
- 005522a0 ["INT_ADD", "register:40f0:8", ["const:5522a0:8", "const:4:8"]]
- 005522a0 ["CALL", null, ["callee:004427f4:8"]]
+ 005522e0 ["INT_ADD", "register:40f0:8", ["const:5522e0:8", "const:4:8"]]
+ 005522e0 ["CALL", null, ["callee:004427f4:8"]]
- 005522a0 bytes 45c1fb97
+ 005522e0 bytes 45c1fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd4b8a6a219ff559d9623a50fd983460"></a>

### [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) → [`00552840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md) FUN_00552840

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00551ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551ff4.md) [`00552840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005529a4",
      "incomplete_value": false,
      "site": "005529ac",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552964",
      "incomplete_value": false,
      "site": "0055296c",
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
            "const:f13:8"
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
      "definition_site": "005529c8",
      "incomplete_value": false,
      "site": "005529d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552988",
      "incomplete_value": false,
      "site": "00552994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "definition_site": "00552b04",
      "incomplete_value": false,
      "site": "00552b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552ac4",
      "incomplete_value": false,
      "site": "00552acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "005529a4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005529c8",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00552b04",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005529a4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "005529c8",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00552b04",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055296c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-0055296c) · [`00552994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-00552994) · [`00552acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-00552acc)
- 新版 [`005529ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md#insn-005529ac) · [`005529d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md#insn-005529d4) · [`00552b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md#insn-00552b0c)

~~~diff
- 0055296c ["INT_ADD", "register:40f0:8", ["const:55296c:8", "const:4:8"]]
- 0055296c ["CALL", null, ["callee:00441e94:8"]]
+ 005529ac ["INT_ADD", "register:40f0:8", ["const:5529ac:8", "const:4:8"]]
+ 005529ac ["CALL", null, ["callee:00441e94:8"]]
- 0055296c bytes 3abdfb97
+ 005529ac bytes 3abdfb97
- 00552994 ["INT_ADD", "register:40f0:8", ["const:552994:8", "const:4:8"]]
- 00552994 ["CALL", null, ["callee:004427f4:8"]]
+ 005529d4 ["INT_ADD", "register:40f0:8", ["const:5529d4:8", "const:4:8"]]
+ 005529d4 ["CALL", null, ["callee:004427f4:8"]]
- 00552994 bytes 88bffb97
+ 005529d4 bytes 88bffb97
- 00552acc ["INT_ADD", "register:40f0:8", ["const:552acc:8", "const:4:8"]]
- 00552acc ["CALL", null, ["callee:00441e94:8"]]
+ 00552b0c ["INT_ADD", "register:40f0:8", ["const:552b0c:8", "const:4:8"]]
+ 00552b0c ["CALL", null, ["callee:00441e94:8"]]
- 00552acc bytes e2bcfb97
+ 00552b0c bytes e2bcfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23bda61ca4787c43f7a7789014d7bba7"></a>

### [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) → [`00553078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md) FUN_00553078

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00552840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00552/00552840.md) [`00553078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005531d8",
      "incomplete_value": false,
      "site": "005531e0",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553198",
      "incomplete_value": false,
      "site": "005531a0",
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
            "const:f13:8"
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
      "definition_site": "005531fc",
      "incomplete_value": false,
      "site": "00553208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005531bc",
      "incomplete_value": false,
      "site": "005531c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "definition_site": "00553338",
      "incomplete_value": false,
      "site": "00553340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005532f8",
      "incomplete_value": false,
      "site": "00553300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "005531d8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005531fc",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00553338",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005531d8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "005531fc",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00553338",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005531a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-005531a0) · [`005531c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-005531c8) · [`00553300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-00553300)
- 新版 [`005531e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md#insn-005531e0) · [`00553208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md#insn-00553208) · [`00553340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md#insn-00553340)

~~~diff
- 005531a0 ["INT_ADD", "register:40f0:8", ["const:5531a0:8", "const:4:8"]]
- 005531a0 ["CALL", null, ["callee:00441e94:8"]]
+ 005531e0 ["INT_ADD", "register:40f0:8", ["const:5531e0:8", "const:4:8"]]
+ 005531e0 ["CALL", null, ["callee:00441e94:8"]]
- 005531a0 bytes 2dbbfb97
+ 005531e0 bytes 2dbbfb97
- 005531c8 ["INT_ADD", "register:40f0:8", ["const:5531c8:8", "const:4:8"]]
- 005531c8 ["CALL", null, ["callee:004427f4:8"]]
+ 00553208 ["INT_ADD", "register:40f0:8", ["const:553208:8", "const:4:8"]]
+ 00553208 ["CALL", null, ["callee:004427f4:8"]]
- 005531c8 bytes 7bbdfb97
+ 00553208 bytes 7bbdfb97
- 00553300 ["INT_ADD", "register:40f0:8", ["const:553300:8", "const:4:8"]]
- 00553300 ["CALL", null, ["callee:00441e94:8"]]
+ 00553340 ["INT_ADD", "register:40f0:8", ["const:553340:8", "const:4:8"]]
+ 00553340 ["CALL", null, ["callee:00441e94:8"]]
- 00553300 bytes d5bafb97
+ 00553340 bytes d5bafb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4163d55d87b8a66b4b7477737b0761f1"></a>

### [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) → [`005538ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md) FUN_005538ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00553078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/00553078.md) [`005538ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00553a08",
      "incomplete_value": false,
      "site": "00553a10",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005539c8",
      "incomplete_value": false,
      "site": "005539d0",
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
            "const:f13:8"
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
      "definition_site": "00553a2c",
      "incomplete_value": false,
      "site": "00553a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005539ec",
      "incomplete_value": false,
      "site": "005539f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "definition_site": "00553b68",
      "incomplete_value": false,
      "site": "00553b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553b28",
      "incomplete_value": false,
      "site": "00553b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "00553a08",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00553a2c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00553b68",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00553a08",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00553a2c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00553b68",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005539d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-005539d0) · [`005539f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-005539f8) · [`00553b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-00553b30)
- 新版 [`00553a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md#insn-00553a10) · [`00553a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md#insn-00553a38) · [`00553b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md#insn-00553b70)

~~~diff
- 005539d0 ["INT_ADD", "register:40f0:8", ["const:5539d0:8", "const:4:8"]]
- 005539d0 ["CALL", null, ["callee:00441e94:8"]]
+ 00553a10 ["INT_ADD", "register:40f0:8", ["const:553a10:8", "const:4:8"]]
+ 00553a10 ["CALL", null, ["callee:00441e94:8"]]
- 005539d0 bytes 21b9fb97
+ 00553a10 bytes 21b9fb97
- 005539f8 ["INT_ADD", "register:40f0:8", ["const:5539f8:8", "const:4:8"]]
- 005539f8 ["CALL", null, ["callee:004427f4:8"]]
+ 00553a38 ["INT_ADD", "register:40f0:8", ["const:553a38:8", "const:4:8"]]
+ 00553a38 ["CALL", null, ["callee:004427f4:8"]]
- 005539f8 bytes 6fbbfb97
+ 00553a38 bytes 6fbbfb97
- 00553b30 ["INT_ADD", "register:40f0:8", ["const:553b30:8", "const:4:8"]]
- 00553b30 ["CALL", null, ["callee:00441e94:8"]]
+ 00553b70 ["INT_ADD", "register:40f0:8", ["const:553b70:8", "const:4:8"]]
+ 00553b70 ["CALL", null, ["callee:00441e94:8"]]
- 00553b30 bytes c9b8fb97
+ 00553b70 bytes c9b8fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05827b769400549be9f643f860209357"></a>

### [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) → [`005540cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md) FUN_005540cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`005538ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00553/005538ac.md) [`005540cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

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
      "definition_site": "00554220",
      "incomplete_value": false,
      "site": "00554228",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005541e0",
      "incomplete_value": false,
      "site": "005541e8",
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
            "const:f13:8"
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
      "definition_site": "00554244",
      "incomplete_value": false,
      "site": "00554250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554204",
      "incomplete_value": false,
      "site": "00554210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "definition_site": "0055437c",
      "incomplete_value": false,
      "site": "00554384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055433c",
      "incomplete_value": false,
      "site": "00554344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "00554220",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00554244",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0055437c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00554220",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00554244",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0055437c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005541e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-005541e8) · [`00554210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-00554210) · [`00554344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-00554344)
- 新版 [`00554228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md#insn-00554228) · [`00554250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md#insn-00554250) · [`00554384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md#insn-00554384)

~~~diff
- 005541e8 ["INT_ADD", "register:40f0:8", ["const:5541e8:8", "const:4:8"]]
- 005541e8 ["CALL", null, ["callee:00441e94:8"]]
+ 00554228 ["INT_ADD", "register:40f0:8", ["const:554228:8", "const:4:8"]]
+ 00554228 ["CALL", null, ["callee:00441e94:8"]]
- 005541e8 bytes 1bb7fb97
+ 00554228 bytes 1bb7fb97
- 00554210 ["INT_ADD", "register:40f0:8", ["const:554210:8", "const:4:8"]]
- 00554210 ["CALL", null, ["callee:004427f4:8"]]
+ 00554250 ["INT_ADD", "register:40f0:8", ["const:554250:8", "const:4:8"]]
+ 00554250 ["CALL", null, ["callee:004427f4:8"]]
- 00554210 bytes 69b9fb97
+ 00554250 bytes 69b9fb97
- 00554344 ["INT_ADD", "register:40f0:8", ["const:554344:8", "const:4:8"]]
- 00554344 ["CALL", null, ["callee:00441e94:8"]]
+ 00554384 ["INT_ADD", "register:40f0:8", ["const:554384:8", "const:4:8"]]
+ 00554384 ["CALL", null, ["callee:00441e94:8"]]
- 00554344 bytes c4b6fb97
+ 00554384 bytes c4b6fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b779763bf1f6dffd452c76a9ec1c5bf2"></a>

### [`00554888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md) → [`005548c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005548c8.md) FUN_005548c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) [`00554888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`005540cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005540cc.md) [`005548c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005548c8.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00554a18",
      "incomplete_value": false,
      "site": "00554a20",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005549d8",
      "incomplete_value": false,
      "site": "005549e0",
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
            "const:f13:8"
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
      "definition_site": "00554b74",
      "incomplete_value": false,
      "site": "00554b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554b34",
      "incomplete_value": false,
      "site": "00554b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:da7:8"
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
      "definition_site": "00554b8c",
      "incomplete_value": false,
      "site": "00554b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00554b4c",
      "incomplete_value": false,
      "site": "00554b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ea9:8"
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
      "00554a18",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00554a3c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00554b74",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00554a18",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00554a3c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00554b74",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005549e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-005549e0) · [`00554b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-00554b3c) · [`00554b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-00554b58)
- 新版 [`00554a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005548c8.md#insn-00554a20) · [`00554b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005548c8.md#insn-00554b7c) · [`00554b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00554/005548c8.md#insn-00554b98)

~~~diff
- 005549e0 ["INT_ADD", "register:40f0:8", ["const:5549e0:8", "const:4:8"]]
- 005549e0 ["CALL", null, ["callee:00441e94:8"]]
+ 00554a20 ["INT_ADD", "register:40f0:8", ["const:554a20:8", "const:4:8"]]
+ 00554a20 ["CALL", null, ["callee:00441e94:8"]]
- 005549e0 bytes 1db5fb97
+ 00554a20 bytes 1db5fb97
- 00554b3c ["INT_ADD", "register:40f0:8", ["const:554b3c:8", "const:4:8"]]
- 00554b3c ["CALL", null, ["callee:00441e94:8"]]
+ 00554b7c ["INT_ADD", "register:40f0:8", ["const:554b7c:8", "const:4:8"]]
+ 00554b7c ["CALL", null, ["callee:00441e94:8"]]
- 00554b3c bytes c6b4fb97
+ 00554b7c bytes c6b4fb97
- 00554b58 ["INT_ADD", "register:40f0:8", ["const:554b58:8", "const:4:8"]]
- 00554b58 ["CALL", null, ["callee:004427f4:8"]]
+ 00554b98 ["INT_ADD", "register:40f0:8", ["const:554b98:8", "const:4:8"]]
+ 00554b98 ["CALL", null, ["callee:004427f4:8"]]
- 00554b58 bytes 17b7fb97
+ 00554b98 bytes 17b7fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7317f2b7169e896b5ff9dc300357dfd1"></a>

### [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) → [`005550b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md) FUN_005550b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00551e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md) · 呼出先 6件 [`00550ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md) [`005551d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551d4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00551eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551eac.md) · 呼出先 6件 [`00550f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550f34.md) [`00555214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555214.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005550e8",
      "incomplete_value": false,
      "site": "00555104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005550a8",
      "incomplete_value": false,
      "site": "005550c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
      "00555104",
      "DATA",
      [
        "storage",
        "00c6a8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00555198",
      "READ",
      [
        "storage",
        "00c6a8e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00555104",
      "DATA",
      [
        "storage",
        "00c6acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00555198",
      "READ",
      [
        "storage",
        "00c6ace8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-00555098) · [`005550a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-005550a8) · [`005550cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-005550cc)
- 新版 [`005550d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md#insn-005550d8) · [`005550e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md#insn-005550e8) · [`0055510c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005550b0.md#insn-0055510c)

~~~diff
- 00555098 ["INT_ADD", "register:40f0:8", ["const:555098:8", "const:4:8"]]
- 00555098 ["CALL", null, ["callee:00c57e90:8"]]
+ 005550d8 ["INT_ADD", "register:40f0:8", ["const:5550d8:8", "const:4:8"]]
+ 005550d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00555098 bytes 7e0a1c94
+ 005550d8 bytes 6e0b1c94
- 005550a8 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 005550a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005550a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005550a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005550e8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005550e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005550e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005550e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005550a8 bytes 08612391
+ 005550e8 bytes 08613391
- 005550cc ["INT_ADD", "register:40f0:8", ["const:5550cc:8", "const:4:8"]]
- 005550cc ["CALL", null, ["callee:00550f34:8"]]
+ 0055510c ["INT_ADD", "register:40f0:8", ["const:55510c:8", "const:4:8"]]
+ 0055510c ["CALL", null, ["callee:00550f34:8"]]
- 005550cc bytes 8aefff97
+ 0055510c bytes 8aefff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8403e2a80225c97af34425c6b105a40d"></a>

### [`00555194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555194.md) → [`005551d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005551d4.md) FUN_005551d4

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
      "definition_site": "005551d8",
      "incomplete_value": false,
      "site": "005551dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555198",
      "incomplete_value": false,
      "site": "0055519c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "005551dc",
      "DATA",
      [
        "storage",
        "00c6a8d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005551dc",
      "DATA",
      [
        "storage",
        "00c6acd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555194.md#insn-00555198)
- 新版 [`005551d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005551d4.md#insn-005551d8)

~~~diff
- 00555198 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00555198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005551d8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005551d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005551d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005551d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555198 bytes 08612391
+ 005551d8 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d570ac5fcc8fba85851d5239765d83"></a>

### [`005551a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551a4.md) → [`005551e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005551e4.md) FUN_005551e4

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
      "definition_site": "005551f4",
      "incomplete_value": false,
      "site": "005551fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005551b4",
      "incomplete_value": false,
      "site": "005551bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "005551fc",
      "DATA",
      [
        "storage",
        "00c6a8d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005551fc",
      "DATA",
      [
        "storage",
        "00c6acd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005551b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551a4.md#insn-005551b4) · [`005551c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551a4.md#insn-005551c0)
- 新版 [`005551f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005551e4.md#insn-005551f4) · [`00555200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005551e4.md#insn-00555200)

~~~diff
- 005551b4 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 005551b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005551b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005551b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005551f4 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005551f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005551f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005551f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005551b4 bytes 08612391
+ 005551f4 bytes 08613391
- 005551c0 ["INT_ADD", "register:40f0:8", ["const:5551c0:8", "const:4:8"]]
- 005551c0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00555200 ["INT_ADD", "register:40f0:8", ["const:555200:8", "const:4:8"]]
+ 00555200 ["CALL", null, ["callee:00c57ea0:8"]]
- 005551c0 bytes 380a1c94
+ 00555200 bytes 280b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-645a52fdc40e37be8c94c2910f7bd9f7"></a>

### [`00555234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md) → [`00555274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555274.md) FUN_00555274

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00555280",
      "incomplete_value": false,
      "site": "00555280",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555240",
      "incomplete_value": false,
      "site": "00555240",
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
            "const:808:8"
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
      "00555278",
      "READ",
      [
        "storage",
        "00ca5808",
        null,
        "undefined4"
      ]
    ],
    [
      "00555280",
      "WRITE",
      [
        "storage",
        "00ca5808",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00555278",
      "READ",
      [
        "storage",
        "00ca5c08",
        null,
        "undefined4"
      ]
    ],
    [
      "00555280",
      "WRITE",
      [
        "storage",
        "00ca5c08",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md#insn-00555240) · [`00555238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md#insn-00555238)
- 新版 [`00555280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555274.md#insn-00555280) · [`00555278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555274.md#insn-00555278)

~~~diff
- 00555240 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
- 00555240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00555280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 00555280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00555240 bytes 090908b9
+ 00555280 bytes 09090cb9
- 00555238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
- 00555238 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00555238 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00555278 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c08:8"]]
+ 00555278 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00555278 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00555238 bytes 090948b9
+ 00555278 bytes 09094cb9
~~~


<a id="compare-3d1a7111b284cac3bf14a73f5da3daa5"></a>

### [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) → [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) FUN_00555478

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00555284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555284.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md)
- 新版 呼出元 1件 [`005552c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552c4.md) · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004684e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004684e8.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 5件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00555548",
      "incomplete_value": true,
      "site": "00555548",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00555508",
      "incomplete_value": true,
      "site": "00555508",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055561c",
      "incomplete_value": true,
      "site": "0055561c",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005555dc",
      "incomplete_value": true,
      "site": "005555dc",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005556f4",
      "incomplete_value": true,
      "site": "005556f4",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005556b4",
      "incomplete_value": true,
      "site": "005556b4",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005554d0",
      "READ",
      [
        "storage",
        "00ca5868",
        null,
        "undefined1"
      ]
    ],
    [
      "005554d8",
      "READ",
      [
        "storage",
        "00ca5850",
        null,
        "undefined8"
      ]
    ],
    [
      "005554dc",
      "WRITE",
      [
        "storage",
        "00ca5858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005554d0",
      "READ",
      [
        "storage",
        "00ca5c68",
        null,
        "undefined1"
      ]
    ],
    [
      "005554d8",
      "READ",
      [
        "storage",
        "00ca5c50",
        null,
        "undefined8"
      ]
    ],
    [
      "005554dc",
      "WRITE",
      [
        "storage",
        "00ca5c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-00555508) · [`005555dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-005555dc) · [`005556a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-005556a4)
- 新版 [`00555548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md#insn-00555548) · [`0055561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md#insn-0055561c) · [`005556e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md#insn-005556e4)

~~~diff
- 00555508 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:858:8"]]
- 00555508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
+ 00555548 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c58:8"]]
+ 00555548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00555508 bytes 3b2d04f9
+ 00555548 bytes 3b2d06f9
- 005555dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:858:8"]]
- 005555dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
+ 0055561c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c58:8"]]
+ 0055561c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 005555dc bytes 3a2d04f9
+ 0055561c bytes 3a2d06f9
- 005556a4 ["INT_ADD", "register:40f0:8", ["const:5556a4:8", "const:4:8"]]
- 005556a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005556e4 ["INT_ADD", "register:40f0:8", ["const:5556e4:8", "const:4:8"]]
+ 005556e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 005556a4 bytes 03091c94
+ 005556e4 bytes f3091c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a999b8b0793c7f253a328a9a5304251"></a>

### [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) → [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) FUN_00555e0c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00559874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md) [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00556fcc",
      "incomplete_value": true,
      "site": "00556fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00556f8c",
      "incomplete_value": true,
      "site": "00556f90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
    "ordinal": 211,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00555e4c",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ],
    [
      "00555e58",
      "READ",
      [
        "storage",
        "00ca6054",
        null,
        "undefined4"
      ]
    ],
    [
      "00555f3c",
      "READ",
      [
        "storage",
        "00ca6050",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00555e4c",
      "READ",
      [
        "storage",
        "00c9b250",
        null,
        "pointer"
      ]
    ],
    [
      "00555e58",
      "READ",
      [
        "storage",
        "00ca6454",
        null,
        "undefined4"
      ]
    ],
    [
      "00555f3c",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555e00) · [`00555e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555e0c) · [`00555ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555ef8)
- 新版 [`00555e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md#insn-00555e40) · [`00555e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md#insn-00555e4c) · [`00555f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md#insn-00555f38)

~~~diff
- 00555e00 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00555e40 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00555e00 bytes 2a3a00b0
+ 00555e40 bytes 2a3a00d0
- 00555e0c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e50:8"]]
- 00555e0c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00555e4c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:250:8"]]
+ 00555e4c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00555e0c bytes 4a2947f9
+ 00555e4c bytes 4a2941f9
- 00555ef8 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00555ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00555f38 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00555f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00555f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00555f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555ef8 bytes 08410191
+ 00555f38 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98807b474d27e24890537443129de67"></a>

### [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) → [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) FUN_00559964

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md) · 呼出先 14件 [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md)
- 新版 呼出元 1件 [`0055a53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a53c.md) · 呼出先 14件 [`004684e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004684e8.md) [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) [`00559c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559c10.md) [`00559f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.58% / 新版 94.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00559a88",
      "incomplete_value": false,
      "site": "00559a8c",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559a48",
      "incomplete_value": false,
      "site": "00559a4c",
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
            "const:810:8"
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
      "definition_site": "00559aec",
      "incomplete_value": false,
      "site": "00559af0",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559aac",
      "incomplete_value": false,
      "site": "00559ab0",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00559b34",
      "incomplete_value": false,
      "site": "00559b44",
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
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559af4",
      "incomplete_value": false,
      "site": "00559b04",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055999c",
      "READ",
      [
        "storage",
        "00ca5828",
        null,
        "undefined1"
      ]
    ],
    [
      "005599a4",
      "READ",
      [
        "storage",
        "00ca5810",
        null,
        "undefined8"
      ]
    ],
    [
      "005599a8",
      "WRITE",
      [
        "storage",
        "00ca5818",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055999c",
      "READ",
      [
        "storage",
        "00ca5c28",
        null,
        "undefined1"
      ]
    ],
    [
      "005599a4",
      "READ",
      [
        "storage",
        "00ca5c10",
        null,
        "undefined8"
      ]
    ],
    [
      "005599a8",
      "WRITE",
      [
        "storage",
        "00ca5c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559a4c) · [`00559ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559ab0) · [`00559af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559af4)
- 新版 [`00559a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md#insn-00559a8c) · [`00559af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md#insn-00559af0) · [`00559b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md#insn-00559b34)

~~~diff
- 00559a4c ["INT_ADD", "register:40f0:8", ["const:559a4c:8", "const:4:8"]]
- 00559a4c ["CALL", null, ["callee:00559c10:8"]]
+ 00559a8c ["INT_ADD", "register:40f0:8", ["const:559a8c:8", "const:4:8"]]
+ 00559a8c ["CALL", null, ["callee:00559c10:8"]]
- 00559a4c bytes 61000094
+ 00559a8c bytes 61000094
- 00559ab0 ["INT_ADD", "register:40f0:8", ["const:559ab0:8", "const:4:8"]]
- 00559ab0 ["CALL", null, ["callee:00559f40:8"]]
+ 00559af0 ["INT_ADD", "register:40f0:8", ["const:559af0:8", "const:4:8"]]
+ 00559af0 ["CALL", null, ["callee:00559f40:8"]]
- 00559ab0 bytes 14010094
+ 00559af0 bytes 14010094
- 00559af4 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00559af4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00559af4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00559af4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00559b34 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00559b34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00559b34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00559b34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00559af4 bytes 00a02091
+ 00559b34 bytes 00a03091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8936e189a0c6eece54053305ce9665c4"></a>

### [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) → [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) FUN_0055a438

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) · 呼出先 8件 [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) [`0058ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md)
- 新版 呼出元 1件 [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) · 呼出先 8件 [`004684e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004684e8.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) [`00559c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559c10.md) [`00559f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559f40.md) [`0058ffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055a4d8",
      "incomplete_value": false,
      "site": "0055a4e4",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a498",
      "incomplete_value": false,
      "site": "0055a4a4",
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
            "const:848:8"
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
      "definition_site": "0055a500",
      "incomplete_value": false,
      "site": "0055a518",
      "value": [
        "leaf",
        "const:4684e8:8"
      ]
    },
    "old": {
      "definition_site": "0055a4c0",
      "incomplete_value": false,
      "site": "0055a4d8",
      "value": [
        "leaf",
        "const:4684a8:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055a508",
      "incomplete_value": false,
      "site": "0055a518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a4c8",
      "incomplete_value": false,
      "site": "0055a4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a450",
      "READ",
      [
        "storage",
        "00ca5848",
        null,
        "undefined1"
      ]
    ],
    [
      "0055a460",
      "READ",
      [
        "storage",
        "00ca5830",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a470",
      "PARAM",
      [
        "storage",
        "00ca5830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055a450",
      "READ",
      [
        "storage",
        "00ca5c48",
        null,
        "undefined1"
      ]
    ],
    [
      "0055a460",
      "READ",
      [
        "storage",
        "00ca5c30",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a470",
      "PARAM",
      [
        "storage",
        "00ca5c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a498) · [`0055a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a4a4) · [`0055a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a4d8)
- 新版 [`0055a4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md#insn-0055a4d8) · [`0055a4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md#insn-0055a4e4) · [`0055a518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md#insn-0055a518)

~~~diff
- 0055a498 ["COPY", "tmp:0:8", ["const:848:8"]]
- 0055a498 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0055a498 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0055a498 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055a4d8 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 0055a4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055a4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055a4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0055a498 bytes 00202191
+ 0055a4d8 bytes 00203191
- 0055a4a4 ["INT_ADD", "register:40f0:8", ["const:55a4a4:8", "const:4:8"]]
- 0055a4a4 ["CALL", null, ["callee:00c57e50:8"]]
+ 0055a4e4 ["INT_ADD", "register:40f0:8", ["const:55a4e4:8", "const:4:8"]]
+ 0055a4e4 ["CALL", null, ["callee:00c57e50:8"]]
- 0055a4a4 bytes 6bf51b94
+ 0055a4e4 bytes 5bf61b94
- 0055a4d8 ["INT_ADD", "register:40f0:8", ["const:55a4d8:8", "const:4:8"]]
- 0055a4d8 ["CALL", null, ["callee:00c57e30:8"]]
+ 0055a518 ["INT_ADD", "register:40f0:8", ["const:55a518:8", "const:4:8"]]
+ 0055a518 ["CALL", null, ["callee:00c57e30:8"]]
- 0055a4d8 bytes 56f51b94
+ 0055a518 bytes 46f61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-534cc8eab5058f2b5f6851ae042d2f3f"></a>

### [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) → [`0055a5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md) FUN_0055a5a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a5b0",
      "incomplete_value": true,
      "site": "0055a5b4",
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
      "definition_site": "0055a570",
      "incomplete_value": true,
      "site": "0055a574",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a5b0",
      "READ",
      [
        "storage",
        "00ca6010",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a5b0",
      "READ",
      [
        "storage",
        "00ca6410",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md#insn-0055a56c)
- 新版 [`0055a5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5a8.md#insn-0055a5ac)

~~~diff
- 0055a56c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0055a56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a5ac ["COPY", "tmp:0:8", ["const:410:8"]]
+ 0055a5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a56c bytes 08410091
+ 0055a5ac bytes 08411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f9a2c82e9ae4d9991e85c5648de634"></a>

### [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) → [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md) FUN_0055a5fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`00468d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468d08.md) [`00468e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468e20.md) [`0046a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a9fc.md) [`0046ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046ab48.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a61c",
      "incomplete_value": true,
      "site": "0055a61c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:268:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a5dc",
      "incomplete_value": true,
      "site": "0055a5dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e68:8"
              ]
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
      "0055a608",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0055a60c",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a614",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a608",
      "READ",
      [
        "storage",
        "00c9b240",
        null,
        "pointer"
      ]
    ],
    [
      "0055a60c",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a614",
      "READ",
      [
        "storage",
        "00c9b268",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5bc) · [`0055a5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5c4) · [`0055a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5c8)
- 新版 [`0055a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md#insn-0055a5fc) · [`0055a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md#insn-0055a604) · [`0055a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5fc.md#insn-0055a608)

~~~diff
- 0055a5bc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0055a5fc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0055a5bc bytes 083a0090
+ 0055a5fc bytes 083a00b0
- 0055a5c4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0055a604 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0055a5c4 bytes 093a0090
+ 0055a604 bytes 093a00b0
- 0055a5c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e40:8"]]
- 0055a5c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055a608 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
+ 0055a608 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055a5c8 bytes 082147f9
+ 0055a608 bytes 082141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cff492d4e91c762292a0014b40a9761b"></a>

### [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md) → [`0055a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md) FUN_0055a624

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f1c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a634",
      "incomplete_value": true,
      "site": "0055a634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a5f4",
      "incomplete_value": true,
      "site": "0055a5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a634",
      "incomplete_value": true,
      "site": "0055a634",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a5f4",
      "incomplete_value": true,
      "site": "0055a5f4",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a644",
      "incomplete_value": true,
      "site": "0055a644",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a604",
      "incomplete_value": true,
      "site": "0055a604",
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
            "const:8:8"
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
      "0055a630",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "0055a634",
      "WRITE",
      [
        "storage",
        "00ca3a20",
        null,
        "undefined4"
      ]
    ],
    [
      "0055a634",
      "WRITE",
      [
        "storage",
        "00ca3a24",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a630",
      "READ",
      [
        "storage",
        "00c9b270",
        null,
        "pointer"
      ]
    ],
    [
      "0055a634",
      "WRITE",
      [
        "storage",
        "00ca3e20",
        null,
        "undefined4"
      ]
    ],
    [
      "0055a634",
      "WRITE",
      [
        "storage",
        "00ca3e24",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5e4) · [`0055a5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5ec) · [`0055a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5f0)
- 新版 [`0055a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md#insn-0055a624) · [`0055a62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md#insn-0055a62c) · [`0055a630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md#insn-0055a630)

~~~diff
- 0055a5e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0055a624 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0055a5e4 bytes 083a0090
+ 0055a624 bytes 083a00b0
- 0055a5ec ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 0055a62c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 0055a5ec bytes 093a0090
+ 0055a62c bytes 093a00b0
- 0055a5f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 0055a5f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055a630 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 0055a630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055a5f0 bytes 083947f9
+ 0055a630 bytes 083941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96910287aa57dacb0be2cfbf0563dc9a"></a>

### [`0055a674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a674.md) → [`0055a6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b4.md) FUN_0055a6b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`008aac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008aa/008aac28.md) [`008abcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008abcf8.md) [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a6bc",
      "incomplete_value": true,
      "site": "0055a6c0",
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
      "definition_site": "0055a67c",
      "incomplete_value": true,
      "site": "0055a680",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a6bc",
      "READ",
      [
        "storage",
        "00ca6060",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a6bc",
      "READ",
      [
        "storage",
        "00ca6460",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a674.md#insn-0055a678)
- 新版 [`0055a6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b4.md#insn-0055a6b8)

~~~diff
- 0055a678 ["COPY", "tmp:0:8", ["const:60:8"]]
- 0055a678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a6b8 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 0055a6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a678 bytes 08810191
+ 0055a6b8 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-645b17863c66b03ab155c14bf6a4d50b"></a>

### [`0055a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a684.md) → [`0055a6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6c4.md) FUN_0055a6c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) [`008aac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008aa/008aac28.md) [`008abcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008abcf8.md) [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a6cc",
      "incomplete_value": true,
      "site": "0055a6d0",
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
      "definition_site": "0055a68c",
      "incomplete_value": true,
      "site": "0055a690",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a6cc",
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a6cc",
      "READ",
      [
        "storage",
        "00ca645c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a684.md#insn-0055a688)
- 新版 [`0055a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6c4.md#insn-0055a6c8)

~~~diff
- 0055a688 ["COPY", "tmp:0:8", ["const:5c:8"]]
- 0055a688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a6c8 ["COPY", "tmp:0:8", ["const:45c:8"]]
+ 0055a6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a688 bytes 08710191
+ 0055a6c8 bytes 08711191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56e2367b1334bdb97a5110412c9d8afa"></a>

### [`0055a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a694.md) → [`0055a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6d4.md) FUN_0055a6d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a6dc",
      "incomplete_value": true,
      "site": "0055a6e0",
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
      "definition_site": "0055a69c",
      "incomplete_value": true,
      "site": "0055a6a0",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a6dc",
      "READ",
      [
        "storage",
        "00ca6068",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a6dc",
      "READ",
      [
        "storage",
        "00ca6468",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a694.md#insn-0055a698)
- 新版 [`0055a6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6d4.md#insn-0055a6d8)

~~~diff
- 0055a698 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0055a698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a6d8 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0055a6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a698 bytes 08a10191
+ 0055a6d8 bytes 08a11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad487d6a9f4b597e023268459e7dad2"></a>

### [`0055a6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6a4.md) → [`0055a6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6e4.md) FUN_0055a6e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a6ec",
      "incomplete_value": true,
      "site": "0055a6f0",
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
      "definition_site": "0055a6ac",
      "incomplete_value": true,
      "site": "0055a6b0",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a6ec",
      "READ",
      [
        "storage",
        "00ca6064",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a6ec",
      "READ",
      [
        "storage",
        "00ca6464",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6a4.md#insn-0055a6a8)
- 新版 [`0055a6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6e4.md#insn-0055a6e8)

~~~diff
- 0055a6a8 ["COPY", "tmp:0:8", ["const:64:8"]]
- 0055a6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a6e8 ["COPY", "tmp:0:8", ["const:464:8"]]
+ 0055a6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a6a8 bytes 08910191
+ 0055a6e8 bytes 08911191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-531f6fa4efac545e2c178be488a48e3d"></a>

### [`0055b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md) → [`0055b138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b138.md) FUN_0055b138

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0055b144",
      "incomplete_value": false,
      "site": "0055b148",
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
      "definition_site": "0055b104",
      "incomplete_value": false,
      "site": "0055b108",
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
      "0055b144",
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
      "0055b144",
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

- 旧版 [`0055b108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md#insn-0055b108) · [`0055b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md#insn-0055b104)
- 新版 [`0055b148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b138.md#insn-0055b148) · [`0055b144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b138.md#insn-0055b144)

~~~diff
- 0055b108 ["INT_ADD", "register:40f0:8", ["const:55b108:8", "const:4:8"]]
- 0055b108 ["CALL", null, ["callee:0043b778:8"]]
+ 0055b148 ["INT_ADD", "register:40f0:8", ["const:55b148:8", "const:4:8"]]
+ 0055b148 ["CALL", null, ["callee:0043b778:8"]]
- 0055b108 bytes 8c81fb97
+ 0055b148 bytes 8c81fb97
- 0055b104 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0055b104 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0055b104 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0055b104 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b144 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0055b144 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b144 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b144 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0055b104 bytes 00303c91
+ 0055b144 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cdbf3ed49788af2ba61196f0589e74c"></a>

### [`0055b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md) → [`0055b14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b14c.md) FUN_0055b14c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0055a6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0055b158",
      "incomplete_value": false,
      "site": "0055b15c",
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
      "definition_site": "0055b118",
      "incomplete_value": false,
      "site": "0055b11c",
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
      "0055b158",
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
      "0055b158",
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

- 旧版 [`0055b11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md#insn-0055b11c) · [`0055b118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md#insn-0055b118)
- 新版 [`0055b15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b14c.md#insn-0055b15c) · [`0055b158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b14c.md#insn-0055b158)

~~~diff
- 0055b11c ["INT_ADD", "register:40f0:8", ["const:55b11c:8", "const:4:8"]]
- 0055b11c ["CALL", null, ["callee:0043b778:8"]]
+ 0055b15c ["INT_ADD", "register:40f0:8", ["const:55b15c:8", "const:4:8"]]
+ 0055b15c ["CALL", null, ["callee:0043b778:8"]]
- 0055b11c bytes 8781fb97
+ 0055b15c bytes 8781fb97
- 0055b118 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0055b118 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0055b118 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0055b118 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b158 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0055b158 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b158 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b158 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0055b118 bytes 00303c91
+ 0055b158 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639952bcb69f7f33a774c0c07a2c20a7"></a>

### [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) → [`0055b248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md) FUN_0055b248

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00555284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555284.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 5件 [`005552c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552c4.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`00559874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559874.md) [`00559f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559f40.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0055b254",
      "incomplete_value": false,
      "site": "0055b258",
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
      "definition_site": "0055b214",
      "incomplete_value": false,
      "site": "0055b218",
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
      "0055b254",
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
      "0055b254",
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

- 旧版 [`0055b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md#insn-0055b218) · [`0055b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md#insn-0055b214)
- 新版 [`0055b258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md#insn-0055b258) · [`0055b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b248.md#insn-0055b254)

~~~diff
- 0055b218 ["INT_ADD", "register:40f0:8", ["const:55b218:8", "const:4:8"]]
- 0055b218 ["CALL", null, ["callee:0043b778:8"]]
+ 0055b258 ["INT_ADD", "register:40f0:8", ["const:55b258:8", "const:4:8"]]
+ 0055b258 ["CALL", null, ["callee:0043b778:8"]]
- 0055b218 bytes 4881fb97
+ 0055b258 bytes 4881fb97
- 0055b214 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0055b214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0055b214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0055b214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b254 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0055b254 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b254 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b254 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0055b214 bytes 00303c91
+ 0055b254 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b64af8d34767ddb634bb0cddf674d696"></a>

### [`0055b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md) → [`0055b25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md) FUN_0055b25c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md) · 呼出先 5件 [`0055b340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b340.md) [`0055c694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c694.md) [`0055c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c69c.md) [`0055e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e500.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`0055c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md) · 呼出先 5件 [`0055b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b380.md) [`0055c6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6d4.md) [`0055c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6dc.md) [`0055e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e540.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.81% / 新版 82.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b27c",
      "incomplete_value": false,
      "site": "0055b27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b23c",
      "incomplete_value": false,
      "site": "0055b23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "definition_site": "0055b298",
      "incomplete_value": false,
      "site": "0055b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b258",
      "incomplete_value": false,
      "site": "0055b258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "0055b298",
      "incomplete_value": false,
      "site": "0055b298",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b258",
      "incomplete_value": false,
      "site": "0055b258",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055b27c",
      "DATA",
      [
        "storage",
        "00c6aa38",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b298",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b298",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b27c",
      "DATA",
      [
        "storage",
        "00c6ae38",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b298",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b298",
      "DATA",
      [
        "storage",
        "00c6adb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md#insn-0055b230) · [`0055b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md#insn-0055b240) · [`0055b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md#insn-0055b248)
- 新版 [`0055b270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md#insn-0055b270) · [`0055b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md#insn-0055b280) · [`0055b288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md#insn-0055b288)

~~~diff
- 0055b230 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 0055b230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b270 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0055b270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b230 bytes 08e12891
+ 0055b270 bytes 08e13891
- 0055b240 ["INT_ADD", "register:40f0:8", ["const:55b240:8", "const:4:8"]]
- 0055b240 ["CALL", null, ["callee:0055e540:8"]]
+ 0055b280 ["INT_ADD", "register:40f0:8", ["const:55b280:8", "const:4:8"]]
+ 0055b280 ["CALL", null, ["callee:0055e540:8"]]
- 0055b240 bytes b00c0094
+ 0055b280 bytes b00c0094
- 0055b248 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0055b248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b288 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0055b288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b248 bytes 08212591
+ 0055b288 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb56ce954f076e63a76b7d370b60027c"></a>

### [`0055c320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md) → [`0055c360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md) FUN_0055c360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0055b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 2件 [`0055b25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b25c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0055c390",
      "incomplete_value": false,
      "site": "0055c39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c350",
      "incomplete_value": false,
      "site": "0055c35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "0055c39c",
      "DATA",
      [
        "storage",
        "00c6aa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c39c",
      "DATA",
      [
        "storage",
        "00c6ae60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c344) · [`0055c350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c350) · [`0055c368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c368)
- 新版 [`0055c384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md#insn-0055c384) · [`0055c390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md#insn-0055c390) · [`0055c3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c360.md#insn-0055c3a8)

~~~diff
- 0055c344 ["INT_ADD", "register:40f0:8", ["const:55c344:8", "const:4:8"]]
- 0055c344 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055c384 ["INT_ADD", "register:40f0:8", ["const:55c384:8", "const:4:8"]]
+ 0055c384 ["CALL", null, ["callee:00c57e90:8"]]
- 0055c344 bytes d3ed1b94
+ 0055c384 bytes c3ee1b94
- 0055c350 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 0055c350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c390 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0055c390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c350 bytes 08812991
+ 0055c390 bytes 08813991
- 0055c368 ["INT_ADD", "register:40f0:8", ["const:55c368:8", "const:4:8"]]
- 0055c368 ["CALL", null, ["callee:0055b25c:8"]]
+ 0055c3a8 ["INT_ADD", "register:40f0:8", ["const:55c3a8:8", "const:4:8"]]
+ 0055c3a8 ["CALL", null, ["callee:0055b25c:8"]]
- 0055c368 bytes adfbff97
+ 0055c3a8 bytes adfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f388596166ebe2b4a37b979065a0b87a"></a>

### [`0055c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md) → [`0055c3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c3e4.md) FUN_0055c3e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c3f8",
      "incomplete_value": false,
      "site": "0055c404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c3b8",
      "incomplete_value": false,
      "site": "0055c3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "0055c410",
      "incomplete_value": false,
      "site": "0055c410",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c3d0",
      "incomplete_value": false,
      "site": "0055c3d0",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c404",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c410",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c404",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c410",
      "DATA",
      [
        "storage",
        "00c6adb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md#insn-0055c410) · [`0055c3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md#insn-0055c3b8) · [`0055c3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md#insn-0055c3c0)
- 新版 [`0055c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c3e4.md#insn-0055c450) · [`0055c3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c3e4.md#insn-0055c3f8)

~~~diff
- 0055c410 ["INT_ADD", "register:40f0:8", ["const:55c410:8", "const:4:8"]]
- 0055c410 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055c450 ["INT_ADD", "register:40f0:8", ["const:55c450:8", "const:4:8"]]
+ 0055c450 ["CALL", null, ["callee:00c53d00:8"]]
- 0055c410 bytes 34dd1b94
+ 0055c450 bytes 2cde1b94
- 0055c3b8 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0055c3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c3f8 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0055c3f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c3f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c3f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c3b8 bytes 08212591
+ 0055c3f8 bytes 08213591
- 0055c3c0 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0055c3c0 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4066b987dc7686b6d808096d2ad92b0f"></a>

### [`0055c444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md) → [`0055c484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c484.md) FUN_0055c484

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0055c498",
      "incomplete_value": false,
      "site": "0055c4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c458",
      "incomplete_value": false,
      "site": "0055c464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "0055c4b0",
      "incomplete_value": false,
      "site": "0055c4b0",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c470",
      "incomplete_value": false,
      "site": "0055c470",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c4a4",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c4b0",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c4a4",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c4b0",
      "DATA",
      [
        "storage",
        "00c6adb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md#insn-0055c4b0) · [`0055c458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md#insn-0055c458) · [`0055c460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md#insn-0055c460)
- 新版 [`0055c4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c484.md#insn-0055c4f0) · [`0055c498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c484.md#insn-0055c498)

~~~diff
- 0055c4b0 ["INT_ADD", "register:40f0:8", ["const:55c4b0:8", "const:4:8"]]
- 0055c4b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055c4f0 ["INT_ADD", "register:40f0:8", ["const:55c4f0:8", "const:4:8"]]
+ 0055c4f0 ["CALL", null, ["callee:00c53d00:8"]]
- 0055c4b0 bytes 0cdd1b94
+ 0055c4f0 bytes 04de1b94
- 0055c458 ["COPY", "tmp:0:8", ["const:948:8"]]
- 0055c458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c498 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0055c498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c458 bytes 08212591
+ 0055c498 bytes 08213591
- 0055c460 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0055c460 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4b90be6aeefdb66de4900252d977ae"></a>

### [`0055c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md) → [`0055c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c52c.md) FUN_0055c52c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c54c",
      "incomplete_value": false,
      "site": "0055c54c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c50c",
      "incomplete_value": false,
      "site": "0055c50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "definition_site": "0055c54c",
      "incomplete_value": false,
      "site": "0055c54c",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c50c",
      "incomplete_value": false,
      "site": "0055c50c",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c54c",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c54c",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c54c",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c54c",
      "DATA",
      [
        "storage",
        "00c6adb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c54c) · [`0055c4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c4fc) · [`0055c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c51c)
- 新版 [`0055c58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c52c.md#insn-0055c58c) · [`0055c53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c52c.md#insn-0055c53c) · [`0055c55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c52c.md#insn-0055c55c)

~~~diff
- 0055c54c ["INT_ADD", "register:40f0:8", ["const:55c54c:8", "const:4:8"]]
- 0055c54c ["CALL", null, ["callee:00c53d00:8"]]
+ 0055c58c ["INT_ADD", "register:40f0:8", ["const:55c58c:8", "const:4:8"]]
+ 0055c58c ["CALL", null, ["callee:00c53d00:8"]]
- 0055c54c bytes e5dc1b94
+ 0055c58c bytes dddd1b94
- 0055c4fc ["COPY", "tmp:0:8", ["const:948:8"]]
- 0055c4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c53c ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0055c53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c4fc bytes 08212591
+ 0055c53c bytes 08213591
- 0055c51c ["INT_ADD", "register:40f0:8", ["const:55c51c:8", "const:4:8"]]
- 0055c51c ["CALL", null, ["callee:00c53d00:8"]]
+ 0055c55c ["INT_ADD", "register:40f0:8", ["const:55c55c:8", "const:4:8"]]
+ 0055c55c ["CALL", null, ["callee:00c53d00:8"]]
- 0055c51c bytes f1dc1b94
+ 0055c55c bytes e9dd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51a9ffcc96cd16fb4bab933247c99d63"></a>

### [`0055c624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c624.md) → [`0055c664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c664.md) FUN_0055c664

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
      "definition_site": "0055c668",
      "incomplete_value": false,
      "site": "0055c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c628",
      "incomplete_value": false,
      "site": "0055c62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
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
      "0055c66c",
      "DATA",
      [
        "storage",
        "00c6aa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c66c",
      "DATA",
      [
        "storage",
        "00c6ae60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c624.md#insn-0055c628)
- 新版 [`0055c668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c664.md#insn-0055c668)

~~~diff
- 0055c628 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 0055c628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c668 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 0055c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c628 bytes 08812991
+ 0055c668 bytes 08813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c897efdee684ed4a6b2d247a7a9d675a"></a>

### [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) → [`0055c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md) FUN_0055c6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00551274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551274.md) [`0055b4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055b/0055b4b8.md) [`00a994a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a994a4.md) · 呼出先 2件 [`0055c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c710",
      "incomplete_value": false,
      "site": "0055c718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c6d0",
      "incomplete_value": false,
      "site": "0055c6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "definition_site": "0055c724",
      "incomplete_value": false,
      "site": "0055c724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c6e4",
      "incomplete_value": false,
      "site": "0055c6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "0055c718",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c724",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c718",
      "DATA",
      [
        "storage",
        "00c6af00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c724",
      "DATA",
      [
        "storage",
        "00c6aeb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6c8) · [`0055c6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6d0) · [`0055c6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6d4)
- 新版 [`0055c708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md#insn-0055c708) · [`0055c710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6e4.md#insn-0055c710)

~~~diff
- 0055c6c8 ["INT_ADD", "register:40f0:8", ["const:55c6c8:8", "const:4:8"]]
- 0055c6c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055c708 ["INT_ADD", "register:40f0:8", ["const:55c708:8", "const:4:8"]]
+ 0055c708 ["CALL", null, ["callee:00c57e90:8"]]
- 0055c6c8 bytes f2ec1b94
+ 0055c708 bytes e2ed1b94
- 0055c6d0 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0055c6d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c6d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c6d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c710 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0055c710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c6d0 bytes 08012c91
+ 0055c710 bytes 08013c91
- 0055c6d4 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 0055c6d4 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c58ca81a8189dbeb74874e1226a8afd"></a>

### [`0055c7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e4.md) → [`0055c824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c824.md) FUN_0055c824

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
      "definition_site": "0055c830",
      "incomplete_value": false,
      "site": "0055c834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c7f0",
      "incomplete_value": false,
      "site": "0055c7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "0055c834",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c834",
      "DATA",
      [
        "storage",
        "00c6aeb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e4.md#insn-0055c7f0)
- 新版 [`0055c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c824.md#insn-0055c830)

~~~diff
- 0055c7f0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 0055c7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c830 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0055c830 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c830 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c830 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c7f0 bytes 29c12a91
+ 0055c830 bytes 29c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f44eb6b02e7f6870ac741c252b4aec"></a>

### [`0055c808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md) → [`0055c848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c848.md) FUN_0055c848

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
      "definition_site": "0055c850",
      "incomplete_value": false,
      "site": "0055c854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c810",
      "incomplete_value": false,
      "site": "0055c814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "0055c854",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c854",
      "DATA",
      [
        "storage",
        "00c6aeb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md#insn-0055c810) · [`0055c834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md#insn-0055c834)
- 新版 [`0055c850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c848.md#insn-0055c850) · [`0055c874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c848.md#insn-0055c874)

~~~diff
- 0055c810 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 0055c810 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c810 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c810 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c850 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0055c850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c810 bytes 29c12a91
+ 0055c850 bytes 29c13a91
- 0055c834 ["INT_ADD", "register:40f0:8", ["const:55c834:8", "const:4:8"]]
- 0055c834 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0055c874 ["INT_ADD", "register:40f0:8", ["const:55c874:8", "const:4:8"]]
+ 0055c874 ["CALL", null, ["callee:00c57eb0:8"]]
- 0055c834 bytes 9fec1b94
+ 0055c874 bytes 8fed1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8281b4b6adb831225529ed7bb59480"></a>

### [`0055c974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c974.md) → [`0055c9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c9b4.md) FUN_0055c9b4

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
      "definition_site": "0055c9b8",
      "incomplete_value": false,
      "site": "0055c9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c978",
      "incomplete_value": false,
      "site": "0055c97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "0055c9bc",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c9bc",
      "DATA",
      [
        "storage",
        "00c6af00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c974.md#insn-0055c978)
- 新版 [`0055c9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c9b4.md#insn-0055c9b8)

~~~diff
- 0055c978 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0055c978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c9b8 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0055c9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c978 bytes 08012c91
+ 0055c9b8 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522dfef6ac292c211d5fc5b47a141a4a"></a>

### [`0055c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c984.md) → [`0055c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c9c4.md) FUN_0055c9c4

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
      "definition_site": "0055c9d4",
      "incomplete_value": false,
      "site": "0055c9dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c994",
      "incomplete_value": false,
      "site": "0055c99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "0055c9dc",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c9dc",
      "DATA",
      [
        "storage",
        "00c6af00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c984.md#insn-0055c994) · [`0055c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c984.md#insn-0055c9a0)
- 新版 [`0055c9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c9c4.md#insn-0055c9d4) · [`0055c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c9c4.md#insn-0055c9e0)

~~~diff
- 0055c994 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0055c994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c9d4 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0055c9d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c994 bytes 08012c91
+ 0055c9d4 bytes 08013c91
- 0055c9a0 ["INT_ADD", "register:40f0:8", ["const:55c9a0:8", "const:4:8"]]
- 0055c9a0 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0055c9e0 ["INT_ADD", "register:40f0:8", ["const:55c9e0:8", "const:4:8"]]
+ 0055c9e0 ["CALL", null, ["callee:00c57ea0:8"]]
- 0055c9a0 bytes 40ec1b94
+ 0055c9e0 bytes 30ed1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bca818c17e8ca43f8b5ebd9a10cbec6d"></a>

### [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) → [`0055ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md) FUN_0055ca04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) · 呼出先 3件 [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) · 呼出先 3件 [`0055c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c888.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ca34",
      "incomplete_value": false,
      "site": "0055ca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c9f4",
      "incomplete_value": false,
      "site": "0055ca00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "definition_site": "0055ca54",
      "incomplete_value": false,
      "site": "0055ca54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ca14",
      "incomplete_value": false,
      "site": "0055ca14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "0055ca40",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ca54",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ca40",
      "DATA",
      [
        "storage",
        "00c6af00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ca54",
      "DATA",
      [
        "storage",
        "00c6aeb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055ca54) · [`0055c9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055c9ec) · [`0055c9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055c9f4)
- 新版 [`0055ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md#insn-0055ca94) · [`0055ca2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md#insn-0055ca2c) · [`0055ca34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055ca04.md#insn-0055ca34)

~~~diff
- 0055ca54 ["INT_ADD", "register:40f0:8", ["const:55ca54:8", "const:4:8"]]
- 0055ca54 ["CALL", null, ["callee:00c57f40:8"]]
+ 0055ca94 ["INT_ADD", "register:40f0:8", ["const:55ca94:8", "const:4:8"]]
+ 0055ca94 ["CALL", null, ["callee:00c57f40:8"]]
- 0055ca54 bytes 3bec1b94
+ 0055ca94 bytes 2bed1b94
- 0055c9ec ["INT_ADD", "register:40f0:8", ["const:55c9ec:8", "const:4:8"]]
- 0055c9ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0055ca2c ["INT_ADD", "register:40f0:8", ["const:55ca2c:8", "const:4:8"]]
+ 0055ca2c ["CALL", null, ["callee:00c57e90:8"]]
- 0055c9ec bytes 29ec1b94
+ 0055ca2c bytes 19ed1b94
- 0055c9f4 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0055c9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ca34 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0055ca34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ca34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ca34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c9f4 bytes 08012c91
+ 0055ca34 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd47e130e7b70612e9ccd2d9f2093dda"></a>

### [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) → [`0055cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cae0.md) FUN_0055cae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md) · 呼出先 11件 [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`0055d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d3f0.md) · 呼出先 11件 [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0055d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cb10",
      "incomplete_value": false,
      "site": "0055cb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cad0",
      "incomplete_value": false,
      "site": "0055cadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "definition_site": "0055cb64",
      "incomplete_value": false,
      "site": "0055cb70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cb24",
      "incomplete_value": false,
      "site": "0055cb30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "0055cb1c",
      "DATA",
      [
        "storage",
        "00c6ab50",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cb70",
      "DATA",
      [
        "storage",
        "00c6ab90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055cb1c",
      "DATA",
      [
        "storage",
        "00c6af50",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cb70",
      "DATA",
      [
        "storage",
        "00c6af90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cad0) · [`0055cad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cad4) · [`0055cb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cb14)
- 新版 [`0055cb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cae0.md#insn-0055cb10) · [`0055cb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cae0.md#insn-0055cb54)

~~~diff
- 0055cad0 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 0055cad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055cad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055cad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055cb10 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0055cb10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055cb10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055cb10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055cad0 bytes 08412d91
+ 0055cb10 bytes 08413d91
- 0055cad4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0055cad4 bytes f40300aa
- 0055cb14 ["INT_ADD", "register:40f0:8", ["const:55cb14:8", "const:4:8"]]
- 0055cb14 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055cb54 ["INT_ADD", "register:40f0:8", ["const:55cb54:8", "const:4:8"]]
+ 0055cb54 ["CALL", null, ["callee:00c57e90:8"]]
- 0055cb14 bytes dfeb1b94
+ 0055cb54 bytes cfec1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba5a50839de844926eae82449b6d99e"></a>

### [`0055d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md) → [`0055d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d3f0.md) FUN_0055d3f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00467bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467bb0.md) · 呼出先 2件 [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00467bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467bf0.md) · 呼出先 2件 [`0055cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cae0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0055d424",
      "incomplete_value": false,
      "site": "0055d430",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d3e4",
      "incomplete_value": false,
      "site": "0055d3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0055d430",
      "DATA",
      [
        "storage",
        "00c6ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d430",
      "DATA",
      [
        "storage",
        "00c6b020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3d8) · [`0055d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3e0) · [`0055d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3e4)
- 新版 [`0055d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d3f0.md#insn-0055d418) · [`0055d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d3f0.md#insn-0055d420) · [`0055d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d3f0.md#insn-0055d424)

~~~diff
- 0055d3d8 ["INT_ADD", "register:40f0:8", ["const:55d3d8:8", "const:4:8"]]
- 0055d3d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0055d418 ["INT_ADD", "register:40f0:8", ["const:55d418:8", "const:4:8"]]
+ 0055d418 ["CALL", null, ["callee:00c57e90:8"]]
- 0055d3d8 bytes aee91b94
+ 0055d418 bytes 9eea1b94
- 0055d3e0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055d420 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055d3e0 bytes 683800b0
+ 0055d420 bytes 683800d0
- 0055d3e4 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0055d3e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d3e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d3e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d424 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 0055d424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d3e4 bytes 08813091
+ 0055d424 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a5c1f377f4d6216e1a8886e8f84aa9"></a>

### [`0055d43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d43c.md) → [`0055d47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d47c.md) FUN_0055d47c

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
      "definition_site": "0055d480",
      "incomplete_value": false,
      "site": "0055d484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d440",
      "incomplete_value": false,
      "site": "0055d444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "0055d484",
      "DATA",
      [
        "storage",
        "00c6ab90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d484",
      "DATA",
      [
        "storage",
        "00c6af90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d43c.md#insn-0055d440)
- 新版 [`0055d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d47c.md#insn-0055d480)

~~~diff
- 0055d440 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0055d440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d480 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0055d480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d440 bytes 08412e91
+ 0055d480 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eb80ac23ebbe13f894c87e39cbf325b"></a>

### [`0055d44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d44c.md) → [`0055d48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d48c.md) FUN_0055d48c

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
      "definition_site": "0055d49c",
      "incomplete_value": false,
      "site": "0055d4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d45c",
      "incomplete_value": false,
      "site": "0055d464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "0055d4a4",
      "DATA",
      [
        "storage",
        "00c6ab90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d4a4",
      "DATA",
      [
        "storage",
        "00c6af90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d44c.md#insn-0055d45c) · [`0055d468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d44c.md#insn-0055d468)
- 新版 [`0055d49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d48c.md#insn-0055d49c) · [`0055d4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d48c.md#insn-0055d4a8)

~~~diff
- 0055d45c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0055d45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d49c ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0055d49c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d49c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d49c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d45c bytes 08412e91
+ 0055d49c bytes 08413e91
- 0055d468 ["INT_ADD", "register:40f0:8", ["const:55d468:8", "const:4:8"]]
- 0055d468 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0055d4a8 ["INT_ADD", "register:40f0:8", ["const:55d4a8:8", "const:4:8"]]
+ 0055d4a8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0055d468 bytes 8ee91b94
+ 0055d4a8 bytes 7eea1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fd293139f3050cc91e28b0baeb5bd53"></a>

### [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) → [`0055d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md) FUN_0055d4c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) · 呼出先 1件 [`0055dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md)
- 新版 呼出元 1件 [`0055cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055cae0.md) · 呼出先 1件 [`0055df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055df00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d4e4",
      "incomplete_value": true,
      "site": "0055d4e8",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d4a4",
      "incomplete_value": true,
      "site": "0055d4a8",
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
            "const:be0:8"
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
      "0055d4e8",
      "DATA",
      [
        "storage",
        "00c6abe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d4e8",
      "DATA",
      [
        "storage",
        "00c6afe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md#insn-0055d4a4) · [`0055d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md#insn-0055d4f8)
- 新版 [`0055d4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md#insn-0055d4e4) · [`0055d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d4c8.md#insn-0055d538)

~~~diff
- 0055d4a4 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 0055d4a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d4a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d4a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d4e4 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 0055d4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d4a4 bytes 08812f91
+ 0055d4e4 bytes 08813f91
- 0055d4f8 ["INT_ADD", "register:40f0:8", ["const:55d4f8:8", "const:4:8"]]
- 0055d4f8 ["CALL", null, ["callee:0055df00:8"]]
+ 0055d538 ["INT_ADD", "register:40f0:8", ["const:55d538:8", "const:4:8"]]
+ 0055d538 ["CALL", null, ["callee:0055df00:8"]]
- 0055d4f8 bytes 72020094
+ 0055d538 bytes 72020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a499694b5ece8e9dd45a4c7f8258c8c6"></a>

### [`0055e43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e43c.md) → [`0055e47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e47c.md) FUN_0055e47c

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
      "definition_site": "0055e480",
      "incomplete_value": false,
      "site": "0055e484",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e440",
      "incomplete_value": false,
      "site": "0055e444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0055e484",
      "DATA",
      [
        "storage",
        "00c6ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e484",
      "DATA",
      [
        "storage",
        "00c6b020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e43c.md#insn-0055e43c) · [`0055e440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e43c.md#insn-0055e440)
- 新版 [`0055e47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e47c.md#insn-0055e47c) · [`0055e480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e47c.md#insn-0055e480)

~~~diff
- 0055e43c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055e47c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055e43c bytes 68380090
+ 0055e47c bytes 683800b0
- 0055e440 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0055e440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e480 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 0055e480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e440 bytes 08813091
+ 0055e480 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bdfed3574d42e5589f9cb65975cba97"></a>

### [`0055e44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e44c.md) → [`0055e48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e48c.md) FUN_0055e48c

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
      "definition_site": "0055e49c",
      "incomplete_value": false,
      "site": "0055e4a4",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e45c",
      "incomplete_value": false,
      "site": "0055e464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "0055e4a4",
      "DATA",
      [
        "storage",
        "00c6ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e4a4",
      "DATA",
      [
        "storage",
        "00c6b020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e44c.md#insn-0055e458) · [`0055e45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e44c.md#insn-0055e45c) · [`0055e468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e44c.md#insn-0055e468)
- 新版 [`0055e498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e48c.md#insn-0055e498) · [`0055e49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e48c.md#insn-0055e49c) · [`0055e4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e48c.md#insn-0055e4a8)

~~~diff
- 0055e458 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055e498 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055e458 bytes 68380090
+ 0055e498 bytes 683800b0
- 0055e45c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0055e45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e49c ["COPY", "tmp:0:8", ["const:20:8"]]
+ 0055e49c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e49c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e49c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e45c bytes 08813091
+ 0055e49c bytes 08810091
- 0055e468 ["INT_ADD", "register:40f0:8", ["const:55e468:8", "const:4:8"]]
- 0055e468 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0055e4a8 ["INT_ADD", "register:40f0:8", ["const:55e4a8:8", "const:4:8"]]
+ 0055e4a8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0055e468 bytes 8ee51b94
+ 0055e4a8 bytes 7ee61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c44a86c2315e57123cac929699ca5d44"></a>

### [`0055e47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md) → [`0055e4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e4bc.md) FUN_0055e4bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0055e4d4",
      "incomplete_value": false,
      "site": "0055e4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e494",
      "incomplete_value": false,
      "site": "0055e498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "0055e4d8",
      "DATA",
      [
        "storage",
        "00c6ab50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e4d8",
      "DATA",
      [
        "storage",
        "00c6af50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e494) · [`0055e4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e4a8) · [`0055e4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e4bc)
- 新版 [`0055e4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e4bc.md#insn-0055e4d4) · [`0055e4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e4bc.md#insn-0055e4e8) · [`0055e4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e4bc.md#insn-0055e4fc)

~~~diff
- 0055e494 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 0055e494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e4d4 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0055e4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e494 bytes 08412d91
+ 0055e4d4 bytes 08413d91
- 0055e4a8 ["INT_ADD", "register:40f0:8", ["const:55e4a8:8", "const:4:8"]]
- 0055e4a8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055e4e8 ["INT_ADD", "register:40f0:8", ["const:55e4e8:8", "const:4:8"]]
+ 0055e4e8 ["CALL", null, ["callee:00c53d00:8"]]
- 0055e4a8 bytes 0ed51b94
+ 0055e4e8 bytes 06d61b94
- 0055e4bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0055e4bc ["INT_ADD", "register:40f0:8", ["const:55e4bc:8", "const:4:8"]]
- 0055e4bc ["CALLIND", null, ["register:0:8"]]
+ 0055e4fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055e4fc ["INT_ADD", "register:40f0:8", ["const:55e4fc:8", "const:4:8"]]
+ 0055e4fc ["CALLIND", null, ["register:0:8"]]
- 0055e4bc bytes 00013fd6
+ 0055e4fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebe1f22ed824f1dd850e4e2a92217d9f"></a>

### [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) → [`0055e5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md) FUN_0055e5ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00551ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md) [`00551f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md) [`0055c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md) [`0055c444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md) [`0055c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 6件 [`00551f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f0c.md) [`00551f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551f7c.md) [`0055c3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c3e4.md) [`0055c484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c484.md) [`0055c52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c52c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0055e5c0",
      "incomplete_value": false,
      "site": "0055e5c4",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e580",
      "incomplete_value": false,
      "site": "0055e584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      "0055e5c4",
      "DATA",
      [
        "storage",
        "00c6ac70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e5c4",
      "DATA",
      [
        "storage",
        "00c6b070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e57c) · [`0055e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e580) · [`0055e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e594)
- 新版 [`0055e5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md#insn-0055e5bc) · [`0055e5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md#insn-0055e5c0) · [`0055e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e5ac.md#insn-0055e5d4)

~~~diff
- 0055e57c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055e5bc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055e57c bytes 68380090
+ 0055e5bc bytes 683800b0
- 0055e580 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 0055e580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e5c0 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 0055e5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e580 bytes 08c13191
+ 0055e5c0 bytes 08c10191
- 0055e594 ["INT_ADD", "register:40f0:8", ["const:55e594:8", "const:4:8"]]
- 0055e594 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055e5d4 ["INT_ADD", "register:40f0:8", ["const:55e5d4:8", "const:4:8"]]
+ 0055e5d4 ["CALL", null, ["callee:00c53d00:8"]]
- 0055e594 bytes d3d41b94
+ 0055e5d4 bytes cbd51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dd89abf60da0cb7f05cc037cfba4bd2"></a>

### [`0055ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md) → [`0055ed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md) FUN_0055ed08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md) · 呼出先 7件 [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0048d424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d424.md) · 呼出先 7件 [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055eefc",
      "incomplete_value": false,
      "site": "0055ef04",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eebc",
      "incomplete_value": false,
      "site": "0055eec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "definition_site": "0055ef28",
      "incomplete_value": false,
      "site": "0055ef28",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eee8",
      "incomplete_value": false,
      "site": "0055eee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "0055ef44",
      "incomplete_value": false,
      "site": "0055ef44",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ef04",
      "incomplete_value": false,
      "site": "0055ef04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0055ef04",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef28",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef44",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ef04",
      "DATA",
      [
        "storage",
        "00c6b148",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef28",
      "DATA",
      [
        "storage",
        "00c6b0d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef44",
      "DATA",
      [
        "storage",
        "00c6b0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ed14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed14) · [`0055ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed2c) · [`0055ed48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed48)
- 新版 [`0055ed54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md#insn-0055ed54) · [`0055ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md#insn-0055ed6c) · [`0055ed88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md#insn-0055ed88)

~~~diff
- 0055ed14 ["COPY", "register:0:8", ["register:4040:8"]]
- 0055ed14 ["INT_ADD", "register:40f0:8", ["const:55ed14:8", "const:4:8"]]
- 0055ed14 ["CALLIND", null, ["register:0:8"]]
+ 0055ed54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055ed54 ["INT_ADD", "register:40f0:8", ["const:55ed54:8", "const:4:8"]]
+ 0055ed54 ["CALLIND", null, ["register:0:8"]]
- 0055ed14 bytes 00013fd6
+ 0055ed54 bytes 00013fd6
- 0055ed2c ["INT_ADD", "register:40f0:8", ["const:55ed2c:8", "const:4:8"]]
- 0055ed2c ["CALL", null, ["callee:00581494:8"]]
+ 0055ed6c ["INT_ADD", "register:40f0:8", ["const:55ed6c:8", "const:4:8"]]
+ 0055ed6c ["CALL", null, ["callee:00581494:8"]]
- 0055ed2c bytes ca890094
+ 0055ed6c bytes ca890094
- 0055ed48 ["COPY", "register:0:8", ["register:4048:8"]]
- 0055ed48 ["INT_ADD", "register:40f0:8", ["const:55ed48:8", "const:4:8"]]
- 0055ed48 ["CALLIND", null, ["register:0:8"]]
+ 0055ed88 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055ed88 ["INT_ADD", "register:40f0:8", ["const:55ed88:8", "const:4:8"]]
+ 0055ed88 ["CALLIND", null, ["register:0:8"]]
- 0055ed48 bytes 20013fd6
+ 0055ed88 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e33ef577dc900feb2b99a79df7b0df4"></a>

### [`0055f308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md) → [`0055f348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f348.md) FUN_0055f348

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
      "definition_site": "0055f360",
      "incomplete_value": false,
      "site": "0055f364",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f320",
      "incomplete_value": false,
      "site": "0055f324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0055f364",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f364",
      "DATA",
      [
        "storage",
        "00c6b0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f31c) · [`0055f320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f320) · [`0055f334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f334)
- 新版 [`0055f35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f348.md#insn-0055f35c) · [`0055f360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f348.md#insn-0055f360) · [`0055f374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f348.md#insn-0055f374)

~~~diff
- 0055f31c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055f35c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055f31c bytes 483800f0
+ 0055f35c bytes 68380090
- 0055f320 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0055f320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f360 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 0055f360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f320 bytes 08413391
+ 0055f360 bytes 08410391
- 0055f334 ["INT_ADD", "register:40f0:8", ["const:55f334:8", "const:4:8"]]
- 0055f334 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055f374 ["INT_ADD", "register:40f0:8", ["const:55f374:8", "const:4:8"]]
+ 0055f374 ["CALL", null, ["callee:00c53d00:8"]]
- 0055f334 bytes 6bd11b94
+ 0055f374 bytes 63d21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2b7ff539269d116cb16fbf880b35f4"></a>

### [`0055f3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md) → [`0055f3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f3e4.md) FUN_0055f3e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0055f3fc",
      "incomplete_value": false,
      "site": "0055f400",
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
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f3bc",
      "incomplete_value": false,
      "site": "0055f3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "0055f400",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f400",
      "DATA",
      [
        "storage",
        "00c6b0d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f400) · [`0055f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f3b8) · [`0055f3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f3bc)
- 新版 [`0055f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f3e4.md#insn-0055f440) · [`0055f3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f3e4.md#insn-0055f3f8) · [`0055f3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f3e4.md#insn-0055f3fc)

~~~diff
- 0055f400 ["INT_ADD", "register:40f0:8", ["const:55f400:8", "const:4:8"]]
- 0055f400 ["CALL", null, ["callee:00c53d00:8"]]
+ 0055f440 ["INT_ADD", "register:40f0:8", ["const:55f440:8", "const:4:8"]]
+ 0055f440 ["CALL", null, ["callee:00c53d00:8"]]
- 0055f400 bytes 38d11b94
+ 0055f440 bytes 30d21b94
- 0055f3b8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055f3f8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055f3b8 bytes 483800f0
+ 0055f3f8 bytes 68380090
- 0055f3bc ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0055f3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f3fc ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 0055f3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f3bc bytes 08413391
+ 0055f3fc bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942daae869dadf3e084ed4608cd816b6"></a>

### [`0055f430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f430.md) → [`0055f470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f470.md) FUN_0055f470

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
      "definition_site": "0055f474",
      "incomplete_value": false,
      "site": "0055f478",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f434",
      "incomplete_value": false,
      "site": "0055f438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "0055f478",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f478",
      "DATA",
      [
        "storage",
        "00c6b148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f430.md#insn-0055f430) · [`0055f434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f430.md#insn-0055f434)
- 新版 [`0055f470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f470.md#insn-0055f470) · [`0055f474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f470.md#insn-0055f474)

~~~diff
- 0055f430 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055f470 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055f430 bytes 483800f0
+ 0055f470 bytes 68380090
- 0055f434 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0055f434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f474 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0055f474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f434 bytes 08213591
+ 0055f474 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c72c5b5e03bd66b3bb4cc4a716c57c"></a>

### [`0055f440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f440.md) → [`0055f480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f480.md) FUN_0055f480

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
      "definition_site": "0055f490",
      "incomplete_value": false,
      "site": "0055f498",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f450",
      "incomplete_value": false,
      "site": "0055f458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "0055f498",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f498",
      "DATA",
      [
        "storage",
        "00c6b148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f440.md#insn-0055f44c) · [`0055f450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f440.md#insn-0055f450) · [`0055f45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f440.md#insn-0055f45c)
- 新版 [`0055f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f480.md#insn-0055f48c) · [`0055f490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f480.md#insn-0055f490) · [`0055f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f480.md#insn-0055f49c)

~~~diff
- 0055f44c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0055f48c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055f44c bytes 483800f0
+ 0055f48c bytes 68380090
- 0055f450 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0055f450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f490 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0055f490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f450 bytes 08213591
+ 0055f490 bytes 08210591
- 0055f45c ["INT_ADD", "register:40f0:8", ["const:55f45c:8", "const:4:8"]]
- 0055f45c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0055f49c ["INT_ADD", "register:40f0:8", ["const:55f49c:8", "const:4:8"]]
+ 0055f49c ["CALL", null, ["callee:00c57ea0:8"]]
- 0055f45c bytes 91e11b94
+ 0055f49c bytes 81e21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c27590c737ff536865cb8aac01b9213"></a>

### [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) → [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) FUN_0055f4c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 18件 [`0048031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md) [`004805e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md) [`0048067c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 18件 [`0048035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/0048035c.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480484.md) [`00480628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480628.md) [`004806bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004806bc.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055f50c",
      "incomplete_value": true,
      "site": "0055f50c",
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
            "const:c74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f4cc",
      "incomplete_value": true,
      "site": "0055f4cc",
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
            "const:874:8"
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
      "definition_site": "0055f4f0",
      "incomplete_value": false,
      "site": "0055f4f4",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f4b0",
      "incomplete_value": false,
      "site": "0055f4b4",
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
            "const:878:8"
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
      "definition_site": "0055f508",
      "incomplete_value": false,
      "site": "0055f510",
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
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f4c8",
      "incomplete_value": false,
      "site": "0055f4d0",
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
            "const:878:8"
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
      "0055f4d4",
      "READ",
      [
        "storage",
        "00ca5878",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4e0",
      "READ",
      [
        "storage",
        "00ca5874",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4f0",
      "PARAM",
      [
        "storage",
        "00ca5878",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f4d4",
      "READ",
      [
        "storage",
        "00ca5c78",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4e0",
      "READ",
      [
        "storage",
        "00ca5c74",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4f0",
      "PARAM",
      [
        "storage",
        "00ca5c78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f490) · [`0055f4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f4b4) · [`0055f4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f4cc)
- 新版 [`0055f4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md#insn-0055f4d0) · [`0055f4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md#insn-0055f4f4) · [`0055f50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md#insn-0055f50c)

~~~diff
- 0055f490 ["COPY", "tmp:0:8", ["const:878:8"]]
- 0055f490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f4d0 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 0055f4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f490 bytes 08e12191
+ 0055f4d0 bytes 08e13191
- 0055f4b4 ["INT_ADD", "register:40f0:8", ["const:55f4b4:8", "const:4:8"]]
- 0055f4b4 ["CALL", null, ["callee:00c57e50:8"]]
+ 0055f4f4 ["INT_ADD", "register:40f0:8", ["const:55f4f4:8", "const:4:8"]]
+ 0055f4f4 ["CALL", null, ["callee:00c57e50:8"]]
- 0055f4b4 bytes 67e11b94
+ 0055f4f4 bytes 57e21b94
- 0055f4cc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0055f4cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:874:8"]]
- 0055f4cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0055f50c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0055f50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:c74:8"]]
+ 0055f50c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0055f4cc bytes 09d12139
+ 0055f50c bytes 09d13139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbe512d77e097af37b97d87473712fb1"></a>

### [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) → [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) FUN_0055f578

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) [`00a9f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md) · 呼出先 5件 [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 2件 [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md) [`00a9f41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9f41c.md) · 呼出先 5件 [`005603c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md) [`00560468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f5bc",
      "incomplete_value": true,
      "site": "0055f5c0",
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
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f57c",
      "incomplete_value": true,
      "site": "0055f580",
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
            "const:890:8"
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
      "definition_site": "0055f5d8",
      "incomplete_value": false,
      "site": "0055f5ec",
      "value": [
        "leaf",
        "const:560468:8"
      ]
    },
    "old": {
      "definition_site": "0055f598",
      "incomplete_value": false,
      "site": "0055f5ac",
      "value": [
        "leaf",
        "const:560428:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f5e0",
      "incomplete_value": false,
      "site": "0055f5ec",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f5a0",
      "incomplete_value": false,
      "site": "0055f5ac",
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
            "const:880:8"
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
      "0055f590",
      "READ",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f59c",
      "READ",
      [
        "storage",
        "00ca5880",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f5bc",
      "PARAM",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f590",
      "READ",
      [
        "storage",
        "00ca5c90",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f59c",
      "READ",
      [
        "storage",
        "00ca5c80",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f5bc",
      "PARAM",
      [
        "storage",
        "00ca5c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f580) · [`0055f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f5ac) · [`0055f5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f5b8)
- 新版 [`0055f5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md#insn-0055f5c0) · [`0055f5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md#insn-0055f5ec) · [`0055f5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md#insn-0055f5f8)

~~~diff
- 0055f580 ["INT_ADD", "register:40f0:8", ["const:55f580:8", "const:4:8"]]
- 0055f580 ["CALL", null, ["callee:00c57e50:8"]]
+ 0055f5c0 ["INT_ADD", "register:40f0:8", ["const:55f5c0:8", "const:4:8"]]
+ 0055f5c0 ["CALL", null, ["callee:00c57e50:8"]]
- 0055f580 bytes 34e11b94
+ 0055f5c0 bytes 24e21b94
- 0055f5ac ["INT_ADD", "register:40f0:8", ["const:55f5ac:8", "const:4:8"]]
- 0055f5ac ["CALL", null, ["callee:00c57e30:8"]]
+ 0055f5ec ["INT_ADD", "register:40f0:8", ["const:55f5ec:8", "const:4:8"]]
+ 0055f5ec ["CALL", null, ["callee:00c57e30:8"]]
- 0055f5ac bytes 21e11b94
+ 0055f5ec bytes 11e21b94
- 0055f5b8 ["INT_ADD", "register:40f0:8", ["const:55f5b8:8", "const:4:8"]]
- 0055f5b8 ["CALL", null, ["callee:00c57e70:8"]]
+ 0055f5f8 ["INT_ADD", "register:40f0:8", ["const:55f5f8:8", "const:4:8"]]
+ 0055f5f8 ["CALL", null, ["callee:00c57e70:8"]]
- 0055f5b8 bytes 2ee11b94
+ 0055f5f8 bytes 1ee21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bb9dcb6bf08e4ce4be7e0b81a3aa962"></a>

### [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) → [`0055f618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md) FUN_0055f618

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 5件 [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 5件 [`005603c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/005603c0.md) [`00560468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560468.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f664",
      "incomplete_value": false,
      "site": "0055f668",
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
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f624",
      "incomplete_value": false,
      "site": "0055f628",
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
            "const:890:8"
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
      "definition_site": "0055f680",
      "incomplete_value": false,
      "site": "0055f694",
      "value": [
        "leaf",
        "const:560468:8"
      ]
    },
    "old": {
      "definition_site": "0055f640",
      "incomplete_value": false,
      "site": "0055f654",
      "value": [
        "leaf",
        "const:560428:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f688",
      "incomplete_value": false,
      "site": "0055f694",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f648",
      "incomplete_value": false,
      "site": "0055f654",
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
            "const:880:8"
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
      "0055f630",
      "READ",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f644",
      "READ",
      [
        "storage",
        "00ca5880",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f664",
      "PARAM",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f630",
      "READ",
      [
        "storage",
        "00ca5c90",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f644",
      "READ",
      [
        "storage",
        "00ca5c80",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f664",
      "PARAM",
      [
        "storage",
        "00ca5c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f5e8) · [`0055f628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f628) · [`0055f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f654)
- 新版 [`0055f628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md#insn-0055f628) · [`0055f668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md#insn-0055f668) · [`0055f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f618.md#insn-0055f694)

~~~diff
- 0055f5e8 ["COPY", "tmp:0:8", ["const:890:8"]]
- 0055f5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f628 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 0055f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f5e8 bytes 08412291
+ 0055f628 bytes 08413291
- 0055f628 ["INT_ADD", "register:40f0:8", ["const:55f628:8", "const:4:8"]]
- 0055f628 ["CALL", null, ["callee:00c57e50:8"]]
+ 0055f668 ["INT_ADD", "register:40f0:8", ["const:55f668:8", "const:4:8"]]
+ 0055f668 ["CALL", null, ["callee:00c57e50:8"]]
- 0055f628 bytes 0ae11b94
+ 0055f668 bytes fae11b94
- 0055f654 ["INT_ADD", "register:40f0:8", ["const:55f654:8", "const:4:8"]]
- 0055f654 ["CALL", null, ["callee:00c57e30:8"]]
+ 0055f694 ["INT_ADD", "register:40f0:8", ["const:55f694:8", "const:4:8"]]
+ 0055f694 ["CALL", null, ["callee:00c57e30:8"]]
- 0055f654 bytes f7e01b94
+ 0055f694 bytes e7e11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c0329823f67a6edcf1140ff86de4e69"></a>

### [`0055f688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md) → [`0055f6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f6c8.md) FUN_0055f6c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0055f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0055f868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f770",
      "incomplete_value": true,
      "site": "0055f774",
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
      "definition_site": "0055f730",
      "incomplete_value": true,
      "site": "0055f734",
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
      "0055f6f8",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0055f700",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0055f714",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0055f6f8",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0055f700",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "0055f714",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f6b8) · [`0055f6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f6c0) · [`0055f700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f700)
- 新版 [`0055f6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f6c8.md#insn-0055f6f8) · [`0055f700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f6c8.md#insn-0055f700) · [`0055f740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f6c8.md#insn-0055f740)

~~~diff
- 0055f6b8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:888:8"]]
- 0055f6b8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055f6f8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c88:8"]]
+ 0055f6f8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0055f6b8 bytes 394744f9
+ 0055f6f8 bytes 394746f9
- 0055f6c0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:7b8:8"]]
- 0055f6c0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055f700 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:bb8:8"]]
+ 0055f700 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0055f6c0 bytes 18df43f9
+ 0055f700 bytes 18df45f9
- 0055f700 ["INT_ADD", "register:40f0:8", ["const:55f700:8", "const:4:8"]]
- 0055f700 ["CALL", null, ["callee:00c581e0:8"]]
+ 0055f740 ["INT_ADD", "register:40f0:8", ["const:55f740:8", "const:4:8"]]
+ 0055f740 ["CALL", null, ["callee:00c581e0:8"]]
- 0055f700 bytes b8e11b94
+ 0055f740 bytes a8e21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b5eaeae24914c6a9ef41b75499b8cc3"></a>

### [`0055f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md) → [`0055f868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f868.md) FUN_0055f868

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055f688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md) · 呼出先 6件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0055f6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f6c8.md) · 呼出先 6件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f8d4",
      "incomplete_value": true,
      "site": "0055f8d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f894",
      "incomplete_value": true,
      "site": "0055f898",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f930",
      "incomplete_value": true,
      "site": "0055f934",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f8f0",
      "incomplete_value": true,
      "site": "0055f8f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
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
      "definition_site": "0055f980",
      "incomplete_value": true,
      "site": "0055f984",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f940",
      "incomplete_value": true,
      "site": "0055f944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "0055f8d4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "0055f8d4",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0055f930",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f8d4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "0055f8d4",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0055f930",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f898) · [`0055f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f8b4) · [`0055f8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f8f4)
- 新版 [`0055f8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f868.md#insn-0055f8d8) · [`0055f8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f868.md#insn-0055f8f4) · [`0055f934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f868.md#insn-0055f934)

~~~diff
- 0055f898 ["INT_ADD", "register:40f0:8", ["const:55f898:8", "const:4:8"]]
- 0055f898 ["CALL", null, ["callee:00c58280:8"]]
+ 0055f8d8 ["INT_ADD", "register:40f0:8", ["const:55f8d8:8", "const:4:8"]]
+ 0055f8d8 ["CALL", null, ["callee:00c58280:8"]]
- 0055f898 bytes 7ae11b94
+ 0055f8d8 bytes 6ae21b94
- 0055f8b4 ["INT_ADD", "register:40f0:8", ["const:55f8b4:8", "const:4:8"]]
- 0055f8b4 ["CALL", null, ["callee:00c58290:8"]]
+ 0055f8f4 ["INT_ADD", "register:40f0:8", ["const:55f8f4:8", "const:4:8"]]
+ 0055f8f4 ["CALL", null, ["callee:00c58290:8"]]
- 0055f8b4 bytes 77e11b94
+ 0055f8f4 bytes 67e21b94
- 0055f8f4 ["INT_ADD", "register:40f0:8", ["const:55f8f4:8", "const:4:8"]]
- 0055f8f4 ["CALL", null, ["callee:00c58280:8"]]
+ 0055f934 ["INT_ADD", "register:40f0:8", ["const:55f934:8", "const:4:8"]]
+ 0055f934 ["CALL", null, ["callee:00c58280:8"]]
- 0055f8f4 bytes 63e11b94
+ 0055f934 bytes 53e21b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3419142ebe3aa834ef2fa5c7729c6577"></a>

### [`0055fc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md) → [`0055fc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md) FUN_0055fc7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "0055fcac",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055fc6c",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0055fcac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0055fcac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md#insn-0055fc6c) · [`0055fc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md#insn-0055fc90)
- 新版 [`0055fcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md#insn-0055fcac) · [`0055fcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md#insn-0055fcd0)

~~~diff
- 0055fc6c ["INT_ADD", "register:40f0:8", ["const:55fc6c:8", "const:4:8"]]
- 0055fc6c ["CALL", null, ["ram:46dac0:8"]]
+ 0055fcac ["INT_ADD", "register:40f0:8", ["const:55fcac:8", "const:4:8"]]
+ 0055fcac ["CALL", null, ["ram:46db00:8"]]
- 0055fc6c bytes 9537fc97
+ 0055fcac bytes 9537fc97
- 0055fc90 ["INT_ADD", "register:40f0:8", ["const:55fc90:8", "const:4:8"]]
- 0055fc90 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055fcd0 ["INT_ADD", "register:40f0:8", ["const:55fcd0:8", "const:4:8"]]
+ 0055fcd0 ["CALL", null, ["callee:00c57ee0:8"]]
- 0055fc90 bytes 94df1b94
+ 0055fcd0 bytes 84e01b94
~~~


<a id="compare-1b5821512034da25ae1258e9f33d35b9"></a>

### [`0055fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md) → [`0055fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md) FUN_0055fcd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "0055fd04",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055fcc4",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0055fd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0055fd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md#insn-0055fcc4) · [`0055fce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md#insn-0055fce8)
- 新版 [`0055fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md#insn-0055fd04) · [`0055fd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md#insn-0055fd28)

~~~diff
- 0055fcc4 ["INT_ADD", "register:40f0:8", ["const:55fcc4:8", "const:4:8"]]
- 0055fcc4 ["CALL", null, ["ram:46dac0:8"]]
+ 0055fd04 ["INT_ADD", "register:40f0:8", ["const:55fd04:8", "const:4:8"]]
+ 0055fd04 ["CALL", null, ["ram:46db00:8"]]
- 0055fcc4 bytes 7f37fc97
+ 0055fd04 bytes 7f37fc97
- 0055fce8 ["INT_ADD", "register:40f0:8", ["const:55fce8:8", "const:4:8"]]
- 0055fce8 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0055fd28 ["INT_ADD", "register:40f0:8", ["const:55fd28:8", "const:4:8"]]
+ 0055fd28 ["CALL", null, ["callee:00c57ee0:8"]]
- 0055fce8 bytes 7edf1b94
+ 0055fd28 bytes 6ee01b94
~~~


<a id="compare-5592caf19ffac6558c0461f4d1abcb82"></a>

### [`00560000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md) → [`00560040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560040.md) FUN_00560040

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055ff18.md) [`0059777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059777c.md) · 呼出先 4件 [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 2件 [`0055ff58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055ff58.md) [`005977bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005977bc.md) · 呼出先 4件 [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560084",
      "incomplete_value": true,
      "site": "00560084",
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
      "definition_site": "00560044",
      "incomplete_value": true,
      "site": "00560044",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056007c",
      "incomplete_value": true,
      "site": "00560088",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056003c",
      "incomplete_value": true,
      "site": "00560048",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00560094",
      "incomplete_value": true,
      "site": "00560094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "00560054",
      "incomplete_value": true,
      "site": "00560054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "00560064",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      "00560068",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "0056007c",
      "READ",
      [
        "storage",
        "00c92e78",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00560064",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00560068",
      "READ",
      [
        "storage",
        "00c9b288",
        null,
        "pointer"
      ]
    ],
    [
      "0056007c",
      "READ",
      [
        "storage",
        "00c93278",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-00560018) · [`0056001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-0056001c) · [`00560024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-00560024)
- 新版 [`00560058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560040.md#insn-00560058) · [`0056005c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560040.md#insn-0056005c) · [`00560064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560040.md#insn-00560064)

~~~diff
- 00560018 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 00560058 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 00560018 bytes d93900d0
+ 00560058 bytes d93900f0
- 0056001c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 0056005c ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 0056001c bytes d83900d0
+ 0056005c bytes d83900f0
- 00560024 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e90:8"]]
- 00560024 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00560064 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:290:8"]]
+ 00560064 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00560024 bytes 394b47f9
+ 00560064 bytes 394b41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f82bcc987be0a31fb90e967647a59d4"></a>

### [`0056012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md) → [`0056016c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056016c.md) FUN_0056016c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055ff18.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0055ff58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055ff58.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

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
      "definition_site": "005601dc",
      "incomplete_value": true,
      "site": "005601e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056019c",
      "incomplete_value": true,
      "site": "005601a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00560294",
      "incomplete_value": true,
      "site": "00560298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560254",
      "incomplete_value": true,
      "site": "00560258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "005601dc",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "005601dc",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00560294",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005601dc",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "005601dc",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00560294",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005601a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-005601a0) · [`00560258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-00560258) · [`00560190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-00560190)
- 新版 [`005601e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056016c.md#insn-005601e0) · [`00560298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056016c.md#insn-00560298) · [`005601d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056016c.md#insn-005601d0)

~~~diff
- 005601a0 ["INT_ADD", "register:40f0:8", ["const:5601a0:8", "const:4:8"]]
- 005601a0 ["CALL", null, ["callee:00c58280:8"]]
+ 005601e0 ["INT_ADD", "register:40f0:8", ["const:5601e0:8", "const:4:8"]]
+ 005601e0 ["CALL", null, ["callee:00c58280:8"]]
- 005601a0 bytes 38df1b94
+ 005601e0 bytes 28e01b94
- 00560258 ["INT_ADD", "register:40f0:8", ["const:560258:8", "const:4:8"]]
- 00560258 ["CALL", null, ["callee:00c58280:8"]]
+ 00560298 ["INT_ADD", "register:40f0:8", ["const:560298:8", "const:4:8"]]
+ 00560298 ["CALL", null, ["callee:00c58280:8"]]
- 00560258 bytes 0adf1b94
+ 00560298 bytes fadf1b94
- 00560190 ["INT_ADD", "register:40f0:8", ["const:560190:8", "const:4:8"]]
- 00560190 ["CALL", null, ["callee:00c58270:8"]]
+ 005601d0 ["INT_ADD", "register:40f0:8", ["const:5601d0:8", "const:4:8"]]
+ 005601d0 ["CALL", null, ["callee:00c58270:8"]]
- 00560190 bytes 38df1b94
+ 005601d0 bytes 28e01b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

