# v16.0.0 → v16.0.1 · 最優先の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-77ed8c65cb57a9997c061a9261aacc76"></a>

### [`007fc21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc21c.md) → [`007fc25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md) FUN_007fc25c

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
      "definition_site": "007fc280",
      "incomplete_value": false,
      "site": "007fc280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc240",
      "incomplete_value": false,
      "site": "007fc240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "007fc280",
      "DATA",
      [
        "storage",
        "00c7cd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc280",
      "DATA",
      [
        "storage",
        "00c7d130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc21c.md#insn-007fc230) · [`007fc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc21c.md#insn-007fc238) · [`007fc23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc21c.md#insn-007fc23c)
- 新版 [`007fc270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md#insn-007fc270) · [`007fc278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md#insn-007fc278) · [`007fc27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc25c.md#insn-007fc27c)

~~~diff
- 007fc230 ["INT_ADD", "register:40f0:8", ["const:7fc230:8", "const:4:8"]]
- 007fc230 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc270 ["INT_ADD", "register:40f0:8", ["const:7fc270:8", "const:4:8"]]
+ 007fc270 ["CALL", null, ["callee:00c57e90:8"]]
- 007fc230 bytes 186e1194
+ 007fc270 bytes 086f1194
- 007fc238 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc278 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc238 bytes 08240090
+ 007fc278 bytes 082400b0
- 007fc23c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 007fc23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc27c ["COPY", "tmp:0:8", ["const:130:8"]]
+ 007fc27c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc27c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc27c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc23c bytes 08c13491
+ 007fc27c bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2296fee44c90fb1bb7a9b430350463c7"></a>

### [`007fc26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc26c.md) → [`007fc2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md) FUN_007fc2ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc2d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc290",
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
      "007fc2d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc2d0",
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

- 旧版 [`007fc290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc26c.md#insn-007fc290) · [`007fc29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc26c.md#insn-007fc29c)
- 新版 [`007fc2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md#insn-007fc2d0) · [`007fc2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc2ac.md#insn-007fc2dc)

~~~diff
- 007fc290 ["INT_ADD", "register:40f0:8", ["const:7fc290:8", "const:4:8"]]
- 007fc290 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc2d0 ["INT_ADD", "register:40f0:8", ["const:7fc2d0:8", "const:4:8"]]
+ 007fc2d0 ["CALL", null, ["ram:47acf4:8"]]
- 007fc290 bytes 89faf197
+ 007fc2d0 bytes 89faf197
- 007fc29c ["INT_ADD", "register:40f0:8", ["const:7fc29c:8", "const:4:8"]]
- 007fc29c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc2dc ["INT_ADD", "register:40f0:8", ["const:7fc2dc:8", "const:4:8"]]
+ 007fc2dc ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc29c bytes be02f297
+ 007fc2dc bytes be02f297
~~~


<a id="compare-5c9f71f60676ce980ca4e0c3e66fb50f"></a>

### [`007fc2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc2e0.md) → [`007fc320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md) FUN_007fc320

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
      "definition_site": "007fc344",
      "incomplete_value": false,
      "site": "007fc344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc304",
      "incomplete_value": false,
      "site": "007fc304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007fc344",
      "DATA",
      [
        "storage",
        "00c7cdb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc344",
      "DATA",
      [
        "storage",
        "00c7d1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc2e0.md#insn-007fc2f4) · [`007fc2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc2e0.md#insn-007fc2fc) · [`007fc300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc2e0.md#insn-007fc300)
- 新版 [`007fc334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md#insn-007fc334) · [`007fc33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md#insn-007fc33c) · [`007fc340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc320.md#insn-007fc340)

~~~diff
- 007fc2f4 ["INT_ADD", "register:40f0:8", ["const:7fc2f4:8", "const:4:8"]]
- 007fc2f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc334 ["INT_ADD", "register:40f0:8", ["const:7fc334:8", "const:4:8"]]
+ 007fc334 ["CALL", null, ["callee:00c57e90:8"]]
- 007fc2f4 bytes e76d1194
+ 007fc334 bytes d76e1194
- 007fc2fc ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc33c ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc2fc bytes 08240090
+ 007fc33c bytes 082400b0
- 007fc300 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007fc300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc340 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 007fc340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc300 bytes 08c13691
+ 007fc340 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1be681408ca01dcb74b63779ae68cf3"></a>

### [`007fc330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc330.md) → [`007fc370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md) FUN_007fc370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc394",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc354",
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
      "007fc394",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc394",
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

- 旧版 [`007fc354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc330.md#insn-007fc354) · [`007fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc330.md#insn-007fc360)
- 新版 [`007fc394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md#insn-007fc394) · [`007fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc370.md#insn-007fc3a0)

~~~diff
- 007fc354 ["INT_ADD", "register:40f0:8", ["const:7fc354:8", "const:4:8"]]
- 007fc354 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc394 ["INT_ADD", "register:40f0:8", ["const:7fc394:8", "const:4:8"]]
+ 007fc394 ["CALL", null, ["ram:47acf4:8"]]
- 007fc354 bytes 58faf197
+ 007fc394 bytes 58faf197
- 007fc360 ["INT_ADD", "register:40f0:8", ["const:7fc360:8", "const:4:8"]]
- 007fc360 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc3a0 ["INT_ADD", "register:40f0:8", ["const:7fc3a0:8", "const:4:8"]]
+ 007fc3a0 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc360 bytes 8d02f297
+ 007fc3a0 bytes 8d02f297
~~~


<a id="compare-e1b25ff03b647a3af6ffe8ad9d80af5f"></a>

### [`007fc3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3a4.md) → [`007fc3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md) FUN_007fc3e4

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
      "definition_site": "007fc3f8",
      "incomplete_value": false,
      "site": "007fc3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc3b8",
      "incomplete_value": false,
      "site": "007fc3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "007fc3fc",
      "DATA",
      [
        "storage",
        "00c7ce30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc3fc",
      "DATA",
      [
        "storage",
        "00c7d230",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3a4.md#insn-007fc3b0) · [`007fc3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3a4.md#insn-007fc3b4) · [`007fc3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3a4.md#insn-007fc3b8)
- 新版 [`007fc3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md#insn-007fc3f0) · [`007fc3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md#insn-007fc3f4) · [`007fc3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc3e4.md#insn-007fc3f8)

~~~diff
- 007fc3b0 ["INT_ADD", "register:40f0:8", ["const:7fc3b0:8", "const:4:8"]]
- 007fc3b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc3f0 ["INT_ADD", "register:40f0:8", ["const:7fc3f0:8", "const:4:8"]]
+ 007fc3f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007fc3b0 bytes b86d1194
+ 007fc3f0 bytes a86e1194
- 007fc3b4 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc3f4 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc3b4 bytes 08240090
+ 007fc3f4 bytes 082400b0
- 007fc3b8 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 007fc3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc3f8 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 007fc3f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc3f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc3f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc3b8 bytes 08c13891
+ 007fc3f8 bytes 08c10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ca675387075f6b1a2bd5507e61f7bb"></a>

### [`007fc3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3e0.md) → [`007fc420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md) FUN_007fc420

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc444",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc404",
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
      "007fc444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc444",
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

- 旧版 [`007fc404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3e0.md#insn-007fc404) · [`007fc410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc3e0.md#insn-007fc410)
- 新版 [`007fc444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md#insn-007fc444) · [`007fc450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc420.md#insn-007fc450)

~~~diff
- 007fc404 ["INT_ADD", "register:40f0:8", ["const:7fc404:8", "const:4:8"]]
- 007fc404 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc444 ["INT_ADD", "register:40f0:8", ["const:7fc444:8", "const:4:8"]]
+ 007fc444 ["CALL", null, ["ram:47acf4:8"]]
- 007fc404 bytes 2cfaf197
+ 007fc444 bytes 2cfaf197
- 007fc410 ["INT_ADD", "register:40f0:8", ["const:7fc410:8", "const:4:8"]]
- 007fc410 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc450 ["INT_ADD", "register:40f0:8", ["const:7fc450:8", "const:4:8"]]
+ 007fc450 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc410 bytes 6102f297
+ 007fc450 bytes 6102f297
~~~


<a id="compare-4951d127c678bc993362cb6fa6267557"></a>

### [`007fc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc454.md) → [`007fc494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md) FUN_007fc494

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
      "definition_site": "007fc4b8",
      "incomplete_value": false,
      "site": "007fc4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc478",
      "incomplete_value": false,
      "site": "007fc478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007fc4b8",
      "DATA",
      [
        "storage",
        "00c7ceb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc4b8",
      "DATA",
      [
        "storage",
        "00c7d2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc454.md#insn-007fc468) · [`007fc470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc454.md#insn-007fc470) · [`007fc474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc454.md#insn-007fc474)
- 新版 [`007fc4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md#insn-007fc4a8) · [`007fc4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md#insn-007fc4b0) · [`007fc4b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc494.md#insn-007fc4b4)

~~~diff
- 007fc468 ["INT_ADD", "register:40f0:8", ["const:7fc468:8", "const:4:8"]]
- 007fc468 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc4a8 ["INT_ADD", "register:40f0:8", ["const:7fc4a8:8", "const:4:8"]]
+ 007fc4a8 ["CALL", null, ["callee:00c57e90:8"]]
- 007fc468 bytes 8a6d1194
+ 007fc4a8 bytes 7a6e1194
- 007fc470 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc4b0 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc470 bytes 08240090
+ 007fc4b0 bytes 082400b0
- 007fc474 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007fc474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc4b4 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 007fc4b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc4b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc4b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc474 bytes 08c13a91
+ 007fc4b4 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab984777c59ed0124c408da994298bc4"></a>

### [`007fc4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc4a4.md) → [`007fc4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md) FUN_007fc4e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

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
      "site": "007fc50c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc4cc",
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
      "007fc50c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc50c",
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

- 旧版 [`007fc4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc4a4.md#insn-007fc4cc) · [`007fc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc4a4.md#insn-007fc4d8)
- 新版 [`007fc50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md#insn-007fc50c) · [`007fc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc4e4.md#insn-007fc518)

~~~diff
- 007fc4cc ["INT_ADD", "register:40f0:8", ["const:7fc4cc:8", "const:4:8"]]
- 007fc4cc ["CALL", null, ["ram:47acb4:8"]]
+ 007fc50c ["INT_ADD", "register:40f0:8", ["const:7fc50c:8", "const:4:8"]]
+ 007fc50c ["CALL", null, ["ram:47acf4:8"]]
- 007fc4cc bytes faf9f197
+ 007fc50c bytes faf9f197
- 007fc4d8 ["INT_ADD", "register:40f0:8", ["const:7fc4d8:8", "const:4:8"]]
- 007fc4d8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc518 ["INT_ADD", "register:40f0:8", ["const:7fc518:8", "const:4:8"]]
+ 007fc518 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc4d8 bytes 2f02f297
+ 007fc518 bytes 2f02f297
~~~


<a id="compare-c0376d951140a067e10f0493a532661f"></a>

### [`007fc560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc560.md) → [`007fc5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md) FUN_007fc5a0

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
      "definition_site": "007fc5b4",
      "incomplete_value": false,
      "site": "007fc5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc574",
      "incomplete_value": false,
      "site": "007fc578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "007fc5b8",
      "DATA",
      [
        "storage",
        "00c7cf30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc5b8",
      "DATA",
      [
        "storage",
        "00c7d330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc560.md#insn-007fc56c) · [`007fc570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc560.md#insn-007fc570) · [`007fc574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc560.md#insn-007fc574)
- 新版 [`007fc5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md#insn-007fc5ac) · [`007fc5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md#insn-007fc5b0) · [`007fc5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5a0.md#insn-007fc5b4)

~~~diff
- 007fc56c ["INT_ADD", "register:40f0:8", ["const:7fc56c:8", "const:4:8"]]
- 007fc56c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc5ac ["INT_ADD", "register:40f0:8", ["const:7fc5ac:8", "const:4:8"]]
+ 007fc5ac ["CALL", null, ["callee:00c57e90:8"]]
- 007fc56c bytes 496d1194
+ 007fc5ac bytes 396e1194
- 007fc570 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc5b0 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc570 bytes 08240090
+ 007fc5b0 bytes 082400b0
- 007fc574 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007fc574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc5b4 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007fc5b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc5b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc5b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc574 bytes 08c13c91
+ 007fc5b4 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d9d5fbd726e94a8978df0a5a956f624"></a>

### [`007fc59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc59c.md) → [`007fc5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md) FUN_007fc5dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "007fc600",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc5c0",
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
      "007fc600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc600",
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

- 旧版 [`007fc5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc59c.md#insn-007fc5c0) · [`007fc5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc59c.md#insn-007fc5cc) · [`007fc5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc59c.md#insn-007fc5ec)
- 新版 [`007fc600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc600) · [`007fc60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc60c) · [`007fc62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc5dc.md#insn-007fc62c)

~~~diff
- 007fc5c0 ["INT_ADD", "register:40f0:8", ["const:7fc5c0:8", "const:4:8"]]
- 007fc5c0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc600 ["INT_ADD", "register:40f0:8", ["const:7fc600:8", "const:4:8"]]
+ 007fc600 ["CALL", null, ["ram:47acf4:8"]]
- 007fc5c0 bytes bdf9f197
+ 007fc600 bytes bdf9f197
- 007fc5cc ["INT_ADD", "register:40f0:8", ["const:7fc5cc:8", "const:4:8"]]
- 007fc5cc ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc60c ["INT_ADD", "register:40f0:8", ["const:7fc60c:8", "const:4:8"]]
+ 007fc60c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc5cc bytes f201f297
+ 007fc60c bytes f201f297
- 007fc5ec ["INT_ADD", "register:40f0:8", ["const:7fc5ec:8", "const:4:8"]]
- 007fc5ec ["CALL", null, ["callee:008514f8:8"]]
+ 007fc62c ["INT_ADD", "register:40f0:8", ["const:7fc62c:8", "const:4:8"]]
+ 007fc62c ["CALL", null, ["callee:008514f8:8"]]
- 007fc5ec bytes b3530194
+ 007fc62c bytes b3530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ee9c1bb9d638469ccca45dadf336e42"></a>

### [`007fc640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc640.md) → [`007fc680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md) FUN_007fc680

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
      "definition_site": "007fc694",
      "incomplete_value": false,
      "site": "007fc698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc654",
      "incomplete_value": false,
      "site": "007fc658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7c000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "007fc698",
      "DATA",
      [
        "storage",
        "00c7cfb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc698",
      "DATA",
      [
        "storage",
        "00c7d3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc640.md#insn-007fc64c) · [`007fc650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc640.md#insn-007fc650) · [`007fc654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc640.md#insn-007fc654)
- 新版 [`007fc68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md#insn-007fc68c) · [`007fc690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md#insn-007fc690) · [`007fc694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc680.md#insn-007fc694)

~~~diff
- 007fc64c ["INT_ADD", "register:40f0:8", ["const:7fc64c:8", "const:4:8"]]
- 007fc64c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc68c ["INT_ADD", "register:40f0:8", ["const:7fc68c:8", "const:4:8"]]
+ 007fc68c ["CALL", null, ["callee:00c57e90:8"]]
- 007fc64c bytes 116d1194
+ 007fc68c bytes 016e1194
- 007fc650 ["COPY", "register:4040:8", ["const:c7c000:8"]]
+ 007fc690 ["COPY", "register:4040:8", ["const:c7d000:8"]]
- 007fc650 bytes 08240090
+ 007fc690 bytes 082400b0
- 007fc654 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007fc654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc694 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 007fc694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc654 bytes 08c13e91
+ 007fc694 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851f67f713f002044726034ad0378709"></a>

### [`007fc67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc67c.md) → [`007fc6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md) FUN_007fc6bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

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
      "site": "007fc6e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc6a0",
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
      "007fc6e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc6e0",
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

- 旧版 [`007fc6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc67c.md#insn-007fc6a0) · [`007fc6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc67c.md#insn-007fc6ac) · [`007fc6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc67c.md#insn-007fc6cc)
- 新版 [`007fc6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc6e0) · [`007fc6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc6ec) · [`007fc70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc6bc.md#insn-007fc70c)

~~~diff
- 007fc6a0 ["INT_ADD", "register:40f0:8", ["const:7fc6a0:8", "const:4:8"]]
- 007fc6a0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc6e0 ["INT_ADD", "register:40f0:8", ["const:7fc6e0:8", "const:4:8"]]
+ 007fc6e0 ["CALL", null, ["ram:47acf4:8"]]
- 007fc6a0 bytes 85f9f197
+ 007fc6e0 bytes 85f9f197
- 007fc6ac ["INT_ADD", "register:40f0:8", ["const:7fc6ac:8", "const:4:8"]]
- 007fc6ac ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc6ec ["INT_ADD", "register:40f0:8", ["const:7fc6ec:8", "const:4:8"]]
+ 007fc6ec ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc6ac bytes ba01f297
+ 007fc6ec bytes ba01f297
- 007fc6cc ["INT_ADD", "register:40f0:8", ["const:7fc6cc:8", "const:4:8"]]
- 007fc6cc ["CALL", null, ["callee:008514f8:8"]]
+ 007fc70c ["INT_ADD", "register:40f0:8", ["const:7fc70c:8", "const:4:8"]]
+ 007fc70c ["CALL", null, ["callee:008514f8:8"]]
- 007fc6cc bytes 7b530194
+ 007fc70c bytes 7b530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-020954a0b978e6a13995ac3eb6985759"></a>

### [`007fc790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc790.md) → [`007fc7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md) FUN_007fc7d0

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
      "definition_site": "007fc7e4",
      "incomplete_value": false,
      "site": "007fc7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc7a4",
      "incomplete_value": false,
      "site": "007fc7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "007fc7e8",
      "DATA",
      [
        "storage",
        "00c7d030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc7e8",
      "DATA",
      [
        "storage",
        "00c7d430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc790.md#insn-007fc79c) · [`007fc7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc790.md#insn-007fc7a4)
- 新版 [`007fc7dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md#insn-007fc7dc) · [`007fc7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc7d0.md#insn-007fc7e4)

~~~diff
- 007fc79c ["INT_ADD", "register:40f0:8", ["const:7fc79c:8", "const:4:8"]]
- 007fc79c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc7dc ["INT_ADD", "register:40f0:8", ["const:7fc7dc:8", "const:4:8"]]
+ 007fc7dc ["CALL", null, ["callee:00c57e90:8"]]
- 007fc79c bytes bd6c1194
+ 007fc7dc bytes ad6d1194
- 007fc7a4 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007fc7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc7e4 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 007fc7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc7a4 bytes 08c10091
+ 007fc7e4 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f866431c724e54fca03fdce2a60e69"></a>

### [`007fc7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc7cc.md) → [`007fc80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md) FUN_007fc80c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc830",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc7f0",
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
      "007fc830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc830",
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

- 旧版 [`007fc7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc7cc.md#insn-007fc7f0) · [`007fc7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc7cc.md#insn-007fc7fc)
- 新版 [`007fc830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md#insn-007fc830) · [`007fc83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc80c.md#insn-007fc83c)

~~~diff
- 007fc7f0 ["INT_ADD", "register:40f0:8", ["const:7fc7f0:8", "const:4:8"]]
- 007fc7f0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc830 ["INT_ADD", "register:40f0:8", ["const:7fc830:8", "const:4:8"]]
+ 007fc830 ["CALL", null, ["ram:47acf4:8"]]
- 007fc7f0 bytes 31f9f197
+ 007fc830 bytes 31f9f197
- 007fc7fc ["INT_ADD", "register:40f0:8", ["const:7fc7fc:8", "const:4:8"]]
- 007fc7fc ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc83c ["INT_ADD", "register:40f0:8", ["const:7fc83c:8", "const:4:8"]]
+ 007fc83c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc7fc bytes 6601f297
+ 007fc83c bytes 6601f297
~~~


<a id="compare-ccd7ebe00cffd7ea78694ba241e808dc"></a>

### [`007fc840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc840.md) → [`007fc880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md) FUN_007fc880

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
      "definition_site": "007fc894",
      "incomplete_value": false,
      "site": "007fc898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc854",
      "incomplete_value": false,
      "site": "007fc858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "007fc898",
      "DATA",
      [
        "storage",
        "00c7d0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc898",
      "DATA",
      [
        "storage",
        "00c7d4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc840.md#insn-007fc84c) · [`007fc854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc840.md#insn-007fc854)
- 新版 [`007fc88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md#insn-007fc88c) · [`007fc894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc880.md#insn-007fc894)

~~~diff
- 007fc84c ["INT_ADD", "register:40f0:8", ["const:7fc84c:8", "const:4:8"]]
- 007fc84c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc88c ["INT_ADD", "register:40f0:8", ["const:7fc88c:8", "const:4:8"]]
+ 007fc88c ["CALL", null, ["callee:00c57e90:8"]]
- 007fc84c bytes 916c1194
+ 007fc88c bytes 816d1194
- 007fc854 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007fc854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc894 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 007fc894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc854 bytes 08c10291
+ 007fc894 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba3e486a4c2f8a399db9bef5e3426fa3"></a>

### [`007fc87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc87c.md) → [`007fc8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md) FUN_007fc8bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc8e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc8a0",
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
      "007fc8e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc8e0",
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

- 旧版 [`007fc8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc87c.md#insn-007fc8a0) · [`007fc8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc87c.md#insn-007fc8ac)
- 新版 [`007fc8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md#insn-007fc8e0) · [`007fc8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc8bc.md#insn-007fc8ec)

~~~diff
- 007fc8a0 ["INT_ADD", "register:40f0:8", ["const:7fc8a0:8", "const:4:8"]]
- 007fc8a0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc8e0 ["INT_ADD", "register:40f0:8", ["const:7fc8e0:8", "const:4:8"]]
+ 007fc8e0 ["CALL", null, ["ram:47acf4:8"]]
- 007fc8a0 bytes 05f9f197
+ 007fc8e0 bytes 05f9f197
- 007fc8ac ["INT_ADD", "register:40f0:8", ["const:7fc8ac:8", "const:4:8"]]
- 007fc8ac ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc8ec ["INT_ADD", "register:40f0:8", ["const:7fc8ec:8", "const:4:8"]]
+ 007fc8ec ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc8ac bytes 3a01f297
+ 007fc8ec bytes 3a01f297
~~~


<a id="compare-55016b242f6bf5a9c5b49cee670b249e"></a>

### [`007fc8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc8f0.md) → [`007fc930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md) FUN_007fc930

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
      "definition_site": "007fc944",
      "incomplete_value": false,
      "site": "007fc948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc904",
      "incomplete_value": false,
      "site": "007fc908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "007fc948",
      "DATA",
      [
        "storage",
        "00c7d130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc948",
      "DATA",
      [
        "storage",
        "00c7d530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc8f0.md#insn-007fc8fc) · [`007fc904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc8f0.md#insn-007fc904)
- 新版 [`007fc93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md#insn-007fc93c) · [`007fc944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc930.md#insn-007fc944)

~~~diff
- 007fc8fc ["INT_ADD", "register:40f0:8", ["const:7fc8fc:8", "const:4:8"]]
- 007fc8fc ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc93c ["INT_ADD", "register:40f0:8", ["const:7fc93c:8", "const:4:8"]]
+ 007fc93c ["CALL", null, ["callee:00c57e90:8"]]
- 007fc8fc bytes 656c1194
+ 007fc93c bytes 556d1194
- 007fc904 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007fc904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc944 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 007fc944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc904 bytes 08c10491
+ 007fc944 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b624af1343bd4bb06964730cb7cfa5"></a>

### [`007fc92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc92c.md) → [`007fc96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md) FUN_007fc96c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fc990",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fc950",
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
      "007fc990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fc990",
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

- 旧版 [`007fc950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc92c.md#insn-007fc950) · [`007fc95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc92c.md#insn-007fc95c)
- 新版 [`007fc990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md#insn-007fc990) · [`007fc99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc96c.md#insn-007fc99c)

~~~diff
- 007fc950 ["INT_ADD", "register:40f0:8", ["const:7fc950:8", "const:4:8"]]
- 007fc950 ["CALL", null, ["ram:47acb4:8"]]
+ 007fc990 ["INT_ADD", "register:40f0:8", ["const:7fc990:8", "const:4:8"]]
+ 007fc990 ["CALL", null, ["ram:47acf4:8"]]
- 007fc950 bytes d9f8f197
+ 007fc990 bytes d9f8f197
- 007fc95c ["INT_ADD", "register:40f0:8", ["const:7fc95c:8", "const:4:8"]]
- 007fc95c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fc99c ["INT_ADD", "register:40f0:8", ["const:7fc99c:8", "const:4:8"]]
+ 007fc99c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fc95c bytes 0e01f297
+ 007fc99c bytes 0e01f297
~~~


<a id="compare-faa7cd7ff9ec022aadff7456a3a31bfa"></a>

### [`007fc9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9a0.md) → [`007fc9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md) FUN_007fc9e0

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
      "definition_site": "007fc9f4",
      "incomplete_value": false,
      "site": "007fc9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fc9b4",
      "incomplete_value": false,
      "site": "007fc9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fc9f8",
      "DATA",
      [
        "storage",
        "00c7d1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fc9f8",
      "DATA",
      [
        "storage",
        "00c7d5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fc9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9a0.md#insn-007fc9ac) · [`007fc9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9a0.md#insn-007fc9b4)
- 新版 [`007fc9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md#insn-007fc9ec) · [`007fc9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fc9e0.md#insn-007fc9f4)

~~~diff
- 007fc9ac ["INT_ADD", "register:40f0:8", ["const:7fc9ac:8", "const:4:8"]]
- 007fc9ac ["CALL", null, ["callee:00c57e90:8"]]
+ 007fc9ec ["INT_ADD", "register:40f0:8", ["const:7fc9ec:8", "const:4:8"]]
+ 007fc9ec ["CALL", null, ["callee:00c57e90:8"]]
- 007fc9ac bytes 396c1194
+ 007fc9ec bytes 296d1194
- 007fc9b4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007fc9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fc9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fc9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fc9f4 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 007fc9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fc9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fc9b4 bytes 08c10691
+ 007fc9f4 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce48c577b9aa01e66aa3fbcb4b6f6c50"></a>

### [`007fc9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9dc.md) → [`007fca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md) FUN_007fca1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fca40",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fca00",
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
      "007fca40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fca40",
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

- 旧版 [`007fca00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9dc.md#insn-007fca00) · [`007fca0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fc9dc.md#insn-007fca0c)
- 新版 [`007fca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md#insn-007fca40) · [`007fca4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca1c.md#insn-007fca4c)

~~~diff
- 007fca00 ["INT_ADD", "register:40f0:8", ["const:7fca00:8", "const:4:8"]]
- 007fca00 ["CALL", null, ["ram:47acb4:8"]]
+ 007fca40 ["INT_ADD", "register:40f0:8", ["const:7fca40:8", "const:4:8"]]
+ 007fca40 ["CALL", null, ["ram:47acf4:8"]]
- 007fca00 bytes adf8f197
+ 007fca40 bytes adf8f197
- 007fca0c ["INT_ADD", "register:40f0:8", ["const:7fca0c:8", "const:4:8"]]
- 007fca0c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fca4c ["INT_ADD", "register:40f0:8", ["const:7fca4c:8", "const:4:8"]]
+ 007fca4c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fca0c bytes e200f297
+ 007fca4c bytes e200f297
~~~


<a id="compare-a4a311b78788818272135c4e24ae00b2"></a>

### [`007fca50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fca50.md) → [`007fca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md) FUN_007fca90

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
      "definition_site": "007fcab4",
      "incomplete_value": false,
      "site": "007fcab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fca74",
      "incomplete_value": false,
      "site": "007fca74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "007fcab4",
      "DATA",
      [
        "storage",
        "00c7d230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcab4",
      "DATA",
      [
        "storage",
        "00c7d630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fca50.md#insn-007fca64) · [`007fca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fca50.md#insn-007fca70)
- 新版 [`007fcaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md#insn-007fcaa4) · [`007fcab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fca90.md#insn-007fcab0)

~~~diff
- 007fca64 ["INT_ADD", "register:40f0:8", ["const:7fca64:8", "const:4:8"]]
- 007fca64 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcaa4 ["INT_ADD", "register:40f0:8", ["const:7fcaa4:8", "const:4:8"]]
+ 007fcaa4 ["CALL", null, ["callee:00c57e90:8"]]
- 007fca64 bytes 0b6c1194
+ 007fcaa4 bytes fb6c1194
- 007fca70 ["COPY", "tmp:0:8", ["const:230:8"]]
- 007fca70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fca70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fca70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcab0 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 007fcab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fca70 bytes 08c10891
+ 007fcab0 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe202aafc23b1b4d8e98a1c5badaf59"></a>

### [`007fcaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcaa0.md) → [`007fcae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md) FUN_007fcae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "007fcb08",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcac8",
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
      "007fcb08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fcb08",
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

- 旧版 [`007fcac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcaa0.md#insn-007fcac8) · [`007fcad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcaa0.md#insn-007fcad4) · [`007fcb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcaa0.md#insn-007fcb14)
- 新版 [`007fcb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb08) · [`007fcb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb14) · [`007fcb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcae0.md#insn-007fcb54)

~~~diff
- 007fcac8 ["INT_ADD", "register:40f0:8", ["const:7fcac8:8", "const:4:8"]]
- 007fcac8 ["CALL", null, ["ram:47acb4:8"]]
+ 007fcb08 ["INT_ADD", "register:40f0:8", ["const:7fcb08:8", "const:4:8"]]
+ 007fcb08 ["CALL", null, ["ram:47acf4:8"]]
- 007fcac8 bytes 7bf8f197
+ 007fcb08 bytes 7bf8f197
- 007fcad4 ["INT_ADD", "register:40f0:8", ["const:7fcad4:8", "const:4:8"]]
- 007fcad4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fcb14 ["INT_ADD", "register:40f0:8", ["const:7fcb14:8", "const:4:8"]]
+ 007fcb14 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fcad4 bytes b000f297
+ 007fcb14 bytes b000f297
- 007fcb14 ["INT_ADD", "register:40f0:8", ["const:7fcb14:8", "const:4:8"]]
- 007fcb14 ["CALL", null, ["callee:008b79c8:8"]]
+ 007fcb54 ["INT_ADD", "register:40f0:8", ["const:7fcb54:8", "const:4:8"]]
+ 007fcb54 ["CALL", null, ["callee:008b79c8:8"]]
- 007fcb14 bytes 9ceb0294
+ 007fcb54 bytes 9deb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-690077fe304fec0e25938c53b39b3938"></a>

### [`007fcb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcb88.md) → [`007fcbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md) FUN_007fcbc8

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
      "definition_site": "007fcbe8",
      "incomplete_value": false,
      "site": "007fcbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcba8",
      "incomplete_value": false,
      "site": "007fcbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fcbec",
      "DATA",
      [
        "storage",
        "00c7d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcbec",
      "DATA",
      [
        "storage",
        "00c7d6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcb88.md#insn-007fcb9c) · [`007fcba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcb88.md#insn-007fcba8)
- 新版 [`007fcbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md#insn-007fcbdc) · [`007fcbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcbc8.md#insn-007fcbe8)

~~~diff
- 007fcb9c ["INT_ADD", "register:40f0:8", ["const:7fcb9c:8", "const:4:8"]]
- 007fcb9c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcbdc ["INT_ADD", "register:40f0:8", ["const:7fcbdc:8", "const:4:8"]]
+ 007fcbdc ["CALL", null, ["callee:00c57e90:8"]]
- 007fcb9c bytes bd6b1194
+ 007fcbdc bytes ad6c1194
- 007fcba8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 007fcba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcbe8 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 007fcbe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcbe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcbe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcba8 bytes 08c10a91
+ 007fcbe8 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9227963368e27d3721eb719c43cfce3e"></a>

### [`007fcbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcbe0.md) → [`007fcc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md) FUN_007fcc20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "site": "007fcc48",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcc08",
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
      "007fcc48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fcc48",
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

- 旧版 [`007fcc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcbe0.md#insn-007fcc08) · [`007fcc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcbe0.md#insn-007fcc14) · [`007fcc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcbe0.md#insn-007fcc38)
- 新版 [`007fcc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcc48) · [`007fcc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcc54) · [`007fcc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcc20.md#insn-007fcc78)

~~~diff
- 007fcc08 ["INT_ADD", "register:40f0:8", ["const:7fcc08:8", "const:4:8"]]
- 007fcc08 ["CALL", null, ["ram:47acb4:8"]]
+ 007fcc48 ["INT_ADD", "register:40f0:8", ["const:7fcc48:8", "const:4:8"]]
+ 007fcc48 ["CALL", null, ["ram:47acf4:8"]]
- 007fcc08 bytes 2bf8f197
+ 007fcc48 bytes 2bf8f197
- 007fcc14 ["INT_ADD", "register:40f0:8", ["const:7fcc14:8", "const:4:8"]]
- 007fcc14 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fcc54 ["INT_ADD", "register:40f0:8", ["const:7fcc54:8", "const:4:8"]]
+ 007fcc54 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fcc14 bytes 6000f297
+ 007fcc54 bytes 6000f297
- 007fcc38 ["INT_ADD", "register:40f0:8", ["const:7fcc38:8", "const:4:8"]]
- 007fcc38 ["CALL", null, ["callee:008514f8:8"]]
+ 007fcc78 ["INT_ADD", "register:40f0:8", ["const:7fcc78:8", "const:4:8"]]
+ 007fcc78 ["CALL", null, ["callee:008514f8:8"]]
- 007fcc38 bytes 20520194
+ 007fcc78 bytes 20520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b7d16f4b9f8a370ccb9e2267b2800d9"></a>

### [`007fccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fccbc.md) → [`007fccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md) FUN_007fccfc

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
      "definition_site": "007fcd1c",
      "incomplete_value": false,
      "site": "007fcd20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fccdc",
      "incomplete_value": false,
      "site": "007fcce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007fcd20",
      "DATA",
      [
        "storage",
        "00c7d330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcd20",
      "DATA",
      [
        "storage",
        "00c7d730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fccbc.md#insn-007fccd0) · [`007fccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fccbc.md#insn-007fccdc)
- 新版 [`007fcd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md#insn-007fcd10) · [`007fcd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md#insn-007fcd1c)

~~~diff
- 007fccd0 ["INT_ADD", "register:40f0:8", ["const:7fccd0:8", "const:4:8"]]
- 007fccd0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcd10 ["INT_ADD", "register:40f0:8", ["const:7fcd10:8", "const:4:8"]]
+ 007fcd10 ["CALL", null, ["callee:00c57e90:8"]]
- 007fccd0 bytes 706b1194
+ 007fcd10 bytes 606c1194
- 007fccdc ["COPY", "tmp:0:8", ["const:330:8"]]
- 007fccdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fccdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fccdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcd1c ["COPY", "tmp:0:8", ["const:730:8"]]
+ 007fcd1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcd1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcd1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fccdc bytes 08c10c91
+ 007fcd1c bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9ac281f61d7abfb218bf025229ce0e"></a>

### [`007fcd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd14.md) → [`007fcd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md) FUN_007fcd54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fcd78",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcd38",
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
      "007fcd78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fcd78",
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

- 旧版 [`007fcd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd14.md#insn-007fcd38) · [`007fcd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd14.md#insn-007fcd44)
- 新版 [`007fcd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md#insn-007fcd78) · [`007fcd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md#insn-007fcd84)

~~~diff
- 007fcd38 ["INT_ADD", "register:40f0:8", ["const:7fcd38:8", "const:4:8"]]
- 007fcd38 ["CALL", null, ["ram:47acb4:8"]]
+ 007fcd78 ["INT_ADD", "register:40f0:8", ["const:7fcd78:8", "const:4:8"]]
+ 007fcd78 ["CALL", null, ["ram:47acf4:8"]]
- 007fcd38 bytes dff7f197
+ 007fcd78 bytes dff7f197
- 007fcd44 ["INT_ADD", "register:40f0:8", ["const:7fcd44:8", "const:4:8"]]
- 007fcd44 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fcd84 ["INT_ADD", "register:40f0:8", ["const:7fcd84:8", "const:4:8"]]
+ 007fcd84 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fcd44 bytes 1400f297
+ 007fcd84 bytes 1400f297
~~~


<a id="compare-e167970785a4aa1d91c58bd9edb1edff"></a>

### [`007fcd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd88.md) → [`007fcdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md) FUN_007fcdc8

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
      "definition_site": "007fcde8",
      "incomplete_value": false,
      "site": "007fcdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcda8",
      "incomplete_value": false,
      "site": "007fcdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "007fcdec",
      "DATA",
      [
        "storage",
        "00c7d3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcdec",
      "DATA",
      [
        "storage",
        "00c7d7b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd88.md#insn-007fcd9c) · [`007fcda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcd88.md#insn-007fcda8)
- 新版 [`007fcddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md#insn-007fcddc) · [`007fcde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcdc8.md#insn-007fcde8)

~~~diff
- 007fcd9c ["INT_ADD", "register:40f0:8", ["const:7fcd9c:8", "const:4:8"]]
- 007fcd9c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcddc ["INT_ADD", "register:40f0:8", ["const:7fcddc:8", "const:4:8"]]
+ 007fcddc ["CALL", null, ["callee:00c57e90:8"]]
- 007fcd9c bytes 3d6b1194
+ 007fcddc bytes 2d6c1194
- 007fcda8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007fcda8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcda8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcda8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcde8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 007fcde8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcde8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcde8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcda8 bytes 08c10e91
+ 007fcde8 bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca192664d22dd8b097e7703e3a2517e"></a>

### [`007fcde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcde0.md) → [`007fce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md) FUN_007fce20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fce44",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fce04",
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
      "007fce44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fce44",
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

- 旧版 [`007fce04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcde0.md#insn-007fce04) · [`007fce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcde0.md#insn-007fce10)
- 新版 [`007fce44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md#insn-007fce44) · [`007fce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce20.md#insn-007fce50)

~~~diff
- 007fce04 ["INT_ADD", "register:40f0:8", ["const:7fce04:8", "const:4:8"]]
- 007fce04 ["CALL", null, ["ram:47acb4:8"]]
+ 007fce44 ["INT_ADD", "register:40f0:8", ["const:7fce44:8", "const:4:8"]]
+ 007fce44 ["CALL", null, ["ram:47acf4:8"]]
- 007fce04 bytes acf7f197
+ 007fce44 bytes acf7f197
- 007fce10 ["INT_ADD", "register:40f0:8", ["const:7fce10:8", "const:4:8"]]
- 007fce10 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fce50 ["INT_ADD", "register:40f0:8", ["const:7fce50:8", "const:4:8"]]
+ 007fce50 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fce10 bytes e1fff197
+ 007fce50 bytes e1fff197
~~~


<a id="compare-328bbd89db5d3d38e014dfa37e9b22af"></a>

### [`007fce54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fce54.md) → [`007fce94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md) FUN_007fce94

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
      "definition_site": "007fceb4",
      "incomplete_value": false,
      "site": "007fceb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fce74",
      "incomplete_value": false,
      "site": "007fce78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "007fceb8",
      "DATA",
      [
        "storage",
        "00c7d430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fceb8",
      "DATA",
      [
        "storage",
        "00c7d830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fce68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fce54.md#insn-007fce68) · [`007fce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fce54.md#insn-007fce74)
- 新版 [`007fcea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md#insn-007fcea8) · [`007fceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fce94.md#insn-007fceb4)

~~~diff
- 007fce68 ["INT_ADD", "register:40f0:8", ["const:7fce68:8", "const:4:8"]]
- 007fce68 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcea8 ["INT_ADD", "register:40f0:8", ["const:7fcea8:8", "const:4:8"]]
+ 007fcea8 ["CALL", null, ["callee:00c57e90:8"]]
- 007fce68 bytes 0a6b1194
+ 007fcea8 bytes fa6b1194
- 007fce74 ["COPY", "tmp:0:8", ["const:430:8"]]
- 007fce74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fce74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fce74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fceb4 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 007fceb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fceb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fceb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fce74 bytes 08c11091
+ 007fceb4 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02afaafc676724848456c153559ced8"></a>

### [`007fceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fceac.md) → [`007fceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md) FUN_007fceec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "site": "007fcf14",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fced4",
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
      "007fcf14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fcf14",
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

- 旧版 [`007fced4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fceac.md#insn-007fced4) · [`007fcee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fceac.md#insn-007fcee0)
- 新版 [`007fcf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md#insn-007fcf14) · [`007fcf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md#insn-007fcf20)

~~~diff
- 007fced4 ["INT_ADD", "register:40f0:8", ["const:7fced4:8", "const:4:8"]]
- 007fced4 ["CALL", null, ["ram:47acb4:8"]]
+ 007fcf14 ["INT_ADD", "register:40f0:8", ["const:7fcf14:8", "const:4:8"]]
+ 007fcf14 ["CALL", null, ["ram:47acf4:8"]]
- 007fced4 bytes 78f7f197
+ 007fcf14 bytes 78f7f197
- 007fcee0 ["INT_ADD", "register:40f0:8", ["const:7fcee0:8", "const:4:8"]]
- 007fcee0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fcf20 ["INT_ADD", "register:40f0:8", ["const:7fcf20:8", "const:4:8"]]
+ 007fcf20 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fcee0 bytes adfff197
+ 007fcf20 bytes adfff197
~~~


<a id="compare-d26d0c946577ca622080abf6d89b4ac7"></a>

### [`007fcf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf44.md) → [`007fcf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md) FUN_007fcf84

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
      "definition_site": "007fcfa4",
      "incomplete_value": false,
      "site": "007fcfa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fcf64",
      "incomplete_value": false,
      "site": "007fcf68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "007fcfa8",
      "DATA",
      [
        "storage",
        "00c7d4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fcfa8",
      "DATA",
      [
        "storage",
        "00c7d8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf44.md#insn-007fcf58) · [`007fcf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf44.md#insn-007fcf64)
- 新版 [`007fcf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md#insn-007fcf98) · [`007fcfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcf84.md#insn-007fcfa4)

~~~diff
- 007fcf58 ["INT_ADD", "register:40f0:8", ["const:7fcf58:8", "const:4:8"]]
- 007fcf58 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fcf98 ["INT_ADD", "register:40f0:8", ["const:7fcf98:8", "const:4:8"]]
+ 007fcf98 ["CALL", null, ["callee:00c57e90:8"]]
- 007fcf58 bytes ce6a1194
+ 007fcf98 bytes be6b1194
- 007fcf64 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007fcf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fcf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fcf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fcfa4 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 007fcfa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcfa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fcfa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fcf64 bytes 08c11291
+ 007fcfa4 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf83274dd6522ede69d6cca498e5b84e"></a>

### [`007fcf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf9c.md) → [`007fcfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md) FUN_007fcfdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "site": "007fd004",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fcfc4",
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
      "007fd004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fd004",
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

- 旧版 [`007fcfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf9c.md#insn-007fcfc4) · [`007fcfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf9c.md#insn-007fcfd0)
- 新版 [`007fd004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md#insn-007fd004) · [`007fd010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md#insn-007fd010)

~~~diff
- 007fcfc4 ["INT_ADD", "register:40f0:8", ["const:7fcfc4:8", "const:4:8"]]
- 007fcfc4 ["CALL", null, ["ram:47acb4:8"]]
+ 007fd004 ["INT_ADD", "register:40f0:8", ["const:7fd004:8", "const:4:8"]]
+ 007fd004 ["CALL", null, ["ram:47acf4:8"]]
- 007fcfc4 bytes 3cf7f197
+ 007fd004 bytes 3cf7f197
- 007fcfd0 ["INT_ADD", "register:40f0:8", ["const:7fcfd0:8", "const:4:8"]]
- 007fcfd0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fd010 ["INT_ADD", "register:40f0:8", ["const:7fd010:8", "const:4:8"]]
+ 007fd010 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fcfd0 bytes 71fff197
+ 007fd010 bytes 71fff197
~~~


<a id="compare-abdb7596973216a74f74f9d5b1687e28"></a>

### [`007fd034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd034.md) → [`007fd074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md) FUN_007fd074

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
      "definition_site": "007fd088",
      "incomplete_value": false,
      "site": "007fd08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd048",
      "incomplete_value": false,
      "site": "007fd04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "007fd08c",
      "DATA",
      [
        "storage",
        "00c7d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd08c",
      "DATA",
      [
        "storage",
        "00c7d930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd034.md#insn-007fd040) · [`007fd048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd034.md#insn-007fd048)
- 新版 [`007fd080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md#insn-007fd080) · [`007fd088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd074.md#insn-007fd088)

~~~diff
- 007fd040 ["INT_ADD", "register:40f0:8", ["const:7fd040:8", "const:4:8"]]
- 007fd040 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fd080 ["INT_ADD", "register:40f0:8", ["const:7fd080:8", "const:4:8"]]
+ 007fd080 ["CALL", null, ["callee:00c57e90:8"]]
- 007fd040 bytes 946a1194
+ 007fd080 bytes 846b1194
- 007fd048 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007fd048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd088 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 007fd088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd048 bytes 08c11491
+ 007fd088 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-248744082689b939a6f2e0bb6b85fb1e"></a>

### [`007fd070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd070.md) → [`007fd0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md) FUN_007fd0b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fd0d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd094",
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
      "007fd0d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fd0d4",
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

- 旧版 [`007fd094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd070.md#insn-007fd094) · [`007fd0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd070.md#insn-007fd0a0)
- 新版 [`007fd0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md#insn-007fd0d4) · [`007fd0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd0b0.md#insn-007fd0e0)

~~~diff
- 007fd094 ["INT_ADD", "register:40f0:8", ["const:7fd094:8", "const:4:8"]]
- 007fd094 ["CALL", null, ["ram:47acb4:8"]]
+ 007fd0d4 ["INT_ADD", "register:40f0:8", ["const:7fd0d4:8", "const:4:8"]]
+ 007fd0d4 ["CALL", null, ["ram:47acf4:8"]]
- 007fd094 bytes 08f7f197
+ 007fd0d4 bytes 08f7f197
- 007fd0a0 ["INT_ADD", "register:40f0:8", ["const:7fd0a0:8", "const:4:8"]]
- 007fd0a0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fd0e0 ["INT_ADD", "register:40f0:8", ["const:7fd0e0:8", "const:4:8"]]
+ 007fd0e0 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fd0a0 bytes 3dfff197
+ 007fd0e0 bytes 3dfff197
~~~


<a id="compare-63eb8389c457abea5da922157d77e17a"></a>

### [`007fd0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd0e4.md) → [`007fd124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md) FUN_007fd124

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007fd148",
      "incomplete_value": false,
      "site": "007fd14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd108",
      "incomplete_value": false,
      "site": "007fd10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007fd14c",
      "DATA",
      [
        "storage",
        "00c7d5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd14c",
      "DATA",
      [
        "storage",
        "00c7d9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd0e4.md#insn-007fd0f8) · [`007fd108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd0e4.md#insn-007fd108)
- 新版 [`007fd138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md#insn-007fd138) · [`007fd148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd124.md#insn-007fd148)

~~~diff
- 007fd0f8 ["INT_ADD", "register:40f0:8", ["const:7fd0f8:8", "const:4:8"]]
- 007fd0f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fd138 ["INT_ADD", "register:40f0:8", ["const:7fd138:8", "const:4:8"]]
+ 007fd138 ["CALL", null, ["callee:00c57e90:8"]]
- 007fd0f8 bytes 666a1194
+ 007fd138 bytes 566b1194
- 007fd108 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007fd108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd148 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 007fd148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd108 bytes 08c11691
+ 007fd148 bytes 08c12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea3dcfb97b5499cef3bfa0b12b7dd12f"></a>

### [`007fd2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd2e4.md) → [`007fd324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md) FUN_007fd324

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
      "definition_site": "007fd344",
      "incomplete_value": false,
      "site": "007fd348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd304",
      "incomplete_value": false,
      "site": "007fd308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "007fd348",
      "DATA",
      [
        "storage",
        "00c7d630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd348",
      "DATA",
      [
        "storage",
        "00c7da30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd2e4.md#insn-007fd2f8) · [`007fd304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd2e4.md#insn-007fd304)
- 新版 [`007fd338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md#insn-007fd338) · [`007fd344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd324.md#insn-007fd344)

~~~diff
- 007fd2f8 ["INT_ADD", "register:40f0:8", ["const:7fd2f8:8", "const:4:8"]]
- 007fd2f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fd338 ["INT_ADD", "register:40f0:8", ["const:7fd338:8", "const:4:8"]]
+ 007fd338 ["CALL", null, ["callee:00c57e90:8"]]
- 007fd2f8 bytes e6691194
+ 007fd338 bytes d66a1194
- 007fd304 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007fd304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd344 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 007fd344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd304 bytes 08c11891
+ 007fd344 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a32d37fdd3ea11ef27c548fef052f2"></a>

### [`007fd33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md) → [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) FUN_007fd37c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) [`007fd5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5a8.md) [`007fd5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5ac.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`007fd5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5e8.md) [`007fd5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5ec.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd424",
      "incomplete_value": false,
      "site": "007fd424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd3e4",
      "incomplete_value": false,
      "site": "007fd3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "007fd474",
      "incomplete_value": true,
      "site": "007fd474",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:16c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd434",
      "incomplete_value": true,
      "site": "007fd434",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:12c:8"
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
      "site": "007fd3bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fd37c",
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
      "007fd3bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fd40c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fd424",
      "DATA",
      [
        "storage",
        "00c7d6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd3bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd40c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd424",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md#insn-007fd37c) · [`007fd3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md#insn-007fd3cc) · [`007fd388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd33c.md#insn-007fd388)
- 新版 [`007fd3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd3bc) · [`007fd40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd40c) · [`007fd3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md#insn-007fd3c8)

~~~diff
- 007fd37c ["INT_ADD", "register:40f0:8", ["const:7fd37c:8", "const:4:8"]]
- 007fd37c ["CALL", null, ["ram:47acb4:8"]]
+ 007fd3bc ["INT_ADD", "register:40f0:8", ["const:7fd3bc:8", "const:4:8"]]
+ 007fd3bc ["CALL", null, ["ram:47acf4:8"]]
- 007fd37c bytes 4ef6f197
+ 007fd3bc bytes 4ef6f197
- 007fd3cc ["INT_ADD", "register:40f0:8", ["const:7fd3cc:8", "const:4:8"]]
- 007fd3cc ["CALL", null, ["ram:47acb4:8"]]
+ 007fd40c ["INT_ADD", "register:40f0:8", ["const:7fd40c:8", "const:4:8"]]
+ 007fd40c ["CALL", null, ["ram:47acf4:8"]]
- 007fd3cc bytes 3af6f197
+ 007fd40c bytes 3af6f197
- 007fd388 ["INT_ADD", "register:40f0:8", ["const:7fd388:8", "const:4:8"]]
- 007fd388 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fd3c8 ["INT_ADD", "register:40f0:8", ["const:7fd3c8:8", "const:4:8"]]
+ 007fd3c8 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fd388 bytes 83fef197
+ 007fd3c8 bytes 83fef197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a0c9f6c54c417e1c9949e66b73b8cd"></a>

### [`007fd558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd558.md) → [`007fd598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md) FUN_007fd598

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
      "definition_site": "007fd5b8",
      "incomplete_value": false,
      "site": "007fd5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd578",
      "incomplete_value": false,
      "site": "007fd57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "007fd5bc",
      "DATA",
      [
        "storage",
        "00c7d6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd5bc",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd558.md#insn-007fd56c) · [`007fd578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd558.md#insn-007fd578)
- 新版 [`007fd5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md#insn-007fd5ac) · [`007fd5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd598.md#insn-007fd5b8)

~~~diff
- 007fd56c ["INT_ADD", "register:40f0:8", ["const:7fd56c:8", "const:4:8"]]
- 007fd56c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fd5ac ["INT_ADD", "register:40f0:8", ["const:7fd5ac:8", "const:4:8"]]
+ 007fd5ac ["CALL", null, ["callee:00c57e90:8"]]
- 007fd56c bytes 49691194
+ 007fd5ac bytes 396a1194
- 007fd578 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 007fd578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd5b8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 007fd5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd578 bytes 08811a91
+ 007fd5b8 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f40600e7f763816b436cd40562ed02"></a>

### [`007fd590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd590.md) → [`007fd5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5d0.md) FUN_007fd5d0

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
      "definition_site": "007fd5d4",
      "incomplete_value": false,
      "site": "007fd5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd594",
      "incomplete_value": false,
      "site": "007fd598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "007fd5d8",
      "DATA",
      [
        "storage",
        "00c7d6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fd5d8",
      "DATA",
      [
        "storage",
        "00c7daa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd590.md#insn-007fd594)
- 新版 [`007fd5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5d0.md#insn-007fd5d4)

~~~diff
- 007fd594 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 007fd594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fd594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fd594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fd5d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 007fd5d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd5d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fd5d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fd594 bytes 08811a91
+ 007fd5d4 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f298134913cab134ebca0915b09395c9"></a>

### [`007fd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md) → [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) FUN_007fd5f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md)
- 新版 呼出元 0件  · 呼出先 23件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.67% / 新版 88.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd728",
      "incomplete_value": true,
      "site": "007fd728",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd6e8",
      "incomplete_value": true,
      "site": "007fd6e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
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
      "definition_site": "007fd72c",
      "incomplete_value": true,
      "site": "007fd72c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007fd6ec",
      "incomplete_value": true,
      "site": "007fd6ec",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fd790",
      "incomplete_value": true,
      "site": "007fd7a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fd750",
      "incomplete_value": true,
      "site": "007fd764",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d0:8"
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
      "007fd64c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fd65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84b90"
      ]
    ],
    [
      "007fd6b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84b90"
      ]
    ]
  ],
  "added": [
    [
      "007fd64c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fd65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ],
    [
      "007fd6b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fd60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md#insn-007fd60c) · [`007fd61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md#insn-007fd61c) · [`007fd670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fd5b0.md#insn-007fd670)
- 新版 [`007fd64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd64c) · [`007fd65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd65c) · [`007fd6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md#insn-007fd6b0)

~~~diff
- 007fd60c ["INT_ADD", "register:40f0:8", ["const:7fd60c:8", "const:4:8"]]
- 007fd60c ["CALL", null, ["ram:47acb4:8"]]
+ 007fd64c ["INT_ADD", "register:40f0:8", ["const:7fd64c:8", "const:4:8"]]
+ 007fd64c ["CALL", null, ["ram:47acf4:8"]]
- 007fd60c bytes aaf5f197
+ 007fd64c bytes aaf5f197
- 007fd61c ["INT_ADD", "register:40f0:8", ["const:7fd61c:8", "const:4:8"]]
- 007fd61c ["CALL", null, ["ram:a84b90:8"]]
+ 007fd65c ["INT_ADD", "register:40f0:8", ["const:7fd65c:8", "const:4:8"]]
+ 007fd65c ["CALL", null, ["ram:a84d88:8"]]
- 007fd61c bytes 5d1d0a94
+ 007fd65c bytes cb1d0a94
- 007fd670 ["INT_ADD", "register:40f0:8", ["const:7fd670:8", "const:4:8"]]
- 007fd670 ["CALL", null, ["ram:a84b90:8"]]
+ 007fd6b0 ["INT_ADD", "register:40f0:8", ["const:7fd6b0:8", "const:4:8"]]
+ 007fd6b0 ["CALL", null, ["ram:a84d88:8"]]
- 007fd670 bytes 481d0a94
+ 007fd6b0 bytes b61d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e27167fadd7562ad1da1c9e55987d21"></a>

### [`007fdbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdbe0.md) → [`007fdc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md) FUN_007fdc20

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
      "definition_site": "007fdc34",
      "incomplete_value": false,
      "site": "007fdc38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdbf4",
      "incomplete_value": false,
      "site": "007fdbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "007fdc38",
      "DATA",
      [
        "storage",
        "00c7d710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdc38",
      "DATA",
      [
        "storage",
        "00c7db10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdbe0.md#insn-007fdbec) · [`007fdbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdbe0.md#insn-007fdbf4)
- 新版 [`007fdc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md#insn-007fdc2c) · [`007fdc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc20.md#insn-007fdc34)

~~~diff
- 007fdbec ["INT_ADD", "register:40f0:8", ["const:7fdbec:8", "const:4:8"]]
- 007fdbec ["CALL", null, ["callee:00c57e90:8"]]
+ 007fdc2c ["INT_ADD", "register:40f0:8", ["const:7fdc2c:8", "const:4:8"]]
+ 007fdc2c ["CALL", null, ["callee:00c57e90:8"]]
- 007fdbec bytes a9671194
+ 007fdc2c bytes 99681194
- 007fdbf4 ["COPY", "tmp:0:8", ["const:710:8"]]
- 007fdbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdc34 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 007fdc34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdc34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdc34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdbf4 bytes 08411c91
+ 007fdc34 bytes 08412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac95e37ceef4e4bcc6e153949882b6f"></a>

### [`007fdc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc1c.md) → [`007fdc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md) FUN_007fdc5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fdc80",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdc40",
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
      "007fdc80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fdc80",
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

- 旧版 [`007fdc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc1c.md#insn-007fdc40) · [`007fdc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc1c.md#insn-007fdc4c)
- 新版 [`007fdc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md#insn-007fdc80) · [`007fdc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdc5c.md#insn-007fdc8c)

~~~diff
- 007fdc40 ["INT_ADD", "register:40f0:8", ["const:7fdc40:8", "const:4:8"]]
- 007fdc40 ["CALL", null, ["ram:47acb4:8"]]
+ 007fdc80 ["INT_ADD", "register:40f0:8", ["const:7fdc80:8", "const:4:8"]]
+ 007fdc80 ["CALL", null, ["ram:47acf4:8"]]
- 007fdc40 bytes 1df4f197
+ 007fdc80 bytes 1df4f197
- 007fdc4c ["INT_ADD", "register:40f0:8", ["const:7fdc4c:8", "const:4:8"]]
- 007fdc4c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fdc8c ["INT_ADD", "register:40f0:8", ["const:7fdc8c:8", "const:4:8"]]
+ 007fdc8c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fdc4c bytes 52fcf197
+ 007fdc8c bytes 52fcf197
~~~


<a id="compare-a80c9b5421c94bc74389b690674975ce"></a>

### [`007fdc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc90.md) → [`007fdcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md) FUN_007fdcd0

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
      "definition_site": "007fdce4",
      "incomplete_value": false,
      "site": "007fdce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdca4",
      "incomplete_value": false,
      "site": "007fdca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "007fdce8",
      "DATA",
      [
        "storage",
        "00c7d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdce8",
      "DATA",
      [
        "storage",
        "00c7db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc90.md#insn-007fdc9c) · [`007fdca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdc90.md#insn-007fdca4)
- 新版 [`007fdcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md#insn-007fdcdc) · [`007fdce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcd0.md#insn-007fdce4)

~~~diff
- 007fdc9c ["INT_ADD", "register:40f0:8", ["const:7fdc9c:8", "const:4:8"]]
- 007fdc9c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fdcdc ["INT_ADD", "register:40f0:8", ["const:7fdcdc:8", "const:4:8"]]
+ 007fdcdc ["CALL", null, ["callee:00c57e90:8"]]
- 007fdc9c bytes 7d671194
+ 007fdcdc bytes 6d681194
- 007fdca4 ["COPY", "tmp:0:8", ["const:790:8"]]
- 007fdca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdce4 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 007fdce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdca4 bytes 08411e91
+ 007fdce4 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f3d65b4300d198bb23afd99443958d"></a>

### [`007fdcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdcb4.md) → [`007fdcf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcf4.md) FUN_007fdcf4

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
      "definition_site": "007fdcf8",
      "incomplete_value": false,
      "site": "007fdcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdcb8",
      "incomplete_value": false,
      "site": "007fdcbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "007fdcfc",
      "DATA",
      [
        "storage",
        "00c7d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdcfc",
      "DATA",
      [
        "storage",
        "00c7db90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdcb4.md#insn-007fdcb8)
- 新版 [`007fdcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdcf4.md#insn-007fdcf8)

~~~diff
- 007fdcb8 ["COPY", "tmp:0:8", ["const:790:8"]]
- 007fdcb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdcb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdcb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdcf8 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 007fdcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdcb8 bytes 08411e91
+ 007fdcf8 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58ca30c7f757c0b40dfa43ab93cbfec0"></a>

### [`007fdccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdccc.md) → [`007fdd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md) FUN_007fdd0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007fdd30",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdcf0",
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
      "007fdd30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fdd30",
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

- 旧版 [`007fdcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdccc.md#insn-007fdcf0) · [`007fdcfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdccc.md#insn-007fdcfc)
- 新版 [`007fdd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md#insn-007fdd30) · [`007fdd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md#insn-007fdd3c)

~~~diff
- 007fdcf0 ["INT_ADD", "register:40f0:8", ["const:7fdcf0:8", "const:4:8"]]
- 007fdcf0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fdd30 ["INT_ADD", "register:40f0:8", ["const:7fdd30:8", "const:4:8"]]
+ 007fdd30 ["CALL", null, ["ram:47acf4:8"]]
- 007fdcf0 bytes f1f3f197
+ 007fdd30 bytes f1f3f197
- 007fdcfc ["INT_ADD", "register:40f0:8", ["const:7fdcfc:8", "const:4:8"]]
- 007fdcfc ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fdd3c ["INT_ADD", "register:40f0:8", ["const:7fdd3c:8", "const:4:8"]]
+ 007fdd3c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fdcfc bytes 26fcf197
+ 007fdd3c bytes 26fcf197
~~~


<a id="compare-1072dcb96c8c3bec4d32888351241f9a"></a>

### [`007fdd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd40.md) → [`007fdd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md) FUN_007fdd80

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
      "definition_site": "007fdda0",
      "incomplete_value": false,
      "site": "007fdda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdd60",
      "incomplete_value": false,
      "site": "007fdd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007fdda4",
      "DATA",
      [
        "storage",
        "00c7d830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdda4",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd40.md#insn-007fdd54) · [`007fdd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd40.md#insn-007fdd60)
- 新版 [`007fdd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md#insn-007fdd94) · [`007fdda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd80.md#insn-007fdda0)

~~~diff
- 007fdd54 ["INT_ADD", "register:40f0:8", ["const:7fdd54:8", "const:4:8"]]
- 007fdd54 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fdd94 ["INT_ADD", "register:40f0:8", ["const:7fdd94:8", "const:4:8"]]
+ 007fdd94 ["CALL", null, ["callee:00c57e90:8"]]
- 007fdd54 bytes 4f671194
+ 007fdd94 bytes 3f681194
- 007fdd60 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007fdd60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdd60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdd60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdda0 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 007fdda0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdda0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdda0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdd60 bytes 08c12091
+ 007fdda0 bytes 08c13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ee35dde1509d7525cb3e37e91c9933d"></a>

### [`007fdd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd98.md) → [`007fddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md) FUN_007fddd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "site": "007fde00",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fddc0",
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
      "007fde00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fde00",
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

- 旧版 [`007fddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd98.md#insn-007fddc0) · [`007fddcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd98.md#insn-007fddcc) · [`007fddf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdd98.md#insn-007fddf0)
- 新版 [`007fde00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde00) · [`007fde0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde0c) · [`007fde30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fddd8.md#insn-007fde30)

~~~diff
- 007fddc0 ["INT_ADD", "register:40f0:8", ["const:7fddc0:8", "const:4:8"]]
- 007fddc0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fde00 ["INT_ADD", "register:40f0:8", ["const:7fde00:8", "const:4:8"]]
+ 007fde00 ["CALL", null, ["ram:47acf4:8"]]
- 007fddc0 bytes bdf3f197
+ 007fde00 bytes bdf3f197
- 007fddcc ["INT_ADD", "register:40f0:8", ["const:7fddcc:8", "const:4:8"]]
- 007fddcc ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fde0c ["INT_ADD", "register:40f0:8", ["const:7fde0c:8", "const:4:8"]]
+ 007fde0c ["CALL", null, ["callee:0047cdd4:8"]]
- 007fddcc bytes f2fbf197
+ 007fde0c bytes f2fbf197
- 007fddf0 ["INT_ADD", "register:40f0:8", ["const:7fddf0:8", "const:4:8"]]
- 007fddf0 ["CALL", null, ["callee:008514f8:8"]]
+ 007fde30 ["INT_ADD", "register:40f0:8", ["const:7fde30:8", "const:4:8"]]
+ 007fde30 ["CALL", null, ["callee:008514f8:8"]]
- 007fddf0 bytes b24d0194
+ 007fde30 bytes b24d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e263720f42d38fc1c64852fc6810738e"></a>

### [`007fde74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fde74.md) → [`007fdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md) FUN_007fdeb4

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
      "definition_site": "007fdec8",
      "incomplete_value": false,
      "site": "007fdecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fde88",
      "incomplete_value": false,
      "site": "007fde8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "007fdecc",
      "DATA",
      [
        "storage",
        "00c7d8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdecc",
      "DATA",
      [
        "storage",
        "00c7dcb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fde80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fde74.md#insn-007fde80) · [`007fde88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fde74.md#insn-007fde88)
- 新版 [`007fdec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md#insn-007fdec0) · [`007fdec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdeb4.md#insn-007fdec8)

~~~diff
- 007fde80 ["INT_ADD", "register:40f0:8", ["const:7fde80:8", "const:4:8"]]
- 007fde80 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fdec0 ["INT_ADD", "register:40f0:8", ["const:7fdec0:8", "const:4:8"]]
+ 007fdec0 ["CALL", null, ["callee:00c57e90:8"]]
- 007fde80 bytes 04671194
+ 007fdec0 bytes f4671194
- 007fde88 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007fde88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fde88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fde88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdec8 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 007fdec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fde88 bytes 08c12291
+ 007fdec8 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c614ae79b2616556d9cef8e6a142a040"></a>

### [`007fdeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdeb0.md) → [`007fdef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md) FUN_007fdef0

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
      "site": "007fdf0c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdecc",
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
      "007fdf0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fdf0c",
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

- 旧版 [`007fdecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdeb0.md#insn-007fdecc) · [`007fded8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdeb0.md#insn-007fded8)
- 新版 [`007fdf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md#insn-007fdf0c) · [`007fdf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdef0.md#insn-007fdf18)

~~~diff
- 007fdecc ["INT_ADD", "register:40f0:8", ["const:7fdecc:8", "const:4:8"]]
- 007fdecc ["CALL", null, ["ram:47acb4:8"]]
+ 007fdf0c ["INT_ADD", "register:40f0:8", ["const:7fdf0c:8", "const:4:8"]]
+ 007fdf0c ["CALL", null, ["ram:47acf4:8"]]
- 007fdecc bytes 7af3f197
+ 007fdf0c bytes 7af3f197
- 007fded8 ["INT_ADD", "register:40f0:8", ["const:7fded8:8", "const:4:8"]]
- 007fded8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007fdf18 ["INT_ADD", "register:40f0:8", ["const:7fdf18:8", "const:4:8"]]
+ 007fdf18 ["CALL", null, ["callee:0047cdd4:8"]]
- 007fded8 bytes affbf197
+ 007fdf18 bytes affbf197
~~~


<a id="compare-9c4e45ca23cbee9f29b71736bc97e799"></a>

### [`007fdf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf1c.md) → [`007fdf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md) FUN_007fdf5c

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
      "definition_site": "007fdf80",
      "incomplete_value": false,
      "site": "007fdf80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fdf40",
      "incomplete_value": false,
      "site": "007fdf40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "007fdf80",
      "DATA",
      [
        "storage",
        "00c7d930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fdf80",
      "DATA",
      [
        "storage",
        "00c7dd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fdf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf1c.md#insn-007fdf30) · [`007fdf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf1c.md#insn-007fdf3c)
- 新版 [`007fdf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md#insn-007fdf70) · [`007fdf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdf5c.md#insn-007fdf7c)

~~~diff
- 007fdf30 ["INT_ADD", "register:40f0:8", ["const:7fdf30:8", "const:4:8"]]
- 007fdf30 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fdf70 ["INT_ADD", "register:40f0:8", ["const:7fdf70:8", "const:4:8"]]
+ 007fdf70 ["CALL", null, ["callee:00c57e90:8"]]
- 007fdf30 bytes d8661194
+ 007fdf70 bytes c8671194
- 007fdf3c ["COPY", "tmp:0:8", ["const:930:8"]]
- 007fdf3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fdf3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fdf3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fdf7c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 007fdf7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fdf7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fdf3c bytes 08c12491
+ 007fdf7c bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4ab41f40278c8264a6b533627d55fc"></a>

### [`007fdf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md) → [`007fdfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md) FUN_007fdfac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "007fe000",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fdfc0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007fe048",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fe008",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007fe000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fe048",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fe000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fe048",
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

- 旧版 [`007fdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md#insn-007fdfc0) · [`007fe008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md#insn-007fe008) · [`007fdf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fd/007fdf6c.md#insn-007fdf90)
- 新版 [`007fe000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fe000) · [`007fe048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fe048) · [`007fdfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdfac.md#insn-007fdfd0)

~~~diff
- 007fdfc0 ["INT_ADD", "register:40f0:8", ["const:7fdfc0:8", "const:4:8"]]
- 007fdfc0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fe000 ["INT_ADD", "register:40f0:8", ["const:7fe000:8", "const:4:8"]]
+ 007fe000 ["CALL", null, ["ram:47acf4:8"]]
- 007fdfc0 bytes 3df3f197
+ 007fe000 bytes 3df3f197
- 007fe008 ["INT_ADD", "register:40f0:8", ["const:7fe008:8", "const:4:8"]]
- 007fe008 ["CALL", null, ["ram:47acb4:8"]]
+ 007fe048 ["INT_ADD", "register:40f0:8", ["const:7fe048:8", "const:4:8"]]
+ 007fe048 ["CALL", null, ["ram:47acf4:8"]]
- 007fe008 bytes 2bf3f197
+ 007fe048 bytes 2bf3f197
- 007fdf90 ["INT_ADD", "register:40f0:8", ["const:7fdf90:8", "const:4:8"]]
- 007fdf90 ["CALL", null, ["callee:008b9298:8"]]
+ 007fdfd0 ["INT_ADD", "register:40f0:8", ["const:7fdfd0:8", "const:4:8"]]
+ 007fdfd0 ["CALL", null, ["callee:008b9298:8"]]
- 007fdf90 bytes b1ec0294
+ 007fdfd0 bytes b2ec0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c28871a1a479a1c06210df591683d5f"></a>

### [`007fe068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe068.md) → [`007fe0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md) FUN_007fe0a8

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
      "definition_site": "007fe0c8",
      "incomplete_value": false,
      "site": "007fe0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe088",
      "incomplete_value": false,
      "site": "007fe08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "007fe0cc",
      "DATA",
      [
        "storage",
        "00c7d9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe0cc",
      "DATA",
      [
        "storage",
        "00c7ddb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe068.md#insn-007fe07c) · [`007fe088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe068.md#insn-007fe088)
- 新版 [`007fe0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md#insn-007fe0bc) · [`007fe0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe0a8.md#insn-007fe0c8)

~~~diff
- 007fe07c ["INT_ADD", "register:40f0:8", ["const:7fe07c:8", "const:4:8"]]
- 007fe07c ["CALL", null, ["callee:00c57e90:8"]]
+ 007fe0bc ["INT_ADD", "register:40f0:8", ["const:7fe0bc:8", "const:4:8"]]
+ 007fe0bc ["CALL", null, ["callee:00c57e90:8"]]
- 007fe07c bytes 85661194
+ 007fe0bc bytes 75671194
- 007fe088 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007fe088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fe088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fe088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fe0c8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 007fe0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fe088 bytes 08c12691
+ 007fe0c8 bytes 08c13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e268ff205a933fe6be932dcff6e1a1da"></a>

### [`007fe0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe0c0.md) → [`007fe100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe100.md) FUN_007fe100

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.28% / 新版 96.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007fe15c",
      "incomplete_value": true,
      "site": "007fe15c",
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
      "definition_site": "007fe11c",
      "incomplete_value": true,
      "site": "007fe11c",
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
      "definition_site": "007fe164",
      "incomplete_value": false,
      "site": "007fe174",
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
      "definition_site": "007fe124",
      "incomplete_value": false,
      "site": "007fe134",
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
      "definition_site": "007fe16c",
      "incomplete_value": false,
      "site": "007fe174",
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
      "definition_site": "007fe12c",
      "incomplete_value": false,
      "site": "007fe134",
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
      "007fe158",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007fe164",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fe16c",
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
      "007fe158",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007fe164",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007fe16c",
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

- 旧版 [`007fe134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe0c0.md#insn-007fe134) · [`007fe160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe0c0.md#insn-007fe160) · [`007fe238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe0c0.md#insn-007fe238)
- 新版 [`007fe174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe100.md#insn-007fe174) · [`007fe1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe100.md#insn-007fe1a0) · [`007fe278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe100.md#insn-007fe278)

~~~diff
- 007fe134 ["INT_ADD", "register:40f0:8", ["const:7fe134:8", "const:4:8"]]
- 007fe134 ["CALL", null, ["callee:00c58610:8"]]
+ 007fe174 ["INT_ADD", "register:40f0:8", ["const:7fe174:8", "const:4:8"]]
+ 007fe174 ["CALL", null, ["callee:00c58610:8"]]
- 007fe134 bytes 37681194
+ 007fe174 bytes 27691194
- 007fe160 ["INT_ADD", "register:40f0:8", ["const:7fe160:8", "const:4:8"]]
- 007fe160 ["CALL", null, ["ram:64d600:8"]]
+ 007fe1a0 ["INT_ADD", "register:40f0:8", ["const:7fe1a0:8", "const:4:8"]]
+ 007fe1a0 ["CALL", null, ["ram:64d640:8"]]
- 007fe160 bytes 283df997
+ 007fe1a0 bytes 283df997
- 007fe238 ["INT_ADD", "register:40f0:8", ["const:7fe238:8", "const:4:8"]]
- 007fe238 ["CALL", null, ["ram:46c984:8"]]
+ 007fe278 ["INT_ADD", "register:40f0:8", ["const:7fe278:8", "const:4:8"]]
+ 007fe278 ["CALL", null, ["ram:46c9c4:8"]]
- 007fe238 bytes d3b9f197
+ 007fe278 bytes d3b9f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-186b5e2420e8177da1aefa393bda0b44"></a>

### [`007fe4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe4b4.md) → [`007fe4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe4f4.md) FUN_007fe4f4

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
      "definition_site": "007fe518",
      "incomplete_value": false,
      "site": "007fe518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe4d8",
      "incomplete_value": false,
      "site": "007fe4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "007fe518",
      "DATA",
      [
        "storage",
        "00c7da30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe518",
      "DATA",
      [
        "storage",
        "00c7de30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe4b4.md#insn-007fe4c8) · [`007fe4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe4b4.md#insn-007fe4d4)
- 新版 [`007fe508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe4f4.md#insn-007fe508) · [`007fe514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe4f4.md#insn-007fe514)

~~~diff
- 007fe4c8 ["INT_ADD", "register:40f0:8", ["const:7fe4c8:8", "const:4:8"]]
- 007fe4c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fe508 ["INT_ADD", "register:40f0:8", ["const:7fe508:8", "const:4:8"]]
+ 007fe508 ["CALL", null, ["callee:00c57e90:8"]]
- 007fe4c8 bytes 72651194
+ 007fe508 bytes 62661194
- 007fe4d4 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007fe4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fe4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fe4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fe514 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 007fe514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fe4d4 bytes 08c12891
+ 007fe514 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e361eed3dd1746ead65678fcd70efe"></a>

### [`007fe504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe504.md) → [`007fe544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe544.md) FUN_007fe544

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

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
      "site": "007fe574",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007fe534",
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
      "007fe574",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007fe574",
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

- 旧版 [`007fe534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe504.md#insn-007fe534) · [`007fe530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe504.md#insn-007fe530)
- 新版 [`007fe574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe544.md#insn-007fe574) · [`007fe570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe544.md#insn-007fe570)

~~~diff
- 007fe534 ["INT_ADD", "register:40f0:8", ["const:7fe534:8", "const:4:8"]]
- 007fe534 ["CALL", null, ["ram:47acb4:8"]]
+ 007fe574 ["INT_ADD", "register:40f0:8", ["const:7fe574:8", "const:4:8"]]
+ 007fe574 ["CALL", null, ["ram:47acf4:8"]]
- 007fe534 bytes e0f1f197
+ 007fe574 bytes e0f1f197
- 007fe530 ["INT_ADD", "register:40f0:8", ["const:7fe530:8", "const:4:8"]]
- 007fe530 ["CALL", null, ["callee:008b9178:8"]]
+ 007fe570 ["INT_ADD", "register:40f0:8", ["const:7fe570:8", "const:4:8"]]
+ 007fe570 ["CALL", null, ["callee:008b9178:8"]]
- 007fe530 bytes 01eb0294
+ 007fe570 bytes 02eb0294
~~~


<a id="compare-f2e40e2fed8af90bfdebc12539d84b6b"></a>

### [`007fe57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe57c.md) → [`007fe5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe5bc.md) FUN_007fe5bc

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
      "definition_site": "007fe5c8",
      "incomplete_value": false,
      "site": "007fe5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe588",
      "incomplete_value": false,
      "site": "007fe58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fe5cc",
      "DATA",
      [
        "storage",
        "00c7dab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe5cc",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe57c.md#insn-007fe588)
- 新版 [`007fe5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe5bc.md#insn-007fe5c8)

~~~diff
- 007fe588 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007fe588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fe588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fe588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fe5c8 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007fe5c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe5c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe5c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fe588 bytes 29c12a91
+ 007fe5c8 bytes 29c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba421193cc81613765f9f870912387aa"></a>

### [`007fe5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5a0.md) → [`007fe5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe5e0.md) FUN_007fe5e0

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
      "definition_site": "007fe5e8",
      "incomplete_value": false,
      "site": "007fe5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe5a8",
      "incomplete_value": false,
      "site": "007fe5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fe5ec",
      "DATA",
      [
        "storage",
        "00c7dab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe5ec",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5a0.md#insn-007fe5a8) · [`007fe5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5a0.md#insn-007fe5cc)
- 新版 [`007fe5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe5e0.md#insn-007fe5e8) · [`007fe60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe5e0.md#insn-007fe60c)

~~~diff
- 007fe5a8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007fe5a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fe5a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fe5a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fe5e8 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007fe5e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe5e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fe5e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fe5a8 bytes 29c12a91
+ 007fe5e8 bytes 29c13a91
- 007fe5cc ["INT_ADD", "register:40f0:8", ["const:7fe5cc:8", "const:4:8"]]
- 007fe5cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 007fe60c ["INT_ADD", "register:40f0:8", ["const:7fe60c:8", "const:4:8"]]
+ 007fe60c ["CALL", null, ["callee:00c57eb0:8"]]
- 007fe5cc bytes 39651194
+ 007fe60c bytes 29661194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe426abf8c2e15d342387731cf92f80"></a>

### [`007fe5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5e0.md) → [`007fe620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe620.md) FUN_007fe620

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
      "definition_site": "007fe658",
      "incomplete_value": false,
      "site": "007fe658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe618",
      "incomplete_value": false,
      "site": "007fe618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "007fe658",
      "DATA",
      [
        "storage",
        "00c7dab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe658",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5e0.md#insn-007fe5fc) · [`007fe608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5e0.md#insn-007fe608) · [`007fe634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe5e0.md#insn-007fe634)
- 新版 [`007fe63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe620.md#insn-007fe63c) · [`007fe648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe620.md#insn-007fe648) · [`007fe674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe620.md#insn-007fe674)

~~~diff
- 007fe5fc ["INT_ADD", "register:40f0:8", ["const:7fe5fc:8", "const:4:8"]]
- 007fe5fc ["CALL", null, ["callee:00c57e90:8"]]
+ 007fe63c ["INT_ADD", "register:40f0:8", ["const:7fe63c:8", "const:4:8"]]
+ 007fe63c ["CALL", null, ["callee:00c57e90:8"]]
- 007fe5fc bytes 25651194
+ 007fe63c bytes 15661194
- 007fe608 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007fe608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fe608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fe608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fe648 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007fe648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fe648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fe608 bytes 08c12a91
+ 007fe648 bytes 08c13a91
- 007fe634 ["INT_ADD", "register:40f0:8", ["const:7fe634:8", "const:4:8"]]
- 007fe634 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fe674 ["INT_ADD", "register:40f0:8", ["const:7fe674:8", "const:4:8"]]
+ 007fe674 ["CALL", null, ["callee:00c57e90:8"]]
- 007fe634 bytes 17651194
+ 007fe674 bytes 07661194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad12405bdb2c0dd5ab3ef9e59fc78c39"></a>

### [`007fe6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe6a4.md) → [`007fe6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe6e4.md) FUN_007fe6e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
      "definition_site": "007fe71c",
      "incomplete_value": false,
      "site": "007fe71c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe6dc",
      "incomplete_value": false,
      "site": "007fe6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "007fe71c",
      "DATA",
      [
        "storage",
        "00c7dab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fe71c",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe6a4.md#insn-007fe6d8) · [`007fe6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe6a4.md#insn-007fe6f0) · [`007fe708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe6a4.md#insn-007fe708)
- 新版 [`007fe718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe6e4.md#insn-007fe718) · [`007fe730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe6e4.md#insn-007fe730) · [`007fe748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe6e4.md#insn-007fe748)

~~~diff
- 007fe6d8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 007fe6d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007fe6d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007fe6d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007fe718 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 007fe718 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007fe718 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007fe718 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007fe6d8 bytes 4ac12a91
+ 007fe718 bytes 4ac13a91
- 007fe6f0 ["INT_ADD", "register:40f0:8", ["const:7fe6f0:8", "const:4:8"]]
- 007fe6f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fe730 ["INT_ADD", "register:40f0:8", ["const:7fe730:8", "const:4:8"]]
+ 007fe730 ["CALL", null, ["callee:00c57e90:8"]]
- 007fe6f0 bytes e8641194
+ 007fe730 bytes d8651194
- 007fe708 ["INT_ADD", "register:40f0:8", ["const:7fe708:8", "const:4:8"]]
- 007fe708 ["CALL", null, ["callee:00c58000:8"]]
+ 007fe748 ["INT_ADD", "register:40f0:8", ["const:7fe748:8", "const:4:8"]]
+ 007fe748 ["CALL", null, ["callee:00c58000:8"]]
- 007fe708 bytes 3e651194
+ 007fe748 bytes 2e661194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af3f0f1b1ca06a825340e862e86efa4"></a>

### [`007fe7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe7a0.md) → [`007fe7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7e0.md) FUN_007fe7e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007feec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007feec0.md) [`007feec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007feec4.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007fef00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef00.md) [`007fef04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef04.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.76% / 新版 96.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007fe8c0",
      "incomplete_value": true,
      "site": "007fe8d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe880",
      "incomplete_value": true,
      "site": "007fe890",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8fc:8"
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
      "definition_site": "007fe8e8",
      "incomplete_value": false,
      "site": "007fe8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe8a8",
      "incomplete_value": false,
      "site": "007fe8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "007fe928",
      "incomplete_value": true,
      "site": "007fe93c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fe8e8",
      "incomplete_value": true,
      "site": "007fe8fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c38:8"
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
      "007fe830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fe84c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007fe8c0",
      "READ",
      [
        "storage",
        "002a58fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007fe830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fe84c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007fe8c0",
      "READ",
      [
        "storage",
        "002a59d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fe7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe7a0.md#insn-007fe7f0) · [`007fe80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe7a0.md#insn-007fe80c) · [`007fe988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe7a0.md#insn-007fe988)
- 新版 [`007fe830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7e0.md#insn-007fe830) · [`007fe84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7e0.md#insn-007fe84c) · [`007fe9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe7e0.md#insn-007fe9c8)

~~~diff
- 007fe7f0 ["INT_ADD", "register:40f0:8", ["const:7fe7f0:8", "const:4:8"]]
- 007fe7f0 ["CALL", null, ["ram:47acb4:8"]]
+ 007fe830 ["INT_ADD", "register:40f0:8", ["const:7fe830:8", "const:4:8"]]
+ 007fe830 ["CALL", null, ["ram:47acf4:8"]]
- 007fe7f0 bytes 31f1f197
+ 007fe830 bytes 31f1f197
- 007fe80c ["INT_ADD", "register:40f0:8", ["const:7fe80c:8", "const:4:8"]]
- 007fe80c ["CALL", null, ["ram:47acb4:8"]]
+ 007fe84c ["INT_ADD", "register:40f0:8", ["const:7fe84c:8", "const:4:8"]]
+ 007fe84c ["CALL", null, ["ram:47acf4:8"]]
- 007fe80c bytes 2af1f197
+ 007fe84c bytes 2af1f197
- 007fe988 ["INT_ADD", "register:40f0:8", ["const:7fe988:8", "const:4:8"]]
- 007fe988 ["CALL", null, ["ram:804034:8"]]
+ 007fe9c8 ["INT_ADD", "register:40f0:8", ["const:7fe9c8:8", "const:4:8"]]
+ 007fe9c8 ["CALL", null, ["ram:804074:8"]]
- 007fe988 bytes ab150094
+ 007fe9c8 bytes ab150094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e368e9d6b53f3976e581b883ff88c17e"></a>

### [`007fee8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fee8c.md) → [`007feecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007feecc.md) FUN_007feecc

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
      "definition_site": "007feee0",
      "incomplete_value": false,
      "site": "007feee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007feea0",
      "incomplete_value": false,
      "site": "007feea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007feee4",
      "DATA",
      [
        "storage",
        "00c7db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007feee4",
      "DATA",
      [
        "storage",
        "00c7df20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fee98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fee8c.md#insn-007fee98) · [`007feea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fee8c.md#insn-007feea0)
- 新版 [`007feed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007feecc.md#insn-007feed8) · [`007feee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007feecc.md#insn-007feee0)

~~~diff
- 007fee98 ["INT_ADD", "register:40f0:8", ["const:7fee98:8", "const:4:8"]]
- 007fee98 ["CALL", null, ["callee:00c57e90:8"]]
+ 007feed8 ["INT_ADD", "register:40f0:8", ["const:7feed8:8", "const:4:8"]]
+ 007feed8 ["CALL", null, ["callee:00c57e90:8"]]
- 007fee98 bytes fe621194
+ 007feed8 bytes ee631194
- 007feea0 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 007feea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007feea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007feea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007feee0 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007feee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007feee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007feee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007feea0 bytes 08812c91
+ 007feee0 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a425d733e125fa881db9aa28af3b467"></a>

### [`007feeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007feeb0.md) → [`007feef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007feef0.md) FUN_007feef0

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
      "definition_site": "007feef4",
      "incomplete_value": false,
      "site": "007feef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007feeb4",
      "incomplete_value": false,
      "site": "007feeb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007feef8",
      "DATA",
      [
        "storage",
        "00c7db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007feef8",
      "DATA",
      [
        "storage",
        "00c7df20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007feeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007feeb0.md#insn-007feeb4)
- 新版 [`007feef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007feef0.md#insn-007feef4)

~~~diff
- 007feeb4 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 007feeb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007feeb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007feeb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007feef4 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007feef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007feef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007feef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007feeb4 bytes 08812c91
+ 007feef4 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-611b2c7169b6e5db55cdbc79746ebb24"></a>

### [`007fef0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef0c.md) → [`007fef4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef4c.md) FUN_007fef4c

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
      "definition_site": "007fef60",
      "incomplete_value": false,
      "site": "007fef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fef20",
      "incomplete_value": false,
      "site": "007fef24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "007fef64",
      "DATA",
      [
        "storage",
        "00c7dba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fef64",
      "DATA",
      [
        "storage",
        "00c7dfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fef18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef0c.md#insn-007fef18) · [`007fef20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef0c.md#insn-007fef20)
- 新版 [`007fef58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef4c.md#insn-007fef58) · [`007fef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef4c.md#insn-007fef60)

~~~diff
- 007fef18 ["INT_ADD", "register:40f0:8", ["const:7fef18:8", "const:4:8"]]
- 007fef18 ["CALL", null, ["callee:00c57e90:8"]]
+ 007fef58 ["INT_ADD", "register:40f0:8", ["const:7fef58:8", "const:4:8"]]
+ 007fef58 ["CALL", null, ["callee:00c57e90:8"]]
- 007fef18 bytes de621194
+ 007fef58 bytes ce631194
- 007fef20 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 007fef20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fef20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fef20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fef60 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 007fef60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fef60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fef60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fef20 bytes 08812e91
+ 007fef60 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5374ced82fdcb283914d937805dadb67"></a>

### [`007fef30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef30.md) → [`007fef70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef70.md) FUN_007fef70

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
      "definition_site": "007fef74",
      "incomplete_value": false,
      "site": "007fef78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fef34",
      "incomplete_value": false,
      "site": "007fef38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007fef78",
      "DATA",
      [
        "storage",
        "00c7dba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fef78",
      "DATA",
      [
        "storage",
        "00c7dfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fef34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef30.md#insn-007fef34)
- 新版 [`007fef74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fef70.md#insn-007fef74)

~~~diff
- 007fef34 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 007fef34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007fef34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007fef34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007fef74 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 007fef74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007fef74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007fef74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007fef34 bytes 08812e91
+ 007fef74 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fafcdfa4de06bb9ab3e94d8d8706c5"></a>

### [`007fef88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef88.md) → [`007fefc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefc8.md) FUN_007fefc8

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
      "definition_site": "007fefd4",
      "incomplete_value": false,
      "site": "007fefd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fef94",
      "incomplete_value": false,
      "site": "007fef98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "007fefd8",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007fefd8",
      "DATA",
      [
        "storage",
        "00c7e030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fef90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef88.md#insn-007fef90) · [`007fef94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fef88.md#insn-007fef94)
- 新版 [`007fefd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefc8.md#insn-007fefd0) · [`007fefd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefc8.md#insn-007fefd4)

~~~diff
- 007fef90 ["COPY", "register:4048:8", ["const:c7d000:8"]]
+ 007fefd0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 007fef90 bytes e92300f0
+ 007fefd0 bytes 09240090
- 007fef94 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007fef94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fef94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fef94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007fefd4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007fefd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007fefd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007fefd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fef94 bytes 29c13091
+ 007fefd4 bytes 29c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35d2dfc2504ad784719f9ffecb3943cf"></a>

### [`007fefac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md) → [`007fefec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefec.md) FUN_007fefec

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
      "definition_site": "007feff4",
      "incomplete_value": false,
      "site": "007feff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007fefb4",
      "incomplete_value": false,
      "site": "007fefb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "007feff8",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007feff8",
      "DATA",
      [
        "storage",
        "00c7e030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007fefb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md#insn-007fefb0) · [`007fefb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md#insn-007fefb4) · [`007fefd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md#insn-007fefd8)
- 新版 [`007feff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefec.md#insn-007feff0) · [`007feff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefec.md#insn-007feff4) · [`007ff018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fefec.md#insn-007ff018)

~~~diff
- 007fefb0 ["COPY", "register:4048:8", ["const:c7d000:8"]]
+ 007feff0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 007fefb0 bytes e92300f0
+ 007feff0 bytes 09240090
- 007fefb4 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007fefb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007fefb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007fefb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007feff4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007feff4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007feff4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007feff4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007fefb4 bytes 29c13091
+ 007feff4 bytes 29c10091
- 007fefd8 ["INT_ADD", "register:40f0:8", ["const:7fefd8:8", "const:4:8"]]
- 007fefd8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ff018 ["INT_ADD", "register:40f0:8", ["const:7ff018:8", "const:4:8"]]
+ 007ff018 ["CALL", null, ["callee:00c57eb0:8"]]
- 007fefd8 bytes b6621194
+ 007ff018 bytes a6631194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a118e63a61c89e0d0fc996f25b1c075e"></a>

### [`007fefec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefec.md) → [`007ff02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff02c.md) FUN_007ff02c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ff05c",
      "incomplete_value": false,
      "site": "007ff05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff01c",
      "incomplete_value": false,
      "site": "007ff01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "007ff05c",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff05c",
      "DATA",
      [
        "storage",
        "00c7e030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefec.md#insn-007ff004) · [`007ff00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefec.md#insn-007ff00c) · [`007ff010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefec.md#insn-007ff010)
- 新版 [`007ff044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff02c.md#insn-007ff044) · [`007ff04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff02c.md#insn-007ff04c) · [`007ff050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff02c.md#insn-007ff050)

~~~diff
- 007ff004 ["INT_ADD", "register:40f0:8", ["const:7ff004:8", "const:4:8"]]
- 007ff004 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff044 ["INT_ADD", "register:40f0:8", ["const:7ff044:8", "const:4:8"]]
+ 007ff044 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff004 bytes a3621194
+ 007ff044 bytes 93631194
- 007ff00c ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff04c ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff00c bytes e82300d0
+ 007ff04c bytes e82300f0
- 007ff010 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007ff010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff050 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007ff050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff010 bytes 08c13091
+ 007ff050 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8428de504f80da99db75556888d7d6cb"></a>

### [`007ff0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff0a0.md) → [`007ff0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff0e0.md) FUN_007ff0e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
      "definition_site": "007ff10c",
      "incomplete_value": false,
      "site": "007ff10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff0cc",
      "incomplete_value": false,
      "site": "007ff0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "007ff10c",
      "DATA",
      [
        "storage",
        "00c7dc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff10c",
      "DATA",
      [
        "storage",
        "00c7e030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff0a0.md#insn-007ff0c0) · [`007ff0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff0a0.md#insn-007ff0c4) · [`007ff0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff0a0.md#insn-007ff0e4)
- 新版 [`007ff100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff0e0.md#insn-007ff100) · [`007ff104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff0e0.md#insn-007ff104) · [`007ff124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff0e0.md#insn-007ff124)

~~~diff
- 007ff0c0 ["COPY", "register:4050:8", ["const:c7d000:8"]]
+ 007ff100 ["COPY", "register:4050:8", ["const:c7e000:8"]]
- 007ff0c0 bytes ea2300d0
+ 007ff100 bytes ea2300f0
- 007ff0c4 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 007ff0c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ff0c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ff0c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ff104 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 007ff104 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff104 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ff104 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ff0c4 bytes 4ac13091
+ 007ff104 bytes 4ac10091
- 007ff0e4 ["INT_ADD", "register:40f0:8", ["const:7ff0e4:8", "const:4:8"]]
- 007ff0e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff124 ["INT_ADD", "register:40f0:8", ["const:7ff124:8", "const:4:8"]]
+ 007ff124 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff0e4 bytes 6b621194
+ 007ff124 bytes 5b631194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988dbe4a9b8dc2f79ac39274327bc660"></a>

### [`007ff188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff188.md) → [`007ff1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff1c8.md) FUN_007ff1c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "007ff1e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff1a8",
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
      "site": "007ff1f4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff1b4",
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
      "007ff1e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ff1f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007ff1e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ff1f4",
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

- 旧版 [`007ff1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff188.md#insn-007ff1a8) · [`007ff1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff188.md#insn-007ff1b4)
- 新版 [`007ff1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff1c8.md#insn-007ff1e8) · [`007ff1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff1c8.md#insn-007ff1f4)

~~~diff
- 007ff1a8 ["INT_ADD", "register:40f0:8", ["const:7ff1a8:8", "const:4:8"]]
- 007ff1a8 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff1e8 ["INT_ADD", "register:40f0:8", ["const:7ff1e8:8", "const:4:8"]]
+ 007ff1e8 ["CALL", null, ["ram:47acf4:8"]]
- 007ff1a8 bytes c3eef197
+ 007ff1e8 bytes c3eef197
- 007ff1b4 ["INT_ADD", "register:40f0:8", ["const:7ff1b4:8", "const:4:8"]]
- 007ff1b4 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff1f4 ["INT_ADD", "register:40f0:8", ["const:7ff1f4:8", "const:4:8"]]
+ 007ff1f4 ["CALL", null, ["ram:47acf4:8"]]
- 007ff1b4 bytes c0eef197
+ 007ff1f4 bytes c0eef197
~~~


<a id="compare-ee16fc5bd00f8c3ba61876818139ad1b"></a>

### [`007ff294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff294.md) → [`007ff2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff2d4.md) FUN_007ff2d4

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
      "definition_site": "007ff2f4",
      "incomplete_value": false,
      "site": "007ff2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff2b4",
      "incomplete_value": false,
      "site": "007ff2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "007ff2f8",
      "DATA",
      [
        "storage",
        "00c7dcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff2f8",
      "DATA",
      [
        "storage",
        "00c7e0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff294.md#insn-007ff2a8) · [`007ff2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff294.md#insn-007ff2b0) · [`007ff2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff294.md#insn-007ff2b4)
- 新版 [`007ff2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff2d4.md#insn-007ff2e8) · [`007ff2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff2d4.md#insn-007ff2f0) · [`007ff2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff2d4.md#insn-007ff2f4)

~~~diff
- 007ff2a8 ["INT_ADD", "register:40f0:8", ["const:7ff2a8:8", "const:4:8"]]
- 007ff2a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff2e8 ["INT_ADD", "register:40f0:8", ["const:7ff2e8:8", "const:4:8"]]
+ 007ff2e8 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff2a8 bytes fa611194
+ 007ff2e8 bytes ea621194
- 007ff2b0 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff2f0 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff2b0 bytes e82300d0
+ 007ff2f0 bytes e82300f0
- 007ff2b4 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007ff2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff2f4 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 007ff2f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff2f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff2f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff2b4 bytes 08c13291
+ 007ff2f4 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6284fff464e46b3d080672323e720a9e"></a>

### [`007ff2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2cc.md) → [`007ff30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff30c.md) FUN_007ff30c

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
      "definition_site": "007ff310",
      "incomplete_value": false,
      "site": "007ff314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff2d0",
      "incomplete_value": false,
      "site": "007ff2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "007ff314",
      "DATA",
      [
        "storage",
        "00c7dcb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff314",
      "DATA",
      [
        "storage",
        "00c7e0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2cc.md#insn-007ff2cc) · [`007ff2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2cc.md#insn-007ff2d0)
- 新版 [`007ff30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff30c.md#insn-007ff30c) · [`007ff310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff30c.md#insn-007ff310)

~~~diff
- 007ff2cc ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff30c ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff2cc bytes e82300d0
+ 007ff30c bytes e82300f0
- 007ff2d0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 007ff2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff310 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 007ff310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff2d0 bytes 08c13291
+ 007ff310 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b29a8f3542291596aa55addba533f9c"></a>

### [`007ff2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2ec.md) → [`007ff32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff32c.md) FUN_007ff32c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007ff57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff57c.md) [`007ff580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff580.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007ff5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5bc.md) [`007ff5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5c0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ff448",
      "incomplete_value": true,
      "site": "007ff448",
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
      "definition_site": "007ff408",
      "incomplete_value": true,
      "site": "007ff408",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff364",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff324",
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
      "site": "007ff380",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff340",
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
      "007ff364",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ff380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ff3d0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "007ff364",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ff380",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ff3d0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2ec.md#insn-007ff324) · [`007ff340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2ec.md#insn-007ff340) · [`007ff3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff2ec.md#insn-007ff3a8)
- 新版 [`007ff364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff32c.md#insn-007ff364) · [`007ff380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff32c.md#insn-007ff380) · [`007ff3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff32c.md#insn-007ff3e8)

~~~diff
- 007ff324 ["INT_ADD", "register:40f0:8", ["const:7ff324:8", "const:4:8"]]
- 007ff324 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff364 ["INT_ADD", "register:40f0:8", ["const:7ff364:8", "const:4:8"]]
+ 007ff364 ["CALL", null, ["ram:47acf4:8"]]
- 007ff324 bytes 64eef197
+ 007ff364 bytes 64eef197
- 007ff340 ["INT_ADD", "register:40f0:8", ["const:7ff340:8", "const:4:8"]]
- 007ff340 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff380 ["INT_ADD", "register:40f0:8", ["const:7ff380:8", "const:4:8"]]
+ 007ff380 ["CALL", null, ["ram:47acf4:8"]]
- 007ff340 bytes 5deef197
+ 007ff380 bytes 5deef197
- 007ff3a8 ["COPY", "tmp:0:8", ["const:898:8"]]
- 007ff3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff3e8 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 007ff3e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff3e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff3e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff3a8 bytes 29612291
+ 007ff3e8 bytes 29612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c20944f3e53906517c2e7aab37f75225"></a>

### [`007ff52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff52c.md) → [`007ff56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff56c.md) FUN_007ff56c

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
      "definition_site": "007ff58c",
      "incomplete_value": false,
      "site": "007ff590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff54c",
      "incomplete_value": false,
      "site": "007ff550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007ff590",
      "DATA",
      [
        "storage",
        "00c7dd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff590",
      "DATA",
      [
        "storage",
        "00c7e120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff52c.md#insn-007ff540) · [`007ff548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff52c.md#insn-007ff548) · [`007ff54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff52c.md#insn-007ff54c)
- 新版 [`007ff580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff56c.md#insn-007ff580) · [`007ff588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff56c.md#insn-007ff588) · [`007ff58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff56c.md#insn-007ff58c)

~~~diff
- 007ff540 ["INT_ADD", "register:40f0:8", ["const:7ff540:8", "const:4:8"]]
- 007ff540 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff580 ["INT_ADD", "register:40f0:8", ["const:7ff580:8", "const:4:8"]]
+ 007ff580 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff540 bytes 54611194
+ 007ff580 bytes 44621194
- 007ff548 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff588 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff548 bytes e82300d0
+ 007ff588 bytes e82300f0
- 007ff54c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007ff54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff58c ["COPY", "tmp:0:8", ["const:120:8"]]
+ 007ff58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff54c bytes 08813491
+ 007ff58c bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2458ef2dc2a2ba8cd2a7bdf850a66a08"></a>

### [`007ff564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff564.md) → [`007ff5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5a4.md) FUN_007ff5a4

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
      "definition_site": "007ff5a8",
      "incomplete_value": false,
      "site": "007ff5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff568",
      "incomplete_value": false,
      "site": "007ff56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
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
      "007ff5ac",
      "DATA",
      [
        "storage",
        "00c7dd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff5ac",
      "DATA",
      [
        "storage",
        "00c7e120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff564.md#insn-007ff564) · [`007ff568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff564.md#insn-007ff568)
- 新版 [`007ff5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5a4.md#insn-007ff5a4) · [`007ff5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5a4.md#insn-007ff5a8)

~~~diff
- 007ff564 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff5a4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff564 bytes e82300d0
+ 007ff5a4 bytes e82300f0
- 007ff568 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 007ff568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff5a8 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 007ff5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff568 bytes 08813491
+ 007ff5a8 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee93056e29744bc9a93bae9195e5148e"></a>

### [`007ff584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff584.md) → [`007ff5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5c4.md) FUN_007ff5c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007ff5e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff5a8",
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
      "007ff5e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007ff5e8",
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

- 旧版 [`007ff5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff584.md#insn-007ff5a8) · [`007ff5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff584.md#insn-007ff5b4)
- 新版 [`007ff5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5c4.md#insn-007ff5e8) · [`007ff5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff5c4.md#insn-007ff5f4)

~~~diff
- 007ff5a8 ["INT_ADD", "register:40f0:8", ["const:7ff5a8:8", "const:4:8"]]
- 007ff5a8 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff5e8 ["INT_ADD", "register:40f0:8", ["const:7ff5e8:8", "const:4:8"]]
+ 007ff5e8 ["CALL", null, ["ram:47acf4:8"]]
- 007ff5a8 bytes c3edf197
+ 007ff5e8 bytes c3edf197
- 007ff5b4 ["INT_ADD", "register:40f0:8", ["const:7ff5b4:8", "const:4:8"]]
- 007ff5b4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007ff5f4 ["INT_ADD", "register:40f0:8", ["const:7ff5f4:8", "const:4:8"]]
+ 007ff5f4 ["CALL", null, ["callee:0047cdd4:8"]]
- 007ff5b4 bytes f8f5f197
+ 007ff5f4 bytes f8f5f197
~~~


<a id="compare-1c8c9c75b92da2eb6dc7684e050dae95"></a>

### [`007ff5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff5f8.md) → [`007ff638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff638.md) FUN_007ff638

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
      "definition_site": "007ff658",
      "incomplete_value": false,
      "site": "007ff65c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff618",
      "incomplete_value": false,
      "site": "007ff61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "007ff65c",
      "DATA",
      [
        "storage",
        "00c7ddb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff65c",
      "DATA",
      [
        "storage",
        "00c7e1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff5f8.md#insn-007ff60c) · [`007ff614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff5f8.md#insn-007ff614) · [`007ff618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff5f8.md#insn-007ff618)
- 新版 [`007ff64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff638.md#insn-007ff64c) · [`007ff654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff638.md#insn-007ff654) · [`007ff658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff638.md#insn-007ff658)

~~~diff
- 007ff60c ["INT_ADD", "register:40f0:8", ["const:7ff60c:8", "const:4:8"]]
- 007ff60c ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff64c ["INT_ADD", "register:40f0:8", ["const:7ff64c:8", "const:4:8"]]
+ 007ff64c ["CALL", null, ["callee:00c57e90:8"]]
- 007ff60c bytes 21611194
+ 007ff64c bytes 11621194
- 007ff614 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff654 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff614 bytes e82300d0
+ 007ff654 bytes e82300f0
- 007ff618 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 007ff618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff658 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 007ff658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff618 bytes 08c13691
+ 007ff658 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfabe0a2e32e3d1b352c22add7535cd7"></a>

### [`007ff650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff650.md) → [`007ff690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff690.md) FUN_007ff690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007ff858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff858.md) [`007ff85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff85c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007ff898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff898.md) [`007ff89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff89c.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ff730",
      "incomplete_value": false,
      "site": "007ff730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff6f0",
      "incomplete_value": false,
      "site": "007ff6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "site": "007ff6c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff688",
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
      "site": "007ff6e4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff6a4",
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
      "007ff6c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ff6e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ff730",
      "DATA",
      [
        "storage",
        "00c7de20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff6c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ff6e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ff730",
      "DATA",
      [
        "storage",
        "00c7e220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff650.md#insn-007ff688) · [`007ff6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff650.md#insn-007ff6a4) · [`007ff6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff650.md#insn-007ff6e4)
- 新版 [`007ff6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff690.md#insn-007ff6c8) · [`007ff6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff690.md#insn-007ff6e4) · [`007ff724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff690.md#insn-007ff724)

~~~diff
- 007ff688 ["INT_ADD", "register:40f0:8", ["const:7ff688:8", "const:4:8"]]
- 007ff688 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff6c8 ["INT_ADD", "register:40f0:8", ["const:7ff6c8:8", "const:4:8"]]
+ 007ff6c8 ["CALL", null, ["ram:47acf4:8"]]
- 007ff688 bytes 8bedf197
+ 007ff6c8 bytes 8bedf197
- 007ff6a4 ["INT_ADD", "register:40f0:8", ["const:7ff6a4:8", "const:4:8"]]
- 007ff6a4 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff6e4 ["INT_ADD", "register:40f0:8", ["const:7ff6e4:8", "const:4:8"]]
+ 007ff6e4 ["CALL", null, ["ram:47acf4:8"]]
- 007ff6a4 bytes 84edf197
+ 007ff6e4 bytes 84edf197
- 007ff6e4 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff724 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff6e4 bytes e82300d0
+ 007ff724 bytes e82300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d2d7486781b4096ae8d3702200a056"></a>

### [`007ff810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff810.md) → [`007ff850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff850.md) FUN_007ff850

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
      "definition_site": "007ff874",
      "incomplete_value": false,
      "site": "007ff874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff834",
      "incomplete_value": false,
      "site": "007ff834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "007ff874",
      "DATA",
      [
        "storage",
        "00c7de20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff874",
      "DATA",
      [
        "storage",
        "00c7e220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff810.md#insn-007ff824) · [`007ff82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff810.md#insn-007ff82c) · [`007ff830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff810.md#insn-007ff830)
- 新版 [`007ff864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff850.md#insn-007ff864) · [`007ff86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff850.md#insn-007ff86c) · [`007ff870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff850.md#insn-007ff870)

~~~diff
- 007ff824 ["INT_ADD", "register:40f0:8", ["const:7ff824:8", "const:4:8"]]
- 007ff824 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff864 ["INT_ADD", "register:40f0:8", ["const:7ff864:8", "const:4:8"]]
+ 007ff864 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff824 bytes 9b601194
+ 007ff864 bytes 8b611194
- 007ff82c ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff86c ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff82c bytes e82300d0
+ 007ff86c bytes e82300f0
- 007ff830 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 007ff830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff870 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 007ff870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff830 bytes 08813891
+ 007ff870 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a2e278565ca64c3cb5a45a2ca719d8"></a>

### [`007ff860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff860.md) → [`007ff8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff8a0.md) FUN_007ff8a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "007ff8c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ff884",
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
      "007ff8c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007ff8c4",
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

- 旧版 [`007ff884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff860.md#insn-007ff884) · [`007ff890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff860.md#insn-007ff890)
- 新版 [`007ff8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff8a0.md#insn-007ff8c4) · [`007ff8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff8a0.md#insn-007ff8d0)

~~~diff
- 007ff884 ["INT_ADD", "register:40f0:8", ["const:7ff884:8", "const:4:8"]]
- 007ff884 ["CALL", null, ["ram:47acb4:8"]]
+ 007ff8c4 ["INT_ADD", "register:40f0:8", ["const:7ff8c4:8", "const:4:8"]]
+ 007ff8c4 ["CALL", null, ["ram:47acf4:8"]]
- 007ff884 bytes 0cedf197
+ 007ff8c4 bytes 0cedf197
- 007ff890 ["INT_ADD", "register:40f0:8", ["const:7ff890:8", "const:4:8"]]
- 007ff890 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007ff8d0 ["INT_ADD", "register:40f0:8", ["const:7ff8d0:8", "const:4:8"]]
+ 007ff8d0 ["CALL", null, ["callee:0047cdd4:8"]]
- 007ff890 bytes 41f5f197
+ 007ff8d0 bytes 41f5f197
~~~


<a id="compare-23c8e74666997917e574ea72606dd579"></a>

### [`007ff8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff8d4.md) → [`007ff914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff914.md) FUN_007ff914

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
      "definition_site": "007ff938",
      "incomplete_value": false,
      "site": "007ff938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff8f8",
      "incomplete_value": false,
      "site": "007ff8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007ff938",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff938",
      "DATA",
      [
        "storage",
        "00c7e2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff8d4.md#insn-007ff8e8) · [`007ff8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff8d4.md#insn-007ff8f0) · [`007ff8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff8d4.md#insn-007ff8f4)
- 新版 [`007ff928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff914.md#insn-007ff928) · [`007ff930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff914.md#insn-007ff930) · [`007ff934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff914.md#insn-007ff934)

~~~diff
- 007ff8e8 ["INT_ADD", "register:40f0:8", ["const:7ff8e8:8", "const:4:8"]]
- 007ff8e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ff928 ["INT_ADD", "register:40f0:8", ["const:7ff928:8", "const:4:8"]]
+ 007ff928 ["CALL", null, ["callee:00c57e90:8"]]
- 007ff8e8 bytes 6a601194
+ 007ff928 bytes 5a611194
- 007ff8f0 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ff930 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ff8f0 bytes e82300d0
+ 007ff930 bytes e82300f0
- 007ff8f4 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007ff8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ff8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ff8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ff934 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 007ff934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ff934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ff8f4 bytes 08c13a91
+ 007ff934 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65989e8b6b554e5c87019f8aada54f27"></a>

### [`007ff908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff908.md) → [`007ff948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff948.md) FUN_007ff948

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
      "definition_site": "007ff954",
      "incomplete_value": false,
      "site": "007ff954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff914",
      "incomplete_value": false,
      "site": "007ff914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "007ff954",
      "DATA",
      [
        "storage",
        "00c7deb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ff954",
      "DATA",
      [
        "storage",
        "00c7e2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff908.md#insn-007ff90c) · [`007ff910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff908.md#insn-007ff910)
- 新版 [`007ff94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff948.md#insn-007ff94c) · [`007ff950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff948.md#insn-007ff950)

~~~diff
- 007ff90c ["COPY", "register:4048:8", ["const:c7d000:8"]]
+ 007ff94c ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 007ff90c bytes e92300d0
+ 007ff94c bytes e92300f0
- 007ff910 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 007ff910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ff950 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 007ff950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ff950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff910 bytes 29c13a91
+ 007ff950 bytes 29c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d07ad46824994beb0ae9ffcc77211ad9"></a>

### [`007ff9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff9e4.md) → [`007ffa24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa24.md) FUN_007ffa24

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
      "definition_site": "007ffa2c",
      "incomplete_value": false,
      "site": "007ffa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ff9ec",
      "incomplete_value": false,
      "site": "007ff9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "007ffa30",
      "DATA",
      [
        "storage",
        "00c7df30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffa30",
      "DATA",
      [
        "storage",
        "00c7e330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ff9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff9e4.md#insn-007ff9e8) · [`007ff9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff9e4.md#insn-007ff9ec) · [`007ffa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff9e4.md#insn-007ffa10)
- 新版 [`007ffa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa24.md#insn-007ffa28) · [`007ffa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa24.md#insn-007ffa2c) · [`007ffa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa24.md#insn-007ffa50)

~~~diff
- 007ff9e8 ["COPY", "register:4048:8", ["const:c7d000:8"]]
+ 007ffa28 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 007ff9e8 bytes e92300d0
+ 007ffa28 bytes e92300f0
- 007ff9ec ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007ff9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ff9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ff9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ffa2c ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007ffa2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffa2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffa2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ff9ec bytes 29c13c91
+ 007ffa2c bytes 29c10c91
- 007ffa10 ["INT_ADD", "register:40f0:8", ["const:7ffa10:8", "const:4:8"]]
- 007ffa10 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007ffa50 ["INT_ADD", "register:40f0:8", ["const:7ffa50:8", "const:4:8"]]
+ 007ffa50 ["CALL", null, ["callee:00c57eb0:8"]]
- 007ffa10 bytes 28601194
+ 007ffa50 bytes 18611194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c796eb9acc04ebeac62a5b6851c410f"></a>

### [`007ffa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffa24.md) → [`007ffa64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md) FUN_007ffa64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007ffa98",
      "incomplete_value": false,
      "site": "007ffa98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffa58",
      "incomplete_value": false,
      "site": "007ffa58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "007ffa98",
      "DATA",
      [
        "storage",
        "00c7df30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffa98",
      "DATA",
      [
        "storage",
        "00c7e330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffa24.md#insn-007ffa38) · [`007ffa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffa24.md#insn-007ffa44) · [`007ffa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffa24.md#insn-007ffa48)
- 新版 [`007ffa78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md#insn-007ffa78) · [`007ffa84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md#insn-007ffa84) · [`007ffa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md#insn-007ffa88)

~~~diff
- 007ffa38 ["INT_ADD", "register:40f0:8", ["const:7ffa38:8", "const:4:8"]]
- 007ffa38 ["CALL", null, ["callee:00c57e90:8"]]
+ 007ffa78 ["INT_ADD", "register:40f0:8", ["const:7ffa78:8", "const:4:8"]]
+ 007ffa78 ["CALL", null, ["callee:00c57e90:8"]]
- 007ffa38 bytes 16601194
+ 007ffa78 bytes 06611194
- 007ffa44 ["COPY", "register:4048:8", ["const:c7d000:8"]]
+ 007ffa84 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 007ffa44 bytes e92300d0
+ 007ffa84 bytes e92300f0
- 007ffa48 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007ffa48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ffa48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ffa48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ffa88 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007ffa88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffa88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ffa88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ffa48 bytes 29c13c91
+ 007ffa88 bytes 29c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c71e433d5c39aed3ba2299be52039d7"></a>

### [`007ffaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffaa8.md) → [`007ffae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffae8.md) FUN_007ffae8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "007ffaec",
      "incomplete_value": false,
      "site": "007ffaf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffaac",
      "incomplete_value": false,
      "site": "007ffab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "007ffaf0",
      "DATA",
      [
        "storage",
        "00c7df30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffaf0",
      "DATA",
      [
        "storage",
        "00c7e330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffaa8.md#insn-007ffaa8) · [`007ffaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffaa8.md#insn-007ffaac)
- 新版 [`007ffae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffae8.md#insn-007ffae8) · [`007ffaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffae8.md#insn-007ffaec)

~~~diff
- 007ffaa8 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ffae8 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ffaa8 bytes e82300d0
+ 007ffae8 bytes e82300f0
- 007ffaac ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007ffaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffaec ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007ffaec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffaec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffaec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffaac bytes 08c13c91
+ 007ffaec bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae17048632c65521f63e6ab7c2ad931a"></a>

### [`007ffb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb3c.md) → [`007ffb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb7c.md) FUN_007ffb7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007ffdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdb4.md) [`007ffdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdb8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007ffdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdf4.md) [`007ffdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdf8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

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
      "site": "007ffbd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ffb90",
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
      "site": "007ffbec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ffbac",
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
      "007ffbd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ffbec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007ffc50",
      "DATA",
      [
        "storage",
        "00c7dfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffbd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ffbec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007ffc50",
      "DATA",
      [
        "storage",
        "00c7e3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb3c.md#insn-007ffb90) · [`007ffbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb3c.md#insn-007ffbac) · [`007ffb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffb3c.md#insn-007ffb74)
- 新版 [`007ffbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb7c.md#insn-007ffbd0) · [`007ffbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb7c.md#insn-007ffbec) · [`007ffbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffb7c.md#insn-007ffbb4)

~~~diff
- 007ffb90 ["INT_ADD", "register:40f0:8", ["const:7ffb90:8", "const:4:8"]]
- 007ffb90 ["CALL", null, ["ram:47acb4:8"]]
+ 007ffbd0 ["INT_ADD", "register:40f0:8", ["const:7ffbd0:8", "const:4:8"]]
+ 007ffbd0 ["CALL", null, ["ram:47acf4:8"]]
- 007ffb90 bytes 49ecf197
+ 007ffbd0 bytes 49ecf197
- 007ffbac ["INT_ADD", "register:40f0:8", ["const:7ffbac:8", "const:4:8"]]
- 007ffbac ["CALL", null, ["ram:47acb4:8"]]
+ 007ffbec ["INT_ADD", "register:40f0:8", ["const:7ffbec:8", "const:4:8"]]
+ 007ffbec ["CALL", null, ["ram:47acf4:8"]]
- 007ffbac bytes 42ecf197
+ 007ffbec bytes 42ecf197
- 007ffb74 ["INT_ADD", "register:40f0:8", ["const:7ffb74:8", "const:4:8"]]
- 007ffb74 ["CALL", null, ["callee:008b6f50:8"]]
+ 007ffbb4 ["INT_ADD", "register:40f0:8", ["const:7ffbb4:8", "const:4:8"]]
+ 007ffbb4 ["CALL", null, ["callee:008b6f50:8"]]
- 007ffb74 bytes e6dc0294
+ 007ffbb4 bytes e7dc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad4294b38e3eda0b6d8a70a97693d28"></a>

### [`007ffd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffd80.md) → [`007ffdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdc0.md) FUN_007ffdc0

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
      "definition_site": "007ffdd4",
      "incomplete_value": false,
      "site": "007ffdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffd94",
      "incomplete_value": false,
      "site": "007ffd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "007ffdd8",
      "DATA",
      [
        "storage",
        "00c7dfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffdd8",
      "DATA",
      [
        "storage",
        "00c7e3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffd80.md#insn-007ffd8c) · [`007ffd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffd80.md#insn-007ffd90) · [`007ffd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffd80.md#insn-007ffd94)
- 新版 [`007ffdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdc0.md#insn-007ffdcc) · [`007ffdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdc0.md#insn-007ffdd0) · [`007ffdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffdc0.md#insn-007ffdd4)

~~~diff
- 007ffd8c ["INT_ADD", "register:40f0:8", ["const:7ffd8c:8", "const:4:8"]]
- 007ffd8c ["CALL", null, ["callee:00c57e90:8"]]
+ 007ffdcc ["INT_ADD", "register:40f0:8", ["const:7ffdcc:8", "const:4:8"]]
+ 007ffdcc ["CALL", null, ["callee:00c57e90:8"]]
- 007ffd8c bytes 415f1194
+ 007ffdcc bytes 31601194
- 007ffd90 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ffdd0 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ffd90 bytes e82300d0
+ 007ffdd0 bytes e82300f0
- 007ffd94 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 007ffd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffdd4 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 007ffdd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffdd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffdd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffd94 bytes 08813e91
+ 007ffdd4 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9738c2f5d4c616d735e9a90611cd23e"></a>

### [`007ffda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffda4.md) → [`007ffde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffde4.md) FUN_007ffde4

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
      "definition_site": "007ffde8",
      "incomplete_value": false,
      "site": "007ffdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ffda8",
      "incomplete_value": false,
      "site": "007ffdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "007ffdec",
      "DATA",
      [
        "storage",
        "00c7dfa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ffdec",
      "DATA",
      [
        "storage",
        "00c7e3a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ffda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffda4.md#insn-007ffda4) · [`007ffda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffda4.md#insn-007ffda8)
- 新版 [`007ffde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffde4.md#insn-007ffde4) · [`007ffde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffde4.md#insn-007ffde8)

~~~diff
- 007ffda4 ["COPY", "register:4040:8", ["const:c7d000:8"]]
+ 007ffde4 ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 007ffda4 bytes e82300d0
+ 007ffde4 bytes e82300f0
- 007ffda8 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 007ffda8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ffda8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ffda8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ffde8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 007ffde8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffde8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ffde8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ffda8 bytes 08813e91
+ 007ffde8 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-808a33e482360b45ee9e11e2b9039205"></a>

### [`007ffdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdfc.md) → [`007ffe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffe3c.md) _INIT_146

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ffe78",
      "incomplete_value": true,
      "site": "007ffe94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ffe38",
      "incomplete_value": true,
      "site": "007ffe54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ffe9c",
      "incomplete_value": true,
      "site": "007ffeb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ffe5c",
      "incomplete_value": true,
      "site": "007ffe78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ffebc",
      "incomplete_value": true,
      "site": "007ffed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007ffe7c",
      "incomplete_value": true,
      "site": "007ffe98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007ffe78",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007ffe9c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007ffebc",
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
      "007ffe78",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007ffe9c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007ffebc",
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

- 旧版 [`007ffe74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdfc.md#insn-007ffe74) · [`007ffe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdfc.md#insn-007ffe94) · [`007fff5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ffdfc.md#insn-007fff5c)
- 新版 [`007ffeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffe3c.md#insn-007ffeb4) · [`007ffed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffe3c.md#insn-007ffed4) · [`007fff9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffe3c.md#insn-007fff9c)

~~~diff
- 007ffe74 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007ffe74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ffe74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ffe74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ffeb4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007ffeb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ffeb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ffeb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ffe74 bytes 4a093691
+ 007ffeb4 bytes 4a093791
- 007ffe94 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007ffe94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ffe94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ffe94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ffed4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 007ffed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ffed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ffed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ffe94 bytes 4a553a91
+ 007ffed4 bytes 4a893d91
- 007fff5c ["INT_ADD", "register:40f0:8", ["const:7fff5c:8", "const:4:8"]]
- 007fff5c ["CALL", null, ["callee:0043b7f8:8"]]
+ 007fff9c ["INT_ADD", "register:40f0:8", ["const:7fff9c:8", "const:4:8"]]
+ 007fff9c ["CALL", null, ["callee:0043b7f8:8"]]
- 007fff5c bytes 17eef097
+ 007fff9c bytes 17eef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77ef9619cae640f1994c33d66f2ce971"></a>

### [`00800938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800938.md) → [`00800978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800978.md) FUN_00800978

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008009bc",
      "incomplete_value": false,
      "site": "008009c8",
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
      "definition_site": "0080097c",
      "incomplete_value": false,
      "site": "00800988",
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
      "definition_site": "00801a28",
      "incomplete_value": true,
      "site": "00801a2c",
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
      "definition_site": "008019e8",
      "incomplete_value": true,
      "site": "008019ec",
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
    "ordinal": 239,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00801a24",
      "incomplete_value": true,
      "site": "00801a30",
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
      "definition_site": "008019e4",
      "incomplete_value": true,
      "site": "008019f0",
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
    "ordinal": 240,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008009c8",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00800b5c",
      "READ",
      [
        "storage",
        "002a2374",
        null,
        "string"
      ]
    ],
    [
      "00800b60",
      "READ",
      [
        "storage",
        "002a237a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008009c8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00800b5c",
      "READ",
      [
        "storage",
        "002a2441",
        null,
        "string"
      ]
    ],
    [
      "00800b60",
      "READ",
      [
        "storage",
        "002a2447",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008019bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800938.md#insn-008019bc) · [`00801a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800938.md#insn-00801a30) · [`00800970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800938.md#insn-00800970)
- 新版 [`008019fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800978.md#insn-008019fc) · [`00801a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800978.md#insn-00801a70) · [`008009b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800978.md#insn-008009b0)

~~~diff
- 008019bc ["INT_ADD", "register:40f0:8", ["const:8019bc:8", "const:4:8"]]
- 008019bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 008019fc ["INT_ADD", "register:40f0:8", ["const:8019fc:8", "const:4:8"]]
+ 008019fc ["CALL", null, ["callee:00c57eb0:8"]]
- 008019bc bytes 3d581194
+ 008019fc bytes 2d591194
- 00801a30 ["INT_ADD", "register:40f0:8", ["const:801a30:8", "const:4:8"]]
- 00801a30 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00801a70 ["INT_ADD", "register:40f0:8", ["const:801a70:8", "const:4:8"]]
+ 00801a70 ["CALL", null, ["callee:00c57fb0:8"]]
- 00801a30 bytes 60581194
+ 00801a70 bytes 50591194
- 00800970 ["INT_ADD", "register:40f0:8", ["const:800970:8", "const:4:8"]]
- 00800970 ["CALL", null, ["callee:00487e20:8"]]
+ 008009b0 ["INT_ADD", "register:40f0:8", ["const:8009b0:8", "const:4:8"]]
+ 008009b0 ["CALL", null, ["callee:00487e20:8"]]
- 00800970 bytes 1c1df297
+ 008009b0 bytes 1c1df297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d416484a40399c164c3042922228c97b"></a>

### [`00801f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801f48.md) → [`00801f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801f88.md) FUN_00801f88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`006270cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/006270cc.md) [`00729cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729cb4.md) [`00730d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730d3c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 8件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`0062710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00627/0062710c.md) [`00729cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729cf4.md) [`00730d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730d7c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00802004",
      "incomplete_value": false,
      "site": "00802008",
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
      "definition_site": "00801fc4",
      "incomplete_value": false,
      "site": "00801fc8",
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
      "00802004",
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
      "00802004",
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

- 旧版 [`00801fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801f48.md#insn-00801fc8) · [`00801fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801f48.md#insn-00801fc4)
- 新版 [`00802008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801f88.md#insn-00802008) · [`00802004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801f88.md#insn-00802004)

~~~diff
- 00801fc8 ["INT_ADD", "register:40f0:8", ["const:801fc8:8", "const:4:8"]]
- 00801fc8 ["CALL", null, ["callee:00442930:8"]]
+ 00802008 ["INT_ADD", "register:40f0:8", ["const:802008:8", "const:4:8"]]
+ 00802008 ["CALL", null, ["callee:00442930:8"]]
- 00801fc8 bytes 4a02f197
+ 00802008 bytes 4a02f197
- 00801fc4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00801fc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00801fc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00801fc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00802004 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00802004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00802004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00802004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00801fc4 bytes 00c00391
+ 00802004 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363a4fc9eaf2c4ecb99442746ecfb8ec"></a>

### [`00802164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802164.md) → [`008021a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008021a4.md) FUN_008021a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00ab0300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab0300.md) · 呼出先 2件 [`00801fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00801/00801fd8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00ab04fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab04fc.md) · 呼出先 2件 [`00802018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802018.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

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
      "site": "00802264",
      "value": [
        "leaf",
        "ram:802018:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00802224",
      "value": [
        "leaf",
        "ram:801fd8:8"
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
      "00802264",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00801fd8"
      ]
    ]
  ],
  "added": [
    [
      "00802264",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802018"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802164.md#insn-00802224) · [`008021c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802164.md#insn-008021c4)
- 新版 [`00802264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008021a4.md#insn-00802264) · [`00802204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008021a4.md#insn-00802204)

~~~diff
- 00802224 ["INT_ADD", "register:40f0:8", ["const:802224:8", "const:4:8"]]
- 00802224 ["CALL", null, ["ram:801fd8:8"]]
+ 00802264 ["INT_ADD", "register:40f0:8", ["const:802264:8", "const:4:8"]]
+ 00802264 ["CALL", null, ["ram:802018:8"]]
- 00802224 bytes 6dffff97
+ 00802264 bytes 6dffff97
- 008021c4 ["INT_ADD", "register:40f0:8", ["const:8021c4:8", "const:4:8"]]
- 008021c4 ["CALL", null, ["callee:008514f8:8"]]
+ 00802204 ["INT_ADD", "register:40f0:8", ["const:802204:8", "const:4:8"]]
+ 00802204 ["CALL", null, ["callee:008514f8:8"]]
- 008021c4 bytes bd3c0194
+ 00802204 bytes bd3c0194
~~~


<a id="compare-58dae112ec3648079be08da1859f4cc2"></a>

### [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) → [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) FUN_008026b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 71件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005e46a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e46a0.md) [`005e486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e486c.md) [`005e48f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e48f0.md) [`005e4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4e34.md) · 呼出先 7件 [`007bbbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbbec.md) [`007bbc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbc70.md) [`00802820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802820.md) [`008029f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008029f8.md) [`00802a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802a88.md)
- 新版 呼出元 71件 [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005e46e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e46e0.md) [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4930.md) [`005e4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e74.md) · 呼出先 7件 [`007bbc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbc2c.md) [`007bbcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbcb0.md) [`00802860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802860.md) [`00802a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802a38.md) [`00802ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ac8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "008026e4",
      "value": [
        "leaf",
        "ram:7bbc2c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008026a4",
      "value": [
        "leaf",
        "ram:7bbbec:8"
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
      "site": "008026f0",
      "value": [
        "leaf",
        "ram:7bbcb0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008026b0",
      "value": [
        "leaf",
        "ram:7bbc70:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008026e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007bbbec"
      ]
    ],
    [
      "008026f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007bbc70"
      ]
    ],
    [
      "008027b0",
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
      "008026e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007bbc2c"
      ]
    ],
    [
      "008026f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007bbcb0"
      ]
    ],
    [
      "008027b0",
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

- 旧版 [`008026a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md#insn-008026a4) · [`008026b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md#insn-008026b0) · [`008026e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md#insn-008026e4)
- 新版 [`008026e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md#insn-008026e4) · [`008026f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md#insn-008026f0) · [`00802724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md#insn-00802724)

~~~diff
- 008026a4 ["INT_ADD", "register:40f0:8", ["const:8026a4:8", "const:4:8"]]
- 008026a4 ["CALL", null, ["ram:7bbbec:8"]]
+ 008026e4 ["INT_ADD", "register:40f0:8", ["const:8026e4:8", "const:4:8"]]
+ 008026e4 ["CALL", null, ["ram:7bbc2c:8"]]
- 008026a4 bytes 52e5fe97
+ 008026e4 bytes 52e5fe97
- 008026b0 ["INT_ADD", "register:40f0:8", ["const:8026b0:8", "const:4:8"]]
- 008026b0 ["CALL", null, ["ram:7bbc70:8"]]
+ 008026f0 ["INT_ADD", "register:40f0:8", ["const:8026f0:8", "const:4:8"]]
+ 008026f0 ["CALL", null, ["ram:7bbcb0:8"]]
- 008026b0 bytes 70e5fe97
+ 008026f0 bytes 70e5fe97
- 008026e4 ["INT_ADD", "register:40f0:8", ["const:8026e4:8", "const:4:8"]]
- 008026e4 ["CALL", null, ["callee:008514f8:8"]]
+ 00802724 ["INT_ADD", "register:40f0:8", ["const:802724:8", "const:4:8"]]
+ 00802724 ["CALL", null, ["callee:008514f8:8"]]
- 008026e4 bytes 753b0194
+ 00802724 bytes 753b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da45bdfda6b2e4b4f17fb53dab929d33"></a>

### [`00802820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802820.md) → [`00802860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802860.md) FUN_00802860

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md)
- 新版 呼出元 1件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.15% / 新版 99.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0080293c",
      "incomplete_value": false,
      "site": "00802940",
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
      "definition_site": "008028fc",
      "incomplete_value": false,
      "site": "00802900",
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
      "0080293c",
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
      "0080293c",
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

- 旧版 [`00802900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802820.md#insn-00802900) · [`0080282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802820.md#insn-0080282c) · [`00802830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802820.md#insn-00802830)
- 新版 [`00802940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802860.md#insn-00802940) · [`0080286c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802860.md#insn-0080286c) · [`00802870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802860.md#insn-00802870)

~~~diff
- 00802900 ["INT_ADD", "register:40f0:8", ["const:802900:8", "const:4:8"]]
- 00802900 ["CALL", null, ["callee:00442930:8"]]
+ 00802940 ["INT_ADD", "register:40f0:8", ["const:802940:8", "const:4:8"]]
+ 00802940 ["CALL", null, ["callee:00442930:8"]]
- 00802900 bytes fcfff097
+ 00802940 bytes fcfff097
- 0080282c ["INT_ADD", "register:40f0:8", ["const:80282c:8", "const:4:8"]]
- 0080282c ["CALL", null, ["callee:008514f8:8"]]
+ 0080286c ["INT_ADD", "register:40f0:8", ["const:80286c:8", "const:4:8"]]
+ 0080286c ["CALL", null, ["callee:008514f8:8"]]
- 0080282c bytes 233b0194
+ 0080286c bytes 233b0194
- 00802830 ["INT_ADD", "register:40f0:8", ["const:802830:8", "const:4:8"]]
- 00802830 ["CALL", null, ["callee:00853c70:8"]]
+ 00802870 ["INT_ADD", "register:40f0:8", ["const:802870:8", "const:4:8"]]
+ 00802870 ["CALL", null, ["callee:00853c70:8"]]
- 00802830 bytes 00450194
+ 00802870 bytes 00450194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3f0c1765810a083d07d2b4f6d1ef86"></a>

### [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) → [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) FUN_00802b58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 87件 [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) [`005e2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2e00.md) [`005e6dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6dbc.md) [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) [`005e7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7efc.md) · 呼出先 3件 [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md)
- 新版 呼出元 87件 [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) [`005e2e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2e40.md) [`005e6dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6dfc.md) [`005e7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7504.md) [`005e7f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7f3c.md) · 呼出先 3件 [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "00802b74",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00802b34",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "00802b74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "00802b74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md#insn-00802b34) · [`00802b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md#insn-00802b28)
- 新版 [`00802b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md#insn-00802b74) · [`00802b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md#insn-00802b68)

~~~diff
- 00802b34 ["INT_ADD", "register:40f0:8", ["const:802b34:8", "const:4:8"]]
- 00802b34 ["CALL", null, ["ram:802b4c:8"]]
+ 00802b74 ["INT_ADD", "register:40f0:8", ["const:802b74:8", "const:4:8"]]
+ 00802b74 ["CALL", null, ["ram:802b8c:8"]]
- 00802b34 bytes 06000094
+ 00802b74 bytes 06000094
- 00802b28 ["INT_ADD", "register:40f0:8", ["const:802b28:8", "const:4:8"]]
- 00802b28 ["CALL", null, ["callee:008026b8:8"]]
+ 00802b68 ["INT_ADD", "register:40f0:8", ["const:802b68:8", "const:4:8"]]
+ 00802b68 ["CALL", null, ["callee:008026b8:8"]]
- 00802b28 bytes d4feff97
+ 00802b68 bytes d4feff97
~~~


<a id="compare-044bea614afd2f5c7a3c8b380ac143e1"></a>

### [`00802d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md) → [`00802d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md) FUN_00802d78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00802d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d0c.md) [`00a06590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06590.md) · 呼出先 8件 [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) [`007bbd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md)
- 新版 呼出元 3件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00802d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d4c.md) [`00a0672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a0672c.md) · 呼出先 8件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

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
      "site": "00802df4",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00802db4",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "00802df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "00802e68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "00802df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "00802e68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00802db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md#insn-00802db4) · [`00802d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md#insn-00802d44) · [`00802d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802d38.md#insn-00802d54)
- 新版 [`00802df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802df4) · [`00802d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802d84) · [`00802d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802d78.md#insn-00802d94)

~~~diff
- 00802db4 ["INT_ADD", "register:40f0:8", ["const:802db4:8", "const:4:8"]]
- 00802db4 ["CALL", null, ["ram:802b4c:8"]]
+ 00802df4 ["INT_ADD", "register:40f0:8", ["const:802df4:8", "const:4:8"]]
+ 00802df4 ["CALL", null, ["ram:802b8c:8"]]
- 00802db4 bytes 66ffff97
+ 00802df4 bytes 66ffff97
- 00802d44 ["INT_ADD", "register:40f0:8", ["const:802d44:8", "const:4:8"]]
- 00802d44 ["CALL", null, ["callee:008514f8:8"]]
+ 00802d84 ["INT_ADD", "register:40f0:8", ["const:802d84:8", "const:4:8"]]
+ 00802d84 ["CALL", null, ["callee:008514f8:8"]]
- 00802d44 bytes dd390194
+ 00802d84 bytes dd390194
- 00802d54 ["INT_ADD", "register:40f0:8", ["const:802d54:8", "const:4:8"]]
- 00802d54 ["CALL", null, ["callee:0067674c:8"]]
+ 00802d94 ["INT_ADD", "register:40f0:8", ["const:802d94:8", "const:4:8"]]
+ 00802d94 ["CALL", null, ["callee:0067674c:8"]]
- 00802d54 bytes 6ecef997
+ 00802d94 bytes 6ecef997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d42631f84837834bc8ab037aab26ffd0"></a>

### [`00803170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803170.md) → [`008031b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031b0.md) FUN_008031b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006bed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · 呼出先 3件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) [`008031a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/008031a4.md)
- 新版 呼出元 10件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 3件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`008031e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031e4.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

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
      "site": "008031cc",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0080318c",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "008031cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "008031e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008031a4"
      ]
    ]
  ],
  "added": [
    [
      "008031cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "008031e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008031e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0080318c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803170.md#insn-0080318c) · [`00803180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803170.md#insn-00803180) · [`008031a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803170.md#insn-008031a0)
- 新版 [`008031cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031b0.md#insn-008031cc) · [`008031c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031b0.md#insn-008031c0) · [`008031e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031b0.md#insn-008031e0)

~~~diff
- 0080318c ["INT_ADD", "register:40f0:8", ["const:80318c:8", "const:4:8"]]
- 0080318c ["CALL", null, ["ram:802b4c:8"]]
+ 008031cc ["INT_ADD", "register:40f0:8", ["const:8031cc:8", "const:4:8"]]
+ 008031cc ["CALL", null, ["ram:802b8c:8"]]
- 0080318c bytes 70feff97
+ 008031cc bytes 70feff97
- 00803180 ["INT_ADD", "register:40f0:8", ["const:803180:8", "const:4:8"]]
- 00803180 ["CALL", null, ["callee:008026b8:8"]]
+ 008031c0 ["INT_ADD", "register:40f0:8", ["const:8031c0:8", "const:4:8"]]
+ 008031c0 ["CALL", null, ["callee:008026b8:8"]]
- 00803180 bytes 3efdff97
+ 008031c0 bytes 3efdff97
- 008031a0 ["BRANCH", null, ["ram:8031a4:8"]]
+ 008031e0 ["BRANCH", null, ["ram:8031e4:8"]]
- 008031a0 bytes 01000014
+ 008031e0 bytes 01000014
~~~


<a id="compare-fa675789380879a314bfd64cc2f92c00"></a>

### [`00803da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803da8.md) → [`00803de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803de8.md) FUN_00803de8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`00a9c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9c/00a9c4f4.md) · 呼出先 5件 [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008031a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/008031a4.md) [`00804034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804034.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`00a9c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9c/00a9c6f0.md) · 呼出先 5件 [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`008031e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/008031e4.md) [`00804074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804074.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

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
      "site": "00803e8c",
      "value": [
        "leaf",
        "ram:8031e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00803e4c",
      "value": [
        "leaf",
        "ram:8031a4:8"
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
      "site": "00804014",
      "value": [
        "leaf",
        "ram:804074:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00803fd4",
      "value": [
        "leaf",
        "ram:804034:8"
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
      "00803e8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008031a4"
      ]
    ],
    [
      "00803fdc",
      "READ",
      [
        "storage",
        "00ca7c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00803fdc",
      "READ",
      [
        "storage",
        "00ca7c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00803e8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008031e4"
      ]
    ],
    [
      "00803fdc",
      "READ",
      [
        "storage",
        "00ca8030",
        null,
        "undefined8"
      ]
    ],
    [
      "00803fdc",
      "READ",
      [
        "storage",
        "00ca8038",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00803e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803da8.md#insn-00803e4c) · [`00803fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803da8.md#insn-00803fd4) · [`00803dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803da8.md#insn-00803dc0)
- 新版 [`00803e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803de8.md#insn-00803e8c) · [`00804014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803de8.md#insn-00804014) · [`00803e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00803/00803de8.md#insn-00803e00)

~~~diff
- 00803e4c ["INT_ADD", "register:40f0:8", ["const:803e4c:8", "const:4:8"]]
- 00803e4c ["CALL", null, ["ram:8031a4:8"]]
+ 00803e8c ["INT_ADD", "register:40f0:8", ["const:803e8c:8", "const:4:8"]]
+ 00803e8c ["CALL", null, ["ram:8031e4:8"]]
- 00803e4c bytes d6fcff97
+ 00803e8c bytes d6fcff97
- 00803fd4 ["INT_ADD", "register:40f0:8", ["const:803fd4:8", "const:4:8"]]
- 00803fd4 ["CALL", null, ["ram:804034:8"]]
+ 00804014 ["INT_ADD", "register:40f0:8", ["const:804014:8", "const:4:8"]]
+ 00804014 ["CALL", null, ["ram:804074:8"]]
- 00803fd4 bytes 18000094
+ 00804014 bytes 18000094
- 00803dc0 ["INT_ADD", "register:40f0:8", ["const:803dc0:8", "const:4:8"]]
- 00803dc0 ["CALL", null, ["callee:008514f8:8"]]
+ 00803e00 ["INT_ADD", "register:40f0:8", ["const:803e00:8", "const:4:8"]]
+ 00803e00 ["CALL", null, ["callee:008514f8:8"]]
- 00803dc0 bytes be350194
+ 00803e00 bytes be350194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d3c08f56577e680d716c022c44475e9"></a>

### [`00804328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804328.md) → [`00804368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804368.md) FUN_00804368

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`00a9c4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9c/00a9c4f4.md) · 呼出先 3件 [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00804034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804034.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00a9c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9c/00a9c6f0.md) · 呼出先 3件 [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00804074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804074.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.21% / 新版 96.21%

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
      "site": "00804548",
      "value": [
        "leaf",
        "ram:804074:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00804508",
      "value": [
        "leaf",
        "ram:804034:8"
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
      "008044c4",
      "READ",
      [
        "storage",
        "00ca7c18",
        null,
        "undefined8"
      ]
    ],
    [
      "008044c4",
      "READ",
      [
        "storage",
        "00ca7c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00804514",
      "READ",
      [
        "storage",
        "00ca7c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008044c4",
      "READ",
      [
        "storage",
        "00ca8018",
        null,
        "undefined8"
      ]
    ],
    [
      "008044c4",
      "READ",
      [
        "storage",
        "00ca8020",
        null,
        "undefined8"
      ]
    ],
    [
      "00804514",
      "READ",
      [
        "storage",
        "00ca8030",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00804508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804328.md#insn-00804508) · [`00804354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804328.md#insn-00804354) · [`0080437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804328.md#insn-0080437c)
- 新版 [`00804548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804368.md#insn-00804548) · [`00804394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804368.md#insn-00804394) · [`008043bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804368.md#insn-008043bc)

~~~diff
- 00804508 ["INT_ADD", "register:40f0:8", ["const:804508:8", "const:4:8"]]
- 00804508 ["CALL", null, ["ram:804034:8"]]
+ 00804548 ["INT_ADD", "register:40f0:8", ["const:804548:8", "const:4:8"]]
+ 00804548 ["CALL", null, ["ram:804074:8"]]
- 00804508 bytes cbfeff97
+ 00804548 bytes cbfeff97
- 00804354 ["INT_ADD", "register:40f0:8", ["const:804354:8", "const:4:8"]]
- 00804354 ["CALL", null, ["callee:008514f8:8"]]
+ 00804394 ["INT_ADD", "register:40f0:8", ["const:804394:8", "const:4:8"]]
+ 00804394 ["CALL", null, ["callee:008514f8:8"]]
- 00804354 bytes 59340194
+ 00804394 bytes 59340194
- 0080437c ["COPY", "register:40b8:8", ["const:ca7000:8"]]
+ 008043bc ["COPY", "register:40b8:8", ["const:ca8000:8"]]
- 0080437c bytes 172500f0
+ 008043bc bytes 37250090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5adcc42f2d451c97459ba19771f864d0"></a>

### [`008056ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md) → [`008056ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md) FUN_008056ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0080fa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080fa8c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 39件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`00677a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00677/00677a40.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0080facc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080f/0080facc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0080581c",
      "incomplete_value": false,
      "site": "00805820",
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
      "definition_site": "008057dc",
      "incomplete_value": false,
      "site": "008057e0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00805844",
      "incomplete_value": false,
      "site": "00805848",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00805804",
      "incomplete_value": false,
      "site": "00805808",
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
            "const:d34:8"
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
      "00805764",
      "DATA",
      [
        "storage",
        "0039b738",
        null,
        "dword"
      ]
    ],
    [
      "008057ec",
      "DATA",
      [
        "storage",
        "0039b750",
        null,
        "byte[39]"
      ]
    ],
    [
      "0080581c",
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
      "00805764",
      "DATA",
      [
        "storage",
        "0039b738",
        null,
        "byte[75]"
      ]
    ],
    [
      "008057ec",
      "DATA",
      [
        "storage",
        "0039b750",
        null,
        "byte[75]"
      ]
    ],
    [
      "0080581c",
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

- 旧版 [`008057a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md#insn-008057a0) · [`008057e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md#insn-008057e0) · [`00805808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md#insn-00805808)
- 新版 [`008057e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md#insn-008057e0) · [`00805820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md#insn-00805820) · [`00805848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md#insn-00805848)

~~~diff
- 008057a0 ["INT_ADD", "register:40f0:8", ["const:8057a0:8", "const:4:8"]]
- 008057a0 ["CALL", null, ["callee:008514f8:8"]]
+ 008057e0 ["INT_ADD", "register:40f0:8", ["const:8057e0:8", "const:4:8"]]
+ 008057e0 ["CALL", null, ["callee:008514f8:8"]]
- 008057a0 bytes 462f0194
+ 008057e0 bytes 462f0194
- 008057e0 ["INT_ADD", "register:40f0:8", ["const:8057e0:8", "const:4:8"]]
- 008057e0 ["CALL", null, ["callee:00442930:8"]]
+ 00805820 ["INT_ADD", "register:40f0:8", ["const:805820:8", "const:4:8"]]
+ 00805820 ["CALL", null, ["callee:00442930:8"]]
- 008057e0 bytes 44f4f097
+ 00805820 bytes 44f4f097
- 00805808 ["INT_ADD", "register:40f0:8", ["const:805808:8", "const:4:8"]]
- 00805808 ["CALL", null, ["callee:00442930:8"]]
+ 00805848 ["INT_ADD", "register:40f0:8", ["const:805848:8", "const:4:8"]]
+ 00805848 ["CALL", null, ["callee:00442930:8"]]
- 00805808 bytes 3af4f097
+ 00805848 bytes 3af4f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b204878eb994136eac30ddc5f34c2bf"></a>

### [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md) → [`00805d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md) FUN_00805d34

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006df6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006df6d4.md) [`006dfbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfbec.md) [`0072c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md) [`0072f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) [`007317cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007317cc.md) · 呼出先 5件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0072c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c804.md) [`0072c8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8fc.md) [`00730ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730ce4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 6件 [`006df714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006df714.md) [`006dfc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfc2c.md) [`0072c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md) [`0072f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) [`0073180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md) · 呼出先 5件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0072c844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c844.md) [`0072c93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c93c.md) [`00730d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730d24.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.68% / 新版 94.68%

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
      "site": "00805e10",
      "value": [
        "leaf",
        "ram:72c844:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00805dd0",
      "value": [
        "leaf",
        "ram:72c804:8"
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
      "00805d60",
      "DATA",
      [
        "storage",
        "002ec9c2",
        "switchD_00805d28::switchdataD_002ec9c2",
        "byte"
      ]
    ],
    [
      "00805e10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072c804"
      ]
    ],
    [
      "00805e48",
      "DATA",
      [
        "storage",
        "0038c8d0",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00805d60",
      "DATA",
      [
        "storage",
        "002eca02",
        "switchD_00805d68::switchdataD_002eca02",
        "byte"
      ]
    ],
    [
      "00805e10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072c844"
      ]
    ],
    [
      "00805e48",
      "DATA",
      [
        "storage",
        "0038c8d0",
        "fde_0038c8d0",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00805dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md#insn-00805dd0) · [`00805e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md#insn-00805e10) · [`00805d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md#insn-00805d14)
- 新版 [`00805e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md#insn-00805e10) · [`00805e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md#insn-00805e50) · [`00805d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805d34.md#insn-00805d54)

~~~diff
- 00805dd0 ["INT_ADD", "register:40f0:8", ["const:805dd0:8", "const:4:8"]]
- 00805dd0 ["CALL", null, ["ram:72c804:8"]]
+ 00805e10 ["INT_ADD", "register:40f0:8", ["const:805e10:8", "const:4:8"]]
+ 00805e10 ["CALL", null, ["ram:72c844:8"]]
- 00805dd0 bytes 8d9afc97
+ 00805e10 bytes 8d9afc97
- 00805e10 ["INT_ADD", "register:40f0:8", ["const:805e10:8", "const:4:8"]]
- 00805e10 ["CALL", null, ["callee:008514f8:8"]]
+ 00805e50 ["INT_ADD", "register:40f0:8", ["const:805e50:8", "const:4:8"]]
+ 00805e50 ["CALL", null, ["callee:008514f8:8"]]
- 00805e10 bytes aa2d0194
+ 00805e50 bytes aa2d0194
- 00805d14 ["COPY", "tmp:0:8", ["const:9c2:8"]]
- 00805d14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00805d14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00805d14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00805d54 ["COPY", "tmp:0:8", ["const:a02:8"]]
+ 00805d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00805d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00805d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00805d14 bytes 29092791
+ 00805d54 bytes 29092891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

