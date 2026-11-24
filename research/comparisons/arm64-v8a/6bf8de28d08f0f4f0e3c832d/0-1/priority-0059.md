# v16.0.0 → v16.0.1 · 最優先の変更候補 (59)

[一覧の目次](README.md)

<a id="compare-b55635eb99dbe40a643bfc364ed5c396"></a>

### [`00a02568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02568.md) → [`00a02704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md) FUN_00a02704

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "site": "00a0273c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a025a0",
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
      "site": "00a02754",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a025b8",
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
      "00a0273c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a02754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a0273c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a02754",
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

- 旧版 [`00a025a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02568.md#insn-00a025a0) · [`00a025b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02568.md#insn-00a025b8) · [`00a02584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02568.md#insn-00a02584)
- 新版 [`00a0273c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a0273c) · [`00a02754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a02754) · [`00a02720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02704.md#insn-00a02720)

~~~diff
- 00a025a0 ["INT_ADD", "register:40f0:8", ["const:a025a0:8", "const:4:8"]]
- 00a025a0 ["CALL", null, ["ram:47acb4:8"]]
+ 00a0273c ["INT_ADD", "register:40f0:8", ["const:a0273c:8", "const:4:8"]]
+ 00a0273c ["CALL", null, ["ram:47acf4:8"]]
- 00a025a0 bytes c5e1e997
+ 00a0273c bytes 6ee1e997
- 00a025b8 ["INT_ADD", "register:40f0:8", ["const:a025b8:8", "const:4:8"]]
- 00a025b8 ["CALL", null, ["ram:47acb4:8"]]
+ 00a02754 ["INT_ADD", "register:40f0:8", ["const:a02754:8", "const:4:8"]]
+ 00a02754 ["CALL", null, ["ram:47acf4:8"]]
- 00a025b8 bytes bfe1e997
+ 00a02754 bytes 68e1e997
- 00a02584 ["INT_ADD", "register:40f0:8", ["const:a02584:8", "const:4:8"]]
- 00a02584 ["CALL", null, ["callee:008b6f48:8"]]
+ 00a02720 ["INT_ADD", "register:40f0:8", ["const:a02720:8", "const:4:8"]]
+ 00a02720 ["CALL", null, ["callee:008b6f48:8"]]
- 00a02584 bytes 60d2fa97
+ 00a02720 bytes 0ad2fa97
~~~


<a id="compare-bfea1405c5fd059b49f5e0a3e46c870a"></a>

### [`00a02608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02608.md) → [`00a027a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md) FUN_00a027a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a027bc",
      "incomplete_value": false,
      "site": "00a027c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02620",
      "incomplete_value": false,
      "site": "00a0262c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a027c8",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a027c8",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02608.md#insn-00a02620) · [`00a02650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02608.md#insn-00a02650)
- 新版 [`00a027bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md#insn-00a027bc) · [`00a027ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a027a4.md#insn-00a027ec)

~~~diff
- 00a02620 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a02620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a02620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a02620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a027bc ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a027bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a027bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a027bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a02620 bytes 08812691
+ 00a027bc bytes 08813691
- 00a02650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02650 ["INT_ADD", "register:40f0:8", ["const:a02650:8", "const:4:8"]]
- 00a02650 ["CALLIND", null, ["register:0:8"]]
+ 00a027ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a027ec ["INT_ADD", "register:40f0:8", ["const:a027ec:8", "const:4:8"]]
+ 00a027ec ["CALLIND", null, ["register:0:8"]]
- 00a02650 bytes 00013fd6
+ 00a027ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa0dd4a023ce30ff16104aeb52d65151"></a>

### [`00a02698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02698.md) → [`00a02834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md) FUN_00a02834

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00a0284c",
      "incomplete_value": false,
      "site": "00a02858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a026b0",
      "incomplete_value": false,
      "site": "00a026bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "00a02858",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a02858",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a026b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02698.md#insn-00a026b0) · [`00a026e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02698.md#insn-00a026e0) · [`00a02710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02698.md#insn-00a02710)
- 新版 [`00a0284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a0284c) · [`00a0287c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a0287c) · [`00a028ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02834.md#insn-00a028ac)

~~~diff
- 00a026b0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a026b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a026b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a026b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a0284c ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a0284c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0284c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0284c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a026b0 bytes 08812691
+ 00a0284c bytes 08813691
- 00a026e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a026e0 ["INT_ADD", "register:40f0:8", ["const:a026e0:8", "const:4:8"]]
- 00a026e0 ["CALLIND", null, ["register:0:8"]]
+ 00a0287c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a0287c ["INT_ADD", "register:40f0:8", ["const:a0287c:8", "const:4:8"]]
+ 00a0287c ["CALLIND", null, ["register:0:8"]]
- 00a026e0 bytes 00013fd6
+ 00a0287c bytes 00013fd6
- 00a02710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02710 ["INT_ADD", "register:40f0:8", ["const:a02710:8", "const:4:8"]]
- 00a02710 ["CALLIND", null, ["register:0:8"]]
+ 00a028ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a028ac ["INT_ADD", "register:40f0:8", ["const:a028ac:8", "const:4:8"]]
+ 00a028ac ["CALLIND", null, ["register:0:8"]]
- 00a02710 bytes 00013fd6
+ 00a028ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9543a6b64a4b5de7b06b85721489a1"></a>

### [`00a02724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02724.md) → [`00a028c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md) FUN_00a028c0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a028ec",
      "incomplete_value": false,
      "site": "00a028f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02750",
      "incomplete_value": false,
      "site": "00a02758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a028f4",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a028f4",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0273c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02724.md#insn-00a0273c) · [`00a02750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02724.md#insn-00a02750) · [`00a02778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02724.md#insn-00a02778)
- 新版 [`00a028d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a028d8) · [`00a028ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a028ec) · [`00a02914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a028c0.md#insn-00a02914)

~~~diff
- 00a0273c ["INT_ADD", "register:40f0:8", ["const:a0273c:8", "const:4:8"]]
- 00a0273c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a028d8 ["INT_ADD", "register:40f0:8", ["const:a028d8:8", "const:4:8"]]
+ 00a028d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a0273c bytes d5540994
+ 00a028d8 bytes 6e550994
- 00a02750 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a02750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a02750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a02750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a028ec ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a028ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a028ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a028ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a02750 bytes 29812691
+ 00a028ec bytes 29813691
- 00a02778 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02778 ["INT_ADD", "register:40f0:8", ["const:a02778:8", "const:4:8"]]
- 00a02778 ["CALLIND", null, ["register:0:8"]]
+ 00a02914 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02914 ["INT_ADD", "register:40f0:8", ["const:a02914:8", "const:4:8"]]
+ 00a02914 ["CALLIND", null, ["register:0:8"]]
- 00a02778 bytes 00013fd6
+ 00a02914 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3c4cf49fe3432d5575f1992320a5c33"></a>

### [`00a02834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02834.md) → [`00a029d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md) FUN_00a029d0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a029f4",
      "incomplete_value": false,
      "site": "00a029fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02858",
      "incomplete_value": false,
      "site": "00a02860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a029fc",
      "DATA",
      [
        "storage",
        "00c8a9a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a029fc",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02834.md#insn-00a02858) · [`00a02880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02834.md#insn-00a02880) · [`00a028b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02834.md#insn-00a028b8)
- 新版 [`00a029f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a029f4) · [`00a02a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a02a1c) · [`00a02a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a029d0.md#insn-00a02a54)

~~~diff
- 00a02858 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00a02858 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a02858 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a02858 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a029f4 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00a029f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a029f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a029f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a02858 bytes 29812691
+ 00a029f4 bytes 29813691
- 00a02880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02880 ["INT_ADD", "register:40f0:8", ["const:a02880:8", "const:4:8"]]
- 00a02880 ["CALLIND", null, ["register:0:8"]]
+ 00a02a1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02a1c ["INT_ADD", "register:40f0:8", ["const:a02a1c:8", "const:4:8"]]
+ 00a02a1c ["CALLIND", null, ["register:0:8"]]
- 00a02880 bytes 00013fd6
+ 00a02a1c bytes 00013fd6
- 00a028b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a028b8 ["INT_ADD", "register:40f0:8", ["const:a028b8:8", "const:4:8"]]
- 00a028b8 ["CALLIND", null, ["register:0:8"]]
+ 00a02a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02a54 ["INT_ADD", "register:40f0:8", ["const:a02a54:8", "const:4:8"]]
+ 00a02a54 ["CALLIND", null, ["register:0:8"]]
- 00a028b8 bytes 00013fd6
+ 00a02a54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1d449203fb187bf01c0354fffe859b"></a>

### [`00a02a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md) → [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) FUN_00a02be8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 28件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02f88",
      "incomplete_value": true,
      "site": "00a02f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:28c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02dec",
      "incomplete_value": true,
      "site": "00a02dfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:24c:8"
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
      "definition_site": "00a02f9c",
      "incomplete_value": true,
      "site": "00a02f9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a02e00",
      "incomplete_value": true,
      "site": "00a02e00",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02f90",
      "incomplete_value": true,
      "site": "00a02fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02df4",
      "incomplete_value": true,
      "site": "00a02e04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "00a02c74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a02c9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a02d20",
      "DATA",
      [
        "storage",
        "0040edd0",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00a02c74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a02c9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a02d20",
      "DATA",
      [
        "storage",
        "0040edd0",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md#insn-00a02ad8) · [`00a02b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md#insn-00a02b00) · [`00a02f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md#insn-00a02f2c)
- 新版 [`00a02c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a02c74) · [`00a02c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a02c9c) · [`00a030c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md#insn-00a030c8)

~~~diff
- 00a02ad8 ["INT_ADD", "register:40f0:8", ["const:a02ad8:8", "const:4:8"]]
- 00a02ad8 ["CALL", null, ["ram:47acb4:8"]]
+ 00a02c74 ["INT_ADD", "register:40f0:8", ["const:a02c74:8", "const:4:8"]]
+ 00a02c74 ["CALL", null, ["ram:47acf4:8"]]
- 00a02ad8 bytes 77e0e997
+ 00a02c74 bytes 20e0e997
- 00a02b00 ["INT_ADD", "register:40f0:8", ["const:a02b00:8", "const:4:8"]]
- 00a02b00 ["CALL", null, ["ram:47acb4:8"]]
+ 00a02c9c ["INT_ADD", "register:40f0:8", ["const:a02c9c:8", "const:4:8"]]
+ 00a02c9c ["CALL", null, ["ram:47acf4:8"]]
- 00a02b00 bytes 6de0e997
+ 00a02c9c bytes 16e0e997
- 00a02f2c ["INT_ADD", "register:40f0:8", ["const:a02f2c:8", "const:4:8"]]
- 00a02f2c ["CALL", null, ["ram:664860:8"]]
+ 00a030c8 ["INT_ADD", "register:40f0:8", ["const:a030c8:8", "const:4:8"]]
+ 00a030c8 ["CALL", null, ["ram:6648a0:8"]]
- 00a02f2c bytes 4d86f197
+ 00a030c8 bytes f685f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d9e4b44a6f44e241c336a3816ee55b"></a>

### [`00a035f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a035f8.md) → [`00a03794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03794.md) FUN_00a03794

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a037a0",
      "incomplete_value": false,
      "site": "00a037ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03604",
      "incomplete_value": false,
      "site": "00a03610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a037ac",
      "DATA",
      [
        "storage",
        "00c8aa10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a037ac",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a035f8.md#insn-00a03604)
- 新版 [`00a037a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03794.md#insn-00a037a0)

~~~diff
- 00a03604 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00a03604 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00a03604 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00a03604 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00a037a0 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00a037a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00a037a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00a037a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00a03604 bytes 4a412891
+ 00a037a0 bytes 4a413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c40eeade12f8f97ffc745f57b9dc01a9"></a>

### [`00a0363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0363c.md) → [`00a037d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md) FUN_00a037d8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a037f0",
      "incomplete_value": false,
      "site": "00a037fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03654",
      "incomplete_value": false,
      "site": "00a03660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "00a037fc",
      "DATA",
      [
        "storage",
        "00c8aa10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a037fc",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0363c.md#insn-00a03654) · [`00a03684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0363c.md#insn-00a03684)
- 新版 [`00a037f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md#insn-00a037f0) · [`00a03820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a037d8.md#insn-00a03820)

~~~diff
- 00a03654 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00a03654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a037f0 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00a037f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a037f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a037f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03654 bytes 08412891
+ 00a037f0 bytes 08413891
- 00a03684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03684 ["INT_ADD", "register:40f0:8", ["const:a03684:8", "const:4:8"]]
- 00a03684 ["CALLIND", null, ["register:0:8"]]
+ 00a03820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03820 ["INT_ADD", "register:40f0:8", ["const:a03820:8", "const:4:8"]]
+ 00a03820 ["CALLIND", null, ["register:0:8"]]
- 00a03684 bytes 00013fd6
+ 00a03820 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df1b8dcfe3cf56a0489046e838f6d90d"></a>

### [`00a03728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03728.md) → [`00a038c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md) FUN_00a038c4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a038e4",
      "incomplete_value": false,
      "site": "00a038e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03748",
      "incomplete_value": false,
      "site": "00a03748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "00a038e4",
      "DATA",
      [
        "storage",
        "00c8aa10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a038e4",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03728.md#insn-00a03744) · [`00a03764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03728.md#insn-00a03764) · [`00a03788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03728.md#insn-00a03788)
- 新版 [`00a038e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a038e0) · [`00a03900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a03900) · [`00a03924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a038c4.md#insn-00a03924)

~~~diff
- 00a03744 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00a03744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a038e0 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00a038e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a038e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a038e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03744 bytes 08412891
+ 00a038e0 bytes 08413891
- 00a03764 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03764 ["INT_ADD", "register:40f0:8", ["const:a03764:8", "const:4:8"]]
- 00a03764 ["CALLIND", null, ["register:0:8"]]
+ 00a03900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03900 ["INT_ADD", "register:40f0:8", ["const:a03900:8", "const:4:8"]]
+ 00a03900 ["CALLIND", null, ["register:0:8"]]
- 00a03764 bytes 00013fd6
+ 00a03900 bytes 00013fd6
- 00a03788 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03788 ["INT_ADD", "register:40f0:8", ["const:a03788:8", "const:4:8"]]
- 00a03788 ["CALLIND", null, ["register:0:8"]]
+ 00a03924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03924 ["INT_ADD", "register:40f0:8", ["const:a03924:8", "const:4:8"]]
+ 00a03924 ["CALLIND", null, ["register:0:8"]]
- 00a03788 bytes 00013fd6
+ 00a03924 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9368dcb2539ab691dab787724cd00df9"></a>

### [`00a03828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03828.md) → [`00a039c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md) FUN_00a039c4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b91c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

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
      "site": "00a03a00",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03864",
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
      "00a03a00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a03a00",
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

- 旧版 [`00a03864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03828.md#insn-00a03864) · [`00a03870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03828.md#insn-00a03870) · [`00a038cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03828.md#insn-00a038cc)
- 新版 [`00a03a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a00) · [`00a03a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a0c) · [`00a03a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md#insn-00a03a68)

~~~diff
- 00a03864 ["INT_ADD", "register:40f0:8", ["const:a03864:8", "const:4:8"]]
- 00a03864 ["CALL", null, ["ram:47acb4:8"]]
+ 00a03a00 ["INT_ADD", "register:40f0:8", ["const:a03a00:8", "const:4:8"]]
+ 00a03a00 ["CALL", null, ["ram:47acf4:8"]]
- 00a03864 bytes 14dde997
+ 00a03a00 bytes bddce997
- 00a03870 ["INT_ADD", "register:40f0:8", ["const:a03870:8", "const:4:8"]]
- 00a03870 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a03a0c ["INT_ADD", "register:40f0:8", ["const:a03a0c:8", "const:4:8"]]
+ 00a03a0c ["CALL", null, ["callee:0047cdd4:8"]]
- 00a03870 bytes 49e5e997
+ 00a03a0c bytes f2e4e997
- 00a038cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00a038cc ["INT_ADD", "register:40f0:8", ["const:a038cc:8", "const:4:8"]]
- 00a038cc ["CALLIND", null, ["register:0:8"]]
+ 00a03a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03a68 ["INT_ADD", "register:40f0:8", ["const:a03a68:8", "const:4:8"]]
+ 00a03a68 ["CALLIND", null, ["register:0:8"]]
- 00a038cc bytes 00013fd6
+ 00a03a68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b912030df9aa7213e72a3c60b0b7c1df"></a>

### [`00a0397c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0397c.md) → [`00a03b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md) FUN_00a03b18

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a03b30",
      "incomplete_value": false,
      "site": "00a03b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03994",
      "incomplete_value": false,
      "site": "00a039a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a03b3c",
      "DATA",
      [
        "storage",
        "00c8aa90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03b3c",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0397c.md#insn-00a03994) · [`00a039c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a0397c.md#insn-00a039c4)
- 新版 [`00a03b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md#insn-00a03b30) · [`00a03b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b18.md#insn-00a03b60)

~~~diff
- 00a03994 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a03994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03b30 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00a03b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03994 bytes 08412a91
+ 00a03b30 bytes 08413a91
- 00a039c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a039c4 ["INT_ADD", "register:40f0:8", ["const:a039c4:8", "const:4:8"]]
- 00a039c4 ["CALLIND", null, ["register:0:8"]]
+ 00a03b60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03b60 ["INT_ADD", "register:40f0:8", ["const:a03b60:8", "const:4:8"]]
+ 00a03b60 ["CALLIND", null, ["register:0:8"]]
- 00a039c4 bytes 00013fd6
+ 00a03b60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc43e51d001ec9af05742a71a926f156"></a>

### [`00a039d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a039d8.md) → [`00a03b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md) FUN_00a03b74

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a03ba0",
      "incomplete_value": false,
      "site": "00a03ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03a04",
      "incomplete_value": false,
      "site": "00a03a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a03ba0",
      "DATA",
      [
        "storage",
        "00c8aa90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03ba0",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a039ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a039d8.md#insn-00a039ec) · [`00a039fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a039d8.md#insn-00a039fc) · [`00a03a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a039d8.md#insn-00a03a20)
- 新版 [`00a03b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03b88) · [`00a03b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03b98) · [`00a03bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03b74.md#insn-00a03bbc)

~~~diff
- 00a039ec ["INT_ADD", "register:40f0:8", ["const:a039ec:8", "const:4:8"]]
- 00a039ec ["CALL", null, ["callee:00c57e90:8"]]
+ 00a03b88 ["INT_ADD", "register:40f0:8", ["const:a03b88:8", "const:4:8"]]
+ 00a03b88 ["CALL", null, ["callee:00c57e90:8"]]
- 00a039ec bytes 29500994
+ 00a03b88 bytes c2500994
- 00a039fc ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a039fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a039fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a039fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03b98 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00a03b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a039fc bytes 08412a91
+ 00a03b98 bytes 08413a91
- 00a03a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03a20 ["INT_ADD", "register:40f0:8", ["const:a03a20:8", "const:4:8"]]
- 00a03a20 ["CALLIND", null, ["register:0:8"]]
+ 00a03bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03bbc ["INT_ADD", "register:40f0:8", ["const:a03bbc:8", "const:4:8"]]
+ 00a03bbc ["CALLIND", null, ["register:0:8"]]
- 00a03a20 bytes 00013fd6
+ 00a03bbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e066c33824603c24dea241e69ff2fa1"></a>

### [`00a03a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03a68.md) → [`00a03c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md) FUN_00a03c04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a03c24",
      "incomplete_value": false,
      "site": "00a03c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03a88",
      "incomplete_value": false,
      "site": "00a03a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00a03c24",
      "DATA",
      [
        "storage",
        "00c8aa90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03c24",
      "DATA",
      [
        "storage",
        "00c8ae90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03a68.md#insn-00a03a84) · [`00a03aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03a68.md#insn-00a03aa4) · [`00a03ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03a68.md#insn-00a03ac8)
- 新版 [`00a03c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c20) · [`00a03c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c40) · [`00a03c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03c04.md#insn-00a03c64)

~~~diff
- 00a03a84 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00a03a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03c20 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00a03c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03a84 bytes 08412a91
+ 00a03c20 bytes 08413a91
- 00a03aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03aa4 ["INT_ADD", "register:40f0:8", ["const:a03aa4:8", "const:4:8"]]
- 00a03aa4 ["CALLIND", null, ["register:0:8"]]
+ 00a03c40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03c40 ["INT_ADD", "register:40f0:8", ["const:a03c40:8", "const:4:8"]]
+ 00a03c40 ["CALLIND", null, ["register:0:8"]]
- 00a03aa4 bytes 00013fd6
+ 00a03c40 bytes 00013fd6
- 00a03ac8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03ac8 ["INT_ADD", "register:40f0:8", ["const:a03ac8:8", "const:4:8"]]
- 00a03ac8 ["CALLIND", null, ["register:0:8"]]
+ 00a03c64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03c64 ["INT_ADD", "register:40f0:8", ["const:a03c64:8", "const:4:8"]]
+ 00a03c64 ["CALLIND", null, ["register:0:8"]]
- 00a03ac8 bytes 00013fd6
+ 00a03c64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04c182d45df9114d78c0e8fe15c803aa"></a>

### [`00a03b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03b68.md) → [`00a03d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md) FUN_00a03d04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b91c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

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
      "site": "00a03d40",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03ba4",
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
      "00a03d40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a03d40",
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

- 旧版 [`00a03ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03b68.md#insn-00a03ba4) · [`00a03bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03b68.md#insn-00a03bb0) · [`00a03c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03b68.md#insn-00a03c0c)
- 新版 [`00a03d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03d40) · [`00a03d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03d4c) · [`00a03da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md#insn-00a03da8)

~~~diff
- 00a03ba4 ["INT_ADD", "register:40f0:8", ["const:a03ba4:8", "const:4:8"]]
- 00a03ba4 ["CALL", null, ["ram:47acb4:8"]]
+ 00a03d40 ["INT_ADD", "register:40f0:8", ["const:a03d40:8", "const:4:8"]]
+ 00a03d40 ["CALL", null, ["ram:47acf4:8"]]
- 00a03ba4 bytes 44dce997
+ 00a03d40 bytes eddbe997
- 00a03bb0 ["INT_ADD", "register:40f0:8", ["const:a03bb0:8", "const:4:8"]]
- 00a03bb0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a03d4c ["INT_ADD", "register:40f0:8", ["const:a03d4c:8", "const:4:8"]]
+ 00a03d4c ["CALL", null, ["callee:0047cdd4:8"]]
- 00a03bb0 bytes 79e4e997
+ 00a03d4c bytes 22e4e997
- 00a03c0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03c0c ["INT_ADD", "register:40f0:8", ["const:a03c0c:8", "const:4:8"]]
- 00a03c0c ["CALLIND", null, ["register:0:8"]]
+ 00a03da8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03da8 ["INT_ADD", "register:40f0:8", ["const:a03da8:8", "const:4:8"]]
+ 00a03da8 ["CALLIND", null, ["register:0:8"]]
- 00a03c0c bytes 00013fd6
+ 00a03da8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e1360464d55eb86b3fb6989494b783"></a>

### [`00a03c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03c7c.md) → [`00a03e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md) FUN_00a03e18

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a03e3c",
      "incomplete_value": false,
      "site": "00a03e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03ca0",
      "incomplete_value": false,
      "site": "00a03ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00a03e3c",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03e3c",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03c7c.md#insn-00a03c90) · [`00a03c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03c7c.md#insn-00a03c9c)
- 新版 [`00a03e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md#insn-00a03e2c) · [`00a03e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e18.md#insn-00a03e38)

~~~diff
- 00a03c90 ["INT_ADD", "register:40f0:8", ["const:a03c90:8", "const:4:8"]]
- 00a03c90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a03e2c ["INT_ADD", "register:40f0:8", ["const:a03e2c:8", "const:4:8"]]
+ 00a03e2c ["CALL", null, ["callee:00c57e90:8"]]
- 00a03c90 bytes 804f0994
+ 00a03e2c bytes 19500994
- 00a03c9c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a03c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a03c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a03c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a03e38 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00a03e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a03e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a03c9c bytes 08812c91
+ 00a03e38 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f0a0a338995df3832983eec569e496"></a>

### [`00a03cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03cb0.md) → [`00a03e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e4c.md) FUN_00a03e4c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a03e58",
      "incomplete_value": false,
      "site": "00a03e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03cbc",
      "incomplete_value": false,
      "site": "00a03cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a03e58",
      "DATA",
      [
        "storage",
        "00c8ab20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a03e58",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03cb0.md#insn-00a03cb8)
- 新版 [`00a03e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e4c.md#insn-00a03e54)

~~~diff
- 00a03cb8 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a03cb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a03cb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a03cb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a03e54 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00a03e54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a03e54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a03e54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a03cb8 bytes 29812c91
+ 00a03e54 bytes 29813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c38f124a38276ea218ad9113855c9c66"></a>

### [`00a03ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03ccc.md) → [`00a03e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md) FUN_00a03e68

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a03ec4",
      "incomplete_value": true,
      "site": "00a03ec4",
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
      "definition_site": "00a03d28",
      "incomplete_value": true,
      "site": "00a03d28",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a03ecc",
      "incomplete_value": false,
      "site": "00a03edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03d30",
      "incomplete_value": false,
      "site": "00a03d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00a03ed4",
      "incomplete_value": false,
      "site": "00a03edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03d38",
      "incomplete_value": false,
      "site": "00a03d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a03ec0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00a03ecc",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a03ed4",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a03ec0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00a03ecc",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a03ed4",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a03d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03ccc.md#insn-00a03d40) · [`00a03f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03ccc.md#insn-00a03f40) · [`00a040dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03ccc.md#insn-00a040dc)
- 新版 [`00a03edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a03edc) · [`00a040dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a040dc) · [`00a04278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md#insn-00a04278)

~~~diff
- 00a03d40 ["INT_ADD", "register:40f0:8", ["const:a03d40:8", "const:4:8"]]
- 00a03d40 ["CALL", null, ["callee:00c58610:8"]]
+ 00a03edc ["INT_ADD", "register:40f0:8", ["const:a03edc:8", "const:4:8"]]
+ 00a03edc ["CALL", null, ["callee:00c58610:8"]]
- 00a03d40 bytes 34510994
+ 00a03edc bytes cd510994
- 00a03f40 ["INT_ADD", "register:40f0:8", ["const:a03f40:8", "const:4:8"]]
- 00a03f40 ["CALL", null, ["callee:008514f8:8"]]
+ 00a040dc ["INT_ADD", "register:40f0:8", ["const:a040dc:8", "const:4:8"]]
+ 00a040dc ["CALL", null, ["callee:008514f8:8"]]
- 00a03f40 bytes 5e35f997
+ 00a040dc bytes 0735f997
- 00a040dc ["INT_ADD", "register:40f0:8", ["const:a040dc:8", "const:4:8"]]
- 00a040dc ["CALL", null, ["ram:46c984:8"]]
+ 00a04278 ["INT_ADD", "register:40f0:8", ["const:a04278:8", "const:4:8"]]
+ 00a04278 ["CALL", null, ["ram:46c9c4:8"]]
- 00a040dc bytes 2aa2e997
+ 00a04278 bytes d3a1e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-049146e19d1ae71065a1bac1eb3a9f0d"></a>

### [`00a043bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a043bc.md) → [`00a04558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md) FUN_00a04558

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a0457c",
      "incomplete_value": false,
      "site": "00a0457c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a043e0",
      "incomplete_value": false,
      "site": "00a043e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "00a0457c",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a0457c",
      "DATA",
      [
        "storage",
        "00c8afa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a043d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a043bc.md#insn-00a043d0) · [`00a043dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a043bc.md#insn-00a043dc)
- 新版 [`00a0456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md#insn-00a0456c) · [`00a04578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04558.md#insn-00a04578)

~~~diff
- 00a043d0 ["INT_ADD", "register:40f0:8", ["const:a043d0:8", "const:4:8"]]
- 00a043d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a0456c ["INT_ADD", "register:40f0:8", ["const:a0456c:8", "const:4:8"]]
+ 00a0456c ["CALL", null, ["callee:00c57e90:8"]]
- 00a043d0 bytes b04d0994
+ 00a0456c bytes 494e0994
- 00a043dc ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00a043dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a043dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a043dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04578 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00a04578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a043dc bytes 08812e91
+ 00a04578 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cb0f38a356adbfa8a90a4c5018c7ef9"></a>

### [`00a043f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a043f0.md) → [`00a0458c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a0458c.md) FUN_00a0458c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a04598",
      "incomplete_value": false,
      "site": "00a04598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a043fc",
      "incomplete_value": false,
      "site": "00a043fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a04598",
      "DATA",
      [
        "storage",
        "00c8aba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04598",
      "DATA",
      [
        "storage",
        "00c8afa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a043f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a043f0.md#insn-00a043f8)
- 新版 [`00a04594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a0458c.md#insn-00a04594)

~~~diff
- 00a043f8 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00a043f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a043f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a043f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a04594 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00a04594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a04594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a04594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a043f8 bytes 29812e91
+ 00a04594 bytes 29813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a387200a029057d9e3b5cb05fdde9cce"></a>

### [`00a04c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c28.md) → [`00a04dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md) FUN_00a04dc4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00a04de8",
      "incomplete_value": false,
      "site": "00a04dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04c4c",
      "incomplete_value": false,
      "site": "00a04c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a04dec",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04dec",
      "DATA",
      [
        "storage",
        "00c8b020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c28.md#insn-00a04c3c) · [`00a04c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c28.md#insn-00a04c48) · [`00a04c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c28.md#insn-00a04c4c)
- 新版 [`00a04dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md#insn-00a04dd8) · [`00a04de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md#insn-00a04de4) · [`00a04de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04dc4.md#insn-00a04de8)

~~~diff
- 00a04c3c ["INT_ADD", "register:40f0:8", ["const:a04c3c:8", "const:4:8"]]
- 00a04c3c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a04dd8 ["INT_ADD", "register:40f0:8", ["const:a04dd8:8", "const:4:8"]]
+ 00a04dd8 ["CALL", null, ["callee:00c57e90:8"]]
- 00a04c3c bytes 954b0994
+ 00a04dd8 bytes 2e4c0994
- 00a04c48 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a04de4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04c48 bytes 281400d0
+ 00a04de4 bytes 281400f0
- 00a04c4c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a04c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04de8 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00a04de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04c4c bytes 08813091
+ 00a04de8 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5f3f006c505daf0a8d3300a73104df2"></a>

### [`00a04c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c68.md) → [`00a04e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e04.md) FUN_00a04e04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a04e08",
      "incomplete_value": false,
      "site": "00a04e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04c6c",
      "incomplete_value": false,
      "site": "00a04c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a04e0c",
      "DATA",
      [
        "storage",
        "00c8ac20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04e0c",
      "DATA",
      [
        "storage",
        "00c8b020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c68.md#insn-00a04c68) · [`00a04c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04c68.md#insn-00a04c6c)
- 新版 [`00a04e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e04.md#insn-00a04e04) · [`00a04e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e04.md#insn-00a04e08)

~~~diff
- 00a04c68 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a04e04 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04c68 bytes 281400d0
+ 00a04e04 bytes 281400f0
- 00a04c6c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a04c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04e08 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00a04e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04c6c bytes 08813091
+ 00a04e08 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d021da64db89f20e102680c00357dd94"></a>

### [`00a04cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04cf8.md) → [`00a04e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md) FUN_00a04e94

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009fb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00a04ea0",
      "incomplete_value": false,
      "site": "00a04ea4",
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
      "definition_site": "00a04d04",
      "incomplete_value": false,
      "site": "00a04d08",
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
      "00a04ea0",
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
      "00a04ea0",
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

- 旧版 [`00a04d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04cf8.md#insn-00a04d08) · [`00a04d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04cf8.md#insn-00a04d04)
- 新版 [`00a04ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md#insn-00a04ea4) · [`00a04ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e94.md#insn-00a04ea0)

~~~diff
- 00a04d08 ["INT_ADD", "register:40f0:8", ["const:a04d08:8", "const:4:8"]]
- 00a04d08 ["CALL", null, ["callee:0043b778:8"]]
+ 00a04ea4 ["INT_ADD", "register:40f0:8", ["const:a04ea4:8", "const:4:8"]]
+ 00a04ea4 ["CALL", null, ["callee:0043b778:8"]]
- 00a04d08 bytes 8cdae897
+ 00a04ea4 bytes 35dae897
- 00a04d04 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00a04d04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a04d04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a04d04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a04ea0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00a04ea0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a04ea0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a04ea0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a04d04 bytes 00303c91
+ 00a04ea0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e662b28ead04250b2241d59b24de178"></a>

### [`00a04d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d10.md) → [`00a04eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md) FUN_00a04eac

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00a04ed0",
      "incomplete_value": false,
      "site": "00a04ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04d34",
      "incomplete_value": false,
      "site": "00a04d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a04ed4",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04ed4",
      "DATA",
      [
        "storage",
        "00c8b0a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d10.md#insn-00a04d24) · [`00a04d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d10.md#insn-00a04d30) · [`00a04d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d10.md#insn-00a04d34)
- 新版 [`00a04ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md#insn-00a04ec0) · [`00a04ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md#insn-00a04ecc) · [`00a04ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eac.md#insn-00a04ed0)

~~~diff
- 00a04d24 ["INT_ADD", "register:40f0:8", ["const:a04d24:8", "const:4:8"]]
- 00a04d24 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a04ec0 ["INT_ADD", "register:40f0:8", ["const:a04ec0:8", "const:4:8"]]
+ 00a04ec0 ["CALL", null, ["callee:00c57e90:8"]]
- 00a04d24 bytes 5b4b0994
+ 00a04ec0 bytes f44b0994
- 00a04d30 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a04ecc ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04d30 bytes 281400d0
+ 00a04ecc bytes 281400f0
- 00a04d34 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a04d34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04d34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04d34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04ed0 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00a04ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04d34 bytes 08813291
+ 00a04ed0 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaa0871dbd131bf0afa9ca452272f86"></a>

### [`00a04d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d50.md) → [`00a04eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eec.md) FUN_00a04eec

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00a04ef0",
      "incomplete_value": false,
      "site": "00a04ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04d54",
      "incomplete_value": false,
      "site": "00a04d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a04ef4",
      "DATA",
      [
        "storage",
        "00c8aca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a04ef4",
      "DATA",
      [
        "storage",
        "00c8b0a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d50.md#insn-00a04d50) · [`00a04d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d50.md#insn-00a04d54)
- 新版 [`00a04eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eec.md#insn-00a04eec) · [`00a04ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04eec.md#insn-00a04ef0)

~~~diff
- 00a04d50 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a04eec ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04d50 bytes 281400d0
+ 00a04eec bytes 281400f0
- 00a04d54 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00a04d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a04d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a04d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a04ef0 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00a04ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a04ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a04d54 bytes 08813291
+ 00a04ef0 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edec8b42cb1cf9a748784c1240d65e79"></a>

### [`00a04d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d78.md) → [`00a04f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md) FUN_00a04f14

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b975c.md) [`009df498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df498.md) [`009df728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df728.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b97a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b97a0.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md) [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a050dc",
      "incomplete_value": true,
      "site": "00a050ec",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:658:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04f40",
      "incomplete_value": true,
      "site": "00a04f50",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "00a050e0",
      "incomplete_value": true,
      "site": "00a050f0",
      "value": [
        "LOAD",
        "16",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04f44",
      "incomplete_value": true,
      "site": "00a04f54",
      "value": [
        "LOAD",
        "16",
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
                "const:c:8"
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
      "definition_site": "00a050e4",
      "incomplete_value": true,
      "site": "00a050f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04f48",
      "incomplete_value": true,
      "site": "00a04f58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:250:8"
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
      "00a050dc",
      "READ",
      [
        "storage",
        "002b5618",
        null,
        "string"
      ]
    ],
    [
      "00a050e0",
      "READ",
      [
        "storage",
        "002b5624",
        null,
        "string"
      ]
    ],
    [
      "00a050e4",
      "READ",
      [
        "storage",
        "002c3250",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a050dc",
      "READ",
      [
        "storage",
        "002b5658",
        null,
        "string"
      ]
    ],
    [
      "00a050e0",
      "READ",
      [
        "storage",
        "002b5664",
        null,
        "string"
      ]
    ],
    [
      "00a050e4",
      "READ",
      [
        "storage",
        "002c3290",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d78.md#insn-00a04dac) · [`00a04dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d78.md#insn-00a04dc0) · [`00a04ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a04/00a04d78.md#insn-00a04ddc)
- 新版 [`00a04f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a04f48) · [`00a04f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a04f5c) · [`00a04f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04f14.md#insn-00a04f78)

~~~diff
- 00a04dac ["INT_ADD", "register:40f0:8", ["const:a04dac:8", "const:4:8"]]
- 00a04dac ["CALL", null, ["callee:008b97a0:8"]]
+ 00a04f48 ["INT_ADD", "register:40f0:8", ["const:a04f48:8", "const:4:8"]]
+ 00a04f48 ["CALL", null, ["callee:008b97a0:8"]]
- 00a04dac bytes 6cd2fa97
+ 00a04f48 bytes 16d2fa97
- 00a04dc0 ["INT_ADD", "register:40f0:8", ["const:a04dc0:8", "const:4:8"]]
- 00a04dc0 ["CALL", null, ["callee:008514f8:8"]]
+ 00a04f5c ["INT_ADD", "register:40f0:8", ["const:a04f5c:8", "const:4:8"]]
+ 00a04f5c ["CALL", null, ["callee:008514f8:8"]]
- 00a04dc0 bytes be31f997
+ 00a04f5c bytes 6731f997
- 00a04ddc ["INT_ADD", "register:40f0:8", ["const:a04ddc:8", "const:4:8"]]
- 00a04ddc ["CALL", null, ["callee:009e4a08:8"]]
+ 00a04f78 ["INT_ADD", "register:40f0:8", ["const:a04f78:8", "const:4:8"]]
+ 00a04f78 ["CALL", null, ["callee:009e4a08:8"]]
- 00a04ddc bytes a47eff97
+ 00a04f78 bytes a47eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5494cfa10b7681aba400d4e232a2d164"></a>

### [`00a050b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050b8.md) → [`00a05254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md) FUN_00a05254

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05278",
      "incomplete_value": false,
      "site": "00a05278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a050dc",
      "incomplete_value": false,
      "site": "00a050dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a05278",
      "DATA",
      [
        "storage",
        "00c8ad20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05278",
      "DATA",
      [
        "storage",
        "00c8b120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a050cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050b8.md#insn-00a050cc) · [`00a050d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050b8.md#insn-00a050d4) · [`00a050d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050b8.md#insn-00a050d8)
- 新版 [`00a05268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md#insn-00a05268) · [`00a05270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md#insn-00a05270) · [`00a05274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05254.md#insn-00a05274)

~~~diff
- 00a050cc ["INT_ADD", "register:40f0:8", ["const:a050cc:8", "const:4:8"]]
- 00a050cc ["CALL", null, ["callee:00c57e90:8"]]
+ 00a05268 ["INT_ADD", "register:40f0:8", ["const:a05268:8", "const:4:8"]]
+ 00a05268 ["CALL", null, ["callee:00c57e90:8"]]
- 00a050cc bytes 714a0994
+ 00a05268 bytes 0a4b0994
- 00a050d4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a05270 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a050d4 bytes 281400b0
+ 00a05270 bytes 281400d0
- 00a050d8 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a050d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a050d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a050d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05274 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00a05274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a050d8 bytes 08813491
+ 00a05274 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99895d2b5b7d01b7c60c190a2037612"></a>

### [`00a050ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050ec.md) → [`00a05288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05288.md) FUN_00a05288

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05294",
      "incomplete_value": true,
      "site": "00a05294",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a050f8",
      "incomplete_value": true,
      "site": "00a050f8",
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
      "00a05294",
      "DATA",
      [
        "storage",
        "00c8ad20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05294",
      "DATA",
      [
        "storage",
        "00c8b120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a050f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050ec.md#insn-00a050f0) · [`00a050f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a050ec.md#insn-00a050f4)
- 新版 [`00a0528c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05288.md#insn-00a0528c) · [`00a05290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05288.md#insn-00a05290)

~~~diff
- 00a050f0 ["COPY", "register:4048:8", ["const:c8a000:8"]]
+ 00a0528c ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a050f0 bytes 291400b0
+ 00a0528c bytes 291400d0
- 00a050f4 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00a050f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a050f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a050f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a05290 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00a05290 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a05290 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a05290 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a050f4 bytes 29813491
+ 00a05290 bytes 29810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-019147b8c3c106fa79d6d1702914bf50"></a>

### [`00a05108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05108.md) → [`00a052a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md) FUN_00a052a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009f7c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f7/009f7c44.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md)

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
      "site": "00a052c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05128",
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
      "site": "00a052d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05134",
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
      "00a052c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a052d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a052c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a052d0",
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

- 旧版 [`00a05128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05108.md#insn-00a05128) · [`00a05134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05108.md#insn-00a05134)
- 新版 [`00a052c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md#insn-00a052c4) · [`00a052d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md#insn-00a052d0)

~~~diff
- 00a05128 ["INT_ADD", "register:40f0:8", ["const:a05128:8", "const:4:8"]]
- 00a05128 ["CALL", null, ["ram:47acb4:8"]]
+ 00a052c4 ["INT_ADD", "register:40f0:8", ["const:a052c4:8", "const:4:8"]]
+ 00a052c4 ["CALL", null, ["ram:47acf4:8"]]
- 00a05128 bytes e3d6e997
+ 00a052c4 bytes 8cd6e997
- 00a05134 ["INT_ADD", "register:40f0:8", ["const:a05134:8", "const:4:8"]]
- 00a05134 ["CALL", null, ["ram:47acb4:8"]]
+ 00a052d0 ["INT_ADD", "register:40f0:8", ["const:a052d0:8", "const:4:8"]]
+ 00a052d0 ["CALL", null, ["ram:47acf4:8"]]
- 00a05134 bytes e0d6e997
+ 00a052d0 bytes 89d6e997
~~~


<a id="compare-bdbf8b5bd925b66dd9f28fa993f27f97"></a>

### [`00a05188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05188.md) → [`00a05324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md) FUN_00a05324

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05344",
      "incomplete_value": false,
      "site": "00a05348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a051a8",
      "incomplete_value": false,
      "site": "00a051ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a05348",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05348",
      "DATA",
      [
        "storage",
        "00c8b1a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05188.md#insn-00a0519c) · [`00a051a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05188.md#insn-00a051a4) · [`00a051a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05188.md#insn-00a051a8)
- 新版 [`00a05338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md#insn-00a05338) · [`00a05340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md#insn-00a05340) · [`00a05344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05324.md#insn-00a05344)

~~~diff
- 00a0519c ["INT_ADD", "register:40f0:8", ["const:a0519c:8", "const:4:8"]]
- 00a0519c ["CALL", null, ["callee:00c57e90:8"]]
+ 00a05338 ["INT_ADD", "register:40f0:8", ["const:a05338:8", "const:4:8"]]
+ 00a05338 ["CALL", null, ["callee:00c57e90:8"]]
- 00a0519c bytes 3d4a0994
+ 00a05338 bytes d64a0994
- 00a051a4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a05340 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a051a4 bytes 281400b0
+ 00a05340 bytes 281400d0
- 00a051a8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a051a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a051a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a051a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05344 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00a05344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a051a8 bytes 08813691
+ 00a05344 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3646fe9ba6c989e003ba3cbcb0c883"></a>

### [`00a051c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051c0.md) → [`00a0535c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0535c.md) FUN_00a0535c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05360",
      "incomplete_value": false,
      "site": "00a05364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a051c4",
      "incomplete_value": false,
      "site": "00a051c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
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
      "00a05364",
      "DATA",
      [
        "storage",
        "00c8ada0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05364",
      "DATA",
      [
        "storage",
        "00c8b1a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a051c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051c0.md#insn-00a051c0) · [`00a051c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051c0.md#insn-00a051c4)
- 新版 [`00a0535c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0535c.md#insn-00a0535c) · [`00a05360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0535c.md#insn-00a05360)

~~~diff
- 00a051c0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a0535c ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a051c0 bytes 281400b0
+ 00a0535c bytes 281400d0
- 00a051c4 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00a051c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a051c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a051c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05360 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00a05360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a051c4 bytes 08813691
+ 00a05360 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7dae9291180fe8223898b448325c76a"></a>

### [`00a051e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051e0.md) → [`00a0537c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md) FUN_00a0537c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a0542c",
      "incomplete_value": true,
      "site": "00a0543c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:852:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05290",
      "incomplete_value": true,
      "site": "00a052a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:812:8"
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
      "definition_site": "00a05440",
      "incomplete_value": true,
      "site": "00a05440",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a052a4",
      "incomplete_value": true,
      "site": "00a052a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a05434",
      "incomplete_value": true,
      "site": "00a05444",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05298",
      "incomplete_value": true,
      "site": "00a052a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "00a053b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a053d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a0542c",
      "READ",
      [
        "storage",
        "002b8812",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a053b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a053d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a0542c",
      "READ",
      [
        "storage",
        "002b8852",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0521c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051e0.md#insn-00a0521c) · [`00a05238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051e0.md#insn-00a05238) · [`00a05274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a051e0.md#insn-00a05274)
- 新版 [`00a053b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a053b8) · [`00a053d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a053d4) · [`00a05410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0537c.md#insn-00a05410)

~~~diff
- 00a0521c ["INT_ADD", "register:40f0:8", ["const:a0521c:8", "const:4:8"]]
- 00a0521c ["CALL", null, ["ram:47acb4:8"]]
+ 00a053b8 ["INT_ADD", "register:40f0:8", ["const:a053b8:8", "const:4:8"]]
+ 00a053b8 ["CALL", null, ["ram:47acf4:8"]]
- 00a0521c bytes a6d6e997
+ 00a053b8 bytes 4fd6e997
- 00a05238 ["INT_ADD", "register:40f0:8", ["const:a05238:8", "const:4:8"]]
- 00a05238 ["CALL", null, ["ram:47acb4:8"]]
+ 00a053d4 ["INT_ADD", "register:40f0:8", ["const:a053d4:8", "const:4:8"]]
+ 00a053d4 ["CALL", null, ["ram:47acf4:8"]]
- 00a05238 bytes 9fd6e997
+ 00a053d4 bytes 48d6e997
- 00a05274 ["INT_ADD", "register:40f0:8", ["const:a05274:8", "const:4:8"]]
- 00a05274 ["CALL", null, ["callee:008514f8:8"]]
+ 00a05410 ["INT_ADD", "register:40f0:8", ["const:a05410:8", "const:4:8"]]
+ 00a05410 ["CALL", null, ["callee:008514f8:8"]]
- 00a05274 bytes 9130f997
+ 00a05410 bytes 3a30f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74fcc80ad3f0f574661b15200f862f92"></a>

### [`00a055f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a055f4.md) → [`00a05790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md) FUN_00a05790

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a057b4",
      "incomplete_value": false,
      "site": "00a057b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05618",
      "incomplete_value": false,
      "site": "00a05618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "00a057b4",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a057b4",
      "DATA",
      [
        "storage",
        "00c8b210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a055f4.md#insn-00a05608) · [`00a05610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a055f4.md#insn-00a05610) · [`00a05614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a055f4.md#insn-00a05614)
- 新版 [`00a057a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md#insn-00a057a4) · [`00a057ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md#insn-00a057ac) · [`00a057b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05790.md#insn-00a057b0)

~~~diff
- 00a05608 ["INT_ADD", "register:40f0:8", ["const:a05608:8", "const:4:8"]]
- 00a05608 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a057a4 ["INT_ADD", "register:40f0:8", ["const:a057a4:8", "const:4:8"]]
+ 00a057a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00a05608 bytes 22490994
+ 00a057a4 bytes bb490994
- 00a05610 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a057ac ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a05610 bytes 281400b0
+ 00a057ac bytes 281400d0
- 00a05614 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a05614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a057b0 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00a057b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a057b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a057b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05614 bytes 08413891
+ 00a057b0 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fc5f0f2df804b680fb542028de837c4"></a>

### [`00a05628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05628.md) → [`00a057c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057c4.md) FUN_00a057c4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a057d0",
      "incomplete_value": false,
      "site": "00a057d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05634",
      "incomplete_value": false,
      "site": "00a05634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "00a057d0",
      "DATA",
      [
        "storage",
        "00c8ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a057d0",
      "DATA",
      [
        "storage",
        "00c8b210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05628.md#insn-00a0562c) · [`00a05630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05628.md#insn-00a05630)
- 新版 [`00a057c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057c4.md#insn-00a057c8) · [`00a057cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057c4.md#insn-00a057cc)

~~~diff
- 00a0562c ["COPY", "register:4048:8", ["const:c8a000:8"]]
+ 00a057c8 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a0562c bytes 291400b0
+ 00a057c8 bytes 291400d0
- 00a05630 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a05630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a05630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a05630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a057cc ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00a057cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a057cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a057cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a05630 bytes 29413891
+ 00a057cc bytes 29410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236195549e5369bca7d6162a69dd522b"></a>

### [`00a05644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05644.md) → [`00a057e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md) FUN_00a057e0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b91c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "site": "00a05808",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0566c",
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
      "00a05808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a05808",
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

- 旧版 [`00a0566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05644.md#insn-00a0566c) · [`00a05678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05644.md#insn-00a05678)
- 新版 [`00a05808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md#insn-00a05808) · [`00a05814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md#insn-00a05814)

~~~diff
- 00a0566c ["INT_ADD", "register:40f0:8", ["const:a0566c:8", "const:4:8"]]
- 00a0566c ["CALL", null, ["ram:47acb4:8"]]
+ 00a05808 ["INT_ADD", "register:40f0:8", ["const:a05808:8", "const:4:8"]]
+ 00a05808 ["CALL", null, ["ram:47acf4:8"]]
- 00a0566c bytes 92d5e997
+ 00a05808 bytes 3bd5e997
- 00a05678 ["INT_ADD", "register:40f0:8", ["const:a05678:8", "const:4:8"]]
- 00a05678 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00a05814 ["INT_ADD", "register:40f0:8", ["const:a05814:8", "const:4:8"]]
+ 00a05814 ["CALL", null, ["callee:0047cdd4:8"]]
- 00a05678 bytes c7dde997
+ 00a05814 bytes 70dde997
~~~


<a id="compare-095cc1bb47ba32110240831178c2b372"></a>

### [`00a056d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a056d0.md) → [`00a0586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md) FUN_00a0586c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05890",
      "incomplete_value": false,
      "site": "00a05890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a056f4",
      "incomplete_value": false,
      "site": "00a056f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "00a05890",
      "DATA",
      [
        "storage",
        "00c8aea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05890",
      "DATA",
      [
        "storage",
        "00c8b2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a056e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a056d0.md#insn-00a056e4) · [`00a056ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a056d0.md#insn-00a056ec) · [`00a056f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a056d0.md#insn-00a056f0)
- 新版 [`00a05880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md#insn-00a05880) · [`00a05888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md#insn-00a05888) · [`00a0588c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0586c.md#insn-00a0588c)

~~~diff
- 00a056e4 ["INT_ADD", "register:40f0:8", ["const:a056e4:8", "const:4:8"]]
- 00a056e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a05880 ["INT_ADD", "register:40f0:8", ["const:a05880:8", "const:4:8"]]
+ 00a05880 ["CALL", null, ["callee:00c57e90:8"]]
- 00a056e4 bytes eb480994
+ 00a05880 bytes 84490994
- 00a056ec ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a05888 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a056ec bytes 281400b0
+ 00a05888 bytes 281400d0
- 00a056f0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00a056f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a056f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a056f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a0588c ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00a0588c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0588c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a0588c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a056f0 bytes 08813a91
+ 00a0588c bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d63c7c1bb1d6c31cae7327c45adfcc31"></a>

### [`00a05704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05704.md) → [`00a058a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058a0.md) FUN_00a058a0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a058ac",
      "incomplete_value": false,
      "site": "00a058ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05710",
      "incomplete_value": false,
      "site": "00a05710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "00a058ac",
      "DATA",
      [
        "storage",
        "00c8aea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a058ac",
      "DATA",
      [
        "storage",
        "00c8b2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05704.md#insn-00a05708) · [`00a0570c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05704.md#insn-00a0570c)
- 新版 [`00a058a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058a0.md#insn-00a058a4) · [`00a058a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058a0.md#insn-00a058a8)

~~~diff
- 00a05708 ["COPY", "register:4048:8", ["const:c8a000:8"]]
+ 00a058a4 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a05708 bytes 291400b0
+ 00a058a4 bytes 291400d0
- 00a0570c ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00a0570c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a0570c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a0570c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a058a8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00a058a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a058a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a058a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a0570c bytes 29813a91
+ 00a058a8 bytes 29810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73546581431f1e6d0caaff99899198a9"></a>

### [`00a05720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05720.md) → [`00a058bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md) FUN_00a058bc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009faa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md)

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
      "site": "00a058dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05740",
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
      "site": "00a058e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0574c",
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
      "00a058dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00a058e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a058dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00a058e8",
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

- 旧版 [`00a05740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05720.md#insn-00a05740) · [`00a0574c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05720.md#insn-00a0574c)
- 新版 [`00a058dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md#insn-00a058dc) · [`00a058e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a058bc.md#insn-00a058e8)

~~~diff
- 00a05740 ["INT_ADD", "register:40f0:8", ["const:a05740:8", "const:4:8"]]
- 00a05740 ["CALL", null, ["ram:47acb4:8"]]
+ 00a058dc ["INT_ADD", "register:40f0:8", ["const:a058dc:8", "const:4:8"]]
+ 00a058dc ["CALL", null, ["ram:47acf4:8"]]
- 00a05740 bytes 5dd5e997
+ 00a058dc bytes 06d5e997
- 00a0574c ["INT_ADD", "register:40f0:8", ["const:a0574c:8", "const:4:8"]]
- 00a0574c ["CALL", null, ["ram:47acb4:8"]]
+ 00a058e8 ["INT_ADD", "register:40f0:8", ["const:a058e8:8", "const:4:8"]]
+ 00a058e8 ["CALL", null, ["ram:47acf4:8"]]
- 00a0574c bytes 5ad5e997
+ 00a058e8 bytes 03d5e997
~~~


<a id="compare-ac20c58b3df13d23eead3761203c780b"></a>

### [`00a057a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057a0.md) → [`00a0593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md) FUN_00a0593c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05950",
      "incomplete_value": false,
      "site": "00a05954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057b4",
      "incomplete_value": false,
      "site": "00a057b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00a05954",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05954",
      "DATA",
      [
        "storage",
        "00c8b320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a057ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057a0.md#insn-00a057ac) · [`00a057b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057a0.md#insn-00a057b0) · [`00a057b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057a0.md#insn-00a057b4)
- 新版 [`00a05948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md#insn-00a05948) · [`00a0594c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md#insn-00a0594c) · [`00a05950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a0593c.md#insn-00a05950)

~~~diff
- 00a057ac ["INT_ADD", "register:40f0:8", ["const:a057ac:8", "const:4:8"]]
- 00a057ac ["CALL", null, ["callee:00c57e90:8"]]
+ 00a05948 ["INT_ADD", "register:40f0:8", ["const:a05948:8", "const:4:8"]]
+ 00a05948 ["CALL", null, ["callee:00c57e90:8"]]
- 00a057ac bytes b9480994
+ 00a05948 bytes 52490994
- 00a057b0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a0594c ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a057b0 bytes 281400b0
+ 00a0594c bytes 281400d0
- 00a057b4 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00a057b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a057b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a057b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05950 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00a05950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a057b4 bytes 08813c91
+ 00a05950 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4d02cf75b1b86375daea1431dace8b"></a>

### [`00a057c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057c4.md) → [`00a05960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05960.md) FUN_00a05960

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a05964",
      "incomplete_value": false,
      "site": "00a05968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057c8",
      "incomplete_value": false,
      "site": "00a057cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00a05968",
      "DATA",
      [
        "storage",
        "00c8af20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a05968",
      "DATA",
      [
        "storage",
        "00c8b320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a057c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057c4.md#insn-00a057c4) · [`00a057c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a057c4.md#insn-00a057c8)
- 新版 [`00a05960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05960.md#insn-00a05960) · [`00a05964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05960.md#insn-00a05964)

~~~diff
- 00a057c4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
+ 00a05960 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a057c4 bytes 281400b0
+ 00a05960 bytes 281400d0
- 00a057c8 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00a057c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a057c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a057c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05964 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00a05964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a057c8 bytes 08813c91
+ 00a05964 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2aedc942598a861c4e85bc54669de7"></a>

### [`00a058b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a058b4.md) → [`00a05a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md) _INIT_206

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00a05a8c",
      "incomplete_value": true,
      "site": "00a05aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a058f0",
      "incomplete_value": true,
      "site": "00a0590c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a05ad0",
      "incomplete_value": true,
      "site": "00a05aec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a05934",
      "incomplete_value": true,
      "site": "00a05950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a05af0",
      "incomplete_value": true,
      "site": "00a05b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a05954",
      "incomplete_value": true,
      "site": "00a0596c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a05a8c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a05ab0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00a05ad0",
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
      "00a05a8c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a05ab0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a05ad0",
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

- 旧版 [`00a0594c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a058b4.md#insn-00a0594c) · [`00a05ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a058b4.md#insn-00a05ae8) · [`00a058e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a058b4.md#insn-00a058e0)
- 新版 [`00a05ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05ae8) · [`00a05c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05c84) · [`00a05a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05a50.md#insn-00a05a7c)

~~~diff
- 00a0594c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00a0594c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00a0594c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00a0594c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00a05ae8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00a05ae8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00a05ae8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00a05ae8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00a0594c bytes 4a553a91
+ 00a05ae8 bytes 4a893d91
- 00a05ae8 ["INT_ADD", "register:40f0:8", ["const:a05ae8:8", "const:4:8"]]
- 00a05ae8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00a05c84 ["INT_ADD", "register:40f0:8", ["const:a05c84:8", "const:4:8"]]
+ 00a05c84 ["CALL", null, ["callee:00c57e30:8"]]
- 00a05ae8 bytes d2470994
+ 00a05c84 bytes 6b480994
- 00a058e0 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00a058e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a058e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a058e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a05a7c ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00a05a7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a05a7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a05a7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a058e0 bytes 73422591
+ 00a05a7c bytes 73423591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab850d214152e7fa43b1e0d87a9985f"></a>

### [`00a05c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md) → [`00a05de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md) FUN_00a05de0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.27% / 新版 96.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05e20",
      "incomplete_value": false,
      "site": "00a05e2c",
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
      "definition_site": "00a05c84",
      "incomplete_value": false,
      "site": "00a05c90",
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
      "definition_site": "00a05e58",
      "incomplete_value": true,
      "site": "00a05e64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05cbc",
      "incomplete_value": true,
      "site": "00a05cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ec:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a05fb4",
      "incomplete_value": true,
      "site": "00a05fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05e18",
      "incomplete_value": true,
      "site": "00a05e24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
              ]
            ]
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
      "00a05e2c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a05e58",
      "READ",
      [
        "storage",
        "002a16ec",
        null,
        "string"
      ]
    ],
    [
      "00a05fb4",
      "READ",
      [
        "storage",
        "002b96ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a05e2c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a05e58",
      "READ",
      [
        "storage",
        "002a17b9",
        null,
        "string"
      ]
    ],
    [
      "00a05fb4",
      "READ",
      [
        "storage",
        "002b96ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md#insn-00a05fc0) · [`00a05c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md#insn-00a05c7c) · [`00a05c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md#insn-00a05c84)
- 新版 [`00a0615c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a0615c) · [`00a05e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a05e18) · [`00a05e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md#insn-00a05e20)

~~~diff
- 00a05fc0 ["INT_ADD", "register:40f0:8", ["const:a05fc0:8", "const:4:8"]]
- 00a05fc0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00a0615c ["INT_ADD", "register:40f0:8", ["const:a0615c:8", "const:4:8"]]
+ 00a0615c ["CALL", null, ["callee:00c57eb0:8"]]
- 00a05fc0 bytes bc460994
+ 00a0615c bytes 55470994
- 00a05c7c ["INT_ADD", "register:40f0:8", ["const:a05c7c:8", "const:4:8"]]
- 00a05c7c ["CALL", null, ["callee:00487e20:8"]]
+ 00a05e18 ["INT_ADD", "register:40f0:8", ["const:a05e18:8", "const:4:8"]]
+ 00a05e18 ["CALL", null, ["callee:00487e20:8"]]
- 00a05c7c bytes 5908ea97
+ 00a05e18 bytes 0208ea97
- 00a05c84 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00a05c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a05c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a05c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a05e20 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00a05e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a05e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a05c84 bytes 08e12491
+ 00a05e20 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b5d096d64ee34168da82917de2a89f9"></a>

### [`00a06374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06374.md) → [`00a06510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md) FUN_00a06510

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 4件 [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`00732c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732c44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008d3410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3410.md)
- 新版 呼出元 1件 [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 4件 [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`00732c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732c84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

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
      "site": "00a065c0",
      "value": [
        "leaf",
        "ram:71c460:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a06424",
      "value": [
        "leaf",
        "ram:71c420:8"
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
      "00a065c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ]
  ],
  "added": [
    [
      "00a065c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a06424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06374.md#insn-00a06424) · [`00a06384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06374.md#insn-00a06384) · [`00a06394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06374.md#insn-00a06394)
- 新版 [`00a065c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a065c0) · [`00a06520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a06520) · [`00a06530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a06530)

~~~diff
- 00a06424 ["INT_ADD", "register:40f0:8", ["const:a06424:8", "const:4:8"]]
- 00a06424 ["CALL", null, ["ram:71c420:8"]]
+ 00a065c0 ["INT_ADD", "register:40f0:8", ["const:a065c0:8", "const:4:8"]]
+ 00a065c0 ["CALL", null, ["ram:71c460:8"]]
- 00a06424 bytes ff57f497
+ 00a065c0 bytes a857f497
- 00a06384 ["INT_ADD", "register:40f0:8", ["const:a06384:8", "const:4:8"]]
- 00a06384 ["CALL", null, ["callee:008514f8:8"]]
+ 00a06520 ["INT_ADD", "register:40f0:8", ["const:a06520:8", "const:4:8"]]
+ 00a06520 ["CALL", null, ["callee:008514f8:8"]]
- 00a06384 bytes 4d2cf997
+ 00a06520 bytes f62bf997
- 00a06394 ["INT_ADD", "register:40f0:8", ["const:a06394:8", "const:4:8"]]
- 00a06394 ["CALL", null, ["callee:00732c84:8"]]
+ 00a06530 ["INT_ADD", "register:40f0:8", ["const:a06530:8", "const:4:8"]]
+ 00a06530 ["CALL", null, ["callee:00732c84:8"]]
- 00a06394 bytes 2cb2f497
+ 00a06530 bytes d5b1f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b33f6551b79a7bced664871fc5b87d0"></a>

### [`00a06590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md) → [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) FUN_00a0672c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007ef2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md) · 呼出先 11件 [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00802cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802cac.md) [`00802d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md) [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md) [`00802e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802e2c.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007ef320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md) · 呼出先 11件 [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00802cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802cec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) [`00802e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802e6c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "site": "00a0679c",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a06600",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "site": "00a067f8",
      "value": [
        "leaf",
        "ram:803d7c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0665c",
      "value": [
        "leaf",
        "ram:803d3c:8"
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
      "00a0679c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "00a067f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803d3c"
      ]
    ]
  ],
  "added": [
    [
      "00a0679c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00a067f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00803d7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a06600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md#insn-00a06600) · [`00a0665c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md#insn-00a0665c) · [`00a065ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md#insn-00a065ac)
- 新版 [`00a0679c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a0679c) · [`00a067f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a067f8) · [`00a06748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md#insn-00a06748)

~~~diff
- 00a06600 ["INT_ADD", "register:40f0:8", ["const:a06600:8", "const:4:8"]]
- 00a06600 ["CALL", null, ["ram:a65bf4:8"]]
+ 00a0679c ["INT_ADD", "register:40f0:8", ["const:a0679c:8", "const:4:8"]]
+ 00a0679c ["CALL", null, ["ram:a65dec:8"]]
- 00a06600 bytes 7d7d0194
+ 00a0679c bytes 947d0194
- 00a0665c ["INT_ADD", "register:40f0:8", ["const:a0665c:8", "const:4:8"]]
- 00a0665c ["CALL", null, ["ram:803d3c:8"]]
+ 00a067f8 ["INT_ADD", "register:40f0:8", ["const:a067f8:8", "const:4:8"]]
+ 00a067f8 ["CALL", null, ["ram:803d7c:8"]]
- 00a0665c bytes b8f5f797
+ 00a067f8 bytes 61f5f797
- 00a065ac ["INT_ADD", "register:40f0:8", ["const:a065ac:8", "const:4:8"]]
- 00a065ac ["CALL", null, ["callee:008514f8:8"]]
+ 00a06748 ["INT_ADD", "register:40f0:8", ["const:a06748:8", "const:4:8"]]
+ 00a06748 ["CALL", null, ["callee:008514f8:8"]]
- 00a065ac bytes c32bf997
+ 00a06748 bytes 6c2bf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ee08f1e01cc11af62b5ba4389ffbb3"></a>

### [`00a0685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a0685c.md) → [`00a069f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md) FUN_00a069f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a05c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05c44.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00a05de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a05de0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00a06a04",
      "incomplete_value": false,
      "site": "00a06a08",
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
      "definition_site": "00a06868",
      "incomplete_value": false,
      "site": "00a0686c",
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
      "00a06a04",
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
      "00a06a04",
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

- 旧版 [`00a0686c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a0685c.md#insn-00a0686c) · [`00a06868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a0685c.md#insn-00a06868)
- 新版 [`00a06a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md#insn-00a06a08) · [`00a06a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069f8.md#insn-00a06a04)

~~~diff
- 00a0686c ["INT_ADD", "register:40f0:8", ["const:a0686c:8", "const:4:8"]]
- 00a0686c ["CALL", null, ["callee:0043b778:8"]]
+ 00a06a08 ["INT_ADD", "register:40f0:8", ["const:a06a08:8", "const:4:8"]]
+ 00a06a08 ["CALL", null, ["callee:0043b778:8"]]
- 00a0686c bytes b3d3e897
+ 00a06a08 bytes 5cd3e897
- 00a06868 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00a06868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a06868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a06868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a06a04 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00a06a04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a06a04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a06a04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a06868 bytes 00303c91
+ 00a06a04 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41538961c79f7eb8ef285aa058c207ad"></a>

### [`00a06870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06870.md) → [`00a06a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06a0c.md) _INIT_207

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06a8c",
      "incomplete_value": true,
      "site": "00a06aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a068f0",
      "incomplete_value": true,
      "site": "00a0690c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a06aac",
      "incomplete_value": true,
      "site": "00a06ac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a06910",
      "incomplete_value": true,
      "site": "00a06928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06ac8",
      "incomplete_value": true,
      "site": "00a06ae4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ac000:8"
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
      "definition_site": "00a0692c",
      "incomplete_value": true,
      "site": "00a06948",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ac000:8"
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
      "00a06a48",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a06a6c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00a06a8c",
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
      "00a06a48",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a06a6c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a06a8c",
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

- 旧版 [`00a06908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06870.md#insn-00a06908) · [`00a06aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06870.md#insn-00a06aa4) · [`00a0689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06870.md#insn-00a0689c)
- 新版 [`00a06aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06a0c.md#insn-00a06aa4) · [`00a06c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06a0c.md#insn-00a06c40) · [`00a06a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06a0c.md#insn-00a06a38)

~~~diff
- 00a06908 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00a06908 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00a06908 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00a06908 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00a06aa4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00a06aa4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00a06aa4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00a06aa4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00a06908 bytes 4a553a91
+ 00a06aa4 bytes 4a893d91
- 00a06aa4 ["INT_ADD", "register:40f0:8", ["const:a06aa4:8", "const:4:8"]]
- 00a06aa4 ["CALL", null, ["callee:00c57e30:8"]]
+ 00a06c40 ["INT_ADD", "register:40f0:8", ["const:a06c40:8", "const:4:8"]]
+ 00a06c40 ["CALL", null, ["callee:00c57e30:8"]]
- 00a06aa4 bytes e3430994
+ 00a06c40 bytes 7c440994
- 00a0689c ["COPY", "tmp:0:8", ["const:968:8"]]
- 00a0689c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a0689c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a0689c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a06a38 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00a06a38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a06a38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a06a38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a0689c bytes 73a22591
+ 00a06a38 bytes 73a23591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59cd7cc885ebaf9ae9ab1fc8f673f0a"></a>

### [`00a148e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md) → [`00a14a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md) FUN_00a14a80

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b1eb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md) · 呼出先 14件 [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`0048206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/0048206c.md) [`00482570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482570.md) [`004825a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md)
- 新版 呼出元 1件 [`00b1ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md) · 呼出先 14件 [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`004820ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820ac.md) [`004825b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825b0.md) [`004825e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a14b9c",
      "incomplete_value": true,
      "site": "00a14ba0",
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
      "definition_site": "00a14a00",
      "incomplete_value": true,
      "site": "00a14a04",
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
      "definition_site": "00a14c3c",
      "incomplete_value": true,
      "site": "00a14c40",
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
                "const:530:8"
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
      "definition_site": "00a14aa0",
      "incomplete_value": true,
      "site": "00a14aa4",
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
                "const:130:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a14b88",
      "value": [
        "leaf",
        "ram:a06d9c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a149ec",
      "value": [
        "leaf",
        "ram:a06c00:8"
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
      "00a14ab8",
      "READ",
      [
        "storage",
        "002a1500",
        null,
        "string"
      ]
    ],
    [
      "00a14b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a06c00"
      ]
    ],
    [
      "00a14b94",
      "READ",
      [
        "storage",
        "00c9a898",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a14ab8",
      "READ",
      [
        "storage",
        "002a15cd",
        null,
        "string"
      ]
    ],
    [
      "00a14b88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a06d9c"
      ]
    ],
    [
      "00a14b94",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a149ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md#insn-00a149ec) · [`00a1490c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md#insn-00a1490c) · [`00a14914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md#insn-00a14914)
- 新版 [`00a14b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md#insn-00a14b88) · [`00a14aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md#insn-00a14aa8) · [`00a14ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md#insn-00a14ab0)

~~~diff
- 00a149ec ["INT_ADD", "register:40f0:8", ["const:a149ec:8", "const:4:8"]]
- 00a149ec ["CALL", null, ["ram:a06c00:8"]]
+ 00a14b88 ["INT_ADD", "register:40f0:8", ["const:a14b88:8", "const:4:8"]]
+ 00a14b88 ["CALL", null, ["ram:a06d9c:8"]]
- 00a149ec bytes 85c8ff97
+ 00a14b88 bytes 85c8ff97
- 00a1490c ["INT_ADD", "register:40f0:8", ["const:a1490c:8", "const:4:8"]]
- 00a1490c ["CALL", null, ["callee:00481430:8"]]
+ 00a14aa8 ["INT_ADD", "register:40f0:8", ["const:a14aa8:8", "const:4:8"]]
+ 00a14aa8 ["CALL", null, ["callee:00481430:8"]]
- 00a1490c bytes b9b2e997
+ 00a14aa8 bytes 62b2e997
- 00a14914 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a14914 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a14914 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a14914 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a14ab0 ["COPY", "tmp:0:8", ["const:5cd:8"]]
+ 00a14ab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a14ab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a14ab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a14914 bytes 29011491
+ 00a14ab0 bytes 29351791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-594472315368ec0400c4aff0076a1368"></a>

### [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) → [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) FUN_00a1a6a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 127件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0045ab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045ab2c.md) [`0045c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045c8c8.md) [`0045d974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045d974.md) [`00599674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599674.md) · 呼出先 3件 [`00a14bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a14bf0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 127件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0045c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md) [`0045d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md) [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) · 呼出先 3件 [`00a14d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14d8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a1a6d8",
      "incomplete_value": true,
      "site": "00a1a6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1a53c",
      "incomplete_value": true,
      "site": "00a1a53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a1a6e4",
      "value": [
        "leaf",
        "ram:a14d8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a1a548",
      "value": [
        "leaf",
        "ram:a14bf0:8"
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
      "00a1a6c4",
      "READ",
      [
        "storage",
        "002a1500",
        null,
        "string"
      ]
    ],
    [
      "00a1a6e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14bf0"
      ]
    ]
  ],
  "added": [
    [
      "00a1a6c4",
      "READ",
      [
        "storage",
        "002a15cd",
        null,
        "string"
      ]
    ],
    [
      "00a1a6e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14d8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1a548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md#insn-00a1a548) · [`00a1a520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md#insn-00a1a520) · [`00a1a55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md#insn-00a1a55c)
- 新版 [`00a1a6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md#insn-00a1a6e4) · [`00a1a6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md#insn-00a1a6bc) · [`00a1a6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md#insn-00a1a6f8)

~~~diff
- 00a1a548 ["INT_ADD", "register:40f0:8", ["const:a1a548:8", "const:4:8"]]
- 00a1a548 ["CALL", null, ["ram:a14bf0:8"]]
+ 00a1a6e4 ["INT_ADD", "register:40f0:8", ["const:a1a6e4:8", "const:4:8"]]
+ 00a1a6e4 ["CALL", null, ["ram:a14d8c:8"]]
- 00a1a548 bytes aae9ff97
+ 00a1a6e4 bytes aae9ff97
- 00a1a520 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00a1a520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a1a520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a1a520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a1a6bc ["COPY", "tmp:0:8", ["const:5cd:8"]]
+ 00a1a6bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1a6bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1a6bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a1a520 bytes 29011491
+ 00a1a6bc bytes 29351791
- 00a1a55c ["INT_ADD", "register:40f0:8", ["const:a1a55c:8", "const:4:8"]]
- 00a1a55c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00a1a6f8 ["INT_ADD", "register:40f0:8", ["const:a1a6f8:8", "const:4:8"]]
+ 00a1a6f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00a1a55c bytes 55f50894
+ 00a1a6f8 bytes eef50894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afff7185de55e309482ca4d2de269821"></a>

### [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) → [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) FUN_00a1a750

採用 · 移動量 `+0x19c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) [`00b1eb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1eb70.md) · 呼出先 41件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md)
- 新版 呼出元 2件 [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) [`00b1ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md) · 呼出先 41件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.66% / 新版 99.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a1a7a8",
      "incomplete_value": true,
      "site": "00a1a7a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1a60c",
      "incomplete_value": true,
      "site": "00a1a60c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:835:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a1f328",
      "incomplete_value": false,
      "site": "00a1f32c",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:530:8"
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
      "definition_site": "00a1f18c",
      "incomplete_value": false,
      "site": "00a1f190",
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
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:130:8"
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
    "ordinal": 1182,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a1a798",
      "READ",
      [
        "storage",
        "002b6835",
        null,
        "string"
      ]
    ],
    [
      "00a1a940",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "qword"
      ]
    ],
    [
      "00a1b184",
      "DATA",
      [
        "storage",
        "00344154",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "00a1a798",
      "READ",
      [
        "storage",
        "002b6875",
        null,
        "string"
      ]
    ],
    [
      "00a1a940",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "uleb128"
      ]
    ],
    [
      "00a1b184",
      "DATA",
      [
        "storage",
        "00344154",
        null,
        "byte[55]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a1a5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md#insn-00a1a5ec) · [`00a1a5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md#insn-00a1a5f4) · [`00a1a618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md#insn-00a1a618)
- 新版 [`00a1a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md#insn-00a1a788) · [`00a1a790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md#insn-00a1a790) · [`00a1a7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md#insn-00a1a7b4)

~~~diff
- 00a1a5ec ["INT_ADD", "register:40f0:8", ["const:a1a5ec:8", "const:4:8"]]
- 00a1a5ec ["CALL", null, ["callee:00481430:8"]]
+ 00a1a788 ["INT_ADD", "register:40f0:8", ["const:a1a788:8", "const:4:8"]]
+ 00a1a788 ["CALL", null, ["callee:00481430:8"]]
- 00a1a5ec bytes 819be997
+ 00a1a788 bytes 2a9be997
- 00a1a5f4 ["COPY", "tmp:0:8", ["const:835:8"]]
- 00a1a5f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a1a5f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a1a5f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a1a790 ["COPY", "tmp:0:8", ["const:875:8"]]
+ 00a1a790 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1a790 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a1a790 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a1a5f4 bytes 29d52091
+ 00a1a790 bytes 29d52191
- 00a1a618 ["INT_ADD", "register:40f0:8", ["const:a1a618:8", "const:4:8"]]
- 00a1a618 ["CALL", null, ["callee:00483ff0:8"]]
+ 00a1a7b4 ["INT_ADD", "register:40f0:8", ["const:a1a7b4:8", "const:4:8"]]
+ 00a1a7b4 ["CALL", null, ["callee:00483ff0:8"]]
- 00a1a618 bytes 66a6e997
+ 00a1a7b4 bytes 0fa6e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eebdd504364bdf781f1736b37fdba8ca"></a>

### [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) → [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) FUN_00a223d0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 27件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)
- 新版 呼出元 3件 [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 27件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.69% / 新版 99.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a22428",
      "incomplete_value": true,
      "site": "00a22428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2228c",
      "incomplete_value": true,
      "site": "00a2228c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:835:8"
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
      "definition_site": "00a2242c",
      "incomplete_value": true,
      "site": "00a2242c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:875:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a22290",
      "incomplete_value": true,
      "site": "00a22290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:835:8"
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
      "definition_site": "00a25a28",
      "incomplete_value": true,
      "site": "00a25a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2588c",
      "incomplete_value": true,
      "site": "00a2588c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a22418",
      "READ",
      [
        "storage",
        "002b6835",
        null,
        "string"
      ]
    ],
    [
      "00a22b24",
      "DATA",
      [
        "storage",
        "00295fcc",
        "lsda_exception_table_00295fcc",
        "dwfenc"
      ]
    ],
    [
      "00a22b24",
      "DATA",
      [
        "storage",
        "00295fe0",
        "lsda_exception_table_00295fe0",
        "dwfenc"
      ]
    ]
  ],
  "added": [
    [
      "00a22418",
      "READ",
      [
        "storage",
        "002b6875",
        null,
        "string"
      ]
    ],
    [
      "00a22b24",
      "DATA",
      [
        "storage",
        "00295fcc",
        null,
        "uleb128"
      ]
    ],
    [
      "00a22b24",
      "DATA",
      [
        "storage",
        "00295fe0",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a256f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md#insn-00a256f0) · [`00a256fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md#insn-00a256fc) · [`00a25898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md#insn-00a25898)
- 新版 [`00a2588c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md#insn-00a2588c) · [`00a25898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md#insn-00a25898) · [`00a25a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md#insn-00a25a34)

~~~diff
- 00a256f0 ["INT_ADD", "register:40f0:8", ["const:a256f0:8", "const:4:8"]]
- 00a256f0 ["CALL", null, ["callee:00480b38:8"]]
+ 00a2588c ["INT_ADD", "register:40f0:8", ["const:a2588c:8", "const:4:8"]]
+ 00a2588c ["CALL", null, ["callee:00480b38:8"]]
- 00a256f0 bytes 026de997
+ 00a2588c bytes ab6ce997
- 00a256fc ["INT_ADD", "register:40f0:8", ["const:a256fc:8", "const:4:8"]]
- 00a256fc ["CALL", null, ["callee:00480b90:8"]]
+ 00a25898 ["INT_ADD", "register:40f0:8", ["const:a25898:8", "const:4:8"]]
+ 00a25898 ["CALL", null, ["callee:00480b90:8"]]
- 00a256fc bytes 156de997
+ 00a25898 bytes be6ce997
- 00a25898 ["INT_ADD", "register:40f0:8", ["const:a25898:8", "const:4:8"]]
- 00a25898 ["CALL", null, ["ram:a14bf0:8"]]
+ 00a25a34 ["INT_ADD", "register:40f0:8", ["const:a25a34:8", "const:4:8"]]
+ 00a25a34 ["CALL", null, ["ram:a14d8c:8"]]
- 00a25898 bytes d6bcff97
+ 00a25a34 bytes d6bcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b03634b7c3b68b5124b96ae20ba05d9f"></a>

### [`00a25c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c7c.md) → [`00a25e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e18.md) FUN_00a25e18

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00a25e24",
      "incomplete_value": false,
      "site": "00a25e28",
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
      "definition_site": "00a25c88",
      "incomplete_value": false,
      "site": "00a25c8c",
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
      "00a25e24",
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
      "00a25e24",
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

- 旧版 [`00a25c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c7c.md#insn-00a25c8c) · [`00a25c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c7c.md#insn-00a25c88)
- 新版 [`00a25e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e18.md#insn-00a25e28) · [`00a25e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e18.md#insn-00a25e24)

~~~diff
- 00a25c8c ["INT_ADD", "register:40f0:8", ["const:a25c8c:8", "const:4:8"]]
- 00a25c8c ["CALL", null, ["callee:0043b778:8"]]
+ 00a25e28 ["INT_ADD", "register:40f0:8", ["const:a25e28:8", "const:4:8"]]
+ 00a25e28 ["CALL", null, ["callee:0043b778:8"]]
- 00a25c8c bytes ab56e897
+ 00a25e28 bytes 5456e897
- 00a25c88 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00a25c88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a25c88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a25c88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a25e24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00a25e24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a25e24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a25e24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a25c88 bytes 00303c91
+ 00a25e24 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a68575127f2a8bd11d5fa6d648e02504"></a>

### [`00a25c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c90.md) → [`00a25e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e2c.md) _INIT_208

採用 · 移動量 `+0x19c` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00a25e68",
      "incomplete_value": true,
      "site": "00a25e84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a25ccc",
      "incomplete_value": true,
      "site": "00a25ce8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a25e8c",
      "incomplete_value": true,
      "site": "00a25ea8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a25cf0",
      "incomplete_value": true,
      "site": "00a25d0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a25eac",
      "incomplete_value": true,
      "site": "00a25ec8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a25d10",
      "incomplete_value": true,
      "site": "00a25d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a25e68",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a25e8c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00a25eac",
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
      "00a25e68",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a25e8c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a25eac",
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

- 旧版 [`00a25d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c90.md#insn-00a25d28) · [`00a25df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c90.md#insn-00a25df0) · [`00a25ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a25/00a25c90.md#insn-00a25ea8)
- 新版 [`00a25ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e2c.md#insn-00a25ec4) · [`00a25f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e2c.md#insn-00a25f8c) · [`00a26044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a25/00a25e2c.md#insn-00a26044)

~~~diff
- 00a25d28 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00a25d28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00a25d28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00a25d28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00a25ec4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00a25ec4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00a25ec4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00a25ec4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00a25d28 bytes 4a553a91
+ 00a25ec4 bytes 4a893d91
- 00a25df0 ["INT_ADD", "register:40f0:8", ["const:a25df0:8", "const:4:8"]]
- 00a25df0 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00a25f8c ["INT_ADD", "register:40f0:8", ["const:a25f8c:8", "const:4:8"]]
+ 00a25f8c ["CALL", null, ["callee:0043b7f8:8"]]
- 00a25df0 bytes 7256e897
+ 00a25f8c bytes 1b56e897
- 00a25ea8 ["INT_ADD", "register:40f0:8", ["const:a25ea8:8", "const:4:8"]]
- 00a25ea8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00a26044 ["INT_ADD", "register:40f0:8", ["const:a26044:8", "const:4:8"]]
+ 00a26044 ["CALL", null, ["callee:00c57eb0:8"]]
- 00a25ea8 bytes 02c70894
+ 00a26044 bytes 9bc70894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca3130a17fe0174368e432625c4fd154"></a>

### [`00a2a638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2a638.md) → [`00a2a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2a830.md) FUN_00a2a830

採用 · 移動量 `+0x1f8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 23.33% / 新版 23.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 3件, `unresolved_branch_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2a790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2a80c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2a8b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2a724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2a904"
      ]
    ],
    [
      "unmatched:00a2a730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2a910"
      ]
    ],
    [
      "unmatched:00a2a790",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a2a91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2a904"
      ]
    ],
    [
      "00a2a928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2a910"
      ]
    ],
    [
      "00a2a988",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2a724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2a638.md#insn-00a2a724) · [`00a2a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2a638.md#insn-00a2a730) · [`00a2a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2a638.md#insn-00a2a790)

~~~diff
- 00a2a724 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a2a724 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a2a724 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a2a724 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
- 00a2a724 bytes 4cffff54
- 00a2a730 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a2a730 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a2a730 bytes 48ffffb5
- 00a2a790 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a2a790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00a2a790 bytes e01300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2af4ff2175a8d92a2fc36258633a28b"></a>

### [`00a2ab94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2ab94.md) → [`00a2ad8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2ad8c.md) FUN_00a2ad8c

採用 · 移動量 `+0x1f8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`004802b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004802b8.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 23.33% / 新版 23.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2abc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2abcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2abd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2abc0",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2abcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2abd0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a2adb8",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ],
    [
      "00a2adc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a2adc8",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2abc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2ab94.md#insn-00a2abc0) · [`00a2abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2ab94.md#insn-00a2abcc) · [`00a2abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2a/00a2ab94.md#insn-00a2abd0)

~~~diff
- 00a2abc0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a2abc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a2abc0 bytes e80700f9
- 00a2abcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2abcc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2abcc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2abcc bytes a8831ff8
- 00a2abd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00a2abd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00a2abd0 bytes e11b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d1731998f926fa6f272fbfd32d9171"></a>

### [`00a2e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md) → [`00a2e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e568.md) FUN_00a2e568

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 11件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`0066b964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b964.md)
- 新版 呼出元 1件 [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 11件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`0066b9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066b/0066b9a4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 33.33% / 新版 32.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2e628"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2e774"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a2e820"
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
      "unmatched:00a2e628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2e80c"
      ]
    ],
    [
      "unmatched:00a2e76c",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2e774",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2e9c4"
      ]
    ]
  ],
  "added": [
    [
      "00a2e820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2e80c"
      ]
    ],
    [
      "00a2e964",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a2e96c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2e9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md#insn-00a2e430) · [`00a2e478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md#insn-00a2e478) · [`00a2e4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md#insn-00a2e4cc)
- 新版 [`00a2e628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e568.md#insn-00a2e628) · [`00a2e670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e568.md#insn-00a2e670) · [`00a2e6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e568.md#insn-00a2e6c4)

~~~diff
- 00a2e430 ["INT_ADD", "register:40f0:8", ["const:a2e430:8", "const:4:8"]]
- 00a2e430 ["CALL", null, ["callee:00480be8:8"]]
+ 00a2e628 ["INT_ADD", "register:40f0:8", ["const:a2e628:8", "const:4:8"]]
+ 00a2e628 ["CALL", null, ["callee:00480be8:8"]]
- 00a2e430 bytes de49e997
+ 00a2e628 bytes 7049e997
- 00a2e478 ["INT_ADD", "register:40f0:8", ["const:a2e478:8", "const:4:8"]]
- 00a2e478 ["CALL", null, ["callee:00480be8:8"]]
+ 00a2e670 ["INT_ADD", "register:40f0:8", ["const:a2e670:8", "const:4:8"]]
+ 00a2e670 ["CALL", null, ["callee:00480be8:8"]]
- 00a2e478 bytes cc49e997
+ 00a2e670 bytes 5e49e997
- 00a2e4cc ["INT_ADD", "register:40f0:8", ["const:a2e4cc:8", "const:4:8"]]
- 00a2e4cc ["CALL", null, ["callee:00480be8:8"]]
+ 00a2e6c4 ["INT_ADD", "register:40f0:8", ["const:a2e6c4:8", "const:4:8"]]
+ 00a2e6c4 ["CALL", null, ["callee:00480be8:8"]]
- 00a2e4cc bytes b749e997
+ 00a2e6c4 bytes 4949e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88da4d60581cd2b620acfea1785230e9"></a>

### [`00a2e8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e8fc.md) → [`00a2eaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2eaf4.md) FUN_00a2eaf4

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2e7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e7d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a2e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e9c8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 62.50% / 新版 64.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 2件, `store_condition` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2e944"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2e984"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a2eb7c"
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
      "unmatched:00a2e944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ebf8"
      ]
    ],
    [
      "unmatched:00a2e984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2eb6c"
      ]
    ],
    [
      "00a2eb3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ec84"
      ]
    ]
  ],
  "added": [
    [
      "00a2eb3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ebf8"
      ]
    ],
    [
      "00a2eb7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2eb6c"
      ]
    ],
    [
      "00a2ec74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ec84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2e944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e8fc.md#insn-00a2e944) · [`00a2e984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e8fc.md#insn-00a2e984)
- 新版 [`00a2eb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2eaf4.md#insn-00a2eb7c)

~~~diff
- 00a2e944 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a2e944 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00a2e944 bytes ea050054
- 00a2e984 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00a2e984 bytes 80ffff54
+ 00a2eb7c ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 00a2eb7c bytes 80ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4003046a5ca439c14d8c2d4757eea4"></a>

### [`00a2eaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2eaa4.md) → [`00a2ec9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md) FUN_00a2ec9c

採用 · 移動量 `+0x1f8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a2ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2ebc8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a2edc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 34.62% / 新版 32.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2eac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a2ecc0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2eb7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2eac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2eb7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ed6c"
      ]
    ],
    [
      "unmatched:00a2eba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2edbc"
      ]
    ]
  ],
  "added": [
    [
      "00a2ecc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00a2ed74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2ed6c"
      ]
    ],
    [
      "00a2eda0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2edbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2eac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2eaa4.md#insn-00a2eac8) · [`00a2eb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2eaa4.md#insn-00a2eb00) · [`00a2eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2eaa4.md#insn-00a2eb20)
- 新版 [`00a2ecf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md#insn-00a2ecf8) · [`00a2ed18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md#insn-00a2ed18)

~~~diff
- 00a2eac8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2eac8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2eac8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2eac8 bytes a8831ff8
- 00a2eb00 ["INT_ADD", "register:40f0:8", ["const:a2eb00:8", "const:4:8"]]
- 00a2eb00 ["CALL", null, ["callee:00a2edc0:8"]]
+ 00a2ecf8 ["INT_ADD", "register:40f0:8", ["const:a2ecf8:8", "const:4:8"]]
+ 00a2ecf8 ["CALL", null, ["callee:00a2edc0:8"]]
- 00a2eb00 bytes 32000094
+ 00a2ecf8 bytes 32000094
- 00a2eb20 ["INT_ADD", "register:40f0:8", ["const:a2eb20:8", "const:4:8"]]
- 00a2eb20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a2ed18 ["INT_ADD", "register:40f0:8", ["const:a2ed18:8", "const:4:8"]]
+ 00a2ed18 ["CALL", null, ["callee:00c57e90:8"]]
- 00a2eb20 bytes dca30894
+ 00a2ed18 bytes 5ea40894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46002e3f0923167537118c36ab7dc1ca"></a>

### [`00a2ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2ebc8.md) → [`00a2edc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md) FUN_00a2edc0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2eaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2eaa4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a2ec9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.00% / 新版 83.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00a2ed58",
      "incomplete_value": true,
      "site": "00a2ed60",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a2ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2ebc8.md#insn-00a2ebd0) · [`00a2ebe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2ebc8.md#insn-00a2ebe0) · [`00a2ebf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2ebc8.md#insn-00a2ebf0)
- 新版 [`00a2edc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md#insn-00a2edc8) · [`00a2edd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md#insn-00a2edd8) · [`00a2ede8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md#insn-00a2ede8)

~~~diff
- 00a2ebd0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00a2edc8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00a2ebd0 bytes a0000054
+ 00a2edc8 bytes a0000054
- 00a2ebe0 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a2ebe0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a2edd8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a2edd8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a2ebe0 bytes 6a010054
+ 00a2edd8 bytes 6a010054
- 00a2ebf0 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00a2ede8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00a2ebf0 bytes 20020054
+ 00a2ede8 bytes 20020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c52ac9a038ca9fbf273af81c2b65fe0c"></a>

### [`00a2f090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f090.md) → [`00a2f288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f288.md) FUN_00a2f288

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00a2f294",
      "incomplete_value": false,
      "site": "00a2f298",
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
      "definition_site": "00a2f09c",
      "incomplete_value": false,
      "site": "00a2f0a0",
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
      "00a2f294",
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
      "00a2f294",
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

- 旧版 [`00a2f0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f090.md#insn-00a2f0a0) · [`00a2f09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f090.md#insn-00a2f09c)
- 新版 [`00a2f298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f288.md#insn-00a2f298) · [`00a2f294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f288.md#insn-00a2f294)

~~~diff
- 00a2f0a0 ["INT_ADD", "register:40f0:8", ["const:a2f0a0:8", "const:4:8"]]
- 00a2f0a0 ["CALL", null, ["callee:00442930:8"]]
+ 00a2f298 ["INT_ADD", "register:40f0:8", ["const:a2f298:8", "const:4:8"]]
+ 00a2f298 ["CALL", null, ["callee:00442930:8"]]
- 00a2f0a0 bytes 144ee897
+ 00a2f298 bytes a64de897
- 00a2f09c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00a2f09c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a2f09c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a2f09c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a2f294 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00a2f294 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a2f294 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a2f294 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a2f09c bytes 00303c91
+ 00a2f294 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa697f1d821a21a8fd8f083255d4b93"></a>

### [`00a2f0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f0a4.md) → [`00a2f29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f29c.md) _INIT_209

採用 · 移動量 `+0x1f8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 34.15% / 新版 35.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f0d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f0fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2f0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2f0e0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a2f0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a2f2cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a2f2d8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a2f2f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2f0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f0a4.md#insn-00a2f0d4) · [`00a2f0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f0a4.md#insn-00a2f0fc) · [`00a2f120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f0a4.md#insn-00a2f120)

~~~diff
- 00a2f0d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a2f0d4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2f0d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2f0d4 bytes a9831ff8
- 00a2f0fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a2f0fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a2f0fc bytes e013813c
- 00a2f120 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a2f120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a2f120 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef6eeda126f20ac99a70db5c19ae0058"></a>

### [`00a2f434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md) → [`00a2f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f62c.md) FUN_00a2f62c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.37% / 新版 52.37%

CFGの説明率　旧版 21.23% / 新版 20.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 44件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f584"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2f484",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a2f484",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2f488",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00869e54"
      ]
    ]
  ],
  "added": [
    [
      "00a2f67c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a2f67c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "00a2f680",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00869e54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md#insn-00a2f484) · [`00a2f4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md#insn-00a2f4b4) · [`00a2f584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md#insn-00a2f584)

~~~diff
- 00a2f484 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00a2f484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a2f484 bytes e81f00f9
- 00a2f4b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:21:8"]]
- 00a2f4b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a2f4b4 bytes e013823c
- 00a2f584 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00a2f584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00a2f584 bytes 142000b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91f36d4a43715d08e30e41b40533442f"></a>

### [`00a2fb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fb24.md) → [`00a2fd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fd1c.md) FUN_00a2fd1c

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`0089bc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089bc48.md) · 呼出先 6件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005975e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 6件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00597628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597628.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.19% / 新版 71.19%

CFGの説明率　旧版 23.08% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2fb2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a2fb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fb2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a2fb44",
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
      "00a2fd20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a2fd24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a2fd3c",
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

- 旧版 [`00a2fb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fb24.md#insn-00a2fb28) · [`00a2fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fb24.md#insn-00a2fb2c) · [`00a2fb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fb24.md#insn-00a2fb44)

~~~diff
- 00a2fb28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a2fb28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a2fb28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a2fb28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2fb28 bytes fd7b05a9
- 00a2fb2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a2fb2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a2fb2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a2fb2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a2fb2c bytes f44f06a9
- 00a2fb44 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a2fb44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a2fb44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a2fb44 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82a98def3e883a6a0b1581bfafe7a535"></a>

### [`00a2fc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fc90.md) → [`00a2fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md) FUN_00a2fe88

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 10件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 10件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a2ff74",
      "incomplete_value": false,
      "site": "00a2ff78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:7b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2fd7c",
      "incomplete_value": false,
      "site": "00a2fd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:771:8"
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
      "00a2ff74",
      "PARAM",
      [
        "storage",
        "002bb771",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a2ff74",
      "PARAM",
      [
        "storage",
        "002bb7b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2fd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fc90.md#insn-00a2fd80) · [`00a2fd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fc90.md#insn-00a2fd34) · [`00a2fd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fc90.md#insn-00a2fd48)
- 新版 [`00a2ff78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md#insn-00a2ff78) · [`00a2ff2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md#insn-00a2ff2c) · [`00a2ff40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md#insn-00a2ff40)

~~~diff
- 00a2fd80 ["INT_ADD", "register:40f0:8", ["const:a2fd80:8", "const:4:8"]]
- 00a2fd80 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a2ff78 ["INT_ADD", "register:40f0:8", ["const:a2ff78:8", "const:4:8"]]
+ 00a2ff78 ["CALL", null, ["callee:00c57f60:8"]]
- 00a2fd80 bytes 789f0894
+ 00a2ff78 bytes fa9f0894
- 00a2fd34 ["INT_ADD", "register:40f0:8", ["const:a2fd34:8", "const:4:8"]]
- 00a2fd34 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a2ff2c ["INT_ADD", "register:40f0:8", ["const:a2ff2c:8", "const:4:8"]]
+ 00a2ff2c ["CALL", null, ["callee:00c57e90:8"]]
- 00a2fd34 bytes 579f0894
+ 00a2ff2c bytes d99f0894
- 00a2fd48 ["INT_ADD", "register:40f0:8", ["const:a2fd48:8", "const:4:8"]]
- 00a2fd48 ["CALL", null, ["callee:00c58000:8"]]
+ 00a2ff40 ["INT_ADD", "register:40f0:8", ["const:a2ff40:8", "const:4:8"]]
+ 00a2ff40 ["CALL", null, ["callee:00c58000:8"]]
- 00a2fd48 bytes ae9f0894
+ 00a2ff40 bytes 30a00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2dd13f861db807d073104ef3ad01930"></a>

### [`00a2ff5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2ff5c.md) → [`00a30154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30154.md) FUN_00a30154

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`0089bc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089bc48.md) · 呼出先 9件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 2件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a30240",
      "incomplete_value": true,
      "site": "00a30250",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:c09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a30048",
      "incomplete_value": true,
      "site": "00a30058",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:bc9:8"
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
      "00a30240",
      "READ",
      [
        "storage",
        "002aebc9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a30240",
      "READ",
      [
        "storage",
        "002aec09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a30008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2ff5c.md#insn-00a30008) · [`00a3001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2ff5c.md#insn-00a3001c) · [`00a30044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2ff5c.md#insn-00a30044)
- 新版 [`00a30200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30154.md#insn-00a30200) · [`00a30214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30154.md#insn-00a30214) · [`00a3023c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30154.md#insn-00a3023c)

~~~diff
- 00a30008 ["INT_ADD", "register:40f0:8", ["const:a30008:8", "const:4:8"]]
- 00a30008 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a30200 ["INT_ADD", "register:40f0:8", ["const:a30200:8", "const:4:8"]]
+ 00a30200 ["CALL", null, ["callee:00c57e90:8"]]
- 00a30008 bytes a29e0894
+ 00a30200 bytes 249f0894
- 00a3001c ["INT_ADD", "register:40f0:8", ["const:a3001c:8", "const:4:8"]]
- 00a3001c ["CALL", null, ["callee:00c58000:8"]]
+ 00a30214 ["INT_ADD", "register:40f0:8", ["const:a30214:8", "const:4:8"]]
+ 00a30214 ["CALL", null, ["callee:00c58000:8"]]
- 00a3001c bytes f99e0894
+ 00a30214 bytes 7b9f0894
- 00a30044 ["COPY", "tmp:0:8", ["const:bc9:8"]]
- 00a30044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a30044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a30044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3023c ["COPY", "tmp:0:8", ["const:c09:8"]]
+ 00a3023c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3023c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3023c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a30044 bytes 08252f91
+ 00a3023c bytes 08253091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da0c17fea7f7f50f1d9f62a17831814"></a>

### [`00a3025c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a3025c.md) → [`00a30454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30454.md) FUN_00a30454

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2c028.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md)
- 新版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 48.61% / 新版 48.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a303f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3042c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30474"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a30360",
      "PARAM",
      [
        "storage",
        "002bb771",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a303f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a305d8"
      ]
    ],
    [
      "unmatched:00a3042c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30630"
      ]
    ]
  ],
  "added": [
    [
      "00a30558",
      "PARAM",
      [
        "storage",
        "002bb7b1",
        null,
        "string"
      ]
    ],
    [
      "00a305e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a305d8"
      ]
    ],
    [
      "00a30624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30630"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a30364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a3025c.md#insn-00a30364) · [`00a30394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a3025c.md#insn-00a30394) · [`00a303f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a3025c.md#insn-00a303f0)
- 新版 [`00a3055c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30454.md#insn-00a3055c) · [`00a3058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30454.md#insn-00a3058c)

~~~diff
- 00a30364 ["INT_ADD", "register:40f0:8", ["const:a30364:8", "const:4:8"]]
- 00a30364 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a3055c ["INT_ADD", "register:40f0:8", ["const:a3055c:8", "const:4:8"]]
+ 00a3055c ["CALL", null, ["callee:00c57f60:8"]]
- 00a30364 bytes ff9d0894
+ 00a3055c bytes 819e0894
- 00a30394 ["INT_ADD", "register:40f0:8", ["const:a30394:8", "const:4:8"]]
- 00a30394 ["CALL", null, ["callee:00493998:8"]]
+ 00a3058c ["INT_ADD", "register:40f0:8", ["const:a3058c:8", "const:4:8"]]
+ 00a3058c ["CALL", null, ["callee:00493998:8"]]
- 00a30394 bytes 718de997
+ 00a3058c bytes 038de997
- 00a303f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a303f0 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00a303f0 bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-990ebd7db645d1553ceeea4c06d9648a"></a>

### [`00a30648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30648.md) → [`00a30840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30840.md) FUN_00a30840

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) [`0089bc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089bc48.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md)
- 新版 呼出元 2件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3095c",
      "incomplete_value": true,
      "site": "00a3096c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:c09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a30764",
      "incomplete_value": true,
      "site": "00a30774",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:bc9:8"
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
      "00a3095c",
      "READ",
      [
        "storage",
        "002aebc9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a3095c",
      "READ",
      [
        "storage",
        "002aec09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30648.md#insn-00a3096c) · [`00a30714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30648.md#insn-00a30714) · [`00a30730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30648.md#insn-00a30730)
- 新版 [`00a30b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30840.md#insn-00a30b64) · [`00a3090c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30840.md#insn-00a3090c) · [`00a30928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30840.md#insn-00a30928)

~~~diff
- 00a3096c ["INT_ADD", "register:40f0:8", ["const:a3096c:8", "const:4:8"]]
- 00a3096c ["CALL", null, ["callee:00440ec0:8"]]
+ 00a30b64 ["INT_ADD", "register:40f0:8", ["const:a30b64:8", "const:4:8"]]
+ 00a30b64 ["CALL", null, ["callee:00440ec0:8"]]
- 00a3096c bytes 4541e897
+ 00a30b64 bytes d740e897
- 00a30714 ["INT_ADD", "register:40f0:8", ["const:a30714:8", "const:4:8"]]
- 00a30714 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a3090c ["INT_ADD", "register:40f0:8", ["const:a3090c:8", "const:4:8"]]
+ 00a3090c ["CALL", null, ["callee:00c57e90:8"]]
- 00a30714 bytes df9c0894
+ 00a3090c bytes 619d0894
- 00a30730 ["INT_ADD", "register:40f0:8", ["const:a30730:8", "const:4:8"]]
- 00a30730 ["CALL", null, ["callee:00c58000:8"]]
+ 00a30928 ["INT_ADD", "register:40f0:8", ["const:a30928:8", "const:4:8"]]
+ 00a30928 ["CALL", null, ["callee:00c58000:8"]]
- 00a30730 bytes 349d0894
+ 00a30928 bytes b69d0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f530683b60da1df6a898094d3e331cb5"></a>

### [`00a30a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30a50.md) → [`00a30c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30c48.md) _INIT_210

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 60.00% / 新版 58.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30aec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a30a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a30a8c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a30aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a30c78",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a30c84",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a30ca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a30a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30a50.md#insn-00a30a80) · [`00a30aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30a50.md#insn-00a30aa8) · [`00a30aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30a50.md#insn-00a30aec)

~~~diff
- 00a30a80 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a30a80 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a30a80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a30a80 bytes a9831ff8
- 00a30aa8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a30aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a30aa8 bytes e013813c
- 00a30aec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
- 00a30aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a30aec bytes e013853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40a56bdd9389e451d68a180fe57db84b"></a>

### [`00a30de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30de8.md) → [`00a30fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30fe0.md) FUN_00a30fe0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 21件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.29% / 新版 66.29%

CFGの説明率　旧版 44.10% / 新版 43.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 24件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 52件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30e38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a30fdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a30e38",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a30e38",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a30e3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0086a6a4"
      ]
    ]
  ],
  "added": [
    [
      "00a31030",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a31030",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "00a31034",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0086a6a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a30e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30de8.md#insn-00a30e38) · [`00a30e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30de8.md#insn-00a30e6c) · [`00a30e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a30/00a30de8.md#insn-00a30e98)
- 新版 [`00a31090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30fe0.md#insn-00a31090)

~~~diff
- 00a30e38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a8:8"]]
- 00a30e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a30e38 bytes e85700f9
- 00a30e6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:89:8"]]
- 00a30e6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a30e6c bytes e093883c
- 00a30e98 ["INT_ADD", "register:40f0:8", ["const:a30e98:8", "const:4:8"]]
- 00a30e98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00a31090 ["INT_ADD", "register:40f0:8", ["const:a31090:8", "const:4:8"]]
+ 00a31090 ["CALL", null, ["callee:00c57eb0:8"]]
- 00a30e98 bytes 069b0894
+ 00a31090 bytes 889b0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adad30d12e208dc031e2aa1e99290ef3"></a>

### [`00a31924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31924.md) → [`00a31b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md) FUN_00a31b1c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 11件 [`005e0e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0e68.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006269f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/006269f4.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md)
- 新版 呼出元 11件 [`005e0ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0ea8.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00626a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a34.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31924.md#insn-00a31938) · [`00a31948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31924.md#insn-00a31948) · [`00a31964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31924.md#insn-00a31964)
- 新版 [`00a31b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md#insn-00a31b30) · [`00a31b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md#insn-00a31b40) · [`00a31b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md#insn-00a31b5c)

~~~diff
- 00a31938 ["INT_ADD", "register:40f0:8", ["const:a31938:8", "const:4:8"]]
- 00a31938 ["CALL", null, ["callee:00802b58:8"]]
+ 00a31b30 ["INT_ADD", "register:40f0:8", ["const:a31b30:8", "const:4:8"]]
+ 00a31b30 ["CALL", null, ["callee:00802b58:8"]]
- 00a31938 bytes 7844f797
+ 00a31b30 bytes 0a44f797
- 00a31948 ["BRANCH", null, ["local:b8:8"]]
+ 00a31b40 ["BRANCH", null, ["local:b7:8"]]
- 00a31948 bytes 0b000014
+ 00a31b40 bytes 0b000014
- 00a31964 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a31964 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00a31b5c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a31b5c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a31964 bytes 6a000054
+ 00a31b5c bytes 6a000054
~~~


<a id="compare-63f9d754f206e6ad7a022d34f21d76f3"></a>

### [`00a31ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ab8.md) → [`00a31cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md) FUN_00a31cb0

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a31d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31d5c.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a31f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f54.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.12% / 新版 91.12%

CFGの説明率　旧版 58.67% / 新版 59.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31b68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a31b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31da0"
      ]
    ],
    [
      "unmatched:00a31bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31df4"
      ]
    ],
    [
      "unmatched:00a31c3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31e1c"
      ]
    ]
  ],
  "added": [
    [
      "00a31d94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31da0"
      ]
    ],
    [
      "00a31dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31df4"
      ]
    ],
    [
      "00a31e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a31e1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a31b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ab8.md#insn-00a31b64) · [`00a31b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ab8.md#insn-00a31b68) · [`00a31b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ab8.md#insn-00a31b8c)

~~~diff
- 00a31b64 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:68:8"]]
- 00a31b64 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a31b64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a31b64 bytes 1f3400f9
- 00a31b68 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a31b68 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a31b68 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a31b68 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a31b68 bytes 1f7c00a9
- 00a31b8c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:58:8"]]
- 00a31b8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a31b8c bytes 082c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92c5f584e16b39917d0a8faa55934151"></a>

### [`00a31ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ddc.md) → [`00a31fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31fd4.md) _INIT_211

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 74.01% / 新版 74.01%

CFGの説明率　旧版 77.42% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31e0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31e34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31e58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a31e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a31e18",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a31e34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a32004",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a32010",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a3202c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a31e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ddc.md#insn-00a31e0c) · [`00a31e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ddc.md#insn-00a31e34) · [`00a31e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a31/00a31ddc.md#insn-00a31e58)

~~~diff
- 00a31e0c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a31e0c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a31e0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a31e0c bytes a9831ff8
- 00a31e34 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a31e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a31e34 bytes e013813c
- 00a31e58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a31e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a31e58 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc61e0e27b111e947c3e95221a241715"></a>

### [`00a3216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3216c.md) → [`00a32364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32364.md) FUN_00a32364

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3237c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a32180",
      "incomplete_value": true,
      "site": "00a32188",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              [
                "leaf",
                "const:20:8"
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a32184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3216c.md#insn-00a32184) · [`00a32188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a3216c.md#insn-00a32188)
- 新版 [`00a32380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32364.md#insn-00a32380) · [`00a3237c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32364.md#insn-00a3237c)

~~~diff
- 00a32184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00a32184 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00a32184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00a32184 bytes 7f1200b9
- 00a32188 ["INT_ADD", "register:40f0:8", ["const:a32188:8", "const:4:8"]]
- 00a32188 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00a32380 ["INT_ADD", "register:40f0:8", ["const:a32380:8", "const:4:8"]]
+ 00a32380 ["CALL", null, ["callee:005c3e7c:8"]]
- 00a32188 bytes 2d47ee97
+ 00a32380 bytes bf46ee97
+ 00a3237c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
+ 00a3237c ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00a3237c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00a3237c bytes 7f1200b9
~~~


<a id="compare-6a9341a1fca2a923eb2242e69e5370bd"></a>

### [`00a32308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32308.md) → [`00a32500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32500.md) FUN_00a32500

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.68% / 新版 89.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a32540",
      "incomplete_value": false,
      "site": "00a3254c",
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
      "definition_site": "00a32348",
      "incomplete_value": false,
      "site": "00a32354",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a32578",
      "incomplete_value": true,
      "site": "00a32578",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a32380",
      "incomplete_value": true,
      "site": "00a32380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd6:8"
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
      "definition_site": "00a3257c",
      "incomplete_value": true,
      "site": "00a3257c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a32384",
      "incomplete_value": true,
      "site": "00a32384",
      "value": [
        "LOAD",
        "8",
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
      "00a3254c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a32560",
      "READ",
      [
        "storage",
        "002abdd6",
        null,
        "string"
      ]
    ],
    [
      "00a32568",
      "READ",
      [
        "storage",
        "002abddb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a3254c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a32560",
      "READ",
      [
        "storage",
        "002abe16",
        null,
        "string"
      ]
    ],
    [
      "00a32568",
      "READ",
      [
        "storage",
        "002abe1b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3233c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32308.md#insn-00a3233c) · [`00a32348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32308.md#insn-00a32348) · [`00a32358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32308.md#insn-00a32358)
- 新版 [`00a32534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32500.md#insn-00a32534) · [`00a32540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32500.md#insn-00a32540) · [`00a32550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32500.md#insn-00a32550)

~~~diff
- 00a3233c ["INT_ADD", "register:40f0:8", ["const:a3233c:8", "const:4:8"]]
- 00a3233c ["CALL", null, ["callee:00487e20:8"]]
+ 00a32534 ["INT_ADD", "register:40f0:8", ["const:a32534:8", "const:4:8"]]
+ 00a32534 ["CALL", null, ["callee:00487e20:8"]]
- 00a3233c bytes a956e997
+ 00a32534 bytes 3b56e997
- 00a32348 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00a32348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a32348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a32348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a32540 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00a32540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a32540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a32540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a32348 bytes 08e12491
+ 00a32540 bytes 08e13491
- 00a32358 ["INT_ADD", "register:40f0:8", ["const:a32358:8", "const:4:8"]]
- 00a32358 ["CALL", null, ["callee:005c179c:8"]]
+ 00a32550 ["INT_ADD", "register:40f0:8", ["const:a32550:8", "const:4:8"]]
+ 00a32550 ["CALL", null, ["callee:005c179c:8"]]
- 00a32358 bytes 013dee97
+ 00a32550 bytes 933cee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca2900df779061c91671ebe8fad1e8b"></a>

### [`00a325b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a325b8.md) → [`00a327b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a327b0.md) FUN_00a327b0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a8509c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a85/00a8509c.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 1件 [`00a85294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a85/00a85294.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.93% / 新版 89.93%

CFGの説明率　旧版 53.85% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32734"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32744"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a327c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a3283c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008070c4"
      ]
    ],
    [
      "00a329ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a327c8"
      ]
    ],
    [
      "unmatched:00a327c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a329b0"
      ]
    ]
  ],
  "added": [
    [
      "00a3283c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00807104"
      ]
    ],
    [
      "00a329ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a329c0"
      ]
    ],
    [
      "00a329b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a329b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a32644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a325b8.md#insn-00a32644) · [`00a32734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a325b8.md#insn-00a32734) · [`00a32744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a325b8.md#insn-00a32744)
- 新版 [`00a3283c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a327b0.md#insn-00a3283c)

~~~diff
- 00a32644 ["INT_ADD", "register:40f0:8", ["const:a32644:8", "const:4:8"]]
- 00a32644 ["CALL", null, ["ram:8070c4:8"]]
+ 00a3283c ["INT_ADD", "register:40f0:8", ["const:a3283c:8", "const:4:8"]]
+ 00a3283c ["CALL", null, ["ram:807104:8"]]
- 00a32644 bytes a052f797
+ 00a3283c bytes 3252f797
- 00a32734 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a32734 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a32734 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00a32734 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00a32734 bytes 4981899a
- 00a32744 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a32744 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a32744 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a32744 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a32744 bytes 3c31889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba60429928d4576502574bb039b99cf2"></a>

### [`00a32ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32ca0.md) → [`00a32e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md) FUN_00a32e98

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007ef644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef644.md) [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md) [`009d9790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d9790.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 8件 [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md) [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.19% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32ca0.md#insn-00a32cfc) · [`00a32d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32ca0.md#insn-00a32d1c) · [`00a32d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32ca0.md#insn-00a32d38)
- 新版 [`00a32ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md#insn-00a32ef4) · [`00a32f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md#insn-00a32f14) · [`00a32f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e98.md#insn-00a32f30)

~~~diff
- 00a32cfc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a32cfc ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00a32ef4 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a32ef4 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00a32cfc bytes 2a040054
+ 00a32ef4 bytes 2a040054
- 00a32d1c ["BRANCH", null, ["local:b19:8"]]
+ 00a32f14 ["BRANCH", null, ["local:b21:8"]]
- 00a32d1c bytes 1b000014
+ 00a32f14 bytes 1b000014
- 00a32d38 ["INT_ADD", "register:40f0:8", ["const:a32d38:8", "const:4:8"]]
- 00a32d38 ["CALL", null, ["callee:00c57e90:8"]]
+ 00a32f30 ["INT_ADD", "register:40f0:8", ["const:a32f30:8", "const:4:8"]]
+ 00a32f30 ["CALL", null, ["callee:00c57e90:8"]]
- 00a32d38 bytes 56930894
+ 00a32f30 bytes d8930894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95beb5009fe2c3cc89fb7be74bb052b1"></a>

### [`00a32d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32d9c.md) → [`00a32f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32f94.md) FUN_00a32f94

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`007196f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md) [`0080018c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/0080018c.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) [`008001cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001cc.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 47.71% / 新版 46.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32da0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32da0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32da4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a32da0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a32da4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a32fd0",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "00a32f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a32f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a32fd0",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a32da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32d9c.md#insn-00a32da0) · [`00a32da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32d9c.md#insn-00a32da4) · [`00a32e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32d9c.md#insn-00a32e04)
- 新版 [`00a32ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32f94.md#insn-00a32ffc)

~~~diff
- 00a32da0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a32da0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a32da0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a32da0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a32da0 bytes fd7b01a9
- 00a32da4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a32da4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a32da4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a32da4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a32da4 bytes fc6f02a9
- 00a32e04 ["INT_ADD", "register:40f0:8", ["const:a32e04:8", "const:4:8"]]
- 00a32e04 ["CALL", null, ["callee:008514f8:8"]]
+ 00a32ffc ["INT_ADD", "register:40f0:8", ["const:a32ffc:8", "const:4:8"]]
+ 00a32ffc ["CALL", null, ["callee:008514f8:8"]]
- 00a32e04 bytes ad79f897
+ 00a32ffc bytes 3f79f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4834edc99e5c216fcd321769f277039f"></a>

### [`00a33434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md) → [`00a3362c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md) FUN_00a3362c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 9件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 9件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 96.67% / 新版 93.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a33474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a33474) · [`00a33480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a33480) · [`00a3348c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33434.md#insn-00a3348c)
- 新版 [`00a3366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a3366c) · [`00a33678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a33678) · [`00a33684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3362c.md#insn-00a33684)

~~~diff
- 00a33474 ["INT_ADD", "register:40f0:8", ["const:a33474:8", "const:4:8"]]
- 00a33474 ["CALL", null, ["callee:00480be8:8"]]
+ 00a3366c ["INT_ADD", "register:40f0:8", ["const:a3366c:8", "const:4:8"]]
+ 00a3366c ["CALL", null, ["callee:00480be8:8"]]
- 00a33474 bytes cd35e997
+ 00a3366c bytes 5f35e997
- 00a33480 ["INT_ADD", "register:40f0:8", ["const:a33480:8", "const:4:8"]]
- 00a33480 ["CALL", null, ["callee:00481098:8"]]
+ 00a33678 ["INT_ADD", "register:40f0:8", ["const:a33678:8", "const:4:8"]]
+ 00a33678 ["CALL", null, ["callee:00481098:8"]]
- 00a33480 bytes f636e997
+ 00a33678 bytes 8836e997
- 00a3348c ["INT_ADD", "register:40f0:8", ["const:a3348c:8", "const:4:8"]]
- 00a3348c ["CALL", null, ["callee:00480d48:8"]]
+ 00a33684 ["INT_ADD", "register:40f0:8", ["const:a33684:8", "const:4:8"]]
+ 00a33684 ["CALL", null, ["callee:00480d48:8"]]
- 00a3348c bytes 1f36e997
+ 00a33684 bytes b135e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60fe3832620a6976e552e6f615a3c5a5"></a>

### [`00a33614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33614.md) → [`00a3380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a3380c.md) _INIT_212

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 2件, `store_value` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a33848",
      "incomplete_value": true,
      "site": "00a33864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a33650",
      "incomplete_value": true,
      "site": "00a3366c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33698"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a33848",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a3386c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a33690",
      "WRITE",
      [
        "storage",
        "Stack[-0xef]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a33848",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00a3386c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00a33888",
      "WRITE",
      [
        "storage",
        "Stack[-0xef]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a33690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33614.md#insn-00a33690) · [`00a33698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33614.md#insn-00a33698) · [`00a336a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33614.md#insn-00a336a0)

~~~diff
- 00a33690 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a33690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a33690 bytes e013833c
- 00a33698 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a33698 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:61:8"]]
- 00a33698 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a33698 bytes e9130678
- 00a336a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 00a336a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a336a0 bytes e96b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d80a963d58f1dffd0a3b864c6261ab"></a>

### [`00a33d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33d84.md) → [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) FUN_00a33f7c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a3539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md) [`00a35f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md) [`00a36920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36920.md) · 呼出先 4件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00a33ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33ab4.md) [`00a38c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38c60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) [`00a3611c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a3611c.md) [`00a36b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a36b18.md) · 呼出先 4件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00a33cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md) [`00a38e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.23% / 新版 83.23%

CFGの説明率　旧版 72.22% / 新版 70.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33e28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a33ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a34020"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a33e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33d84.md#insn-00a33e28) · [`00a33e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33d84.md#insn-00a33e98) · [`00a33ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33d84.md#insn-00a33ea8)
- 新版 [`00a34090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md#insn-00a34090)

~~~diff
- 00a33e28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00a33e28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a33e28 bytes 895200b9
- 00a33e98 ["INT_ADD", "register:40f0:8", ["const:a33e98:8", "const:4:8"]]
- 00a33e98 ["CALL", null, ["callee:0048793c:8"]]
+ 00a34090 ["INT_ADD", "register:40f0:8", ["const:a34090:8", "const:4:8"]]
+ 00a34090 ["CALL", null, ["callee:0048793c:8"]]
- 00a33e98 bytes 994ee997
+ 00a34090 bytes 2b4ee997
- 00a33ea8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00a33ea8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a33ea8 bytes 895200b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-000d552c518d73292de4155b15e2aa05"></a>

### [`00a34030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34030.md) → [`00a34228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34228.md) FUN_00a34228

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00809998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00809/00809998.md) [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) [`00a34020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34020.md) [`00a36e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md) [`00a389f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a389f4.md) · 呼出先 9件 [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00597a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a0c.md) [`00597a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a24.md) [`00597a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a2c.md)
- 新版 呼出元 5件 [`008099d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md) [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) [`00a34218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34218.md) [`00a37064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37064.md) [`00a38bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38bec.md) · 呼出先 9件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md) [`00597a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a6c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.67% / 新版 75.67%

CFGの説明率　旧版 33.70% / 新版 34.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34044"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a34040",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a34044",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a34048",
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
      "00a34238",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a3423c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a34240",
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

- 旧版 [`00a34040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34030.md#insn-00a34040) · [`00a34044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34030.md#insn-00a34044) · [`00a34048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34030.md#insn-00a34048)

~~~diff
- 00a34040 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a34040 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a34040 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a34040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a34040 bytes fa670ca9
- 00a34044 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a34044 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a34044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a34044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a34044 bytes f85f0da9
- 00a34048 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a34048 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a34048 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00a34048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a34048 bytes f6570ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88c0cb64c22187e1cf0753554fca2741"></a>

### [`00a34558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34558.md) → [`00a34750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34750.md) FUN_00a34750

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) [`009d3284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3284.md) [`009d3794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3794.md) [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 10件 [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00597a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a0c.md) [`00597a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a18.md) [`00597a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a24.md)
- 新版 呼出元 4件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) [`009d3420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3420.md) [`009d3930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3930.md) [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 10件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.60% / 新版 83.60%

CFGの説明率　旧版 38.46% / 新版 39.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a346e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a346ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a346f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3473c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a347f8"
      ]
    ],
    [
      "unmatched:00a348f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a34c50"
      ]
    ],
    [
      "unmatched:00a3492c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a34c24"
      ]
    ]
  ],
  "added": [
    [
      "00a34934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a347f8"
      ]
    ],
    [
      "00a34ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a34c50"
      ]
    ],
    [
      "00a34b24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a34c24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a346e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34558.md#insn-00a346e8) · [`00a346ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34558.md#insn-00a346ec) · [`00a346f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34558.md#insn-00a346f0)

~~~diff
- 00a346e8 ["COPY", "register:100:1", ["const:0:1"]]
- 00a346e8 ["COPY", "register:101:1", ["const:0:1"]]
- 00a346e8 ["COPY", "register:102:1", ["const:1:1"]]
- 00a346e8 ["COPY", "register:103:1", ["const:1:1"]]
- 00a346e8 bytes 0020681e
- 00a346ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a346ec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a346ec ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00a346ec ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00a346ec bytes 29818a9a
- 00a346f0 ["COPY", "register:100:1", ["const:0:1"]]
- 00a346f0 ["COPY", "register:101:1", ["const:0:1"]]
- 00a346f0 ["COPY", "register:102:1", ["const:1:1"]]
- 00a346f0 ["COPY", "register:103:1", ["const:1:1"]]
- 00a346f0 bytes 0020681e
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-863b40f8f3079f77c2285963a752e504"></a>

### [`00a34c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34c1c.md) → [`00a34e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md) FUN_00a34e14

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 10件 [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) [`00597a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a0c.md) [`00597a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a18.md) [`00597a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a24.md)
- 新版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 10件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.99% / 新版 85.99%

CFGの説明率　旧版 36.62% / 新版 35.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `return_value_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a34dc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a34e58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00597778"
      ]
    ],
    [
      "unmatched:00a34eb4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00597a58"
      ]
    ],
    [
      "unmatched:00a35038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a352fc"
      ]
    ]
  ],
  "added": [
    [
      "00a35050",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00597778"
      ]
    ],
    [
      "00a350ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00597a58"
      ]
    ],
    [
      "00a35230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a352fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a34cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34c1c.md#insn-00a34cbc) · [`00a34d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34c1c.md#insn-00a34d18) · [`00a34d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a34/00a34c1c.md#insn-00a34d1c)
- 新版 [`00a34eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a34/00a34e14.md#insn-00a34eb4)

~~~diff
- 00a34cbc ["BRANCH", null, ["local:b4:8"]]
+ 00a34eb4 ["BRANCH", null, ["local:b5:8"]]
- 00a34cbc bytes 09000014
+ 00a34eb4 bytes 09000014
- 00a34d18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 00a34d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00a34d18 bytes 001900b9
- 00a34d1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4:8"]]
- 00a34d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00a34d1c bytes 000500b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375065dfa74ba23cd5c524362f16a100"></a>

### [`00a3539c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md) → [`00a35594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35594.md) FUN_00a35594

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 6件 [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00a33d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33d84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 6件 [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00a33f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33f7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.34% / 新版 87.34%

CFGの説明率　旧版 18.18% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a353a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a353a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a353a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a353a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a353a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a353a8",
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
      "00a35598",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a3559c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a355a0",
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

- 旧版 [`00a353a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md#insn-00a353a0) · [`00a353a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md#insn-00a353a4) · [`00a353a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a3539c.md#insn-00a353a8)

~~~diff
- 00a353a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a353a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a353a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a353a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a353a0 bytes fd7b02a9
- 00a353a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00a353a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00a353a4 bytes f71b00f9
- 00a353a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a353a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a353a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a353a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a353a8 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e9ed444474f82fa275301239b0f0402"></a>

### [`00a35500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md) → [`00a356f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md) FUN_00a356f8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 4件 [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md) [`00727e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md) [`00727f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md)
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 4件 [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md) [`00727e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727e68.md) [`00727fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727fb4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a35518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md#insn-00a35518) · [`00a35520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md#insn-00a35520) · [`00a35524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35500.md#insn-00a35524)
- 新版 [`00a35710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a35710) · [`00a35718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a35718) · [`00a3571c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a356f8.md#insn-00a3571c)

~~~diff
- 00a35518 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a35518 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a35710 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a35710 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a35518 bytes ab050054
+ 00a35710 bytes ab050054
- 00a35520 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a35520 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a35520 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00a35718 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a35718 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00a35718 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00a35520 bytes a8010054
+ 00a35718 bytes a8010054
- 00a35524 ["INT_ADD", "register:40f0:8", ["const:a35524:8", "const:4:8"]]
- 00a35524 ["CALL", null, ["callee:00727d1c:8"]]
+ 00a3571c ["INT_ADD", "register:40f0:8", ["const:a3571c:8", "const:4:8"]]
+ 00a3571c ["CALL", null, ["callee:00727d1c:8"]]
- 00a35524 bytes eec9f397
+ 00a3571c bytes 80c9f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1abbbcea9993fa704a5c66eaacb7388c"></a>

### [`00a355f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a355f8.md) → [`00a357f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a357f0.md) FUN_00a357f0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-75c9cf5f2dfcb50eb050812f26871ce3"></a>

### [`00a35608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35608.md) → [`00a35800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35800.md) FUN_00a35800

採用 · 移動量 `+0x1f8` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-50a01b282a9fe8758f68acff4d4bf96d"></a>

### [`00a35694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35694.md) → [`00a3588c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a3588c.md) FUN_00a3588c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-16dd77a181e58a981ad5d95375a71532"></a>

### [`00a356e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a356e4.md) → [`00a358dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a358dc.md) FUN_00a358dc

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.18% / 新版 90.18%

CFGの説明率　旧版 76.00% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a35910"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a35718",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3571c",
      "READ",
      [
        "storage",
        "01123a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a35a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a35880"
      ]
    ]
  ],
  "added": [
    [
      "00a35910",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a35914",
      "READ",
      [
        "storage",
        "01123e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a35a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a35a78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a35718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a356e4.md#insn-00a35718) · [`00a35768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a356e4.md#insn-00a35768) · [`00a3576c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a356e4.md#insn-00a3576c)

~~~diff
- 00a35718 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a35718 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a35718 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a35718 bytes a9831ff8
- 00a35768 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a35768 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00a35768 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a35768 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00a35768 bytes 1c01899a
- 00a3576c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a3576c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a3576c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a3576c ["INT_ADD", "tmp:1:8", ["register:4058:8", "const:1:8"]]
- 00a3576c bytes 55158b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c0e01b59adf7ec95291f48094acbd35"></a>

### [`00a35c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35c68.md) → [`00a35e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35e60.md) FUN_00a35e60

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.05% / 新版 84.05%

CFGの説明率　旧版 60.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a35c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a35c70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a35c74",
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
      "00a35e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a35e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a35e6c",
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

- 旧版 [`00a35c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35c68.md#insn-00a35c6c) · [`00a35c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35c68.md#insn-00a35c70) · [`00a35c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35c68.md#insn-00a35c74)

~~~diff
- 00a35c6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a35c6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a35c6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a35c6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a35c6c bytes fd7b03a9
- 00a35c70 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a35c70 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a35c70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a35c70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a35c70 bytes fc6f04a9
- 00a35c74 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a35c74 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a35c74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a35c74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a35c74 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0451edb2590a33d2bd6f520e7f0c99d"></a>

### [`00a35f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md) → [`00a3611c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a3611c.md) FUN_00a3611c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.65% / 新版 70.65%

CFGの説明率　旧版 35.88% / 新版 35.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 5件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 18件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35f50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a35f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a35f50",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a35f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a36134",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a36148",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00a36150",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a35f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md#insn-00a35f3c) · [`00a35f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md#insn-00a35f50) · [`00a35f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md#insn-00a35f58)

~~~diff
- 00a35f3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a35f3c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a35f3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a35f3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a35f3c bytes f44f0ca9
- 00a35f50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a35f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a35f50 bytes e80700f9
- 00a35f58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a35f58 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a35f58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a35f58 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9bc0ef232168fa4216283b52df56eff"></a>

### [`00a3689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a3689c.md) → [`00a36a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a36a94.md) FUN_00a36a94

採用 · 移動量 `+0x1f8` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-535feaaa8437d0a8c98d92dfac638767"></a>

### [`00a368cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a368cc.md) → [`00a36ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a36ac4.md) FUN_00a36ac4

採用 · 移動量 `+0x1f8` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009d3958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d3/009d3958.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-625c2e1d5de5909197ffcc8a496e1200"></a>

### [`00a36920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36920.md) → [`00a36b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a36b18.md) FUN_00a36b18

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md)
- 新版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.46% / 新版 62.46%

CFGの説明率　旧版 24.29% / 新版 24.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a36934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a36934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3694c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a36934",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3694c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a369b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487a64"
      ]
    ]
  ],
  "added": [
    [
      "00a36b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a36b44",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00a36ba8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487a64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a36934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36920.md#insn-00a36934) · [`00a3694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36920.md#insn-00a3694c) · [`00a369bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36920.md#insn-00a369bc)

~~~diff
- 00a36934 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a36934 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a36934 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00a36934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a36934 bytes f44f09a9
- 00a3694c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3694c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a3694c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3694c bytes a8831ff8
- 00a369bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00a369bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00a369bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a369bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00a369bc bytes ff430039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b70eca672977a2cb805e2e2f3490cd7"></a>

### [`00a36e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md) → [`00a37064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37064.md) FUN_00a37064

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`00725424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725424.md) [`00735670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md) [`00735b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735b4c.md) [`00739464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md) [`00727e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727e28.md) [`00727f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727f74.md)
- 新版 呼出元 10件 [`0062c0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062c/0062c0c0.md) [`00725464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725464.md) [`007356b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md) [`00735b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735b8c.md) [`007394a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md) [`00727e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727e68.md) [`00727fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727fb4.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.92% / 新版 56.92%

CFGの説明率　旧版 15.82% / 新版 15.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 40件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a36f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a36f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a36f44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a36ec0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a371a4"
      ]
    ],
    [
      "00a370c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a36ebc"
      ]
    ],
    [
      "00a370cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a36eb8"
      ]
    ]
  ],
  "added": [
    [
      "00a370b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a371a4"
      ]
    ],
    [
      "00a370c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a370b4"
      ]
    ],
    [
      "00a370cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a370b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a36f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md#insn-00a36f38) · [`00a36f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md#insn-00a36f44) · [`00a36f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a36/00a36e6c.md#insn-00a36f48)

~~~diff
- 00a36f38 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a36f38 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a36f38 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a36f38 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a36f38 bytes 1ffc02a9
- 00a36f44 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a36f44 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a36f44 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a36f44 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a36f44 bytes 1f7c00a9
- 00a36f48 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00a36f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00a36f48 bytes 170800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46f6b669bbf43b9ce84e3fa16eca35ee"></a>

### [`00a37694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37694.md) → [`00a3788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a3788c.md) FUN_00a3788c

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.98% / 新版 80.98%

CFGの説明率　旧版 44.12% / 新版 42.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3769c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a37698",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3769c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a376a0",
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
      "00a37890",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a37894",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a37898",
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

- 旧版 [`00a37698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37694.md#insn-00a37698) · [`00a3769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37694.md#insn-00a3769c) · [`00a376a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37694.md#insn-00a376a0)

~~~diff
- 00a37698 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a37698 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a37698 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a37698 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a37698 bytes fd7b03a9
- 00a3769c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a3769c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a3769c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a3769c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3769c bytes fc6f04a9
- 00a376a0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a376a0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a376a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a376a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a376a0 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a15fcd3131f4552ee9b22b201d15752"></a>

### [`00a37950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37950.md) → [`00a37b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37b48.md) FUN_00a37b48

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a37c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37c0c.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a37e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37e04.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.09% / 新版 95.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a37dac",
      "incomplete_value": false,
      "site": "00a37db0",
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
      "definition_site": "00a37bb4",
      "incomplete_value": false,
      "site": "00a37bb8",
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a37dc8",
      "incomplete_value": false,
      "site": "00a37dcc",
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
      "definition_site": "00a37bd0",
      "incomplete_value": false,
      "site": "00a37bd4",
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
      "00a37b80",
      "READ",
      [
        "storage",
        "01123a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a37ce4",
      "READ",
      [
        "storage",
        "01123a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a37dac",
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
      "00a37b80",
      "READ",
      [
        "storage",
        "01123e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a37ce4",
      "READ",
      [
        "storage",
        "01123e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00a37dac",
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

- 旧版 [`00a37bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37950.md#insn-00a37bb8) · [`00a37bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37950.md#insn-00a37bd4) · [`00a37988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37950.md#insn-00a37988)
- 新版 [`00a37db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37b48.md#insn-00a37db0) · [`00a37dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37b48.md#insn-00a37dcc) · [`00a37b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37b48.md#insn-00a37b80)

~~~diff
- 00a37bb8 ["INT_ADD", "register:40f0:8", ["const:a37bb8:8", "const:4:8"]]
- 00a37bb8 ["CALL", null, ["callee:00442930:8"]]
+ 00a37db0 ["INT_ADD", "register:40f0:8", ["const:a37db0:8", "const:4:8"]]
+ 00a37db0 ["CALL", null, ["callee:00442930:8"]]
- 00a37bb8 bytes 4e2be897
+ 00a37db0 bytes e02ae897
- 00a37bd4 ["INT_ADD", "register:40f0:8", ["const:a37bd4:8", "const:4:8"]]
- 00a37bd4 ["CALL", null, ["callee:00442930:8"]]
+ 00a37dcc ["INT_ADD", "register:40f0:8", ["const:a37dcc:8", "const:4:8"]]
+ 00a37dcc ["CALL", null, ["callee:00442930:8"]]
- 00a37bd4 bytes 472be897
+ 00a37dcc bytes d92ae897
- 00a37988 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a10:8"]]
- 00a37988 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a37b80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:e10:8"]]
+ 00a37b80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00a37988 bytes c90a45f9
+ 00a37b80 bytes c90a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ce7957c45698ea8e370008622a5f49"></a>

### [`00a37cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37cf0.md) → [`00a37ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ee8.md) FUN_00a37ee8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00732cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732cb8.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00732cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cf8.md) · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a37f70",
      "incomplete_value": false,
      "site": "00a37f74",
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
      "definition_site": "00a37d78",
      "incomplete_value": false,
      "site": "00a37d7c",
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
      "00a37f70",
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
      "00a37f70",
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

- 旧版 [`00a37d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37cf0.md#insn-00a37d7c) · [`00a37d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37cf0.md#insn-00a37d00) · [`00a37d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37cf0.md#insn-00a37d3c)
- 新版 [`00a37f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ee8.md#insn-00a37f74) · [`00a37ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ee8.md#insn-00a37ef8) · [`00a37f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37ee8.md#insn-00a37f34)

~~~diff
- 00a37d7c ["INT_ADD", "register:40f0:8", ["const:a37d7c:8", "const:4:8"]]
- 00a37d7c ["CALL", null, ["callee:00442930:8"]]
+ 00a37f74 ["INT_ADD", "register:40f0:8", ["const:a37f74:8", "const:4:8"]]
+ 00a37f74 ["CALL", null, ["callee:00442930:8"]]
- 00a37d7c bytes dd2ae897
+ 00a37f74 bytes 6f2ae897
- 00a37d00 ["INT_ADD", "register:40f0:8", ["const:a37d00:8", "const:4:8"]]
- 00a37d00 ["CALL", null, ["callee:008514f8:8"]]
+ 00a37ef8 ["INT_ADD", "register:40f0:8", ["const:a37ef8:8", "const:4:8"]]
+ 00a37ef8 ["CALL", null, ["callee:008514f8:8"]]
- 00a37d00 bytes ee65f897
+ 00a37ef8 bytes 8065f897
- 00a37d3c ["INT_ADD", "register:40f0:8", ["const:a37d3c:8", "const:4:8"]]
- 00a37d3c ["CALL", null, ["callee:008514f8:8"]]
+ 00a37f34 ["INT_ADD", "register:40f0:8", ["const:a37f34:8", "const:4:8"]]
+ 00a37f34 ["CALL", null, ["callee:008514f8:8"]]
- 00a37d3c bytes df65f897
+ 00a37f34 bytes 7165f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22c68cc6571c18d936056d43c5030e81"></a>

### [`00a37d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37d90.md) → [`00a37f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37f88.md) FUN_00a37f88

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 1件 [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 1件 [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a37fac",
      "incomplete_value": false,
      "site": "00a37fb4",
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
            "const:21b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a37db4",
      "incomplete_value": false,
      "site": "00a37dbc",
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
            "const:1db:8"
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
      "00a37fac",
      "PARAM",
      [
        "storage",
        "002b31db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a37fac",
      "PARAM",
      [
        "storage",
        "002b321b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a37dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37d90.md#insn-00a37dbc) · [`00a37db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37d90.md#insn-00a37db4)
- 新版 [`00a37fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37f88.md#insn-00a37fb4) · [`00a37fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a37/00a37f88.md#insn-00a37fac)

~~~diff
- 00a37dbc ["INT_ADD", "register:40f0:8", ["const:a37dbc:8", "const:4:8"]]
- 00a37dbc ["CALL", null, ["callee:00c58190:8"]]
+ 00a37fb4 ["INT_ADD", "register:40f0:8", ["const:a37fb4:8", "const:4:8"]]
+ 00a37fb4 ["CALL", null, ["callee:00c58190:8"]]
- 00a37dbc bytes f57f0894
+ 00a37fb4 bytes 77800894
- 00a37db4 ["COPY", "tmp:0:8", ["const:1db:8"]]
- 00a37db4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a37db4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a37db4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a37fac ["COPY", "tmp:0:8", ["const:21b:8"]]
+ 00a37fac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a37fac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a37fac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a37db4 bytes 216c0791
+ 00a37fac bytes 216c0891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-437590040f90a67593faa489a0bb03a3"></a>

### [`00a37e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md) → [`00a38064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md) FUN_00a38064

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a37e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md#insn-00a37e80) · [`00a37ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37e6c.md#insn-00a37ea0)
- 新版 [`00a38078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md#insn-00a38078) · [`00a38098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38064.md#insn-00a38098)

~~~diff
- 00a37e80 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00a37e80 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00a38078 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00a38078 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a37e80 bytes 350200b4
+ 00a38078 bytes 350200b4
- 00a37ea0 ["INT_ADD", "register:40f0:8", ["const:a37ea0:8", "const:4:8"]]
- 00a37ea0 ["CALL", null, ["callee:00869228:8"]]
+ 00a38098 ["INT_ADD", "register:40f0:8", ["const:a38098:8", "const:4:8"]]
+ 00a38098 ["CALL", null, ["callee:00869228:8"]]
- 00a37ea0 bytes d2c4f897
+ 00a38098 bytes 64c4f897
~~~


<a id="compare-bfcbdbdec5cbde31ce8c265d9bdfa3b9"></a>

### [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) → [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) FUN_00a38108

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a898d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a89/00a898d8.md) [`00b11858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) · 呼出先 35件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md) [`0048206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/0048206c.md) [`00482570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482570.md)
- 新版 呼出元 2件 [`00a89ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a89/00a89ad0.md) [`00b11c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md) · 呼出先 35件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md) [`004820ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004820ac.md) [`004825b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 72.22% / 新版 72.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 18件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a37f14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a37f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a37f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a37f18",
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
      "00a38108",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a3810c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a38110",
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

- 旧版 [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md#insn-00a37f10) · [`00a37f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md#insn-00a37f14) · [`00a37f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md#insn-00a37f18)

~~~diff
- 00a37f10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a37f10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a37f10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a37f10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a37f10 bytes fd7bbaa9
- 00a37f14 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a37f14 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a37f14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a37f14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a37f14 bytes fc6f01a9
- 00a37f18 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a37f18 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a37f18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a37f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a37f18 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f64a5b506526c37f026c38af3cdf1f"></a>

### [`00a38acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38acc.md) → [`00a38cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md) FUN_00a38cc4

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a33ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33ab4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00726220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726220.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00a33cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33cac.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00726260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.09% / 新版 91.09%

CFGの説明率　旧版 83.33% / 新版 88.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a38da8",
      "incomplete_value": true,
      "site": "00a38dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:14:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_RIGHT",
              [
                "leaf",
                "const:14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a38bb0",
      "incomplete_value": true,
      "site": "00a38bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:14:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_RIGHT",
              [
                "live",
                "register:4040:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a38bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38acc.md#insn-00a38bb4) · [`00a38b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38acc.md#insn-00a38b28) · [`00a38b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38acc.md#insn-00a38b5c)
- 新版 [`00a38dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38dac) · [`00a38d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38d20) · [`00a38d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md#insn-00a38d54)

~~~diff
- 00a38bb4 ["INT_ADD", "register:40f0:8", ["const:a38bb4:8", "const:4:8"]]
- 00a38bb4 ["CALL", null, ["callee:00c58090:8"]]
+ 00a38dac ["INT_ADD", "register:40f0:8", ["const:a38dac:8", "const:4:8"]]
+ 00a38dac ["CALL", null, ["callee:00c58090:8"]]
- 00a38bb4 bytes 377c0894
+ 00a38dac bytes b97c0894
- 00a38b28 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a38b28 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a38b28 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
+ 00a38d20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a38d20 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00a38d20 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00a38b28 bytes 68090054
+ 00a38d20 bytes 68090054
- 00a38b5c ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00a38b5c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00a38d54 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
+ 00a38d54 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a38b5c bytes 580300b4
+ 00a38d54 bytes 580300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

