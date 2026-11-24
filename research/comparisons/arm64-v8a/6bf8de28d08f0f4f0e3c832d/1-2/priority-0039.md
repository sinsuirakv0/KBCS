# v16.0.1 → v16.0.2 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-feb2986f680c5907422d453df17c82e3"></a>

### [`0079d994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md) → [`0079d9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md) FUN_0079d9ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079da10",
      "incomplete_value": false,
      "site": "0079da10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d9b8",
      "incomplete_value": false,
      "site": "0079d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "0079da10",
      "DATA",
      [
        "storage",
        "00c79e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079da10",
      "DATA",
      [
        "storage",
        "00c79f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md#insn-0079d9a8) · [`0079d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d994.md#insn-0079d9b4)
- 新版 [`0079da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md#insn-0079da00) · [`0079da0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md#insn-0079da0c)

~~~diff
- 0079d9a8 ["INT_ADD", "register:40f0:8", ["const:79d9a8:8", "const:4:8"]]
- 0079d9a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079da00 ["INT_ADD", "register:40f0:8", ["const:79da00:8", "const:4:8"]]
+ 0079da00 ["CALL", null, ["callee:00c57f60:8"]]
- 0079d9a8 bytes 3ae91294
+ 0079da00 bytes 58e91294
- 0079d9b4 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0079d9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079da0c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0079da0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079da0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079da0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d9b4 bytes 08a13991
+ 0079da0c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8717105e8633f7a1d2d15d92606c699f"></a>

### [`0079d9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9c8.md) → [`0079da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da20.md) FUN_0079da20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079da2c",
      "incomplete_value": false,
      "site": "0079da2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d9d4",
      "incomplete_value": false,
      "site": "0079d9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "0079da2c",
      "DATA",
      [
        "storage",
        "00c79e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079da2c",
      "DATA",
      [
        "storage",
        "00c79f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9c8.md#insn-0079d9d0)
- 新版 [`0079da28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da20.md#insn-0079da28)

~~~diff
- 0079d9d0 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0079d9d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079d9d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079d9d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079da28 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0079da28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079da28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079da28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079d9d0 bytes 29a13991
+ 0079da28 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b3135f29f4e08a6e6789d51193167a7"></a>

### [`0079d9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md) → [`0079da3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md) FUN_0079da3c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) [`0079b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b280.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md) [`0079b2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

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
      "site": "0079da64",
      "value": [
        "leaf",
        "ram:768ee8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079da0c",
      "value": [
        "leaf",
        "ram:768e90:8"
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
      "0079da64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ]
  ],
  "added": [
    [
      "0079da64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da0c) · [`0079da04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da04) · [`0079da90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md#insn-0079da90)
- 新版 [`0079da64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079da64) · [`0079da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079da5c) · [`0079dae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079dae8)

~~~diff
- 0079da0c ["INT_ADD", "register:40f0:8", ["const:79da0c:8", "const:4:8"]]
- 0079da0c ["CALL", null, ["ram:768e90:8"]]
+ 0079da64 ["INT_ADD", "register:40f0:8", ["const:79da64:8", "const:4:8"]]
+ 0079da64 ["CALL", null, ["ram:768ee8:8"]]
- 0079da0c bytes 212dff97
+ 0079da64 bytes 212dff97
- 0079da04 ["INT_ADD", "register:40f0:8", ["const:79da04:8", "const:4:8"]]
- 0079da04 ["CALL", null, ["callee:00851550:8"]]
+ 0079da5c ["INT_ADD", "register:40f0:8", ["const:79da5c:8", "const:4:8"]]
+ 0079da5c ["CALL", null, ["callee:00851550:8"]]
- 0079da04 bytes bdce0294
+ 0079da5c bytes bdce0294
- 0079da90 ["INT_ADD", "register:40f0:8", ["const:79da90:8", "const:4:8"]]
- 0079da90 ["CALL", null, ["callee:00459db4:8"]]
+ 0079dae8 ["INT_ADD", "register:40f0:8", ["const:79dae8:8", "const:4:8"]]
+ 0079dae8 ["CALL", null, ["callee:00459db4:8"]]
- 0079da90 bytes b9f0f297
+ 0079dae8 bytes b3f0f297
~~~


<a id="compare-84557618ef63087d9bcb021b62223f6e"></a>

### [`0079dac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md) → [`0079db1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md) FUN_0079db1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079db40",
      "incomplete_value": false,
      "site": "0079db40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dae8",
      "incomplete_value": false,
      "site": "0079dae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "0079db40",
      "DATA",
      [
        "storage",
        "00c79ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079db40",
      "DATA",
      [
        "storage",
        "00c79fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md#insn-0079dad8) · [`0079dae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dac4.md#insn-0079dae4)
- 新版 [`0079db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md#insn-0079db30) · [`0079db3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md#insn-0079db3c)

~~~diff
- 0079dad8 ["INT_ADD", "register:40f0:8", ["const:79dad8:8", "const:4:8"]]
- 0079dad8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079db30 ["INT_ADD", "register:40f0:8", ["const:79db30:8", "const:4:8"]]
+ 0079db30 ["CALL", null, ["callee:00c57f60:8"]]
- 0079dad8 bytes eee81294
+ 0079db30 bytes 0ce91294
- 0079dae4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0079dae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079db3c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0079db3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079db3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079db3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dae4 bytes 08a13b91
+ 0079db3c bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c812d6039a1bed5d7732661958ff874"></a>

### [`0079daf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079daf8.md) → [`0079db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db50.md) FUN_0079db50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079db5c",
      "incomplete_value": false,
      "site": "0079db5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db04",
      "incomplete_value": false,
      "site": "0079db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "0079db5c",
      "DATA",
      [
        "storage",
        "00c79ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079db5c",
      "DATA",
      [
        "storage",
        "00c79fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079daf8.md#insn-0079db00)
- 新版 [`0079db58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db50.md#insn-0079db58)

~~~diff
- 0079db00 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0079db00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079db00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079db00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079db58 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0079db58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079db58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079db00 bytes 29a13b91
+ 0079db58 bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f875d268f2704f47679c20e36ed50b9e"></a>

### [`0079db48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md) → [`0079dba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md) FUN_0079dba0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079dbc4",
      "incomplete_value": false,
      "site": "0079dbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db6c",
      "incomplete_value": false,
      "site": "0079db6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "0079dbc4",
      "DATA",
      [
        "storage",
        "00c79f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dbc4",
      "DATA",
      [
        "storage",
        "00c7a048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md#insn-0079db5c) · [`0079db64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md#insn-0079db64) · [`0079db68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db48.md#insn-0079db68)
- 新版 [`0079dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbb4) · [`0079dbbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbbc) · [`0079dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbc0)

~~~diff
- 0079db5c ["INT_ADD", "register:40f0:8", ["const:79db5c:8", "const:4:8"]]
- 0079db5c ["CALL", null, ["callee:00c57f60:8"]]
+ 0079dbb4 ["INT_ADD", "register:40f0:8", ["const:79dbb4:8", "const:4:8"]]
+ 0079dbb4 ["CALL", null, ["callee:00c57f60:8"]]
- 0079db5c bytes cde81294
+ 0079dbb4 bytes ebe81294
- 0079db64 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079dbbc ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079db64 bytes e8260090
+ 0079dbbc bytes e82600b0
- 0079db68 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0079db68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079db68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079db68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dbc0 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0079dbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079db68 bytes 08e13d91
+ 0079dbc0 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a22bc72c5de8d9c4b14e0b9a7df74157"></a>

### [`0079db7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db7c.md) → [`0079dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md) FUN_0079dbd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079dbe0",
      "incomplete_value": false,
      "site": "0079dbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db88",
      "incomplete_value": false,
      "site": "0079db88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "0079dbe0",
      "DATA",
      [
        "storage",
        "00c79f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dbe0",
      "DATA",
      [
        "storage",
        "00c7a048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db7c.md#insn-0079db80) · [`0079db84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db7c.md#insn-0079db84)
- 新版 [`0079dbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md#insn-0079dbd8) · [`0079dbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md#insn-0079dbdc)

~~~diff
- 0079db80 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079dbd8 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079db80 bytes e9260090
+ 0079dbd8 bytes e92600b0
- 0079db84 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0079db84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079db84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079db84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dbdc ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0079dbdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dbdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dbdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079db84 bytes 29e13d91
+ 0079dbdc bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f366779cb69508991b5e6334f789315e"></a>

### [`0079dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md) → [`0079dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md) FUN_0079dc98

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079dcbc",
      "incomplete_value": false,
      "site": "0079dcbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dc64",
      "incomplete_value": false,
      "site": "0079dc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "0079dcbc",
      "DATA",
      [
        "storage",
        "00c79ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dcbc",
      "DATA",
      [
        "storage",
        "00c7a0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md#insn-0079dc54) · [`0079dc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md#insn-0079dc5c) · [`0079dc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc40.md#insn-0079dc60)
- 新版 [`0079dcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md#insn-0079dcac) · [`0079dcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md#insn-0079dcb4) · [`0079dcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md#insn-0079dcb8)

~~~diff
- 0079dc54 ["INT_ADD", "register:40f0:8", ["const:79dc54:8", "const:4:8"]]
- 0079dc54 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079dcac ["INT_ADD", "register:40f0:8", ["const:79dcac:8", "const:4:8"]]
+ 0079dcac ["CALL", null, ["callee:00c57f60:8"]]
- 0079dc54 bytes 8fe81294
+ 0079dcac bytes ade81294
- 0079dc5c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079dcb4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079dc5c bytes e8260090
+ 0079dcb4 bytes e82600b0
- 0079dc60 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 0079dc60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dc60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dc60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dcb8 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 0079dcb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dcb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dcb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dc60 bytes 08e13f91
+ 0079dcb8 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997fb75ab3183594e8ec770072994126"></a>

### [`0079dc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc74.md) → [`0079dccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md) FUN_0079dccc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079dcd8",
      "incomplete_value": false,
      "site": "0079dcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dc80",
      "incomplete_value": false,
      "site": "0079dc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "0079dcd8",
      "DATA",
      [
        "storage",
        "00c79ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dcd8",
      "DATA",
      [
        "storage",
        "00c7a0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc74.md#insn-0079dc78) · [`0079dc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dc74.md#insn-0079dc7c)
- 新版 [`0079dcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md#insn-0079dcd0) · [`0079dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md#insn-0079dcd4)

~~~diff
- 0079dc78 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079dcd0 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079dc78 bytes e9260090
+ 0079dcd0 bytes e92600b0
- 0079dc7c ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 0079dc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dcd4 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 0079dcd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dcd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dcd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dc7c bytes 29e13f91
+ 0079dcd4 bytes 29210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8462519cbe21c51175ec369c2dd443"></a>

### [`0079dcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md) → [`0079dd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md) FUN_0079dd1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079dd40",
      "incomplete_value": false,
      "site": "0079dd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dce8",
      "incomplete_value": false,
      "site": "0079dce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "0079dd40",
      "DATA",
      [
        "storage",
        "00c7a088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dd40",
      "DATA",
      [
        "storage",
        "00c7a158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md#insn-0079dcd8) · [`0079dce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcc4.md#insn-0079dce4)
- 新版 [`0079dd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md#insn-0079dd30) · [`0079dd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md#insn-0079dd3c)

~~~diff
- 0079dcd8 ["INT_ADD", "register:40f0:8", ["const:79dcd8:8", "const:4:8"]]
- 0079dcd8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079dd30 ["INT_ADD", "register:40f0:8", ["const:79dd30:8", "const:4:8"]]
+ 0079dd30 ["CALL", null, ["callee:00c57f60:8"]]
- 0079dcd8 bytes 6ee81294
+ 0079dd30 bytes 8ce81294
- 0079dce4 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0079dce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dd3c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0079dd3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dd3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dd3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dce4 bytes 08210291
+ 0079dd3c bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116df3d0a1b90a5deab090e23af636a8"></a>

### [`0079dcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcf8.md) → [`0079dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd50.md) FUN_0079dd50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079dd5c",
      "incomplete_value": false,
      "site": "0079dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dd04",
      "incomplete_value": false,
      "site": "0079dd04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "0079dd5c",
      "DATA",
      [
        "storage",
        "00c7a088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dd5c",
      "DATA",
      [
        "storage",
        "00c7a158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079dcf8.md#insn-0079dd00)
- 新版 [`0079dd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd50.md#insn-0079dd58)

~~~diff
- 0079dd00 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0079dd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dd58 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0079dd58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dd00 bytes 29210291
+ 0079dd58 bytes 29610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12324029dbb707edf50f9cc88d2aaeff"></a>

### [`0079ddb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md) → [`0079de0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md) FUN_0079de0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "0079de44",
      "incomplete_value": false,
      "site": "0079de4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ddec",
      "incomplete_value": false,
      "site": "0079ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "0079de4c",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079df04",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079de4c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "0079df04",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079dde4) · [`0079ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079ddec) · [`0079ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079ddb4.md#insn-0079ddf0)
- 新版 [`0079de3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md#insn-0079de3c) · [`0079de44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md#insn-0079de44)

~~~diff
- 0079dde4 ["INT_ADD", "register:40f0:8", ["const:79dde4:8", "const:4:8"]]
- 0079dde4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079de3c ["INT_ADD", "register:40f0:8", ["const:79de3c:8", "const:4:8"]]
+ 0079de3c ["CALL", null, ["callee:00c57f60:8"]]
- 0079dde4 bytes 2be81294
+ 0079de3c bytes 49e81294
- 0079ddec ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 0079ddec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079ddec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079ddec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079de44 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 0079de44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079de44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079de44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079ddec bytes 08011791
+ 0079de44 bytes 08411a91
- 0079ddf0 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0079ddf0 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44cddc916c1a8575ed63be6111dc6298"></a>

### [`0079df2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md) → [`0079df84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md) FUN_0079df84

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079df9c",
      "incomplete_value": false,
      "site": "0079dfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079df44",
      "incomplete_value": false,
      "site": "0079df54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "0079dfac",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dfac",
      "DATA",
      [
        "storage",
        "00c7a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079df44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md#insn-0079df44) · [`0079df78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079df2c.md#insn-0079df78)
- 新版 [`0079df9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md#insn-0079df9c) · [`0079dfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md#insn-0079dfd0)

~~~diff
- 0079df44 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0079df44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079df44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079df44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0079df9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079df44 bytes 08210491
+ 0079df9c bytes 08610791
- 0079df78 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079df78 ["INT_ADD", "register:40f0:8", ["const:79df78:8", "const:4:8"]]
- 0079df78 ["CALLIND", null, ["register:0:8"]]
+ 0079dfd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079dfd0 ["INT_ADD", "register:40f0:8", ["const:79dfd0:8", "const:4:8"]]
+ 0079dfd0 ["CALLIND", null, ["register:0:8"]]
- 0079df78 bytes 00013fd6
+ 0079dfd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cc57c93666fdfd2b92c4d70c01f8d16"></a>

### [`0079e048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md) → [`0079e0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md) FUN_0079e0a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079e0d0",
      "incomplete_value": false,
      "site": "0079e0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e078",
      "incomplete_value": false,
      "site": "0079e078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "0079e0d0",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e0d0",
      "DATA",
      [
        "storage",
        "00c7a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e0d0) · [`0079e060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e060) · [`0079e070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e048.md#insn-0079e070)
- 新版 [`0079e128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e128) · [`0079e0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e0b8) · [`0079e0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e0c8)

~~~diff
- 0079e0d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e0d0 ["INT_ADD", "register:40f0:8", ["const:79e0d0:8", "const:4:8"]]
- 0079e0d0 ["CALLIND", null, ["register:0:8"]]
+ 0079e128 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e128 ["INT_ADD", "register:40f0:8", ["const:79e128:8", "const:4:8"]]
+ 0079e128 ["CALLIND", null, ["register:0:8"]]
- 0079e0d0 bytes 00013fd6
+ 0079e128 bytes 00013fd6
- 0079e060 ["INT_ADD", "register:40f0:8", ["const:79e060:8", "const:4:8"]]
- 0079e060 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079e0b8 ["INT_ADD", "register:40f0:8", ["const:79e0b8:8", "const:4:8"]]
+ 0079e0b8 ["CALL", null, ["callee:00c57f60:8"]]
- 0079e060 bytes 8ce71294
+ 0079e0b8 bytes aae71294
- 0079e070 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0079e070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e0c8 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0079e0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e070 bytes 08210491
+ 0079e0c8 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63355d4822b1b4062406662df490fd5"></a>

### [`0079e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md) → [`0079e1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e1a8.md) FUN_0079e1a8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "0079e1d0",
      "incomplete_value": false,
      "site": "0079e1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e178",
      "incomplete_value": false,
      "site": "0079e178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "0079e1d0",
      "DATA",
      [
        "storage",
        "00c7a108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e1d0",
      "DATA",
      [
        "storage",
        "00c7a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md#insn-0079e170) · [`0079e174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md#insn-0079e174) · [`0079e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e150.md#insn-0079e194)
- 新版 [`0079e1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e1a8.md#insn-0079e1c8) · [`0079e1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e1a8.md#insn-0079e1ec)

~~~diff
- 0079e170 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0079e170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e1c8 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0079e1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e170 bytes 08210491
+ 0079e1c8 bytes 08610791
- 0079e174 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0079e174 bytes f40301aa
- 0079e194 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e194 ["INT_ADD", "register:40f0:8", ["const:79e194:8", "const:4:8"]]
- 0079e194 ["CALLIND", null, ["register:0:8"]]
+ 0079e1ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e1ec ["INT_ADD", "register:40f0:8", ["const:79e1ec:8", "const:4:8"]]
+ 0079e1ec ["CALLIND", null, ["register:0:8"]]
- 0079e194 bytes 00013fd6
+ 0079e1ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d3a7cb686f7456429913f27a5f55d8d"></a>

### [`0079e4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4f4.md) → [`0079e54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md) FUN_0079e54c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079e558",
      "incomplete_value": false,
      "site": "0079e564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e500",
      "incomplete_value": false,
      "site": "0079e50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "0079e564",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e564",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e4f4.md#insn-0079e500)
- 新版 [`0079e558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md#insn-0079e558)

~~~diff
- 0079e500 ["COPY", "tmp:0:8", ["const:188:8"]]
- 0079e500 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079e500 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079e500 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079e558 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0079e558 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e558 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e558 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079e500 bytes 4a210691
+ 0079e558 bytes 4a610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b7453f3154487159857ada3674f9e3e"></a>

### [`0079e594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md) → [`0079e5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md) FUN_0079e5ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079e618",
      "incomplete_value": false,
      "site": "0079e618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e5c0",
      "incomplete_value": false,
      "site": "0079e5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "0079e618",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e618",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5a8) · [`0079e5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5b8) · [`0079e5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e594.md#insn-0079e5dc)
- 新版 [`0079e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md#insn-0079e600) · [`0079e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md#insn-0079e610) · [`0079e634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md#insn-0079e634)

~~~diff
- 0079e5a8 ["INT_ADD", "register:40f0:8", ["const:79e5a8:8", "const:4:8"]]
- 0079e5a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079e600 ["INT_ADD", "register:40f0:8", ["const:79e600:8", "const:4:8"]]
+ 0079e600 ["CALL", null, ["callee:00c57f60:8"]]
- 0079e5a8 bytes 3ae61294
+ 0079e600 bytes 58e61294
- 0079e5b8 ["COPY", "tmp:0:8", ["const:188:8"]]
- 0079e5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e610 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0079e610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e5b8 bytes 08210691
+ 0079e610 bytes 08610991
- 0079e5dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e5dc ["INT_ADD", "register:40f0:8", ["const:79e5dc:8", "const:4:8"]]
- 0079e5dc ["CALLIND", null, ["register:0:8"]]
+ 0079e634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e634 ["INT_ADD", "register:40f0:8", ["const:79e634:8", "const:4:8"]]
+ 0079e634 ["CALLIND", null, ["register:0:8"]]
- 0079e5dc bytes 00013fd6
+ 0079e634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a4c04487e4a06c62f55710bce9ceb8b"></a>

### [`0079e61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md) → [`0079e674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md) FUN_0079e674

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079e690",
      "incomplete_value": false,
      "site": "0079e690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e638",
      "incomplete_value": false,
      "site": "0079e638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "0079e690",
      "DATA",
      [
        "storage",
        "00c7a188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e690",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md#insn-0079e634) · [`0079e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e61c.md#insn-0079e658)
- 新版 [`0079e68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md#insn-0079e68c) · [`0079e6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md#insn-0079e6b0)

~~~diff
- 0079e634 ["COPY", "tmp:0:8", ["const:188:8"]]
- 0079e634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079e634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079e634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079e68c ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0079e68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079e634 bytes 29210691
+ 0079e68c bytes 29610991
- 0079e658 ["COPY", "register:0:8", ["register:4048:8"]]
- 0079e658 ["INT_ADD", "register:40f0:8", ["const:79e658:8", "const:4:8"]]
- 0079e658 ["CALLIND", null, ["register:0:8"]]
+ 0079e6b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079e6b0 ["INT_ADD", "register:40f0:8", ["const:79e6b0:8", "const:4:8"]]
+ 0079e6b0 ["CALLIND", null, ["register:0:8"]]
- 0079e658 bytes 20013fd6
+ 0079e6b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1104881fb1a14c3c95c2a104fde3beb"></a>

### [`0079e760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md) → [`0079e7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md) FUN_0079e7b8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "0079e7f0",
      "incomplete_value": false,
      "site": "0079e7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e798",
      "incomplete_value": false,
      "site": "0079e7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "0079e7f8",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "0079e8b0",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e7f8",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "0079e8b0",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e790) · [`0079e798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e798) · [`0079e79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e760.md#insn-0079e79c)
- 新版 [`0079e7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md#insn-0079e7e8) · [`0079e7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md#insn-0079e7f0)

~~~diff
- 0079e790 ["INT_ADD", "register:40f0:8", ["const:79e790:8", "const:4:8"]]
- 0079e790 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079e7e8 ["INT_ADD", "register:40f0:8", ["const:79e7e8:8", "const:4:8"]]
+ 0079e7e8 ["CALL", null, ["callee:00c57f60:8"]]
- 0079e790 bytes c0e51294
+ 0079e7e8 bytes dee51294
- 0079e798 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 0079e798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e7f0 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 0079e7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e798 bytes 08011791
+ 0079e7f0 bytes 08411a91
- 0079e79c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0079e79c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ebaecfc19e9b1fe61fb5bd1aaeeef3c"></a>

### [`0079e8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md) → [`0079e930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md) FUN_0079e930

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079e948",
      "incomplete_value": false,
      "site": "0079e958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e8f0",
      "incomplete_value": false,
      "site": "0079e900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "0079e958",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e958",
      "DATA",
      [
        "storage",
        "00c7a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md#insn-0079e8f0) · [`0079e924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e8d8.md#insn-0079e924)
- 新版 [`0079e948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md#insn-0079e948) · [`0079e97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md#insn-0079e97c)

~~~diff
- 0079e8f0 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0079e8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e948 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0079e948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e8f0 bytes 08210891
+ 0079e948 bytes 08610b91
- 0079e924 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e924 ["INT_ADD", "register:40f0:8", ["const:79e924:8", "const:4:8"]]
- 0079e924 ["CALLIND", null, ["register:0:8"]]
+ 0079e97c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079e97c ["INT_ADD", "register:40f0:8", ["const:79e97c:8", "const:4:8"]]
+ 0079e97c ["CALLIND", null, ["register:0:8"]]
- 0079e924 bytes 00013fd6
+ 0079e97c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5d34530f5675844bfa04853edc55ce0"></a>

### [`0079e968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md) → [`0079e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md) FUN_0079e9c0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0079e9d8",
      "incomplete_value": false,
      "site": "0079e9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e980",
      "incomplete_value": false,
      "site": "0079e990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "0079e9e8",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e9e8",
      "DATA",
      [
        "storage",
        "00c7a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e980) · [`0079e9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e9b4) · [`0079e9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079e968.md#insn-0079e9e0)
- 新版 [`0079e9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079e9d8) · [`0079ea0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079ea0c) · [`0079ea38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079ea38)

~~~diff
- 0079e980 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0079e980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e9d8 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0079e9d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e9d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e9d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e980 bytes 08210891
+ 0079e9d8 bytes 08610b91
- 0079e9b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e9b4 ["INT_ADD", "register:40f0:8", ["const:79e9b4:8", "const:4:8"]]
- 0079e9b4 ["CALLIND", null, ["register:0:8"]]
+ 0079ea0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ea0c ["INT_ADD", "register:40f0:8", ["const:79ea0c:8", "const:4:8"]]
+ 0079ea0c ["CALLIND", null, ["register:0:8"]]
- 0079e9b4 bytes 00013fd6
+ 0079ea0c bytes 00013fd6
- 0079e9e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e9e0 ["INT_ADD", "register:40f0:8", ["const:79e9e0:8", "const:4:8"]]
- 0079e9e0 ["CALLIND", null, ["register:0:8"]]
+ 0079ea38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ea38 ["INT_ADD", "register:40f0:8", ["const:79ea38:8", "const:4:8"]]
+ 0079ea38 ["CALLIND", null, ["register:0:8"]]
- 0079e9e0 bytes 00013fd6
+ 0079ea38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-956b116703c0a9d429935d970b46f81e"></a>

### [`0079eafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md) → [`0079eb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md) FUN_0079eb54

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "0079eb7c",
      "incomplete_value": false,
      "site": "0079eb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079eb24",
      "incomplete_value": false,
      "site": "0079eb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "0079eb7c",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079eb7c",
      "DATA",
      [
        "storage",
        "00c7a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md#insn-0079eb1c) · [`0079eb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md#insn-0079eb20) · [`0079eb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eafc.md#insn-0079eb40)
- 新版 [`0079eb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md#insn-0079eb74) · [`0079eb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md#insn-0079eb98)

~~~diff
- 0079eb1c ["COPY", "tmp:0:8", ["const:208:8"]]
- 0079eb1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079eb1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079eb1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079eb74 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0079eb74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eb74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079eb74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079eb1c bytes 08210891
+ 0079eb74 bytes 08610b91
- 0079eb20 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0079eb20 bytes f40301aa
- 0079eb40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079eb40 ["INT_ADD", "register:40f0:8", ["const:79eb40:8", "const:4:8"]]
- 0079eb40 ["CALLIND", null, ["register:0:8"]]
+ 0079eb98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079eb98 ["INT_ADD", "register:40f0:8", ["const:79eb98:8", "const:4:8"]]
+ 0079eb98 ["CALLIND", null, ["register:0:8"]]
- 0079eb40 bytes 00013fd6
+ 0079eb98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c66d83b3006c75763651251b652c2f5f"></a>

### [`0079ee88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee88.md) → [`0079eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eee0.md) FUN_0079eee0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079eeec",
      "incomplete_value": false,
      "site": "0079eef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ee94",
      "incomplete_value": false,
      "site": "0079eea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "0079eef8",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079eef8",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ee94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ee88.md#insn-0079ee94)
- 新版 [`0079eeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eee0.md#insn-0079eeec)

~~~diff
- 0079ee94 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0079ee94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079ee94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079ee94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079eeec ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0079eeec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079eeec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079eeec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079ee94 bytes 4a210a91
+ 0079eeec bytes 4a610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b729968f590959e866507efc1baab6"></a>

### [`0079eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md) → [`0079ef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md) FUN_0079ef24

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0079ef3c",
      "incomplete_value": false,
      "site": "0079ef48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079eee4",
      "incomplete_value": false,
      "site": "0079eef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "0079ef48",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ef48",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md#insn-0079eee4) · [`0079ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079eecc.md#insn-0079ef14)
- 新版 [`0079ef3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md#insn-0079ef3c) · [`0079ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md#insn-0079ef6c)

~~~diff
- 0079eee4 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0079eee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079eee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079eee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079ef3c ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0079ef3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ef3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079ef3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079eee4 bytes 08210a91
+ 0079ef3c bytes 08610d91
- 0079ef14 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ef14 ["INT_ADD", "register:40f0:8", ["const:79ef14:8", "const:4:8"]]
- 0079ef14 ["CALLIND", null, ["register:0:8"]]
+ 0079ef6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ef6c ["INT_ADD", "register:40f0:8", ["const:79ef6c:8", "const:4:8"]]
+ 0079ef6c ["CALLIND", null, ["register:0:8"]]
- 0079ef14 bytes 00013fd6
+ 0079ef6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-180ffbfe34c76b57a04a0c081a32e4b2"></a>

### [`0079ef28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md) → [`0079ef80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md) FUN_0079ef80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079efac",
      "incomplete_value": false,
      "site": "0079efac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ef54",
      "incomplete_value": false,
      "site": "0079ef54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "0079efac",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079efac",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ef3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef3c) · [`0079ef4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef4c) · [`0079ef70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079ef28.md#insn-0079ef70)
- 新版 [`0079ef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079ef94) · [`0079efa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079efa4) · [`0079efc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079efc8)

~~~diff
- 0079ef3c ["INT_ADD", "register:40f0:8", ["const:79ef3c:8", "const:4:8"]]
- 0079ef3c ["CALL", null, ["callee:00c57f60:8"]]
+ 0079ef94 ["INT_ADD", "register:40f0:8", ["const:79ef94:8", "const:4:8"]]
+ 0079ef94 ["CALL", null, ["callee:00c57f60:8"]]
- 0079ef3c bytes d5e31294
+ 0079ef94 bytes f3e31294
- 0079ef4c ["COPY", "tmp:0:8", ["const:288:8"]]
- 0079ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079efa4 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0079efa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079efa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079efa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079ef4c bytes 08210a91
+ 0079efa4 bytes 08610d91
- 0079ef70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ef70 ["INT_ADD", "register:40f0:8", ["const:79ef70:8", "const:4:8"]]
- 0079ef70 ["CALLIND", null, ["register:0:8"]]
+ 0079efc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079efc8 ["INT_ADD", "register:40f0:8", ["const:79efc8:8", "const:4:8"]]
+ 0079efc8 ["CALLIND", null, ["register:0:8"]]
- 0079ef70 bytes 00013fd6
+ 0079efc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41025ad5bbad6c5889cb8bfefdcfd2bb"></a>

### [`0079efb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md) → [`0079f008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md) FUN_0079f008

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079f024",
      "incomplete_value": false,
      "site": "0079f024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079efcc",
      "incomplete_value": false,
      "site": "0079efcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "0079f024",
      "DATA",
      [
        "storage",
        "00c7a288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f024",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079efc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md#insn-0079efc8) · [`0079efec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079e/0079efb0.md#insn-0079efec)
- 新版 [`0079f020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md#insn-0079f020) · [`0079f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md#insn-0079f044)

~~~diff
- 0079efc8 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0079efc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079efc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079efc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079f020 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0079f020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079efc8 bytes 29210a91
+ 0079f020 bytes 29610d91
- 0079efec ["COPY", "register:0:8", ["register:4048:8"]]
- 0079efec ["INT_ADD", "register:40f0:8", ["const:79efec:8", "const:4:8"]]
- 0079efec ["CALLIND", null, ["register:0:8"]]
+ 0079f044 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079f044 ["INT_ADD", "register:40f0:8", ["const:79f044:8", "const:4:8"]]
+ 0079f044 ["CALLIND", null, ["register:0:8"]]
- 0079efec bytes 20013fd6
+ 0079f044 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a77e7db6e3052df942509ca3696be1"></a>

### [`0079f26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md) → [`0079f2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md) FUN_0079f2c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079f2dc",
      "incomplete_value": true,
      "site": "0079f2ec",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f284",
      "incomplete_value": true,
      "site": "0079f294",
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
            "const:308:8"
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
      "0079f2ec",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f2ec",
      "DATA",
      [
        "storage",
        "00c7a3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md#insn-0079f284) · [`0079f2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f26c.md#insn-0079f2b8)
- 新版 [`0079f2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md#insn-0079f2dc) · [`0079f310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md#insn-0079f310)

~~~diff
- 0079f284 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0079f284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f2dc ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0079f2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f284 bytes 08210c91
+ 0079f2dc bytes 08610f91
- 0079f2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f2b8 ["INT_ADD", "register:40f0:8", ["const:79f2b8:8", "const:4:8"]]
- 0079f2b8 ["CALLIND", null, ["register:0:8"]]
+ 0079f310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f310 ["INT_ADD", "register:40f0:8", ["const:79f310:8", "const:4:8"]]
+ 0079f310 ["CALLIND", null, ["register:0:8"]]
- 0079f2b8 bytes 00013fd6
+ 0079f310 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37c8fa8acbbd00bf381fe5038ea4fed9"></a>

### [`0079f388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md) → [`0079f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md) FUN_0079f3e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079f410",
      "incomplete_value": false,
      "site": "0079f410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f3b8",
      "incomplete_value": false,
      "site": "0079f3b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "0079f410",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f410",
      "DATA",
      [
        "storage",
        "00c7a3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f410) · [`0079f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f3a0) · [`0079f3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f388.md#insn-0079f3b0)
- 新版 [`0079f468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f468) · [`0079f3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f3f8) · [`0079f408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f408)

~~~diff
- 0079f410 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f410 ["INT_ADD", "register:40f0:8", ["const:79f410:8", "const:4:8"]]
- 0079f410 ["CALLIND", null, ["register:0:8"]]
+ 0079f468 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f468 ["INT_ADD", "register:40f0:8", ["const:79f468:8", "const:4:8"]]
+ 0079f468 ["CALLIND", null, ["register:0:8"]]
- 0079f410 bytes 00013fd6
+ 0079f468 bytes 00013fd6
- 0079f3a0 ["INT_ADD", "register:40f0:8", ["const:79f3a0:8", "const:4:8"]]
- 0079f3a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079f3f8 ["INT_ADD", "register:40f0:8", ["const:79f3f8:8", "const:4:8"]]
+ 0079f3f8 ["CALL", null, ["callee:00c57f60:8"]]
- 0079f3a0 bytes bce21294
+ 0079f3f8 bytes dae21294
- 0079f3b0 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0079f3b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f3b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f3b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f408 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0079f408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f3b0 bytes 08210c91
+ 0079f408 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f452022a64af9bdaf1070bcd27425a0e"></a>

### [`0079f490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md) → [`0079f4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f4e8.md) FUN_0079f4e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079f510",
      "incomplete_value": false,
      "site": "0079f510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f4b8",
      "incomplete_value": false,
      "site": "0079f4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "0079f510",
      "DATA",
      [
        "storage",
        "00c7a308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f510",
      "DATA",
      [
        "storage",
        "00c7a3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f4b0) · [`0079f4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f4d4) · [`0079f50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f490.md#insn-0079f50c)
- 新版 [`0079f508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f4e8.md#insn-0079f508) · [`0079f52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f4e8.md#insn-0079f52c) · [`0079f564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f4e8.md#insn-0079f564)

~~~diff
- 0079f4b0 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0079f4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f508 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0079f508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f4b0 bytes 08210c91
+ 0079f508 bytes 08610f91
- 0079f4d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f4d4 ["INT_ADD", "register:40f0:8", ["const:79f4d4:8", "const:4:8"]]
- 0079f4d4 ["CALLIND", null, ["register:0:8"]]
+ 0079f52c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f52c ["INT_ADD", "register:40f0:8", ["const:79f52c:8", "const:4:8"]]
+ 0079f52c ["CALLIND", null, ["register:0:8"]]
- 0079f4d4 bytes 00013fd6
+ 0079f52c bytes 00013fd6
- 0079f50c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f50c ["INT_ADD", "register:40f0:8", ["const:79f50c:8", "const:4:8"]]
- 0079f50c ["CALLIND", null, ["register:0:8"]]
+ 0079f564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f564 ["INT_ADD", "register:40f0:8", ["const:79f564:8", "const:4:8"]]
+ 0079f564 ["CALLIND", null, ["register:0:8"]]
- 0079f50c bytes 00013fd6
+ 0079f564 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e47bb217d5638ac9da6863ab090e18"></a>

### [`0079f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f834.md) → [`0079f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f88c.md) FUN_0079f88c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079f898",
      "incomplete_value": false,
      "site": "0079f8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f840",
      "incomplete_value": false,
      "site": "0079f84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0079f8a4",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f8a4",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f834.md#insn-0079f840)
- 新版 [`0079f898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f88c.md#insn-0079f898)

~~~diff
- 0079f840 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0079f840 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079f840 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079f840 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079f898 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0079f898 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079f898 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079f898 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079f840 bytes 4a210e91
+ 0079f898 bytes 4a611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84108d815a69ce284d3eb49b631b2681"></a>

### [`0079f878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md) → [`0079f8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md) FUN_0079f8d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0079f8e8",
      "incomplete_value": false,
      "site": "0079f8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f890",
      "incomplete_value": false,
      "site": "0079f89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0079f8f4",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f8f4",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md#insn-0079f890) · [`0079f8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f878.md#insn-0079f8c0)
- 新版 [`0079f8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md#insn-0079f8e8) · [`0079f918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md#insn-0079f918)

~~~diff
- 0079f890 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0079f890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f8e8 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0079f8e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f8e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f8e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f890 bytes 08210e91
+ 0079f8e8 bytes 08611191
- 0079f8c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f8c0 ["INT_ADD", "register:40f0:8", ["const:79f8c0:8", "const:4:8"]]
- 0079f8c0 ["CALLIND", null, ["register:0:8"]]
+ 0079f918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f918 ["INT_ADD", "register:40f0:8", ["const:79f918:8", "const:4:8"]]
+ 0079f918 ["CALLIND", null, ["register:0:8"]]
- 0079f8c0 bytes 00013fd6
+ 0079f918 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05802e6fbff9888cafd0ae57149d0951"></a>

### [`0079f8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md) → [`0079f92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f92c.md) FUN_0079f92c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0079f958",
      "incomplete_value": false,
      "site": "0079f958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f900",
      "incomplete_value": false,
      "site": "0079f900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0079f958",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f958",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f8e8) · [`0079f8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f8f8) · [`0079f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f8d4.md#insn-0079f91c)
- 新版 [`0079f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f92c.md#insn-0079f940) · [`0079f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f92c.md#insn-0079f950) · [`0079f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f92c.md#insn-0079f974)

~~~diff
- 0079f8e8 ["INT_ADD", "register:40f0:8", ["const:79f8e8:8", "const:4:8"]]
- 0079f8e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0079f940 ["INT_ADD", "register:40f0:8", ["const:79f940:8", "const:4:8"]]
+ 0079f940 ["CALL", null, ["callee:00c57f60:8"]]
- 0079f8e8 bytes 6ae11294
+ 0079f940 bytes 88e11294
- 0079f8f8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0079f8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079f8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079f8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079f950 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0079f950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079f950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079f8f8 bytes 08210e91
+ 0079f950 bytes 08611191
- 0079f91c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f91c ["INT_ADD", "register:40f0:8", ["const:79f91c:8", "const:4:8"]]
- 0079f91c ["CALLIND", null, ["register:0:8"]]
+ 0079f974 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079f974 ["INT_ADD", "register:40f0:8", ["const:79f974:8", "const:4:8"]]
+ 0079f974 ["CALLIND", null, ["register:0:8"]]
- 0079f91c bytes 00013fd6
+ 0079f974 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c403e2c7a9967987e38f11e67a28ab41"></a>

### [`0079f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md) → [`0079f9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f9b4.md) FUN_0079f9b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0079f9d0",
      "incomplete_value": false,
      "site": "0079f9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079f978",
      "incomplete_value": false,
      "site": "0079f978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "0079f9d0",
      "DATA",
      [
        "storage",
        "00c7a388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f9d0",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md#insn-0079f974) · [`0079f998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079f95c.md#insn-0079f998)
- 新版 [`0079f9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f9b4.md#insn-0079f9cc) · [`0079f9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f9b4.md#insn-0079f9f0)

~~~diff
- 0079f974 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0079f974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079f974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079f974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079f9cc ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0079f9cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f9cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079f9cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079f974 bytes 29210e91
+ 0079f9cc bytes 29611191
- 0079f998 ["COPY", "register:0:8", ["register:4048:8"]]
- 0079f998 ["INT_ADD", "register:40f0:8", ["const:79f998:8", "const:4:8"]]
- 0079f998 ["CALLIND", null, ["register:0:8"]]
+ 0079f9f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079f9f0 ["INT_ADD", "register:40f0:8", ["const:79f9f0:8", "const:4:8"]]
+ 0079f9f0 ["CALLIND", null, ["register:0:8"]]
- 0079f998 bytes 20013fd6
+ 0079f9f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21cdeed7c29e0be7fe85982287145055"></a>

### [`0079faa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md) → [`0079faf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079faf8.md) _INIT_142

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0079fb34",
      "incomplete_value": true,
      "site": "0079fb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079fadc",
      "incomplete_value": true,
      "site": "0079faf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079fd28",
      "incomplete_value": false,
      "site": "0079fd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079fcd0",
      "incomplete_value": false,
      "site": "0079fcd4",
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079fb34",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0079fb58",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0079fb78",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0079fb34",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0079fb58",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0079fb78",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079fcd4) · [`0079fac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079fac8) · [`0079facc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079f/0079faa0.md#insn-0079facc)
- 新版 [`0079fd2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079faf8.md#insn-0079fd2c) · [`0079fb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079faf8.md#insn-0079fb20) · [`0079fb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079faf8.md#insn-0079fb24)

~~~diff
- 0079fcd4 ["INT_ADD", "register:40f0:8", ["const:79fcd4:8", "const:4:8"]]
- 0079fcd4 ["CALL", null, ["callee:00c57f00:8"]]
+ 0079fd2c ["INT_ADD", "register:40f0:8", ["const:79fd2c:8", "const:4:8"]]
+ 0079fd2c ["CALL", null, ["callee:00c57f00:8"]]
- 0079fcd4 bytes 57e01294
+ 0079fd2c bytes 75e01294
- 0079fac8 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 0079fb20 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 0079fac8 bytes 53280090
+ 0079fb20 bytes 532800b0
- 0079facc ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0079facc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0079facc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0079facc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0079fb24 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0079fb24 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0079fb24 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0079fb24 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0079facc bytes 73e23c91
+ 0079fb24 bytes 73e20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d0aeaeb24790959c7363cbeece36be9"></a>

### [`007a1ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md) → [`007a1b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md) FUN_007a1b08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007a18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a18d0.md) [`007a1c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1c44.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`007a1928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1928.md) [`007a1c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1c9c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "007a1b14",
      "incomplete_value": false,
      "site": "007a1b18",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007a1abc",
      "incomplete_value": false,
      "site": "007a1ac0",
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
      "007a1b14",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007a1b14",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007a1ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md#insn-007a1ac0) · [`007a1abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a1/007a1ab0.md#insn-007a1abc)
- 新版 [`007a1b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md#insn-007a1b18) · [`007a1b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a1/007a1b08.md#insn-007a1b14)

~~~diff
- 007a1ac0 ["INT_ADD", "register:40f0:8", ["const:7a1ac0:8", "const:4:8"]]
- 007a1ac0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 007a1b18 ["INT_ADD", "register:40f0:8", ["const:7a1b18:8", "const:4:8"]]
+ 007a1b18 ["CALL", null, ["callee:0043b7b8:8"]]
- 007a1ac0 bytes 2e67f297
+ 007a1b18 bytes 2867f297
- 007a1abc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007a1abc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007a1abc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007a1abc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007a1b14 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 007a1b14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007a1b14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007a1b14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007a1abc bytes 00303d91
+ 007a1b14 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2843db965e39d85f4ef69af205370b62"></a>

### [`007aa3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md) → [`007aa440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa440.md) _INIT_143

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "007aa47c",
      "incomplete_value": true,
      "site": "007aa498",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aa424",
      "incomplete_value": true,
      "site": "007aa440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aa4a0",
      "incomplete_value": true,
      "site": "007aa4bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aa448",
      "incomplete_value": true,
      "site": "007aa464",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aa4c0",
      "incomplete_value": true,
      "site": "007aa4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aa468",
      "incomplete_value": true,
      "site": "007aa484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007aa47c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007aa4a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007aa4c0",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007aa47c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "007aa4a0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "007aa4c0",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aa4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa4bc) · [`007aa4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa4dc) · [`007aa548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa3e8.md#insn-007aa548)
- 新版 [`007aa514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa440.md#insn-007aa514) · [`007aa534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa440.md#insn-007aa534) · [`007aa5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa440.md#insn-007aa5a0)

~~~diff
- 007aa4bc ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 007aa4bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aa4bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aa4bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aa514 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 007aa514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aa514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aa514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aa4bc bytes 29753d91
+ 007aa514 bytes 29413c91
- 007aa4dc ["COPY", "tmp:0:8", ["const:f09:8"]]
- 007aa4dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aa4dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aa4dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aa534 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 007aa534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aa534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aa534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aa4dc bytes 29253c91
+ 007aa534 bytes 29f13a91
- 007aa548 ["INT_ADD", "register:40f0:8", ["const:7aa548:8", "const:4:8"]]
- 007aa548 ["CALL", null, ["callee:0043b838:8"]]
+ 007aa5a0 ["INT_ADD", "register:40f0:8", ["const:7aa5a0:8", "const:4:8"]]
+ 007aa5a0 ["CALL", null, ["callee:0043b838:8"]]
- 007aa548 bytes ac44f297
+ 007aa5a0 bytes a644f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30eb779ec477047e76ebd58ee130640b"></a>

### [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) → [`007aa860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md) FUN_007aa860

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00aadf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf8c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`007ad8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`007aaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md) [`00aadffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aad/00aadffc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007aaa00",
      "incomplete_value": false,
      "site": "007aaa04",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aa9a8",
      "incomplete_value": false,
      "site": "007aa9ac",
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
      "007aa8c0",
      "READ",
      [
        "storage",
        "00ca7f80",
        null,
        "undefined1"
      ]
    ],
    [
      "007aa8c4",
      "READ",
      [
        "storage",
        "00ca7f88",
        null,
        "undefined8"
      ]
    ],
    [
      "007aa8c4",
      "READ",
      [
        "storage",
        "00ca7f90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007aa8c0",
      "READ",
      [
        "storage",
        "00ca8080",
        null,
        "undefined1"
      ]
    ],
    [
      "007aa8c4",
      "READ",
      [
        "storage",
        "00ca8088",
        null,
        "undefined8"
      ]
    ],
    [
      "007aa8c4",
      "READ",
      [
        "storage",
        "00ca8090",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aa9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa9ac) · [`007aa84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa84c) · [`007aa85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md#insn-007aa85c)
- 新版 [`007aaa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md#insn-007aaa04) · [`007aa8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md#insn-007aa8a4) · [`007aa8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md#insn-007aa8b4)

~~~diff
- 007aa9ac ["INT_ADD", "register:40f0:8", ["const:7aa9ac:8", "const:4:8"]]
- 007aa9ac ["CALL", null, ["callee:00442970:8"]]
+ 007aaa04 ["INT_ADD", "register:40f0:8", ["const:7aaa04:8", "const:4:8"]]
+ 007aaa04 ["CALL", null, ["callee:00442970:8"]]
- 007aa9ac bytes e15ff297
+ 007aaa04 bytes db5ff297
- 007aa84c ["INT_ADD", "register:40f0:8", ["const:7aa84c:8", "const:4:8"]]
- 007aa84c ["CALL", null, ["callee:007aaa80:8"]]
+ 007aa8a4 ["INT_ADD", "register:40f0:8", ["const:7aa8a4:8", "const:4:8"]]
+ 007aa8a4 ["CALL", null, ["callee:007aaa80:8"]]
- 007aa84c bytes 77000094
+ 007aa8a4 bytes 77000094
- 007aa85c ["COPY", "register:4040:8", ["const:ca7000:8"]]
+ 007aa8b4 ["COPY", "register:4040:8", ["const:ca8000:8"]]
- 007aa85c bytes e82700b0
+ 007aa8b4 bytes e82700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aa788b8055e4cf19d9e4320bdbd2f14"></a>

### [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) → [`007aaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md) FUN_007aaa80

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 2件 [`007aa860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md) [`007aad5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007aaab4",
      "incomplete_value": false,
      "site": "007aaab8",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aaa5c",
      "incomplete_value": false,
      "site": "007aaa60",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aabf8",
      "incomplete_value": true,
      "site": "007aabfc",
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
      "definition_site": "007aaba0",
      "incomplete_value": true,
      "site": "007aaba4",
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
      "definition_site": "007aabf4",
      "incomplete_value": true,
      "site": "007aac00",
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
      "definition_site": "007aab9c",
      "incomplete_value": true,
      "site": "007aaba8",
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
      "007aaab8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "007aaac0",
      "PARAM",
      [
        "storage",
        "00ca7fb8",
        null,
        "undefined1"
      ]
    ],
    [
      "007aaaf8",
      "PARAM",
      [
        "storage",
        "00ca7fa0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007aaab8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "007aaac0",
      "PARAM",
      [
        "storage",
        "00ca80b8",
        null,
        "undefined1"
      ]
    ],
    [
      "007aaaf8",
      "PARAM",
      [
        "storage",
        "00ca80a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aaa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaa54) · [`007aaa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaa70) · [`007aaaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md#insn-007aaaac)
- 新版 [`007aaaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md#insn-007aaaac) · [`007aaac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md#insn-007aaac8) · [`007aab04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md#insn-007aab04)

~~~diff
- 007aaa54 ["INT_ADD", "register:40f0:8", ["const:7aaa54:8", "const:4:8"]]
- 007aaa54 ["CALL", null, ["callee:00487e60:8"]]
+ 007aaaac ["INT_ADD", "register:40f0:8", ["const:7aaaac:8", "const:4:8"]]
+ 007aaaac ["CALL", null, ["callee:00487e60:8"]]
- 007aaa54 bytes f374f397
+ 007aaaac bytes ed74f397
- 007aaa70 ["INT_ADD", "register:40f0:8", ["const:7aaa70:8", "const:4:8"]]
- 007aaa70 ["CALL", null, ["callee:0048ce94:8"]]
+ 007aaac8 ["INT_ADD", "register:40f0:8", ["const:7aaac8:8", "const:4:8"]]
+ 007aaac8 ["CALL", null, ["callee:0048ce94:8"]]
- 007aaa70 bytes f988f397
+ 007aaac8 bytes f388f397
- 007aaaac ["INT_ADD", "register:40f0:8", ["const:7aaaac:8", "const:4:8"]]
- 007aaaac ["CALL", null, ["callee:00492e48:8"]]
+ 007aab04 ["INT_ADD", "register:40f0:8", ["const:7aab04:8", "const:4:8"]]
+ 007aab04 ["CALL", null, ["callee:00492e48:8"]]
- 007aaaac bytes d7a0f397
+ 007aab04 bytes d1a0f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44250e559d5394bb78589db1c6e98ffb"></a>

### [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) → [`007aad5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md) FUN_007aad5c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007aeff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md) · 呼出先 8件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`007aaa28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaa28.md) [`00aadf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`007af050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af050.md) · 呼出先 8件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`007aaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaa80.md) [`00aadffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aad/00aadffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007aaeac",
      "incomplete_value": false,
      "site": "007aaeb0",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aae54",
      "incomplete_value": false,
      "site": "007aae58",
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
      "007aadcc",
      "PARAM",
      [
        "storage",
        "002bb7c4",
        null,
        "string"
      ]
    ],
    [
      "007aadd8",
      "PARAM",
      [
        "storage",
        "002ab92e",
        null,
        "string"
      ]
    ],
    [
      "007aaeac",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007aadcc",
      "PARAM",
      [
        "storage",
        "002bb770",
        null,
        "string"
      ]
    ],
    [
      "007aadd8",
      "PARAM",
      [
        "storage",
        "002ab8d2",
        null,
        "string"
      ]
    ],
    [
      "007aaeac",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aae58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aae58) · [`007aad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aad4c) · [`007aad74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md#insn-007aad74)
- 新版 [`007aaeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md#insn-007aaeb0) · [`007aada4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md#insn-007aada4) · [`007aadcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md#insn-007aadcc)

~~~diff
- 007aae58 ["INT_ADD", "register:40f0:8", ["const:7aae58:8", "const:4:8"]]
- 007aae58 ["CALL", null, ["callee:00442970:8"]]
+ 007aaeb0 ["INT_ADD", "register:40f0:8", ["const:7aaeb0:8", "const:4:8"]]
+ 007aaeb0 ["CALL", null, ["callee:00442970:8"]]
- 007aae58 bytes b65ef297
+ 007aaeb0 bytes b05ef297
- 007aad4c ["INT_ADD", "register:40f0:8", ["const:7aad4c:8", "const:4:8"]]
- 007aad4c ["CALL", null, ["callee:007aaa80:8"]]
+ 007aada4 ["INT_ADD", "register:40f0:8", ["const:7aada4:8", "const:4:8"]]
+ 007aada4 ["CALL", null, ["callee:007aaa80:8"]]
- 007aad4c bytes 37ffff97
+ 007aada4 bytes 37ffff97
- 007aad74 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 007aad74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007aad74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007aad74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007aadcc ["COPY", "tmp:0:8", ["const:770:8"]]
+ 007aadcc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007aadcc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007aadcc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007aad74 bytes 21101f91
+ 007aadcc bytes 21c01d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddd5ebfa524f35740a7ba842ab2f23cc"></a>

### [`007aaef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md) → [`007aaf4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaf4c.md) _INIT_144

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 74.77% / 新版 74.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 11件, `store_value` 11件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aaf88",
      "incomplete_value": true,
      "site": "007aafa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aaf30",
      "incomplete_value": true,
      "site": "007aaf4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aafac",
      "incomplete_value": true,
      "site": "007aafc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aaf54",
      "incomplete_value": true,
      "site": "007aaf70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007aafcc",
      "incomplete_value": true,
      "site": "007aafe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aaf74",
      "incomplete_value": true,
      "site": "007aaf90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007aaf88",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007aafac",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007aafcc",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007aaf88",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "007aafac",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "007aafcc",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aafc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007aafc8) · [`007aafe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007aafe8) · [`007ab054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aaef4.md#insn-007ab054)
- 新版 [`007ab020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaf4c.md#insn-007ab020) · [`007ab040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaf4c.md#insn-007ab040) · [`007ab0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aaf4c.md#insn-007ab0ac)

~~~diff
- 007aafc8 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 007aafc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aafc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aafc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ab020 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 007ab020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ab020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ab020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aafc8 bytes 29753d91
+ 007ab020 bytes 29413c91
- 007aafe8 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 007aafe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aafe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aafe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ab040 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 007ab040 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ab040 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ab040 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aafe8 bytes 29253c91
+ 007ab040 bytes 29f13a91
- 007ab054 ["INT_ADD", "register:40f0:8", ["const:7ab054:8", "const:4:8"]]
- 007ab054 ["CALL", null, ["callee:0043b838:8"]]
+ 007ab0ac ["INT_ADD", "register:40f0:8", ["const:7ab0ac:8", "const:4:8"]]
+ 007ab0ac ["CALL", null, ["callee:0043b838:8"]]
- 007ab054 bytes e941f297
+ 007ab0ac bytes e341f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b933bc8a472a856dbb27352bd4ec34a"></a>

### [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) → [`007ab45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md) FUN_007ab45c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009311c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/009311c4.md) · 呼出先 6件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) [`007ae774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae774.md) [`007ae84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae84c.md) [`007ae850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae850.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00931218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00931/00931218.md) · 呼出先 6件 [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) [`007ae7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae7cc.md) [`007ae8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8a4.md) [`007ae8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab53c",
      "incomplete_value": false,
      "site": "007ab540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab4e4",
      "incomplete_value": false,
      "site": "007ab4e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "definition_site": "007ab58c",
      "incomplete_value": false,
      "site": "007ab58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab534",
      "incomplete_value": false,
      "site": "007ab534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "007ab540",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab58c",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab5c8",
      "READ",
      [
        "storage",
        "00c7a4b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ab540",
      "DATA",
      [
        "storage",
        "00c7a4d8",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab58c",
      "DATA",
      [
        "storage",
        "00c7a568",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab5c8",
      "READ",
      [
        "storage",
        "00c7a588",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab45c) · [`007ab494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab494) · [`007ab4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md#insn-007ab4c0)
- 新版 [`007ab4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md#insn-007ab4b4) · [`007ab4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md#insn-007ab4ec) · [`007ab518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md#insn-007ab518)

~~~diff
- 007ab45c ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab45c ["INT_ADD", "register:40f0:8", ["const:7ab45c:8", "const:4:8"]]
- 007ab45c ["CALLIND", null, ["register:0:8"]]
+ 007ab4b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab4b4 ["INT_ADD", "register:40f0:8", ["const:7ab4b4:8", "const:4:8"]]
+ 007ab4b4 ["CALLIND", null, ["register:0:8"]]
- 007ab45c bytes 00013fd6
+ 007ab4b4 bytes 00013fd6
- 007ab494 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab494 ["INT_ADD", "register:40f0:8", ["const:7ab494:8", "const:4:8"]]
- 007ab494 ["CALLIND", null, ["register:0:8"]]
+ 007ab4ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab4ec ["INT_ADD", "register:40f0:8", ["const:7ab4ec:8", "const:4:8"]]
+ 007ab4ec ["CALLIND", null, ["register:0:8"]]
- 007ab494 bytes 00013fd6
+ 007ab4ec bytes 00013fd6
- 007ab4c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ab4c0 ["INT_ADD", "register:40f0:8", ["const:7ab4c0:8", "const:4:8"]]
- 007ab4c0 ["CALLIND", null, ["register:0:8"]]
+ 007ab518 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ab518 ["INT_ADD", "register:40f0:8", ["const:7ab518:8", "const:4:8"]]
+ 007ab518 ["CALLIND", null, ["register:0:8"]]
- 007ab4c0 bytes 00013fd6
+ 007ab518 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63bf3218ccab8766622dd4ccc709751"></a>

### [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) → [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) FUN_007ab7ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ab404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab404.md) · 呼出先 14件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)
- 新版 呼出元 1件 [`007ab45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab45c.md) · 呼出先 14件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab800",
      "incomplete_value": false,
      "site": "007ab804",
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
                "const:c6e000:8"
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
    "old": {
      "definition_site": "007ab7a8",
      "incomplete_value": false,
      "site": "007ab7ac",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:c88:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab830",
      "incomplete_value": false,
      "site": "007ab834",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "007ab7d8",
      "incomplete_value": false,
      "site": "007ab7dc",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ab8c0",
      "incomplete_value": false,
      "site": "007ab8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ab868",
      "incomplete_value": false,
      "site": "007ab868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "007ab804",
      "DATA",
      [
        "storage",
        "00c6ec98",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab834",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab8c0",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ab804",
      "DATA",
      [
        "storage",
        "00c6ed68",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab834",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "007ab8c0",
      "DATA",
      [
        "storage",
        "00c7a968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ab780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab780) · [`007ab798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab798) · [`007ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md#insn-007ab7a0)
- 新版 [`007ab7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md#insn-007ab7d8) · [`007ab7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md#insn-007ab7f0) · [`007ab7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md#insn-007ab7f8)

~~~diff
- 007ab780 ["INT_ADD", "register:40f0:8", ["const:7ab780:8", "const:4:8"]]
- 007ab780 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ab7d8 ["INT_ADD", "register:40f0:8", ["const:7ab7d8:8", "const:4:8"]]
+ 007ab7d8 ["CALL", null, ["callee:00c57f60:8"]]
- 007ab780 bytes c4b11294
+ 007ab7d8 bytes e2b11294
- 007ab798 ["INT_ADD", "register:40f0:8", ["const:7ab798:8", "const:4:8"]]
- 007ab798 ["CALL", null, ["callee:0059b948:8"]]
+ 007ab7f0 ["INT_ADD", "register:40f0:8", ["const:7ab7f0:8", "const:4:8"]]
+ 007ab7f0 ["CALL", null, ["callee:0059b948:8"]]
- 007ab798 bytes 5cc0f797
+ 007ab7f0 bytes 56c0f797
- 007ab7a0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 007ab7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ab7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ab7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ab7f8 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 007ab7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ab7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ab7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ab7a0 bytes 08213291
+ 007ab7f8 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f2fb0c4ca6196bbf990ff4a322f5c59"></a>

### [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) → [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) FUN_007abc7c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ae7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae7c4.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 1件 [`007ae81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae81c.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007abcc8",
      "incomplete_value": false,
      "site": "007abcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abc70",
      "incomplete_value": false,
      "site": "007abc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "007abd28",
      "incomplete_value": true,
      "site": "007abd28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abcd0",
      "incomplete_value": true,
      "site": "007abcd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
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
      "definition_site": "007abdec",
      "incomplete_value": true,
      "site": "007abdec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:44f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007abd94",
      "incomplete_value": true,
      "site": "007abd94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49c:8"
              ]
            ]
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
      "007abcd8",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "007abd14",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "007abdd0",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007abcd8",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "007abd14",
      "READ",
      [
        "storage",
        "002afb2c",
        null,
        "string"
      ]
    ],
    [
      "007abdd0",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007abe70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007abe70) · [`007ac020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007ac020) · [`007abc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md#insn-007abc64)
- 新版 [`007abec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md#insn-007abec8) · [`007ac078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md#insn-007ac078) · [`007abcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md#insn-007abcbc)

~~~diff
- 007abe70 ["COPY", "register:0:8", ["register:4040:8"]]
- 007abe70 ["INT_ADD", "register:40f0:8", ["const:7abe70:8", "const:4:8"]]
- 007abe70 ["CALLIND", null, ["register:0:8"]]
+ 007abec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007abec8 ["INT_ADD", "register:40f0:8", ["const:7abec8:8", "const:4:8"]]
+ 007abec8 ["CALLIND", null, ["register:0:8"]]
- 007abe70 bytes 00013fd6
+ 007abec8 bytes 00013fd6
- 007ac020 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ac020 ["INT_ADD", "register:40f0:8", ["const:7ac020:8", "const:4:8"]]
- 007ac020 ["CALLIND", null, ["register:0:8"]]
+ 007ac078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ac078 ["INT_ADD", "register:40f0:8", ["const:7ac078:8", "const:4:8"]]
+ 007ac078 ["CALLIND", null, ["register:0:8"]]
- 007ac020 bytes 00013fd6
+ 007ac078 bytes 00013fd6
- 007abc64 ["INT_ADD", "register:40f0:8", ["const:7abc64:8", "const:4:8"]]
- 007abc64 ["CALL", null, ["callee:00c57f60:8"]]
+ 007abcbc ["INT_ADD", "register:40f0:8", ["const:7abcbc:8", "const:4:8"]]
+ 007abcbc ["CALL", null, ["callee:00c57f60:8"]]
- 007abc64 bytes 8bb01294
+ 007abcbc bytes a9b01294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8572639eed73810ea06b873501d45bf3"></a>

### [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) → [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) FUN_007ac418

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md)
- 新版 呼出元 1件 [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) · 呼出先 15件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cacc.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac468",
      "incomplete_value": true,
      "site": "007ac468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac410",
      "incomplete_value": true,
      "site": "007ac410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
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
      "definition_site": "007ac54c",
      "incomplete_value": true,
      "site": "007ac54c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:492:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac4f4",
      "incomplete_value": true,
      "site": "007ac4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac540",
      "incomplete_value": true,
      "site": "007ac550",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac4e8",
      "incomplete_value": true,
      "site": "007ac4f8",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
      "007ac444",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "007ac494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ac4a8",
      "READ",
      [
        "storage",
        "002c12fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ac444",
      "READ",
      [
        "storage",
        "002afb2c",
        null,
        "string"
      ]
    ],
    [
      "007ac494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "007ac4a8",
      "READ",
      [
        "storage",
        "002c133a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac3e4) · [`007ac43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac43c) · [`007ac49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md#insn-007ac49c)
- 新版 [`007ac43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md#insn-007ac43c) · [`007ac494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md#insn-007ac494) · [`007ac4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md#insn-007ac4f4)

~~~diff
- 007ac3e4 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 007ac3e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ac3e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ac3e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ac43c ["COPY", "tmp:0:8", ["const:b2c:8"]]
+ 007ac43c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ac43c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ac43c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ac3e4 bytes 4a212e91
+ 007ac43c bytes 4ab12c91
- 007ac43c ["INT_ADD", "register:40f0:8", ["const:7ac43c:8", "const:4:8"]]
- 007ac43c ["CALL", null, ["ram:48ccf8:8"]]
+ 007ac494 ["INT_ADD", "register:40f0:8", ["const:7ac494:8", "const:4:8"]]
+ 007ac494 ["CALL", null, ["ram:48cd38:8"]]
- 007ac43c bytes 2f82f397
+ 007ac494 bytes 2982f397
- 007ac49c ["INT_ADD", "register:40f0:8", ["const:7ac49c:8", "const:4:8"]]
- 007ac49c ["CALL", null, ["callee:00c57f80:8"]]
+ 007ac4f4 ["INT_ADD", "register:40f0:8", ["const:7ac4f4:8", "const:4:8"]]
+ 007ac4f4 ["CALL", null, ["callee:00c57f80:8"]]
- 007ac49c bytes 85ae1294
+ 007ac4f4 bytes a3ae1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4702d95a4df136a56b61c6e8909d5941"></a>

### [`007ac6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md) → [`007ac738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md) FUN_007ac738

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 6件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) [`007aec3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec3c.md) [`007aec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec40.md) [`007aecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc0.md) [`007aecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc4.md)
- 新版 呼出元 1件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) · 呼出先 6件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) [`007aec94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec94.md) [`007aec98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec98.md) [`007aed18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed18.md) [`007aed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac760",
      "incomplete_value": false,
      "site": "007ac760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac708",
      "incomplete_value": false,
      "site": "007ac708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "definition_site": "007ac774",
      "incomplete_value": false,
      "site": "007ac774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac71c",
      "incomplete_value": false,
      "site": "007ac71c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "007ac760",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac774",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac7ac",
      "READ",
      [
        "storage",
        "00c7a638",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ac760",
      "DATA",
      [
        "storage",
        "00c7a668",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac774",
      "DATA",
      [
        "storage",
        "00c7a6e8",
        null,
        "undefined *"
      ]
    ],
    [
      "007ac7ac",
      "READ",
      [
        "storage",
        "00c7a708",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac704) · [`007ac718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac718) · [`007ac72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md#insn-007ac72c)
- 新版 [`007ac75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac75c) · [`007ac770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac770) · [`007ac784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac784)

~~~diff
- 007ac704 ["COPY", "tmp:0:8", ["const:598:8"]]
- 007ac704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ac704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ac704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ac75c ["COPY", "tmp:0:8", ["const:668:8"]]
+ 007ac75c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac75c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac75c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ac704 bytes 08611691
+ 007ac75c bytes 08a11991
- 007ac718 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007ac718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ac718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ac718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ac770 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 007ac770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ac770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ac718 bytes 08611891
+ 007ac770 bytes 08a11b91
- 007ac72c ["INT_ADD", "register:40f0:8", ["const:7ac72c:8", "const:4:8"]]
- 007ac72c ["CALL", null, ["callee:007ad37c:8"]]
+ 007ac784 ["INT_ADD", "register:40f0:8", ["const:7ac784:8", "const:4:8"]]
+ 007ac784 ["CALL", null, ["callee:007ad37c:8"]]
- 007ac72c bytes fe020094
+ 007ac784 bytes fe020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b1c0d36b34675ad381456f2d7e3b6e4"></a>

### [`007ac82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md) → [`007ac884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac884.md) FUN_007ac884

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00597658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597658.md)
- 新版 呼出元 1件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`00597698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597698.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac8a4",
      "incomplete_value": true,
      "site": "007ac8bc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ac84c",
      "incomplete_value": true,
      "site": "007ac864",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ac8c0",
      "incomplete_value": true,
      "site": "007ac8c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ac868",
      "incomplete_value": true,
      "site": "007ac868",
      "value": [
        "LOAD",
        "8",
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
      "007ac8a4",
      "READ",
      [
        "storage",
        "002b4085",
        null,
        "string"
      ]
    ],
    [
      "007ac8b4",
      "READ",
      [
        "storage",
        "002b4093",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ac8a4",
      "READ",
      [
        "storage",
        "002b40b6",
        null,
        "string"
      ]
    ],
    [
      "007ac8b4",
      "READ",
      [
        "storage",
        "002b40c4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ac8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac8c0) · [`007ac844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac844) · [`007ac878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac82c.md#insn-007ac878)
- 新版 [`007ac918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac884.md#insn-007ac918) · [`007ac89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac884.md#insn-007ac89c) · [`007ac8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac884.md#insn-007ac8d0)

~~~diff
- 007ac8c0 ["INT_ADD", "register:40f0:8", ["const:7ac8c0:8", "const:4:8"]]
- 007ac8c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ac918 ["INT_ADD", "register:40f0:8", ["const:7ac918:8", "const:4:8"]]
+ 007ac918 ["CALL", null, ["callee:00c57f80:8"]]
- 007ac8c0 bytes 7cad1294
+ 007ac918 bytes 9aad1294
- 007ac844 ["COPY", "tmp:0:8", ["const:85:8"]]
- 007ac844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ac844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ac844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ac89c ["COPY", "tmp:0:8", ["const:b6:8"]]
+ 007ac89c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ac89c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ac89c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ac844 bytes 29150291
+ 007ac89c bytes 29d90291
- 007ac878 ["INT_ADD", "register:40f0:8", ["const:7ac878:8", "const:4:8"]]
- 007ac878 ["CALL", null, ["callee:0048ce94:8"]]
+ 007ac8d0 ["INT_ADD", "register:40f0:8", ["const:7ac8d0:8", "const:4:8"]]
+ 007ac8d0 ["CALL", null, ["callee:0048ce94:8"]]
- 007ac878 bytes 7781f397
+ 007ac8d0 bytes 7181f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aae3fadc5bc7b11d00159be04be62d1"></a>

### [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) → [`007acb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md) FUN_007acb24

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) · 呼出先 17件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md)
- 新版 呼出元 1件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) · 呼出先 17件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007acb70",
      "incomplete_value": false,
      "site": "007acb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007acb18",
      "incomplete_value": false,
      "site": "007acb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "007acbc0",
      "incomplete_value": true,
      "site": "007acbd4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007acb68",
      "incomplete_value": true,
      "site": "007acb7c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:34e:8"
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
      "definition_site": "007acbd8",
      "incomplete_value": true,
      "site": "007acbd8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007acb80",
      "incomplete_value": true,
      "site": "007acb80",
      "value": [
        "LOAD",
        "8",
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
      "007acb74",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "007acbc0",
      "READ",
      [
        "storage",
        "002c034e",
        null,
        "string"
      ]
    ],
    [
      "007acbd0",
      "READ",
      [
        "storage",
        "002c035c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007acb74",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "007acbc0",
      "READ",
      [
        "storage",
        "002c038e",
        null,
        "string"
      ]
    ],
    [
      "007acbd0",
      "READ",
      [
        "storage",
        "002c039c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007acd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acd5c) · [`007acb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acb00) · [`007acb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md#insn-007acb18)
- 新版 [`007acdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md#insn-007acdb4) · [`007acb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md#insn-007acb58) · [`007acb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md#insn-007acb70)

~~~diff
- 007acd5c ["INT_ADD", "register:40f0:8", ["const:7acd5c:8", "const:4:8"]]
- 007acd5c ["CALL", null, ["callee:00749010:8"]]
+ 007acdb4 ["INT_ADD", "register:40f0:8", ["const:7acdb4:8", "const:4:8"]]
+ 007acdb4 ["CALL", null, ["callee:00749010:8"]]
- 007acd5c bytes 9770fe97
+ 007acdb4 bytes 9770fe97
- 007acb00 ["INT_ADD", "register:40f0:8", ["const:7acb00:8", "const:4:8"]]
- 007acb00 ["CALL", null, ["callee:00c57f60:8"]]
+ 007acb58 ["INT_ADD", "register:40f0:8", ["const:7acb58:8", "const:4:8"]]
+ 007acb58 ["CALL", null, ["callee:00c57f60:8"]]
- 007acb00 bytes e4ac1294
+ 007acb58 bytes 02ad1294
- 007acb18 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 007acb18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007acb18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007acb18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007acb70 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 007acb70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007acb70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007acb70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007acb18 bytes 08812b91
+ 007acb70 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85884c2524ca3c759e3a28540ae453ca"></a>

### [`007ad104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md) → [`007ad15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad15c.md) FUN_007ad15c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 10件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00b0e934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md)
- 新版 呼出元 1件 [`008978e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) · 呼出先 10件 [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00b0e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad1ac",
      "incomplete_value": true,
      "site": "007ad1b0",
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
      "definition_site": "007ad154",
      "incomplete_value": true,
      "site": "007ad158",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad1a8",
      "incomplete_value": true,
      "site": "007ad1b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007ad150",
      "incomplete_value": true,
      "site": "007ad15c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ad1bc",
      "incomplete_value": true,
      "site": "007ad1bc",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
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
      "definition_site": "007ad164",
      "incomplete_value": true,
      "site": "007ad164",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
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
      "unmatched:007ad144",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "007ad1a8",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "007ad1a8",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "007ad198",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "007ad1a8",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "007ad1a8",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ad20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad20c) · [`007ad140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad140) · [`007ad144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md#insn-007ad144)
- 新版 [`007ad264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad15c.md#insn-007ad264) · [`007ad19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad15c.md#insn-007ad19c)

~~~diff
- 007ad20c ["INT_ADD", "register:40f0:8", ["const:7ad20c:8", "const:4:8"]]
- 007ad20c ["CALL", null, ["callee:00b0e9d0:8"]]
+ 007ad264 ["INT_ADD", "register:40f0:8", ["const:7ad264:8", "const:4:8"]]
+ 007ad264 ["CALL", null, ["callee:00b0e9d0:8"]]
- 007ad20c bytes ca850d94
+ 007ad264 bytes db850d94
- 007ad140 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c88:8"]]
- 007ad140 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 007ad19c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c88:8"]]
+ 007ad19c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 007ad140 bytes 184746f9
+ 007ad19c bytes f74646f9
- 007ad144 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:bb8:8"]]
- 007ad144 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 007ad144 bytes f7de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67fdeef78839d180f364a600eaacf8dc"></a>

### [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) → [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) FUN_007ad37c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ac6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac6e0.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a59bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)
- 新版 呼出元 1件 [`007ac738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a59fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a59fc.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.08% / 新版 97.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad438",
      "incomplete_value": false,
      "site": "007ad43c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "007ad3e0",
      "incomplete_value": false,
      "site": "007ad3e4",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad4c8",
      "incomplete_value": false,
      "site": "007ad4c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad470",
      "incomplete_value": false,
      "site": "007ad470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad5d8",
      "incomplete_value": false,
      "site": "007ad5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad580",
      "incomplete_value": false,
      "site": "007ad580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007ad43c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad4c8",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad53c",
      "READ",
      [
        "storage",
        "00c7a9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ad43c",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad4c8",
      "DATA",
      [
        "storage",
        "00c7aa68",
        null,
        "undefined *"
      ]
    ],
    [
      "007ad53c",
      "READ",
      [
        "storage",
        "00c7aa90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ad358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad358) · [`007ad384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad384) · [`007ad390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md#insn-007ad390)
- 新版 [`007ad3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md#insn-007ad3b0) · [`007ad3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md#insn-007ad3dc) · [`007ad3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md#insn-007ad3e8)

~~~diff
- 007ad358 ["INT_ADD", "register:40f0:8", ["const:7ad358:8", "const:4:8"]]
- 007ad358 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ad3b0 ["INT_ADD", "register:40f0:8", ["const:7ad3b0:8", "const:4:8"]]
+ 007ad3b0 ["CALL", null, ["callee:00c57f60:8"]]
- 007ad358 bytes ceaa1294
+ 007ad3b0 bytes ecaa1294
- 007ad384 ["INT_ADD", "register:40f0:8", ["const:7ad384:8", "const:4:8"]]
- 007ad384 ["CALL", null, ["callee:0043bb60:8"]]
+ 007ad3dc ["INT_ADD", "register:40f0:8", ["const:7ad3dc:8", "const:4:8"]]
+ 007ad3dc ["CALL", null, ["callee:0043bb60:8"]]
- 007ad384 bytes e739f297
+ 007ad3dc bytes e139f297
- 007ad390 ["INT_ADD", "register:40f0:8", ["const:7ad390:8", "const:4:8"]]
- 007ad390 ["CALL", null, ["callee:005a59fc:8"]]
+ 007ad3e8 ["INT_ADD", "register:40f0:8", ["const:7ad3e8:8", "const:4:8"]]
+ 007ad3e8 ["CALL", null, ["callee:005a59fc:8"]]
- 007ad390 bytes 8be1f797
+ 007ad3e8 bytes 85e1f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-800b6ba3e0881d2d4afb155d30562b05"></a>

### [`007ad848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md) → [`007ad8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md) FUN_007ad8a0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007aec44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec44.md) · 呼出先 10件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007aa808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aa808.md) [`007aed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed30.md)
- 新版 呼出元 1件 [`007aec9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec9c.md) · 呼出先 10件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`007aa860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa860.md) [`007aed88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed88.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ad90c",
      "incomplete_value": false,
      "site": "007ad914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ad8b4",
      "incomplete_value": false,
      "site": "007ad8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "site": "007ad8e8",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad890",
      "value": [
        "leaf",
        "ram:764384:8"
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
      "site": "007ad904",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ad8ac",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007ad8e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "007ad904",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ad914",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ad8e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "007ad904",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "007ad914",
      "DATA",
      [
        "storage",
        "00c7a768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ad890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad890) · [`007ad8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad8ac) · [`007ad884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad848.md#insn-007ad884)
- 新版 [`007ad8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md#insn-007ad8e8) · [`007ad904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md#insn-007ad904) · [`007ad8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad8a0.md#insn-007ad8dc)

~~~diff
- 007ad890 ["INT_ADD", "register:40f0:8", ["const:7ad890:8", "const:4:8"]]
- 007ad890 ["CALL", null, ["ram:764384:8"]]
+ 007ad8e8 ["INT_ADD", "register:40f0:8", ["const:7ad8e8:8", "const:4:8"]]
+ 007ad8e8 ["CALL", null, ["ram:7643dc:8"]]
- 007ad890 bytes bddafe97
+ 007ad8e8 bytes bddafe97
- 007ad8ac ["INT_ADD", "register:40f0:8", ["const:7ad8ac:8", "const:4:8"]]
- 007ad8ac ["CALL", null, ["ram:48ccf8:8"]]
+ 007ad904 ["INT_ADD", "register:40f0:8", ["const:7ad904:8", "const:4:8"]]
+ 007ad904 ["CALL", null, ["ram:48cd38:8"]]
- 007ad8ac bytes 137df397
+ 007ad904 bytes 0d7df397
- 007ad884 ["INT_ADD", "register:40f0:8", ["const:7ad884:8", "const:4:8"]]
- 007ad884 ["CALL", null, ["callee:00aa3e94:8"]]
+ 007ad8dc ["INT_ADD", "register:40f0:8", ["const:7ad8dc:8", "const:4:8"]]
+ 007ad8dc ["CALL", null, ["callee:00aa3e94:8"]]
- 007ad884 bytes 68d90b94
+ 007ad8dc bytes 6ed90b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac3d90ff4d337bff039f4b39d75268f"></a>

### [`007ad984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md) → [`007ad9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md) FUN_007ad9dc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007aecc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecc8.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md)
- 新版 呼出元 1件 [`007aed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed20.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007adbb0",
      "incomplete_value": false,
      "site": "007adbb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007adb58",
      "incomplete_value": false,
      "site": "007adb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007adb3c",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007adae4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007ada24",
      "PARAM",
      [
        "storage",
        "002b93d4",
        null,
        "string"
      ]
    ],
    [
      "007ada48",
      "PARAM",
      [
        "storage",
        "002b858a",
        null,
        "string"
      ]
    ],
    [
      "007ada54",
      "PARAM",
      [
        "storage",
        "002b7769",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007ada24",
      "PARAM",
      [
        "storage",
        "002b9380",
        null,
        "string"
      ]
    ],
    [
      "007ada48",
      "PARAM",
      [
        "storage",
        "002b8536",
        null,
        "string"
      ]
    ],
    [
      "007ada54",
      "PARAM",
      [
        "storage",
        "002b77a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007adae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007adae4) · [`007adbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007adbb8) · [`007ad9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad984.md#insn-007ad9cc)
- 新版 [`007adb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md#insn-007adb3c) · [`007adc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md#insn-007adc10) · [`007ada24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad9dc.md#insn-007ada24)

~~~diff
- 007adae4 ["INT_ADD", "register:40f0:8", ["const:7adae4:8", "const:4:8"]]
- 007adae4 ["CALL", null, ["ram:48ccf8:8"]]
+ 007adb3c ["INT_ADD", "register:40f0:8", ["const:7adb3c:8", "const:4:8"]]
+ 007adb3c ["CALL", null, ["ram:48cd38:8"]]
- 007adae4 bytes 857cf397
+ 007adb3c bytes 7f7cf397
- 007adbb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007adbb8 ["INT_ADD", "register:40f0:8", ["const:7adbb8:8", "const:4:8"]]
- 007adbb8 ["CALLIND", null, ["register:0:8"]]
+ 007adc10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007adc10 ["INT_ADD", "register:40f0:8", ["const:7adc10:8", "const:4:8"]]
+ 007adc10 ["CALLIND", null, ["register:0:8"]]
- 007adbb8 bytes 00013fd6
+ 007adc10 bytes 00013fd6
- 007ad9cc ["COPY", "tmp:0:8", ["const:3d4:8"]]
- 007ad9cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007ad9cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007ad9cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ada24 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 007ada24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ada24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ada24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007ad9cc bytes 21500f91
+ 007ada24 bytes 21000e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f01d59870a029da08e707f1f91b2a09"></a>

### [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) → [`007addb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md) FUN_007addb0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0081d1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1ec.md) · 呼出先 8件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) [`007aeff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff0.md) [`007aeff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff4.md) [`007af0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0fc.md) [`007af100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af100.md)
- 新版 呼出元 1件 [`0081d244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081d/0081d244.md) · 呼出先 8件 [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) [`007af048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af048.md) [`007af04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af04c.md) [`007af154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af154.md) [`007af158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af158.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ade18",
      "incomplete_value": false,
      "site": "007ade18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007addc0",
      "incomplete_value": false,
      "site": "007addc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "007ade2c",
      "incomplete_value": false,
      "site": "007ade34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007addd4",
      "incomplete_value": false,
      "site": "007adddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "007addf4",
      "PARAM",
      [
        "storage",
        "002a04c5",
        null,
        "string"
      ]
    ],
    [
      "007ade00",
      "PARAM",
      [
        "storage",
        "002b8582",
        null,
        "string"
      ]
    ],
    [
      "007ade18",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007addf4",
      "PARAM",
      [
        "storage",
        "002a0478",
        null,
        "string"
      ]
    ],
    [
      "007ade00",
      "PARAM",
      [
        "storage",
        "002b852e",
        null,
        "string"
      ]
    ],
    [
      "007ade18",
      "DATA",
      [
        "storage",
        "00c7a868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007add9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007add9c) · [`007adda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007adda8) · [`007addb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md#insn-007addb0)
- 新版 [`007addf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md#insn-007addf4) · [`007ade00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md#insn-007ade00) · [`007ade08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md#insn-007ade08)

~~~diff
- 007add9c ["COPY", "tmp:0:8", ["const:4c5:8"]]
- 007add9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007add9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007add9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007addf4 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 007addf4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007addf4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007addf4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007add9c bytes 21141391
+ 007addf4 bytes 21e01191
- 007adda8 ["COPY", "tmp:0:8", ["const:582:8"]]
- 007adda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007adda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007adda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007ade00 ["COPY", "tmp:0:8", ["const:52e:8"]]
+ 007ade00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007ade00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007ade00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007adda8 bytes 21081691
+ 007ade00 bytes 21b81491
- 007addb0 ["INT_ADD", "register:40f0:8", ["const:7addb0:8", "const:4:8"]]
- 007addb0 ["CALL", null, ["callee:00c58260:8"]]
+ 007ade08 ["INT_ADD", "register:40f0:8", ["const:7ade08:8", "const:4:8"]]
+ 007ade08 ["CALL", null, ["callee:00c58260:8"]]
- 007addb0 bytes f8a81294
+ 007ade08 bytes 16a91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9a8e53b3033ae2ee4bc97dd90b03d20"></a>

### [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) → [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) FUN_007adf74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007add58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007add58.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a5018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)
- 新版 呼出元 1件 [`007addb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007addb0.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a5058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5058.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae0c0",
      "incomplete_value": false,
      "site": "007ae0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae068",
      "incomplete_value": false,
      "site": "007ae068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "definition_site": "007ae1d0",
      "incomplete_value": false,
      "site": "007ae1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae178",
      "incomplete_value": false,
      "site": "007ae178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "007ae034",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae0c0",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae134",
      "READ",
      [
        "storage",
        "00c7aac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae034",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae0c0",
      "DATA",
      [
        "storage",
        "00c7ab68",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae134",
      "READ",
      [
        "storage",
        "00c7ab90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007adf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf50) · [`007adf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf7c) · [`007adf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md#insn-007adf88)
- 新版 [`007adfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md#insn-007adfa8) · [`007adfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md#insn-007adfd4) · [`007adfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md#insn-007adfe0)

~~~diff
- 007adf50 ["INT_ADD", "register:40f0:8", ["const:7adf50:8", "const:4:8"]]
- 007adf50 ["CALL", null, ["callee:00c57f60:8"]]
+ 007adfa8 ["INT_ADD", "register:40f0:8", ["const:7adfa8:8", "const:4:8"]]
+ 007adfa8 ["CALL", null, ["callee:00c57f60:8"]]
- 007adf50 bytes d0a71294
+ 007adfa8 bytes eea71294
- 007adf7c ["INT_ADD", "register:40f0:8", ["const:7adf7c:8", "const:4:8"]]
- 007adf7c ["CALL", null, ["callee:0043bb60:8"]]
+ 007adfd4 ["INT_ADD", "register:40f0:8", ["const:7adfd4:8", "const:4:8"]]
+ 007adfd4 ["CALL", null, ["callee:0043bb60:8"]]
- 007adf7c bytes e936f297
+ 007adfd4 bytes e336f297
- 007adf88 ["INT_ADD", "register:40f0:8", ["const:7adf88:8", "const:4:8"]]
- 007adf88 ["CALL", null, ["callee:005a5058:8"]]
+ 007adfe0 ["INT_ADD", "register:40f0:8", ["const:7adfe0:8", "const:4:8"]]
+ 007adfe0 ["CALL", null, ["callee:005a5058:8"]]
- 007adf88 bytes 24dcf797
+ 007adfe0 bytes 1edcf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d47bd914838ae3211d0128ca525afb12"></a>

### [`007ae440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md) → [`007ae498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae498.md) FUN_007ae498

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae4bc",
      "incomplete_value": false,
      "site": "007ae4c0",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "007ae464",
      "incomplete_value": false,
      "site": "007ae468",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ae4c0",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae4c0",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae45c) · [`007ae474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae474) · [`007ae484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae440.md#insn-007ae484)
- 新版 [`007ae4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae498.md#insn-007ae4b4) · [`007ae4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae498.md#insn-007ae4cc) · [`007ae4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae498.md#insn-007ae4dc)

~~~diff
- 007ae45c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 007ae45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae4b4 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 007ae4b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae4b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae4b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae45c bytes 08412891
+ 007ae4b4 bytes 08812b91
- 007ae474 ["INT_ADD", "register:40f0:8", ["const:7ae474:8", "const:4:8"]]
- 007ae474 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae4cc ["INT_ADD", "register:40f0:8", ["const:7ae4cc:8", "const:4:8"]]
+ 007ae4cc ["CALL", null, ["callee:00c57f80:8"]]
- 007ae474 bytes 8fa61294
+ 007ae4cc bytes ada61294
- 007ae484 ["INT_ADD", "register:40f0:8", ["const:7ae484:8", "const:4:8"]]
- 007ae484 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae4dc ["INT_ADD", "register:40f0:8", ["const:7ae4dc:8", "const:4:8"]]
+ 007ae4dc ["CALL", null, ["callee:00c57f80:8"]]
- 007ae484 bytes 8ba61294
+ 007ae4dc bytes a9a61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40fcd44ee2ced12d24ccf497c5a5ae4f"></a>

### [`007ae4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md) → [`007ae4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae4fc.md) FUN_007ae4fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae530",
      "incomplete_value": false,
      "site": "007ae534",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "007ae4d8",
      "incomplete_value": false,
      "site": "007ae4dc",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ae534",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae534",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4c8) · [`007ae4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4d0) · [`007ae4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae4a4.md#insn-007ae4e8)
- 新版 [`007ae520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae4fc.md#insn-007ae520) · [`007ae528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae4fc.md#insn-007ae528) · [`007ae540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae4fc.md#insn-007ae540)

~~~diff
- 007ae4c8 ["INT_ADD", "register:40f0:8", ["const:7ae4c8:8", "const:4:8"]]
- 007ae4c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae520 ["INT_ADD", "register:40f0:8", ["const:7ae520:8", "const:4:8"]]
+ 007ae520 ["CALL", null, ["callee:00c57f80:8"]]
- 007ae4c8 bytes 7aa61294
+ 007ae520 bytes 98a61294
- 007ae4d0 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 007ae4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae528 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 007ae528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae4d0 bytes 08412891
+ 007ae528 bytes 08812b91
- 007ae4e8 ["INT_ADD", "register:40f0:8", ["const:7ae4e8:8", "const:4:8"]]
- 007ae4e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae540 ["INT_ADD", "register:40f0:8", ["const:7ae540:8", "const:4:8"]]
+ 007ae540 ["CALL", null, ["callee:00c57f80:8"]]
- 007ae4e8 bytes 72a61294
+ 007ae540 bytes 90a61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1150ee9f3403a0cd58d38c34803f6550"></a>

### [`007ae518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md) → [`007ae570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae570.md) FUN_007ae570

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ae5a4",
      "incomplete_value": false,
      "site": "007ae5a8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "007ae54c",
      "incomplete_value": false,
      "site": "007ae550",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ae5a8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae5a8",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae53c) · [`007ae544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae544) · [`007ae55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae518.md#insn-007ae55c)
- 新版 [`007ae594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae570.md#insn-007ae594) · [`007ae59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae570.md#insn-007ae59c) · [`007ae5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae570.md#insn-007ae5b4)

~~~diff
- 007ae53c ["INT_ADD", "register:40f0:8", ["const:7ae53c:8", "const:4:8"]]
- 007ae53c ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae594 ["INT_ADD", "register:40f0:8", ["const:7ae594:8", "const:4:8"]]
+ 007ae594 ["CALL", null, ["callee:00c57f80:8"]]
- 007ae53c bytes 5da61294
+ 007ae594 bytes 7ba61294
- 007ae544 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 007ae544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae59c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 007ae59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae544 bytes 08412891
+ 007ae59c bytes 08812b91
- 007ae55c ["INT_ADD", "register:40f0:8", ["const:7ae55c:8", "const:4:8"]]
- 007ae55c ["CALL", null, ["callee:00c57f80:8"]]
+ 007ae5b4 ["INT_ADD", "register:40f0:8", ["const:7ae5b4:8", "const:4:8"]]
+ 007ae5b4 ["CALL", null, ["callee:00c57f80:8"]]
- 007ae55c bytes 55a61294
+ 007ae5b4 bytes 73a61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f7f0d790fad650c0c7f282ac5e07303"></a>

### [`007ae58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae58c.md) → [`007ae5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae5e4.md) FUN_007ae5e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007ae5f0",
      "incomplete_value": false,
      "site": "007ae5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae598",
      "incomplete_value": false,
      "site": "007ae5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "007ae5fc",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae5fc",
      "DATA",
      [
        "storage",
        "00c7a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae58c.md#insn-007ae598)
- 新版 [`007ae5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae5e4.md#insn-007ae5f0)

~~~diff
- 007ae598 ["COPY", "tmp:0:8", ["const:408:8"]]
- 007ae598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ae598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ae598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ae5f0 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007ae5f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae5f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae5f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ae598 bytes 4a211091
+ 007ae5f0 bytes 4a611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f3544fadc543ec8322f3f4882317b9f"></a>

### [`007ae5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md) → [`007ae628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae628.md) FUN_007ae628

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007ae640",
      "incomplete_value": false,
      "site": "007ae64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae5e8",
      "incomplete_value": false,
      "site": "007ae5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "007ae64c",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae64c",
      "DATA",
      [
        "storage",
        "00c7a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md#insn-007ae5e8) · [`007ae618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae5d0.md#insn-007ae618)
- 新版 [`007ae640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae628.md#insn-007ae640) · [`007ae670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae628.md#insn-007ae670)

~~~diff
- 007ae5e8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 007ae5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae640 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007ae640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae5e8 bytes 08211091
+ 007ae640 bytes 08611391
- 007ae618 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae618 ["INT_ADD", "register:40f0:8", ["const:7ae618:8", "const:4:8"]]
- 007ae618 ["CALLIND", null, ["register:0:8"]]
+ 007ae670 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae670 ["INT_ADD", "register:40f0:8", ["const:7ae670:8", "const:4:8"]]
+ 007ae670 ["CALLIND", null, ["register:0:8"]]
- 007ae618 bytes 00013fd6
+ 007ae670 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86701007ae4c7bc5151b70b41d55a46"></a>

### [`007ae62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md) → [`007ae684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae684.md) FUN_007ae684

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007ae6ac",
      "incomplete_value": false,
      "site": "007ae6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae654",
      "incomplete_value": false,
      "site": "007ae658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "007ae6b0",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae6b0",
      "DATA",
      [
        "storage",
        "00c7a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae640) · [`007ae654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae654) · [`007ae678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae62c.md#insn-007ae678)
- 新版 [`007ae698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae684.md#insn-007ae698) · [`007ae6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae684.md#insn-007ae6ac) · [`007ae6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae684.md#insn-007ae6d0)

~~~diff
- 007ae640 ["INT_ADD", "register:40f0:8", ["const:7ae640:8", "const:4:8"]]
- 007ae640 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ae698 ["INT_ADD", "register:40f0:8", ["const:7ae698:8", "const:4:8"]]
+ 007ae698 ["CALL", null, ["callee:00c57f60:8"]]
- 007ae640 bytes 14a61294
+ 007ae698 bytes 32a61294
- 007ae654 ["COPY", "tmp:0:8", ["const:408:8"]]
- 007ae654 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae654 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae654 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ae6ac ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007ae6ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae6ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae6ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae654 bytes 29211091
+ 007ae6ac bytes 29611391
- 007ae678 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ae678 ["INT_ADD", "register:40f0:8", ["const:7ae678:8", "const:4:8"]]
- 007ae678 ["CALLIND", null, ["register:0:8"]]
+ 007ae6d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ae6d0 ["INT_ADD", "register:40f0:8", ["const:7ae6d0:8", "const:4:8"]]
+ 007ae6d0 ["CALLIND", null, ["register:0:8"]]
- 007ae678 bytes 00013fd6
+ 007ae6d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770c724c44d5111a56b68cfaf0aa8af9"></a>

### [`007ae6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md) → [`007ae714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae714.md) FUN_007ae714

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "007ae730",
      "incomplete_value": false,
      "site": "007ae734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae6d8",
      "incomplete_value": false,
      "site": "007ae6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "007ae734",
      "DATA",
      [
        "storage",
        "00c7a408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae734",
      "DATA",
      [
        "storage",
        "00c7a4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md#insn-007ae6d8) · [`007ae700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae6bc.md#insn-007ae700)
- 新版 [`007ae730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae714.md#insn-007ae730) · [`007ae758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae714.md#insn-007ae758)

~~~diff
- 007ae6d8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 007ae6d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007ae6d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007ae6d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007ae730 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 007ae730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007ae730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007ae6d8 bytes 4a211091
+ 007ae730 bytes 4a611391
- 007ae700 ["COPY", "register:0:8", ["register:4048:8"]]
- 007ae700 ["INT_ADD", "register:40f0:8", ["const:7ae700:8", "const:4:8"]]
- 007ae700 ["CALLIND", null, ["register:0:8"]]
+ 007ae758 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007ae758 ["INT_ADD", "register:40f0:8", ["const:7ae758:8", "const:4:8"]]
+ 007ae758 ["CALLIND", null, ["register:0:8"]]
- 007ae700 bytes 20013fd6
+ 007ae758 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0a9504a7f2dd1e18926641cf1944c04"></a>

### [`007ae804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md) → [`007ae85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md) FUN_007ae85c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007ae880",
      "incomplete_value": false,
      "site": "007ae880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae828",
      "incomplete_value": false,
      "site": "007ae828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae880",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae880",
      "DATA",
      [
        "storage",
        "00c7a568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md#insn-007ae818) · [`007ae824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae804.md#insn-007ae824)
- 新版 [`007ae870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md#insn-007ae870) · [`007ae87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md#insn-007ae87c)

~~~diff
- 007ae818 ["INT_ADD", "register:40f0:8", ["const:7ae818:8", "const:4:8"]]
- 007ae818 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ae870 ["INT_ADD", "register:40f0:8", ["const:7ae870:8", "const:4:8"]]
+ 007ae870 ["CALL", null, ["callee:00c57f60:8"]]
- 007ae818 bytes 9ea51294
+ 007ae870 bytes bca51294
- 007ae824 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007ae824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae87c ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007ae87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae824 bytes 08611291
+ 007ae87c bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8667197f8c32f59aa6f6afe68b26fa50"></a>

### [`007ae838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae838.md) → [`007ae890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae890.md) FUN_007ae890

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007ae89c",
      "incomplete_value": false,
      "site": "007ae89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae844",
      "incomplete_value": false,
      "site": "007ae844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae89c",
      "DATA",
      [
        "storage",
        "00c7a498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae89c",
      "DATA",
      [
        "storage",
        "00c7a568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae838.md#insn-007ae840)
- 新版 [`007ae898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae890.md#insn-007ae898)

~~~diff
- 007ae840 ["COPY", "tmp:0:8", ["const:498:8"]]
- 007ae840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ae898 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 007ae898 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae898 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ae898 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae840 bytes 29611291
+ 007ae898 bytes 29a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82356966a29fa2c8eb955cd9446787eb"></a>

### [`007ae854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md) → [`007ae8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md) FUN_007ae8ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`007ae990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae990.md) [`007ae994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae994.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) [`007ae9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9e8.md) [`007ae9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9ec.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "site": "007ae8c8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ae870",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007ae8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007ae8d8",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae910",
      "READ",
      [
        "storage",
        "00c7a538",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ae8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "007ae8d8",
      "DATA",
      [
        "storage",
        "00c7a5e8",
        null,
        "undefined *"
      ]
    ],
    [
      "007ae910",
      "READ",
      [
        "storage",
        "00c7a608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae870) · [`007ae878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae878) · [`007ae890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae854.md#insn-007ae890)
- 新版 [`007ae8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8c8) · [`007ae8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8d0) · [`007ae8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8e8)

~~~diff
- 007ae870 ["INT_ADD", "register:40f0:8", ["const:7ae870:8", "const:4:8"]]
- 007ae870 ["CALL", null, ["ram:48ccf8:8"]]
+ 007ae8c8 ["INT_ADD", "register:40f0:8", ["const:7ae8c8:8", "const:4:8"]]
+ 007ae8c8 ["CALL", null, ["ram:48cd38:8"]]
- 007ae870 bytes 2279f397
+ 007ae8c8 bytes 1c79f397
- 007ae878 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007ae878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae8d0 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 007ae8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae878 bytes 08611491
+ 007ae8d0 bytes 08a11791
- 007ae890 ["INT_ADD", "register:40f0:8", ["const:7ae890:8", "const:4:8"]]
- 007ae890 ["CALL", null, ["callee:00493914:8"]]
+ 007ae8e8 ["INT_ADD", "register:40f0:8", ["const:7ae8e8:8", "const:4:8"]]
+ 007ae8e8 ["CALL", null, ["callee:00493914:8"]]
- 007ae890 bytes 1194f397
+ 007ae8e8 bytes 0b94f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c749d41c0aa899a056ca695a77a1a99d"></a>

### [`007ae95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md) → [`007ae9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md) FUN_007ae9b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007ae9c8",
      "incomplete_value": false,
      "site": "007ae9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae970",
      "incomplete_value": false,
      "site": "007ae974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae9cc",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae9cc",
      "DATA",
      [
        "storage",
        "00c7a5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md#insn-007ae968) · [`007ae970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae95c.md#insn-007ae970)
- 新版 [`007ae9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md#insn-007ae9c0) · [`007ae9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md#insn-007ae9c8)

~~~diff
- 007ae968 ["INT_ADD", "register:40f0:8", ["const:7ae968:8", "const:4:8"]]
- 007ae968 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ae9c0 ["INT_ADD", "register:40f0:8", ["const:7ae9c0:8", "const:4:8"]]
+ 007ae9c0 ["CALL", null, ["callee:00c57f60:8"]]
- 007ae968 bytes 4aa51294
+ 007ae9c0 bytes 68a51294
- 007ae970 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007ae970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae9c8 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 007ae9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae970 bytes 08611491
+ 007ae9c8 bytes 08a11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a55688a8e914a0dc9c761f9c89dba23f"></a>

### [`007ae980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae980.md) → [`007ae9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9d8.md) FUN_007ae9d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007ae9dc",
      "incomplete_value": false,
      "site": "007ae9e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ae984",
      "incomplete_value": false,
      "site": "007ae988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007ae9e0",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ae9e0",
      "DATA",
      [
        "storage",
        "00c7a5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae980.md#insn-007ae984)
- 新版 [`007ae9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9d8.md#insn-007ae9dc)

~~~diff
- 007ae984 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007ae984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ae984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ae984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ae9dc ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 007ae9dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae9dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ae9dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ae984 bytes 08611491
+ 007ae9dc bytes 08a11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-815cd17461dfbdfff928d68e95d10377"></a>

### [`007ae998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md) → [`007ae9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md) FUN_007ae9f0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.79% / 新版 95.79%

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
      "site": "007aeae8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aea90",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007aea10",
      "READ",
      [
        "storage",
        "002b7769",
        null,
        "string"
      ]
    ],
    [
      "007aea1c",
      "READ",
      [
        "storage",
        "002b776f",
        null,
        "string"
      ]
    ],
    [
      "007aeae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "007aea10",
      "READ",
      [
        "storage",
        "002b77a9",
        null,
        "string"
      ]
    ],
    [
      "007aea1c",
      "READ",
      [
        "storage",
        "002b77af",
        null,
        "string"
      ]
    ],
    [
      "007aeae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aea90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007aea90) · [`007ae9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007ae9b0) · [`007ae9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007ae998.md#insn-007ae9e0)
- 新版 [`007aeae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md#insn-007aeae8) · [`007aea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md#insn-007aea08) · [`007aea38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9f0.md#insn-007aea38)

~~~diff
- 007aea90 ["INT_ADD", "register:40f0:8", ["const:7aea90:8", "const:4:8"]]
- 007aea90 ["CALL", null, ["ram:48ccf8:8"]]
+ 007aeae8 ["INT_ADD", "register:40f0:8", ["const:7aeae8:8", "const:4:8"]]
+ 007aeae8 ["CALL", null, ["ram:48cd38:8"]]
- 007aea90 bytes 9a78f397
+ 007aeae8 bytes 9478f397
- 007ae9b0 ["COPY", "tmp:0:8", ["const:769:8"]]
- 007ae9b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ae9b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ae9b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aea08 ["COPY", "tmp:0:8", ["const:7a9:8"]]
+ 007aea08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aea08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aea08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ae9b0 bytes 29a51d91
+ 007aea08 bytes 29a51e91
- 007ae9e0 ["INT_ADD", "register:40f0:8", ["const:7ae9e0:8", "const:4:8"]]
- 007ae9e0 ["CALL", null, ["callee:0048ce94:8"]]
+ 007aea38 ["INT_ADD", "register:40f0:8", ["const:7aea38:8", "const:4:8"]]
+ 007aea38 ["CALL", null, ["callee:0048ce94:8"]]
- 007ae9e0 bytes 1d79f397
+ 007aea38 bytes 1779f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46db6245671ff7a552e2aba75b8a9b09"></a>

### [`007aebf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md) → [`007aec4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md) FUN_007aec4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007aec70",
      "incomplete_value": false,
      "site": "007aec70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aec18",
      "incomplete_value": false,
      "site": "007aec18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007aec70",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aec70",
      "DATA",
      [
        "storage",
        "00c7a668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md#insn-007aec08) · [`007aec14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aebf4.md#insn-007aec14)
- 新版 [`007aec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md#insn-007aec60) · [`007aec6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md#insn-007aec6c)

~~~diff
- 007aec08 ["INT_ADD", "register:40f0:8", ["const:7aec08:8", "const:4:8"]]
- 007aec08 ["CALL", null, ["callee:00c57f60:8"]]
+ 007aec60 ["INT_ADD", "register:40f0:8", ["const:7aec60:8", "const:4:8"]]
+ 007aec60 ["CALL", null, ["callee:00c57f60:8"]]
- 007aec08 bytes a2a41294
+ 007aec60 bytes c0a41294
- 007aec14 ["COPY", "tmp:0:8", ["const:598:8"]]
- 007aec14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aec14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aec14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aec6c ["COPY", "tmp:0:8", ["const:668:8"]]
+ 007aec6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aec6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aec14 bytes 08611691
+ 007aec6c bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb30e638789080e3b626648f3d0e9586"></a>

### [`007aec28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec28.md) → [`007aec80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec80.md) FUN_007aec80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007aec8c",
      "incomplete_value": false,
      "site": "007aec8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aec34",
      "incomplete_value": false,
      "site": "007aec34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007aec8c",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aec8c",
      "DATA",
      [
        "storage",
        "00c7a668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aec30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec28.md#insn-007aec30)
- 新版 [`007aec88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec80.md#insn-007aec88)

~~~diff
- 007aec30 ["COPY", "tmp:0:8", ["const:598:8"]]
- 007aec30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aec30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aec30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aec88 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 007aec88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aec88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aec88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aec30 bytes 29611691
+ 007aec88 bytes 29a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c881b7eb359e9e33bf5930f295727fd"></a>

### [`007aec78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md) → [`007aecd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md) FUN_007aecd0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007aecf4",
      "incomplete_value": false,
      "site": "007aecf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aec9c",
      "incomplete_value": false,
      "site": "007aec9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "007aecf4",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aecf4",
      "DATA",
      [
        "storage",
        "00c7a6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aec8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md#insn-007aec8c) · [`007aec98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aec78.md#insn-007aec98)
- 新版 [`007aece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md#insn-007aece4) · [`007aecf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md#insn-007aecf0)

~~~diff
- 007aec8c ["INT_ADD", "register:40f0:8", ["const:7aec8c:8", "const:4:8"]]
- 007aec8c ["CALL", null, ["callee:00c57f60:8"]]
+ 007aece4 ["INT_ADD", "register:40f0:8", ["const:7aece4:8", "const:4:8"]]
+ 007aece4 ["CALL", null, ["callee:00c57f60:8"]]
- 007aec8c bytes 81a41294
+ 007aece4 bytes 9fa41294
- 007aec98 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007aec98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aec98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aec98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aecf0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 007aecf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aecf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aecf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aec98 bytes 08611891
+ 007aecf0 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67aea1e0b045aa3b7c739edefe73991e"></a>

### [`007aecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecac.md) → [`007aed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed04.md) FUN_007aed04

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007aed10",
      "incomplete_value": false,
      "site": "007aed10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aecb8",
      "incomplete_value": false,
      "site": "007aecb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "007aed10",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aed10",
      "DATA",
      [
        "storage",
        "00c7a6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aecb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecac.md#insn-007aecb4)
- 新版 [`007aed0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed04.md#insn-007aed0c)

~~~diff
- 007aecb4 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007aecb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aecb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aecb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aed0c ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 007aed0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aed0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aed0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aecb4 bytes 29611891
+ 007aed0c bytes 29a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e495ff3d9a9c7131559cc19ddaa80f43"></a>

### [`007aecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md) → [`007aed54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed54.md) FUN_007aed54

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007aed68",
      "incomplete_value": false,
      "site": "007aed6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aed10",
      "incomplete_value": false,
      "site": "007aed14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "007aed6c",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aed6c",
      "DATA",
      [
        "storage",
        "00c7a768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md#insn-007aed08) · [`007aed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aecfc.md#insn-007aed10)
- 新版 [`007aed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed54.md#insn-007aed60) · [`007aed68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed54.md#insn-007aed68)

~~~diff
- 007aed08 ["INT_ADD", "register:40f0:8", ["const:7aed08:8", "const:4:8"]]
- 007aed08 ["CALL", null, ["callee:00c57f60:8"]]
+ 007aed60 ["INT_ADD", "register:40f0:8", ["const:7aed60:8", "const:4:8"]]
+ 007aed60 ["CALL", null, ["callee:00c57f60:8"]]
- 007aed08 bytes 62a41294
+ 007aed60 bytes 80a41294
- 007aed10 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007aed10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aed10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aed10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aed68 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 007aed68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aed10 bytes 08611a91
+ 007aed68 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c2b57a31642df991e37f723256fea2f"></a>

### [`007aed20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed20.md) → [`007aed78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed78.md) FUN_007aed78

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007aed7c",
      "incomplete_value": false,
      "site": "007aed80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aed24",
      "incomplete_value": false,
      "site": "007aed28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "007aed80",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aed80",
      "DATA",
      [
        "storage",
        "00c7a768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aed24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed20.md#insn-007aed24)
- 新版 [`007aed7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed78.md#insn-007aed7c)

~~~diff
- 007aed24 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007aed24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aed24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aed24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aed7c ["COPY", "tmp:0:8", ["const:768:8"]]
+ 007aed7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aed7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aed24 bytes 08611a91
+ 007aed7c bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fea97a6a11da49c4572f7f675e03daa6"></a>

### [`007aed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md) → [`007aed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md) FUN_007aed90

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044c4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c4cc.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "site": "007aedac",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aed54",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007aedac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "007aedac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aed54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed54) · [`007aed60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed60) · [`007aed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md#insn-007aed6c)
- 新版 [`007aedac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md#insn-007aedac) · [`007aedb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md#insn-007aedb8) · [`007aedc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md#insn-007aedc4)

~~~diff
- 007aed54 ["INT_ADD", "register:40f0:8", ["const:7aed54:8", "const:4:8"]]
- 007aed54 ["CALL", null, ["ram:48ccf8:8"]]
+ 007aedac ["INT_ADD", "register:40f0:8", ["const:7aedac:8", "const:4:8"]]
+ 007aedac ["CALL", null, ["ram:48cd38:8"]]
- 007aed54 bytes e977f397
+ 007aedac bytes e377f397
- 007aed60 ["INT_ADD", "register:40f0:8", ["const:7aed60:8", "const:4:8"]]
- 007aed60 ["CALL", null, ["callee:0044c4cc:8"]]
+ 007aedb8 ["INT_ADD", "register:40f0:8", ["const:7aedb8:8", "const:4:8"]]
+ 007aedb8 ["CALL", null, ["callee:0044c4cc:8"]]
- 007aed60 bytes cb75f297
+ 007aedb8 bytes c575f297
- 007aed6c ["INT_ADD", "register:40f0:8", ["const:7aed6c:8", "const:4:8"]]
- 007aed6c ["CALL", null, ["callee:004928ec:8"]]
+ 007aedc4 ["INT_ADD", "register:40f0:8", ["const:7aedc4:8", "const:4:8"]]
+ 007aedc4 ["CALL", null, ["callee:004928ec:8"]]
- 007aed6c bytes d08ef397
+ 007aedc4 bytes ca8ef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6da7758ba18280088110a9fa3157112"></a>

### [`007aee18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md) → [`007aee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee70.md) FUN_007aee70

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007aee78",
      "incomplete_value": false,
      "site": "007aee7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aee20",
      "incomplete_value": false,
      "site": "007aee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "007aee7c",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aee7c",
      "DATA",
      [
        "storage",
        "00c7a7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md#insn-007aee20) · [`007aee44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee18.md#insn-007aee44)
- 新版 [`007aee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee70.md#insn-007aee78) · [`007aee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee70.md#insn-007aee9c)

~~~diff
- 007aee20 ["COPY", "tmp:0:8", ["const:718:8"]]
- 007aee20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007aee20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007aee20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007aee78 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007aee78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007aee78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007aee78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007aee20 bytes 29611c91
+ 007aee78 bytes 29a11f91
- 007aee44 ["INT_ADD", "register:40f0:8", ["const:7aee44:8", "const:4:8"]]
- 007aee44 ["CALL", null, ["callee:00c57f80:8"]]
+ 007aee9c ["INT_ADD", "register:40f0:8", ["const:7aee9c:8", "const:4:8"]]
+ 007aee9c ["CALL", null, ["callee:00c57f80:8"]]
- 007aee44 bytes 1ba41294
+ 007aee9c bytes 39a41294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f970b0143641243eb5ebc884f2eeb1ba"></a>

### [`007aee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md) → [`007aeeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeeb0.md) FUN_007aeeb0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007aeedc",
      "incomplete_value": false,
      "site": "007aeedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aee84",
      "incomplete_value": false,
      "site": "007aee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007aeedc",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aeedc",
      "DATA",
      [
        "storage",
        "00c7a7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aee6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aee6c) · [`007aee7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aee7c) · [`007aeea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aee58.md#insn-007aeea4)
- 新版 [`007aeec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeeb0.md#insn-007aeec4) · [`007aeed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeeb0.md#insn-007aeed4) · [`007aeefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeeb0.md#insn-007aeefc)

~~~diff
- 007aee6c ["INT_ADD", "register:40f0:8", ["const:7aee6c:8", "const:4:8"]]
- 007aee6c ["CALL", null, ["callee:00c57f60:8"]]
+ 007aeec4 ["INT_ADD", "register:40f0:8", ["const:7aeec4:8", "const:4:8"]]
+ 007aeec4 ["CALL", null, ["callee:00c57f60:8"]]
- 007aee6c bytes 09a41294
+ 007aeec4 bytes 27a41294
- 007aee7c ["COPY", "tmp:0:8", ["const:718:8"]]
- 007aee7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007aee7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007aee7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007aeed4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007aeed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007aeed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007aeed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007aee7c bytes 4a611c91
+ 007aeed4 bytes 4aa11f91
- 007aeea4 ["INT_ADD", "register:40f0:8", ["const:7aeea4:8", "const:4:8"]]
- 007aeea4 ["CALL", null, ["callee:0043bb60:8"]]
+ 007aeefc ["INT_ADD", "register:40f0:8", ["const:7aeefc:8", "const:4:8"]]
+ 007aeefc ["CALL", null, ["callee:0043bb60:8"]]
- 007aeea4 bytes 1f33f297
+ 007aeefc bytes 1933f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c5e25a645480b7ea0081020684b08d"></a>

### [`007aeecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeecc.md) → [`007aef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md) FUN_007aef24

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "007aef2c",
      "incomplete_value": false,
      "site": "007aef2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aeed4",
      "incomplete_value": false,
      "site": "007aeed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "007aef2c",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aef2c",
      "DATA",
      [
        "storage",
        "00c7a7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aeed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeecc.md#insn-007aeed0)
- 新版 [`007aef28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md#insn-007aef28)

~~~diff
- 007aeed0 ["COPY", "tmp:0:8", ["const:718:8"]]
- 007aeed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aeed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aeed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aef28 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 007aef28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aef28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aef28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aeed0 bytes 08611c91
+ 007aef28 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-315f5bba5cdeca79464cad9c5385c42e"></a>

### [`007aef50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md) → [`007aefa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md) FUN_007aefa8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "007aefb8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007aef60",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "007aefb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "007aefb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef50.md#insn-007aef60)
- 新版 [`007aefb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md#insn-007aefb8)

~~~diff
- 007aef60 ["INT_ADD", "register:40f0:8", ["const:7aef60:8", "const:4:8"]]
- 007aef60 ["CALL", null, ["ram:48ccf8:8"]]
+ 007aefb8 ["INT_ADD", "register:40f0:8", ["const:7aefb8:8", "const:4:8"]]
+ 007aefb8 ["CALL", null, ["ram:48cd38:8"]]
- 007aef60 bytes 6677f397
+ 007aefb8 bytes 6077f397
~~~


<a id="compare-cf5f2400f31c1370faa361028ba015b9"></a>

### [`007aefa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md) → [`007aeff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeff8.md) FUN_007aeff8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007af018",
      "incomplete_value": false,
      "site": "007af01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aefc0",
      "incomplete_value": false,
      "site": "007aefc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007af01c",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af01c",
      "DATA",
      [
        "storage",
        "00c7a868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aefb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md#insn-007aefb4) · [`007aefc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefa0.md#insn-007aefc0)
- 新版 [`007af00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeff8.md#insn-007af00c) · [`007af018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aeff8.md#insn-007af018)

~~~diff
- 007aefb4 ["INT_ADD", "register:40f0:8", ["const:7aefb4:8", "const:4:8"]]
- 007aefb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007af00c ["INT_ADD", "register:40f0:8", ["const:7af00c:8", "const:4:8"]]
+ 007af00c ["CALL", null, ["callee:00c57f60:8"]]
- 007aefb4 bytes b7a31294
+ 007af00c bytes d5a31294
- 007aefc0 ["COPY", "tmp:0:8", ["const:798:8"]]
- 007aefc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aefc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aefc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af018 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 007af018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aefc0 bytes 08611e91
+ 007af018 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7235642bac514ee7b1ab434375963a88"></a>

### [`007aefd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefd8.md) → [`007af030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af030.md) FUN_007af030

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007af034",
      "incomplete_value": false,
      "site": "007af038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aefdc",
      "incomplete_value": false,
      "site": "007aefe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "007af038",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af038",
      "DATA",
      [
        "storage",
        "00c7a868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aefdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aefd8.md#insn-007aefdc)
- 新版 [`007af034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af030.md#insn-007af034)

~~~diff
- 007aefdc ["COPY", "tmp:0:8", ["const:798:8"]]
- 007aefdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aefdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aefdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af034 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 007af034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aefdc bytes 08611e91
+ 007af034 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3be344b3b48cb1cff9817131d52f300b"></a>

### [`007aeff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md) → [`007af050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af050.md) FUN_007af050

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007aad04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007aa/007aad04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`007aad5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aad5c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "site": "007af084",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007af02c",
      "value": [
        "leaf",
        "ram:764384:8"
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
      "007af084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ],
  "added": [
    [
      "007af084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af02c) · [`007af024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af024) · [`007af038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aeff8.md#insn-007af038)
- 新版 [`007af084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af050.md#insn-007af084) · [`007af07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af050.md#insn-007af07c) · [`007af090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af050.md#insn-007af090)

~~~diff
- 007af02c ["INT_ADD", "register:40f0:8", ["const:7af02c:8", "const:4:8"]]
- 007af02c ["CALL", null, ["ram:764384:8"]]
+ 007af084 ["INT_ADD", "register:40f0:8", ["const:7af084:8", "const:4:8"]]
+ 007af084 ["CALL", null, ["ram:7643dc:8"]]
- 007af02c bytes d6d4fe97
+ 007af084 bytes d6d4fe97
- 007af024 ["INT_ADD", "register:40f0:8", ["const:7af024:8", "const:4:8"]]
- 007af024 ["CALL", null, ["callee:00851550:8"]]
+ 007af07c ["INT_ADD", "register:40f0:8", ["const:7af07c:8", "const:4:8"]]
+ 007af07c ["CALL", null, ["callee:00851550:8"]]
- 007af024 bytes 35890294
+ 007af07c bytes 35890294
- 007af038 ["INT_ADD", "register:40f0:8", ["const:7af038:8", "const:4:8"]]
- 007af038 ["CALL", null, ["callee:007aad5c:8"]]
+ 007af090 ["INT_ADD", "register:40f0:8", ["const:7af090:8", "const:4:8"]]
+ 007af090 ["CALL", null, ["callee:007aad5c:8"]]
- 007af038 bytes 33efff97
+ 007af090 bytes 33efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e095e6826e99abcaed3747fcb5262c3"></a>

### [`007af0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md) → [`007af120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af120.md) FUN_007af120

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007af134",
      "incomplete_value": false,
      "site": "007af138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af0dc",
      "incomplete_value": false,
      "site": "007af0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "007af138",
      "DATA",
      [
        "storage",
        "00c7a818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af138",
      "DATA",
      [
        "storage",
        "00c7a8e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md#insn-007af0d4) · [`007af0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af0c8.md#insn-007af0dc)
- 新版 [`007af12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af120.md#insn-007af12c) · [`007af134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af120.md#insn-007af134)

~~~diff
- 007af0d4 ["INT_ADD", "register:40f0:8", ["const:7af0d4:8", "const:4:8"]]
- 007af0d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007af12c ["INT_ADD", "register:40f0:8", ["const:7af12c:8", "const:4:8"]]
+ 007af12c ["CALL", null, ["callee:00c57f60:8"]]
- 007af0d4 bytes 6fa31294
+ 007af12c bytes 8da31294
- 007af0dc ["COPY", "tmp:0:8", ["const:818:8"]]
- 007af0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af134 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 007af134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af0dc bytes 08612091
+ 007af134 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af21dd93e11cffcb46f315745b57f4ec"></a>

### [`007af130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md) → [`007af188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af188.md) FUN_007af188

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ab754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007ab754.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007ab7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007ab7ac.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "007af1c0",
      "incomplete_value": false,
      "site": "007af1c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af168",
      "incomplete_value": false,
      "site": "007af170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "007af1c8",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af280",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af1c8",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "007af280",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af160) · [`007af168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af168) · [`007af16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af130.md#insn-007af16c)
- 新版 [`007af1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af188.md#insn-007af1b8) · [`007af1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af188.md#insn-007af1c0)

~~~diff
- 007af160 ["INT_ADD", "register:40f0:8", ["const:7af160:8", "const:4:8"]]
- 007af160 ["CALL", null, ["callee:00c57f60:8"]]
+ 007af1b8 ["INT_ADD", "register:40f0:8", ["const:7af1b8:8", "const:4:8"]]
+ 007af1b8 ["CALL", null, ["callee:00c57f60:8"]]
- 007af160 bytes 4ca31294
+ 007af1b8 bytes 6aa31294
- 007af168 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 007af168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af1c0 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 007af1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af168 bytes 08011791
+ 007af1c0 bytes 08411a91
- 007af16c ["COPY", "register:4098:8", ["register:4000:8"]]
- 007af16c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fab37eff2322e2a55dc817a0e3dbb30"></a>

### [`007af2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af2a8.md) → [`007af300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af300.md) FUN_007af300

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007af30c",
      "incomplete_value": false,
      "site": "007af318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af2b4",
      "incomplete_value": false,
      "site": "007af2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007af318",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af318",
      "DATA",
      [
        "storage",
        "00c7a968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af2a8.md#insn-007af2b4)
- 新版 [`007af30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af300.md#insn-007af30c)

~~~diff
- 007af2b4 ["COPY", "tmp:0:8", ["const:898:8"]]
- 007af2b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007af2b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007af2b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007af30c ["COPY", "tmp:0:8", ["const:968:8"]]
+ 007af30c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007af30c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007af30c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007af2b4 bytes 4a612291
+ 007af30c bytes 4aa12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2e45996f58e5fa5098f75095da9112"></a>

### [`007af348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md) → [`007af3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af3a0.md) FUN_007af3a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007af3cc",
      "incomplete_value": false,
      "site": "007af3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af374",
      "incomplete_value": false,
      "site": "007af374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007af3cc",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af3cc",
      "DATA",
      [
        "storage",
        "00c7a968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af35c) · [`007af36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af36c) · [`007af390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af348.md#insn-007af390)
- 新版 [`007af3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af3a0.md#insn-007af3b4) · [`007af3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af3a0.md#insn-007af3c4) · [`007af3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af3a0.md#insn-007af3e8)

~~~diff
- 007af35c ["INT_ADD", "register:40f0:8", ["const:7af35c:8", "const:4:8"]]
- 007af35c ["CALL", null, ["callee:00c57f60:8"]]
+ 007af3b4 ["INT_ADD", "register:40f0:8", ["const:7af3b4:8", "const:4:8"]]
+ 007af3b4 ["CALL", null, ["callee:00c57f60:8"]]
- 007af35c bytes cda21294
+ 007af3b4 bytes eba21294
- 007af36c ["COPY", "tmp:0:8", ["const:898:8"]]
- 007af36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af3c4 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 007af3c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af3c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af3c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af36c bytes 08612291
+ 007af3c4 bytes 08a12591
- 007af390 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af390 ["INT_ADD", "register:40f0:8", ["const:7af390:8", "const:4:8"]]
- 007af390 ["CALLIND", null, ["register:0:8"]]
+ 007af3e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af3e8 ["INT_ADD", "register:40f0:8", ["const:7af3e8:8", "const:4:8"]]
+ 007af3e8 ["CALLIND", null, ["register:0:8"]]
- 007af390 bytes 00013fd6
+ 007af3e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b59abc7721cc4bb5b525c5c82d0d771"></a>

### [`007af3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md) → [`007af428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af428.md) FUN_007af428

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007af444",
      "incomplete_value": false,
      "site": "007af444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af3ec",
      "incomplete_value": false,
      "site": "007af3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007af444",
      "DATA",
      [
        "storage",
        "00c7a898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af444",
      "DATA",
      [
        "storage",
        "00c7a968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md#insn-007af3e8) · [`007af40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af3d0.md#insn-007af40c)
- 新版 [`007af440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af428.md#insn-007af440) · [`007af464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af428.md#insn-007af464)

~~~diff
- 007af3e8 ["COPY", "tmp:0:8", ["const:898:8"]]
- 007af3e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007af3e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007af3e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007af440 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 007af440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007af440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007af440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007af3e8 bytes 29612291
+ 007af440 bytes 29a12591
- 007af40c ["COPY", "register:0:8", ["register:4048:8"]]
- 007af40c ["INT_ADD", "register:40f0:8", ["const:7af40c:8", "const:4:8"]]
- 007af40c ["CALLIND", null, ["register:0:8"]]
+ 007af464 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007af464 ["INT_ADD", "register:40f0:8", ["const:7af464:8", "const:4:8"]]
+ 007af464 ["CALLIND", null, ["register:0:8"]]
- 007af40c bytes 20013fd6
+ 007af464 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-885242695ccd7e48990e9fcf90ad1af3"></a>

### [`007af62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af62c.md) → [`007af684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af684.md) FUN_007af684

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007af690",
      "incomplete_value": false,
      "site": "007af69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af638",
      "incomplete_value": false,
      "site": "007af644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "007af69c",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af69c",
      "DATA",
      [
        "storage",
        "00c7a9e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af62c.md#insn-007af638)
- 新版 [`007af690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af684.md#insn-007af690)

~~~diff
- 007af638 ["COPY", "tmp:0:8", ["const:918:8"]]
- 007af638 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007af638 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007af638 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007af690 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 007af690 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007af690 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007af690 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007af638 bytes 4a612491
+ 007af690 bytes 4aa12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db75f4ec5e40178bc16977a8f4504ffb"></a>

### [`007af670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md) → [`007af6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af6c8.md) FUN_007af6c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007af6e0",
      "incomplete_value": false,
      "site": "007af6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af688",
      "incomplete_value": false,
      "site": "007af694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "007af6ec",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af6ec",
      "DATA",
      [
        "storage",
        "00c7a9e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md#insn-007af688) · [`007af6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af670.md#insn-007af6b8)
- 新版 [`007af6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af6c8.md#insn-007af6e0) · [`007af710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af6c8.md#insn-007af710)

~~~diff
- 007af688 ["COPY", "tmp:0:8", ["const:918:8"]]
- 007af688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af6e0 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 007af6e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af6e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af6e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af688 bytes 08612491
+ 007af6e0 bytes 08a12791
- 007af6b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af6b8 ["INT_ADD", "register:40f0:8", ["const:7af6b8:8", "const:4:8"]]
- 007af6b8 ["CALLIND", null, ["register:0:8"]]
+ 007af710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af710 ["INT_ADD", "register:40f0:8", ["const:7af710:8", "const:4:8"]]
+ 007af710 ["CALLIND", null, ["register:0:8"]]
- 007af6b8 bytes 00013fd6
+ 007af710 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea9efc1a3870a8d733906bc8066fa2e"></a>

### [`007af6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af6cc.md) → [`007af724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af724.md) FUN_007af724

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007af750",
      "incomplete_value": false,
      "site": "007af750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af6f8",
      "incomplete_value": false,
      "site": "007af6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "007af750",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af750",
      "DATA",
      [
        "storage",
        "00c7a9e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af6cc.md#insn-007af6e0) · [`007af6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af6cc.md#insn-007af6f0) · [`007af714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af6cc.md#insn-007af714)
- 新版 [`007af738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af724.md#insn-007af738) · [`007af748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af724.md#insn-007af748) · [`007af76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af724.md#insn-007af76c)

~~~diff
- 007af6e0 ["INT_ADD", "register:40f0:8", ["const:7af6e0:8", "const:4:8"]]
- 007af6e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007af738 ["INT_ADD", "register:40f0:8", ["const:7af738:8", "const:4:8"]]
+ 007af738 ["CALL", null, ["callee:00c57f60:8"]]
- 007af6e0 bytes eca11294
+ 007af738 bytes 0aa21294
- 007af6f0 ["COPY", "tmp:0:8", ["const:918:8"]]
- 007af6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af748 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 007af748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af6f0 bytes 08612491
+ 007af748 bytes 08a12791
- 007af714 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af714 ["INT_ADD", "register:40f0:8", ["const:7af714:8", "const:4:8"]]
- 007af714 ["CALLIND", null, ["register:0:8"]]
+ 007af76c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af76c ["INT_ADD", "register:40f0:8", ["const:7af76c:8", "const:4:8"]]
+ 007af76c ["CALLIND", null, ["register:0:8"]]
- 007af714 bytes 00013fd6
+ 007af76c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca93a033ba9424b6daa222ccdf93ca57"></a>

### [`007af754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af754.md) → [`007af7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af7ac.md) FUN_007af7ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007af7c8",
      "incomplete_value": false,
      "site": "007af7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af770",
      "incomplete_value": false,
      "site": "007af770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:918:8"
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
      "007af7c8",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af7c8",
      "DATA",
      [
        "storage",
        "00c7a9e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af754.md#insn-007af76c) · [`007af790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af754.md#insn-007af790)
- 新版 [`007af7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af7ac.md#insn-007af7c4) · [`007af7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af7ac.md#insn-007af7e8)

~~~diff
- 007af76c ["COPY", "tmp:0:8", ["const:918:8"]]
- 007af76c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007af76c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007af76c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007af7c4 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 007af7c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007af7c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007af7c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007af76c bytes 29612491
+ 007af7c4 bytes 29a12791
- 007af790 ["COPY", "register:0:8", ["register:4048:8"]]
- 007af790 ["INT_ADD", "register:40f0:8", ["const:7af790:8", "const:4:8"]]
- 007af790 ["CALLIND", null, ["register:0:8"]]
+ 007af7e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007af7e8 ["INT_ADD", "register:40f0:8", ["const:7af7e8:8", "const:4:8"]]
+ 007af7e8 ["CALLIND", null, ["register:0:8"]]
- 007af790 bytes 20013fd6
+ 007af7e8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d6ba64143f7dac27da28ba852f2bf6d"></a>

### [`007af898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af898.md) → [`007af8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af8f0.md) FUN_007af8f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "007af928",
      "incomplete_value": false,
      "site": "007af930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af8d0",
      "incomplete_value": false,
      "site": "007af8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "007af930",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af9e8",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af930",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "007af9e8",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af898.md#insn-007af8c8) · [`007af8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af898.md#insn-007af8d0) · [`007af8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af898.md#insn-007af8d4)
- 新版 [`007af920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af8f0.md#insn-007af920) · [`007af928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af8f0.md#insn-007af928)

~~~diff
- 007af8c8 ["INT_ADD", "register:40f0:8", ["const:7af8c8:8", "const:4:8"]]
- 007af8c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007af920 ["INT_ADD", "register:40f0:8", ["const:7af920:8", "const:4:8"]]
+ 007af920 ["CALL", null, ["callee:00c57f60:8"]]
- 007af8c8 bytes 72a11294
+ 007af920 bytes 90a11294
- 007af8d0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 007af8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af928 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 007af928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af8d0 bytes 08011791
+ 007af928 bytes 08411a91
- 007af8d4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007af8d4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4c90d55f49aafe5410f056c09362ae8"></a>

### [`007afa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa10.md) → [`007afa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afa68.md) FUN_007afa68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007afa74",
      "incomplete_value": false,
      "site": "007afa80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afa1c",
      "incomplete_value": false,
      "site": "007afa28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "007afa80",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afa80",
      "DATA",
      [
        "storage",
        "00c7aa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afa1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa10.md#insn-007afa1c)
- 新版 [`007afa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afa68.md#insn-007afa74)

~~~diff
- 007afa1c ["COPY", "tmp:0:8", ["const:998:8"]]
- 007afa1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007afa1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007afa1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007afa74 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007afa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007afa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007afa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007afa1c bytes 4a612691
+ 007afa74 bytes 4aa12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95170b49b11c624c441647fb2fb8da78"></a>

### [`007afa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa54.md) → [`007afaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afaac.md) FUN_007afaac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007afac4",
      "incomplete_value": false,
      "site": "007afad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afa6c",
      "incomplete_value": false,
      "site": "007afa78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007afad0",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afad0",
      "DATA",
      [
        "storage",
        "00c7aa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afa6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa54.md#insn-007afa6c) · [`007afa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa54.md#insn-007afa9c)
- 新版 [`007afac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afaac.md#insn-007afac4) · [`007afaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afaac.md#insn-007afaf4)

~~~diff
- 007afa6c ["COPY", "tmp:0:8", ["const:998:8"]]
- 007afa6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afa6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afa6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afac4 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007afac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afa6c bytes 08612691
+ 007afac4 bytes 08a12991
- 007afa9c ["COPY", "register:0:8", ["register:4040:8"]]
- 007afa9c ["INT_ADD", "register:40f0:8", ["const:7afa9c:8", "const:4:8"]]
- 007afa9c ["CALLIND", null, ["register:0:8"]]
+ 007afaf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afaf4 ["INT_ADD", "register:40f0:8", ["const:7afaf4:8", "const:4:8"]]
+ 007afaf4 ["CALLIND", null, ["register:0:8"]]
- 007afa9c bytes 00013fd6
+ 007afaf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62537961aa303205a82a3215d8ee5018"></a>

### [`007afab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afab0.md) → [`007afb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb08.md) FUN_007afb08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007afb34",
      "incomplete_value": false,
      "site": "007afb34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afadc",
      "incomplete_value": false,
      "site": "007afadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007afb34",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afb34",
      "DATA",
      [
        "storage",
        "00c7aa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afab0.md#insn-007afac4) · [`007afad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afab0.md#insn-007afad4) · [`007afaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afab0.md#insn-007afaf8)
- 新版 [`007afb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb08.md#insn-007afb1c) · [`007afb2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb08.md#insn-007afb2c) · [`007afb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb08.md#insn-007afb50)

~~~diff
- 007afac4 ["INT_ADD", "register:40f0:8", ["const:7afac4:8", "const:4:8"]]
- 007afac4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007afb1c ["INT_ADD", "register:40f0:8", ["const:7afb1c:8", "const:4:8"]]
+ 007afb1c ["CALL", null, ["callee:00c57f60:8"]]
- 007afac4 bytes f3a01294
+ 007afb1c bytes 11a11294
- 007afad4 ["COPY", "tmp:0:8", ["const:998:8"]]
- 007afad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afb2c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007afb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afad4 bytes 08612691
+ 007afb2c bytes 08a12991
- 007afaf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afaf8 ["INT_ADD", "register:40f0:8", ["const:7afaf8:8", "const:4:8"]]
- 007afaf8 ["CALLIND", null, ["register:0:8"]]
+ 007afb50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afb50 ["INT_ADD", "register:40f0:8", ["const:7afb50:8", "const:4:8"]]
+ 007afb50 ["CALLIND", null, ["register:0:8"]]
- 007afaf8 bytes 00013fd6
+ 007afb50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f45e154eede6e2028a460e6ae0e9122"></a>

### [`007afb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afb38.md) → [`007afb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb90.md) FUN_007afb90

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007afbac",
      "incomplete_value": false,
      "site": "007afbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afb54",
      "incomplete_value": false,
      "site": "007afb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007afbac",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afbac",
      "DATA",
      [
        "storage",
        "00c7aa68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afb38.md#insn-007afb50) · [`007afb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afb38.md#insn-007afb74)
- 新版 [`007afba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb90.md#insn-007afba8) · [`007afbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afb90.md#insn-007afbcc)

~~~diff
- 007afb50 ["COPY", "tmp:0:8", ["const:998:8"]]
- 007afb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007afb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007afb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007afba8 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 007afba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007afba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007afba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007afb50 bytes 29612691
+ 007afba8 bytes 29a12991
- 007afb74 ["COPY", "register:0:8", ["register:4048:8"]]
- 007afb74 ["INT_ADD", "register:40f0:8", ["const:7afb74:8", "const:4:8"]]
- 007afb74 ["CALLIND", null, ["register:0:8"]]
+ 007afbcc ["COPY", "register:0:8", ["register:4048:8"]]
+ 007afbcc ["INT_ADD", "register:40f0:8", ["const:7afbcc:8", "const:4:8"]]
+ 007afbcc ["CALLIND", null, ["register:0:8"]]
- 007afb74 bytes 20013fd6
+ 007afbcc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f602ddad27607a3e349abd3074e7d5"></a>

### [`007afc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc7c.md) → [`007afcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afcd4.md) FUN_007afcd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007afce0",
      "incomplete_value": false,
      "site": "007afcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afc88",
      "incomplete_value": false,
      "site": "007afc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007afcec",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afcec",
      "DATA",
      [
        "storage",
        "00c7aae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc7c.md#insn-007afc88)
- 新版 [`007afce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afcd4.md#insn-007afce0)

~~~diff
- 007afc88 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007afc88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007afc88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007afc88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007afce0 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 007afce0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007afce0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007afce0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007afc88 bytes 4a612891
+ 007afce0 bytes 4aa12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6641f2924663a3b87927eb85a99d56e8"></a>

### [`007afcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afcc0.md) → [`007afd18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd18.md) FUN_007afd18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007afd30",
      "incomplete_value": false,
      "site": "007afd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afcd8",
      "incomplete_value": false,
      "site": "007afce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007afd3c",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afd3c",
      "DATA",
      [
        "storage",
        "00c7aae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afcc0.md#insn-007afcd8) · [`007afd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afcc0.md#insn-007afd08)
- 新版 [`007afd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd18.md#insn-007afd30) · [`007afd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd18.md#insn-007afd60)

~~~diff
- 007afcd8 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007afcd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afcd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afcd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afd30 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 007afd30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afcd8 bytes 08612891
+ 007afd30 bytes 08a12b91
- 007afd08 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afd08 ["INT_ADD", "register:40f0:8", ["const:7afd08:8", "const:4:8"]]
- 007afd08 ["CALLIND", null, ["register:0:8"]]
+ 007afd60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afd60 ["INT_ADD", "register:40f0:8", ["const:7afd60:8", "const:4:8"]]
+ 007afd60 ["CALLIND", null, ["register:0:8"]]
- 007afd08 bytes 00013fd6
+ 007afd60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8294130d0d8fa79c0f714a0139d8b986"></a>

### [`007afd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md) → [`007afd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd74.md) FUN_007afd74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007afda0",
      "incomplete_value": false,
      "site": "007afda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afd48",
      "incomplete_value": false,
      "site": "007afd48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007afda0",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afda0",
      "DATA",
      [
        "storage",
        "00c7aae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md#insn-007afd30) · [`007afd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md#insn-007afd40) · [`007afd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md#insn-007afd64)
- 新版 [`007afd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd74.md#insn-007afd88) · [`007afd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd74.md#insn-007afd98) · [`007afdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afd74.md#insn-007afdbc)

~~~diff
- 007afd30 ["INT_ADD", "register:40f0:8", ["const:7afd30:8", "const:4:8"]]
- 007afd30 ["CALL", null, ["callee:00c57f60:8"]]
+ 007afd88 ["INT_ADD", "register:40f0:8", ["const:7afd88:8", "const:4:8"]]
+ 007afd88 ["CALL", null, ["callee:00c57f60:8"]]
- 007afd30 bytes 58a01294
+ 007afd88 bytes 76a01294
- 007afd40 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007afd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afd98 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 007afd98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afd40 bytes 08612891
+ 007afd98 bytes 08a12b91
- 007afd64 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afd64 ["INT_ADD", "register:40f0:8", ["const:7afd64:8", "const:4:8"]]
- 007afd64 ["CALLIND", null, ["register:0:8"]]
+ 007afdbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afdbc ["INT_ADD", "register:40f0:8", ["const:7afdbc:8", "const:4:8"]]
+ 007afdbc ["CALLIND", null, ["register:0:8"]]
- 007afd64 bytes 00013fd6
+ 007afdbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3b56312708addbe3fc180d4dc56366a"></a>

### [`007afda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afda4.md) → [`007afdfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afdfc.md) FUN_007afdfc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007afe18",
      "incomplete_value": false,
      "site": "007afe18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afdc0",
      "incomplete_value": false,
      "site": "007afdc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "007afe18",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afe18",
      "DATA",
      [
        "storage",
        "00c7aae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afda4.md#insn-007afdbc) · [`007afde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afda4.md#insn-007afde0)
- 新版 [`007afe14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afdfc.md#insn-007afe14) · [`007afe38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007afdfc.md#insn-007afe38)

~~~diff
- 007afdbc ["COPY", "tmp:0:8", ["const:a18:8"]]
- 007afdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007afdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007afdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007afe14 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 007afe14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007afe14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007afe14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007afdbc bytes 29612891
+ 007afe14 bytes 29a12b91
- 007afde0 ["COPY", "register:0:8", ["register:4048:8"]]
- 007afde0 ["INT_ADD", "register:40f0:8", ["const:7afde0:8", "const:4:8"]]
- 007afde0 ["CALLIND", null, ["register:0:8"]]
+ 007afe38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007afe38 ["INT_ADD", "register:40f0:8", ["const:7afe38:8", "const:4:8"]]
+ 007afe38 ["CALLIND", null, ["register:0:8"]]
- 007afde0 bytes 20013fd6
+ 007afe38 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45862494c0829a42084269ba7151db7f"></a>

### [`007aff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md) → [`007aff94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007aff94.md) FUN_007aff94

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "007affcc",
      "incomplete_value": false,
      "site": "007affd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007aff74",
      "incomplete_value": false,
      "site": "007aff7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "007affd4",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007b008c",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007affd4",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "007b008c",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aff6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md#insn-007aff6c) · [`007aff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md#insn-007aff74) · [`007aff78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md#insn-007aff78)
- 新版 [`007affc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007aff94.md#insn-007affc4) · [`007affcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007aff94.md#insn-007affcc)

~~~diff
- 007aff6c ["INT_ADD", "register:40f0:8", ["const:7aff6c:8", "const:4:8"]]
- 007aff6c ["CALL", null, ["callee:00c57f60:8"]]
+ 007affc4 ["INT_ADD", "register:40f0:8", ["const:7affc4:8", "const:4:8"]]
+ 007affc4 ["CALL", null, ["callee:00c57f60:8"]]
- 007aff6c bytes c99f1294
+ 007affc4 bytes e79f1294
- 007aff74 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 007aff74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aff74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aff74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007affcc ["COPY", "tmp:0:8", ["const:690:8"]]
+ 007affcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007affcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007affcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aff74 bytes 08011791
+ 007affcc bytes 08411a91
- 007aff78 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007aff78 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38106ebca877064b8a651726bf116136"></a>

### [`007b00b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00b4.md) → [`007b010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b010c.md) FUN_007b010c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007b0118",
      "incomplete_value": false,
      "site": "007b0124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b00c0",
      "incomplete_value": false,
      "site": "007b00cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "007b0124",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0124",
      "DATA",
      [
        "storage",
        "00c7ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b00c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00b4.md#insn-007b00c0)
- 新版 [`007b0118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b010c.md#insn-007b0118)

~~~diff
- 007b00c0 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 007b00c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b00c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b00c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b0118 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 007b0118 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0118 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0118 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b00c0 bytes 4a612a91
+ 007b0118 bytes 4aa12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

