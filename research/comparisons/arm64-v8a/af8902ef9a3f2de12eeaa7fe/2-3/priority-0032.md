# v16.0.0 → v16.0.1 · 最優先の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-a154bc1bd26f77002c6241562a03d0d8"></a>

### [`006b7a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a48.md) → [`006b7a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7a88.md) FUN_006b7a88

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
      "definition_site": "006b7a9c",
      "incomplete_value": false,
      "site": "006b7aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7a5c",
      "incomplete_value": false,
      "site": "006b7a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "006b7aa0",
      "DATA",
      [
        "storage",
        "00c75b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b7aa0",
      "DATA",
      [
        "storage",
        "00c75f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a48.md#insn-006b7a54) · [`006b7a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a48.md#insn-006b7a5c)
- 新版 `006b7a94`（命令位置の公開資料なし） · `006b7a9c`（命令位置の公開資料なし）

~~~diff
- 006b7a54 ["INT_ADD", "register:40f0:8", ["const:6b7a54:8", "const:4:8"]]
- 006b7a54 ["CALL", null, ["callee:00c57e90:8"]]
+ 006b7a94 ["INT_ADD", "register:40f0:8", ["const:6b7a94:8", "const:4:8"]]
+ 006b7a94 ["CALL", null, ["callee:00c57e90:8"]]
- 006b7a54 bytes 0f801694
+ 006b7a94 bytes ff801694
- 006b7a5c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 006b7a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7a9c ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 006b7a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7a5c bytes 08812c91
+ 006b7a9c bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa9a20bcc181dfa3128455958ffec3d0"></a>

### [`006b7a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a6c.md) → [`006b7aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7aac.md) FUN_006b7aac

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
      "definition_site": "006b7ab0",
      "incomplete_value": false,
      "site": "006b7ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7a70",
      "incomplete_value": false,
      "site": "006b7a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "006b7ab4",
      "DATA",
      [
        "storage",
        "00c75b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b7ab4",
      "DATA",
      [
        "storage",
        "00c75f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a6c.md#insn-006b7a70)
- 新版 `006b7ab0`（命令位置の公開資料なし）

~~~diff
- 006b7a70 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 006b7a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7ab0 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 006b7ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7a70 bytes 08812c91
+ 006b7ab0 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e0de48ee16dba14155b6bdd23dca73"></a>

### [`006b7a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a84.md) → [`006b7ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7ac4.md) FUN_006b7ac4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "006b7ae0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b7aa0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006b7ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006b7ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a84.md#insn-006b7aa0) · [`006b7aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7a84.md#insn-006b7aac)
- 新版 `006b7ae0`（命令位置の公開資料なし） · `006b7aec`（命令位置の公開資料なし）

~~~diff
- 006b7aa0 ["INT_ADD", "register:40f0:8", ["const:6b7aa0:8", "const:4:8"]]
- 006b7aa0 ["CALL", null, ["ram:47acb4:8"]]
+ 006b7ae0 ["INT_ADD", "register:40f0:8", ["const:6b7ae0:8", "const:4:8"]]
+ 006b7ae0 ["CALL", null, ["ram:47acf4:8"]]
- 006b7aa0 bytes 850cf797
+ 006b7ae0 bytes 850cf797
- 006b7aac ["INT_ADD", "register:40f0:8", ["const:6b7aac:8", "const:4:8"]]
- 006b7aac ["CALL", null, ["callee:0047cdd4:8"]]
+ 006b7aec ["INT_ADD", "register:40f0:8", ["const:6b7aec:8", "const:4:8"]]
+ 006b7aec ["CALL", null, ["callee:0047cdd4:8"]]
- 006b7aac bytes ba14f797
+ 006b7aec bytes ba14f797
~~~


<a id="compare-9788a197dca1ac8b78c36b92aa8c26b3"></a>

### [`006b7b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b14.md) → [`006b7b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7b54.md) FUN_006b7b54

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
      "definition_site": "006b7b58",
      "incomplete_value": false,
      "site": "006b7b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7b18",
      "incomplete_value": false,
      "site": "006b7b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "006b7b5c",
      "DATA",
      [
        "storage",
        "00c75ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b7b5c",
      "DATA",
      [
        "storage",
        "00c75fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b14.md#insn-006b7b18)
- 新版 `006b7b58`（命令位置の公開資料なし）

~~~diff
- 006b7b18 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 006b7b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7b58 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 006b7b58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7b58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7b58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7b18 bytes 08812e91
+ 006b7b58 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c708fb411b6ea8fcc25e3f2b788931c"></a>

### [`006b7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b2c.md) → [`006b7b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7b6c.md) FUN_006b7b6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "006b7b88",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b7b48",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006b7b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006b7b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b2c.md#insn-006b7b48) · [`006b7b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b2c.md#insn-006b7b54)
- 新版 `006b7b88`（命令位置の公開資料なし） · `006b7b94`（命令位置の公開資料なし）

~~~diff
- 006b7b48 ["INT_ADD", "register:40f0:8", ["const:6b7b48:8", "const:4:8"]]
- 006b7b48 ["CALL", null, ["ram:47acb4:8"]]
+ 006b7b88 ["INT_ADD", "register:40f0:8", ["const:6b7b88:8", "const:4:8"]]
+ 006b7b88 ["CALL", null, ["ram:47acf4:8"]]
- 006b7b48 bytes 5b0cf797
+ 006b7b88 bytes 5b0cf797
- 006b7b54 ["INT_ADD", "register:40f0:8", ["const:6b7b54:8", "const:4:8"]]
- 006b7b54 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006b7b94 ["INT_ADD", "register:40f0:8", ["const:6b7b94:8", "const:4:8"]]
+ 006b7b94 ["CALL", null, ["callee:0047cdd4:8"]]
- 006b7b54 bytes 9014f797
+ 006b7b94 bytes 9014f797
~~~


<a id="compare-d818359a2a15b2b1aaecaaa1438cee8d"></a>

### [`006b7b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b98.md) → [`006b7bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7bd8.md) FUN_006b7bd8

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
      "definition_site": "006b7bfc",
      "incomplete_value": false,
      "site": "006b7bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7bbc",
      "incomplete_value": false,
      "site": "006b7bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
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
      "006b7bfc",
      "DATA",
      [
        "storage",
        "00c75c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b7bfc",
      "DATA",
      [
        "storage",
        "00c76020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b98.md#insn-006b7bac) · [`006b7bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b98.md#insn-006b7bb4) · [`006b7bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7b98.md#insn-006b7bb8)
- 新版 `006b7bec`（命令位置の公開資料なし） · `006b7bf4`（命令位置の公開資料なし） · `006b7bf8`（命令位置の公開資料なし）

~~~diff
- 006b7bac ["INT_ADD", "register:40f0:8", ["const:6b7bac:8", "const:4:8"]]
- 006b7bac ["CALL", null, ["callee:00c57e90:8"]]
+ 006b7bec ["INT_ADD", "register:40f0:8", ["const:6b7bec:8", "const:4:8"]]
+ 006b7bec ["CALL", null, ["callee:00c57e90:8"]]
- 006b7bac bytes b97f1694
+ 006b7bec bytes a9801694
- 006b7bb4 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b7bf4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b7bb4 bytes e82d00d0
+ 006b7bf4 bytes e82d00f0
- 006b7bb8 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 006b7bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7bf8 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 006b7bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7bb8 bytes 08813091
+ 006b7bf8 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de6644fc1e20b936d35f5859e04050a6"></a>

### [`006b7bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7bcc.md) → [`006b7c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7c0c.md) FUN_006b7c0c

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
      "definition_site": "006b7c10",
      "incomplete_value": false,
      "site": "006b7c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7bd0",
      "incomplete_value": false,
      "site": "006b7bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
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
      "006b7c14",
      "DATA",
      [
        "storage",
        "00c75c20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b7c14",
      "DATA",
      [
        "storage",
        "00c76020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7bcc.md#insn-006b7bcc) · [`006b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7bcc.md#insn-006b7bd0)
- 新版 `006b7c0c`（命令位置の公開資料なし） · `006b7c10`（命令位置の公開資料なし）

~~~diff
- 006b7bcc ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b7c0c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b7bcc bytes e82d00d0
+ 006b7c0c bytes e82d00f0
- 006b7bd0 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 006b7bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7c10 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 006b7c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7bd0 bytes 08813091
+ 006b7c10 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1529e7a8e7760cadf913f2efd2f066c6"></a>

### [`006b7c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7c1c.md) → [`006b7c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7c5c.md) FUN_006b7c5c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006b7bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7bec.md) [`006b80a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b80a8.md) [`006b8130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8130.md) [`006b81b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b81b8.md) · 呼出先 10件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`006b7c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7c2c.md) [`006b80e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80e8.md) [`006b8170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8170.md) [`006b81f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b81f8.md) · 呼出先 10件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.95% / 新版 89.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b7cc8",
      "incomplete_value": true,
      "site": "006b7cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:354:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7c88",
      "incomplete_value": true,
      "site": "006b7c88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:287:8"
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
      "definition_site": "006b7d28",
      "incomplete_value": true,
      "site": "006b7d38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7ce8",
      "incomplete_value": true,
      "site": "006b7cf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:21c:8"
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
      "definition_site": "006b7d2c",
      "incomplete_value": true,
      "site": "006b7d3c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006b7cec",
      "incomplete_value": true,
      "site": "006b7cfc",
      "value": [
        "LOAD",
        "16",
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
      "006b7c9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84a90"
      ]
    ],
    [
      "006b7cb4",
      "READ",
      [
        "storage",
        "002a2287",
        null,
        "string"
      ]
    ],
    [
      "006b7d28",
      "READ",
      [
        "storage",
        "0029f21c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b7c9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84c88"
      ]
    ],
    [
      "006b7cb4",
      "READ",
      [
        "storage",
        "002a2354",
        null,
        "string"
      ]
    ],
    [
      "006b7d28",
      "READ",
      [
        "storage",
        "0029f2e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7c1c.md#insn-006b7c5c) · [`006b7d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7c1c.md#insn-006b7d68) · [`006b7c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7c1c.md#insn-006b7c50)
- 新版 `006b7c9c`（命令位置の公開資料なし） · `006b7da8`（命令位置の公開資料なし） · `006b7c90`（命令位置の公開資料なし）

~~~diff
- 006b7c5c ["INT_ADD", "register:40f0:8", ["const:6b7c5c:8", "const:4:8"]]
- 006b7c5c ["CALL", null, ["ram:a84a90:8"]]
+ 006b7c9c ["INT_ADD", "register:40f0:8", ["const:6b7c9c:8", "const:4:8"]]
+ 006b7c9c ["CALL", null, ["ram:a84c88:8"]]
- 006b7c5c bytes 8d330f94
+ 006b7c9c bytes fb330f94
- 006b7d68 ["INT_ADD", "register:40f0:8", ["const:6b7d68:8", "const:4:8"]]
- 006b7d68 ["CALL", null, ["ram:a84b00:8"]]
+ 006b7da8 ["INT_ADD", "register:40f0:8", ["const:6b7da8:8", "const:4:8"]]
+ 006b7da8 ["CALL", null, ["ram:a84cf8:8"]]
- 006b7d68 bytes 66330f94
+ 006b7da8 bytes d4330f94
- 006b7c50 ["INT_ADD", "register:40f0:8", ["const:6b7c50:8", "const:4:8"]]
- 006b7c50 ["CALL", null, ["callee:008514f8:8"]]
+ 006b7c90 ["INT_ADD", "register:40f0:8", ["const:6b7c90:8", "const:4:8"]]
+ 006b7c90 ["CALL", null, ["callee:008514f8:8"]]
- 006b7c50 bytes 1a660694
+ 006b7c90 bytes 1a660694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15ed7cb2866d09557c397c3620a768a"></a>

### [`006b8054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8054.md) → [`006b8094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8094.md) FUN_006b8094

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
      "definition_site": "006b80b8",
      "incomplete_value": false,
      "site": "006b80b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8078",
      "incomplete_value": false,
      "site": "006b8078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "006b80b8",
      "DATA",
      [
        "storage",
        "00c75ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b80b8",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8054.md#insn-006b8068) · [`006b8070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8054.md#insn-006b8070) · [`006b8074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8054.md#insn-006b8074)
- 新版 `006b80a8`（命令位置の公開資料なし） · `006b80b0`（命令位置の公開資料なし） · `006b80b4`（命令位置の公開資料なし）

~~~diff
- 006b8068 ["INT_ADD", "register:40f0:8", ["const:6b8068:8", "const:4:8"]]
- 006b8068 ["CALL", null, ["callee:00c57e90:8"]]
+ 006b80a8 ["INT_ADD", "register:40f0:8", ["const:6b80a8:8", "const:4:8"]]
+ 006b80a8 ["CALL", null, ["callee:00c57e90:8"]]
- 006b8068 bytes 8a7e1694
+ 006b80a8 bytes 7a7f1694
- 006b8070 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b80b0 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b8070 bytes e82d00b0
+ 006b80b0 bytes e82d00d0
- 006b8074 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 006b8074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b8074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b8074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b80b4 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 006b80b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b80b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b80b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b8074 bytes 08813291
+ 006b80b4 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d65814f0accda6c179411ec7693c7267"></a>

### [`006b8088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8088.md) → [`006b80c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80c8.md) FUN_006b80c8

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
      "definition_site": "006b80cc",
      "incomplete_value": false,
      "site": "006b80d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b808c",
      "incomplete_value": false,
      "site": "006b8090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "006b80d0",
      "DATA",
      [
        "storage",
        "00c75ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b80d0",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8088.md#insn-006b8088) · [`006b808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8088.md#insn-006b808c)
- 新版 `006b80c8`（命令位置の公開資料なし） · `006b80cc`（命令位置の公開資料なし）

~~~diff
- 006b8088 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b80c8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b8088 bytes e82d00b0
+ 006b80c8 bytes e82d00d0
- 006b808c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 006b808c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b808c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b808c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b80cc ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 006b80cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b80cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b80cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b808c bytes 08813291
+ 006b80cc bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b053aeee5823a3b9a4d659d9f788d9"></a>

### [`006b80dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b80dc.md) → [`006b811c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b811c.md) FUN_006b811c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8140",
      "incomplete_value": true,
      "site": "006b8140",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8100",
      "incomplete_value": true,
      "site": "006b8100",
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
            "const:d20:8"
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
      "006b8140",
      "DATA",
      [
        "storage",
        "00c75d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b8140",
      "DATA",
      [
        "storage",
        "00c76120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b80f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b80dc.md#insn-006b80f0) · [`006b80f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b80dc.md#insn-006b80f8) · [`006b80fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b80dc.md#insn-006b80fc)
- 新版 `006b8130`（命令位置の公開資料なし） · `006b8138`（命令位置の公開資料なし） · `006b813c`（命令位置の公開資料なし）

~~~diff
- 006b80f0 ["INT_ADD", "register:40f0:8", ["const:6b80f0:8", "const:4:8"]]
- 006b80f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 006b8130 ["INT_ADD", "register:40f0:8", ["const:6b8130:8", "const:4:8"]]
+ 006b8130 ["CALL", null, ["callee:00c57e90:8"]]
- 006b80f0 bytes 687e1694
+ 006b8130 bytes 587f1694
- 006b80f8 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b8138 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b80f8 bytes e82d00b0
+ 006b8138 bytes e82d00d0
- 006b80fc ["COPY", "tmp:0:8", ["const:d20:8"]]
- 006b80fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b80fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b80fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b813c ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006b813c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b813c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b813c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b80fc bytes 08813491
+ 006b813c bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4717373c14b26da95df8578b5da0375d"></a>

### [`006b8110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8110.md) → [`006b8150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8150.md) FUN_006b8150

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
      "definition_site": "006b8154",
      "incomplete_value": false,
      "site": "006b8158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8114",
      "incomplete_value": false,
      "site": "006b8118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "006b8158",
      "DATA",
      [
        "storage",
        "00c75d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b8158",
      "DATA",
      [
        "storage",
        "00c76120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8110.md#insn-006b8110) · [`006b8114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8110.md#insn-006b8114)
- 新版 `006b8150`（命令位置の公開資料なし） · `006b8154`（命令位置の公開資料なし）

~~~diff
- 006b8110 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b8150 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b8110 bytes e82d00b0
+ 006b8150 bytes e82d00d0
- 006b8114 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 006b8114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b8114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b8114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b8154 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006b8154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b8114 bytes 08813491
+ 006b8154 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361c36d6e15e478acbada0d981fe17f5"></a>

### [`006b8164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8164.md) → [`006b81a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b81a4.md) FUN_006b81a4

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
      "definition_site": "006b81c8",
      "incomplete_value": false,
      "site": "006b81c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8188",
      "incomplete_value": false,
      "site": "006b8188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "006b81c8",
      "DATA",
      [
        "storage",
        "00c75da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b81c8",
      "DATA",
      [
        "storage",
        "00c761a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8164.md#insn-006b8178) · [`006b8180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8164.md#insn-006b8180) · [`006b8184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8164.md#insn-006b8184)
- 新版 `006b81b8`（命令位置の公開資料なし） · `006b81c0`（命令位置の公開資料なし） · `006b81c4`（命令位置の公開資料なし）

~~~diff
- 006b8178 ["INT_ADD", "register:40f0:8", ["const:6b8178:8", "const:4:8"]]
- 006b8178 ["CALL", null, ["callee:00c57e90:8"]]
+ 006b81b8 ["INT_ADD", "register:40f0:8", ["const:6b81b8:8", "const:4:8"]]
+ 006b81b8 ["CALL", null, ["callee:00c57e90:8"]]
- 006b8178 bytes 467e1694
+ 006b81b8 bytes 367f1694
- 006b8180 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b81c0 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b8180 bytes e82d00b0
+ 006b81c0 bytes e82d00d0
- 006b8184 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006b8184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b8184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b8184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b81c4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 006b81c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b81c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b81c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b8184 bytes 08813691
+ 006b81c4 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9da776223171fd3a23f30a3ef1b4a69"></a>

### [`006b8198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8198.md) → [`006b81d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b81d8.md) FUN_006b81d8

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
      "definition_site": "006b81dc",
      "incomplete_value": false,
      "site": "006b81e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b819c",
      "incomplete_value": false,
      "site": "006b81a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "006b81e0",
      "DATA",
      [
        "storage",
        "00c75da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b81e0",
      "DATA",
      [
        "storage",
        "00c761a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8198.md#insn-006b8198) · [`006b819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8198.md#insn-006b819c)
- 新版 `006b81d8`（命令位置の公開資料なし） · `006b81dc`（命令位置の公開資料なし）

~~~diff
- 006b8198 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006b81d8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b8198 bytes e82d00b0
+ 006b81d8 bytes e82d00d0
- 006b819c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 006b819c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b819c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b819c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b81dc ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 006b81dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b81dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b81dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b819c bytes 08813691
+ 006b81dc bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f685f8e323ecab128b1cf7a0f15ce38"></a>

### [`006b81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b81e8.md) → [`006b8228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8228.md) _INIT_105

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8264",
      "incomplete_value": true,
      "site": "006b8280",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8224",
      "incomplete_value": true,
      "site": "006b8240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "006b8288",
      "incomplete_value": true,
      "site": "006b82a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b8248",
      "incomplete_value": true,
      "site": "006b8264",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b82a8",
      "incomplete_value": true,
      "site": "006b82c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b8268",
      "incomplete_value": true,
      "site": "006b8284",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b8264",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006b8288",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006b82a8",
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
      "006b8264",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006b8288",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006b82a8",
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

- 旧版 [`006b8260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b81e8.md#insn-006b8260) · [`006b8280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b81e8.md#insn-006b8280) · [`006b841c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b81e8.md#insn-006b841c)
- 新版 `006b82a0`（命令位置の公開資料なし） · `006b82c0`（命令位置の公開資料なし） · `006b845c`（命令位置の公開資料なし）

~~~diff
- 006b8260 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 006b8260 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006b8260 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006b8260 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006b82a0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006b82a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006b82a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006b82a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006b8260 bytes 4a093691
+ 006b82a0 bytes 4a093791
- 006b8280 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006b8280 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006b8280 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006b8280 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006b82c0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006b82c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006b82c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006b82c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006b8280 bytes 4a553a91
+ 006b82c0 bytes 4a893d91
- 006b841c ["INT_ADD", "register:40f0:8", ["const:6b841c:8", "const:4:8"]]
- 006b841c ["CALL", null, ["callee:00c57e30:8"]]
+ 006b845c ["INT_ADD", "register:40f0:8", ["const:6b845c:8", "const:4:8"]]
+ 006b845c ["CALL", null, ["callee:00c57e30:8"]]
- 006b841c bytes 857d1694
+ 006b845c bytes 757e1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9234c453a81a6b58140eaa8c791b00"></a>

### [`006b8578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md) → [`006b85b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b85b8.md) FUN_006b85b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 20件 [`00440b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440b3c.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 20件 [`00440b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b7c.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b85f8",
      "incomplete_value": false,
      "site": "006b8600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b85b8",
      "incomplete_value": false,
      "site": "006b85c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "006b8614",
      "incomplete_value": true,
      "site": "006b8620",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:307:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b85d4",
      "incomplete_value": true,
      "site": "006b85e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:23a:8"
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
      "definition_site": "006b88c8",
      "incomplete_value": true,
      "site": "006b88d4",
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
      "definition_site": "006b8888",
      "incomplete_value": true,
      "site": "006b8894",
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
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b8600",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006b8614",
      "READ",
      [
        "storage",
        "0029f23a",
        null,
        "string"
      ]
    ],
    [
      "006b884c",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006b8600",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006b8614",
      "READ",
      [
        "storage",
        "0029f307",
        null,
        "string"
      ]
    ],
    [
      "006b884c",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b88d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md#insn-006b88d4) · [`006b85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md#insn-006b85b0) · [`006b85b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md#insn-006b85b8)
- 新版 `006b8914`（命令位置の公開資料なし） · `006b85f0`（命令位置の公開資料なし） · `006b85f8`（命令位置の公開資料なし）

~~~diff
- 006b88d4 ["INT_ADD", "register:40f0:8", ["const:6b88d4:8", "const:4:8"]]
- 006b88d4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 006b8914 ["INT_ADD", "register:40f0:8", ["const:6b8914:8", "const:4:8"]]
+ 006b8914 ["CALL", null, ["callee:00c57fb0:8"]]
- 006b88d4 bytes b77c1694
+ 006b8914 bytes a77d1694
- 006b85b0 ["INT_ADD", "register:40f0:8", ["const:6b85b0:8", "const:4:8"]]
- 006b85b0 ["CALL", null, ["callee:00487e20:8"]]
+ 006b85f0 ["INT_ADD", "register:40f0:8", ["const:6b85f0:8", "const:4:8"]]
+ 006b85f0 ["CALL", null, ["callee:00487e20:8"]]
- 006b85b0 bytes 0c3ef797
+ 006b85f0 bytes 0c3ef797
- 006b85b8 ["COPY", "tmp:0:8", ["const:938:8"]]
- 006b85b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b85b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b85b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b85f8 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 006b85f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b85f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b85f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b85b8 bytes 08e12491
+ 006b85f8 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccb1bb05cad0dd91c32c3e20aab9a8f4"></a>

### [`006b8a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md) → [`006b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8a64.md) FUN_006b8a64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006b8b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8b3c.md) [`006b8b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8b9c.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 5件 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)
- 新版 呼出元 3件 [`006b8b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8b7c.md) [`006b8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8bdc.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 5件 [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "site": "006b8b50",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b8b10",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "006b8ab4",
      "DATA",
      [
        "storage",
        "00436304",
        null,
        "byte[63]"
      ]
    ],
    [
      "006b8acc",
      "DATA",
      [
        "storage",
        "00436304",
        null,
        "byte[63]"
      ]
    ],
    [
      "006b8b50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "006b8ab4",
      "DATA",
      [
        "storage",
        "00436304",
        null,
        "uleb128"
      ]
    ],
    [
      "006b8acc",
      "DATA",
      [
        "storage",
        "00436304",
        null,
        "uleb128"
      ]
    ],
    [
      "006b8b50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md#insn-006b8b10) · [`006b8a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md#insn-006b8a70) · [`006b8a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8a24.md#insn-006b8a88)
- 新版 `006b8b50`（命令位置の公開資料なし） · `006b8ab0`（命令位置の公開資料なし） · `006b8ac8`（命令位置の公開資料なし）

~~~diff
- 006b8b10 ["INT_ADD", "register:40f0:8", ["const:6b8b10:8", "const:4:8"]]
- 006b8b10 ["CALL", null, ["ram:a65bf4:8"]]
+ 006b8b50 ["INT_ADD", "register:40f0:8", ["const:6b8b50:8", "const:4:8"]]
+ 006b8b50 ["CALL", null, ["ram:a65dec:8"]]
- 006b8b10 bytes 39b40e94
+ 006b8b50 bytes a7b40e94
- 006b8a70 ["INT_ADD", "register:40f0:8", ["const:6b8a70:8", "const:4:8"]]
- 006b8a70 ["CALL", null, ["callee:008514f8:8"]]
+ 006b8ab0 ["INT_ADD", "register:40f0:8", ["const:6b8ab0:8", "const:4:8"]]
+ 006b8ab0 ["CALL", null, ["callee:008514f8:8"]]
- 006b8a70 bytes 92620694
+ 006b8ab0 bytes 92620694
- 006b8a88 ["INT_ADD", "register:40f0:8", ["const:6b8a88:8", "const:4:8"]]
- 006b8a88 ["CALL", null, ["callee:008514f8:8"]]
+ 006b8ac8 ["INT_ADD", "register:40f0:8", ["const:6b8ac8:8", "const:4:8"]]
+ 006b8ac8 ["CALL", null, ["callee:008514f8:8"]]
- 006b8a88 bytes 8c620694
+ 006b8ac8 bytes 8c620694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d68a785c3d9aaeb0a208a54938d3cdf0"></a>

### [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) → [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) FUN_006b8c44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`006b8578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md) [`006b8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c18.md) [`006b8f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8f20.md) [`006b99a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b9/006b99a4.md) [`006ba500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ba/006ba500.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 17件 [`006b85b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b85b8.md) [`006b8c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c58.md) [`006b8f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8f60.md) [`006b99e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b9/006b99e4.md) [`006ba540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba540.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "006b8c50",
      "incomplete_value": false,
      "site": "006b8c54",
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
      "definition_site": "006b8c10",
      "incomplete_value": false,
      "site": "006b8c14",
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
      "006b8c50",
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
      "006b8c50",
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

- 旧版 [`006b8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md#insn-006b8c14) · [`006b8c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md#insn-006b8c10)
- 新版 `006b8c54`（命令位置の公開資料なし） · `006b8c50`（命令位置の公開資料なし）

~~~diff
- 006b8c14 ["INT_ADD", "register:40f0:8", ["const:6b8c14:8", "const:4:8"]]
- 006b8c14 ["CALL", null, ["callee:0043b778:8"]]
+ 006b8c54 ["INT_ADD", "register:40f0:8", ["const:6b8c54:8", "const:4:8"]]
+ 006b8c54 ["CALL", null, ["callee:0043b778:8"]]
- 006b8c14 bytes c90af697
+ 006b8c54 bytes c90af697
- 006b8c10 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 006b8c10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b8c10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b8c10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006b8c50 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 006b8c50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8c50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8c50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b8c10 bytes 00303c91
+ 006b8c50 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca826292f04ebbf7ae234c65d500ba0d"></a>

### [`006b8f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8f0c.md) → [`006b8f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8f4c.md) FUN_006b8f4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c18.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`006b8c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c58.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "006b8f58",
      "incomplete_value": false,
      "site": "006b8f5c",
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
      "definition_site": "006b8f18",
      "incomplete_value": false,
      "site": "006b8f1c",
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
      "006b8f58",
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
      "006b8f58",
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

- 旧版 [`006b8f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8f0c.md#insn-006b8f1c) · [`006b8f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8f0c.md#insn-006b8f18)
- 新版 `006b8f5c`（命令位置の公開資料なし） · `006b8f58`（命令位置の公開資料なし）

~~~diff
- 006b8f1c ["INT_ADD", "register:40f0:8", ["const:6b8f1c:8", "const:4:8"]]
- 006b8f1c ["CALL", null, ["callee:0043b778:8"]]
+ 006b8f5c ["INT_ADD", "register:40f0:8", ["const:6b8f5c:8", "const:4:8"]]
+ 006b8f5c ["CALL", null, ["callee:0043b778:8"]]
- 006b8f1c bytes 070af697
+ 006b8f5c bytes 070af697
- 006b8f18 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 006b8f18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b8f18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b8f18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006b8f58 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 006b8f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006b8f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b8f18 bytes 00303c91
+ 006b8f58 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a726bb6a5c319537d1b6eb632ca29e0"></a>

### [`006bb324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb324.md) → [`006bb364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bb364.md) _INIT_106

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb3a0",
      "incomplete_value": true,
      "site": "006bb3bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb360",
      "incomplete_value": true,
      "site": "006bb37c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "006bb3c4",
      "incomplete_value": true,
      "site": "006bb3e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006bb384",
      "incomplete_value": true,
      "site": "006bb3a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006bb420",
      "incomplete_value": true,
      "site": "006bb43c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb3e0",
      "incomplete_value": true,
      "site": "006bb3fc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:592:8"
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
      "006bb3a0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006bb3c4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006bb3e4",
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
      "006bb3a0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006bb3c4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006bb3e4",
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

- 旧版 [`006bb3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb324.md#insn-006bb3bc) · [`006bb558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb324.md#insn-006bb558) · [`006bb350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb324.md#insn-006bb350)
- 新版 `006bb3fc`（命令位置の公開資料なし） · `006bb598`（命令位置の公開資料なし） · `006bb390`（命令位置の公開資料なし）

~~~diff
- 006bb3bc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006bb3bc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006bb3bc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006bb3bc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006bb3fc ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006bb3fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb3fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb3fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006bb3bc bytes 4a553a91
+ 006bb3fc bytes 4a893d91
- 006bb558 ["INT_ADD", "register:40f0:8", ["const:6bb558:8", "const:4:8"]]
- 006bb558 ["CALL", null, ["callee:00c57e30:8"]]
+ 006bb598 ["INT_ADD", "register:40f0:8", ["const:6bb598:8", "const:4:8"]]
+ 006bb598 ["CALL", null, ["callee:00c57e30:8"]]
- 006bb558 bytes 36711694
+ 006bb598 bytes 26721694
- 006bb350 ["COPY", "tmp:0:8", ["const:330:8"]]
- 006bb350 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006bb350 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006bb350 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006bb390 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 006bb390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006bb390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006bb390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006bb350 bytes 73c20c91
+ 006bb390 bytes 73c21c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514dcb1f1860ff599858868356ea2f67"></a>

### [`006bb8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb8c8.md) → [`006bb908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bb908.md) _INIT_107

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb944",
      "incomplete_value": true,
      "site": "006bb960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb904",
      "incomplete_value": true,
      "site": "006bb920",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "006bb968",
      "incomplete_value": true,
      "site": "006bb984",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006bb928",
      "incomplete_value": true,
      "site": "006bb944",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006bb988",
      "incomplete_value": true,
      "site": "006bb9a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006bb948",
      "incomplete_value": true,
      "site": "006bb964",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bb944",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006bb968",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006bb988",
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
      "006bb944",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006bb968",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006bb988",
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

- 旧版 [`006bb940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb8c8.md#insn-006bb940) · [`006bb960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb8c8.md#insn-006bb960) · [`006bba28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bb8c8.md#insn-006bba28)
- 新版 `006bb980`（命令位置の公開資料なし） · `006bb9a0`（命令位置の公開資料なし） · `006bba68`（命令位置の公開資料なし）

~~~diff
- 006bb940 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 006bb940 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006bb940 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006bb940 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006bb980 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006bb980 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb980 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb980 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006bb940 bytes 4a093691
+ 006bb980 bytes 4a093791
- 006bb960 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006bb960 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006bb960 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006bb960 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006bb9a0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006bb9a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb9a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006bb9a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006bb960 bytes 4a553a91
+ 006bb9a0 bytes 4a893d91
- 006bba28 ["INT_ADD", "register:40f0:8", ["const:6bba28:8", "const:4:8"]]
- 006bba28 ["CALL", null, ["callee:0043b7f8:8"]]
+ 006bba68 ["INT_ADD", "register:40f0:8", ["const:6bba68:8", "const:4:8"]]
+ 006bba68 ["CALL", null, ["callee:0043b7f8:8"]]
- 006bba28 bytes 64fff597
+ 006bba68 bytes 64fff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8037e11617aa534bead4f6c4f8ef7c40"></a>

### [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) → [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) FUN_006bbc98

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006788a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0092472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) · 呼出先 105件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md)
- 新版 呼出元 4件 [`006788e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00678/006788e0.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`009248c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00924/009248c8.md) · 呼出先 105件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 20件, `store_destination` 7件, `store_value` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bcbb8",
      "incomplete_value": true,
      "site": "006bcbd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bcb78",
      "incomplete_value": true,
      "site": "006bcb90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 136,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bd538",
      "incomplete_value": true,
      "site": "006bd544",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bd4f8",
      "incomplete_value": true,
      "site": "006bd504",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 224,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bde70",
      "incomplete_value": true,
      "site": "006bde7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bde30",
      "incomplete_value": true,
      "site": "006bde3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 345,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bbe2c",
      "DATA",
      [
        "storage",
        "0039badc",
        "fde_0039badc",
        "dword"
      ]
    ],
    [
      "006bbe34",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ],
    [
      "006bbe44",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "006bbe2c",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "uleb128"
      ]
    ],
    [
      "006bbe34",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "006bbe44",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bbe64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md#insn-006bbe64) · [`006bbea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md#insn-006bbea4) · [`006bbef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md#insn-006bbef4)
- 新版 `006bbea4`（命令位置の公開資料なし） · `006bbee4`（命令位置の公開資料なし） · `006bbf34`（命令位置の公開資料なし）

~~~diff
- 006bbe64 ["INT_ADD", "register:40f0:8", ["const:6bbe64:8", "const:4:8"]]
- 006bbe64 ["CALL", null, ["callee:0043ddd8:8"]]
+ 006bbea4 ["INT_ADD", "register:40f0:8", ["const:6bbea4:8", "const:4:8"]]
+ 006bbea4 ["CALL", null, ["callee:0043ddd8:8"]]
- 006bbe64 bytes cd07f697
+ 006bbea4 bytes cd07f697
- 006bbea4 ["INT_ADD", "register:40f0:8", ["const:6bbea4:8", "const:4:8"]]
- 006bbea4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006bbee4 ["INT_ADD", "register:40f0:8", ["const:6bbee4:8", "const:4:8"]]
+ 006bbee4 ["CALL", null, ["callee:00c57eb0:8"]]
- 006bbea4 bytes 036f1694
+ 006bbee4 bytes f36f1694
- 006bbef4 ["INT_ADD", "register:40f0:8", ["const:6bbef4:8", "const:4:8"]]
- 006bbef4 ["CALL", null, ["ram:47acb4:8"]]
+ 006bbf34 ["INT_ADD", "register:40f0:8", ["const:6bbf34:8", "const:4:8"]]
+ 006bbf34 ["CALL", null, ["ram:47acf4:8"]]
- 006bbef4 bytes 70fbf697
+ 006bbf34 bytes 70fbf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58ee42364cafbcf7faeaae1160265b1e"></a>

### [`006be9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006be9ac.md) → [`006be9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006be9ec.md) FUN_006be9ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 5件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`006c0068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0068.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 2件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 5件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`006c00a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c00a8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 8件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006be9fc",
      "incomplete_value": false,
      "site": "006be9fc",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006be9bc",
      "incomplete_value": false,
      "site": "006be9bc",
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
            "const:568:8"
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
      "definition_site": "006bea5c",
      "incomplete_value": false,
      "site": "006bea5c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "006bea1c",
      "incomplete_value": false,
      "site": "006bea1c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bea60",
      "incomplete_value": false,
      "site": "006bea60",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bea20",
      "incomplete_value": false,
      "site": "006bea20",
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
            "const:b00:8"
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
      "006be9f8",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "006be9fc",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "006bea18",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006be9f8",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "006be9fc",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "006bea18",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006be9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006be9ac.md#insn-006be9b8) · [`006be9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006be9ac.md#insn-006be9bc) · [`006be9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006be9ac.md#insn-006be9f4)
- 新版 `006be9f8`（命令位置の公開資料なし） · `006be9fc`（命令位置の公開資料なし） · `006bea34`（命令位置の公開資料なし）

~~~diff
- 006be9b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 006be9b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006be9f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 006be9f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006be9b8 bytes 00b542f9
+ 006be9f8 bytes 00b544f9
- 006be9bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 006be9bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 006be9bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 006be9fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 006be9fc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 006be9fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 006be9bc bytes 1fb502f9
+ 006be9fc bytes 1fb504f9
- 006be9f4 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 006be9f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006be9f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006be9f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006bea34 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 006bea34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006bea34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006bea34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006be9f4 bytes 00e02c91
+ 006bea34 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a2c1b7fb33d865a831aa28dd5ea250d"></a>

### [`006bed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md) → [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) FUN_006bed5c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 24件 [`005e486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e486c.md) [`005e4dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4dd8.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`006bffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bffdc.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)
- 新版 呼出元 1件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) · 呼出先 24件 [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e18.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`006c001c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c001c.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 19件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006beddc",
      "incomplete_value": false,
      "site": "006bede4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bed9c",
      "incomplete_value": false,
      "site": "006beda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:ab4:8"
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
      "definition_site": "006bee04",
      "incomplete_value": false,
      "site": "006bee10",
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
            "const:56e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bedc4",
      "incomplete_value": false,
      "site": "006bedd0",
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
            "const:52e:8"
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
      "definition_site": "006bee3c",
      "incomplete_value": false,
      "site": "006bee40",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bedfc",
      "incomplete_value": false,
      "site": "006bee00",
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
            "const:e08:8"
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
      "006bede4",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "006bee10",
      "DATA",
      [
        "storage",
        "002b752e",
        null,
        "string"
      ]
    ],
    [
      "006bee40",
      "DATA",
      [
        "storage",
        "002b1e08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006bede4",
      "DATA",
      [
        "storage",
        "002aeaf4",
        null,
        "string"
      ]
    ],
    [
      "006bee10",
      "DATA",
      [
        "storage",
        "002b756e",
        null,
        "string"
      ]
    ],
    [
      "006bee40",
      "DATA",
      [
        "storage",
        "002b1e48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bee38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md#insn-006bee38) · [`006bee64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md#insn-006bee64) · [`006beedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md#insn-006beedc)
- 新版 `006bee78`（命令位置の公開資料なし） · `006beea4`（命令位置の公開資料なし） · `006bef1c`（命令位置の公開資料なし）

~~~diff
- 006bee38 ["INT_ADD", "register:40f0:8", ["const:6bee38:8", "const:4:8"]]
- 006bee38 ["CALL", null, ["callee:00c5a830:8"]]
+ 006bee78 ["INT_ADD", "register:40f0:8", ["const:6bee78:8", "const:4:8"]]
+ 006bee78 ["CALL", null, ["callee:00c5a830:8"]]
- 006bee38 bytes 7e6d1694
+ 006bee78 bytes 6e6e1694
- 006bee64 ["INT_ADD", "register:40f0:8", ["const:6bee64:8", "const:4:8"]]
- 006bee64 ["CALL", null, ["callee:00c5a830:8"]]
+ 006beea4 ["INT_ADD", "register:40f0:8", ["const:6beea4:8", "const:4:8"]]
+ 006beea4 ["CALL", null, ["callee:00c5a830:8"]]
- 006bee64 bytes 736d1694
+ 006beea4 bytes 636e1694
- 006beedc ["INT_ADD", "register:40f0:8", ["const:6beedc:8", "const:4:8"]]
- 006beedc ["CALL", null, ["callee:00c5a830:8"]]
+ 006bef1c ["INT_ADD", "register:40f0:8", ["const:6bef1c:8", "const:4:8"]]
+ 006bef1c ["CALL", null, ["callee:00c5a830:8"]]
- 006beedc bytes 556d1694
+ 006bef1c bytes 456e1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a110b575a56cdfa0afaa51530fac7c3"></a>

### [`006bf84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md) → [`006bf88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf88c.md) FUN_006bf88c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`006797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006797c0.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`00925834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00925/00925834.md) · 呼出先 10件 [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md)
- 新版 呼出元 4件 [`00679800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00679/00679800.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) [`009259d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00925/009259d0.md) · 呼出先 10件 [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f1c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.50% / 新版 90.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006bf9c8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006bf988",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006bf9d8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006bf998",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006bf9f8",
      "incomplete_value": true,
      "site": "006bf9fc",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf9b8",
      "incomplete_value": true,
      "site": "006bf9bc",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bf8c4",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "006bf8d8",
      "READ",
      [
        "storage",
        "00ca4894",
        null,
        "undefined4"
      ]
    ],
    [
      "006bf9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006bf8c4",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "006bf8d8",
      "READ",
      [
        "storage",
        "00ca4c94",
        null,
        "undefined4"
      ]
    ],
    [
      "006bf9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bf988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md#insn-006bf988) · [`006bf998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md#insn-006bf998) · [`006bf9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md#insn-006bf9b8)
- 新版 `006bf9c8`（命令位置の公開資料なし） · `006bf9d8`（命令位置の公開資料なし） · `006bf9f8`（命令位置の公開資料なし）

~~~diff
- 006bf988 ["INT_ADD", "register:40f0:8", ["const:6bf988:8", "const:4:8"]]
- 006bf988 ["CALL", null, ["ram:46c984:8"]]
+ 006bf9c8 ["INT_ADD", "register:40f0:8", ["const:6bf9c8:8", "const:4:8"]]
+ 006bf9c8 ["CALL", null, ["ram:46c9c4:8"]]
- 006bf988 bytes ffb3f697
+ 006bf9c8 bytes ffb3f697
- 006bf998 ["INT_ADD", "register:40f0:8", ["const:6bf998:8", "const:4:8"]]
- 006bf998 ["CALL", null, ["ram:46c984:8"]]
+ 006bf9d8 ["INT_ADD", "register:40f0:8", ["const:6bf9d8:8", "const:4:8"]]
+ 006bf9d8 ["CALL", null, ["ram:46c9c4:8"]]
- 006bf998 bytes fbb3f697
+ 006bf9d8 bytes fbb3f697
- 006bf9b8 ["COPY", "tmp:0:8", ["const:870:8"]]
- 006bf9b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006bf9b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006bf9b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006bf9f8 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 006bf9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006bf9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006bf9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006bf9b8 bytes 00c02191
+ 006bf9f8 bytes 00c03191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcd519f7abf82d152920a963f80bf999"></a>

### [`006c0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0330.md) → [`006c0370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0370.md) FUN_006c0370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0384",
      "incomplete_value": true,
      "site": "006c0388",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0344",
      "incomplete_value": true,
      "site": "006c0348",
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
            "const:e20:8"
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
      "006c0388",
      "DATA",
      [
        "storage",
        "00c75e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c0388",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c033c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0330.md#insn-006c033c) · [`006c0340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0330.md#insn-006c0340) · [`006c0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0330.md#insn-006c0344)
- 新版 `006c037c`（命令位置の公開資料なし） · `006c0380`（命令位置の公開資料なし） · `006c0384`（命令位置の公開資料なし）

~~~diff
- 006c033c ["INT_ADD", "register:40f0:8", ["const:6c033c:8", "const:4:8"]]
- 006c033c ["CALL", null, ["callee:00c57e90:8"]]
+ 006c037c ["INT_ADD", "register:40f0:8", ["const:6c037c:8", "const:4:8"]]
+ 006c037c ["CALL", null, ["callee:00c57e90:8"]]
- 006c033c bytes d55d1694
+ 006c037c bytes c55e1694
- 006c0340 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006c0380 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006c0340 bytes a82d00b0
+ 006c0380 bytes a82d00d0
- 006c0344 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006c0344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c0344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c0344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c0384 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 006c0384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c0344 bytes 08813891
+ 006c0384 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cd981dfcd1c5fd06d495fa96f112263"></a>

### [`006c0354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0354.md) → [`006c0394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0394.md) FUN_006c0394

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
      "definition_site": "006c0398",
      "incomplete_value": false,
      "site": "006c039c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0358",
      "incomplete_value": false,
      "site": "006c035c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "006c039c",
      "DATA",
      [
        "storage",
        "00c75e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c039c",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c0354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0354.md#insn-006c0354) · [`006c0358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0354.md#insn-006c0358)
- 新版 `006c0394`（命令位置の公開資料なし） · `006c0398`（命令位置の公開資料なし）

~~~diff
- 006c0354 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006c0394 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006c0354 bytes a82d00b0
+ 006c0394 bytes a82d00d0
- 006c0358 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 006c0358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c0358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c0358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c0398 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 006c0398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c0358 bytes 08813891
+ 006c0398 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f54170efb3a0ee4d59169c888d1873e"></a>

### [`006c036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md) → [`006c03ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c03ac.md) FUN_006c03ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.28% / 新版 94.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0484",
      "incomplete_value": true,
      "site": "006c0494",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0444",
      "incomplete_value": true,
      "site": "006c0454",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:303:8"
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
      "definition_site": "006c0498",
      "incomplete_value": true,
      "site": "006c0498",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c0458",
      "incomplete_value": true,
      "site": "006c0458",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0534",
      "incomplete_value": true,
      "site": "006c0544",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c04f4",
      "incomplete_value": true,
      "site": "006c0504",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:303:8"
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
      "006c03f8",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ],
    [
      "006c0410",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ],
    [
      "006c0464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006c03f8",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "006c0410",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ],
    [
      "006c0464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c0424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md#insn-006c0424) · [`006c0558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md#insn-006c0558) · [`006c0580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md#insn-006c0580)
- 新版 `006c0464`（命令位置の公開資料なし） · `006c0598`（命令位置の公開資料なし） · `006c05c0`（命令位置の公開資料なし）

~~~diff
- 006c0424 ["INT_ADD", "register:40f0:8", ["const:6c0424:8", "const:4:8"]]
- 006c0424 ["CALL", null, ["ram:47acb4:8"]]
+ 006c0464 ["INT_ADD", "register:40f0:8", ["const:6c0464:8", "const:4:8"]]
+ 006c0464 ["CALL", null, ["ram:47acf4:8"]]
- 006c0424 bytes 24eaf697
+ 006c0464 bytes 24eaf697
- 006c0558 ["INT_ADD", "register:40f0:8", ["const:6c0558:8", "const:4:8"]]
- 006c0558 ["CALL", null, ["ram:48ccb8:8"]]
+ 006c0598 ["INT_ADD", "register:40f0:8", ["const:6c0598:8", "const:4:8"]]
+ 006c0598 ["CALL", null, ["ram:48ccf8:8"]]
- 006c0558 bytes d831f797
+ 006c0598 bytes d831f797
- 006c0580 ["INT_ADD", "register:40f0:8", ["const:6c0580:8", "const:4:8"]]
- 006c0580 ["CALL", null, ["callee:00c57f60:8"]]
+ 006c05c0 ["INT_ADD", "register:40f0:8", ["const:6c05c0:8", "const:4:8"]]
+ 006c05c0 ["CALL", null, ["callee:00c57f60:8"]]
- 006c0580 bytes 785d1694
+ 006c05c0 bytes 685e1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53179e6b6a07f42cd9fe6e2f38b9d2e"></a>

### [`006c093c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c093c.md) → [`006c097c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c097c.md) _INIT_108

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c09b8",
      "incomplete_value": true,
      "site": "006c09d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0978",
      "incomplete_value": true,
      "site": "006c0994",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "006c09dc",
      "incomplete_value": true,
      "site": "006c09f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006c099c",
      "incomplete_value": true,
      "site": "006c09b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006c09fc",
      "incomplete_value": true,
      "site": "006c0a18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006c09bc",
      "incomplete_value": true,
      "site": "006c09d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c09b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006c09dc",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006c09fc",
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
      "006c09b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006c09dc",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006c09fc",
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

- 旧版 [`006c09b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c093c.md#insn-006c09b4) · [`006c09d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c093c.md#insn-006c09d4) · [`006c0a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c093c.md#insn-006c0a9c)
- 新版 `006c09f4`（命令位置の公開資料なし） · `006c0a14`（命令位置の公開資料なし） · `006c0adc`（命令位置の公開資料なし）

~~~diff
- 006c09b4 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 006c09b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006c09b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006c09b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006c09f4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006c09f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006c09f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006c09f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006c09b4 bytes 4a093691
+ 006c09f4 bytes 4a093791
- 006c09d4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006c09d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006c09d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006c09d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006c0a14 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006c0a14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006c0a14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006c0a14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006c09d4 bytes 4a553a91
+ 006c0a14 bytes 4a893d91
- 006c0a9c ["INT_ADD", "register:40f0:8", ["const:6c0a9c:8", "const:4:8"]]
- 006c0a9c ["CALL", null, ["callee:0043b7f8:8"]]
+ 006c0adc ["INT_ADD", "register:40f0:8", ["const:6c0adc:8", "const:4:8"]]
+ 006c0adc ["CALL", null, ["callee:0043b7f8:8"]]
- 006c0a9c bytes 47ebf597
+ 006c0adc bytes 47ebf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0457f22299b0a91167eb9b6b58eb33b"></a>

### [`006c1fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1fd8.md) → [`006c2018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c2/006c2018.md) FUN_006c2018

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) [`008f5a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006c1d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1d48.md) [`006c1dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1dd4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 6件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006c1d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c1/006c1d88.md) [`006c1e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c1/006c1e14.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.25% / 新版 99.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c2128",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c20e8",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c22dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c229c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006c2128",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006c22dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006c2128",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006c22dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c20e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1fd8.md#insn-006c20e8) · [`006c229c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1fd8.md#insn-006c229c) · [`006c2078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1fd8.md#insn-006c2078)
- 新版 `006c2128`（命令位置の公開資料なし） · `006c22dc`（命令位置の公開資料なし） · `006c20b8`（命令位置の公開資料なし）

~~~diff
- 006c20e8 ["INT_ADD", "register:40f0:8", ["const:6c20e8:8", "const:4:8"]]
- 006c20e8 ["CALL", null, ["ram:47acb4:8"]]
+ 006c2128 ["INT_ADD", "register:40f0:8", ["const:6c2128:8", "const:4:8"]]
+ 006c2128 ["CALL", null, ["ram:47acf4:8"]]
- 006c20e8 bytes f3e2f697
+ 006c2128 bytes f3e2f697
- 006c229c ["INT_ADD", "register:40f0:8", ["const:6c229c:8", "const:4:8"]]
- 006c229c ["CALL", null, ["ram:47acb4:8"]]
+ 006c22dc ["INT_ADD", "register:40f0:8", ["const:6c22dc:8", "const:4:8"]]
+ 006c22dc ["CALL", null, ["ram:47acf4:8"]]
- 006c229c bytes 86e2f697
+ 006c22dc bytes 86e2f697
- 006c2078 ["INT_ADD", "register:40f0:8", ["const:6c2078:8", "const:4:8"]]
- 006c2078 ["CALL", null, ["callee:008514f8:8"]]
+ 006c20b8 ["INT_ADD", "register:40f0:8", ["const:6c20b8:8", "const:4:8"]]
+ 006c20b8 ["CALL", null, ["callee:008514f8:8"]]
- 006c2078 bytes 103d0694
+ 006c20b8 bytes 103d0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0f0003741a40bfcc22d68c63f3ad32"></a>

### [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md) → [`006c3278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3278.md) FUN_006c3278

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006c307c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c307c.md) [`006c30b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c30b0.md) [`006c30d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c30d8.md) [`006c3174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3174.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 10件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006c30bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c30bc.md) [`006c30f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c30f0.md) [`006c3118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3118.md) [`006c31b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c31b4.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3668",
      "incomplete_value": true,
      "site": "006c3678",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3628",
      "incomplete_value": true,
      "site": "006c3638",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3680",
      "incomplete_value": true,
      "site": "006c368c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3640",
      "incomplete_value": true,
      "site": "006c364c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c34e4",
      "incomplete_value": false,
      "site": "006c34fc",
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
      "definition_site": "006c34a4",
      "incomplete_value": false,
      "site": "006c34bc",
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
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c33b4",
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "006c340c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006c341c",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006c33b4",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "006c340c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006c341c",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c347c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md#insn-006c347c) · [`006c34bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md#insn-006c34bc) · [`006c352c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md#insn-006c352c)
- 新版 `006c34bc`（命令位置の公開資料なし） · `006c34fc`（命令位置の公開資料なし） · `006c356c`（命令位置の公開資料なし）

~~~diff
- 006c347c ["INT_ADD", "register:40f0:8", ["const:6c347c:8", "const:4:8"]]
- 006c347c ["CALL", null, ["callee:00c57eb0:8"]]
+ 006c34bc ["INT_ADD", "register:40f0:8", ["const:6c34bc:8", "const:4:8"]]
+ 006c34bc ["CALL", null, ["callee:00c57eb0:8"]]
- 006c347c bytes 8d511694
+ 006c34bc bytes 7d521694
- 006c34bc ["INT_ADD", "register:40f0:8", ["const:6c34bc:8", "const:4:8"]]
- 006c34bc ["CALL", null, ["callee:00c57e30:8"]]
+ 006c34fc ["INT_ADD", "register:40f0:8", ["const:6c34fc:8", "const:4:8"]]
+ 006c34fc ["CALL", null, ["callee:00c57e30:8"]]
- 006c34bc bytes 5d511694
+ 006c34fc bytes 4d521694
- 006c352c ["INT_ADD", "register:40f0:8", ["const:6c352c:8", "const:4:8"]]
- 006c352c ["CALL", null, ["ram:46c984:8"]]
+ 006c356c ["INT_ADD", "register:40f0:8", ["const:6c356c:8", "const:4:8"]]
+ 006c356c ["CALL", null, ["ram:46c9c4:8"]]
- 006c352c bytes 16a5f697
+ 006c356c bytes 16a5f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46895f452cb79d678da9f52434129e59"></a>

### [`006c3a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3a34.md) → [`006c3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3a74.md) FUN_006c3a74

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 3件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`006c3238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3238.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 3件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006c3278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3278.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3bec",
      "incomplete_value": true,
      "site": "006c3c04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
      "definition_site": "006c3bac",
      "incomplete_value": true,
      "site": "006c3bc4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3bec",
      "incomplete_value": true,
      "site": "006c3c10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
      "definition_site": "006c3bac",
      "incomplete_value": true,
      "site": "006c3bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c3aec",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c3aac",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006c3aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006c3b00",
      "READ",
      [
        "storage",
        "002c43d0",
        null,
        "undefined8"
      ]
    ],
    [
      "006c3b1c",
      "READ",
      [
        "storage",
        "002c3e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006c3aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006c3b00",
      "READ",
      [
        "storage",
        "002c4410",
        null,
        "undefined8"
      ]
    ],
    [
      "006c3b1c",
      "READ",
      [
        "storage",
        "002c3e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c3aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3a34.md#insn-006c3aac) · [`006c3b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3a34.md#insn-006c3b58) · [`006c3b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3a34.md#insn-006c3b98)
- 新版 `006c3aec`（命令位置の公開資料なし） · `006c3b98`（命令位置の公開資料なし） · `006c3bd8`（命令位置の公開資料なし）

~~~diff
- 006c3aac ["INT_ADD", "register:40f0:8", ["const:6c3aac:8", "const:4:8"]]
- 006c3aac ["CALL", null, ["ram:46c984:8"]]
+ 006c3aec ["INT_ADD", "register:40f0:8", ["const:6c3aec:8", "const:4:8"]]
+ 006c3aec ["CALL", null, ["ram:46c9c4:8"]]
- 006c3aac bytes b6a3f697
+ 006c3aec bytes b6a3f697
- 006c3b58 ["INT_ADD", "register:40f0:8", ["const:6c3b58:8", "const:4:8"]]
- 006c3b58 ["CALL", null, ["ram:46c984:8"]]
+ 006c3b98 ["INT_ADD", "register:40f0:8", ["const:6c3b98:8", "const:4:8"]]
+ 006c3b98 ["CALL", null, ["ram:46c9c4:8"]]
- 006c3b58 bytes 8ba3f697
+ 006c3b98 bytes 8ba3f697
- 006c3b98 ["INT_ADD", "register:40f0:8", ["const:6c3b98:8", "const:4:8"]]
- 006c3b98 ["CALL", null, ["callee:008514f8:8"]]
+ 006c3bd8 ["INT_ADD", "register:40f0:8", ["const:6c3bd8:8", "const:4:8"]]
+ 006c3bd8 ["CALL", null, ["callee:008514f8:8"]]
- 006c3b98 bytes 48360694
+ 006c3bd8 bytes 48360694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b251f962382abeeb64c8974fef37ceef"></a>

### [`006c3d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3d10.md) → [`006c3d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c3/006c3d50.md) FUN_006c3d50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 4件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a827d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a827d8.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 4件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a829d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a82/00a829d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.11% / 新版 96.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3f80",
      "incomplete_value": true,
      "site": "006c3f90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3f40",
      "incomplete_value": true,
      "site": "006c3f50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:ea8:8"
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
      "definition_site": "006c3f98",
      "incomplete_value": true,
      "site": "006c3fa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3f58",
      "incomplete_value": true,
      "site": "006c3f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c3e34",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c3df4",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006c3ddc",
      "READ",
      [
        "storage",
        "002c3fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c3e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006c3f20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006c3ddc",
      "READ",
      [
        "storage",
        "002c3ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c3e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006c3f20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c3df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3d10.md#insn-006c3df4) · [`006c3ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3d10.md#insn-006c3ee0) · [`006c3f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c3/006c3d10.md#insn-006c3f78)
- 新版 `006c3e34`（命令位置の公開資料なし） · `006c3f20`（命令位置の公開資料なし） · `006c3fb8`（命令位置の公開資料なし）

~~~diff
- 006c3df4 ["INT_ADD", "register:40f0:8", ["const:6c3df4:8", "const:4:8"]]
- 006c3df4 ["CALL", null, ["ram:46c984:8"]]
+ 006c3e34 ["INT_ADD", "register:40f0:8", ["const:6c3e34:8", "const:4:8"]]
+ 006c3e34 ["CALL", null, ["ram:46c9c4:8"]]
- 006c3df4 bytes e4a2f697
+ 006c3e34 bytes e4a2f697
- 006c3ee0 ["INT_ADD", "register:40f0:8", ["const:6c3ee0:8", "const:4:8"]]
- 006c3ee0 ["CALL", null, ["ram:46c984:8"]]
+ 006c3f20 ["INT_ADD", "register:40f0:8", ["const:6c3f20:8", "const:4:8"]]
+ 006c3f20 ["CALL", null, ["ram:46c9c4:8"]]
- 006c3ee0 bytes a9a2f697
+ 006c3f20 bytes a9a2f697
- 006c3f78 ["INT_ADD", "register:40f0:8", ["const:6c3f78:8", "const:4:8"]]
- 006c3f78 ["CALL", null, ["ram:46c984:8"]]
+ 006c3fb8 ["INT_ADD", "register:40f0:8", ["const:6c3fb8:8", "const:4:8"]]
+ 006c3fb8 ["CALL", null, ["ram:46c9c4:8"]]
- 006c3f78 bytes 83a2f697
+ 006c3fb8 bytes 83a2f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21d804a3416eb620d8c625669b56bb4"></a>

### [`006c41f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c41f8.md) → [`006c4238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4238.md) FUN_006c4238

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) [`006e9364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9364.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006c0ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0ef8.md) [`006c4180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4180.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) [`006e93a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e93a4.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006c0f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f38.md) [`006c41c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c41c0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.33% / 新版 95.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c42d8",
      "value": [
        "leaf",
        "ram:6c0f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4298",
      "value": [
        "leaf",
        "ram:6c0ef8:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c436c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c432c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c43b0",
      "value": [
        "leaf",
        "ram:6c0f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4370",
      "value": [
        "leaf",
        "ram:6c0ef8:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c42d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0ef8"
      ]
    ],
    [
      "006c436c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006c43b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0ef8"
      ]
    ]
  ],
  "added": [
    [
      "006c42d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0f38"
      ]
    ],
    [
      "006c436c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006c43b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c41f8.md#insn-006c4298) · [`006c432c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c41f8.md#insn-006c432c) · [`006c4370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c41f8.md#insn-006c4370)
- 新版 `006c42d8`（命令位置の公開資料なし） · `006c436c`（命令位置の公開資料なし） · `006c43b0`（命令位置の公開資料なし）

~~~diff
- 006c4298 ["INT_ADD", "register:40f0:8", ["const:6c4298:8", "const:4:8"]]
- 006c4298 ["CALL", null, ["ram:6c0ef8:8"]]
+ 006c42d8 ["INT_ADD", "register:40f0:8", ["const:6c42d8:8", "const:4:8"]]
+ 006c42d8 ["CALL", null, ["ram:6c0f38:8"]]
- 006c4298 bytes 18f3ff97
+ 006c42d8 bytes 18f3ff97
- 006c432c ["INT_ADD", "register:40f0:8", ["const:6c432c:8", "const:4:8"]]
- 006c432c ["CALL", null, ["ram:47acb4:8"]]
+ 006c436c ["INT_ADD", "register:40f0:8", ["const:6c436c:8", "const:4:8"]]
+ 006c436c ["CALL", null, ["ram:47acf4:8"]]
- 006c432c bytes 62daf697
+ 006c436c bytes 62daf697
- 006c4370 ["INT_ADD", "register:40f0:8", ["const:6c4370:8", "const:4:8"]]
- 006c4370 ["CALL", null, ["ram:6c0ef8:8"]]
+ 006c43b0 ["INT_ADD", "register:40f0:8", ["const:6c43b0:8", "const:4:8"]]
+ 006c43b0 ["CALL", null, ["ram:6c0f38:8"]]
- 006c4370 bytes e2f2ff97
+ 006c43b0 bytes e2f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a92b6f974ead2ba65ae7e043ce87531a"></a>

### [`006c43a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c43a4.md) → [`006c43e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c43e4.md) FUN_006c43e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`0064be48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064be48.md) [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) [`006e7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md) [`006e9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 18件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00469104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469104.md)
- 新版 呼出元 6件 [`0064be88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064be88.md) [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) [`006e7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md) [`006e9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e9e64.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 18件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00469144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469144.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4458",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4418",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c44b0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4470",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4644",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4604",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 23,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c4458",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006c44b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006c44f0",
      "READ",
      [
        "storage",
        "00c9b0f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006c4458",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006c44b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006c44f0",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c43a4.md#insn-006c4418) · [`006c4470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c43a4.md#insn-006c4470) · [`006c44b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c43a4.md#insn-006c44b0)
- 新版 `006c4458`（命令位置の公開資料なし） · `006c44b0`（命令位置の公開資料なし） · `006c44f0`（命令位置の公開資料なし）

~~~diff
- 006c4418 ["INT_ADD", "register:40f0:8", ["const:6c4418:8", "const:4:8"]]
- 006c4418 ["CALL", null, ["ram:46c984:8"]]
+ 006c4458 ["INT_ADD", "register:40f0:8", ["const:6c4458:8", "const:4:8"]]
+ 006c4458 ["CALL", null, ["ram:46c9c4:8"]]
- 006c4418 bytes 5ba1f697
+ 006c4458 bytes 5ba1f697
- 006c4470 ["INT_ADD", "register:40f0:8", ["const:6c4470:8", "const:4:8"]]
- 006c4470 ["CALL", null, ["ram:46c984:8"]]
+ 006c44b0 ["INT_ADD", "register:40f0:8", ["const:6c44b0:8", "const:4:8"]]
+ 006c44b0 ["CALL", null, ["ram:46c9c4:8"]]
- 006c4470 bytes 45a1f697
+ 006c44b0 bytes 45a1f697
- 006c44b0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:f0:8"]]
- 006c44b0 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c44f0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:4f0:8"]]
+ 006c44f0 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 006c44b0 bytes 7b7b40f9
+ 006c44f0 bytes 7b7b42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cef1302b32f2932435b66d349921c8c"></a>

### [`006c5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c5048.md) → [`006c5088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c5088.md) FUN_006c5088

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`00682aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682aa4.md) [`006834a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00683/006834a0.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 9件 [`00682ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682ae4.md) [`006834e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00683/006834e0.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c50fc",
      "incomplete_value": false,
      "site": "006c5100",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c50bc",
      "incomplete_value": false,
      "site": "006c50c0",
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
            "const:f0:8"
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
      "006c50fc",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c50fc",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c5048.md#insn-006c50c0) · [`006c50bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c5048.md#insn-006c50bc)
- 新版 `006c5100`（命令位置の公開資料なし） · `006c50fc`（命令位置の公開資料なし）

~~~diff
- 006c50c0 ["INT_ADD", "register:40f0:8", ["const:6c50c0:8", "const:4:8"]]
- 006c50c0 ["CALL", null, ["callee:00442930:8"]]
+ 006c5100 ["INT_ADD", "register:40f0:8", ["const:6c5100:8", "const:4:8"]]
+ 006c5100 ["CALL", null, ["callee:00442930:8"]]
- 006c50c0 bytes 0cf6f597
+ 006c5100 bytes 0cf6f597
- 006c50bc ["COPY", "tmp:0:8", ["const:f0:8"]]
- 006c50bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c50bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c50bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c50fc ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 006c50fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c50fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c50fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c50bc bytes 00c00391
+ 006c50fc bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14d07a6ede5905e22f323a4ec567224"></a>

### [`006c50d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c50d0.md) → [`006c5110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c5110.md) FUN_006c5110

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`008f380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f380c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`008f39a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f39a8.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.18% / 新版 99.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c52f0",
      "incomplete_value": false,
      "site": "006c52f4",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52b0",
      "incomplete_value": false,
      "site": "006c52b4",
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
            "const:f0:8"
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
      "006c52f0",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c52f0",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c52b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c50d0.md#insn-006c52b4) · [`006c52b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c50d0.md#insn-006c52b0)
- 新版 `006c52f4`（命令位置の公開資料なし） · `006c52f0`（命令位置の公開資料なし）

~~~diff
- 006c52b4 ["INT_ADD", "register:40f0:8", ["const:6c52b4:8", "const:4:8"]]
- 006c52b4 ["CALL", null, ["callee:00442930:8"]]
+ 006c52f4 ["INT_ADD", "register:40f0:8", ["const:6c52f4:8", "const:4:8"]]
+ 006c52f4 ["CALL", null, ["callee:00442930:8"]]
- 006c52b4 bytes 8ff5f597
+ 006c52f4 bytes 8ff5f597
- 006c52b0 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 006c52b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c52b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c52b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c52f0 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 006c52f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c52f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c52f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c52b0 bytes 00c00391
+ 006c52f0 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa13b236caefbedea99a10fc96d3778d"></a>

### [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) → [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) FUN_006c6e10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 14件 [`00682950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682950.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) · 呼出先 71件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0068996c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/0068996c.md) [`006cb074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb074.md) [`006d5e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d5/006d5e64.md)
- 新版 呼出元 14件 [`00682990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682990.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) · 呼出先 71件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006899ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/006899ac.md) [`006cb0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb0b4.md) [`006d5ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d5/006d5ea4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.98% / 新版 99.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006cab88",
      "incomplete_value": false,
      "site": "006cab94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2df000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cab48",
      "incomplete_value": false,
      "site": "006cab54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2df000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "ordinal": 264,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006cab88",
      "PARAM",
      [
        "storage",
        "002dfc78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006cab88",
      "PARAM",
      [
        "storage",
        "002dfcb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cab54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md#insn-006cab54) · [`006c6e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md#insn-006c6e30) · [`006c6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md#insn-006c6e50)
- 新版 `006cab94`（命令位置の公開資料なし） · `006c6e70`（命令位置の公開資料なし） · `006c6e90`（命令位置の公開資料なし）

~~~diff
- 006cab54 ["INT_ADD", "register:40f0:8", ["const:6cab54:8", "const:4:8"]]
- 006cab54 ["CALL", null, ["callee:00c58000:8"]]
+ 006cab94 ["INT_ADD", "register:40f0:8", ["const:6cab94:8", "const:4:8"]]
+ 006cab94 ["CALL", null, ["callee:00c58000:8"]]
- 006cab54 bytes 2b341694
+ 006cab94 bytes 1b351694
- 006c6e30 ["INT_ADD", "register:40f0:8", ["const:6c6e30:8", "const:4:8"]]
- 006c6e30 ["CALL", null, ["callee:00676a60:8"]]
+ 006c6e70 ["INT_ADD", "register:40f0:8", ["const:6c6e70:8", "const:4:8"]]
+ 006c6e70 ["CALL", null, ["callee:00676a60:8"]]
- 006c6e30 bytes fcbefe97
+ 006c6e70 bytes fcbefe97
- 006c6e50 ["INT_ADD", "register:40f0:8", ["const:6c6e50:8", "const:4:8"]]
- 006c6e50 ["CALL", null, ["callee:008514f8:8"]]
+ 006c6e90 ["INT_ADD", "register:40f0:8", ["const:6c6e90:8", "const:4:8"]]
+ 006c6e90 ["CALL", null, ["callee:008514f8:8"]]
- 006c6e50 bytes 9a290694
+ 006c6e90 bytes 9a290694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f206e8ba26f5f8fd32fe84f67ce1dfd"></a>

### [`006cb84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb84c.md) → [`006cb88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb88c.md) FUN_006cb88c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006cba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cba34.md) [`006ccb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cc/006ccb38.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`006d6fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d6/006d6fe0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`006cba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cba74.md) [`006ccb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cc/006ccb78.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006d7020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7020.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006cb8dc",
      "incomplete_value": true,
      "site": "006cb8e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb89c",
      "incomplete_value": true,
      "site": "006cb8a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006cb960",
      "incomplete_value": true,
      "site": "006cb96c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb920",
      "incomplete_value": true,
      "site": "006cb92c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:288:8"
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
      "006cb8dc",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ],
    [
      "006cb960",
      "READ",
      [
        "storage",
        "002c4288",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006cb8dc",
      "READ",
      [
        "storage",
        "002c3fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "006cb960",
      "READ",
      [
        "storage",
        "002c42c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb84c.md#insn-006cb88c) · [`006cb89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb84c.md#insn-006cb89c) · [`006cb8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb84c.md#insn-006cb8b0)
- 新版 `006cb8cc`（命令位置の公開資料なし） · `006cb8dc`（命令位置の公開資料なし） · `006cb8f0`（命令位置の公開資料なし）

~~~diff
- 006cb88c ["INT_ADD", "register:40f0:8", ["const:6cb88c:8", "const:4:8"]]
- 006cb88c ["CALL", null, ["callee:00c57e90:8"]]
+ 006cb8cc ["INT_ADD", "register:40f0:8", ["const:6cb8cc:8", "const:4:8"]]
+ 006cb8cc ["CALL", null, ["callee:00c57e90:8"]]
- 006cb88c bytes 81301694
+ 006cb8cc bytes 71311694
- 006cb89c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
- 006cb89c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 006cb89c ["COPY", "register:5008:8", ["const:0:8"]]
- 006cb89c ["COPY", "register:5010:8", ["const:0:8"]]
+ 006cb8dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 006cb8dc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006cb8dc ["COPY", "register:5008:8", ["const:0:8"]]
+ 006cb8dc ["COPY", "register:5010:8", ["const:0:8"]]
- 006cb89c bytes 00c147fd
+ 006cb8dc bytes 00e147fd
- 006cb8b0 ["INT_ADD", "register:40f0:8", ["const:6cb8b0:8", "const:4:8"]]
- 006cb8b0 ["CALL", null, ["callee:0043bba4:8"]]
+ 006cb8f0 ["INT_ADD", "register:40f0:8", ["const:6cb8f0:8", "const:4:8"]]
+ 006cb8f0 ["CALL", null, ["callee:0043bba4:8"]]
- 006cb8b0 bytes adc0f597
+ 006cb8f0 bytes adc0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1a4cb383de14aab428051dd7d151ba"></a>

### [`006cdc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cd/006cdc48.md) → [`006cdc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cd/006cdc88.md) FUN_006cdc88

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`009f77f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f77f4.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 35件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md)
- 新版 呼出元 5件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`009f7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7990.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 35件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006cec98",
      "incomplete_value": true,
      "site": "006cec98",
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
      "definition_site": "006cec58",
      "incomplete_value": true,
      "site": "006cec58",
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
    "ordinal": 156,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006cec98",
      "incomplete_value": true,
      "site": "006cec98",
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
      "definition_site": "006cec58",
      "incomplete_value": true,
      "site": "006cec58",
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
    "ordinal": 157,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006cdd34",
      "value": [
        "leaf",
        "ram:6cba74:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006cdcf4",
      "value": [
        "leaf",
        "ram:6cba34:8"
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
      "006cdd34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006cba34"
      ]
    ],
    [
      "006cdd40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ccb38"
      ]
    ],
    [
      "006cdd98",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "byte[11]"
      ]
    ]
  ],
  "added": [
    [
      "006cdd34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006cba74"
      ]
    ],
    [
      "006cdd40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ccb78"
      ]
    ],
    [
      "006cdd98",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "byte[15]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cdcf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cd/006cdc48.md#insn-006cdcf4) · [`006cdd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cd/006cdc48.md#insn-006cdd00) · [`006cec98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cd/006cdc48.md#insn-006cec98)
- 新版 `006cdd34`（命令位置の公開資料なし） · `006cdd40`（命令位置の公開資料なし） · `006cecd8`（命令位置の公開資料なし）

~~~diff
- 006cdcf4 ["INT_ADD", "register:40f0:8", ["const:6cdcf4:8", "const:4:8"]]
- 006cdcf4 ["CALL", null, ["ram:6cba34:8"]]
+ 006cdd34 ["INT_ADD", "register:40f0:8", ["const:6cdd34:8", "const:4:8"]]
+ 006cdd34 ["CALL", null, ["ram:6cba74:8"]]
- 006cdcf4 bytes 50f7ff97
+ 006cdd34 bytes 50f7ff97
- 006cdd00 ["INT_ADD", "register:40f0:8", ["const:6cdd00:8", "const:4:8"]]
- 006cdd00 ["CALL", null, ["ram:6ccb38:8"]]
+ 006cdd40 ["INT_ADD", "register:40f0:8", ["const:6cdd40:8", "const:4:8"]]
+ 006cdd40 ["CALL", null, ["ram:6ccb78:8"]]
- 006cdd00 bytes 8efbff97
+ 006cdd40 bytes 8efbff97
- 006cec98 ["INT_ADD", "register:40f0:8", ["const:6cec98:8", "const:4:8"]]
- 006cec98 ["CALL", null, ["callee:008514f8:8"]]
+ 006cecd8 ["INT_ADD", "register:40f0:8", ["const:6cecd8:8", "const:4:8"]]
+ 006cecd8 ["CALL", null, ["callee:008514f8:8"]]
- 006cec98 bytes 080a0694
+ 006cecd8 bytes 080a0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88107ae18deef8d74ad74e0705785cfb"></a>

### [`006d09dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d09dc.md) → [`006d0a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d0a1c.md) FUN_006d0a1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 13件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`006d7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e30.md) [`006d7e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 13件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006d7e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7e70.md) [`006d7e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7e74.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d0ab8",
      "incomplete_value": false,
      "site": "006d0ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0a78",
      "incomplete_value": false,
      "site": "006d0a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "006d0b68",
      "incomplete_value": true,
      "site": "006d0b6c",
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
                "const:7a0:8"
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
      "definition_site": "006d0b28",
      "incomplete_value": true,
      "site": "006d0b2c",
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
                "const:3a0:8"
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0a48",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0a08",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006d0a48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006d0ab8",
      "DATA",
      [
        "storage",
        "00c75f18",
        null,
        "undefined *"
      ]
    ],
    [
      "006d0b1c",
      "READ",
      [
        "storage",
        "00c75f38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d0a48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006d0ab8",
      "DATA",
      [
        "storage",
        "00c76318",
        null,
        "undefined *"
      ]
    ],
    [
      "006d0b1c",
      "READ",
      [
        "storage",
        "00c76338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d09dc.md#insn-006d0a08) · [`006d0aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d09dc.md#insn-006d0aec) · [`006d0a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d09dc.md#insn-006d0a04)
- 新版 `006d0a48`（命令位置の公開資料なし） · `006d0b2c`（命令位置の公開資料なし） · `006d0a44`（命令位置の公開資料なし）

~~~diff
- 006d0a08 ["INT_ADD", "register:40f0:8", ["const:6d0a08:8", "const:4:8"]]
- 006d0a08 ["CALL", null, ["ram:46c984:8"]]
+ 006d0a48 ["INT_ADD", "register:40f0:8", ["const:6d0a48:8", "const:4:8"]]
+ 006d0a48 ["CALL", null, ["ram:46c9c4:8"]]
- 006d0a08 bytes df6ff697
+ 006d0a48 bytes df6ff697
- 006d0aec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f68:8"]]
- 006d0aec ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006d0b2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:368:8"]]
+ 006d0b2c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 006d0aec bytes b5b647f9
+ 006d0b2c bytes b5b641f9
- 006d0a04 ["INT_ADD", "register:40f0:8", ["const:6d0a04:8", "const:4:8"]]
- 006d0a04 ["CALL", null, ["callee:008514f8:8"]]
+ 006d0a44 ["INT_ADD", "register:40f0:8", ["const:6d0a44:8", "const:4:8"]]
+ 006d0a44 ["CALL", null, ["callee:008514f8:8"]]
- 006d0a04 bytes ad020694
+ 006d0a44 bytes ad020694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3ec47f8d2167289cb631323c45c3d78"></a>

### [`006d0c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0c00.md) → [`006d0c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d0c40.md) FUN_006d0c40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 13件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`006d8210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8210.md) [`006d8214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8214.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 13件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006d8250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8250.md) [`006d8254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8254.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.93% / 新版 96.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d0dbc",
      "incomplete_value": false,
      "site": "006d0dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0d7c",
      "incomplete_value": false,
      "site": "006d0d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0c74",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0c34",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006d0c74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006d0d20",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "006d0d34",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0c74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006d0d20",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "006d0d34",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0c00.md#insn-006d0c34) · [`006d0c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0c00.md#insn-006d0c30) · [`006d0c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0c00.md#insn-006d0c6c)
- 新版 `006d0c74`（命令位置の公開資料なし） · `006d0c70`（命令位置の公開資料なし） · `006d0cac`（命令位置の公開資料なし）

~~~diff
- 006d0c34 ["INT_ADD", "register:40f0:8", ["const:6d0c34:8", "const:4:8"]]
- 006d0c34 ["CALL", null, ["ram:46c984:8"]]
+ 006d0c74 ["INT_ADD", "register:40f0:8", ["const:6d0c74:8", "const:4:8"]]
+ 006d0c74 ["CALL", null, ["ram:46c9c4:8"]]
- 006d0c34 bytes 546ff697
+ 006d0c74 bytes 546ff697
- 006d0c30 ["INT_ADD", "register:40f0:8", ["const:6d0c30:8", "const:4:8"]]
- 006d0c30 ["CALL", null, ["callee:008514f8:8"]]
+ 006d0c70 ["INT_ADD", "register:40f0:8", ["const:6d0c70:8", "const:4:8"]]
+ 006d0c70 ["CALL", null, ["callee:008514f8:8"]]
- 006d0c30 bytes 22020694
+ 006d0c70 bytes 22020694
- 006d0c6c ["INT_ADD", "register:40f0:8", ["const:6d0c6c:8", "const:4:8"]]
- 006d0c6c ["CALL", null, ["callee:00a468fc:8"]]
+ 006d0cac ["INT_ADD", "register:40f0:8", ["const:6d0cac:8", "const:4:8"]]
+ 006d0cac ["CALL", null, ["callee:00a468fc:8"]]
- 006d0c6c bytes a6d60d94
+ 006d0cac bytes 14d70d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fa3d8352be3a7d4b507a291391dbfc7"></a>

### [`006d0f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0f0c.md) → [`006d0f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d0/006d0f4c.md) FUN_006d0f4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 13件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`006d83a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a0.md) [`006d83a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 13件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006d83e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d83e0.md) [`006d83e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d83e4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.93% / 新版 96.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d10c8",
      "incomplete_value": false,
      "site": "006d10c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1088",
      "incomplete_value": false,
      "site": "006d1088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0f80",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0f40",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006d0f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006d102c",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "006d1040",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006d102c",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "006d1040",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0f0c.md#insn-006d0f40) · [`006d0f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0f0c.md#insn-006d0f3c) · [`006d0f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0f0c.md#insn-006d0f78)
- 新版 `006d0f80`（命令位置の公開資料なし） · `006d0f7c`（命令位置の公開資料なし） · `006d0fb8`（命令位置の公開資料なし）

~~~diff
- 006d0f40 ["INT_ADD", "register:40f0:8", ["const:6d0f40:8", "const:4:8"]]
- 006d0f40 ["CALL", null, ["ram:46c984:8"]]
+ 006d0f80 ["INT_ADD", "register:40f0:8", ["const:6d0f80:8", "const:4:8"]]
+ 006d0f80 ["CALL", null, ["ram:46c9c4:8"]]
- 006d0f40 bytes 916ef697
+ 006d0f80 bytes 916ef697
- 006d0f3c ["INT_ADD", "register:40f0:8", ["const:6d0f3c:8", "const:4:8"]]
- 006d0f3c ["CALL", null, ["callee:008514f8:8"]]
+ 006d0f7c ["INT_ADD", "register:40f0:8", ["const:6d0f7c:8", "const:4:8"]]
+ 006d0f7c ["CALL", null, ["callee:008514f8:8"]]
- 006d0f3c bytes 5f010694
+ 006d0f7c bytes 5f010694
- 006d0f78 ["INT_ADD", "register:40f0:8", ["const:6d0f78:8", "const:4:8"]]
- 006d0f78 ["CALL", null, ["callee:00a468fc:8"]]
+ 006d0fb8 ["INT_ADD", "register:40f0:8", ["const:6d0fb8:8", "const:4:8"]]
+ 006d0fb8 ["CALL", null, ["callee:00a468fc:8"]]
- 006d0f78 bytes e3d50d94
+ 006d0fb8 bytes 51d60d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-310211517fb6bd8da30920066b78dc3b"></a>

### [`006d1478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1478.md) → [`006d14b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d14b8.md) FUN_006d14b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`008f380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f380c.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 6件 [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c4e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4e2c.md) [`006d7eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7eb4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`008f39a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f39a8.md) [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 6件 [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006c4e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4e6c.md) [`006d7ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7ef4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.54% / 新版 99.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d17d0",
      "incomplete_value": false,
      "site": "006d17d8",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1790",
      "incomplete_value": false,
      "site": "006d1798",
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
            "const:30e:8"
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
      "006d17d0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006d17d0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1478.md#insn-006d1758) · [`006d1798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1478.md#insn-006d1798) · [`006d14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1478.md#insn-006d14b8)
- 新版 `006d1798`（命令位置の公開資料なし） · `006d17d8`（命令位置の公開資料なし） · `006d14f8`（命令位置の公開資料なし）

~~~diff
- 006d1758 ["INT_ADD", "register:40f0:8", ["const:6d1758:8", "const:4:8"]]
- 006d1758 ["CALL", null, ["callee:008514f8:8"]]
+ 006d1798 ["INT_ADD", "register:40f0:8", ["const:6d1798:8", "const:4:8"]]
+ 006d1798 ["CALL", null, ["callee:008514f8:8"]]
- 006d1758 bytes 58ff0594
+ 006d1798 bytes 58ff0594
- 006d1798 ["INT_ADD", "register:40f0:8", ["const:6d1798:8", "const:4:8"]]
- 006d1798 ["CALL", null, ["callee:00c58190:8"]]
+ 006d17d8 ["INT_ADD", "register:40f0:8", ["const:6d17d8:8", "const:4:8"]]
+ 006d17d8 ["CALL", null, ["callee:00c58190:8"]]
- 006d1798 bytes 7e191694
+ 006d17d8 bytes 6e1a1694
- 006d14b8 ["INT_ADD", "register:40f0:8", ["const:6d14b8:8", "const:4:8"]]
- 006d14b8 ["CALL", null, ["callee:006c4e6c:8"]]
+ 006d14f8 ["INT_ADD", "register:40f0:8", ["const:6d14f8:8", "const:4:8"]]
+ 006d14f8 ["CALL", null, ["callee:006c4e6c:8"]]
- 006d14b8 bytes 5dceff97
+ 006d14f8 bytes 5dceff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f8a7397c2cd5dd24fc6a01a95ccf06"></a>

### [`006d1808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md) → [`006d1848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1848.md) FUN_006d1848

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c4e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4e2c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`008f6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6694.md) [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006c4e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4e6c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.77% / 新版 99.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d188c",
      "incomplete_value": false,
      "site": "006d1894",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d184c",
      "incomplete_value": false,
      "site": "006d1854",
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
            "const:30e:8"
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
      "006d188c",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "006d1a08",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "byte[15]"
      ]
    ],
    [
      "006d1a24",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "006d188c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "006d1a08",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "qword"
      ]
    ],
    [
      "006d1a24",
      "DATA",
      [
        "storage",
        "003c9660",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md#insn-006d1854) · [`006d1840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md#insn-006d1840) · [`006d184c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md#insn-006d184c)
- 新版 `006d1894`（命令位置の公開資料なし） · `006d1880`（命令位置の公開資料なし） · `006d188c`（命令位置の公開資料なし）

~~~diff
- 006d1854 ["INT_ADD", "register:40f0:8", ["const:6d1854:8", "const:4:8"]]
- 006d1854 ["CALL", null, ["callee:00c58190:8"]]
+ 006d1894 ["INT_ADD", "register:40f0:8", ["const:6d1894:8", "const:4:8"]]
+ 006d1894 ["CALL", null, ["callee:00c58190:8"]]
- 006d1854 bytes 4f191694
+ 006d1894 bytes 3f1a1694
- 006d1840 ["INT_ADD", "register:40f0:8", ["const:6d1840:8", "const:4:8"]]
- 006d1840 ["CALL", null, ["callee:008514f8:8"]]
+ 006d1880 ["INT_ADD", "register:40f0:8", ["const:6d1880:8", "const:4:8"]]
+ 006d1880 ["CALL", null, ["callee:008514f8:8"]]
- 006d1840 bytes 1eff0594
+ 006d1880 bytes 1eff0594
- 006d184c ["COPY", "tmp:0:8", ["const:30e:8"]]
- 006d184c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006d184c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006d184c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006d188c ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 006d188c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006d188c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006d188c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006d184c bytes 21380c91
+ 006d188c bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb9535b7bd9f4201371549cf3346636"></a>

### [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) → [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) FUN_006d1fe4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00694490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694490.md) [`008f5a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`009a319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a319c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 45件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md)
- 新版 呼出元 6件 [`006944d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006944d0.md) [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`009a3338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3338.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 45件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value, unresolved_call_alignment

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 6件, `store_value` 38件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d2510",
      "incomplete_value": true,
      "site": "006d2510",
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
      "definition_site": "006d24d0",
      "incomplete_value": true,
      "site": "006d24d0",
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
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d2538",
      "incomplete_value": true,
      "site": "006d253c",
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
      "definition_site": "006d24f8",
      "incomplete_value": true,
      "site": "006d24fc",
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
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d257c",
      "incomplete_value": true,
      "site": "006d257c",
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
      "definition_site": "006d253c",
      "incomplete_value": true,
      "site": "006d253c",
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
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d2028",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "006d209c",
      "DATA",
      [
        "storage",
        "00c76098",
        null,
        "undefined *"
      ]
    ],
    [
      "006d209c",
      "DATA",
      [
        "storage",
        "00c76118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d2028",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "006d209c",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ],
    [
      "006d209c",
      "DATA",
      [
        "storage",
        "00c76518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d257c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md#insn-006d257c) · [`006d2610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md#insn-006d2610) · [`006d346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md#insn-006d346c)
- 新版 `006d25bc`（命令位置の公開資料なし） · `006d2650`（命令位置の公開資料なし） · `006d34ac`（命令位置の公開資料なし）

~~~diff
- 006d257c ["INT_ADD", "register:40f0:8", ["const:6d257c:8", "const:4:8"]]
- 006d257c ["CALL", null, ["callee:00a46784:8"]]
+ 006d25bc ["INT_ADD", "register:40f0:8", ["const:6d25bc:8", "const:4:8"]]
+ 006d25bc ["CALL", null, ["callee:00a46784:8"]]
- 006d257c bytes 04d00d94
+ 006d25bc bytes 72d00d94
- 006d2610 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
- 006d2610 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006d2650 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
+ 006d2650 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006d2610 bytes 08b547f9
+ 006d2650 bytes 08b541f9
- 006d346c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 006d34ac ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 006d346c bytes 282e00f0
+ 006d34ac bytes 482e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80bf30c545ea7855eec6e1505f559dca"></a>

### [`006d3dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md) → [`006d3e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d3/006d3e3c.md) FUN_006d3e3c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 44件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 3件 [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 44件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d48cc",
      "incomplete_value": true,
      "site": "006d48cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:63d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d488c",
      "incomplete_value": true,
      "site": "006d488c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d48d0",
      "incomplete_value": true,
      "site": "006d48d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d4890",
      "incomplete_value": true,
      "site": "006d4890",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d44a4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4464",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 96,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d4020",
      "READ",
      [
        "storage",
        "002c4118",
        null,
        "undefined8"
      ]
    ],
    [
      "006d43a8",
      "DATA",
      [
        "storage",
        "0039ba9c",
        null,
        "uleb128"
      ]
    ],
    [
      "006d44a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006d4020",
      "READ",
      [
        "storage",
        "002c4158",
        null,
        "undefined8"
      ]
    ],
    [
      "006d43a8",
      "DATA",
      [
        "storage",
        "0039ba9c",
        null,
        "qword"
      ]
    ],
    [
      "006d44a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md#insn-006d4464) · [`006d44c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md#insn-006d44c4) · [`006d4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md#insn-006d4504)
- 新版 `006d44a4`（命令位置の公開資料なし） · `006d4504`（命令位置の公開資料なし） · `006d4544`（命令位置の公開資料なし）

~~~diff
- 006d4464 ["INT_ADD", "register:40f0:8", ["const:6d4464:8", "const:4:8"]]
- 006d4464 ["CALL", null, ["ram:46c984:8"]]
+ 006d44a4 ["INT_ADD", "register:40f0:8", ["const:6d44a4:8", "const:4:8"]]
+ 006d44a4 ["CALL", null, ["ram:46c9c4:8"]]
- 006d4464 bytes 4861f697
+ 006d44a4 bytes 4861f697
- 006d44c4 ["INT_ADD", "register:40f0:8", ["const:6d44c4:8", "const:4:8"]]
- 006d44c4 ["CALL", null, ["ram:47acb4:8"]]
+ 006d4504 ["INT_ADD", "register:40f0:8", ["const:6d4504:8", "const:4:8"]]
+ 006d4504 ["CALL", null, ["ram:47acf4:8"]]
- 006d44c4 bytes fc99f697
+ 006d4504 bytes fc99f697
- 006d4504 ["INT_ADD", "register:40f0:8", ["const:6d4504:8", "const:4:8"]]
- 006d4504 ["CALL", null, ["ram:46c984:8"]]
+ 006d4544 ["INT_ADD", "register:40f0:8", ["const:6d4544:8", "const:4:8"]]
+ 006d4544 ["CALL", null, ["ram:46c9c4:8"]]
- 006d4504 bytes 2061f697
+ 006d4544 bytes 2061f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c60e6890297f16d70a2a682a0cf320"></a>

### [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) → [`006d4d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d4/006d4d94.md) FUN_006d4d94

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 26件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00467e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e5c.md) [`00467e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e64.md)
- 新版 呼出元 3件 [`008f7e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7e78.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 26件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md) [`00467ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ea4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4dcc",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4d8c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4e14",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4dd4",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4fc0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4f80",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 24,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d4dcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006d4e14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006d4fc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006d4dcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006d4e14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006d4fc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md#insn-006d4d8c) · [`006d4dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md#insn-006d4dd4) · [`006d4f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md#insn-006d4f70)
- 新版 `006d4dcc`（命令位置の公開資料なし） · `006d4e14`（命令位置の公開資料なし） · `006d4fb0`（命令位置の公開資料なし）

~~~diff
- 006d4d8c ["INT_ADD", "register:40f0:8", ["const:6d4d8c:8", "const:4:8"]]
- 006d4d8c ["CALL", null, ["ram:46c984:8"]]
+ 006d4dcc ["INT_ADD", "register:40f0:8", ["const:6d4dcc:8", "const:4:8"]]
+ 006d4dcc ["CALL", null, ["ram:46c9c4:8"]]
- 006d4d8c bytes fe5ef697
+ 006d4dcc bytes fe5ef697
- 006d4dd4 ["INT_ADD", "register:40f0:8", ["const:6d4dd4:8", "const:4:8"]]
- 006d4dd4 ["CALL", null, ["ram:46c984:8"]]
+ 006d4e14 ["INT_ADD", "register:40f0:8", ["const:6d4e14:8", "const:4:8"]]
+ 006d4e14 ["CALL", null, ["ram:46c9c4:8"]]
- 006d4dd4 bytes ec5ef697
+ 006d4e14 bytes ec5ef697
- 006d4f70 ["INT_ADD", "register:40f0:8", ["const:6d4f70:8", "const:4:8"]]
- 006d4f70 ["CALL", null, ["callee:00468f88:8"]]
+ 006d4fb0 ["INT_ADD", "register:40f0:8", ["const:6d4fb0:8", "const:4:8"]]
+ 006d4fb0 ["CALL", null, ["callee:00468f88:8"]]
- 006d4f70 bytes f64ff697
+ 006d4fb0 bytes f64ff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22da7567e6d49f12c717f44121dc2d41"></a>

### [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) → [`006d7088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7088.md) FUN_006d7088

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 呼出先 10件 [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`006cfeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cf/006cfeec.md) · 呼出先 10件 [`006d738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d738c.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

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
      "definition_site": "006d7348",
      "incomplete_value": false,
      "site": "006d734c",
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
            "const:fd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7308",
      "incomplete_value": false,
      "site": "006d730c",
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
            "const:f04:8"
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
      "006d7348",
      "PARAM",
      [
        "storage",
        "002a9f04",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d7348",
      "PARAM",
      [
        "storage",
        "002a9fd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d730c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md#insn-006d730c) · [`006d70c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md#insn-006d70c8) · [`006d70e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md#insn-006d70e8)
- 新版 `006d734c`（命令位置の公開資料なし） · `006d7108`（命令位置の公開資料なし） · `006d7128`（命令位置の公開資料なし）

~~~diff
- 006d730c ["INT_ADD", "register:40f0:8", ["const:6d730c:8", "const:4:8"]]
- 006d730c ["CALL", null, ["callee:006d7650:8"]]
+ 006d734c ["INT_ADD", "register:40f0:8", ["const:6d734c:8", "const:4:8"]]
+ 006d734c ["CALL", null, ["callee:006d7650:8"]]
- 006d730c bytes c1000094
+ 006d734c bytes c1000094
- 006d70c8 ["INT_ADD", "register:40f0:8", ["const:6d70c8:8", "const:4:8"]]
- 006d70c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d7108 ["INT_ADD", "register:40f0:8", ["const:6d7108:8", "const:4:8"]]
+ 006d7108 ["CALL", null, ["callee:00c57e90:8"]]
- 006d70c8 bytes 72021694
+ 006d7108 bytes 62031694
- 006d70e8 ["INT_ADD", "register:40f0:8", ["const:6d70e8:8", "const:4:8"]]
- 006d70e8 ["CALL", null, ["callee:00c58090:8"]]
+ 006d7128 ["INT_ADD", "register:40f0:8", ["const:6d7128:8", "const:4:8"]]
+ 006d7128 ["CALL", null, ["callee:00c58090:8"]]
- 006d70e8 bytes ea021694
+ 006d7128 bytes da031694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8088cc81d00fe6ec227fecdd087056d6"></a>

### [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) → [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) FUN_006d7650

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) [`006d773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md) [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) [`007f4150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md) · 呼出先 4件 [`006d7674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7674.md) [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 4件 [`006d7088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7088.md) [`006d777c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d777c.md) [`007f3e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md) [`007f4190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md) · 呼出先 4件 [`006d76b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76b4.md) [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "006d7680",
      "incomplete_value": true,
      "site": "006d7688",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:548:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7640",
      "incomplete_value": true,
      "site": "006d7648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
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
      "definition_site": "006d7684",
      "incomplete_value": true,
      "site": "006d7688",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:550:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7644",
      "incomplete_value": true,
      "site": "006d7648",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
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
      "006d7680",
      "READ",
      [
        "storage",
        "00c9b148",
        null,
        "pointer"
      ]
    ],
    [
      "006d7680",
      "PARAM",
      [
        "storage",
        "00c96470",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d7684",
      "READ",
      [
        "storage",
        "00c9b150",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d7680",
      "READ",
      [
        "storage",
        "00c9b548",
        null,
        "pointer"
      ]
    ],
    [
      "006d7680",
      "PARAM",
      [
        "storage",
        "00c96870",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d7684",
      "READ",
      [
        "storage",
        "00c9b550",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md#insn-006d7648) · [`006d7624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md#insn-006d7624) · [`006d7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md#insn-006d7630)
- 新版 `006d7688`（命令位置の公開資料なし） · `006d7664`（命令位置の公開資料なし） · `006d7670`（命令位置の公開資料なし）

~~~diff
- 006d7648 ["INT_ADD", "register:40f0:8", ["const:6d7648:8", "const:4:8"]]
- 006d7648 ["CALL", null, ["callee:00c57f10:8"]]
+ 006d7688 ["INT_ADD", "register:40f0:8", ["const:6d7688:8", "const:4:8"]]
+ 006d7688 ["CALL", null, ["callee:00c57f10:8"]]
- 006d7648 bytes 32011694
+ 006d7688 bytes 22021694
- 006d7624 ["INT_ADD", "register:40f0:8", ["const:6d7624:8", "const:4:8"]]
- 006d7624 ["CALL", null, ["callee:00c57ef0:8"]]
+ 006d7664 ["INT_ADD", "register:40f0:8", ["const:6d7664:8", "const:4:8"]]
+ 006d7664 ["CALL", null, ["callee:00c57ef0:8"]]
- 006d7624 bytes 33011694
+ 006d7664 bytes 23021694
- 006d7630 ["INT_ADD", "register:40f0:8", ["const:6d7630:8", "const:4:8"]]
- 006d7630 ["CALL", null, ["callee:006d76b4:8"]]
+ 006d7670 ["INT_ADD", "register:40f0:8", ["const:6d7670:8", "const:4:8"]]
+ 006d7670 ["CALL", null, ["callee:006d76b4:8"]]
- 006d7630 bytes 11000094
+ 006d7670 bytes 11000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8bd9c0d86226e5dbfbcb26f1ae94e9"></a>

### [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) → [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) FUN_006d76a0

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 25件 [`006cfeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cf/006cfeec.md) [`006d7088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7088.md) [`006d738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d738c.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`007f3e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "006d76ac",
      "incomplete_value": false,
      "site": "006d76b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:f23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d766c",
      "incomplete_value": false,
      "site": "006d7670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:ee3:8"
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
      "006d76ac",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d76ac",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md#insn-006d7670) · [`006d766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md#insn-006d766c)
- 新版 `006d76b0`（命令位置の公開資料なし） · `006d76ac`（命令位置の公開資料なし）

~~~diff
- 006d7670 ["INT_ADD", "register:40f0:8", ["const:6d7670:8", "const:4:8"]]
- 006d7670 ["CALL", null, ["callee:0043b778:8"]]
+ 006d76b0 ["INT_ADD", "register:40f0:8", ["const:6d76b0:8", "const:4:8"]]
+ 006d76b0 ["CALL", null, ["callee:0043b778:8"]]
- 006d7670 bytes 3290f597
+ 006d76b0 bytes 3290f597
- 006d766c ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 006d766c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d766c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d766c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d76ac ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 006d76ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d76ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d76ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d766c bytes 008c3b91
+ 006d76ac bytes 008c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba1aa40cbd3d3f30c2b5490c91497ac3"></a>

### [`006d773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md) → [`006d777c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d777c.md) FUN_006d777c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7b50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`006cfeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cf/006cfeec.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d7b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7b90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "006d7b24",
      "incomplete_value": false,
      "site": "006d7b28",
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
            "const:bd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7ae4",
      "incomplete_value": false,
      "site": "006d7ae8",
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
            "const:afb:8"
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
      "006d7b24",
      "PARAM",
      [
        "storage",
        "002a7afb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d7b24",
      "PARAM",
      [
        "storage",
        "002a7bd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md#insn-006d7ae8) · [`006d77cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md#insn-006d77cc) · [`006d77ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md#insn-006d77ec)
- 新版 `006d7b28`（命令位置の公開資料なし） · `006d780c`（命令位置の公開資料なし） · `006d782c`（命令位置の公開資料なし）

~~~diff
- 006d7ae8 ["INT_ADD", "register:40f0:8", ["const:6d7ae8:8", "const:4:8"]]
- 006d7ae8 ["CALL", null, ["callee:006d7650:8"]]
+ 006d7b28 ["INT_ADD", "register:40f0:8", ["const:6d7b28:8", "const:4:8"]]
+ 006d7b28 ["CALL", null, ["callee:006d7650:8"]]
- 006d7ae8 bytes cafeff97
+ 006d7b28 bytes cafeff97
- 006d77cc ["INT_ADD", "register:40f0:8", ["const:6d77cc:8", "const:4:8"]]
- 006d77cc ["CALL", null, ["callee:00c57e90:8"]]
+ 006d780c ["INT_ADD", "register:40f0:8", ["const:6d780c:8", "const:4:8"]]
+ 006d780c ["CALL", null, ["callee:00c57e90:8"]]
- 006d77cc bytes b1001694
+ 006d780c bytes a1011694
- 006d77ec ["INT_ADD", "register:40f0:8", ["const:6d77ec:8", "const:4:8"]]
- 006d77ec ["CALL", null, ["callee:00c58090:8"]]
+ 006d782c ["INT_ADD", "register:40f0:8", ["const:6d782c:8", "const:4:8"]]
+ 006d782c ["CALL", null, ["callee:00c58090:8"]]
- 006d77ec bytes 29011694
+ 006d782c bytes 19021694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93aa5690c9486b7ba6d7d0d19299f50d"></a>

### [`006d7de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7de8.md) → [`006d7e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7e28.md) FUN_006d7e28

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
      "definition_site": "006d7e4c",
      "incomplete_value": false,
      "site": "006d7e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7e0c",
      "incomplete_value": false,
      "site": "006d7e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "006d7e4c",
      "DATA",
      [
        "storage",
        "00c75f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d7e4c",
      "DATA",
      [
        "storage",
        "00c76318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7de8.md#insn-006d7dfc) · [`006d7e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7de8.md#insn-006d7e04) · [`006d7e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7de8.md#insn-006d7e08)
- 新版 `006d7e3c`（命令位置の公開資料なし） · `006d7e44`（命令位置の公開資料なし） · `006d7e48`（命令位置の公開資料なし）

~~~diff
- 006d7dfc ["INT_ADD", "register:40f0:8", ["const:6d7dfc:8", "const:4:8"]]
- 006d7dfc ["CALL", null, ["callee:00c57e90:8"]]
+ 006d7e3c ["INT_ADD", "register:40f0:8", ["const:6d7e3c:8", "const:4:8"]]
+ 006d7e3c ["CALL", null, ["callee:00c57e90:8"]]
- 006d7dfc bytes 25ff1594
+ 006d7e3c bytes 15001694
- 006d7e04 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006d7e44 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d7e04 bytes e82c00d0
+ 006d7e44 bytes e82c00f0
- 006d7e08 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 006d7e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d7e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d7e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d7e48 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 006d7e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d7e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d7e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d7e08 bytes 08613c91
+ 006d7e48 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0575ef737ff9a976af3137f3d3b8f97d"></a>

### [`006d7e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e1c.md) → [`006d7e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7e5c.md) FUN_006d7e5c

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
      "definition_site": "006d7e68",
      "incomplete_value": false,
      "site": "006d7e68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7e28",
      "incomplete_value": false,
      "site": "006d7e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "006d7e68",
      "DATA",
      [
        "storage",
        "00c75f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d7e68",
      "DATA",
      [
        "storage",
        "00c76318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e1c.md#insn-006d7e20) · [`006d7e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e1c.md#insn-006d7e24)
- 新版 `006d7e60`（命令位置の公開資料なし） · `006d7e64`（命令位置の公開資料なし）

~~~diff
- 006d7e20 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 006d7e60 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006d7e20 bytes e92c00d0
+ 006d7e60 bytes e92c00f0
- 006d7e24 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 006d7e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d7e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d7e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d7e64 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 006d7e64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d7e64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d7e64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d7e24 bytes 29613c91
+ 006d7e64 bytes 29610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca69af9b85b82b5431f3f9b0a671409"></a>

### [`006d7e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e38.md) → [`006d7e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7e78.md) FUN_006d7e78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006d4c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4c04.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006d4c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d4/006d4c44.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7e98",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7e58",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7ea4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7e64",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006d7e98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d7ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006d7e98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d7ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e38.md#insn-006d7e58) · [`006d7e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e38.md#insn-006d7e64)
- 新版 `006d7e98`（命令位置の公開資料なし） · `006d7ea4`（命令位置の公開資料なし）

~~~diff
- 006d7e58 ["INT_ADD", "register:40f0:8", ["const:6d7e58:8", "const:4:8"]]
- 006d7e58 ["CALL", null, ["ram:47acb4:8"]]
+ 006d7e98 ["INT_ADD", "register:40f0:8", ["const:6d7e98:8", "const:4:8"]]
+ 006d7e98 ["CALL", null, ["ram:47acf4:8"]]
- 006d7e58 bytes 978bf697
+ 006d7e98 bytes 978bf697
- 006d7e64 ["INT_ADD", "register:40f0:8", ["const:6d7e64:8", "const:4:8"]]
- 006d7e64 ["CALL", null, ["ram:47acb4:8"]]
+ 006d7ea4 ["INT_ADD", "register:40f0:8", ["const:6d7ea4:8", "const:4:8"]]
+ 006d7ea4 ["CALL", null, ["ram:47acf4:8"]]
- 006d7e64 bytes 948bf697
+ 006d7ea4 bytes 948bf697
~~~


<a id="compare-85194568efa284f355e47d241f1a9fd4"></a>

### [`006d81c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81c8.md) → [`006d8208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8208.md) FUN_006d8208

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
      "definition_site": "006d822c",
      "incomplete_value": false,
      "site": "006d822c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d81ec",
      "incomplete_value": false,
      "site": "006d81ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "006d822c",
      "DATA",
      [
        "storage",
        "00c75f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d822c",
      "DATA",
      [
        "storage",
        "00c76398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d81dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81c8.md#insn-006d81dc) · [`006d81e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81c8.md#insn-006d81e4) · [`006d81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81c8.md#insn-006d81e8)
- 新版 `006d821c`（命令位置の公開資料なし） · `006d8224`（命令位置の公開資料なし） · `006d8228`（命令位置の公開資料なし）

~~~diff
- 006d81dc ["INT_ADD", "register:40f0:8", ["const:6d81dc:8", "const:4:8"]]
- 006d81dc ["CALL", null, ["callee:00c57e90:8"]]
+ 006d821c ["INT_ADD", "register:40f0:8", ["const:6d821c:8", "const:4:8"]]
+ 006d821c ["CALL", null, ["callee:00c57e90:8"]]
- 006d81dc bytes 2dfe1594
+ 006d821c bytes 1dff1594
- 006d81e4 ["COPY", "register:4040:8", ["const:c75000:8"]]
+ 006d8224 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d81e4 bytes e82c00b0
+ 006d8224 bytes e82c00d0
- 006d81e8 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 006d81e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d81e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d81e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8228 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 006d8228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d81e8 bytes 08613e91
+ 006d8228 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90ba64ef9bf68862e250204155490c3"></a>

### [`006d81fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81fc.md) → [`006d823c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d823c.md) FUN_006d823c

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
      "definition_site": "006d8248",
      "incomplete_value": false,
      "site": "006d8248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8208",
      "incomplete_value": false,
      "site": "006d8208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "006d8248",
      "DATA",
      [
        "storage",
        "00c75f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8248",
      "DATA",
      [
        "storage",
        "00c76398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81fc.md#insn-006d8200) · [`006d8204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81fc.md#insn-006d8204)
- 新版 `006d8240`（命令位置の公開資料なし） · `006d8244`（命令位置の公開資料なし）

~~~diff
- 006d8200 ["COPY", "register:4048:8", ["const:c75000:8"]]
+ 006d8240 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006d8200 bytes e92c00b0
+ 006d8240 bytes e92c00d0
- 006d8204 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 006d8204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d8204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d8204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d8244 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 006d8244 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8244 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8244 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d8204 bytes 29613e91
+ 006d8244 bytes 29610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-132d51af0b0b882068ddb3f38324617b"></a>

### [`006d8358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8358.md) → [`006d8398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8398.md) FUN_006d8398

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
      "definition_site": "006d83bc",
      "incomplete_value": false,
      "site": "006d83bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d837c",
      "incomplete_value": false,
      "site": "006d837c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "006d83bc",
      "DATA",
      [
        "storage",
        "00c76018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d83bc",
      "DATA",
      [
        "storage",
        "00c76418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d836c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8358.md#insn-006d836c) · [`006d8378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8358.md#insn-006d8378)
- 新版 `006d83ac`（命令位置の公開資料なし） · `006d83b8`（命令位置の公開資料なし）

~~~diff
- 006d836c ["INT_ADD", "register:40f0:8", ["const:6d836c:8", "const:4:8"]]
- 006d836c ["CALL", null, ["callee:00c57e90:8"]]
+ 006d83ac ["INT_ADD", "register:40f0:8", ["const:6d83ac:8", "const:4:8"]]
+ 006d83ac ["CALL", null, ["callee:00c57e90:8"]]
- 006d836c bytes c9fd1594
+ 006d83ac bytes b9fe1594
- 006d8378 ["COPY", "tmp:0:8", ["const:18:8"]]
- 006d8378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d83b8 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 006d83b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d83b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d83b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8378 bytes 08610091
+ 006d83b8 bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b61ecd19806e433917cea287c89e0ec"></a>

### [`006d838c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d838c.md) → [`006d83cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d83cc.md) FUN_006d83cc

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
      "definition_site": "006d83d8",
      "incomplete_value": false,
      "site": "006d83d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8398",
      "incomplete_value": false,
      "site": "006d8398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "006d83d8",
      "DATA",
      [
        "storage",
        "00c76018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d83d8",
      "DATA",
      [
        "storage",
        "00c76418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d838c.md#insn-006d8394)
- 新版 `006d83d4`（命令位置の公開資料なし）

~~~diff
- 006d8394 ["COPY", "tmp:0:8", ["const:18:8"]]
- 006d8394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d8394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d8394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d83d4 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 006d83d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d83d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d83d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d8394 bytes 29610091
+ 006d83d4 bytes 29611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3db097701d4f740d926c09082b3a24f"></a>

### [`006d83a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a8.md) → [`006d83e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d83e8.md) FUN_006d83e8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c4e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4e2c.md) [`006d1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1218.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006c4e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4e6c.md) [`006d1258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1258.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d842c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d83ec",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d8454",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d8414",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006d842c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d8454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d8620",
      "DATA",
      [
        "storage",
        "003c8d48",
        null,
        "byte[11]"
      ]
    ]
  ],
  "added": [
    [
      "006d842c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d8454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d8620",
      "DATA",
      [
        "storage",
        "003c8d48",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d83ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a8.md#insn-006d83ec) · [`006d8414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a8.md#insn-006d8414) · [`006d840c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a8.md#insn-006d840c)
- 新版 `006d842c`（命令位置の公開資料なし） · `006d8454`（命令位置の公開資料なし） · `006d844c`（命令位置の公開資料なし）

~~~diff
- 006d83ec ["INT_ADD", "register:40f0:8", ["const:6d83ec:8", "const:4:8"]]
- 006d83ec ["CALL", null, ["ram:47acb4:8"]]
+ 006d842c ["INT_ADD", "register:40f0:8", ["const:6d842c:8", "const:4:8"]]
+ 006d842c ["CALL", null, ["ram:47acf4:8"]]
- 006d83ec bytes 328af697
+ 006d842c bytes 328af697
- 006d8414 ["INT_ADD", "register:40f0:8", ["const:6d8414:8", "const:4:8"]]
- 006d8414 ["CALL", null, ["ram:47acb4:8"]]
+ 006d8454 ["INT_ADD", "register:40f0:8", ["const:6d8454:8", "const:4:8"]]
+ 006d8454 ["CALL", null, ["ram:47acf4:8"]]
- 006d8414 bytes 288af697
+ 006d8454 bytes 288af697
- 006d840c ["INT_ADD", "register:40f0:8", ["const:6d840c:8", "const:4:8"]]
- 006d840c ["CALL", null, ["callee:006d1258:8"]]
+ 006d844c ["INT_ADD", "register:40f0:8", ["const:6d844c:8", "const:4:8"]]
+ 006d844c ["CALL", null, ["callee:006d1258:8"]]
- 006d840c bytes 83e3ff97
+ 006d844c bytes 83e3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4a3d1c02b15ef9239da4d394969028"></a>

### [`006d86d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d86d8.md) → [`006d8718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8718.md) FUN_006d8718

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
      "definition_site": "006d873c",
      "incomplete_value": false,
      "site": "006d873c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d86fc",
      "incomplete_value": false,
      "site": "006d86fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "006d873c",
      "DATA",
      [
        "storage",
        "00c76098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d873c",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d86ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d86d8.md#insn-006d86ec) · [`006d86f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d86d8.md#insn-006d86f8)
- 新版 `006d872c`（命令位置の公開資料なし） · `006d8738`（命令位置の公開資料なし）

~~~diff
- 006d86ec ["INT_ADD", "register:40f0:8", ["const:6d86ec:8", "const:4:8"]]
- 006d86ec ["CALL", null, ["callee:00c57e90:8"]]
+ 006d872c ["INT_ADD", "register:40f0:8", ["const:6d872c:8", "const:4:8"]]
+ 006d872c ["CALL", null, ["callee:00c57e90:8"]]
- 006d86ec bytes e9fc1594
+ 006d872c bytes d9fd1594
- 006d86f8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 006d86f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d86f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d86f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8738 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 006d8738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d86f8 bytes 08610291
+ 006d8738 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1a1fe9b0b021a84c7de2ef0f62ff2f2"></a>

### [`006d870c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d870c.md) → [`006d874c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d874c.md) FUN_006d874c

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
      "definition_site": "006d8758",
      "incomplete_value": false,
      "site": "006d8758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8718",
      "incomplete_value": false,
      "site": "006d8718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "006d8758",
      "DATA",
      [
        "storage",
        "00c76098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8758",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d870c.md#insn-006d8714)
- 新版 `006d8754`（命令位置の公開資料なし）

~~~diff
- 006d8714 ["COPY", "tmp:0:8", ["const:98:8"]]
- 006d8714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d8714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d8714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d8754 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 006d8754 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8754 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8754 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d8714 bytes 29610291
+ 006d8754 bytes 29611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c33310c3623d471c557b732d82c1b3bc"></a>

### [`006d8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8c70.md) → [`006d8cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8cb0.md) FUN_006d8cb0

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
      "definition_site": "006d8cd4",
      "incomplete_value": false,
      "site": "006d8cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8c94",
      "incomplete_value": false,
      "site": "006d8c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "006d8cd4",
      "DATA",
      [
        "storage",
        "00c76118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8cd4",
      "DATA",
      [
        "storage",
        "00c76518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8c70.md#insn-006d8c84) · [`006d8c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8c70.md#insn-006d8c90)
- 新版 `006d8cc4`（命令位置の公開資料なし） · `006d8cd0`（命令位置の公開資料なし）

~~~diff
- 006d8c84 ["INT_ADD", "register:40f0:8", ["const:6d8c84:8", "const:4:8"]]
- 006d8c84 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d8cc4 ["INT_ADD", "register:40f0:8", ["const:6d8cc4:8", "const:4:8"]]
+ 006d8cc4 ["CALL", null, ["callee:00c57e90:8"]]
- 006d8c84 bytes 83fb1594
+ 006d8cc4 bytes 73fc1594
- 006d8c90 ["COPY", "tmp:0:8", ["const:118:8"]]
- 006d8c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8cd0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 006d8cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8c90 bytes 08610491
+ 006d8cd0 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e7a44968eb4dee440d903dbc336c195"></a>

### [`006d8ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8ca4.md) → [`006d8ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8ce4.md) FUN_006d8ce4

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
      "definition_site": "006d8cf0",
      "incomplete_value": false,
      "site": "006d8cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8cb0",
      "incomplete_value": false,
      "site": "006d8cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "006d8cf0",
      "DATA",
      [
        "storage",
        "00c76118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8cf0",
      "DATA",
      [
        "storage",
        "00c76518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8ca4.md#insn-006d8cac)
- 新版 `006d8cec`（命令位置の公開資料なし）

~~~diff
- 006d8cac ["COPY", "tmp:0:8", ["const:118:8"]]
- 006d8cac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d8cac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d8cac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d8cec ["COPY", "tmp:0:8", ["const:518:8"]]
+ 006d8cec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8cec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8cec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d8cac bytes 29610491
+ 006d8cec bytes 29611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66f406b983837d4f0b99b373988ccc5"></a>

### [`006d8cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8cc0.md) → [`006d8d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8d00.md) FUN_006d8d00

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664e00.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c4e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4e2c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00664bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664bcc.md) [`00664e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e40.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`006c4e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4e6c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.85% / 新版 99.85%

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
      "site": "006d93c8",
      "value": [
        "leaf",
        "ram:75a418:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9388",
      "value": [
        "leaf",
        "ram:75a3d8:8"
      ]
    },
    "ordinal": 54,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d8dd8",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "byte[23]"
      ]
    ],
    [
      "006d8ee4",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "byte[23]"
      ]
    ],
    [
      "006d9000",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "006d8dd8",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "qword"
      ]
    ],
    [
      "006d8ee4",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "qword"
      ]
    ],
    [
      "006d9000",
      "DATA",
      [
        "storage",
        "0039ba9d",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8cc0.md#insn-006d9388) · [`006d8cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8cc0.md#insn-006d8cec) · [`006d8cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8cc0.md#insn-006d8cfc)
- 新版 `006d93c8`（命令位置の公開資料なし） · `006d8d2c`（命令位置の公開資料なし） · `006d8d3c`（命令位置の公開資料なし）

~~~diff
- 006d9388 ["INT_ADD", "register:40f0:8", ["const:6d9388:8", "const:4:8"]]
- 006d9388 ["CALL", null, ["ram:75a3d8:8"]]
+ 006d93c8 ["INT_ADD", "register:40f0:8", ["const:6d93c8:8", "const:4:8"]]
+ 006d93c8 ["CALL", null, ["ram:75a418:8"]]
- 006d9388 bytes 14040294
+ 006d93c8 bytes 14040294
- 006d8cec ["INT_ADD", "register:40f0:8", ["const:6d8cec:8", "const:4:8"]]
- 006d8cec ["CALL", null, ["callee:008514f8:8"]]
+ 006d8d2c ["INT_ADD", "register:40f0:8", ["const:6d8d2c:8", "const:4:8"]]
+ 006d8d2c ["CALL", null, ["callee:008514f8:8"]]
- 006d8cec bytes f3e10594
+ 006d8d2c bytes f3e10594
- 006d8cfc ["INT_ADD", "register:40f0:8", ["const:6d8cfc:8", "const:4:8"]]
- 006d8cfc ["CALL", null, ["callee:008514f8:8"]]
+ 006d8d3c ["INT_ADD", "register:40f0:8", ["const:6d8d3c:8", "const:4:8"]]
+ 006d8d3c ["CALL", null, ["callee:008514f8:8"]]
- 006d8cfc bytes efe10594
+ 006d8d3c bytes efe10594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90fb0d4d160014f3167cd82deda8f793"></a>

### [`006d9828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9828.md) → [`006d9868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9868.md) FUN_006d9868

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
      "definition_site": "006d9874",
      "incomplete_value": false,
      "site": "006d9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9834",
      "incomplete_value": false,
      "site": "006d9834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "006d9874",
      "DATA",
      [
        "storage",
        "00c76198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9874",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9828.md#insn-006d9830)
- 新版 `006d9870`（命令位置の公開資料なし）

~~~diff
- 006d9830 ["COPY", "tmp:0:8", ["const:198:8"]]
- 006d9830 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d9830 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d9830 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d9870 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006d9870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d9870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d9870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d9830 bytes 29610691
+ 006d9870 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8ab6c05ac37aa98be37dc86ced09fa"></a>

### [`006d9844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md) → [`006d9884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9884.md) FUN_006d9884

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md) [`00a468f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9900",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d98c0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9928",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d98e8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006d9900",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9928",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006d9900",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d9928",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d98c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md#insn-006d98c0) · [`006d98e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md#insn-006d98e8) · [`006d9894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md#insn-006d9894)
- 新版 `006d9900`（命令位置の公開資料なし） · `006d9928`（命令位置の公開資料なし） · `006d98d4`（命令位置の公開資料なし）

~~~diff
- 006d98c0 ["INT_ADD", "register:40f0:8", ["const:6d98c0:8", "const:4:8"]]
- 006d98c0 ["CALL", null, ["ram:47acb4:8"]]
+ 006d9900 ["INT_ADD", "register:40f0:8", ["const:6d9900:8", "const:4:8"]]
+ 006d9900 ["CALL", null, ["ram:47acf4:8"]]
- 006d98c0 bytes fd84f697
+ 006d9900 bytes fd84f697
- 006d98e8 ["INT_ADD", "register:40f0:8", ["const:6d98e8:8", "const:4:8"]]
- 006d98e8 ["CALL", null, ["ram:47acb4:8"]]
+ 006d9928 ["INT_ADD", "register:40f0:8", ["const:6d9928:8", "const:4:8"]]
+ 006d9928 ["CALL", null, ["ram:47acf4:8"]]
- 006d98e8 bytes f384f697
+ 006d9928 bytes f384f697
- 006d9894 ["INT_ADD", "register:40f0:8", ["const:6d9894:8", "const:4:8"]]
- 006d9894 ["CALL", null, ["callee:008b6ea4:8"]]
+ 006d98d4 ["INT_ADD", "register:40f0:8", ["const:6d98d4:8", "const:4:8"]]
+ 006d98d4 ["CALL", null, ["callee:008b6ea4:8"]]
- 006d9894 bytes 73750794
+ 006d98d4 bytes 74750794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55970b73d8160b544f61b9a3cf141f16"></a>

### [`006d992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d992c.md) → [`006d996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d996c.md) FUN_006d996c

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
      "definition_site": "006d9990",
      "incomplete_value": false,
      "site": "006d9990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9950",
      "incomplete_value": false,
      "site": "006d9950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "006d9990",
      "DATA",
      [
        "storage",
        "00c76218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9990",
      "DATA",
      [
        "storage",
        "00c76618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d992c.md#insn-006d9940) · [`006d994c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d992c.md#insn-006d994c)
- 新版 `006d9980`（命令位置の公開資料なし） · `006d998c`（命令位置の公開資料なし）

~~~diff
- 006d9940 ["INT_ADD", "register:40f0:8", ["const:6d9940:8", "const:4:8"]]
- 006d9940 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d9980 ["INT_ADD", "register:40f0:8", ["const:6d9980:8", "const:4:8"]]
+ 006d9980 ["CALL", null, ["callee:00c57e90:8"]]
- 006d9940 bytes 54f81594
+ 006d9980 bytes 44f91594
- 006d994c ["COPY", "tmp:0:8", ["const:218:8"]]
- 006d994c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d994c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d994c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d998c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 006d998c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d998c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d998c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d994c bytes 08610891
+ 006d998c bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1097ff8e632a263b8ee736f52519bea5"></a>

### [`006d9960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9960.md) → [`006d99a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d99a0.md) FUN_006d99a0

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
      "definition_site": "006d99ac",
      "incomplete_value": false,
      "site": "006d99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d996c",
      "incomplete_value": false,
      "site": "006d996c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "006d99ac",
      "DATA",
      [
        "storage",
        "00c76218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d99ac",
      "DATA",
      [
        "storage",
        "00c76618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9960.md#insn-006d9968)
- 新版 `006d99a8`（命令位置の公開資料なし）

~~~diff
- 006d9968 ["COPY", "tmp:0:8", ["const:218:8"]]
- 006d9968 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d9968 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d9968 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d99a8 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 006d99a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d99a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d99a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d9968 bytes 29610891
+ 006d99a8 bytes 29611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf5628902c59a41cb4b4488f9b66e8a"></a>

### [`006d997c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md) → [`006d99bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d99bc.md) FUN_006d99bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9a2c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d99ec",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006d9a54",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9a14",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006d9a2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006d9a2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d9a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d99ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md#insn-006d99ec) · [`006d9a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md#insn-006d9a14) · [`006d99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md#insn-006d99cc)
- 新版 `006d9a2c`（命令位置の公開資料なし） · `006d9a54`（命令位置の公開資料なし） · `006d9a0c`（命令位置の公開資料なし）

~~~diff
- 006d99ec ["INT_ADD", "register:40f0:8", ["const:6d99ec:8", "const:4:8"]]
- 006d99ec ["CALL", null, ["ram:47acb4:8"]]
+ 006d9a2c ["INT_ADD", "register:40f0:8", ["const:6d9a2c:8", "const:4:8"]]
+ 006d9a2c ["CALL", null, ["ram:47acf4:8"]]
- 006d99ec bytes b284f697
+ 006d9a2c bytes b284f697
- 006d9a14 ["INT_ADD", "register:40f0:8", ["const:6d9a14:8", "const:4:8"]]
- 006d9a14 ["CALL", null, ["ram:47acb4:8"]]
+ 006d9a54 ["INT_ADD", "register:40f0:8", ["const:6d9a54:8", "const:4:8"]]
+ 006d9a54 ["CALL", null, ["ram:47acf4:8"]]
- 006d9a14 bytes a884f697
+ 006d9a54 bytes a884f697
- 006d99cc ["INT_ADD", "register:40f0:8", ["const:6d99cc:8", "const:4:8"]]
- 006d99cc ["CALL", null, ["callee:008b6ea4:8"]]
+ 006d9a0c ["INT_ADD", "register:40f0:8", ["const:6d9a0c:8", "const:4:8"]]
+ 006d9a0c ["CALL", null, ["callee:008b6ea4:8"]]
- 006d99cc bytes 25750794
+ 006d9a0c bytes 26750794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4c7bb898da5a31f4466ad7ff382fa8"></a>

### [`006d9a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a58.md) → [`006d9a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9a98.md) FUN_006d9a98

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
      "definition_site": "006d9abc",
      "incomplete_value": false,
      "site": "006d9abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9a7c",
      "incomplete_value": false,
      "site": "006d9a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006d9abc",
      "DATA",
      [
        "storage",
        "00c76298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9abc",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a58.md#insn-006d9a6c) · [`006d9a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a58.md#insn-006d9a78)
- 新版 `006d9aac`（命令位置の公開資料なし） · `006d9ab8`（命令位置の公開資料なし）

~~~diff
- 006d9a6c ["INT_ADD", "register:40f0:8", ["const:6d9a6c:8", "const:4:8"]]
- 006d9a6c ["CALL", null, ["callee:00c57e90:8"]]
+ 006d9aac ["INT_ADD", "register:40f0:8", ["const:6d9aac:8", "const:4:8"]]
+ 006d9aac ["CALL", null, ["callee:00c57e90:8"]]
- 006d9a6c bytes 09f81594
+ 006d9aac bytes f9f81594
- 006d9a78 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006d9a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9ab8 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 006d9ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9a78 bytes 08610a91
+ 006d9ab8 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1faf6b6483a6529f85abc8549a7b3407"></a>

### [`006d9a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a8c.md) → [`006d9acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9acc.md) FUN_006d9acc

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
      "definition_site": "006d9ad8",
      "incomplete_value": false,
      "site": "006d9ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9a98",
      "incomplete_value": false,
      "site": "006d9a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "006d9ad8",
      "DATA",
      [
        "storage",
        "00c76298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9ad8",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a8c.md#insn-006d9a94)
- 新版 `006d9ad4`（命令位置の公開資料なし）

~~~diff
- 006d9a94 ["COPY", "tmp:0:8", ["const:298:8"]]
- 006d9a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d9a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d9a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d9ad4 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 006d9ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d9ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d9ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d9a94 bytes 29610a91
+ 006d9ad4 bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e61cb2f67e437a7598c8dbc9d74e96"></a>

### [`006d9c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c24.md) → [`006d9c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9c64.md) FUN_006d9c64

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
      "definition_site": "006d9c84",
      "incomplete_value": false,
      "site": "006d9c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9c44",
      "incomplete_value": false,
      "site": "006d9c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
      "006d9c88",
      "DATA",
      [
        "storage",
        "00c76318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9c88",
      "DATA",
      [
        "storage",
        "00c76718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c24.md#insn-006d9c38) · [`006d9c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c24.md#insn-006d9c44)
- 新版 `006d9c78`（命令位置の公開資料なし） · `006d9c84`（命令位置の公開資料なし）

~~~diff
- 006d9c38 ["INT_ADD", "register:40f0:8", ["const:6d9c38:8", "const:4:8"]]
- 006d9c38 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d9c78 ["INT_ADD", "register:40f0:8", ["const:6d9c78:8", "const:4:8"]]
+ 006d9c78 ["CALL", null, ["callee:00c57e90:8"]]
- 006d9c38 bytes 96f71594
+ 006d9c78 bytes 86f81594
- 006d9c44 ["COPY", "tmp:0:8", ["const:318:8"]]
- 006d9c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9c84 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 006d9c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9c44 bytes 08610c91
+ 006d9c84 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1376f0267a9ae228e26324439921500a"></a>

### [`006d9c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c5c.md) → [`006d9c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9c9c.md) FUN_006d9c9c

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
      "definition_site": "006d9ca0",
      "incomplete_value": false,
      "site": "006d9ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9c60",
      "incomplete_value": false,
      "site": "006d9c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "006d9ca4",
      "DATA",
      [
        "storage",
        "00c76318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9ca4",
      "DATA",
      [
        "storage",
        "00c76718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c5c.md#insn-006d9c60)
- 新版 `006d9ca0`（命令位置の公開資料なし）

~~~diff
- 006d9c60 ["COPY", "tmp:0:8", ["const:318:8"]]
- 006d9c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9ca0 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 006d9ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9c60 bytes 08610c91
+ 006d9ca0 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3f2d5eecf4a19abf9ef7c2d8856260e"></a>

### [`006d9c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c7c.md) → [`006d9cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9cbc.md) FUN_006d9cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9cf0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9cb0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9cfc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9cbc",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006d9cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006d9cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006d9cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c7c.md#insn-006d9cb0) · [`006d9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c7c.md#insn-006d9cbc) · [`006d9d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c7c.md#insn-006d9d48)
- 新版 `006d9cf0`（命令位置の公開資料なし） · `006d9cfc`（命令位置の公開資料なし） · `006d9d88`（命令位置の公開資料なし）

~~~diff
- 006d9cb0 ["INT_ADD", "register:40f0:8", ["const:6d9cb0:8", "const:4:8"]]
- 006d9cb0 ["CALL", null, ["ram:47acb4:8"]]
+ 006d9cf0 ["INT_ADD", "register:40f0:8", ["const:6d9cf0:8", "const:4:8"]]
+ 006d9cf0 ["CALL", null, ["ram:47acf4:8"]]
- 006d9cb0 bytes 0184f697
+ 006d9cf0 bytes 0184f697
- 006d9cbc ["INT_ADD", "register:40f0:8", ["const:6d9cbc:8", "const:4:8"]]
- 006d9cbc ["CALL", null, ["ram:47acb4:8"]]
+ 006d9cfc ["INT_ADD", "register:40f0:8", ["const:6d9cfc:8", "const:4:8"]]
+ 006d9cfc ["CALL", null, ["ram:47acf4:8"]]
- 006d9cbc bytes fe83f697
+ 006d9cfc bytes fe83f697
- 006d9d48 ["INT_ADD", "register:40f0:8", ["const:6d9d48:8", "const:4:8"]]
- 006d9d48 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d9d88 ["INT_ADD", "register:40f0:8", ["const:6d9d88:8", "const:4:8"]]
+ 006d9d88 ["CALL", null, ["callee:00c57e90:8"]]
- 006d9d48 bytes 52f71594
+ 006d9d88 bytes 42f81594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-702e0b717a8153c4a4732bd755182dbe"></a>

### [`006d9f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f40.md) → [`006d9f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9f80.md) FUN_006d9f80

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
      "definition_site": "006d9fa0",
      "incomplete_value": false,
      "site": "006d9fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9f60",
      "incomplete_value": false,
      "site": "006d9f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "006d9fa4",
      "DATA",
      [
        "storage",
        "00c76398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9fa4",
      "DATA",
      [
        "storage",
        "00c76798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f40.md#insn-006d9f54) · [`006d9f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f40.md#insn-006d9f60)
- 新版 `006d9f94`（命令位置の公開資料なし） · `006d9fa0`（命令位置の公開資料なし）

~~~diff
- 006d9f54 ["INT_ADD", "register:40f0:8", ["const:6d9f54:8", "const:4:8"]]
- 006d9f54 ["CALL", null, ["callee:00c57e90:8"]]
+ 006d9f94 ["INT_ADD", "register:40f0:8", ["const:6d9f94:8", "const:4:8"]]
+ 006d9f94 ["CALL", null, ["callee:00c57e90:8"]]
- 006d9f54 bytes cff61594
+ 006d9f94 bytes bff71594
- 006d9f60 ["COPY", "tmp:0:8", ["const:398:8"]]
- 006d9f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9fa0 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 006d9fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9f60 bytes 08610e91
+ 006d9fa0 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae19f3e5ff7f1245f94cd84fc3ab59d"></a>

### [`006d9f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f78.md) → [`006d9fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9fb8.md) FUN_006d9fb8

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
      "definition_site": "006d9fbc",
      "incomplete_value": false,
      "site": "006d9fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9f7c",
      "incomplete_value": false,
      "site": "006d9f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
      "006d9fc0",
      "DATA",
      [
        "storage",
        "00c76398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9fc0",
      "DATA",
      [
        "storage",
        "00c76798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f78.md#insn-006d9f7c)
- 新版 `006d9fbc`（命令位置の公開資料なし）

~~~diff
- 006d9f7c ["COPY", "tmp:0:8", ["const:398:8"]]
- 006d9f7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9f7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9f7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9fbc ["COPY", "tmp:0:8", ["const:798:8"]]
+ 006d9fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9f7c bytes 08610e91
+ 006d9fbc bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb499c11f5be7d35a2c676e438d9778c"></a>

### [`006d9f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f98.md) → [`006d9fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9fd8.md) FUN_006d9fd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.87% / 新版 98.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da00c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9fcc",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da018",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9fd8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006da00c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006da00c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006da018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f98.md#insn-006d9fcc) · [`006d9fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f98.md#insn-006d9fd8) · [`006da064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f98.md#insn-006da064)
- 新版 `006da00c`（命令位置の公開資料なし） · `006da018`（命令位置の公開資料なし） · `006da0a4`（命令位置の公開資料なし）

~~~diff
- 006d9fcc ["INT_ADD", "register:40f0:8", ["const:6d9fcc:8", "const:4:8"]]
- 006d9fcc ["CALL", null, ["ram:47acb4:8"]]
+ 006da00c ["INT_ADD", "register:40f0:8", ["const:6da00c:8", "const:4:8"]]
+ 006da00c ["CALL", null, ["ram:47acf4:8"]]
- 006d9fcc bytes 3a83f697
+ 006da00c bytes 3a83f697
- 006d9fd8 ["INT_ADD", "register:40f0:8", ["const:6d9fd8:8", "const:4:8"]]
- 006d9fd8 ["CALL", null, ["ram:47acb4:8"]]
+ 006da018 ["INT_ADD", "register:40f0:8", ["const:6da018:8", "const:4:8"]]
+ 006da018 ["CALL", null, ["ram:47acf4:8"]]
- 006d9fd8 bytes 3783f697
+ 006da018 bytes 3783f697
- 006da064 ["INT_ADD", "register:40f0:8", ["const:6da064:8", "const:4:8"]]
- 006da064 ["CALL", null, ["callee:00c57e90:8"]]
+ 006da0a4 ["INT_ADD", "register:40f0:8", ["const:6da0a4:8", "const:4:8"]]
+ 006da0a4 ["CALL", null, ["callee:00c57e90:8"]]
- 006da064 bytes 8bf61594
+ 006da0a4 bytes 7bf71594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed9fe5738388af9ae3818b91fa27835d"></a>

### [`006da288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da288.md) → [`006da2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da2c8.md) FUN_006da2c8

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
      "definition_site": "006da2e8",
      "incomplete_value": false,
      "site": "006da2ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da2a8",
      "incomplete_value": false,
      "site": "006da2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "006da2ec",
      "DATA",
      [
        "storage",
        "00c76418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da2ec",
      "DATA",
      [
        "storage",
        "00c76818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da288.md#insn-006da29c) · [`006da2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da288.md#insn-006da2a8)
- 新版 `006da2dc`（命令位置の公開資料なし） · `006da2e8`（命令位置の公開資料なし）

~~~diff
- 006da29c ["INT_ADD", "register:40f0:8", ["const:6da29c:8", "const:4:8"]]
- 006da29c ["CALL", null, ["callee:00c57e90:8"]]
+ 006da2dc ["INT_ADD", "register:40f0:8", ["const:6da2dc:8", "const:4:8"]]
+ 006da2dc ["CALL", null, ["callee:00c57e90:8"]]
- 006da29c bytes fdf51594
+ 006da2dc bytes edf61594
- 006da2a8 ["COPY", "tmp:0:8", ["const:418:8"]]
- 006da2a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006da2a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006da2a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da2e8 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 006da2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006da2a8 bytes 08611091
+ 006da2e8 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2fb408376668982296529bb8267da78"></a>

### [`006da2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2c0.md) → [`006da300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da300.md) FUN_006da300

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
      "definition_site": "006da304",
      "incomplete_value": false,
      "site": "006da308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da2c4",
      "incomplete_value": false,
      "site": "006da2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
      "006da308",
      "DATA",
      [
        "storage",
        "00c76418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da308",
      "DATA",
      [
        "storage",
        "00c76818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2c0.md#insn-006da2c4)
- 新版 `006da304`（命令位置の公開資料なし）

~~~diff
- 006da2c4 ["COPY", "tmp:0:8", ["const:418:8"]]
- 006da2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006da2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006da2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da304 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 006da304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006da2c4 bytes 08611091
+ 006da304 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d19ad997605c51e2569a99651d8c138"></a>

### [`006da2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2e0.md) → [`006da320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da320.md) FUN_006da320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da598",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da558",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da5cc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da58c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006da598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da5cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006da598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006da5cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2e0.md#insn-006da518) · [`006da558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2e0.md#insn-006da558) · [`006da58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2e0.md#insn-006da58c)
- 新版 `006da558`（命令位置の公開資料なし） · `006da598`（命令位置の公開資料なし） · `006da5cc`（命令位置の公開資料なし）

~~~diff
- 006da518 ["INT_ADD", "register:40f0:8", ["const:6da518:8", "const:4:8"]]
- 006da518 ["CALL", null, ["callee:0043bba4:8"]]
+ 006da558 ["INT_ADD", "register:40f0:8", ["const:6da558:8", "const:4:8"]]
+ 006da558 ["CALL", null, ["callee:0043bba4:8"]]
- 006da518 bytes 9385f597
+ 006da558 bytes 9385f597
- 006da558 ["INT_ADD", "register:40f0:8", ["const:6da558:8", "const:4:8"]]
- 006da558 ["CALL", null, ["ram:47acb4:8"]]
+ 006da598 ["INT_ADD", "register:40f0:8", ["const:6da598:8", "const:4:8"]]
+ 006da598 ["CALL", null, ["ram:47acf4:8"]]
- 006da558 bytes d781f697
+ 006da598 bytes d781f697
- 006da58c ["INT_ADD", "register:40f0:8", ["const:6da58c:8", "const:4:8"]]
- 006da58c ["CALL", null, ["ram:47acb4:8"]]
+ 006da5cc ["INT_ADD", "register:40f0:8", ["const:6da5cc:8", "const:4:8"]]
+ 006da5cc ["CALL", null, ["ram:47acf4:8"]]
- 006da58c bytes ca81f697
+ 006da5cc bytes ca81f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4119f73fa6409cb95618b1d9a4c4f0f0"></a>

### [`006da5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da5e0.md) → [`006da620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da620.md) FUN_006da620

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
      "definition_site": "006da644",
      "incomplete_value": false,
      "site": "006da644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da604",
      "incomplete_value": false,
      "site": "006da604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
      "006da644",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da644",
      "DATA",
      [
        "storage",
        "00c76898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da5e0.md#insn-006da5f4) · [`006da600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da5e0.md#insn-006da600)
- 新版 `006da634`（命令位置の公開資料なし） · `006da640`（命令位置の公開資料なし）

~~~diff
- 006da5f4 ["INT_ADD", "register:40f0:8", ["const:6da5f4:8", "const:4:8"]]
- 006da5f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 006da634 ["INT_ADD", "register:40f0:8", ["const:6da634:8", "const:4:8"]]
+ 006da634 ["CALL", null, ["callee:00c57e90:8"]]
- 006da5f4 bytes 27f51594
+ 006da634 bytes 17f61594
- 006da600 ["COPY", "tmp:0:8", ["const:498:8"]]
- 006da600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006da600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006da600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da640 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 006da640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006da600 bytes 08611291
+ 006da640 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3781c6fd89453dd08f3336650d6ab9ef"></a>

### [`006da614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da614.md) → [`006da654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da654.md) FUN_006da654

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
      "definition_site": "006da660",
      "incomplete_value": false,
      "site": "006da660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da620",
      "incomplete_value": false,
      "site": "006da620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
      "006da660",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da660",
      "DATA",
      [
        "storage",
        "00c76898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da614.md#insn-006da61c)
- 新版 `006da65c`（命令位置の公開資料なし）

~~~diff
- 006da61c ["COPY", "tmp:0:8", ["const:498:8"]]
- 006da61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006da61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006da61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006da65c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 006da65c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006da65c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006da65c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006da61c bytes 29611291
+ 006da65c bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d20c65dc71363f1b5f458312a898d138"></a>

### [`006da630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md) → [`006da670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da670.md) FUN_006da670

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006da740",
      "incomplete_value": true,
      "site": "006da740",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:9e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da700",
      "incomplete_value": true,
      "site": "006da700",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:9a0:8"
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
      "definition_site": "006da744",
      "incomplete_value": true,
      "site": "006da744",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006da704",
      "incomplete_value": true,
      "site": "006da704",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da6a4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da664",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "006da6a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da6c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da6fc",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "006da6a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006da6c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006da6fc",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md#insn-006da664) · [`006da680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md#insn-006da680) · [`006da6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md#insn-006da6c0)
- 新版 `006da6a4`（命令位置の公開資料なし） · `006da6c0`（命令位置の公開資料なし） · `006da700`（命令位置の公開資料なし）

~~~diff
- 006da664 ["INT_ADD", "register:40f0:8", ["const:6da664:8", "const:4:8"]]
- 006da664 ["CALL", null, ["ram:47acb4:8"]]
+ 006da6a4 ["INT_ADD", "register:40f0:8", ["const:6da6a4:8", "const:4:8"]]
+ 006da6a4 ["CALL", null, ["ram:47acf4:8"]]
- 006da664 bytes 9481f697
+ 006da6a4 bytes 9481f697
- 006da680 ["INT_ADD", "register:40f0:8", ["const:6da680:8", "const:4:8"]]
- 006da680 ["CALL", null, ["ram:47acb4:8"]]
+ 006da6c0 ["INT_ADD", "register:40f0:8", ["const:6da6c0:8", "const:4:8"]]
+ 006da6c0 ["CALL", null, ["ram:47acf4:8"]]
- 006da680 bytes 8d81f697
+ 006da6c0 bytes 8d81f697
- 006da6c0 ["INT_ADD", "register:40f0:8", ["const:6da6c0:8", "const:4:8"]]
- 006da6c0 ["CALL", null, ["callee:008514f8:8"]]
+ 006da700 ["INT_ADD", "register:40f0:8", ["const:6da700:8", "const:4:8"]]
+ 006da700 ["CALL", null, ["callee:008514f8:8"]]
- 006da6c0 bytes 7edb0594
+ 006da700 bytes 7edb0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414df86e8817f9ee3932e02e92fe8c97"></a>

### [`006da7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da7dc.md) → [`006da81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da81c.md) _INIT_109

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006da858",
      "incomplete_value": true,
      "site": "006da874",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da818",
      "incomplete_value": true,
      "site": "006da834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "006da87c",
      "incomplete_value": true,
      "site": "006da898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006da83c",
      "incomplete_value": true,
      "site": "006da858",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006da89c",
      "incomplete_value": true,
      "site": "006da8b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006da85c",
      "incomplete_value": true,
      "site": "006da878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006da858",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006da87c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "006da89c",
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
      "006da858",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "006da87c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "006da89c",
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

- 旧版 [`006da854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da7dc.md#insn-006da854) · [`006da874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da7dc.md#insn-006da874) · [`006da93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da7dc.md#insn-006da93c)
- 新版 `006da894`（命令位置の公開資料なし） · `006da8b4`（命令位置の公開資料なし） · `006da97c`（命令位置の公開資料なし）

~~~diff
- 006da854 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 006da854 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006da854 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006da854 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006da894 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 006da894 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006da894 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006da894 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006da854 bytes 4a093691
+ 006da894 bytes 4a093791
- 006da874 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 006da874 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 006da874 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 006da874 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 006da8b4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 006da8b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 006da8b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 006da8b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 006da874 bytes 4a553a91
+ 006da8b4 bytes 4a893d91
- 006da93c ["INT_ADD", "register:40f0:8", ["const:6da93c:8", "const:4:8"]]
- 006da93c ["CALL", null, ["callee:0043b7f8:8"]]
+ 006da97c ["INT_ADD", "register:40f0:8", ["const:6da97c:8", "const:4:8"]]
+ 006da97c ["CALL", null, ["callee:0043b7f8:8"]]
- 006da93c bytes 9f83f597
+ 006da97c bytes 9f83f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ff09fe106450780202f62d8b093187"></a>

### [`006dad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md) → [`006dad74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006dad74.md) FUN_006dad74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 9件 [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`006dab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 9件 [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`006dabac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006dabac.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.00% / 新版 87.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006dada8",
      "incomplete_value": false,
      "site": "006dadb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dad68",
      "incomplete_value": false,
      "site": "006dad70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "006dae64",
      "incomplete_value": true,
      "site": "006dae68",
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
      "definition_site": "006dae24",
      "incomplete_value": true,
      "site": "006dae28",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dae60",
      "incomplete_value": true,
      "site": "006dae6c",
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
      "definition_site": "006dae20",
      "incomplete_value": true,
      "site": "006dae2c",
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
      "006dadb0",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006dadc4",
      "READ",
      [
        "storage",
        "002b763b",
        null,
        "string"
      ]
    ],
    [
      "006dae54",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006dadb0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006dadc4",
      "READ",
      [
        "storage",
        "002b767b",
        null,
        "string"
      ]
    ],
    [
      "006dae54",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md#insn-006dae6c) · [`006dad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md#insn-006dad60) · [`006dad68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md#insn-006dad68)
- 新版 `006daeac`（命令位置の公開資料なし） · `006dada0`（命令位置の公開資料なし） · `006dada8`（命令位置の公開資料なし）

~~~diff
- 006dae6c ["INT_ADD", "register:40f0:8", ["const:6dae6c:8", "const:4:8"]]
- 006dae6c ["CALL", null, ["callee:00c57fb0:8"]]
+ 006daeac ["INT_ADD", "register:40f0:8", ["const:6daeac:8", "const:4:8"]]
+ 006daeac ["CALL", null, ["callee:00c57fb0:8"]]
- 006dae6c bytes 51f31594
+ 006daeac bytes 41f41594
- 006dad60 ["INT_ADD", "register:40f0:8", ["const:6dad60:8", "const:4:8"]]
- 006dad60 ["CALL", null, ["callee:00487e20:8"]]
+ 006dada0 ["INT_ADD", "register:40f0:8", ["const:6dada0:8", "const:4:8"]]
+ 006dada0 ["CALL", null, ["callee:00487e20:8"]]
- 006dad60 bytes 20b4f697
+ 006dada0 bytes 20b4f697
- 006dad68 ["COPY", "tmp:0:8", ["const:938:8"]]
- 006dad68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006dad68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006dad68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006dada8 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 006dada8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006dada8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006dada8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006dad68 bytes 08e12491
+ 006dada8 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-712236f370c604e6440d7ba44a5115a0"></a>

### [`006db088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db088.md) → [`006db0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db0c8.md) FUN_006db0c8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006db108",
      "incomplete_value": false,
      "site": "006db10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db0c8",
      "incomplete_value": false,
      "site": "006db0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "006db128",
      "incomplete_value": true,
      "site": "006db134",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db0e8",
      "incomplete_value": true,
      "site": "006db0f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
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
      "definition_site": "006db124",
      "incomplete_value": true,
      "site": "006db138",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db0e4",
      "incomplete_value": true,
      "site": "006db0f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c3:8"
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
      "006db10c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006db124",
      "READ",
      [
        "storage",
        "002ad9c3",
        null,
        "string"
      ]
    ],
    [
      "006db124",
      "READ",
      [
        "storage",
        "002ad9d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006db10c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006db124",
      "READ",
      [
        "storage",
        "002ada03",
        null,
        "string"
      ]
    ],
    [
      "006db124",
      "READ",
      [
        "storage",
        "002ada13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006db134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db088.md#insn-006db134) · [`006db2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db088.md#insn-006db2ec) · [`006db0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db088.md#insn-006db0c0)
- 新版 `006db174`（命令位置の公開資料なし） · `006db32c`（命令位置の公開資料なし） · `006db100`（命令位置の公開資料なし）

~~~diff
- 006db134 ["INT_ADD", "register:40f0:8", ["const:6db134:8", "const:4:8"]]
- 006db134 ["CALL", null, ["callee:0048791c:8"]]
+ 006db174 ["INT_ADD", "register:40f0:8", ["const:6db174:8", "const:4:8"]]
+ 006db174 ["CALL", null, ["callee:0048791c:8"]]
- 006db134 bytes eab1f697
+ 006db174 bytes eab1f697
- 006db2ec ["INT_ADD", "register:40f0:8", ["const:6db2ec:8", "const:4:8"]]
- 006db2ec ["CALL", null, ["callee:00c57fb0:8"]]
+ 006db32c ["INT_ADD", "register:40f0:8", ["const:6db32c:8", "const:4:8"]]
+ 006db32c ["CALL", null, ["callee:00c57fb0:8"]]
- 006db2ec bytes 31f21594
+ 006db32c bytes 21f31594
- 006db0c0 ["INT_ADD", "register:40f0:8", ["const:6db0c0:8", "const:4:8"]]
- 006db0c0 ["CALL", null, ["callee:00487e20:8"]]
+ 006db100 ["INT_ADD", "register:40f0:8", ["const:6db100:8", "const:4:8"]]
+ 006db100 ["CALL", null, ["callee:00487e20:8"]]
- 006db0c0 bytes 48b3f697
+ 006db100 bytes 48b3f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3230602d887031d9d6dd86655d149697"></a>

### [`006db3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md) → [`006db3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006db3e0.md) FUN_006db3e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · 呼出先 27件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) · 呼出先 27件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.68% / 新版 89.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006db49c",
      "incomplete_value": true,
      "site": "006db4b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:32c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db45c",
      "incomplete_value": true,
      "site": "006db470",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:25f:8"
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
      "definition_site": "006db4d0",
      "incomplete_value": true,
      "site": "006db4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
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
    "old": {
      "definition_site": "006db490",
      "incomplete_value": true,
      "site": "006db49c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:4b6:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006db620",
      "incomplete_value": false,
      "site": "006db620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db5e0",
      "incomplete_value": false,
      "site": "006db5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006db45c",
      "READ",
      [
        "storage",
        "00ca7914",
        null,
        "undefined4"
      ]
    ],
    [
      "006db478",
      "READ",
      [
        "storage",
        "00ca7910",
        null,
        "undefined4"
      ]
    ],
    [
      "006db49c",
      "READ",
      [
        "storage",
        "0029f25f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006db45c",
      "READ",
      [
        "storage",
        "00ca7d14",
        null,
        "undefined4"
      ]
    ],
    [
      "006db478",
      "READ",
      [
        "storage",
        "00ca7d10",
        null,
        "undefined4"
      ]
    ],
    [
      "006db49c",
      "READ",
      [
        "storage",
        "0029f32c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006db50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md#insn-006db50c) · [`006db744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md#insn-006db744) · [`006db794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md#insn-006db794)
- 新版 `006db54c`（命令位置の公開資料なし） · `006db784`（命令位置の公開資料なし） · `006db7d4`（命令位置の公開資料なし）

~~~diff
- 006db50c ["INT_ADD", "register:40f0:8", ["const:6db50c:8", "const:4:8"]]
- 006db50c ["CALL", null, ["ram:664860:8"]]
+ 006db54c ["INT_ADD", "register:40f0:8", ["const:6db54c:8", "const:4:8"]]
+ 006db54c ["CALL", null, ["ram:6648a0:8"]]
- 006db50c bytes d524fe97
+ 006db54c bytes d524fe97
- 006db744 ["INT_ADD", "register:40f0:8", ["const:6db744:8", "const:4:8"]]
- 006db744 ["CALL", null, ["callee:0047e60c:8"]]
+ 006db784 ["INT_ADD", "register:40f0:8", ["const:6db784:8", "const:4:8"]]
+ 006db784 ["CALL", null, ["callee:0047e60c:8"]]
- 006db744 bytes a28bf697
+ 006db784 bytes a28bf697
- 006db794 ["INT_ADD", "register:40f0:8", ["const:6db794:8", "const:4:8"]]
- 006db794 ["CALL", null, ["callee:00c53d00:8"]]
+ 006db7d4 ["INT_ADD", "register:40f0:8", ["const:6db7d4:8", "const:4:8"]]
+ 006db7d4 ["CALL", null, ["callee:00c53d00:8"]]
- 006db794 bytes 53e01594
+ 006db7d4 bytes 4be11594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20de38fea6e2192b706c5b5bfcc4745c"></a>

### [`006dc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md) → [`006dc114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc114.md) FUN_006dc114

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0071cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071cff4.md) [`007287f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007287f8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006dbda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006dbda8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0071d034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d034.md) [`00728838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728838.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006dc374",
      "incomplete_value": false,
      "site": "006dc378",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc334",
      "incomplete_value": false,
      "site": "006dc338",
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
            "const:f0:8"
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
      "006dc374",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "006dc3a0",
      "READ",
      [
        "storage",
        "00ca7914",
        null,
        "undefined4"
      ]
    ],
    [
      "006dc3bc",
      "READ",
      [
        "storage",
        "00ca7910",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "006dc374",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "006dc3a0",
      "READ",
      [
        "storage",
        "00ca7d14",
        null,
        "undefined4"
      ]
    ],
    [
      "006dc3bc",
      "READ",
      [
        "storage",
        "00ca7d10",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dc338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md#insn-006dc338) · [`006dc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md#insn-006dc378) · [`006dc194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md#insn-006dc194)
- 新版 `006dc378`（命令位置の公開資料なし） · `006dc3b8`（命令位置の公開資料なし） · `006dc1d4`（命令位置の公開資料なし）

~~~diff
- 006dc338 ["INT_ADD", "register:40f0:8", ["const:6dc338:8", "const:4:8"]]
- 006dc338 ["CALL", null, ["callee:00442930:8"]]
+ 006dc378 ["INT_ADD", "register:40f0:8", ["const:6dc378:8", "const:4:8"]]
+ 006dc378 ["CALL", null, ["callee:00442930:8"]]
- 006dc338 bytes 6e99f597
+ 006dc378 bytes 6e99f597
- 006dc378 ["COPY", "tmp:0:8", ["const:910:8"]]
- 006dc378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006dc378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006dc378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006dc3b8 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 006dc3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006dc3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006dc3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006dc378 bytes 08412491
+ 006dc3b8 bytes 08413491
- 006dc194 ["INT_ADD", "register:40f0:8", ["const:6dc194:8", "const:4:8"]]
- 006dc194 ["CALL", null, ["callee:0071d034:8"]]
+ 006dc1d4 ["INT_ADD", "register:40f0:8", ["const:6dc1d4:8", "const:4:8"]]
+ 006dc1d4 ["CALL", null, ["callee:0071d034:8"]]
- 006dc194 bytes 98030194
+ 006dc1d4 bytes 98030194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c87415fe618df583745082db4c4ec8da"></a>

### [`006dc900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md) → [`006dc940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc940.md) FUN_006dc940

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f0614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md) · 呼出先 18件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md)
- 新版 呼出元 1件 [`006f0654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0654.md) · 呼出先 18件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0046f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md) [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.60% / 新版 87.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 7件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dc9bc",
      "incomplete_value": true,
      "site": "006dc9d0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc97c",
      "incomplete_value": true,
      "site": "006dc990",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e43:8"
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
      "definition_site": "006dc9bc",
      "incomplete_value": true,
      "site": "006dc9d4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc97c",
      "incomplete_value": true,
      "site": "006dc994",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e43:8"
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
      "definition_site": "006dcbf0",
      "incomplete_value": true,
      "site": "006dcc00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dcbb0",
      "incomplete_value": true,
      "site": "006dcbc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f26:8"
              ]
            ]
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
      "006dc970",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dc984",
      "READ",
      [
        "storage",
        "002a2292",
        null,
        "string"
      ]
    ],
    [
      "006dc9bc",
      "READ",
      [
        "storage",
        "002b2e43",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dc970",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dc984",
      "READ",
      [
        "storage",
        "002a235f",
        null,
        "string"
      ]
    ],
    [
      "006dc9bc",
      "READ",
      [
        "storage",
        "002b2e83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dc9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md#insn-006dc9cc) · [`006dcc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md#insn-006dcc44) · [`006dcc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md#insn-006dcc84)
- 新版 `006dca0c`（命令位置の公開資料なし） · `006dcc84`（命令位置の公開資料なし） · `006dccc4`（命令位置の公開資料なし）

~~~diff
- 006dc9cc ["INT_ADD", "register:40f0:8", ["const:6dc9cc:8", "const:4:8"]]
- 006dc9cc ["CALL", null, ["callee:0047e60c:8"]]
+ 006dca0c ["INT_ADD", "register:40f0:8", ["const:6dca0c:8", "const:4:8"]]
+ 006dca0c ["CALL", null, ["callee:0047e60c:8"]]
- 006dc9cc bytes 0087f697
+ 006dca0c bytes 0087f697
- 006dcc44 ["INT_ADD", "register:40f0:8", ["const:6dcc44:8", "const:4:8"]]
- 006dcc44 ["CALL", null, ["callee:0046e970:8"]]
+ 006dcc84 ["INT_ADD", "register:40f0:8", ["const:6dcc84:8", "const:4:8"]]
+ 006dcc84 ["CALL", null, ["callee:0046e970:8"]]
- 006dcc44 bytes 3b47f697
+ 006dcc84 bytes 3b47f697
- 006dcc84 ["INT_ADD", "register:40f0:8", ["const:6dcc84:8", "const:4:8"]]
- 006dcc84 ["CALL", null, ["callee:008514f8:8"]]
+ 006dccc4 ["INT_ADD", "register:40f0:8", ["const:6dccc4:8", "const:4:8"]]
+ 006dccc4 ["CALL", null, ["callee:008514f8:8"]]
- 006dcc84 bytes 0dd20594
+ 006dccc4 bytes 0dd20594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f060c7e8785e61bfcace45eb1725c27"></a>

### [`006dd430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md) → [`006dd470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dd/006dd470.md) FUN_006dd470

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 10件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 10件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dd4b4",
      "incomplete_value": true,
      "site": "006dd4c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:35f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dd474",
      "incomplete_value": true,
      "site": "006dd484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:292:8"
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
      "definition_site": "006dd4e4",
      "incomplete_value": true,
      "site": "006dd4f8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:e83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dd4a4",
      "incomplete_value": true,
      "site": "006dd4b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:e43:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "006dd658",
      "incomplete_value": false,
      "site": "006dd658",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "006dd618",
      "incomplete_value": false,
      "site": "006dd618",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dd4a0",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd4b4",
      "READ",
      [
        "storage",
        "002a2292",
        null,
        "string"
      ]
    ],
    [
      "006dd4e4",
      "READ",
      [
        "storage",
        "002b2e43",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dd4a0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd4b4",
      "READ",
      [
        "storage",
        "002a235f",
        null,
        "string"
      ]
    ],
    [
      "006dd4e4",
      "READ",
      [
        "storage",
        "002b2e83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dd4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md#insn-006dd4ec) · [`006dd5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md#insn-006dd5e8) · [`006dd5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md#insn-006dd5f0)
- 新版 `006dd52c`（命令位置の公開資料なし） · `006dd628`（命令位置の公開資料なし） · `006dd630`（命令位置の公開資料なし）

~~~diff
- 006dd4ec ["INT_ADD", "register:40f0:8", ["const:6dd4ec:8", "const:4:8"]]
- 006dd4ec ["CALL", null, ["callee:0047e60c:8"]]
+ 006dd52c ["INT_ADD", "register:40f0:8", ["const:6dd52c:8", "const:4:8"]]
+ 006dd52c ["CALL", null, ["callee:0047e60c:8"]]
- 006dd4ec bytes 3884f697
+ 006dd52c bytes 3884f697
- 006dd5e8 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 006dd5e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006dd5e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006dd5e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006dd628 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 006dd628 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006dd628 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006dd628 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006dd5e8 bytes 00e02c91
+ 006dd628 bytes 00e03c91
- 006dd5f0 ["INT_ADD", "register:40f0:8", ["const:6dd5f0:8", "const:4:8"]]
- 006dd5f0 ["CALL", null, ["callee:00c57e50:8"]]
+ 006dd630 ["INT_ADD", "register:40f0:8", ["const:6dd630:8", "const:4:8"]]
+ 006dd630 ["CALL", null, ["callee:00c57e50:8"]]
- 006dd5f0 bytes 18e91594
+ 006dd630 bytes 08ea1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67261909055a530d0c0f81dbd53d1c8b"></a>

### [`006dd6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd6e4.md) → [`006dd724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dd/006dd724.md) FUN_006dd724

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`006dc8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc8c4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006b2b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2b5c.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 5件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`006dc904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc904.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ddcc4",
      "incomplete_value": true,
      "site": "006ddcd4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ddc84",
      "incomplete_value": true,
      "site": "006ddc94",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f20:8"
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
      "definition_site": "006dde3c",
      "incomplete_value": true,
      "site": "006dde4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dddfc",
      "incomplete_value": true,
      "site": "006dde0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006dd8d4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006dd894",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006dd744",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[35]"
      ]
    ],
    [
      "006dd758",
      "DATA",
      [
        "storage",
        "004341b0",
        null,
        "uleb128"
      ]
    ],
    [
      "006dd76c",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[35]"
      ]
    ]
  ],
  "added": [
    [
      "006dd744",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[43]"
      ]
    ],
    [
      "006dd758",
      "DATA",
      [
        "storage",
        "004341b0",
        null,
        "dword"
      ]
    ],
    [
      "006dd76c",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[43]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dd894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd6e4.md#insn-006dd894) · [`006dda14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd6e4.md#insn-006dda14) · [`006dda40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd6e4.md#insn-006dda40)
- 新版 `006dd8d4`（命令位置の公開資料なし） · `006dda54`（命令位置の公開資料なし） · `006dda80`（命令位置の公開資料なし）

~~~diff
- 006dd894 ["INT_ADD", "register:40f0:8", ["const:6dd894:8", "const:4:8"]]
- 006dd894 ["CALL", null, ["ram:46c984:8"]]
+ 006dd8d4 ["INT_ADD", "register:40f0:8", ["const:6dd8d4:8", "const:4:8"]]
+ 006dd8d4 ["CALL", null, ["ram:46c9c4:8"]]
- 006dd894 bytes 3c3cf697
+ 006dd8d4 bytes 3c3cf697
- 006dda14 ["INT_ADD", "register:40f0:8", ["const:6dda14:8", "const:4:8"]]
- 006dda14 ["CALL", null, ["ram:46c984:8"]]
+ 006dda54 ["INT_ADD", "register:40f0:8", ["const:6dda54:8", "const:4:8"]]
+ 006dda54 ["CALL", null, ["ram:46c9c4:8"]]
- 006dda14 bytes dc3bf697
+ 006dda54 bytes dc3bf697
- 006dda40 ["INT_ADD", "register:40f0:8", ["const:6dda40:8", "const:4:8"]]
- 006dda40 ["CALL", null, ["ram:46c984:8"]]
+ 006dda80 ["INT_ADD", "register:40f0:8", ["const:6dda80:8", "const:4:8"]]
+ 006dda80 ["CALL", null, ["ram:46c9c4:8"]]
- 006dda40 bytes d13bf697
+ 006dda80 bytes d13bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ed318dff4a15c1869b422f6587512c"></a>

### [`006de6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de6d4.md) → [`006de714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de714.md) FUN_006de714

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 3件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 3件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "006de74c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006de70c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006de74c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006de74c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006de70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de6d4.md#insn-006de70c) · [`006de6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de6d4.md#insn-006de6ec) · [`006de708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de6d4.md#insn-006de708)
- 新版 `006de74c`（命令位置の公開資料なし） · `006de72c`（命令位置の公開資料なし） · `006de748`（命令位置の公開資料なし）

~~~diff
- 006de70c ["INT_ADD", "register:40f0:8", ["const:6de70c:8", "const:4:8"]]
- 006de70c ["CALL", null, ["ram:46c984:8"]]
+ 006de74c ["INT_ADD", "register:40f0:8", ["const:6de74c:8", "const:4:8"]]
+ 006de74c ["CALL", null, ["ram:46c9c4:8"]]
- 006de70c bytes 9e38f697
+ 006de74c bytes 9e38f697
- 006de6ec ["INT_ADD", "register:40f0:8", ["const:6de6ec:8", "const:4:8"]]
- 006de6ec ["CALL", null, ["callee:0046d7b0:8"]]
+ 006de72c ["INT_ADD", "register:40f0:8", ["const:6de72c:8", "const:4:8"]]
+ 006de72c ["CALL", null, ["callee:0046d7b0:8"]]
- 006de6ec bytes 213cf697
+ 006de72c bytes 213cf697
- 006de708 ["INT_ADD", "register:40f0:8", ["const:6de708:8", "const:4:8"]]
- 006de708 ["CALL", null, ["callee:008514f8:8"]]
+ 006de748 ["INT_ADD", "register:40f0:8", ["const:6de748:8", "const:4:8"]]
+ 006de748 ["CALL", null, ["callee:008514f8:8"]]
- 006de708 bytes 6ccb0594
+ 006de748 bytes 6ccb0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de74565e6324e8669b43f00f0038d388"></a>

### [`006de7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de7d8.md) → [`006de818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de818.md) FUN_006de818

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 5件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006de9e8",
      "incomplete_value": true,
      "site": "006de9f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "old": {
      "definition_site": "006de9a8",
      "incomplete_value": true,
      "site": "006de9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:d10:8"
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006de854",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006de814",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006de854",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006de9e8",
      "READ",
      [
        "storage",
        "002c3d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006de854",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006de9e8",
      "READ",
      [
        "storage",
        "002c3d50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006de814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de7d8.md#insn-006de814) · [`006de810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de7d8.md#insn-006de810) · [`006de82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de7d8.md#insn-006de82c)
- 新版 `006de854`（命令位置の公開資料なし） · `006de850`（命令位置の公開資料なし） · `006de86c`（命令位置の公開資料なし）

~~~diff
- 006de814 ["INT_ADD", "register:40f0:8", ["const:6de814:8", "const:4:8"]]
- 006de814 ["CALL", null, ["ram:46c984:8"]]
+ 006de854 ["INT_ADD", "register:40f0:8", ["const:6de854:8", "const:4:8"]]
+ 006de854 ["CALL", null, ["ram:46c9c4:8"]]
- 006de814 bytes 5c38f697
+ 006de854 bytes 5c38f697
- 006de810 ["INT_ADD", "register:40f0:8", ["const:6de810:8", "const:4:8"]]
- 006de810 ["CALL", null, ["callee:008514f8:8"]]
+ 006de850 ["INT_ADD", "register:40f0:8", ["const:6de850:8", "const:4:8"]]
+ 006de850 ["CALL", null, ["callee:008514f8:8"]]
- 006de810 bytes 2acb0594
+ 006de850 bytes 2acb0594
- 006de82c ["INT_ADD", "register:40f0:8", ["const:6de82c:8", "const:4:8"]]
- 006de82c ["CALL", null, ["callee:0046d7b0:8"]]
+ 006de86c ["INT_ADD", "register:40f0:8", ["const:6de86c:8", "const:4:8"]]
+ 006de86c ["CALL", null, ["callee:0046d7b0:8"]]
- 006de82c bytes d13bf697
+ 006de86c bytes d13bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d66747d092863865e5d21b04981732e0"></a>

### [`006dea54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006dea54.md) → [`006dea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006dea94.md) FUN_006dea94

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 11件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 2件 [`006b2b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2b5c.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 11件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006df034",
      "incomplete_value": true,
      "site": "006df03c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006deff4",
      "incomplete_value": true,
      "site": "006deffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006debbc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006deb7c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006decdc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006dec9c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 32,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dead4",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[35]"
      ]
    ],
    [
      "006deb10",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "byte[23]"
      ]
    ],
    [
      "006deb24",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "006dead4",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[43]"
      ]
    ],
    [
      "006deb10",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "dword"
      ]
    ],
    [
      "006deb24",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006deb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006dea54.md#insn-006deb3c) · [`006deb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006dea54.md#insn-006deb7c) · [`006dec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006dea54.md#insn-006dec9c)
- 新版 `006deb7c`（命令位置の公開資料なし） · `006debbc`（命令位置の公開資料なし） · `006decdc`（命令位置の公開資料なし）

~~~diff
- 006deb3c ["INT_ADD", "register:40f0:8", ["const:6deb3c:8", "const:4:8"]]
- 006deb3c ["CALL", null, ["callee:008514f8:8"]]
+ 006deb7c ["INT_ADD", "register:40f0:8", ["const:6deb7c:8", "const:4:8"]]
+ 006deb7c ["CALL", null, ["callee:008514f8:8"]]
- 006deb3c bytes 5fca0594
+ 006deb7c bytes 5fca0594
- 006deb7c ["INT_ADD", "register:40f0:8", ["const:6deb7c:8", "const:4:8"]]
- 006deb7c ["CALL", null, ["ram:47acb4:8"]]
+ 006debbc ["INT_ADD", "register:40f0:8", ["const:6debbc:8", "const:4:8"]]
+ 006debbc ["CALL", null, ["ram:47acf4:8"]]
- 006deb7c bytes 4e70f697
+ 006debbc bytes 4e70f697
- 006dec9c ["INT_ADD", "register:40f0:8", ["const:6dec9c:8", "const:4:8"]]
- 006dec9c ["CALL", null, ["ram:47acb4:8"]]
+ 006decdc ["INT_ADD", "register:40f0:8", ["const:6decdc:8", "const:4:8"]]
+ 006decdc ["CALL", null, ["ram:47acf4:8"]]
- 006dec9c bytes 0670f697
+ 006decdc bytes 0670f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b1cadbf3dfae43700a45aa5f7ce5df"></a>

### [`006dfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md) → [`006dfdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfdc8.md) FUN_006dfdc8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.99% / 新版 95.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006dfe14",
      "incomplete_value": false,
      "site": "006dfe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dfdd4",
      "incomplete_value": false,
      "site": "006dfde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "006dff04",
      "incomplete_value": true,
      "site": "006dff18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dfec4",
      "incomplete_value": true,
      "site": "006dfed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006e01e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dfe24",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006dff04",
      "READ",
      [
        "storage",
        "002a9f3c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006e01d8",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006dfe24",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006dff04",
      "READ",
      [
        "storage",
        "002aa009",
        null,
        "string"
      ]
    ],
    [
      "006e0218",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e01ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md#insn-006e01ac) · [`006e01e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md#insn-006e01e8) · [`006e01ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md#insn-006e01ec)
- 新版 `006e01ec`（命令位置の公開資料なし）

~~~diff
- 006e01ac ["INT_ADD", "register:40f0:8", ["const:6e01ac:8", "const:4:8"]]
- 006e01ac ["CALL", null, ["callee:0048799c:8"]]
+ 006e01ec ["INT_ADD", "register:40f0:8", ["const:6e01ec:8", "const:4:8"]]
+ 006e01ec ["CALL", null, ["callee:0048799c:8"]]
- 006e01ac bytes ec9df697
+ 006e01ec bytes ec9df697
- 006e01e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
- 006e01e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006e01e8 bytes e88300f9
- 006e01ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:148:8"]]
- 006e01ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006e01ec bytes e9a700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ecf993f5ac5b0de74650ae007dd5054"></a>

### [`006e046c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e046c.md) → [`006e04ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e04ac.md) FUN_006e04ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e04ec",
      "incomplete_value": false,
      "site": "006e04f0",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e04ac",
      "incomplete_value": false,
      "site": "006e04b0",
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
            "const:f0:8"
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
      "006e04ec",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e04ec",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e046c.md#insn-006e04b0) · [`006e04ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e046c.md#insn-006e04ac)
- 新版 `006e04f0`（命令位置の公開資料なし） · `006e04ec`（命令位置の公開資料なし）

~~~diff
- 006e04b0 ["INT_ADD", "register:40f0:8", ["const:6e04b0:8", "const:4:8"]]
- 006e04b0 ["CALL", null, ["callee:00442930:8"]]
+ 006e04f0 ["INT_ADD", "register:40f0:8", ["const:6e04f0:8", "const:4:8"]]
+ 006e04f0 ["CALL", null, ["callee:00442930:8"]]
- 006e04b0 bytes 1089f597
+ 006e04f0 bytes 1089f597
- 006e04ac ["COPY", "tmp:0:8", ["const:f0:8"]]
- 006e04ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006e04ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006e04ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006e04ec ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 006e04ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006e04ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006e04ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006e04ac bytes 00c00391
+ 006e04ec bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c55eddcc60e1c2f81a0b6efb5205ea94"></a>

### [`006e15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md) → [`006e15e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e15e0.md) FUN_006e15e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 24件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e1710",
      "incomplete_value": true,
      "site": "006e1710",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e16d0",
      "incomplete_value": true,
      "site": "006e16d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3a7:8"
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
      "definition_site": "006e181c",
      "incomplete_value": true,
      "site": "006e181c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f85:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e17dc",
      "incomplete_value": true,
      "site": "006e17dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006e1aa4",
      "incomplete_value": false,
      "site": "006e1aa4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "definition_site": "006e1a64",
      "incomplete_value": false,
      "site": "006e1a64",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
      "006e1610",
      "DATA",
      [
        "storage",
        "00434658",
        null,
        "dword"
      ]
    ],
    [
      "006e165c",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "006e1694",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006e1610",
      "DATA",
      [
        "storage",
        "00434658",
        "fde_00434658",
        "dword"
      ]
    ],
    [
      "006e165c",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "006e1694",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e1620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md#insn-006e1620) · [`006e1710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md#insn-006e1710) · [`006e1724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md#insn-006e1724)
- 新版 `006e1660`（命令位置の公開資料なし） · `006e1750`（命令位置の公開資料なし） · `006e1764`（命令位置の公開資料なし）

~~~diff
- 006e1620 ["INT_ADD", "register:40f0:8", ["const:6e1620:8", "const:4:8"]]
- 006e1620 ["CALL", null, ["callee:00442930:8"]]
+ 006e1660 ["INT_ADD", "register:40f0:8", ["const:6e1660:8", "const:4:8"]]
+ 006e1660 ["CALL", null, ["callee:00442930:8"]]
- 006e1620 bytes b484f597
+ 006e1660 bytes b484f597
- 006e1710 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 006e1710 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006e1710 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006e1710 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006e1750 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 006e1750 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006e1750 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006e1750 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006e1710 bytes 00002c91
+ 006e1750 bytes 00003c91
- 006e1724 ["INT_ADD", "register:40f0:8", ["const:6e1724:8", "const:4:8"]]
- 006e1724 ["CALL", null, ["callee:0047e60c:8"]]
+ 006e1764 ["INT_ADD", "register:40f0:8", ["const:6e1764:8", "const:4:8"]]
+ 006e1764 ["CALL", null, ["callee:0047e60c:8"]]
- 006e1724 bytes aa73f697
+ 006e1764 bytes aa73f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6e4b31dab0e042b33ca55eabec162e"></a>

### [`006e1da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1da0.md) → [`006e1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1de0.md) FUN_006e1de0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 5件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e1e40",
      "incomplete_value": true,
      "site": "006e1e54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e1e00",
      "incomplete_value": true,
      "site": "006e1e14",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f50:8"
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
      "site": "006e1dfc",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e1dbc",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006e1dfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006e1e40",
      "READ",
      [
        "storage",
        "002c3f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e1dfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006e1e40",
      "READ",
      [
        "storage",
        "002c3f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e1dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1da0.md#insn-006e1dbc) · [`006e1dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1da0.md#insn-006e1dd4) · [`006e1db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1da0.md#insn-006e1db8)
- 新版 `006e1dfc`（命令位置の公開資料なし） · `006e1e14`（命令位置の公開資料なし） · `006e1df8`（命令位置の公開資料なし）

~~~diff
- 006e1dbc ["INT_ADD", "register:40f0:8", ["const:6e1dbc:8", "const:4:8"]]
- 006e1dbc ["CALL", null, ["ram:46c984:8"]]
+ 006e1dfc ["INT_ADD", "register:40f0:8", ["const:6e1dfc:8", "const:4:8"]]
+ 006e1dfc ["CALL", null, ["ram:46c9c4:8"]]
- 006e1dbc bytes f22af697
+ 006e1dfc bytes f22af697
- 006e1dd4 ["INT_ADD", "register:40f0:8", ["const:6e1dd4:8", "const:4:8"]]
- 006e1dd4 ["CALL", null, ["callee:0046d7b0:8"]]
+ 006e1e14 ["INT_ADD", "register:40f0:8", ["const:6e1e14:8", "const:4:8"]]
+ 006e1e14 ["CALL", null, ["callee:0046d7b0:8"]]
- 006e1dd4 bytes 672ef697
+ 006e1e14 bytes 672ef697
- 006e1db8 ["INT_ADD", "register:40f0:8", ["const:6e1db8:8", "const:4:8"]]
- 006e1db8 ["CALL", null, ["callee:008514f8:8"]]
+ 006e1df8 ["INT_ADD", "register:40f0:8", ["const:6e1df8:8", "const:4:8"]]
+ 006e1df8 ["CALL", null, ["callee:008514f8:8"]]
- 006e1db8 bytes c0bd0594
+ 006e1df8 bytes c0bd0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca8d3314c1804c6ed643bbfe45ab3ff"></a>

### [`006e1e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1e68.md) → [`006e1ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1ea8.md) FUN_006e1ea8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 11件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 11件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.86% / 新版 97.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e1fb0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e1f70",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e20bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e207c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 30,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e227c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e223c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 41,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e1edc",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[35]"
      ]
    ],
    [
      "006e1f18",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "byte[23]"
      ]
    ],
    [
      "006e1f2c",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "006e1edc",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[43]"
      ]
    ],
    [
      "006e1f18",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "dword"
      ]
    ],
    [
      "006e1f2c",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e1f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1e68.md#insn-006e1f30) · [`006e1f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1e68.md#insn-006e1f70) · [`006e207c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1e68.md#insn-006e207c)
- 新版 `006e1f70`（命令位置の公開資料なし） · `006e1fb0`（命令位置の公開資料なし） · `006e20bc`（命令位置の公開資料なし）

~~~diff
- 006e1f30 ["INT_ADD", "register:40f0:8", ["const:6e1f30:8", "const:4:8"]]
- 006e1f30 ["CALL", null, ["callee:008514f8:8"]]
+ 006e1f70 ["INT_ADD", "register:40f0:8", ["const:6e1f70:8", "const:4:8"]]
+ 006e1f70 ["CALL", null, ["callee:008514f8:8"]]
- 006e1f30 bytes 62bd0594
+ 006e1f70 bytes 62bd0594
- 006e1f70 ["INT_ADD", "register:40f0:8", ["const:6e1f70:8", "const:4:8"]]
- 006e1f70 ["CALL", null, ["ram:47acb4:8"]]
+ 006e1fb0 ["INT_ADD", "register:40f0:8", ["const:6e1fb0:8", "const:4:8"]]
+ 006e1fb0 ["CALL", null, ["ram:47acf4:8"]]
- 006e1f70 bytes 5163f697
+ 006e1fb0 bytes 5163f697
- 006e207c ["INT_ADD", "register:40f0:8", ["const:6e207c:8", "const:4:8"]]
- 006e207c ["CALL", null, ["ram:47acb4:8"]]
+ 006e20bc ["INT_ADD", "register:40f0:8", ["const:6e20bc:8", "const:4:8"]]
+ 006e20bc ["CALL", null, ["ram:47acf4:8"]]
- 006e207c bytes 0e63f697
+ 006e20bc bytes 0e63f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

