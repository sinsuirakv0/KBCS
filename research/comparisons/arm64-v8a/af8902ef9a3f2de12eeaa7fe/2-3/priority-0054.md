# v16.0.0 → v16.0.1 · 最優先の変更候補 (54)

[一覧の目次](README.md)

<a id="compare-9a877a19bcb8dda61e73e7686c4179ed"></a>

### [`00934468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md) → [`00934604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934604.md) FUN_00934604

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

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
      "site": "00934634",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00934498",
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
      "00934634",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00934634",
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

- 旧版 [`00934498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md#insn-00934498) · [`009344a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md#insn-009344a4) · [`009344ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md#insn-009344ac)
- 新版 `00934634`（命令位置の公開資料なし） · `00934640`（命令位置の公開資料なし） · `00934648`（命令位置の公開資料なし）

~~~diff
- 00934498 ["INT_ADD", "register:40f0:8", ["const:934498:8", "const:4:8"]]
- 00934498 ["CALL", null, ["ram:47acb4:8"]]
+ 00934634 ["INT_ADD", "register:40f0:8", ["const:934634:8", "const:4:8"]]
+ 00934634 ["CALL", null, ["ram:47acf4:8"]]
- 00934498 bytes 071aed97
+ 00934634 bytes b019ed97
- 009344a4 ["INT_ADD", "register:40f0:8", ["const:9344a4:8", "const:4:8"]]
- 009344a4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00934640 ["INT_ADD", "register:40f0:8", ["const:934640:8", "const:4:8"]]
+ 00934640 ["CALL", null, ["callee:0047cdd4:8"]]
- 009344a4 bytes 3c22ed97
+ 00934640 bytes e521ed97
- 009344ac ["INT_ADD", "register:40f0:8", ["const:9344ac:8", "const:4:8"]]
- 009344ac ["CALL", null, ["callee:008b9178:8"]]
+ 00934648 ["INT_ADD", "register:40f0:8", ["const:934648:8", "const:4:8"]]
+ 00934648 ["CALL", null, ["callee:008b9178:8"]]
- 009344ac bytes 2213fe97
+ 00934648 bytes cc12fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711e2c9f5a11913359854a17331d4542"></a>

### [`0093455c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093455c.md) → [`009346f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009346f8.md) FUN_009346f8

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
      "definition_site": "00934718",
      "incomplete_value": false,
      "site": "0093471c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0093457c",
      "incomplete_value": false,
      "site": "00934580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "0093471c",
      "DATA",
      [
        "storage",
        "00c875c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0093471c",
      "DATA",
      [
        "storage",
        "00c879c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093455c.md#insn-00934570) · [`0093457c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093455c.md#insn-0093457c)
- 新版 `0093470c`（命令位置の公開資料なし） · `00934718`（命令位置の公開資料なし）

~~~diff
- 00934570 ["INT_ADD", "register:40f0:8", ["const:934570:8", "const:4:8"]]
- 00934570 ["CALL", null, ["callee:00c57e90:8"]]
+ 0093470c ["INT_ADD", "register:40f0:8", ["const:93470c:8", "const:4:8"]]
+ 0093470c ["CALL", null, ["callee:00c57e90:8"]]
- 00934570 bytes 488d0c94
+ 0093470c bytes e18d0c94
- 0093457c ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 0093457c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0093457c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0093457c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00934718 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00934718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00934718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00934718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0093457c bytes 08211791
+ 00934718 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dba038c780f8f7ab5c2a31f6896e82d"></a>

### [`00934594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934594.md) → [`00934730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934730.md) FUN_00934730

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
      "definition_site": "00934734",
      "incomplete_value": false,
      "site": "00934738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934598",
      "incomplete_value": false,
      "site": "0093459c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00934738",
      "DATA",
      [
        "storage",
        "00c875c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934738",
      "DATA",
      [
        "storage",
        "00c879c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934594.md#insn-00934598)
- 新版 `00934734`（命令位置の公開資料なし）

~~~diff
- 00934598 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00934598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00934734 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00934734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00934734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00934734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934598 bytes 08211791
+ 00934734 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc73cb25a5f00c6b81a13f7153355cc5"></a>

### [`009345b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b4.md) → [`00934750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934750.md) FUN_00934750

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b6e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b6eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6eb4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "site": "00934778",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009345dc",
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
      "site": "00934784",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009345e8",
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
      "00934778",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00934784",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00934778",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00934784",
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

- 旧版 [`009345dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b4.md#insn-009345dc) · [`009345e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b4.md#insn-009345e8) · [`0093460c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009345b4.md#insn-0093460c)
- 新版 `00934778`（命令位置の公開資料なし） · `00934784`（命令位置の公開資料なし） · `009347a8`（命令位置の公開資料なし）

~~~diff
- 009345dc ["INT_ADD", "register:40f0:8", ["const:9345dc:8", "const:4:8"]]
- 009345dc ["CALL", null, ["ram:47acb4:8"]]
+ 00934778 ["INT_ADD", "register:40f0:8", ["const:934778:8", "const:4:8"]]
+ 00934778 ["CALL", null, ["ram:47acf4:8"]]
- 009345dc bytes b619ed97
+ 00934778 bytes 5f19ed97
- 009345e8 ["INT_ADD", "register:40f0:8", ["const:9345e8:8", "const:4:8"]]
- 009345e8 ["CALL", null, ["ram:47acb4:8"]]
+ 00934784 ["INT_ADD", "register:40f0:8", ["const:934784:8", "const:4:8"]]
+ 00934784 ["CALL", null, ["ram:47acf4:8"]]
- 009345e8 bytes b319ed97
+ 00934784 bytes 5c19ed97
- 0093460c ["INT_ADD", "register:40f0:8", ["const:93460c:8", "const:4:8"]]
- 0093460c ["CALL", null, ["callee:008514f8:8"]]
+ 009347a8 ["INT_ADD", "register:40f0:8", ["const:9347a8:8", "const:4:8"]]
+ 009347a8 ["CALL", null, ["callee:008514f8:8"]]
- 0093460c bytes ab73fc97
+ 009347a8 bytes 5473fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b52d5c2a293b60de0253ae2f0c1b52c2"></a>

### [`009346cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346cc.md) → [`00934868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934868.md) FUN_00934868

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
      "definition_site": "0093488c",
      "incomplete_value": false,
      "site": "00934890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009346f0",
      "incomplete_value": false,
      "site": "009346f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "00934890",
      "DATA",
      [
        "storage",
        "00c87648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934890",
      "DATA",
      [
        "storage",
        "00c87a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009346e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346cc.md#insn-009346e0) · [`009346f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/009346cc.md#insn-009346f0)
- 新版 `0093487c`（命令位置の公開資料なし） · `0093488c`（命令位置の公開資料なし）

~~~diff
- 009346e0 ["INT_ADD", "register:40f0:8", ["const:9346e0:8", "const:4:8"]]
- 009346e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0093487c ["INT_ADD", "register:40f0:8", ["const:93487c:8", "const:4:8"]]
+ 0093487c ["CALL", null, ["callee:00c57e90:8"]]
- 009346e0 bytes ec8c0c94
+ 0093487c bytes 858d0c94
- 009346f0 ["COPY", "tmp:0:8", ["const:648:8"]]
- 009346f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009346f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009346f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0093488c ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 0093488c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0093488c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0093488c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009346f0 bytes 08211991
+ 0093488c bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08b30c85083582e9996628f03023f6ed"></a>

### [`0093470c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093470c.md) → [`009348a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009348a8.md) FUN_009348a8

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
      "definition_site": "009348ac",
      "incomplete_value": false,
      "site": "009348b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934710",
      "incomplete_value": false,
      "site": "00934714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "009348b0",
      "DATA",
      [
        "storage",
        "00c87648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009348b0",
      "DATA",
      [
        "storage",
        "00c87a48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/0093470c.md#insn-00934710)
- 新版 `009348ac`（命令位置の公開資料なし）

~~~diff
- 00934710 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00934710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009348ac ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 009348ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009348ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009348ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934710 bytes 08211991
+ 009348ac bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2161f32d7e58eb0d5c7289062e4a06f7"></a>

### [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) → [`009348d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009348d0.md) FUN_009348d0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00707568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00934b4c",
      "incomplete_value": false,
      "site": "00934b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009349b0",
      "incomplete_value": false,
      "site": "009349b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009349e0",
      "incomplete_value": true,
      "site": "009349e0",
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
      "definition_site": "00934844",
      "incomplete_value": true,
      "site": "00934844",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00934910",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00934774",
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
      "00934910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0093492c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "009349d0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00934910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0093492c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009349d0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md#insn-00934774) · [`00934790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md#insn-00934790) · [`00934814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md#insn-00934814)
- 新版 `00934910`（命令位置の公開資料なし） · `0093492c`（命令位置の公開資料なし） · `009349b0`（命令位置の公開資料なし）

~~~diff
- 00934774 ["INT_ADD", "register:40f0:8", ["const:934774:8", "const:4:8"]]
- 00934774 ["CALL", null, ["ram:47acb4:8"]]
+ 00934910 ["INT_ADD", "register:40f0:8", ["const:934910:8", "const:4:8"]]
+ 00934910 ["CALL", null, ["ram:47acf4:8"]]
- 00934774 bytes 5019ed97
+ 00934910 bytes f918ed97
- 00934790 ["INT_ADD", "register:40f0:8", ["const:934790:8", "const:4:8"]]
- 00934790 ["CALL", null, ["ram:47acb4:8"]]
+ 0093492c ["INT_ADD", "register:40f0:8", ["const:93492c:8", "const:4:8"]]
+ 0093492c ["CALL", null, ["ram:47acf4:8"]]
- 00934790 bytes 4919ed97
+ 0093492c bytes f218ed97
- 00934814 ["INT_ADD", "register:40f0:8", ["const:934814:8", "const:4:8"]]
- 00934814 ["CALL", null, ["callee:00707568:8"]]
+ 009349b0 ["INT_ADD", "register:40f0:8", ["const:9349b0:8", "const:4:8"]]
+ 009349b0 ["CALL", null, ["callee:00707568:8"]]
- 00934814 bytes 454bf797
+ 009349b0 bytes ee4af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d910c2aac30b17735a2259dfbbe9a6c2"></a>

### [`00934b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b6c.md) → [`00934d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d08.md) FUN_00934d08

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
      "definition_site": "00934d2c",
      "incomplete_value": false,
      "site": "00934d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934b90",
      "incomplete_value": false,
      "site": "00934b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "00934d2c",
      "DATA",
      [
        "storage",
        "00c876b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934d2c",
      "DATA",
      [
        "storage",
        "00c87ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b6c.md#insn-00934b80) · [`00934b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934b6c.md#insn-00934b8c)
- 新版 `00934d1c`（命令位置の公開資料なし） · `00934d28`（命令位置の公開資料なし）

~~~diff
- 00934b80 ["INT_ADD", "register:40f0:8", ["const:934b80:8", "const:4:8"]]
- 00934b80 ["CALL", null, ["callee:00c57e90:8"]]
+ 00934d1c ["INT_ADD", "register:40f0:8", ["const:934d1c:8", "const:4:8"]]
+ 00934d1c ["CALL", null, ["callee:00c57e90:8"]]
- 00934b80 bytes c48b0c94
+ 00934d1c bytes 5d8c0c94
- 00934b8c ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00934b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00934d28 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00934d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00934d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00934d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934b8c bytes 08e11a91
+ 00934d28 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcdfc066213dd6dd466f1cbed68b6ce9"></a>

### [`00934ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ba0.md) → [`00934d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934d3c.md) FUN_00934d3c

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
      "definition_site": "00934d48",
      "incomplete_value": false,
      "site": "00934d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934bac",
      "incomplete_value": false,
      "site": "00934bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "00934d48",
      "DATA",
      [
        "storage",
        "00c876b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934d48",
      "DATA",
      [
        "storage",
        "00c87ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934ba0.md#insn-00934ba8)
- 新版 `00934d44`（命令位置の公開資料なし）

~~~diff
- 00934ba8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00934ba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00934ba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00934ba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00934d44 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00934d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00934d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00934d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00934ba8 bytes 29e11a91
+ 00934d44 bytes 29e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6051058540bedc47e3bf49a6a336d36"></a>

### [`00934cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cdc.md) → [`00934e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e78.md) FUN_00934e78

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
      "definition_site": "00934e8c",
      "incomplete_value": false,
      "site": "00934e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934cf0",
      "incomplete_value": false,
      "site": "00934cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00934e90",
      "DATA",
      [
        "storage",
        "00c87748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934e90",
      "DATA",
      [
        "storage",
        "00c87b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cdc.md#insn-00934ce8) · [`00934cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934cdc.md#insn-00934cf0)
- 新版 `00934e84`（命令位置の公開資料なし） · `00934e8c`（命令位置の公開資料なし）

~~~diff
- 00934ce8 ["INT_ADD", "register:40f0:8", ["const:934ce8:8", "const:4:8"]]
- 00934ce8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00934e84 ["INT_ADD", "register:40f0:8", ["const:934e84:8", "const:4:8"]]
+ 00934e84 ["CALL", null, ["callee:00c57e90:8"]]
- 00934ce8 bytes 6a8b0c94
+ 00934e84 bytes 038c0c94
- 00934cf0 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00934cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00934e8c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00934e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00934e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00934e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934cf0 bytes 08211d91
+ 00934e8c bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31ab665eaad87aee3213e7ce2a6078f"></a>

### [`00934d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d00.md) → [`00934e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934e9c.md) FUN_00934e9c

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
      "definition_site": "00934ea0",
      "incomplete_value": false,
      "site": "00934ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934d04",
      "incomplete_value": false,
      "site": "00934d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00934ea4",
      "DATA",
      [
        "storage",
        "00c87748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00934ea4",
      "DATA",
      [
        "storage",
        "00c87b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d00.md#insn-00934d04)
- 新版 `00934ea0`（命令位置の公開資料なし）

~~~diff
- 00934d04 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00934d04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934d04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934d04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00934ea0 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00934ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00934ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00934ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934d04 bytes 08211d91
+ 00934ea0 bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e8745db2dba0e753d98d018ec87600"></a>

### [`00934d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md) → [`00934eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934eb4.md) FUN_00934eb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0072755c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/0072755c.md) [`00727560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727560.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0072759c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/0072759c.md) [`007275a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007275a0.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00934f84",
      "incomplete_value": true,
      "site": "00934f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934de8",
      "incomplete_value": true,
      "site": "00934dfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a2:8"
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
      "definition_site": "00934f9c",
      "incomplete_value": true,
      "site": "00934f9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00934e00",
      "incomplete_value": true,
      "site": "00934e00",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00934fb0",
      "incomplete_value": false,
      "site": "00934fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934e14",
      "incomplete_value": false,
      "site": "00934e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "00934ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00934f3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00934f84",
      "READ",
      [
        "storage",
        "002a49a2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00934ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00934f3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00934f84",
      "READ",
      [
        "storage",
        "002a4a6f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md#insn-00934d5c) · [`00934da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md#insn-00934da0) · [`00934d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934d18.md#insn-00934d44)
- 新版 `00934ef8`（命令位置の公開資料なし） · `00934f3c`（命令位置の公開資料なし） · `00934ee0`（命令位置の公開資料なし）

~~~diff
- 00934d5c ["INT_ADD", "register:40f0:8", ["const:934d5c:8", "const:4:8"]]
- 00934d5c ["CALL", null, ["ram:47acb4:8"]]
+ 00934ef8 ["INT_ADD", "register:40f0:8", ["const:934ef8:8", "const:4:8"]]
+ 00934ef8 ["CALL", null, ["ram:47acf4:8"]]
- 00934d5c bytes d617ed97
+ 00934ef8 bytes 7f17ed97
- 00934da0 ["INT_ADD", "register:40f0:8", ["const:934da0:8", "const:4:8"]]
- 00934da0 ["CALL", null, ["ram:47acb4:8"]]
+ 00934f3c ["INT_ADD", "register:40f0:8", ["const:934f3c:8", "const:4:8"]]
+ 00934f3c ["CALL", null, ["ram:47acf4:8"]]
- 00934da0 bytes c517ed97
+ 00934f3c bytes 6e17ed97
- 00934d44 ["INT_ADD", "register:40f0:8", ["const:934d44:8", "const:4:8"]]
- 00934d44 ["CALL", null, ["callee:008514f8:8"]]
+ 00934ee0 ["INT_ADD", "register:40f0:8", ["const:934ee0:8", "const:4:8"]]
+ 00934ee0 ["CALL", null, ["callee:008514f8:8"]]
- 00934d44 bytes dd71fc97
+ 00934ee0 bytes 8671fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683c966f1873d66333e0cce19a9c8cd0"></a>

### [`00934fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fe8.md) → [`00935184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935184.md) FUN_00935184

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
      "definition_site": "00935188",
      "incomplete_value": false,
      "site": "0093518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00934fec",
      "incomplete_value": false,
      "site": "00934ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "0093518c",
      "DATA",
      [
        "storage",
        "00c877b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0093518c",
      "DATA",
      [
        "storage",
        "00c87bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00934fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fe8.md#insn-00934fec)
- 新版 `00935188`（命令位置の公開資料なし）

~~~diff
- 00934fec ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00934fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00934fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00934fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00935188 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00935188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00935188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00935188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00934fec bytes 08e11e91
+ 00935188 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fc3286f306094e163444893e46000f"></a>

### [`00935070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935070.md) → [`0093520c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093520c.md) _INIT_184

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 47.50% / 新版 51.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009350a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009350b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009350b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009350a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009350ac",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009350b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0093523c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00935248",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00935250",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009350a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935070.md#insn-009350a0) · [`009350b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935070.md#insn-009350b4) · [`009350b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935070.md#insn-009350b8)

~~~diff
- 009350a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009350a0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009350a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009350a0 bytes a9831ff8
- 009350b4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 009350b4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 009350b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 009350b4 bytes ea130278
- 009350b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 009350b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 009350b8 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2dbcd0e801d14960206160c4922aedf"></a>

### [`00935514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md) → [`009356b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009356b0.md) FUN_009356b0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00935400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935400.md) · 呼出先 10件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00731e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731e84.md) [`00935dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935dac.md) [`00acbb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md) [`00acbd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd1c.md)
- 新版 呼出元 1件 [`0093559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093559c.md) · 呼出先 10件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00731ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ec4.md) [`00935f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935f48.md) [`00acbd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbd4c.md) [`00acbf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbf18.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.22% / 新版 91.22%

CFGの説明率　旧版 58.97% / 新版 69.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093552c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093552c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093553c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0093552c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0093553c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00935544",
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
      "009356c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009356d8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "009356e0",
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

- 旧版 [`0093552c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md#insn-0093552c) · [`0093553c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md#insn-0093553c) · [`00935544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md#insn-00935544)

~~~diff
- 0093552c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0093552c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0093552c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0093552c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0093552c bytes f44f0aa9
- 0093553c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0093553c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0093553c bytes e80700f9
- 00935544 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00935544 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00935544 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00935544 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd129b97e88984b74915f53f650e2f44"></a>

### [`009357b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009357b4.md) → [`00935950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935950.md) FUN_00935950

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00acba88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00935968",
      "incomplete_value": false,
      "site": "00935974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009357cc",
      "incomplete_value": false,
      "site": "009357d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00935974",
      "DATA",
      [
        "storage",
        "00c87848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00935974",
      "DATA",
      [
        "storage",
        "00c87c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009357cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009357b4.md#insn-009357cc) · [`009357fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009357b4.md#insn-009357fc) · [`00935810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009357b4.md#insn-00935810)
- 新版 `00935968`（命令位置の公開資料なし） · `00935998`（命令位置の公開資料なし） · `009359ac`（命令位置の公開資料なし）

~~~diff
- 009357cc ["COPY", "tmp:0:8", ["const:848:8"]]
- 009357cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009357cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009357cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00935968 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00935968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00935968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00935968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009357cc bytes 08212191
+ 00935968 bytes 08213191
- 009357fc ["COPY", "register:0:8", ["register:4040:8"]]
- 009357fc ["INT_ADD", "register:40f0:8", ["const:9357fc:8", "const:4:8"]]
- 009357fc ["CALLIND", null, ["register:0:8"]]
+ 00935998 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00935998 ["INT_ADD", "register:40f0:8", ["const:935998:8", "const:4:8"]]
+ 00935998 ["CALLIND", null, ["register:0:8"]]
- 009357fc bytes 00013fd6
+ 00935998 bytes 00013fd6
- 00935810 ["INT_ADD", "register:40f0:8", ["const:935810:8", "const:4:8"]]
- 00935810 ["CALL", null, ["callee:00c53d00:8"]]
+ 009359ac ["INT_ADD", "register:40f0:8", ["const:9359ac:8", "const:4:8"]]
+ 009359ac ["CALL", null, ["callee:00c53d00:8"]]
- 00935810 bytes 34780c94
+ 009359ac bytes d5780c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe20748915d126a73b7435c8240720d9"></a>

### [`00935924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935924.md) → [`00935ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935ac0.md) FUN_00935ac0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00935ad4",
      "incomplete_value": true,
      "site": "00935adc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00935950"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00935aec"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00935940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935924.md#insn-00935940) · [`00935950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935924.md#insn-00935950)
- 新版 `00935adc`（命令位置の公開資料なし） · `00935aec`（命令位置の公開資料なし）

~~~diff
- 00935940 ["INT_ADD", "register:40f0:8", ["const:935940:8", "const:4:8"]]
- 00935940 ["CALL", null, ["callee:00c53d00:8"]]
+ 00935adc ["INT_ADD", "register:40f0:8", ["const:935adc:8", "const:4:8"]]
+ 00935adc ["CALL", null, ["callee:00c53d00:8"]]
- 00935940 bytes e8770c94
+ 00935adc bytes 89780c94
- 00935950 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00935950 ["RETURN", null, ["register:0:8"]]
- 00935950 bytes c0035fd6
+ 00935aec ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00935aec ["RETURN", null, ["register:0:8"]]
+ 00935aec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b86bf23774ce02b5509826cfbc27171"></a>

### [`00935d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d6c.md) → [`00935f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935f08.md) FUN_00935f08

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00935f0c",
      "incomplete_value": false,
      "site": "00935f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00935d70",
      "incomplete_value": false,
      "site": "00935d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00935f10",
      "DATA",
      [
        "storage",
        "00c87898",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00935f10",
      "DATA",
      [
        "storage",
        "00c87c98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00935d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d6c.md#insn-00935d70)
- 新版 `00935f0c`（命令位置の公開資料なし）

~~~diff
- 00935d70 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00935d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00935d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00935d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00935f0c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00935f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00935f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00935f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00935d70 bytes 08612291
+ 00935f0c bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f26f88a6feb4cf072c6d6965019d2ad8"></a>

### [`00935d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d7c.md) → [`00935f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935f18.md) FUN_00935f18

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00935f28",
      "incomplete_value": false,
      "site": "00935f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00935d8c",
      "incomplete_value": false,
      "site": "00935d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
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
      "00935f30",
      "DATA",
      [
        "storage",
        "00c87898",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00935f30",
      "DATA",
      [
        "storage",
        "00c87c98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00935d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d7c.md#insn-00935d8c) · [`00935d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935d7c.md#insn-00935d98)
- 新版 `00935f28`（命令位置の公開資料なし） · `00935f34`（命令位置の公開資料なし）

~~~diff
- 00935d8c ["COPY", "tmp:0:8", ["const:898:8"]]
- 00935d8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00935d8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00935d8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00935f28 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00935f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00935f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00935f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00935d8c bytes 08612291
+ 00935f28 bytes 08613291
- 00935d98 ["INT_ADD", "register:40f0:8", ["const:935d98:8", "const:4:8"]]
- 00935d98 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00935f34 ["INT_ADD", "register:40f0:8", ["const:935f34:8", "const:4:8"]]
+ 00935f34 ["CALL", null, ["callee:00c57ea0:8"]]
- 00935d98 bytes 42870c94
+ 00935f34 bytes db870c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d62a0527c62e0a5804bb3ee69f6042d"></a>

### [`00935dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935dbc.md) → [`00935f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935f58.md) _INIT_185

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.45% / 新版 60.45%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 35件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00935dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00935e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00935e38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00935dec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00935df8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00935e14",
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
      "00935f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00935f94",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00935fb0",
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

- 旧版 [`00935dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935dbc.md#insn-00935dec) · [`00935e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935dbc.md#insn-00935e14) · [`00935e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935dbc.md#insn-00935e38)

~~~diff
- 00935dec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00935dec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00935dec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00935dec bytes a9831ff8
- 00935e14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00935e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00935e14 bytes e013813c
- 00935e38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00935e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00935e38 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c71ff2e08c2a892513ba0ed2c50e91c"></a>

### [`0093614c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md) → [`009362e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009362e8.md) FUN_009362e8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 63.16% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00936190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009361bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00936264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00936190",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00936190",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00936194",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0046d490"
      ]
    ]
  ],
  "added": [
    [
      "0093632c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0093632c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "00936330",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0046d490"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00936190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md#insn-00936190) · [`009361bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md#insn-009361bc) · [`00936264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/0093614c.md#insn-00936264)

~~~diff
- 00936190 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00936190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00936190 bytes e82300f9
- 009361bc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009361bc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 009361bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009361bc bytes e91302f8
- 00936264 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00936264 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00936264 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00936264 ["INT_ADD", "tmp:3:8", ["register:4000:8", "const:30:8"]]
- 00936264 bytes 087c03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2305a83d9d3ca3106d6188f432084e97"></a>

### [`00936428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md) → [`009365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) FUN_009365c4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 39件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md) [`005ed758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed758.md) [`005efdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005efdcc.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) · 呼出先 5件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md)
- 新版 呼出元 39件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`005e7c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7c98.md) [`005ed798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed798.md) [`005efe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005efe0c.md) [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) · 呼出先 5件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 90.48% / 新版 79.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00936478"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0093647c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00936614"
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
      "0093674c",
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
      "0093674c",
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

- 旧版 [`00936478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md#insn-00936478) · [`0093647c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md#insn-0093647c) · [`009365b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md#insn-009365b4)
- 新版 `00936750`（命令位置の公開資料なし）

~~~diff
- 00936478 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00936478 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00936478 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00936478 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00936478 bytes 7615819a
- 0093647c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0093647c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0093647c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0093647c ["COPY", "register:40d8:8", ["tmp:0:8"]]
- 0093647c bytes 3b018a9a
- 009365b4 ["INT_ADD", "register:40f0:8", ["const:9365b4:8", "const:4:8"]]
- 009365b4 ["CALL", null, ["callee:00442930:8"]]
+ 00936750 ["INT_ADD", "register:40f0:8", ["const:936750:8", "const:4:8"]]
+ 00936750 ["CALL", null, ["callee:00442930:8"]]
- 009365b4 bytes cf30ec97
+ 00936750 bytes 7830ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3659819c0b973bdc30453f9eb3bff0d1"></a>

### [`009365bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/009365bc.md) → [`00936758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/00936758.md) FUN_00936758

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`006788a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md) [`00726780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726780.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 5件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c57e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e50.md)
- 新版 呼出元 6件 [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`006788e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00678/006788e0.md) [`007267c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 5件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.52% / 新版 82.52%

CFGの説明率　旧版 52.00% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009365c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009365c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009365c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009365c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:009365c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:009365c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0093675c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00936760",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00936764",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009365c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/009365bc.md#insn-009365c0) · [`009365c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/009365bc.md#insn-009365c4) · [`009365c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/009365bc.md#insn-009365c8)

~~~diff
- 009365c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009365c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 009365c0 bytes e80b00fd
- 009365c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009365c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009365c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:18:8"]]
- 009365c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009365c4 bytes fdfb01a9
- 009365c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 009365c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 009365c8 bytes fb1700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31318e7fb7560b864d577349d157bf10"></a>

### [`00936758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936758.md) → [`009368f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009368f4.md) _INIT_186

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009367a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009367b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009367bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00936930",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009367a0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "unmatched:009367b0",
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
      "00936930",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0093693c",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "0093694c",
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

- 旧版 [`009367a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936758.md#insn-009367a0) · [`009367b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936758.md#insn-009367b0) · [`009367bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936758.md#insn-009367bc)

~~~diff
- 009367a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 009367a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 009367a0 bytes e92b00b9
- 009367b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 009367b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009367b0 bytes e013813c
- 009367bc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 009367bc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 009367bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 009367bc bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e45cdd2d53becb2f3cf8b2b6f7e0c25"></a>

### [`00936ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936ae8.md) → [`00936c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/00936c84.md) FUN_00936c84

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00936b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936ae8.md#insn-00936b00)
- 新版 `00936c9c`（命令位置の公開資料なし）

~~~diff
- 00936b00 ["INT_ADD", "register:40f0:8", ["const:936b00:8", "const:4:8"]]
- 00936b00 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00936c9c ["INT_ADD", "register:40f0:8", ["const:936c9c:8", "const:4:8"]]
+ 00936c9c ["CALL", null, ["callee:005c3e7c:8"]]
- 00936b00 bytes cf34f297
+ 00936c9c bytes 7834f297
~~~


<a id="compare-2904c3d102f7315f18c53970b3771b7e"></a>

### [`00936b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936b18.md) → [`00936cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/00936cb4.md) FUN_00936cb4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 21件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.01% / 新版 58.01%

CFGの説明率　旧版 31.30% / 新版 31.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 4件, `unresolved_branch_alignment` 31件, `unresolved_call_alignment` 18件, `unresolved_store_alignment` 90件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00936b18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00936b18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00936b1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00936b18",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00936b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00936b68",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00936cb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00936cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00936d04",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00936b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936b18.md#insn-00936b18) · [`00936b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936b18.md#insn-00936b1c) · [`00936b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936b18.md#insn-00936b68)

~~~diff
- 00936b18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00936b18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00936b18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00936b18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00936b18 bytes fd7bbaa9
- 00936b1c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00936b1c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00936b1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00936b1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00936b1c bytes fc6f01a9
- 00936b68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b8:8"]]
- 00936b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00936b68 bytes e85f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1c7a34029638914b1e338679c1c6a0d"></a>

### [`00937804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md) → [`009379a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/009379a0.md) FUN_009379a0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.19% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00937808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md#insn-00937808) · [`0093782c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md#insn-0093782c) · [`0093784c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937804.md#insn-0093784c)
- 新版 `009379a4`（命令位置の公開資料なし） · `009379c8`（命令位置の公開資料なし） · `009379e8`（命令位置の公開資料なし）

~~~diff
- 00937808 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00937808 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 009379a4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009379a4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00937808 bytes e80300b4
+ 009379a4 bytes e80300b4
- 0093782c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 0093782c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 009379c8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 009379c8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 0093782c bytes 890200b4
+ 009379c8 bytes 890200b4
- 0093784c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0093784c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 009379e8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009379e8 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 0093784c bytes 080200b4
+ 009379e8 bytes 080200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3acd730300876d47261524a6b92a3ae7"></a>

### [`00937924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md) → [`00937ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937ac0.md) FUN_00937ac0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0071e92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e92c.md) [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0080b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 6件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0071e96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e96c.md) [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0080b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.77% / 新版 87.77%

CFGの説明率　旧版 69.86% / 新版 72.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937ba4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937bac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009379dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937b9c"
      ]
    ],
    [
      "unmatched:00937a94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937c44"
      ]
    ],
    [
      "00937d00",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00937b94"
      ]
    ]
  ],
  "added": [
    [
      "00937b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937b9c"
      ]
    ],
    [
      "00937c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937c44"
      ]
    ],
    [
      "00937d00",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00937d30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009379dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md#insn-009379dc) · [`00937a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md#insn-00937a08) · [`00937a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937924.md#insn-00937a94)
- 新版 `00937ba4`（命令位置の公開資料なし）

~~~diff
- 009379dc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009379dc ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 009379dc bytes 280100b4
- 00937a08 ["INT_ADD", "register:40f0:8", ["const:937a08:8", "const:4:8"]]
- 00937a08 ["CALL", null, ["callee:00c57e90:8"]]
+ 00937ba4 ["INT_ADD", "register:40f0:8", ["const:937ba4:8", "const:4:8"]]
+ 00937ba4 ["CALL", null, ["callee:00c57e90:8"]]
- 00937a08 bytes 22800c94
+ 00937ba4 bytes bb800c94
- 00937a94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00937a94 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00937a94 bytes a80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef37625865f233a973ce2632daa39513"></a>

### [`00937c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937c14.md) → [`00937db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937db0.md) FUN_00937db0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 53.49% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00937cac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00937e48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00937c8c",
      "incomplete_value": true,
      "site": "00937c94",
      "value": [
        "live",
        "register:40c0:8"
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
      "unmatched:00937cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937e18"
      ]
    ]
  ],
  "added": [
    [
      "00937e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00937e18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00937c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937c14.md#insn-00937c94) · [`00937cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937c14.md#insn-00937cac) · [`00937df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937c14.md#insn-00937df8)
- 新版 `00937e30`（命令位置の公開資料なし） · `00937f94`（命令位置の公開資料なし）

~~~diff
- 00937c94 ["INT_ADD", "register:40f0:8", ["const:937c94:8", "const:4:8"]]
- 00937c94 ["CALL", null, ["callee:004801d8:8"]]
+ 00937e30 ["INT_ADD", "register:40f0:8", ["const:937e30:8", "const:4:8"]]
+ 00937e30 ["CALL", null, ["callee:004801d8:8"]]
- 00937c94 bytes 4121ed97
+ 00937e30 bytes ea20ed97
- 00937cac ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00937cac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00937cac bytes 8bfeff54
- 00937df8 ["INT_ADD", "register:40f0:8", ["const:937df8:8", "const:4:8"]]
- 00937df8 ["CALL", null, ["callee:00c58000:8"]]
+ 00937f94 ["INT_ADD", "register:40f0:8", ["const:937f94:8", "const:4:8"]]
+ 00937f94 ["CALL", null, ["callee:00c58000:8"]]
- 00937df8 bytes 827f0c94
+ 00937f94 bytes 1b800c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7970e56107a008a8c7eb6b7a9328324c"></a>

### [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) → [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) FUN_009380b0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005dc2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2c0.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0080b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080b/0080b000.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005dc300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dc300.md) [`00676a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0080b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080b/0080b040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.46% / 新版 90.46%

CFGの説明率　旧版 60.78% / 新版 59.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00937f28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00937f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00937f28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00937f2c",
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
      "009380c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009380c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009380c8",
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

- 旧版 [`00937f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md#insn-00937f24) · [`00937f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md#insn-00937f28) · [`00937f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md#insn-00937f2c)

~~~diff
- 00937f24 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00937f24 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00937f24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00937f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00937f24 bytes f85f08a9
- 00937f28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00937f28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00937f28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00937f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00937f28 bytes f65709a9
- 00937f2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00937f2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00937f2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00937f2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00937f2c bytes f44f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab530902b1a03f8635303186573f21a9"></a>

### [`009385d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md) → [`00938774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938774.md) FUN_00938774

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00809998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00809/00809998.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`007196f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196f8.md) [`00938364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938364.md)
- 新版 呼出元 3件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`008099d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00809/008099d8.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) [`00938500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.52% / 新版 83.52%

CFGの説明率　旧版 54.09% / 新版 53.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009386ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00938660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009387e4"
      ]
    ],
    [
      "unmatched:00938664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938864"
      ]
    ],
    [
      "unmatched:0093866c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009387f0"
      ]
    ]
  ],
  "added": [
    [
      "009387fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009387e4"
      ]
    ],
    [
      "00938800",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938864"
      ]
    ],
    [
      "00938808",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009387f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00938660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md#insn-00938660) · [`00938664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md#insn-00938664) · [`0093866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md#insn-0093866c)

~~~diff
- 00938660 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00938660 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00938660 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00938660 ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
- 00938660 bytes 4cffff54
- 00938664 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00938664 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00938664 bytes 2a030054
- 0093866c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0093866c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0093866c bytes 48ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd55028ccedbedfb07c33c36b8252b50"></a>

### [`00938b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938b88.md) → [`00938d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938d24.md) _INIT_187

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.97% / 新版 77.97%

CFGの説明率　旧版 50.00% / 新版 54.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938be0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938c04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00938bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00938bc4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00938be0",
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
      "00938d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00938d60",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00938d7c",
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

- 旧版 [`00938bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938b88.md#insn-00938bb8) · [`00938be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938b88.md#insn-00938be0) · [`00938c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938b88.md#insn-00938c04)

~~~diff
- 00938bb8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00938bb8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00938bb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00938bb8 bytes a9831ff8
- 00938be0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00938be0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00938be0 bytes e013813c
- 00938c04 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00938c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00938c04 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe6460c9e2958dcd23ed089e322c3f83"></a>

### [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md) → [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) FUN_009390b4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.06% / 新版 53.06%

CFGの説明率　旧版 32.32% / 新版 32.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 59件, `unresolved_call_alignment` 29件, `unresolved_store_alignment` 113件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00938f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00938f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00938f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00938f20",
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
      "009390b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009390b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009390bc",
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

- 旧版 [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md#insn-00938f18) · [`00938f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md#insn-00938f1c) · [`00938f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md#insn-00938f20)

~~~diff
- 00938f18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00938f18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00938f18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00938f18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00938f18 bytes fd7bbaa9
- 00938f1c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00938f1c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00938f1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00938f1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00938f1c bytes fc6f01a9
- 00938f20 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00938f20 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00938f20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00938f20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00938f20 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b600cdeb9cf91b741b000e0b44bf5b"></a>

### [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) → [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) FUN_0093b770

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 63件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 63件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.30% / 新版 95.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `call_target` 9件, `store_value` 34件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0093b9b0",
      "incomplete_value": true,
      "site": "0093b9c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0093b814",
      "incomplete_value": true,
      "site": "0093b82c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99f:8"
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
      "definition_site": "0093bae4",
      "incomplete_value": true,
      "site": "0093baec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0093b948",
      "incomplete_value": true,
      "site": "0093b950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0093baf0",
      "incomplete_value": true,
      "site": "0093baf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0093b954",
      "incomplete_value": true,
      "site": "0093b95c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0093b994",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0093b9b0",
      "READ",
      [
        "storage",
        "002b799f",
        null,
        "string"
      ]
    ],
    [
      "0093b9c4",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0093b994",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0093b9b0",
      "READ",
      [
        "storage",
        "002b79df",
        null,
        "string"
      ]
    ],
    [
      "0093b9c4",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093b9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md#insn-0093b9a0) · [`0093bb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md#insn-0093bb60) · [`0093bd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md#insn-0093bd24)
- 新版 `0093bb3c`（命令位置の公開資料なし） · `0093bcfc`（命令位置の公開資料なし） · `0093bec0`（命令位置の公開資料なし）

~~~diff
- 0093b9a0 ["INT_ADD", "register:40f0:8", ["const:93b9a0:8", "const:4:8"]]
- 0093b9a0 ["CALL", null, ["callee:0048ce54:8"]]
+ 0093bb3c ["INT_ADD", "register:40f0:8", ["const:93bb3c:8", "const:4:8"]]
+ 0093bb3c ["CALL", null, ["callee:0048ce54:8"]]
- 0093b9a0 bytes 1d45ed97
+ 0093bb3c bytes c644ed97
- 0093bb60 ["INT_ADD", "register:40f0:8", ["const:93bb60:8", "const:4:8"]]
- 0093bb60 ["CALL", null, ["callee:0093ee40:8"]]
+ 0093bcfc ["INT_ADD", "register:40f0:8", ["const:93bcfc:8", "const:4:8"]]
+ 0093bcfc ["CALL", null, ["callee:0093ee40:8"]]
- 0093bb60 bytes 510c0094
+ 0093bcfc bytes 510c0094
- 0093bd24 ["INT_ADD", "register:40f0:8", ["const:93bd24:8", "const:4:8"]]
- 0093bd24 ["CALL", null, ["callee:008b4a8c:8"]]
+ 0093bec0 ["INT_ADD", "register:40f0:8", ["const:93bec0:8", "const:4:8"]]
+ 0093bec0 ["CALL", null, ["callee:008b4a8c:8"]]
- 0093bd24 bytes 49e3fd97
+ 0093bec0 bytes f3e2fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddbda1365aaebaa10eed728fa1685ab6"></a>

### [`0093f214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f214.md) → [`0093f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3b0.md) FUN_0093f3b0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0093f03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f03c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0093f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f1d8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0093f3bc",
      "incomplete_value": false,
      "site": "0093f3c0",
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
      "definition_site": "0093f220",
      "incomplete_value": false,
      "site": "0093f224",
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
      "0093f3bc",
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
      "0093f3bc",
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

- 旧版 [`0093f224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f214.md#insn-0093f224) · [`0093f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f214.md#insn-0093f220)
- 新版 `0093f3c0`（命令位置の公開資料なし） · `0093f3bc`（命令位置の公開資料なし）

~~~diff
- 0093f224 ["INT_ADD", "register:40f0:8", ["const:93f224:8", "const:4:8"]]
- 0093f224 ["CALL", null, ["callee:0043b778:8"]]
+ 0093f3c0 ["INT_ADD", "register:40f0:8", ["const:93f3c0:8", "const:4:8"]]
+ 0093f3c0 ["CALL", null, ["callee:0043b778:8"]]
- 0093f224 bytes 45f1eb97
+ 0093f3c0 bytes eef0eb97
- 0093f220 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0093f220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0093f220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0093f220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0093f3bc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0093f3bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0093f3bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0093f3bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0093f220 bytes 00303c91
+ 0093f3bc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8224cf759f06c3de1db86424ff86f966"></a>

### [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) → [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) FUN_0093f3c4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00938f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938f18.md) [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) [`009426f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md) [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md)
- 新版 呼出元 2件 [`009390b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00939/009390b4.md) [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 51.17% / 新版 51.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_condition` 13件, `unresolved_branch_alignment` 106件, `unresolved_call_alignment` 52件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 70件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093f37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093f428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0093f458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0093f37c",
      "WRITE",
      [
        "storage",
        "Stack[-0x5e8]",
        null,
        null
      ]
    ],
    [
      "unmatched:0093f428",
      "WRITE",
      [
        "storage",
        "Stack[-0x5c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:0093f458",
      "WRITE",
      [
        "storage",
        "Stack[-0x5a0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0093f518",
      "WRITE",
      [
        "storage",
        "Stack[-0x5e8]",
        null,
        null
      ]
    ],
    [
      "0093f5c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x5c8]",
        null,
        null
      ]
    ],
    [
      "0093f5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x5a0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093f348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md#insn-0093f348) · [`0093f37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md#insn-0093f37c) · [`0093f428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md#insn-0093f428)
- 新版 `0093f4e4`（命令位置の公開資料なし）

~~~diff
- 0093f348 ["INT_ADD", "register:40f0:8", ["const:93f348:8", "const:4:8"]]
- 0093f348 ["CALL", null, ["callee:00942f94:8"]]
+ 0093f4e4 ["INT_ADD", "register:40f0:8", ["const:93f4e4:8", "const:4:8"]]
+ 0093f4e4 ["CALL", null, ["callee:00942f94:8"]]
- 0093f348 bytes ac0e0094
+ 0093f4e4 bytes ac0e0094
- 0093f37c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0093f37c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0093f37c bytes fc1700f9
- 0093f428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 0093f428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0093f428 bytes 0081813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014ec52355536020dc3c3645ab8077fb"></a>

### [`009426f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md) → [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) FUN_0094288c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) [`00943fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.51% / 新版 81.51%

CFGの説明率　旧版 35.90% / 新版 36.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0094271c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942720"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0094271c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00942720",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00942724",
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
      "009428b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009428bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "009428c0",
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

- 旧版 [`0094271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md#insn-0094271c) · [`00942720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md#insn-00942720) · [`00942724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md#insn-00942724)

~~~diff
- 0094271c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0094271c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0094271c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0094271c bytes a8831ff8
- 00942720 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00942720 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00942720 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00942720 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00942720 bytes a1833ea9
- 00942724 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00942724 ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00942724 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00942724 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00942724 bytes a38b3da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0b8621674b478b535bede32855b542"></a>

### [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md) → [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) FUN_00942f94

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md) [`00943fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.55% / 新版 71.55%

CFGの説明率　旧版 27.23% / 新版 24.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 48件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942dfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00942df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00942dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00942e00",
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
      "00942f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00942f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00942f9c",
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

- 旧版 [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md#insn-00942df8) · [`00942dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md#insn-00942dfc) · [`00942e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md#insn-00942e00)

~~~diff
- 00942df8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00942df8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00942df8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00942df8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00942df8 bytes fd7bbca9
- 00942dfc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00942dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00942dfc bytes fc0b00f9
- 00942e00 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00942e00 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00942e00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00942e00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00942e00 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3ecdcd8be3b0fb44610e629acd78216"></a>

### [`0094367c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/0094367c.md) → [`00943818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943818.md) FUN_00943818

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00943680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00943680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00943684"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00943680",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00943684",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00943688",
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
      "0094381c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00943820",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00943824",
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

- 旧版 [`00943680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/0094367c.md#insn-00943680) · [`00943684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/0094367c.md#insn-00943684) · [`00943688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/0094367c.md#insn-00943688)

~~~diff
- 00943680 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00943680 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00943680 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00943680 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00943680 bytes fd7b04a9
- 00943684 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00943684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00943684 bytes fb2b00f9
- 00943688 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00943688 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00943688 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00943688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00943688 bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-387bbc1a4a7184211505eeadea61b68d"></a>

### [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md) → [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) FUN_00943998

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) [`009426f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md) [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md) [`00943fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md)
- 新版 呼出元 1件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 80.84% / 新版 88.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009437fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009437fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00943800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009437fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00943800",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00943804",
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
      "00943998",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0094399c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009439a0",
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

- 旧版 [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md#insn-009437fc) · [`00943800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md#insn-00943800) · [`00943804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md#insn-00943804)

~~~diff
- 009437fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009437fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009437fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 009437fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009437fc bytes fd7bbaa9
- 00943800 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00943800 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00943800 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00943800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00943800 bytes fc6f01a9
- 00943804 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00943804 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00943804 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00943804 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00943804 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9f3416f1b10f414705eb46c33bc02a"></a>

### [`00944600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944600.md) → [`0094479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/0094479c.md) FUN_0094479c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009447a8",
      "incomplete_value": false,
      "site": "009447ac",
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
      "definition_site": "0094460c",
      "incomplete_value": false,
      "site": "00944610",
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
      "009447a8",
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
      "009447a8",
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

- 旧版 [`00944610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944600.md#insn-00944610) · [`0094460c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944600.md#insn-0094460c)
- 新版 `009447ac`（命令位置の公開資料なし） · `009447a8`（命令位置の公開資料なし）

~~~diff
- 00944610 ["INT_ADD", "register:40f0:8", ["const:944610:8", "const:4:8"]]
- 00944610 ["CALL", null, ["callee:0043b778:8"]]
+ 009447ac ["INT_ADD", "register:40f0:8", ["const:9447ac:8", "const:4:8"]]
+ 009447ac ["CALL", null, ["callee:0043b778:8"]]
- 00944610 bytes 4adceb97
+ 009447ac bytes f3dbeb97
- 0094460c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0094460c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0094460c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0094460c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009447a8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009447a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009447a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009447a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0094460c bytes 00303c91
+ 009447a8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f707f2ba625341519176545f4629428f"></a>

### [`00944614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md) → [`009447b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009447b0.md) FUN_009447b0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00944614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009447b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009447b0.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 63.12% / 新版 62.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00944bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00944bc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00944d60"
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
      "unmatched:00944744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00944ba4"
      ]
    ],
    [
      "00944908",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0094492c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009448e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00944ba4"
      ]
    ],
    [
      "00944908",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0094492c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00944744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md#insn-00944744) · [`0094476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md#insn-0094476c) · [`00944774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md#insn-00944774)
- 新版 `00944908`（命令位置の公開資料なし） · `00944910`（命令位置の公開資料なし）

~~~diff
- 00944744 ["CBRANCH", null, ["local:b46:8", "register:101:1"]]
- 00944744 bytes 20160054
- 0094476c ["COPY", "tmp:0:8", ["const:f13:8"]]
- 0094476c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094476c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094476c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944908 ["COPY", "tmp:0:8", ["const:f53:8"]]
+ 00944908 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944908 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944908 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094476c bytes 214c3c91
+ 00944908 bytes 214c3d91
- 00944774 ["INT_ADD", "register:40f0:8", ["const:944774:8", "const:4:8"]]
- 00944774 ["CALL", null, ["callee:00441e94:8"]]
+ 00944910 ["INT_ADD", "register:40f0:8", ["const:944910:8", "const:4:8"]]
+ 00944910 ["CALL", null, ["callee:00441e94:8"]]
- 00944774 bytes b8f5eb97
+ 00944910 bytes 61f5eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f021cafe88ee3d63ffcce91bf453f736"></a>

### [`009450d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450d8.md) → [`00945274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945274.md) FUN_00945274

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00945280",
      "incomplete_value": false,
      "site": "00945284",
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
      "definition_site": "009450e4",
      "incomplete_value": false,
      "site": "009450e8",
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
      "00945280",
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
      "00945280",
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

- 旧版 [`009450e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450d8.md#insn-009450e8) · [`009450e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450d8.md#insn-009450e4)
- 新版 `00945284`（命令位置の公開資料なし） · `00945280`（命令位置の公開資料なし）

~~~diff
- 009450e8 ["INT_ADD", "register:40f0:8", ["const:9450e8:8", "const:4:8"]]
- 009450e8 ["CALL", null, ["callee:0043b778:8"]]
+ 00945284 ["INT_ADD", "register:40f0:8", ["const:945284:8", "const:4:8"]]
+ 00945284 ["CALL", null, ["callee:0043b778:8"]]
- 009450e8 bytes 94d9eb97
+ 00945284 bytes 3dd9eb97
- 009450e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 009450e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009450e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009450e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00945280 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00945280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00945280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00945280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009450e4 bytes 00303c91
+ 00945280 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9592316192712f3618a3d69e991f2b6"></a>

### [`00946428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md) → [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) FUN_009465c4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) [`00946780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md) [`00946ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 3件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.25% / 新版 89.25%

CFGの説明率　旧版 15.79% / 新版 12.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009464d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009464d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00946570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0094664c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00946650",
      "WRITE",
      [
        "storage",
        "Stack[-0x72]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009467e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "009467ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x72]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009464d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md#insn-009464d0) · [`009464d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md#insn-009464d4) · [`00946570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md#insn-00946570)

~~~diff
- 009464d0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 009464d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:18:8"]]
- 009464d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009464d0 bytes 0b8001f8
- 009464d4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 009464d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009464d4 bytes 0080803c
- 00946570 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00946570 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:a:8"]]
- 00946570 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00946570 bytes 68a200f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489a8127b12c7e6f352cce5204a6f8b1"></a>

### [`00946780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md) → [`0094691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/0094691c.md) FUN_0094691c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009450ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00945/009450ec.md) · 呼出先 5件 [`009460ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/009460ec.md) [`00946428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946428.md) [`00946ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946ab4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00945288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00945/00945288.md) · 呼出先 5件 [`00946288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946288.md) [`009465c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/009465c4.md) [`00946c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946c50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.22% / 新版 91.22%

CFGの説明率　旧版 56.25% / 新版 73.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009467c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0094686c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00946870"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009467c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:009467cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00946978"
      ]
    ],
    [
      "unmatched:009467e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00946a64"
      ]
    ]
  ],
  "added": [
    [
      "00946960",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00946968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00946978"
      ]
    ],
    [
      "0094697c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00946a64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009467c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md#insn-009467c4) · [`009467cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md#insn-009467cc) · [`009467e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946780.md#insn-009467e0)

~~~diff
- 009467c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009467c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009467c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009467c4 bytes a9831ff8
- 009467cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009467cc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 009467cc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 009467cc ["CBRANCH", null, ["local:b9:8", "tmp:2:1"]]
- 009467cc bytes 8c000054
- 009467e0 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 009467e0 bytes 40070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a44e6594e7717c1b0620ceeb6e2bfe1"></a>

### [`00946d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946d40.md) → [`00946edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00946/00946edc.md) _INIT_188

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00946f18",
      "incomplete_value": true,
      "site": "00946f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00946d7c",
      "incomplete_value": true,
      "site": "00946d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00946f3c",
      "incomplete_value": true,
      "site": "00946f58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00946da0",
      "incomplete_value": true,
      "site": "00946dbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00946f5c",
      "incomplete_value": true,
      "site": "00946f78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00946dc0",
      "incomplete_value": true,
      "site": "00946ddc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00946f18",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00946f3c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00946f5c",
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
      "00946f18",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00946f3c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00946f5c",
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

- 旧版 [`00946dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946d40.md#insn-00946dd8) · [`00946ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946d40.md#insn-00946ea0) · [`00946f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00946/00946d40.md#insn-00946f58)
- 新版 `00946f74`（命令位置の公開資料なし） · `0094703c`（命令位置の公開資料なし） · `009470f4`（命令位置の公開資料なし）

~~~diff
- 00946dd8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00946dd8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00946dd8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00946dd8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00946f74 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00946f74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00946f74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00946f74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00946dd8 bytes 4a553a91
+ 00946f74 bytes 4a893d91
- 00946ea0 ["INT_ADD", "register:40f0:8", ["const:946ea0:8", "const:4:8"]]
- 00946ea0 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0094703c ["INT_ADD", "register:40f0:8", ["const:94703c:8", "const:4:8"]]
+ 0094703c ["CALL", null, ["callee:0043b7f8:8"]]
- 00946ea0 bytes 46d2eb97
+ 0094703c bytes efd1eb97
- 00946f58 ["INT_ADD", "register:40f0:8", ["const:946f58:8", "const:4:8"]]
- 00946f58 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009470f4 ["INT_ADD", "register:40f0:8", ["const:9470f4:8", "const:4:8"]]
+ 009470f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00946f58 bytes d6420c94
+ 009470f4 bytes 6f430c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936b5427e5e2f5f9bdec48cec9106c39"></a>

### [`00961120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961120.md) → [`009612bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009612bc.md) FUN_009612bc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0097800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`009781a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009781a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.97% / 新版 88.97%

CFGの説明率　旧版 60.34% / 新版 66.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00961124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00961124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00961128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00961124",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00961128",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0096112c",
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
      "009612c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009612c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009612c8",
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

- 旧版 [`00961124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961120.md#insn-00961124) · [`00961128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961120.md#insn-00961128) · [`0096112c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961120.md#insn-0096112c)

~~~diff
- 00961124 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00961124 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00961124 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00961124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00961124 bytes fd7b0da9
- 00961128 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00961128 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00961128 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00961128 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00961128 bytes fc6f0ea9
- 0096112c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0096112c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0096112c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 0096112c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0096112c bytes fa670fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59233df7bbf2c79aa90b7f0e9e017df"></a>

### [`0096145c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/0096145c.md) → [`009615f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009615f8.md) FUN_009615f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 50.00% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00961474",
      "incomplete_value": true,
      "site": "00961480",
      "value": [
        "live",
        "register:4008:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00961660",
      "incomplete_value": true,
      "site": "00961664",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "old": {
      "definition_site": "009614c4",
      "incomplete_value": true,
      "site": "009614c8",
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
            "const:1:8"
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
    "new": null,
    "old": {
      "definition_site": "0096152c",
      "incomplete_value": true,
      "site": "00961530",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00961480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/0096145c.md#insn-00961480) · [`009614c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/0096145c.md#insn-009614c8) · [`00961530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/0096145c.md#insn-00961530)
- 新版 `0096161c`（命令位置の公開資料なし） · `00961664`（命令位置の公開資料なし） · `009616cc`（命令位置の公開資料なし）

~~~diff
- 00961480 ["INT_ADD", "register:40f0:8", ["const:961480:8", "const:4:8"]]
- 00961480 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0096161c ["INT_ADD", "register:40f0:8", ["const:96161c:8", "const:4:8"]]
+ 0096161c ["CALL", null, ["callee:00c57fe0:8"]]
- 00961480 bytes d8d90b94
+ 0096161c bytes 71da0b94
- 009614c8 ["INT_ADD", "register:40f0:8", ["const:9614c8:8", "const:4:8"]]
- 009614c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00961664 ["INT_ADD", "register:40f0:8", ["const:961664:8", "const:4:8"]]
+ 00961664 ["CALL", null, ["callee:00c57e90:8"]]
- 009614c8 bytes 72d90b94
+ 00961664 bytes 0bda0b94
- 00961530 ["INT_ADD", "register:40f0:8", ["const:961530:8", "const:4:8"]]
- 00961530 ["CALL", null, ["callee:0043b764:8"]]
+ 009616cc ["INT_ADD", "register:40f0:8", ["const:9616cc:8", "const:4:8"]]
+ 009616cc ["CALL", null, ["callee:0043b764:8"]]
- 00961530 bytes 7d68eb97
+ 009616cc bytes 2668eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4a8444c01a30f898fbcfd573170572"></a>

### [`00961598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961598.md) → [`00961734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/00961734.md) FUN_00961734

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 1件 [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md)
- 新版 呼出元 3件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 1件 [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009615f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961598.md#insn-009615f0)
- 新版 `0096178c`（命令位置の公開資料なし）

~~~diff
- 009615f0 ["INT_ADD", "register:40f0:8", ["const:9615f0:8", "const:4:8"]]
- 009615f0 ["CALL", null, ["callee:005e8198:8"]]
+ 0096178c ["INT_ADD", "register:40f0:8", ["const:96178c:8", "const:4:8"]]
+ 0096178c ["CALL", null, ["callee:005e8198:8"]]
- 009615f0 bytes da1af297
+ 0096178c bytes 831af297
~~~


<a id="compare-973863728f558e4b18e06c8aac500969"></a>

### [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) → [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) FUN_009617a0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 25件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005cc960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md) [`00604e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e14.md) [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005cc9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc9a0.md) [`00604e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604e54.md) [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.84% / 新版 77.84%

CFGの説明率　旧版 15.71% / 新版 15.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `store_condition` 3件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 17件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00961640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00961df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0096211c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00961640",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00961980",
      "DATA",
      [
        "storage",
        "00333fc8",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:00961984",
      "DATA",
      [
        "storage",
        "00335f64",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "009617dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00961b1c",
      "DATA",
      [
        "storage",
        "00333fc8",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00961b20",
      "DATA",
      [
        "storage",
        "00335f64",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00961640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md#insn-00961640) · [`00961df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md#insn-00961df8)
- 新版 `009617dc`（命令位置の公開資料なし）

~~~diff
- 00961640 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00961640 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00961640 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00961640 bytes a8831ff8
+ 009617dc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009617dc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 009617dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009617dc bytes a8831ff8
- 00961df8 ["INT_LEFT", "tmp:0:8", ["register:4048:8", "const:0:1"]]
- 00961df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00961df8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00961df8 bytes 0069a93c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a623e7c0b9100febc24261d3d6bab71"></a>

### [`00962d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md) → [`00962f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00962/00962f1c.md) FUN_00962f1c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`005cc960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc960.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md) [`0071b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b930.md) [`0082eaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eaec.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005cc9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc9a0.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md) [`0071b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071b970.md) [`0082eb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eb2c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.93% / 新版 80.93%

CFGの説明率　旧版 35.44% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00962d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00962d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00962d84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00962d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00962d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00962d88",
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
      "00962f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00962f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00962f24",
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

- 旧版 [`00962d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md#insn-00962d80) · [`00962d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md#insn-00962d84) · [`00962d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md#insn-00962d88)

~~~diff
- 00962d80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00962d80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00962d80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00962d80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00962d80 bytes fd7bbba9
- 00962d84 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00962d84 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00962d84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00962d84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00962d84 bytes fa6701a9
- 00962d88 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00962d88 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00962d88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00962d88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00962d88 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfceda10c863f95f4cfae708d29f7be2"></a>

### [`00963d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963d90.md) → [`00963f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963f2c.md) FUN_00963f2c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 90.91% / 新版 86.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00963da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963d90.md#insn-00963da4) · [`00963dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963d90.md#insn-00963dac) · [`00963db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963d90.md#insn-00963db4)
- 新版 `00963f40`（命令位置の公開資料なし） · `00963f48`（命令位置の公開資料なし） · `00963f50`（命令位置の公開資料なし）

~~~diff
- 00963da4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00963da4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00963da4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00963da4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00963f40 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00963f40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00963f40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00963f40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00963da4 bytes c8010037
+ 00963f40 bytes c8010037
- 00963dac ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00963dac ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00963dac ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00963dac ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00963f48 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00963f48 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00963f48 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00963f48 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00963dac bytes 08020037
+ 00963f48 bytes 08020037
- 00963db4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00963db4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00963db4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00963db4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00963f50 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00963f50 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00963f50 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00963f50 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00963db4 bytes 48020037
+ 00963f50 bytes 48020037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5afc446d17955d77e89a931cd9af65df"></a>

### [`0097800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md) → [`009781a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009781a8.md) FUN_009781a8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00961120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961120.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0097834c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009612bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009612bc.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`009784e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009784e8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 62.26% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978050"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009781ec"
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
      "unmatched:00978050",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00978118",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009781ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009782b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00978050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md#insn-00978050) · [`009780d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md#insn-009780d8) · [`00978118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md#insn-00978118)
- 新版 `00978274`（命令位置の公開資料なし）

~~~diff
- 00978050 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00978050 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00978050 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00978050 bytes a9831ff8
- 009780d8 ["INT_ADD", "register:40f0:8", ["const:9780d8:8", "const:4:8"]]
- 009780d8 ["CALL", null, ["callee:0043bb20:8"]]
+ 00978274 ["INT_ADD", "register:40f0:8", ["const:978274:8", "const:4:8"]]
+ 00978274 ["CALL", null, ["callee:0043bb20:8"]]
- 009780d8 bytes 820eeb97
+ 00978274 bytes 2b0eeb97
- 00978118 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00978118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00978118 bytes e013803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a31683a01443858795cdb1daf61ec8a"></a>

### [`0097834c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md) → [`009784e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009784e8.md) FUN_009784e8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0097800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097800c.md) [`0097834c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`009781a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009781a8.md) [`009784e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009784e8.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.49% / 新版 78.49%

CFGの説明率　旧版 19.95% / 新版 19.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 51件, `store_condition` 2件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097836c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00978378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097836c",
      "WRITE",
      [
        "storage",
        "Stack[-0x3b8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00978374",
      "WRITE",
      [
        "storage",
        "Stack[-0x38c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00978378",
      "WRITE",
      [
        "storage",
        "Stack[-0x388]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00978508",
      "WRITE",
      [
        "storage",
        "Stack[-0x3b8]",
        null,
        null
      ]
    ],
    [
      "00978510",
      "WRITE",
      [
        "storage",
        "Stack[-0x38c]",
        null,
        null
      ]
    ],
    [
      "00978514",
      "WRITE",
      [
        "storage",
        "Stack[-0x388]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097836c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md#insn-0097836c) · [`00978374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md#insn-00978374) · [`00978378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md#insn-00978378)

~~~diff
- 0097836c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 0097836c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 0097836c bytes e71f00f9
- 00978374 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:64:8"]]
- 00978374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4030:4"]]
- 00978374 bytes e66700b9
- 00978378 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00978378 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00978378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:68:8"]]
- 00978378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00978378 bytes e39706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cd459139cac60dc6cfeda8190d8490a"></a>

### [`00979548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md) → [`009796e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00979/009796e4.md) FUN_009796e4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0097834c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00978/0097834c.md) [`00979548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`009784e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00978/009784e8.md) [`009796e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00979/009796e4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.97% / 新版 86.97%

CFGの説明率　旧版 43.61% / 新版 43.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 38件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00979558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00979558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097955c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00979558",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097955c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00979568",
      "WRITE",
      [
        "storage",
        "Stack[-0x310]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009796f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009796f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00979704",
      "WRITE",
      [
        "storage",
        "Stack[-0x310]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00979558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md#insn-00979558) · [`0097955c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md#insn-0097955c) · [`00979568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md#insn-00979568)

~~~diff
- 00979558 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00979558 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00979558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00979558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00979558 bytes f65704a9
- 0097955c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097955c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097955c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0097955c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097955c bytes f44f05a9
- 00979568 ["COPY", "tmp:0:4", ["register:4028:4"]]
- 00979568 ["COPY", "tmp:1:4", ["register:4038:4"]]
- 00979568 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00979568 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:4"]]
- 00979568 bytes e51f0a29
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1fc04169ba5dc3ae2eb95a77a0674d"></a>

### [`0097a55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md) → [`0097a6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097a/0097a6f8.md) FUN_0097a6f8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00979548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00979/00979548.md) [`0097a55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`009796e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00979/009796e4.md) [`0097a6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097a/0097a6f8.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.75% / 新版 77.75%

CFGの説明率　旧版 31.09% / 新版 29.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 64件, `store_condition` 4件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097a570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097a56c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097a570",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097a57c",
      "WRITE",
      [
        "storage",
        "Stack[-0x300]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097a708",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0097a70c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0097a718",
      "WRITE",
      [
        "storage",
        "Stack[-0x300]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097a56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md#insn-0097a56c) · [`0097a570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md#insn-0097a570) · [`0097a57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md#insn-0097a57c)

~~~diff
- 0097a56c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0097a56c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0097a56c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0097a56c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097a56c bytes f65704a9
- 0097a570 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097a570 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097a570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0097a570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097a570 bytes f44f05a9
- 0097a57c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0097a57c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 0097a57c bytes e70b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a7a19d75b440ead3050dfd727e8886"></a>

### [`0097b4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md) → [`0097b694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097b/0097b694.md) FUN_0097b694

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0097a55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097a/0097a55c.md) [`0097b4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0097a6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097a/0097a6f8.md) [`0097b694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097b/0097b694.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.00% / 新版 78.00%

CFGの説明率　旧版 42.12% / 新版 43.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_condition` 1件, `unresolved_branch_alignment` 23件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097b4f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097b4f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097b4fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097b4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097b4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097b500",
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
      "0097b694",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0097b698",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0097b69c",
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

- 旧版 [`0097b4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md#insn-0097b4f8) · [`0097b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md#insn-0097b4fc) · [`0097b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md#insn-0097b500)

~~~diff
- 0097b4f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097b4f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097b4f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 0097b4f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0097b4f8 bytes fd7bbaa9
- 0097b4fc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0097b4fc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0097b4fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097b4fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097b4fc bytes fc6f01a9
- 0097b500 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0097b500 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0097b500 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0097b500 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097b500 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd05ddb35e338a474e849d2b3efb9c74"></a>

### [`0097c30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md) → [`0097c4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097c/0097c4a8.md) FUN_0097c4a8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0097b4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097b/0097b4f8.md) [`0097c30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0097b694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097b/0097b694.md) [`0097c4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097c/0097c4a8.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.23% / 新版 88.23%

CFGの説明率　旧版 43.53% / 新版 43.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 35件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c564"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097c6b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097c3f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c5a8"
      ]
    ],
    [
      "unmatched:0097c418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c608"
      ]
    ],
    [
      "0097c594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c8bc"
      ]
    ]
  ],
  "added": [
    [
      "0097c594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c5a8"
      ]
    ],
    [
      "0097c5b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c608"
      ]
    ],
    [
      "0097c5d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097c8bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md#insn-0097c3c8) · [`0097c3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md#insn-0097c3f8) · [`0097c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md#insn-0097c418)
- 新版 `0097c564`（命令位置の公開資料なし）

~~~diff
- 0097c3c8 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
+ 0097c564 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 0097c3c8 bytes e00b0054
+ 0097c564 bytes e00b0054
- 0097c3f8 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 0097c3f8 bytes a0000054
- 0097c418 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0097c418 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 0097c418 bytes a3020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7382b3bb26fcbc83758b79e8ac97a655"></a>

### [`0097d024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d024.md) → [`0097d1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d1c0.md) FUN_0097d1c0

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
      "definition_site": "0097d1d4",
      "incomplete_value": false,
      "site": "0097d1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d038",
      "incomplete_value": false,
      "site": "0097d03c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0097d1d8",
      "DATA",
      [
        "storage",
        "00c878e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097d1d8",
      "DATA",
      [
        "storage",
        "00c87ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d024.md#insn-0097d030) · [`0097d038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d024.md#insn-0097d038)
- 新版 `0097d1cc`（命令位置の公開資料なし） · `0097d1d4`（命令位置の公開資料なし）

~~~diff
- 0097d030 ["INT_ADD", "register:40f0:8", ["const:97d030:8", "const:4:8"]]
- 0097d030 ["CALL", null, ["callee:00c57e90:8"]]
+ 0097d1cc ["INT_ADD", "register:40f0:8", ["const:97d1cc:8", "const:4:8"]]
+ 0097d1cc ["CALL", null, ["callee:00c57e90:8"]]
- 0097d030 bytes 986a0b94
+ 0097d1cc bytes 316b0b94
- 0097d038 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 0097d038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097d038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097d038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097d1d4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0097d1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097d038 bytes 08a12391
+ 0097d1d4 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8da8fb5c73c9958876ca28dd4ddd5af9"></a>

### [`0097d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d060.md) → [`0097d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d1fc.md) FUN_0097d1fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "0097d220",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0097d084",
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
      "0097d220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0097d220",
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

- 旧版 [`0097d084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d060.md#insn-0097d084) · [`0097d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d060.md#insn-0097d090)
- 新版 `0097d220`（命令位置の公開資料なし） · `0097d22c`（命令位置の公開資料なし）

~~~diff
- 0097d084 ["INT_ADD", "register:40f0:8", ["const:97d084:8", "const:4:8"]]
- 0097d084 ["CALL", null, ["ram:47acb4:8"]]
+ 0097d220 ["INT_ADD", "register:40f0:8", ["const:97d220:8", "const:4:8"]]
+ 0097d220 ["CALL", null, ["ram:47acf4:8"]]
- 0097d084 bytes 0cf7eb97
+ 0097d220 bytes b5f6eb97
- 0097d090 ["INT_ADD", "register:40f0:8", ["const:97d090:8", "const:4:8"]]
- 0097d090 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0097d22c ["INT_ADD", "register:40f0:8", ["const:97d22c:8", "const:4:8"]]
+ 0097d22c ["CALL", null, ["callee:0047cdd4:8"]]
- 0097d090 bytes 41ffeb97
+ 0097d22c bytes eafeeb97
~~~


<a id="compare-e696ef7270c009bd36c3f55aae808f1e"></a>

### [`0097d12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d12c.md) → [`0097d2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d2c8.md) FUN_0097d2c8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00684f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684f70.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 44.74% / 新版 43.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d1cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d1d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d1d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097d160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d344"
      ]
    ],
    [
      "unmatched:0097d168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d344"
      ]
    ],
    [
      "0097d30c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0097d2fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d344"
      ]
    ],
    [
      "0097d304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d344"
      ]
    ],
    [
      "0097d30c",
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

- 旧版 [`0097d160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d12c.md#insn-0097d160) · [`0097d168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d12c.md#insn-0097d168) · [`0097d170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d12c.md#insn-0097d170)
- 新版 `0097d30c`（命令位置の公開資料なし）

~~~diff
- 0097d160 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097d160 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0097d160 bytes 41020054
- 0097d168 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0097d168 bytes 00020054
- 0097d170 ["INT_ADD", "register:40f0:8", ["const:97d170:8", "const:4:8"]]
- 0097d170 ["CALL", null, ["ram:47acb4:8"]]
+ 0097d30c ["INT_ADD", "register:40f0:8", ["const:97d30c:8", "const:4:8"]]
+ 0097d30c ["CALL", null, ["ram:47acf4:8"]]
- 0097d170 bytes d1f6eb97
+ 0097d30c bytes 7af6eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1695952939d7196eb57bc42df3b1916e"></a>

### [`0097d40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d40c.md) → [`0097d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d5a8.md) FUN_0097d5a8

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
      "definition_site": "0097d5cc",
      "incomplete_value": false,
      "site": "0097d5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d430",
      "incomplete_value": false,
      "site": "0097d430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0097d5cc",
      "DATA",
      [
        "storage",
        "00c879d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097d5cc",
      "DATA",
      [
        "storage",
        "00c87dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d40c.md#insn-0097d420) · [`0097d42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d40c.md#insn-0097d42c)
- 新版 `0097d5bc`（命令位置の公開資料なし） · `0097d5c8`（命令位置の公開資料なし）

~~~diff
- 0097d420 ["INT_ADD", "register:40f0:8", ["const:97d420:8", "const:4:8"]]
- 0097d420 ["CALL", null, ["callee:00c57e90:8"]]
+ 0097d5bc ["INT_ADD", "register:40f0:8", ["const:97d5bc:8", "const:4:8"]]
+ 0097d5bc ["CALL", null, ["callee:00c57e90:8"]]
- 0097d420 bytes 9c690b94
+ 0097d5bc bytes 356a0b94
- 0097d42c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0097d42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097d42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097d42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097d5c8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0097d5c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d5c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d5c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097d42c bytes 08612791
+ 0097d5c8 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f6adc6661ddb4ecf96bc487ac15ac6a"></a>

### [`0097d440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d440.md) → [`0097d5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d5dc.md) FUN_0097d5dc

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
      "definition_site": "0097d5e8",
      "incomplete_value": false,
      "site": "0097d5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d44c",
      "incomplete_value": false,
      "site": "0097d44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0097d5e8",
      "DATA",
      [
        "storage",
        "00c879d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097d5e8",
      "DATA",
      [
        "storage",
        "00c87dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d440.md#insn-0097d448)
- 新版 `0097d5e4`（命令位置の公開資料なし）

~~~diff
- 0097d448 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0097d448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097d448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097d448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097d5e4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0097d5e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097d5e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097d5e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097d448 bytes 29612791
+ 0097d5e4 bytes 29613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96fecf9ef880395bc09ec46c5ef79393"></a>

### [`0097d45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md) → [`0097d5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d5f8.md) FUN_0097d5f8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00689940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689940.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00689980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689980.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 56.82% / 新版 59.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d484"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d518"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d5a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097d484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d65c"
      ]
    ],
    [
      "unmatched:0097d494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0097d688",
      "DATA",
      [
        "storage",
        "0039b22c",
        null,
        "byte[27]"
      ]
    ]
  ],
  "added": [
    [
      "0097d620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097d65c"
      ]
    ],
    [
      "0097d630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0097d688",
      "DATA",
      [
        "storage",
        "0039b22c",
        "fde_0039b22c",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md#insn-0097d484) · [`0097d494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md#insn-0097d494) · [`0097d518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md#insn-0097d518)

~~~diff
- 0097d484 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097d484 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0097d484 bytes e1010054
- 0097d494 ["INT_ADD", "register:40f0:8", ["const:97d494:8", "const:4:8"]]
- 0097d494 ["CALL", null, ["ram:47acb4:8"]]
- 0097d494 bytes 08f6eb97
- 0097d518 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0097d518 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 0097d518 bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d64e733aca6fa5b6922c9ebd8c640ab2"></a>

### [`0097d6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6a8.md) → [`0097d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d844.md) FUN_0097d844

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
      "definition_site": "0097d858",
      "incomplete_value": false,
      "site": "0097d85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d6bc",
      "incomplete_value": false,
      "site": "0097d6c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "0097d85c",
      "DATA",
      [
        "storage",
        "00c87a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097d85c",
      "DATA",
      [
        "storage",
        "00c87e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6a8.md#insn-0097d6b4) · [`0097d6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6a8.md#insn-0097d6bc)
- 新版 `0097d850`（命令位置の公開資料なし） · `0097d858`（命令位置の公開資料なし）

~~~diff
- 0097d6b4 ["INT_ADD", "register:40f0:8", ["const:97d6b4:8", "const:4:8"]]
- 0097d6b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0097d850 ["INT_ADD", "register:40f0:8", ["const:97d850:8", "const:4:8"]]
+ 0097d850 ["CALL", null, ["callee:00c57e90:8"]]
- 0097d6b4 bytes f7680b94
+ 0097d850 bytes 90690b94
- 0097d6bc ["COPY", "tmp:0:8", ["const:a68:8"]]
- 0097d6bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097d6bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097d6bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097d858 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0097d858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097d858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097d6bc bytes 08a12991
+ 0097d858 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41aba569ea5e0ff53803f50102a2497c"></a>

### [`0097d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6e4.md) → [`0097d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d880.md) FUN_0097d880

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 66.67% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0097d8a8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0097d70c",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d7ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "0097d948"
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
      "0097d8a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0097d8a8",
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

- 旧版 [`0097d70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6e4.md#insn-0097d70c) · [`0097d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d6e4.md#insn-0097d7ac)
- 新版 `0097d8a8`（命令位置の公開資料なし） · `0097d948`（命令位置の公開資料なし）

~~~diff
- 0097d70c ["INT_ADD", "register:40f0:8", ["const:97d70c:8", "const:4:8"]]
- 0097d70c ["CALL", null, ["ram:47acb4:8"]]
+ 0097d8a8 ["INT_ADD", "register:40f0:8", ["const:97d8a8:8", "const:4:8"]]
+ 0097d8a8 ["CALL", null, ["ram:47acf4:8"]]
- 0097d70c bytes 6af5eb97
+ 0097d8a8 bytes 13f5eb97
- 0097d7ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 0097d7ac ["RETURN", null, ["register:0:8"]]
- 0097d7ac bytes c0035fd6
+ 0097d948 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0097d948 ["RETURN", null, ["register:0:8"]]
+ 0097d948 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42209e005df04cf2f9a964179864b9f0"></a>

### [`0097deec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097deec.md) → [`0097e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e088.md) FUN_0097e088

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
      "definition_site": "0097e09c",
      "incomplete_value": false,
      "site": "0097e0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097df00",
      "incomplete_value": false,
      "site": "0097df04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "0097e0a0",
      "DATA",
      [
        "storage",
        "00c87b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097e0a0",
      "DATA",
      [
        "storage",
        "00c87f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097deec.md#insn-0097def8) · [`0097df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097deec.md#insn-0097df00)
- 新版 `0097e094`（命令位置の公開資料なし） · `0097e09c`（命令位置の公開資料なし）

~~~diff
- 0097def8 ["INT_ADD", "register:40f0:8", ["const:97def8:8", "const:4:8"]]
- 0097def8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0097e094 ["INT_ADD", "register:40f0:8", ["const:97e094:8", "const:4:8"]]
+ 0097e094 ["CALL", null, ["callee:00c57e90:8"]]
- 0097def8 bytes e6660b94
+ 0097e094 bytes 7f670b94
- 0097df00 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 0097df00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097df00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097df00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e09c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0097e09c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e09c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e09c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097df00 bytes 08a12d91
+ 0097e09c bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ca0717d02d0096d14d8edc0dcb03f7"></a>

### [`0097df28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097df28.md) → [`0097e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e0c4.md) FUN_0097e0c4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.53% / 新版 81.53%

CFGの説明率　旧版 56.52% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e330"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e43c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0097e4cc"
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
      "unmatched:0097e0b4",
      "DATA",
      [
        "storage",
        "00339ade",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:0097e0b8",
      "DATA",
      [
        "storage",
        "00339ae1",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:0097e0bc",
      "DATA",
      [
        "storage",
        "00339ae0",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "0097e250",
      "DATA",
      [
        "storage",
        "00339ade",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0097e254",
      "DATA",
      [
        "storage",
        "00339ae1",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0097e258",
      "DATA",
      [
        "storage",
        "00339ae0",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097df28.md#insn-0097e0a8) · [`0097e244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097df28.md#insn-0097e244) · [`0097e24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097df28.md#insn-0097e24c)
- 新版 `0097e244`（命令位置の公開資料なし）

~~~diff
- 0097e0a8 ["INT_ADD", "register:40f0:8", ["const:97e0a8:8", "const:4:8"]]
- 0097e0a8 ["CALL", null, ["callee:008514f8:8"]]
+ 0097e244 ["INT_ADD", "register:40f0:8", ["const:97e244:8", "const:4:8"]]
+ 0097e244 ["CALL", null, ["callee:008514f8:8"]]
- 0097e0a8 bytes 044dfb97
+ 0097e244 bytes ad4cfb97
- 0097e244 ["INT_ADD", "register:40f0:8", ["const:97e244:8", "const:4:8"]]
- 0097e244 ["CALL", null, ["callee:008514f8:8"]]
- 0097e244 bytes 9d4cfb97
- 0097e24c ["INT_ADD", "register:40f0:8", ["const:97e24c:8", "const:4:8"]]
- 0097e24c ["CALL", null, ["callee:008514f8:8"]]
- 0097e24c bytes 9b4cfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cff952b8f45c194858fc86e98703e45f"></a>

### [`0097e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e4d0.md) → [`0097e66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e66c.md) _INIT_189

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.49% / 新版 69.49%

CFGの説明率　旧版 28.21% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e500"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e518"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097e500",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097e50c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0097e514",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097e69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0097e6a8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0097e6b0",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e4d0.md#insn-0097e500) · [`0097e514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e4d0.md#insn-0097e514) · [`0097e518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e4d0.md#insn-0097e518)

~~~diff
- 0097e500 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0097e500 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0097e500 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0097e500 bytes a9831ff8
- 0097e514 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0097e514 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0097e514 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0097e514 bytes ea130278
- 0097e518 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0097e518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0097e518 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0051654564612a6bc2cff254ad5add66"></a>

### [`0097e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e860.md) → [`0097e9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e9fc.md) FUN_0097e9fc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0059777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059777c.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`0097f19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f19c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005977bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005977bc.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`0097f338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f338.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.67% / 新版 82.67%

CFGの説明率　旧版 31.84% / 新版 30.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `store_value` 3件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097e8b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097eb40",
      "incomplete_value": true,
      "site": "0097eb40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e9a4",
      "incomplete_value": true,
      "site": "0097e9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e2d:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097eaac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097e8b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097e8cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097ebf0"
      ]
    ],
    [
      "0097eb30",
      "READ",
      [
        "storage",
        "002bce2d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097ea4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ],
    [
      "0097ea68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097ebf0"
      ]
    ],
    [
      "0097eb30",
      "READ",
      [
        "storage",
        "002bce6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e860.md#insn-0097e8b0) · [`0097e8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e860.md#insn-0097e8cc) · [`0097e914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e860.md#insn-0097e914)
- 新版 `0097eab0`（命令位置の公開資料なし）

~~~diff
- 0097e8b0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0097e8b0 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "const:1:8"]]
- 0097e8b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0097e8b0 bytes 28130078
- 0097e8cc ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 0097e8cc bytes 400c0054
- 0097e914 ["INT_ADD", "register:40f0:8", ["const:97e914:8", "const:4:8"]]
- 0097e914 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0097eab0 ["INT_ADD", "register:40f0:8", ["const:97eab0:8", "const:4:8"]]
+ 0097eab0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0097e914 bytes 67640b94
+ 0097eab0 bytes 00650b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a19718299b0e43fcf3ef08601120a5"></a>

### [`0097f19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f19c.md) → [`0097f338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f338.md) FUN_0097f338

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097e860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097e/0097e860.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0097e9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097e/0097e9fc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 56.04% / 新版 56.04%

CFGの説明率　旧版 8.62% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f1cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f1f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097f1cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f3c8"
      ]
    ],
    [
      "unmatched:0097f38c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f680"
      ]
    ],
    [
      "unmatched:0097f3a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0097f41c"
      ]
    ]
  ],
  "added": [
    [
      "0097f368",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f3c8"
      ]
    ],
    [
      "0097f528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f680"
      ]
    ],
    [
      "0097f544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f5b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f19c.md#insn-0097f1cc) · [`0097f1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f19c.md#insn-0097f1f0) · [`0097f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f19c.md#insn-0097f244)

~~~diff
- 0097f1cc ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 0097f1cc bytes 00030054
- 0097f1f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097f1f0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0097f1f0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0097f1f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 0097f1f0 bytes 2915819a
- 0097f244 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0097f244 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0097f244 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0097f244 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 0097f244 bytes 0815819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e0bb1c854e1e43b39e89c81cc871dea"></a>

### [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) → [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) FUN_0097f894

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) · 呼出先 11件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044b804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b804.md) [`0044b9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b9d8.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md)
- 新版 呼出元 1件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) · 呼出先 11件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md) [`0044ba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00561fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561fd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 31.82% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f700"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097f6fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f700",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f714",
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
      "0097f898",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0097f89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0097f8b0",
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

- 旧版 [`0097f6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md#insn-0097f6fc) · [`0097f700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md#insn-0097f700) · [`0097f714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md#insn-0097f714)

~~~diff
- 0097f6fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097f6fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097f6fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0097f6fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f6fc bytes fd7b08a9
- 0097f700 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097f700 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097f700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0097f700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f700 bytes f44f09a9
- 0097f714 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0097f714 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0097f714 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0097f714 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-420c8959006145cec00469d9f2c85806"></a>

### [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) → [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) FUN_0097fb20

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009816dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md) [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 26件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md)
- 新版 呼出元 2件 [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 26件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 20.72% / 新版 21.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `store_condition` 25件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f9b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f9f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097f9b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f9d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f9dc",
      "READ",
      [
        "storage",
        "002b627d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097fb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "0097fb74",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "0097fb78",
      "READ",
      [
        "storage",
        "002b62bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md#insn-0097f9b8) · [`0097f9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md#insn-0097f9d8) · [`0097f9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md#insn-0097f9f0)

~~~diff
- 0097f9b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0097f9b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 0097f9b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0097f9b8 bytes a8831df8
- 0097f9d8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0097f9d8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:a0:8"]]
- 0097f9d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0097f9d8 bytes e8830239
- 0097f9f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0097f9f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
- 0097f9f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0097f9f0 bytes a81200f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1f9dd894b1a52ba02c69a2b8746651"></a>

### [`0098059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/0098059c.md) → [`00980738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980738.md) FUN_00980738

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009805b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/0098059c.md#insn-009805b0) · [`009805d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/0098059c.md#insn-009805d4) · [`009805dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/0098059c.md#insn-009805dc)
- 新版 `0098074c`（命令位置の公開資料なし） · `00980770`（命令位置の公開資料なし） · `00980778`（命令位置の公開資料なし）

~~~diff
- 009805b0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 009805b0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 009805b0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 009805b0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 0098074c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 0098074c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0098074c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0098074c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 009805b0 bytes 08010037
+ 0098074c bytes 08010037
- 009805d4 ["INT_ADD", "register:40f0:8", ["const:9805d4:8", "const:4:8"]]
- 009805d4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00980770 ["INT_ADD", "register:40f0:8", ["const:980770:8", "const:4:8"]]
+ 00980770 ["CALL", null, ["callee:00c57eb0:8"]]
- 009805d4 bytes 375d0b94
+ 00980770 bytes d05d0b94
- 009805dc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 009805dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 009805dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 009805dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00980778 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00980778 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00980778 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00980778 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 009805dc bytes 08ff0736
+ 00980778 bytes 08ff0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a14db322af7e377d53204922fbc31e"></a>

### [`00980600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980600.md) → [`0098079c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/0098079c.md) FUN_0098079c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 27.27% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980600",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980604",
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
      "0098079c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009807a0",
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

- 旧版 [`00980600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980600.md#insn-00980600) · [`00980604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980600.md#insn-00980604) · [`0098061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980600.md#insn-0098061c)
- 新版 `009807b8`（命令位置の公開資料なし）

~~~diff
- 00980600 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980600 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980600 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00980600 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00980600 bytes fd7bbea9
- 00980604 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00980604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00980604 bytes f30b00f9
- 0098061c ["INT_ADD", "register:40f0:8", ["const:98061c:8", "const:4:8"]]
- 0098061c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009807b8 ["INT_ADD", "register:40f0:8", ["const:9807b8:8", "const:4:8"]]
+ 009807b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0098061c bytes 255d0b94
+ 009807b8 bytes be5d0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4631820c3a961bac32eba442b5030371"></a>

### [`00980664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980664.md) → [`00980800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980800.md) FUN_00980800

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00980688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980664.md#insn-00980688) · [`0098069c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980664.md#insn-0098069c) · [`009806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980664.md#insn-009806ac)
- 新版 `00980824`（命令位置の公開資料なし） · `00980838`（命令位置の公開資料なし） · `00980848`（命令位置の公開資料なし）

~~~diff
- 00980688 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00980824 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00980688 bytes 60010054
+ 00980824 bytes 60010054
- 0098069c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00980838 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 0098069c bytes c0000054
+ 00980838 bytes c0000054
- 009806ac ["INT_ADD", "register:40f0:8", ["const:9806ac:8", "const:4:8"]]
- 009806ac ["CALL", null, ["callee:00c57eb0:8"]]
+ 00980848 ["INT_ADD", "register:40f0:8", ["const:980848:8", "const:4:8"]]
+ 00980848 ["CALL", null, ["callee:00c57eb0:8"]]
- 009806ac bytes 015d0b94
+ 00980848 bytes 9a5d0b94
~~~


<a id="compare-8a5787fce15a3bb0f8729b6a2edfb095"></a>

### [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) → [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) FUN_00980868

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`00980664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980664.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc0c.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md)
- 新版 呼出元 2件 [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) [`00980800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980800.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md) [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 48.31% / 新版 48.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009806f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980928"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009806f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:009806fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "unmatched:0098079c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00980914"
      ]
    ]
  ],
  "added": [
    [
      "00980894",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00980898",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00980938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00980914"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009806f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md#insn-009806f8) · [`0098075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md#insn-0098075c) · [`00980760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md#insn-00980760)

~~~diff
- 009806f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009806f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 009806f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009806f8 bytes a8831ef8
- 0098075c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0098075c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0098075c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0098075c ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 0098075c bytes 55038b9a
- 00980760 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00980760 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00980760 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00980760 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00980760 bytes 38018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3f027904bd7f358c3f5a0a177aa3b6"></a>

### [`00980c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md) → [`00980e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980e10.md) FUN_00980e10

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) · 呼出先 4件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00981584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md) [`00982030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) · 呼出先 4件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00981720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md) [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.79% / 新版 64.79%

CFGの説明率　旧版 12.50% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980c7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980c78",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980c80",
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
      "00980e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00980e18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00980e1c",
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

- 旧版 [`00980c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md#insn-00980c78) · [`00980c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md#insn-00980c7c) · [`00980c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md#insn-00980c80)

~~~diff
- 00980c78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00980c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 00980c78 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 00980c78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 00980c78 bytes e923026d
- 00980c7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00980c7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00980c7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00980c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980c7c bytes fd7b03a9
- 00980c80 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00980c80 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00980c80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00980c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00980c80 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb01948aa461987352f18d0fc1db0f44"></a>

### [`00981194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981194.md) → [`00981330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981330.md) FUN_00981330

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 68.97% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0098141c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981264",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098140c"
      ]
    ]
  ],
  "added": [
    [
      "00981400",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098140c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981194.md#insn-00981264) · [`00981274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981194.md#insn-00981274) · [`00981280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981194.md#insn-00981280)
- 新版 `00981410`（命令位置の公開資料なし）

~~~diff
- 00981264 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00981264 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00981264 bytes 680000b4
- 00981274 ["INT_ADD", "register:40f0:8", ["const:981274:8", "const:4:8"]]
- 00981274 ["CALL", null, ["callee:0043bba4:8"]]
+ 00981410 ["INT_ADD", "register:40f0:8", ["const:981410:8", "const:4:8"]]
+ 00981410 ["CALL", null, ["callee:0043bba4:8"]]
- 00981274 bytes 3ceaea97
+ 00981410 bytes e5e9ea97
- 00981280 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:50:8"]]
- 00981280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981280 bytes e82a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd4a767fff3c9eed7f65c35762d26d71"></a>

### [`009812a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md) → [`00981440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981440.md) FUN_00981440

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 7件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md) [`0048078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048078c.md) [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`00982030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 7件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) [`004807cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004807cc.md) [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981384"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00981520"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00981320",
      "incomplete_value": true,
      "site": "00981324",
      "value": [
        "live",
        "register:4098:8"
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
      "009814f0",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "unmatched:00981384",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00981578"
      ]
    ]
  ],
  "added": [
    [
      "009814f0",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "00981520",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00981578"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md#insn-00981324) · [`00981370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md#insn-00981370) · [`00981384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009812a4.md#insn-00981384)
- 新版 `009814c0`（命令位置の公開資料なし） · `0098150c`（命令位置の公開資料なし）

~~~diff
- 00981324 ["INT_ADD", "register:40f0:8", ["const:981324:8", "const:4:8"]]
- 00981324 ["CALL", null, ["callee:004807cc:8"]]
+ 009814c0 ["INT_ADD", "register:40f0:8", ["const:9814c0:8", "const:4:8"]]
+ 009814c0 ["CALL", null, ["callee:004807cc:8"]]
- 00981324 bytes 1afdeb97
+ 009814c0 bytes c3fceb97
- 00981370 ["INT_ADD", "register:40f0:8", ["const:981370:8", "const:4:8"]]
- 00981370 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0098150c ["INT_ADD", "register:40f0:8", ["const:98150c:8", "const:4:8"]]
+ 0098150c ["CALL", null, ["callee:00c57eb0:8"]]
- 00981370 bytes d0590b94
+ 0098150c bytes 695a0b94
- 00981384 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00981384 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00981384 bytes c1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91b8ac2b33ba5c043fd2c188dcbed76f"></a>

### [`009813e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009813e0.md) → [`0098157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098157c.md) FUN_0098157c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md) [`004810e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004810e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md) [`00481128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481128.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.19% / 新版 82.19%

CFGの説明率　旧版 30.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009813e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009813e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009813e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009813e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009813e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009813ec",
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
      "00981580",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00981584",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00981588",
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

- 旧版 [`009813e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009813e0.md#insn-009813e4) · [`009813e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009813e0.md#insn-009813e8) · [`009813ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009813e0.md#insn-009813ec)

~~~diff
- 009813e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009813e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009813e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 009813e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009813e4 bytes fd7b03a9
- 009813e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 009813e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 009813e8 bytes f72300f9
- 009813ec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009813ec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009813ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 009813ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009813ec bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf77167d57db3d54ae000ab69ee7306"></a>

### [`00981530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md) → [`009816cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009816cc.md) FUN_009816cc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 2件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`0086a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a470.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 2件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`0086a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a4b0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098155c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981560"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098154c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0086a460"
      ]
    ]
  ],
  "added": [
    [
      "009816e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0086a460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098154c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md#insn-0098154c) · [`00981550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md#insn-00981550) · [`0098155c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981530.md#insn-0098155c)

~~~diff
- 0098154c ["INT_ADD", "register:40f0:8", ["const:98154c:8", "const:4:8"]]
- 0098154c ["CALL", null, ["callee:0086a460:8"]]
- 0098154c bytes b5a3fb97
- 00981550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:60:8"]]
- 00981550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00981550 bytes 743200f9
- 0098155c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0098155c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0098155c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0098155c bytes 9f0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ae3963e92da561e3c4f13ffc68b9e87"></a>

### [`00981584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md) → [`00981720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md) FUN_00981720

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0097f5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f5e0.md) [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) [`00980c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980c74.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`0097f77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md) [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) [`00980e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980e10.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.46% / 新版 58.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981588"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981584",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981588",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098158c",
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
      "00981720",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00981724",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00981728",
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

- 旧版 [`00981584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md#insn-00981584) · [`00981588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md#insn-00981588) · [`0098158c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md#insn-0098158c)

~~~diff
- 00981584 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981584 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981584 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00981584 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981584 bytes fd7bbba9
- 00981588 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00981588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00981588 bytes f90b00f9
- 0098158c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0098158c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0098158c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0098158c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098158c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98e40ad142d82faf01b5066d0128f10b"></a>

### [`009816c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816c0.md) → [`0098185c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098185c.md) FUN_0098185c

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
      "definition_site": "00981868",
      "incomplete_value": false,
      "site": "00981868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009816cc",
      "incomplete_value": false,
      "site": "009816cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c87000:8"
          ],
          [
            "leaf",
            "const:c00:8"
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
      "00981868",
      "DATA",
      [
        "storage",
        "00c87c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981868",
      "DATA",
      [
        "storage",
        "00c88000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009816c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816c0.md#insn-009816c4) · [`009816c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816c0.md#insn-009816c8)
- 新版 `00981860`（命令位置の公開資料なし） · `00981864`（命令位置の公開資料なし）

~~~diff
- 009816c4 ["COPY", "register:4048:8", ["const:c87000:8"]]
+ 00981860 ["COPY", "register:4048:8", ["const:c88000:8"]]
- 009816c4 bytes 291800d0
+ 00981860 bytes 291800f0
- 009816c8 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 009816c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009816c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009816c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981864 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00981864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009816c8 bytes 29013091
+ 00981864 bytes 29010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-674c78c8467079804dd6a762c1642844"></a>

### [`009816dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md) → [`00981878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981878.md) FUN_00981878

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) [`004823bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md) [`004824f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004824f8.md) [`00482570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482570.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) [`004823fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md) [`00482538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md) [`004825b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004825b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.82% / 新版 77.82%

CFGの説明率　旧版 20.95% / 新版 19.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009816e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009816e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009816e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009816e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009816e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009816fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0098187c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00981880",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00981898",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009816e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md#insn-009816e0) · [`009816e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md#insn-009816e4) · [`009816fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009816dc.md#insn-009816fc)

~~~diff
- 009816e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009816e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009816e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 009816e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009816e0 bytes fd7b11a9
- 009816e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:120:8"]]
- 009816e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 009816e4 bytes fc9300f9
- 009816fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009816fc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009816fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009816fc bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c152194d8fa03be3d20d695c71732a74"></a>

### [`00981c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md) → [`00981dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981dbc.md) FUN_00981dbc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00981e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981e24.md) [`0098201c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098201c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00981fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md) [`009821b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 74.36% / 新版 74.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981c28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981c2c",
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
      "00981dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00981dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00981dc8",
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

- 旧版 [`00981c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md#insn-00981c24) · [`00981c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md#insn-00981c28) · [`00981c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md#insn-00981c2c)

~~~diff
- 00981c24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981c24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981c24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00981c24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981c24 bytes fd7b03a9
- 00981c28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00981c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00981c28 bytes f72300f9
- 00981c2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00981c2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00981c2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00981c2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981c2c bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff7338ca44097ddb1e4cd6cae9330d45"></a>

### [`0098201c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098201c.md) → [`009821b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821b8.md) FUN_009821b8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00981c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00981dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981dbc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "009821c4",
      "incomplete_value": false,
      "site": "009821c8",
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
      "definition_site": "00982028",
      "incomplete_value": false,
      "site": "0098202c",
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
      "009821c4",
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
      "009821c4",
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

- 旧版 [`0098202c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098201c.md#insn-0098202c) · [`00982028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098201c.md#insn-00982028)
- 新版 `009821c8`（命令位置の公開資料なし） · `009821c4`（命令位置の公開資料なし）

~~~diff
- 0098202c ["INT_ADD", "register:40f0:8", ["const:98202c:8", "const:4:8"]]
- 0098202c ["CALL", null, ["callee:0043b778:8"]]
+ 009821c8 ["INT_ADD", "register:40f0:8", ["const:9821c8:8", "const:4:8"]]
+ 009821c8 ["CALL", null, ["callee:0043b778:8"]]
- 0098202c bytes c3e5ea97
+ 009821c8 bytes 6ce5ea97
- 00982028 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00982028 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00982028 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00982028 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009821c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 009821c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009821c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009821c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00982028 bytes 00303c91
+ 009821c4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dc7fa631c91d8c2d6dfa309bc741269"></a>

### [`009822b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md) → [`00982450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md) FUN_00982450

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) · 呼出先 5件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md) [`00982544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982544.md) [`009826a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009826a4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 1件 [`0097fb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097fb20.md) · 呼出先 5件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md) [`009826e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md) [`00982840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982840.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 37.93% / 新版 38.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982308"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00982334",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982500"
      ]
    ],
    [
      "unmatched:0098233c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982520"
      ]
    ],
    [
      "unmatched:00982348",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00982340"
      ]
    ]
  ],
  "added": [
    [
      "009824d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982500"
      ]
    ],
    [
      "009824d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982520"
      ]
    ],
    [
      "009824e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009824dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md#insn-00982300) · [`00982304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md#insn-00982304) · [`00982308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md#insn-00982308)

~~~diff
- 00982300 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00982300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00982300 bytes 880200f9
- 00982304 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 00982304 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00982304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00982304 bytes 3f0900f9
- 00982308 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00982308 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00982308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00982308 bytes 1f0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72970bd95fc647e80fa5963d3b7748a5"></a>

### [`00982544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982544.md) → [`009826e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009826e0.md) FUN_009826e0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009822b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00982450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.30% / 新版 80.30%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00982544",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00982548",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098254c",
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
      "009826e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009826e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009826e8",
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

- 旧版 [`00982544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982544.md#insn-00982544) · [`00982548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982544.md#insn-00982548) · [`0098254c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982544.md#insn-0098254c)

~~~diff
- 00982544 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00982544 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00982544 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00982544 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00982544 bytes fd7bbca9
- 00982548 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00982548 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00982548 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00982548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00982548 bytes f85f01a9
- 0098254c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0098254c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0098254c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0098254c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098254c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da90523887c87bfa168899ca2d9b885d"></a>

### [`009826a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009826a4.md) → [`00982840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982840.md) FUN_00982840

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009822b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009822b4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00982450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982450.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.11% / 新版 85.11%

CFGの説明率　旧版 33.33% / 新版 32.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009826fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00982898"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098274c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009828e0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00982750"
      ]
    ],
    [
      "unmatched:0098274c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982948"
      ]
    ],
    [
      "unmatched:009827a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00982750"
      ]
    ]
  ],
  "added": [
    [
      "009828e0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009828ec"
      ]
    ],
    [
      "009828e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00982948"
      ]
    ],
    [
      "00982940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009828ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009826fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009826a4.md#insn-009826fc) · [`00982710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009826a4.md#insn-00982710) · [`0098274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/009826a4.md#insn-0098274c)
- 新版 `009828ac`（命令位置の公開資料なし）

~~~diff
- 009826fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
- 009826fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009826fc bytes 8002823c
- 00982710 ["INT_ADD", "register:40f0:8", ["const:982710:8", "const:4:8"]]
- 00982710 ["CALL", null, ["callee:0043bb20:8"]]
+ 009828ac ["INT_ADD", "register:40f0:8", ["const:9828ac:8", "const:4:8"]]
+ 009828ac ["CALL", null, ["callee:0043bb20:8"]]
- 00982710 bytes f4e4ea97
+ 009828ac bytes 9de4ea97
- 0098274c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0098274c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0098274c bytes 080300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cefe37a0260f2f55a0f2f49bd91c1e9a"></a>

### [`00982840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982840.md) → [`009829dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009829dc.md) _INIT_190

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 50.00% / 新版 47.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982848"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00982844",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00982848",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098284c",
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
      "009829e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009829e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009829e8",
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

- 旧版 [`00982844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982840.md#insn-00982844) · [`00982848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982840.md#insn-00982848) · [`0098284c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982840.md#insn-0098284c)

~~~diff
- 00982844 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00982844 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00982844 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00982844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00982844 bytes fd7b0fa9
- 00982848 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00982848 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00982848 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00982848 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00982848 bytes fc5710a9
- 0098284c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0098284c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0098284c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 0098284c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098284c bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a8961e4b60cc4cc52db2664b91f5a5"></a>

### [`0098486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/0098486c.md) → [`00984a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984a08.md) FUN_00984a08

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 6件 [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`009a2998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 3件 [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`0098cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098cf8c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 6件 [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`009a2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2b34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 33.33% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009848bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00984a30"
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
      "unmatched:00984894",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:009848a8",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "unmatched:009848bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00984a30",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00984a44",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "00984a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/0098486c.md#insn-00984894) · [`009848bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/0098486c.md#insn-009848bc) · [`009848c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/0098486c.md#insn-009848c0)
- 新版 `00984a5c`（命令位置の公開資料なし）

~~~diff
- 00984894 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00984894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00984894 bytes e10b00b9
- 009848bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009848bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009848bc bytes e80b00f9
- 009848c0 ["INT_ADD", "register:40f0:8", ["const:9848c0:8", "const:4:8"]]
- 009848c0 ["CALL", null, ["callee:00695bac:8"]]
+ 00984a5c ["INT_ADD", "register:40f0:8", ["const:984a5c:8", "const:4:8"]]
+ 00984a5c ["CALL", null, ["callee:00695bac:8"]]
- 009848c0 bytes ab44f497
+ 00984a5c bytes 5444f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3585834c869f7cda551bd4bb27516a"></a>

### [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) → [`00984c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984c34.md) FUN_00984c34

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a6fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6fcc.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 14件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00666768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666768.md) [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`009850f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md)
- 新版 呼出元 2件 [`006a700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a700c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 14件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`006667a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/006667a8.md) [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`00985294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985294.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.43% / 新版 68.43%

CFGの説明率　旧版 24.10% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00984e8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00984c7c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00984c90",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00984c98",
      "PARAM",
      [
        "storage",
        "00c70dc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00984c7c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00984c90",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00984c98",
      "PARAM",
      [
        "storage",
        "00c711c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00984b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md#insn-00984b44) · [`00984c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md#insn-00984c30)
- 新版 `00984ce0`（命令位置の公開資料なし）

~~~diff
- 00984b44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00984b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00984b44 bytes ea0700f9
- 00984c30 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00984c30 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00984c30 bytes 190200b4
+ 00984ce0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00984ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00984ce0 bytes ea0700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-028428ef6ef2e27bdbaa8ed215a72070"></a>

### [`009850f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md) → [`00985294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985294.md) FUN_00985294

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 3件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00b2f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md) [`00b3f2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f2fc.md)
- 新版 呼出元 3件 [`00984c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984c34.md) [`0098cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098cf8c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 3件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md) [`00b3f724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f724.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 51.72% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00985220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00985224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098522c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009852e0",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "byte[67]"
      ]
    ],
    [
      "unmatched:009851ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:009851fc",
      "READ",
      [
        "storage",
        "002c3ee8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009852e0",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "uleb128"
      ]
    ],
    [
      "00985388",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00985398",
      "READ",
      [
        "storage",
        "002c3f28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009851ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md#insn-009851ec) · [`00985220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md#insn-00985220) · [`00985224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md#insn-00985224)

~~~diff
- 009851ec ["INT_ADD", "register:40f0:8", ["const:9851ec:8", "const:4:8"]]
- 009851ec ["CALL", null, ["ram:46c984:8"]]
- 009851ec bytes e69deb97
- 00985220 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4:8"]]
- 00985220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00985220 bytes a04200fc
- 00985224 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00985224 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:d0:8"]]
- 00985224 ["STORE", null, ["const:1b1:8", "register:4048:8", "tmp:0:4"]]
- 00985224 bytes 2b0d0db8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d07cc31e0ba8051972bde49e0901688e"></a>

### [`0098c828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c828.md) → [`0098c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098c9c4.md) FUN_0098c9c4

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 3件 [`00664a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a4c.md) [`00664af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664af0.md) [`00affb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affb3c.md)
- 新版 呼出元 2件 [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) · 呼出先 3件 [`00664a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664a8c.md) [`00664b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664b30.md) [`00afff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00afff64.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.35% / 新版 87.35%

CFGの説明率　旧版 29.17% / 新版 28.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098c828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098c828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098c82c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098c828",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098c82c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098c830",
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
      "0098c9c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0098c9c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0098c9cc",
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

- 旧版 [`0098c828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c828.md#insn-0098c828) · [`0098c82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c828.md#insn-0098c82c) · [`0098c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098c828.md#insn-0098c830)

~~~diff
- 0098c828 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098c828 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098c828 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 0098c828 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098c828 bytes fd7bbaa9
- 0098c82c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0098c82c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0098c82c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0098c82c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098c82c bytes fc6f01a9
- 0098c830 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0098c830 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0098c830 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0098c830 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0098c830 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0725f715f6d671d24b1c7db35f194c45"></a>

### [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) → [`0098cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098cf8c.md) FUN_0098cf8c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006a6fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6fcc.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 18件 [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`005e29ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e29ec.md) [`00604e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604e14.md)
- 新版 呼出元 4件 [`006a700c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a700c.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 18件 [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`005e2a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2a2c.md) [`00604e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604e54.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 60.70% / 新版 60.70%

CFGの説明率　旧版 4.76% / 新版 4.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 21件, `store_condition` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098ce3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0098d018",
      "incomplete_value": true,
      "site": "0098d018",
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
      "definition_site": "0098ce7c",
      "incomplete_value": true,
      "site": "0098ce7c",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098cfe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098ce3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098daac"
      ]
    ],
    [
      "0098d014",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0098ce84",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0098cfd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098daac"
      ]
    ],
    [
      "0098d014",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0098d020",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098ce3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md#insn-0098ce3c) · [`0098ce7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md#insn-0098ce7c) · [`0098ce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md#insn-0098ce94)
- 新版 `0098d018`（命令位置の公開資料なし） · `0098d030`（命令位置の公開資料なし）

~~~diff
- 0098ce3c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0098ce3c ["CBRANCH", null, ["local:b80:8", "tmp:0:1"]]
- 0098ce3c bytes aa560054
- 0098ce7c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0098ce7c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0098d018 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0098d018 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0098ce7c bytes 200100b4
+ 0098d018 bytes 200100b4
- 0098ce94 ["INT_ADD", "register:40f0:8", ["const:98ce94:8", "const:4:8"]]
- 0098ce94 ["CALL", null, ["callee:00c58610:8"]]
+ 0098d030 ["INT_ADD", "register:40f0:8", ["const:98d030:8", "const:4:8"]]
+ 0098d030 ["CALL", null, ["callee:00c58610:8"]]
- 0098ce94 bytes df2c0b94
+ 0098d030 bytes 782d0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd1e1530419e5035cf208a233003e98"></a>

### [`00996780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996780.md) → [`0099691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/0099691c.md) FUN_0099691c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`006a657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a657c.md) [`006a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a7/006a7480.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 3件 [`009c75e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c75e0.md) [`009c7630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7630.md) [`009c7a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c7/009c7a0c.md)
- 新版 呼出元 7件 [`006a65bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a65bc.md) [`006a74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a74c0.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 3件 [`009c777c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c777c.md) [`009c77cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c77cc.md) [`009c7ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c7/009c7ba8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 10.00% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009967bc",
      "incomplete_value": true,
      "site": "009967c8",
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
            "const:338:8"
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

- 旧版 [`009967c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996780.md#insn-009967c8) · [`009967a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996780.md#insn-009967a0) · [`009967dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996780.md#insn-009967dc)
- 新版 `00996964`（命令位置の公開資料なし） · `0099693c`（命令位置の公開資料なし） · `00996978`（命令位置の公開資料なし）

~~~diff
- 009967c8 ["INT_ADD", "register:40f0:8", ["const:9967c8:8", "const:4:8"]]
- 009967c8 ["CALL", null, ["callee:009c777c:8"]]
+ 00996964 ["INT_ADD", "register:40f0:8", ["const:996964:8", "const:4:8"]]
+ 00996964 ["CALL", null, ["callee:009c777c:8"]]
- 009967c8 bytes 86c30094
+ 00996964 bytes 86c30094
- 009967a0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 009967a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0099693c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 0099693c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009967a0 bytes c8000034
+ 0099693c bytes c8000034
- 009967dc ["INT_ADD", "register:40f0:8", ["const:9967dc:8", "const:4:8"]]
- 009967dc ["CALL", null, ["callee:009c77cc:8"]]
+ 00996978 ["INT_ADD", "register:40f0:8", ["const:996978:8", "const:4:8"]]
+ 00996978 ["CALL", null, ["callee:009c77cc:8"]]
- 009967dc bytes 95c30094
+ 00996978 bytes 95c30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1d2af33e20d2b053a832a8f0f03e6a"></a>

### [`009969bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/009969bc.md) → [`00996b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996b58.md) FUN_00996b58

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 31.25% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00996a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00996bb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00996a1c",
      "incomplete_value": false,
      "site": "00996a24",
      "value": [
        "leaf",
        "const:28:8"
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
      "unmatched:00996a14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996b94"
      ]
    ]
  ],
  "added": [
    [
      "00996bb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996b94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00996a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/009969bc.md#insn-00996a14) · [`00996a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/009969bc.md#insn-00996a24)
- 新版 `00996bc0`（命令位置の公開資料なし） · `00996bb0`（命令位置の公開資料なし）

~~~diff
- 00996a14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00996a14 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00996a14 bytes 28ffffb5
- 00996a24 ["INT_ADD", "register:40f0:8", ["const:996a24:8", "const:4:8"]]
- 00996a24 ["CALL", null, ["callee:00c57e90:8"]]
+ 00996bc0 ["INT_ADD", "register:40f0:8", ["const:996bc0:8", "const:4:8"]]
+ 00996bc0 ["CALL", null, ["callee:00c57e90:8"]]
- 00996a24 bytes 1b040b94
+ 00996bc0 bytes b4040b94
+ 00996bb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00996bb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00996bb0 bytes 28ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5658fab1f651636adb08af46af088b0e"></a>

### [`00996dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996dc4.md) → [`00996f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996f60.md) FUN_00996f60

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 51.52% / 新版 51.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00996dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00996dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00996f60"
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
      "unmatched:00996dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00996f88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00996dfc"
      ]
    ],
    [
      "unmatched:00996df8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00996fac"
      ]
    ]
  ],
  "added": [
    [
      "00996f60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00996f88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00996f98"
      ]
    ],
    [
      "00996f94",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00996fac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00996dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996dc4.md#insn-00996dc4) · [`00996e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996dc4.md#insn-00996e04) · [`00996e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996dc4.md#insn-00996e7c)

~~~diff
- 00996dc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00996dc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00996dc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00996dc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00996dc4 bytes fd7bbfa9
- 00996e04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00996e04 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00996e04 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00996e04 bytes 68000054
- 00996e7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00996e7c ["RETURN", null, ["register:0:8"]]
- 00996e7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad9b50cf79e79d9c7c95b83f69f0f5c"></a>

### [`009a12bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a12bc.md) → [`009a1458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a1458.md) FUN_009a1458

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 6.25% / 新版 5.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a12f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a1490"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009a149c",
      "incomplete_value": true,
      "site": "009a149c",
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
      "definition_site": "009a1300",
      "incomplete_value": true,
      "site": "009a1300",
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
      "unmatched:009a12f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "009a1498",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:009a1308",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009a1490",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "009a1498",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009a14a4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a12f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a12bc.md#insn-009a12f4) · [`009a1300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a12bc.md#insn-009a1300) · [`009a131c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a12bc.md#insn-009a131c)
- 新版 `009a149c`（命令位置の公開資料なし） · `009a14b8`（命令位置の公開資料なし）

~~~diff
- 009a12f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 009a12f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a12f4 bytes e80f00f9
- 009a1300 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009a1300 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 009a149c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009a149c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009a1300 bytes 480100b4
+ 009a149c bytes 480100b4
- 009a131c ["INT_ADD", "register:40f0:8", ["const:9a131c:8", "const:4:8"]]
- 009a131c ["CALL", null, ["callee:00c58610:8"]]
+ 009a14b8 ["INT_ADD", "register:40f0:8", ["const:9a14b8:8", "const:4:8"]]
+ 009a14b8 ["CALL", null, ["callee:00c58610:8"]]
- 009a131c bytes bddb0a94
+ 009a14b8 bytes 56dc0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

