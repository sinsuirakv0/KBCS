# v16.0.0 → v16.0.1 · 最優先の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-ae266544ae7b18e20aa97ab4ff253392"></a>

### [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) → [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) FUN_0049f42c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 77件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 77件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md) [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) [`004a21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0049f438",
      "incomplete_value": false,
      "site": "0049f43c",
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
      "definition_site": "0049f3f8",
      "incomplete_value": false,
      "site": "0049f3fc",
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
      "0049f438",
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
      "0049f438",
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

- 旧版 [`0049f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md#insn-0049f3fc) · [`0049f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md#insn-0049f3f8)
- 新版 `0049f43c`（命令位置の公開資料なし） · `0049f438`（命令位置の公開資料なし）

~~~diff
- 0049f3fc ["INT_ADD", "register:40f0:8", ["const:49f3fc:8", "const:4:8"]]
- 0049f3fc ["CALL", null, ["callee:0043b778:8"]]
+ 0049f43c ["INT_ADD", "register:40f0:8", ["const:49f43c:8", "const:4:8"]]
+ 0049f43c ["CALL", null, ["callee:0043b778:8"]]
- 0049f3fc bytes cf70fe97
+ 0049f43c bytes cf70fe97
- 0049f3f8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f3f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f438 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f438 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f438 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f438 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f3f8 bytes 00303c91
+ 0049f438 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9101c9fd55e5cda68a96102ba9138beb"></a>

### [`0049f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md) → [`0049f8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8b8.md) FUN_0049f8b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0049f72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0049f8c4",
      "incomplete_value": false,
      "site": "0049f8c8",
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
      "definition_site": "0049f884",
      "incomplete_value": false,
      "site": "0049f888",
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
      "0049f8c4",
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
      "0049f8c4",
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

- 旧版 [`0049f888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md#insn-0049f888) · [`0049f884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f878.md#insn-0049f884)
- 新版 `0049f8c8`（命令位置の公開資料なし） · `0049f8c4`（命令位置の公開資料なし）

~~~diff
- 0049f888 ["INT_ADD", "register:40f0:8", ["const:49f888:8", "const:4:8"]]
- 0049f888 ["CALL", null, ["callee:0043b778:8"]]
+ 0049f8c8 ["INT_ADD", "register:40f0:8", ["const:49f8c8:8", "const:4:8"]]
+ 0049f8c8 ["CALL", null, ["callee:0043b778:8"]]
- 0049f888 bytes ac6ffe97
+ 0049f8c8 bytes ac6ffe97
- 0049f884 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f884 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f884 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f884 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f8c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f8c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f884 bytes 00303c91
+ 0049f8c4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46d794f06f0b12b3037e16875136f0a"></a>

### [`0049f88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md) → [`0049f8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8cc.md) FUN_0049f8cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0049f8d8",
      "incomplete_value": false,
      "site": "0049f8dc",
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
      "definition_site": "0049f898",
      "incomplete_value": false,
      "site": "0049f89c",
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
      "0049f8d8",
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
      "0049f8d8",
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

- 旧版 [`0049f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md#insn-0049f89c) · [`0049f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f88c.md#insn-0049f898)
- 新版 `0049f8dc`（命令位置の公開資料なし） · `0049f8d8`（命令位置の公開資料なし）

~~~diff
- 0049f89c ["INT_ADD", "register:40f0:8", ["const:49f89c:8", "const:4:8"]]
- 0049f89c ["CALL", null, ["callee:00442930:8"]]
+ 0049f8dc ["INT_ADD", "register:40f0:8", ["const:49f8dc:8", "const:4:8"]]
+ 0049f8dc ["CALL", null, ["callee:00442930:8"]]
- 0049f89c bytes 158cfe97
+ 0049f8dc bytes 158cfe97
- 0049f898 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f898 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f898 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f898 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f8d8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f8d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f898 bytes 00303c91
+ 0049f8d8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aa47412dbc434d35a39ba3dbf5df302"></a>

### [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) → [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) FUN_0049f8e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 4件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0049f8ec",
      "incomplete_value": false,
      "site": "0049f8f0",
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
      "definition_site": "0049f8ac",
      "incomplete_value": false,
      "site": "0049f8b0",
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
      "0049f8ec",
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
      "0049f8ec",
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

- 旧版 [`0049f8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md#insn-0049f8b0) · [`0049f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md#insn-0049f8ac)
- 新版 `0049f8f0`（命令位置の公開資料なし） · `0049f8ec`（命令位置の公開資料なし）

~~~diff
- 0049f8b0 ["INT_ADD", "register:40f0:8", ["const:49f8b0:8", "const:4:8"]]
- 0049f8b0 ["CALL", null, ["callee:00442930:8"]]
+ 0049f8f0 ["INT_ADD", "register:40f0:8", ["const:49f8f0:8", "const:4:8"]]
+ 0049f8f0 ["CALL", null, ["callee:00442930:8"]]
- 0049f8b0 bytes 108cfe97
+ 0049f8f0 bytes 108cfe97
- 0049f8ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f8ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f8ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f8ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f8ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f8ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f8ac bytes 00303c91
+ 0049f8ec bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09191edee25dc34c4448babda9be8318"></a>

### [`0049fa3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md) → [`0049fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md) FUN_0049fa7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fad8",
      "incomplete_value": false,
      "site": "0049fae0",
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
            "const:97d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fa98",
      "incomplete_value": false,
      "site": "0049faa0",
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
            "const:93d:8"
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
      "definition_site": "0049fae8",
      "incomplete_value": true,
      "site": "0049faec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049faa8",
      "incomplete_value": true,
      "site": "0049faac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "0049fae0",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049fae8",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049fae8",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049fae0",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "0049fae8",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049fae8",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049faac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049faac) · [`0049fa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049fa90) · [`0049fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fa3c.md#insn-0049fa98)
- 新版 `0049faec`（命令位置の公開資料なし） · `0049fad0`（命令位置の公開資料なし） · `0049fad8`（命令位置の公開資料なし）

~~~diff
- 0049faac ["INT_ADD", "register:40f0:8", ["const:49faac:8", "const:4:8"]]
- 0049faac ["CALL", null, ["callee:00c57f10:8"]]
+ 0049faec ["INT_ADD", "register:40f0:8", ["const:49faec:8", "const:4:8"]]
+ 0049faec ["CALL", null, ["callee:00c57f10:8"]]
- 0049faac bytes 19e01e94
+ 0049faec bytes 09e11e94
- 0049fa90 ["INT_ADD", "register:40f0:8", ["const:49fa90:8", "const:4:8"]]
- 0049fa90 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0049fad0 ["INT_ADD", "register:40f0:8", ["const:49fad0:8", "const:4:8"]]
+ 0049fad0 ["CALL", null, ["callee:00c57ef0:8"]]
- 0049fa90 bytes 18e01e94
+ 0049fad0 bytes 08e11e94
- 0049fa98 ["COPY", "tmp:0:8", ["const:93d:8"]]
- 0049fa98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049fa98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049fa98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049fad8 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 0049fad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049fa98 bytes 08f52491
+ 0049fad8 bytes 08f52591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3faa6a4fe52d9c9b1a4ce9ec4f6d457"></a>

### [`0049fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md) → [`0049faf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md) FUN_0049faf0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 5件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fb74",
      "incomplete_value": true,
      "site": "0049fb8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fb34",
      "incomplete_value": true,
      "site": "0049fb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c90:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fbdc",
      "incomplete_value": false,
      "site": "0049fbe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fb9c",
      "incomplete_value": false,
      "site": "0049fba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:2d:8"
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
      "definition_site": "0049fc00",
      "incomplete_value": false,
      "site": "0049fc04",
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
            "const:7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fbc0",
      "incomplete_value": false,
      "site": "0049fbc4",
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
            "const:3a:8"
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
      "0049fb74",
      "READ",
      [
        "storage",
        "002c2c90",
        null,
        null
      ]
    ],
    [
      "0049fbe4",
      "DATA",
      [
        "storage",
        "002b802d",
        null,
        "string"
      ]
    ],
    [
      "0049fbec",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fb74",
      "READ",
      [
        "storage",
        "002c2cd0",
        null,
        null
      ]
    ],
    [
      "0049fbe4",
      "DATA",
      [
        "storage",
        "002b806d",
        null,
        "string"
      ]
    ],
    [
      "0049fbec",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049fb0c) · [`0049fbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049fbb0) · [`0049fbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md#insn-0049fbe4)
- 新版 `0049fb4c`（命令位置の公開資料なし） · `0049fbf0`（命令位置の公開資料なし） · `0049fc24`（命令位置の公開資料なし）

~~~diff
- 0049fb0c ["INT_ADD", "register:40f0:8", ["const:49fb0c:8", "const:4:8"]]
- 0049fb0c ["CALL", null, ["callee:0049b4a0:8"]]
+ 0049fb4c ["INT_ADD", "register:40f0:8", ["const:49fb4c:8", "const:4:8"]]
+ 0049fb4c ["CALL", null, ["callee:0049b4a0:8"]]
- 0049fb0c bytes 55eeff97
+ 0049fb4c bytes 55eeff97
- 0049fbb0 ["INT_ADD", "register:40f0:8", ["const:49fbb0:8", "const:4:8"]]
- 0049fbb0 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049fbf0 ["INT_ADD", "register:40f0:8", ["const:49fbf0:8", "const:4:8"]]
+ 0049fbf0 ["CALL", null, ["callee:00c57f10:8"]]
- 0049fbb0 bytes d8df1e94
+ 0049fbf0 bytes c8e01e94
- 0049fbe4 ["INT_ADD", "register:40f0:8", ["const:49fbe4:8", "const:4:8"]]
- 0049fbe4 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049fc24 ["INT_ADD", "register:40f0:8", ["const:49fc24:8", "const:4:8"]]
+ 0049fc24 ["CALL", null, ["callee:00c57f10:8"]]
- 0049fbe4 bytes cbdf1e94
+ 0049fc24 bytes bbe01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f848faf5fc14acec0d217f4f9046a868"></a>

### [`0049fc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md) → [`0049fc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md) FUN_0049fc68

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 5件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fd2c",
      "incomplete_value": true,
      "site": "0049fd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fcec",
      "incomplete_value": true,
      "site": "0049fcf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
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
      "definition_site": "0049fd74",
      "incomplete_value": false,
      "site": "0049fd78",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd34",
      "incomplete_value": false,
      "site": "0049fd38",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049fd94",
      "incomplete_value": true,
      "site": "0049fd98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd54",
      "incomplete_value": true,
      "site": "0049fd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "0049fd2c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0049fd78",
      "DATA",
      [
        "storage",
        "002b38fd",
        null,
        "string"
      ]
    ],
    [
      "0049fd94",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fd2c",
      "READ",
      [
        "storage",
        "002c24d0",
        null,
        null
      ]
    ],
    [
      "0049fd78",
      "DATA",
      [
        "storage",
        "002b393d",
        null,
        "string"
      ]
    ],
    [
      "0049fd94",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fd58) · [`0049fc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fc58) · [`0049fcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md#insn-0049fcb0)
- 新版 `0049fd98`（命令位置の公開資料なし） · `0049fc98`（命令位置の公開資料なし） · `0049fcf0`（命令位置の公開資料なし）

~~~diff
- 0049fd58 ["INT_ADD", "register:40f0:8", ["const:49fd58:8", "const:4:8"]]
- 0049fd58 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049fd98 ["INT_ADD", "register:40f0:8", ["const:49fd98:8", "const:4:8"]]
+ 0049fd98 ["CALL", null, ["callee:00c57f10:8"]]
- 0049fd58 bytes 6edf1e94
+ 0049fd98 bytes 5ee01e94
- 0049fc58 ["INT_ADD", "register:40f0:8", ["const:49fc58:8", "const:4:8"]]
- 0049fc58 ["CALL", null, ["callee:0049b3c8:8"]]
+ 0049fc98 ["INT_ADD", "register:40f0:8", ["const:49fc98:8", "const:4:8"]]
+ 0049fc98 ["CALL", null, ["callee:0049b3c8:8"]]
- 0049fc58 bytes ccedff97
+ 0049fc98 bytes ccedff97
- 0049fcb0 ["INT_ADD", "register:40f0:8", ["const:49fcb0:8", "const:4:8"]]
- 0049fcb0 ["CALL", null, ["callee:0049b4a0:8"]]
+ 0049fcf0 ["INT_ADD", "register:40f0:8", ["const:49fcf0:8", "const:4:8"]]
+ 0049fcf0 ["CALL", null, ["callee:0049b4a0:8"]]
- 0049fcb0 bytes ecedff97
+ 0049fcf0 bytes ecedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b9a685ac0e3f806e168f5e49f96d07"></a>

### [`0049fd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md) → [`0049fdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md) FUN_0049fdd0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049ff10.md) · 呼出先 6件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 6件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fea8",
      "incomplete_value": true,
      "site": "0049feb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fe68",
      "incomplete_value": true,
      "site": "0049fe74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fef4",
      "incomplete_value": false,
      "site": "0049fef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bdc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049feb4",
      "incomplete_value": false,
      "site": "0049feb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b9c:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049fe3c",
      "incomplete_value": true,
      "site": "0049fe44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fdfc",
      "incomplete_value": true,
      "site": "0049fe04",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "0049fe3c",
      "READ",
      [
        "storage",
        "00ca3390",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe3c",
      "PARAM",
      [
        "storage",
        "002bc3d4",
        null,
        "string"
      ]
    ],
    [
      "0049fe4c",
      "READ",
      [
        "storage",
        "00ca3390",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fe3c",
      "READ",
      [
        "storage",
        "00ca3790",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe3c",
      "PARAM",
      [
        "storage",
        "002bc414",
        null,
        "string"
      ]
    ],
    [
      "0049fe4c",
      "READ",
      [
        "storage",
        "00ca3790",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fdc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049fdc4) · [`0049fe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049fe04) · [`0049feb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md#insn-0049feb4)
- 新版 `0049fe04`（命令位置の公開資料なし） · `0049fe44`（命令位置の公開資料なし） · `0049fef4`（命令位置の公開資料なし）

~~~diff
- 0049fdc4 ["INT_ADD", "register:40f0:8", ["const:49fdc4:8", "const:4:8"]]
- 0049fdc4 ["CALL", null, ["callee:0049b3c8:8"]]
+ 0049fe04 ["INT_ADD", "register:40f0:8", ["const:49fe04:8", "const:4:8"]]
+ 0049fe04 ["CALL", null, ["callee:0049b3c8:8"]]
- 0049fdc4 bytes 71edff97
+ 0049fe04 bytes 71edff97
- 0049fe04 ["INT_ADD", "register:40f0:8", ["const:49fe04:8", "const:4:8"]]
- 0049fe04 ["CALL", null, ["callee:00c58630:8"]]
+ 0049fe44 ["INT_ADD", "register:40f0:8", ["const:49fe44:8", "const:4:8"]]
+ 0049fe44 ["CALL", null, ["callee:00c58630:8"]]
- 0049fe04 bytes 0be11e94
+ 0049fe44 bytes fbe11e94
- 0049feb4 ["COPY", "tmp:0:8", ["const:b9c:8"]]
- 0049feb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049feb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049feb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049fef4 ["COPY", "tmp:0:8", ["const:bdc:8"]]
+ 0049fef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049feb4 bytes 08712e91
+ 0049fef4 bytes 08712f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3141b2414270d425e749d1a8cf99b692"></a>

### [`004a0238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md) → [`004a0278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md) FUN_004a0278

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a0334",
      "incomplete_value": false,
      "site": "004a033c",
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
            "const:97d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a02f4",
      "incomplete_value": false,
      "site": "004a02fc",
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
            "const:93d:8"
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
      "definition_site": "004a0344",
      "incomplete_value": true,
      "site": "004a0348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0304",
      "incomplete_value": true,
      "site": "004a0308",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "004a033c",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "004a0344",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "004a0344",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a033c",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "004a0344",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "004a0344",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a0308) · [`004a02ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a02ec) · [`004a02f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0238.md#insn-004a02f4)
- 新版 `004a0348`（命令位置の公開資料なし） · `004a032c`（命令位置の公開資料なし） · `004a0334`（命令位置の公開資料なし）

~~~diff
- 004a0308 ["INT_ADD", "register:40f0:8", ["const:4a0308:8", "const:4:8"]]
- 004a0308 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a0348 ["INT_ADD", "register:40f0:8", ["const:4a0348:8", "const:4:8"]]
+ 004a0348 ["CALL", null, ["callee:00c57f10:8"]]
- 004a0308 bytes 02de1e94
+ 004a0348 bytes f2de1e94
- 004a02ec ["INT_ADD", "register:40f0:8", ["const:4a02ec:8", "const:4:8"]]
- 004a02ec ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a032c ["INT_ADD", "register:40f0:8", ["const:4a032c:8", "const:4:8"]]
+ 004a032c ["CALL", null, ["callee:00c57ef0:8"]]
- 004a02ec bytes 01de1e94
+ 004a032c bytes f1de1e94
- 004a02f4 ["COPY", "tmp:0:8", ["const:93d:8"]]
- 004a02f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004a02f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004a02f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004a0334 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 004a0334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004a02f4 bytes 08f52491
+ 004a0334 bytes 08f52591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0922face2bffb408bf5bf88e31d15e9"></a>

### [`004a04a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md) → [`004a04e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md) FUN_004a04e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0328.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`004a0368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "004a04f4",
      "incomplete_value": false,
      "site": "004a04f8",
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
      "definition_site": "004a04b4",
      "incomplete_value": false,
      "site": "004a04b8",
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
      "004a04f4",
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
      "004a04f4",
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

- 旧版 [`004a04b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md#insn-004a04b8) · [`004a04b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a04a8.md#insn-004a04b4)
- 新版 `004a04f8`（命令位置の公開資料なし） · `004a04f4`（命令位置の公開資料なし）

~~~diff
- 004a04b8 ["INT_ADD", "register:40f0:8", ["const:4a04b8:8", "const:4:8"]]
- 004a04b8 ["CALL", null, ["callee:0043b778:8"]]
+ 004a04f8 ["INT_ADD", "register:40f0:8", ["const:4a04f8:8", "const:4:8"]]
+ 004a04f8 ["CALL", null, ["callee:0043b778:8"]]
- 004a04b8 bytes a06cfe97
+ 004a04f8 bytes a06cfe97
- 004a04b4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 004a04b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a04b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a04b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a04f4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 004a04f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a04f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a04f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a04b4 bytes 00303c91
+ 004a04f4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b790395607472a0ab004b67a76cb403"></a>

### [`004a0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md) → [`004a0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) _ZNK5Botan7AES_1289encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0628",
      "incomplete_value": true,
      "site": "004a0634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a05e8",
      "incomplete_value": true,
      "site": "004a05f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a0624",
      "incomplete_value": false,
      "site": "004a0634",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a05e4",
      "incomplete_value": false,
      "site": "004a05f4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a0624",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a0628",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a0628",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a0624",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a0628",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a0628",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a05b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a05b4) · [`004a05f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a05f4) · [`004a059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md#insn-004a059c)
- 新版 `004a05f4`（命令位置の公開資料なし） · `004a0634`（命令位置の公開資料なし） · `004a05dc`（命令位置の公開資料なし）

~~~diff
- 004a05b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a05b4 ["INT_ADD", "register:40f0:8", ["const:4a05b4:8", "const:4:8"]]
- 004a05b4 ["CALLIND", null, ["register:0:8"]]
+ 004a05f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a05f4 ["INT_ADD", "register:40f0:8", ["const:4a05f4:8", "const:4:8"]]
+ 004a05f4 ["CALLIND", null, ["register:0:8"]]
- 004a05b4 bytes 20013fd6
+ 004a05f4 bytes 20013fd6
- 004a05f4 ["INT_ADD", "register:40f0:8", ["const:4a05f4:8", "const:4:8"]]
- 004a05f4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a0634 ["INT_ADD", "register:40f0:8", ["const:4a0634:8", "const:4:8"]]
+ 004a0634 ["CALL", null, ["callee:00c57f10:8"]]
- 004a05f4 bytes 47dd1e94
+ 004a0634 bytes 37de1e94
- 004a059c ["INT_ADD", "register:40f0:8", ["const:4a059c:8", "const:4:8"]]
- 004a059c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a05dc ["INT_ADD", "register:40f0:8", ["const:4a05dc:8", "const:4:8"]]
+ 004a05dc ["CALL", null, ["callee:00c57ef0:8"]]
- 004a059c bytes 55dd1e94
+ 004a05dc bytes 45de1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-812fb6d5a1a400d8574362be245933e5"></a>

### [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) → [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) FUN_004a0688

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0528.md) [`004a1b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md) [`004a1e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md) · 呼出先 4件 [`005358fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005358fc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 3件 [`004a0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) [`004a1b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) [`004a1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) · 呼出先 4件 [`0053593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/0053593c.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a06c8",
      "incomplete_value": true,
      "site": "004a06c8",
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
      "definition_site": "004a0688",
      "incomplete_value": true,
      "site": "004a0688",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0bd4",
      "incomplete_value": false,
      "site": "004a0bf4",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0b94",
      "incomplete_value": false,
      "site": "004a0bb4",
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
            "const:560:8"
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
      "definition_site": "004a0bdc",
      "incomplete_value": false,
      "site": "004a0bf4",
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
            "const:237:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0b9c",
      "incomplete_value": false,
      "site": "004a0bb4",
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
            "const:16a:8"
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
      "004a06c0",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004a06c4",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a06d0",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a06c0",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004a06c4",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a06d0",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0ba8) · [`004a0bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0bb4) · [`004a0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md#insn-004a0bd0)
- 新版 `004a0be8`（命令位置の公開資料なし） · `004a0bf4`（命令位置の公開資料なし） · `004a0c10`（命令位置の公開資料なし）

~~~diff
- 004a0ba8 ["COPY", "register:4018:8", ["const:2ab000:8"]]
+ 004a0be8 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 004a0ba8 bytes 43f0fff0
+ 004a0be8 bytes e3efffd0
- 004a0bb4 ["INT_ADD", "register:40f0:8", ["const:4a0bb4:8", "const:4:8"]]
- 004a0bb4 ["CALL", null, ["callee:00c58650:8"]]
+ 004a0bf4 ["INT_ADD", "register:40f0:8", ["const:4a0bf4:8", "const:4:8"]]
+ 004a0bf4 ["CALL", null, ["callee:00c58650:8"]]
- 004a0bb4 bytes a7dd1e94
+ 004a0bf4 bytes 97de1e94
- 004a0bd0 ["INT_ADD", "register:40f0:8", ["const:4a0bd0:8", "const:4:8"]]
- 004a0bd0 ["CALL", null, ["callee:00c57e50:8"]]
+ 004a0c10 ["INT_ADD", "register:40f0:8", ["const:4a0c10:8", "const:4:8"]]
+ 004a0c10 ["CALL", null, ["callee:00c57e50:8"]]
- 004a0bd0 bytes a0db1e94
+ 004a0c10 bytes 90dc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e45ae406bcb31deb1b9232cceccea1a8"></a>

### [`004a0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md) → [`004a0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) _ZNK5Botan7AES_1289decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0d08",
      "incomplete_value": true,
      "site": "004a0d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0cc8",
      "incomplete_value": true,
      "site": "004a0cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a0d04",
      "incomplete_value": false,
      "site": "004a0d14",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a0cc4",
      "incomplete_value": false,
      "site": "004a0cd4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a0d04",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a0d08",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d08",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a0d04",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a0d08",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d08",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0c94) · [`004a0cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0cd4) · [`004a0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md#insn-004a0c7c)
- 新版 `004a0cd4`（命令位置の公開資料なし） · `004a0d14`（命令位置の公開資料なし） · `004a0cbc`（命令位置の公開資料なし）

~~~diff
- 004a0c94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a0c94 ["INT_ADD", "register:40f0:8", ["const:4a0c94:8", "const:4:8"]]
- 004a0c94 ["CALLIND", null, ["register:0:8"]]
+ 004a0cd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a0cd4 ["INT_ADD", "register:40f0:8", ["const:4a0cd4:8", "const:4:8"]]
+ 004a0cd4 ["CALLIND", null, ["register:0:8"]]
- 004a0c94 bytes 20013fd6
+ 004a0cd4 bytes 20013fd6
- 004a0cd4 ["INT_ADD", "register:40f0:8", ["const:4a0cd4:8", "const:4:8"]]
- 004a0cd4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a0d14 ["INT_ADD", "register:40f0:8", ["const:4a0d14:8", "const:4:8"]]
+ 004a0d14 ["CALL", null, ["callee:00c57f10:8"]]
- 004a0cd4 bytes 8fdb1e94
+ 004a0d14 bytes 7fdc1e94
- 004a0c7c ["INT_ADD", "register:40f0:8", ["const:4a0c7c:8", "const:4:8"]]
- 004a0c7c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a0cbc ["INT_ADD", "register:40f0:8", ["const:4a0cbc:8", "const:4:8"]]
+ 004a0cbc ["CALL", null, ["callee:00c57ef0:8"]]
- 004a0c7c bytes 9ddb1e94
+ 004a0cbc bytes 8ddc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b77a0d699b3341f3aa9a6c7de4e021cf"></a>

### [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) → [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) FUN_004a0d68

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004a0c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0c08.md) [`004a1c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md) [`004a1f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md) · 呼出先 4件 [`005359f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005359f4.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 3件 [`004a0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) [`004a1c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) [`004a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) · 呼出先 4件 [`00535a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a0da8",
      "incomplete_value": true,
      "site": "004a0da8",
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
      "definition_site": "004a0d68",
      "incomplete_value": true,
      "site": "004a0d68",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a12c0",
      "incomplete_value": false,
      "site": "004a12e0",
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
            "const:23f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1280",
      "incomplete_value": false,
      "site": "004a12a0",
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
            "const:172:8"
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
      "definition_site": "004a12c8",
      "incomplete_value": false,
      "site": "004a12e0",
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
            "const:237:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1288",
      "incomplete_value": false,
      "site": "004a12a0",
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
            "const:16a:8"
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
      "004a0da0",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004a0da4",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0db0",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a0da0",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004a0da4",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0db0",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a1294) · [`004a12a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a12a0) · [`004a12bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md#insn-004a12bc)
- 新版 `004a12d4`（命令位置の公開資料なし） · `004a12e0`（命令位置の公開資料なし） · `004a12fc`（命令位置の公開資料なし）

~~~diff
- 004a1294 ["COPY", "register:4018:8", ["const:2ab000:8"]]
+ 004a12d4 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 004a1294 bytes 43f0ffd0
+ 004a12d4 bytes e3efffb0
- 004a12a0 ["INT_ADD", "register:40f0:8", ["const:4a12a0:8", "const:4:8"]]
- 004a12a0 ["CALL", null, ["callee:00c58650:8"]]
+ 004a12e0 ["INT_ADD", "register:40f0:8", ["const:4a12e0:8", "const:4:8"]]
+ 004a12e0 ["CALL", null, ["callee:00c58650:8"]]
- 004a12a0 bytes ecdb1e94
+ 004a12e0 bytes dcdc1e94
- 004a12bc ["INT_ADD", "register:40f0:8", ["const:4a12bc:8", "const:4:8"]]
- 004a12bc ["CALL", null, ["callee:00c57e50:8"]]
+ 004a12fc ["INT_ADD", "register:40f0:8", ["const:4a12fc:8", "const:4:8"]]
+ 004a12fc ["CALL", null, ["callee:00c57e50:8"]]
- 004a12bc bytes e5d91e94
+ 004a12fc bytes d5da1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639198f31343e6491491264fa4d97b86"></a>

### [`004a1314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md) → [`004a1354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md) FUN_004a1354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a12f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a12f4.md) [`004a1d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1d70.md) [`004a208c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a208c.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005359f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/005359f4.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)
- 新版 呼出元 3件 [`004a1334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1334.md) [`004a1db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1db0.md) [`004a20cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20cc.md) · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a174c",
      "value": [
        "leaf",
        "ram:535a34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a170c",
      "value": [
        "leaf",
        "ram:5359f4:8"
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
      "site": "004a1768",
      "value": [
        "leaf",
        "ram:535a34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1728",
      "value": [
        "leaf",
        "ram:5359f4:8"
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
      "site": "004a1784",
      "value": [
        "leaf",
        "ram:535a34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1744",
      "value": [
        "leaf",
        "ram:5359f4:8"
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
      "004a14c8",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ],
    [
      "004a14cc",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ],
    [
      "004a14d0",
      "DATA",
      [
        "storage",
        "002cf300",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a14c8",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      "004a14cc",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      "004a14d0",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a1704) · [`004a170c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a170c) · [`004a1720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md#insn-004a1720)
- 新版 `004a1744`（命令位置の公開資料なし） · `004a174c`（命令位置の公開資料なし） · `004a1760`（命令位置の公開資料なし）

~~~diff
- 004a1704 ["INT_ADD", "register:40f0:8", ["const:4a1704:8", "const:4:8"]]
- 004a1704 ["CALL", null, ["callee:00c57e50:8"]]
+ 004a1744 ["INT_ADD", "register:40f0:8", ["const:4a1744:8", "const:4:8"]]
+ 004a1744 ["CALL", null, ["callee:00c57e50:8"]]
- 004a1704 bytes d3d81e94
+ 004a1744 bytes c3d91e94
- 004a170c ["INT_ADD", "register:40f0:8", ["const:4a170c:8", "const:4:8"]]
- 004a170c ["CALL", null, ["ram:5359f4:8"]]
+ 004a174c ["INT_ADD", "register:40f0:8", ["const:4a174c:8", "const:4:8"]]
+ 004a174c ["CALL", null, ["ram:535a34:8"]]
- 004a170c bytes ba500294
+ 004a174c bytes ba500294
- 004a1720 ["INT_ADD", "register:40f0:8", ["const:4a1720:8", "const:4:8"]]
- 004a1720 ["CALL", null, ["callee:00c57e50:8"]]
+ 004a1760 ["INT_ADD", "register:40f0:8", ["const:4a1760:8", "const:4:8"]]
+ 004a1760 ["CALL", null, ["callee:00c57e50:8"]]
- 004a1720 bytes ccd81e94
+ 004a1760 bytes bcd91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8553925a5e5f7500961e68ffed7e53"></a>

### [`004a1b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md) → [`004a1b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) _ZNK5Botan7AES_1929encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1c30",
      "incomplete_value": true,
      "site": "004a1c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1bf0",
      "incomplete_value": true,
      "site": "004a1bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a1c2c",
      "incomplete_value": false,
      "site": "004a1c3c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a1bec",
      "incomplete_value": false,
      "site": "004a1bfc",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a1c2c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1c30",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c30",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1c2c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1c30",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c30",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1bbc) · [`004a1bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1bfc) · [`004a1ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1b30.md#insn-004a1ba4)
- 新版 `004a1bfc`（命令位置の公開資料なし） · `004a1c3c`（命令位置の公開資料なし） · `004a1be4`（命令位置の公開資料なし）

~~~diff
- 004a1bbc ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1bbc ["INT_ADD", "register:40f0:8", ["const:4a1bbc:8", "const:4:8"]]
- 004a1bbc ["CALLIND", null, ["register:0:8"]]
+ 004a1bfc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1bfc ["INT_ADD", "register:40f0:8", ["const:4a1bfc:8", "const:4:8"]]
+ 004a1bfc ["CALLIND", null, ["register:0:8"]]
- 004a1bbc bytes 20013fd6
+ 004a1bfc bytes 20013fd6
- 004a1bfc ["INT_ADD", "register:40f0:8", ["const:4a1bfc:8", "const:4:8"]]
- 004a1bfc ["CALL", null, ["callee:00c57f10:8"]]
+ 004a1c3c ["INT_ADD", "register:40f0:8", ["const:4a1c3c:8", "const:4:8"]]
+ 004a1c3c ["CALL", null, ["callee:00c57f10:8"]]
- 004a1bfc bytes c5d71e94
+ 004a1c3c bytes b5d81e94
- 004a1ba4 ["INT_ADD", "register:40f0:8", ["const:4a1ba4:8", "const:4:8"]]
- 004a1ba4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a1be4 ["INT_ADD", "register:40f0:8", ["const:4a1be4:8", "const:4:8"]]
+ 004a1be4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004a1ba4 bytes d3d71e94
+ 004a1be4 bytes c3d81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ee0f851f2cbed4ae0ec1274caa7318"></a>

### [`004a1c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md) → [`004a1c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) _ZNK5Botan7AES_1929decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1d50",
      "incomplete_value": true,
      "site": "004a1d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1d10",
      "incomplete_value": true,
      "site": "004a1d1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a1d4c",
      "incomplete_value": false,
      "site": "004a1d5c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a1d0c",
      "incomplete_value": false,
      "site": "004a1d1c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a1d4c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1d50",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a1d50",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1d4c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1d50",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1d50",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1cdc) · [`004a1d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1d1c) · [`004a1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1c50.md#insn-004a1cc4)
- 新版 `004a1d1c`（命令位置の公開資料なし） · `004a1d5c`（命令位置の公開資料なし） · `004a1d04`（命令位置の公開資料なし）

~~~diff
- 004a1cdc ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1cdc ["INT_ADD", "register:40f0:8", ["const:4a1cdc:8", "const:4:8"]]
- 004a1cdc ["CALLIND", null, ["register:0:8"]]
+ 004a1d1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1d1c ["INT_ADD", "register:40f0:8", ["const:4a1d1c:8", "const:4:8"]]
+ 004a1d1c ["CALLIND", null, ["register:0:8"]]
- 004a1cdc bytes 20013fd6
+ 004a1d1c bytes 20013fd6
- 004a1d1c ["INT_ADD", "register:40f0:8", ["const:4a1d1c:8", "const:4:8"]]
- 004a1d1c ["CALL", null, ["callee:00c57f10:8"]]
+ 004a1d5c ["INT_ADD", "register:40f0:8", ["const:4a1d5c:8", "const:4:8"]]
+ 004a1d5c ["CALL", null, ["callee:00c57f10:8"]]
- 004a1d1c bytes 7dd71e94
+ 004a1d5c bytes 6dd81e94
- 004a1cc4 ["INT_ADD", "register:40f0:8", ["const:4a1cc4:8", "const:4:8"]]
- 004a1cc4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a1d04 ["INT_ADD", "register:40f0:8", ["const:4a1d04:8", "const:4:8"]]
+ 004a1d04 ["CALL", null, ["callee:00c57ef0:8"]]
- 004a1cc4 bytes 8bd71e94
+ 004a1d04 bytes 7bd81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cc9c8df7d5ae5288948fee4bc32a6c6"></a>

### [`004a1e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md) → [`004a1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) _ZNK5Botan7AES_2569encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0648.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1f4c",
      "incomplete_value": true,
      "site": "004a1f58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1f0c",
      "incomplete_value": true,
      "site": "004a1f18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a1f48",
      "incomplete_value": false,
      "site": "004a1f58",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a1f08",
      "incomplete_value": false,
      "site": "004a1f18",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a1f48",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a1f4c",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a1f4c",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1f48",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1f4c",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1f4c",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1ed8) · [`004a1f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1f18) · [`004a1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1e4c.md#insn-004a1ec0)
- 新版 `004a1f18`（命令位置の公開資料なし） · `004a1f58`（命令位置の公開資料なし） · `004a1f00`（命令位置の公開資料なし）

~~~diff
- 004a1ed8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1ed8 ["INT_ADD", "register:40f0:8", ["const:4a1ed8:8", "const:4:8"]]
- 004a1ed8 ["CALLIND", null, ["register:0:8"]]
+ 004a1f18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1f18 ["INT_ADD", "register:40f0:8", ["const:4a1f18:8", "const:4:8"]]
+ 004a1f18 ["CALLIND", null, ["register:0:8"]]
- 004a1ed8 bytes 20013fd6
+ 004a1f18 bytes 20013fd6
- 004a1f18 ["INT_ADD", "register:40f0:8", ["const:4a1f18:8", "const:4:8"]]
- 004a1f18 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a1f58 ["INT_ADD", "register:40f0:8", ["const:4a1f58:8", "const:4:8"]]
+ 004a1f58 ["CALL", null, ["callee:00c57f10:8"]]
- 004a1f18 bytes fed61e94
+ 004a1f58 bytes eed71e94
- 004a1ec0 ["INT_ADD", "register:40f0:8", ["const:4a1ec0:8", "const:4:8"]]
- 004a1ec0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a1f00 ["INT_ADD", "register:40f0:8", ["const:4a1f00:8", "const:4:8"]]
+ 004a1f00 ["CALL", null, ["callee:00c57ef0:8"]]
- 004a1ec0 bytes 0cd71e94
+ 004a1f00 bytes fcd71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d02890794fbb837c8c3d21483524a8e"></a>

### [`004a1f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md) → [`004a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) _ZNK5Botan7AES_2569decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a0/004a0d28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a206c",
      "incomplete_value": true,
      "site": "004a2078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a202c",
      "incomplete_value": true,
      "site": "004a2038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "definition_site": "004a2068",
      "incomplete_value": false,
      "site": "004a2078",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a2028",
      "incomplete_value": false,
      "site": "004a2038",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a2068",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a206c",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004a206c",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a2068",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a206c",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a206c",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a1ff8) · [`004a2038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a2038) · [`004a1fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1f6c.md#insn-004a1fe0)
- 新版 `004a2038`（命令位置の公開資料なし） · `004a2078`（命令位置の公開資料なし） · `004a2020`（命令位置の公開資料なし）

~~~diff
- 004a1ff8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1ff8 ["INT_ADD", "register:40f0:8", ["const:4a1ff8:8", "const:4:8"]]
- 004a1ff8 ["CALLIND", null, ["register:0:8"]]
+ 004a2038 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a2038 ["INT_ADD", "register:40f0:8", ["const:4a2038:8", "const:4:8"]]
+ 004a2038 ["CALLIND", null, ["register:0:8"]]
- 004a1ff8 bytes 20013fd6
+ 004a2038 bytes 20013fd6
- 004a2038 ["INT_ADD", "register:40f0:8", ["const:4a2038:8", "const:4:8"]]
- 004a2038 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a2078 ["INT_ADD", "register:40f0:8", ["const:4a2078:8", "const:4:8"]]
+ 004a2078 ["CALL", null, ["callee:00c57f10:8"]]
- 004a2038 bytes b6d61e94
+ 004a2078 bytes a6d71e94
- 004a1fe0 ["INT_ADD", "register:40f0:8", ["const:4a1fe0:8", "const:4:8"]]
- 004a1fe0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a2020 ["INT_ADD", "register:40f0:8", ["const:4a2020:8", "const:4:8"]]
+ 004a2020 ["CALL", null, ["callee:00c57ef0:8"]]
- 004a1fe0 bytes c4d61e94
+ 004a2020 bytes b4d71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17722e31241d91f4b27e21314b238cf1"></a>

### [`004a2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md) → [`004a21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) _ZN5Botan19AlgorithmIdentifierC1ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59040.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c59440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59440.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a21f0",
      "incomplete_value": true,
      "site": "004a21f0",
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
      "definition_site": "004a21b0",
      "incomplete_value": true,
      "site": "004a21b0",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a21f0",
      "incomplete_value": true,
      "site": "004a21f0",
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
      "definition_site": "004a21b0",
      "incomplete_value": true,
      "site": "004a21b0",
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
      "004a21d0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a21dc",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a21f0",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a21d0",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a21dc",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a21f0",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a2190) · [`004a2198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a2198) · [`004a219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2168.md#insn-004a219c)
- 新版 `004a21d0`（命令位置の公開資料なし） · `004a21dc`（命令位置の公開資料なし）

~~~diff
- 004a2190 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 004a2190 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a21d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a21d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2190 bytes 089d44f9
+ 004a21d0 bytes 089d46f9
- 004a2198 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a2198 bytes f30300aa
- 004a219c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 004a219c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a21dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a21dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a219c bytes 29a144f9
+ 004a21dc bytes 29a146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f224090e6e6bb23a74400a63a2259bf8"></a>

### [`004a22a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md) → [`004a22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a20.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 1件 [`00c58e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e20.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2310",
      "incomplete_value": true,
      "site": "004a2310",
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
      "definition_site": "004a22d0",
      "incomplete_value": true,
      "site": "004a22d0",
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
      "004a2300",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a2310",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a2300",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a2310",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md#insn-004a2310) · [`004a22c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md#insn-004a22c0) · [`004a22c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a22a4.md#insn-004a22c8)
- 新版 `004a2350`（命令位置の公開資料なし） · `004a2300`（命令位置の公開資料なし）

~~~diff
- 004a2310 ["INT_ADD", "register:40f0:8", ["const:4a2310:8", "const:4:8"]]
- 004a2310 ["CALL", null, ["callee:00c58000:8"]]
+ 004a2350 ["INT_ADD", "register:40f0:8", ["const:4a2350:8", "const:4:8"]]
+ 004a2350 ["CALL", null, ["callee:00c58000:8"]]
- 004a2310 bytes 3cd61e94
+ 004a2350 bytes 2cd71e94
- 004a22c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 004a22c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a2300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a22c0 bytes 089d44f9
+ 004a2300 bytes 089d46f9
- 004a22c8 ["COPY", "register:4040:8", ["register:4000:8"]]
- 004a22c8 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-095ea6d56e3bf75deab97224f0f7b653"></a>

### [`004a2370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2370.md) → [`004a23b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md) _ZN5Botan4OIDS6lookupERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 24.80% / 新版 24.80%

CFGの説明率　旧版 22.26% / 新版 22.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 75件, `store_value` 12件, `unresolved_branch_alignment` 130件, `unresolved_call_alignment` 436件

アドレスに依存する影響 `call_argument_candidate` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a256c",
      "incomplete_value": true,
      "site": "004a257c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ccb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a252c",
      "incomplete_value": true,
      "site": "004a253c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c8b:8"
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
      "definition_site": "004a2580",
      "incomplete_value": true,
      "site": "004a2580",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a2540",
      "incomplete_value": true,
      "site": "004a2540",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a25d4",
      "incomplete_value": true,
      "site": "004a25e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:142:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2594",
      "incomplete_value": true,
      "site": "004a25a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:102:8"
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
      "004a24fc",
      "PARAM",
      [
        "storage",
        "002a8aa3",
        null,
        "string"
      ]
    ],
    [
      "004a2508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:004a24ec"
      ]
    ],
    [
      "unmatched:004a24d0",
      "PARAM",
      [
        "storage",
        "002bb291",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a24fc",
      "PARAM",
      [
        "storage",
        "002a8b70",
        null,
        "string"
      ]
    ],
    [
      "004a2508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004a252c"
      ]
    ],
    [
      "004a2510",
      "PARAM",
      [
        "storage",
        "002bb2d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2370.md#insn-004a24bc) · [`004a24fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2370.md#insn-004a24fc) · [`004a2524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a2/004a2370.md#insn-004a2524)
- 新版 `004a24fc`（命令位置の公開資料なし） · `004a2564`（命令位置の公開資料なし）

~~~diff
- 004a24bc ["COPY", "tmp:0:8", ["const:aa3:8"]]
- 004a24bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a24bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a24bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a24fc ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 004a24fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a24fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a24fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a24bc bytes 218c2a91
+ 004a24fc bytes 21c02d91
- 004a24fc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004a24fc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004a24fc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004a24fc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004a24fc bytes c0020036
- 004a2524 ["COPY", "tmp:0:8", ["const:c8b:8"]]
- 004a2524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004a2524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004a2524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004a2564 ["COPY", "tmp:0:8", ["const:ccb:8"]]
+ 004a2564 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004a2564 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004a2564 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004a2524 bytes 292d3291
+ 004a2564 bytes 292d3391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47fecc6fd99f29c5b3bd471d21c1c77"></a>

### [`004a4fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md) → [`004a502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md) _ZN5Botan19AlgorithmIdentifierC2ERKNS_3OIDENS0_15Encoding_OptionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59320.md) · 呼出先 5件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md) · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5074",
      "incomplete_value": true,
      "site": "004a5074",
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
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5034",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5074",
      "incomplete_value": true,
      "site": "004a5074",
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
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5034",
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
      "004a5054",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a5060",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a5074",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5054",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a5060",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a5074",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a5014) · [`004a501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a501c) · [`004a5020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a4/004a4fec.md#insn-004a5020)
- 新版 `004a5054`（命令位置の公開資料なし） · `004a5060`（命令位置の公開資料なし）

~~~diff
- 004a5014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 004a5014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a5054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5014 bytes 089d44f9
+ 004a5054 bytes 089d46f9
- 004a501c ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a501c bytes f30300aa
- 004a5020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 004a5020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a5060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5020 bytes 29a144f9
+ 004a5060 bytes 29a146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0469b593718d7b74bbfc32c36972874"></a>

### [`004a50d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md) → [`004a5118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md) _ZN5Botan19AlgorithmIdentifierC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a10.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 1件 [`00c58e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e10.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5134",
      "incomplete_value": true,
      "site": "004a5138",
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
      "definition_site": "004a50f4",
      "incomplete_value": true,
      "site": "004a50f8",
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
      "004a5130",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004a5138",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5130",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a5138",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a50f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a50f0) · [`004a5104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a5104) · [`004a5118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a50d8.md#insn-004a5118)
- 新版 `004a5130`（命令位置の公開資料なし） · `004a5144`（命令位置の公開資料なし） · `004a5158`（命令位置の公開資料なし）

~~~diff
- 004a50f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 004a50f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a5130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a50f0 bytes 089d44f9
+ 004a5130 bytes 089d46f9
- 004a5104 ["INT_ADD", "register:40f0:8", ["const:4a5104:8", "const:4:8"]]
- 004a5104 ["CALL", null, ["callee:00c58680:8"]]
+ 004a5144 ["INT_ADD", "register:40f0:8", ["const:4a5144:8", "const:4:8"]]
+ 004a5144 ["CALL", null, ["callee:00c58680:8"]]
- 004a5104 bytes 5fcc1e94
+ 004a5144 bytes 4fcd1e94
- 004a5118 ["INT_ADD", "register:40f0:8", ["const:4a5118:8", "const:4:8"]]
- 004a5118 ["CALL", null, ["callee:00c57e90:8"]]
+ 004a5158 ["INT_ADD", "register:40f0:8", ["const:4a5158:8", "const:4:8"]]
+ 004a5158 ["CALL", null, ["callee:00c57e90:8"]]
- 004a5118 bytes 5eca1e94
+ 004a5158 bytes 4ecb1e94
~~~


<a id="compare-a6f8673476ae56d2530017a8279eacac"></a>

### [`004a5398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md) → [`004a53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md) _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md) · 呼出先 6件 [`00542f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582e0.md)
- 新版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) · 呼出先 6件 [`00542f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542f88.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c586e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a54c0",
      "incomplete_value": true,
      "site": "004a54c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5480",
      "incomplete_value": true,
      "site": "004a5480",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a5500",
      "incomplete_value": true,
      "site": "004a5500",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a54c0",
      "incomplete_value": true,
      "site": "004a54c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
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
      "004a54b0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a54f0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a54b0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a54f0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a5480) · [`004a54c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a54c0) · [`004a53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md#insn-004a53c4)
- 新版 `004a54c0`（命令位置の公開資料なし） · `004a5500`（命令位置の公開資料なし） · `004a5404`（命令位置の公開資料なし）

~~~diff
- 004a5480 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a5480 ["INT_ADD", "register:40f0:8", ["const:4a5480:8", "const:4:8"]]
- 004a5480 ["CALLIND", null, ["register:0:8"]]
+ 004a54c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a54c0 ["INT_ADD", "register:40f0:8", ["const:4a54c0:8", "const:4:8"]]
+ 004a54c0 ["CALLIND", null, ["register:0:8"]]
- 004a5480 bytes 20013fd6
+ 004a54c0 bytes 20013fd6
- 004a54c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a54c0 ["INT_ADD", "register:40f0:8", ["const:4a54c0:8", "const:4:8"]]
- 004a54c0 ["CALLIND", null, ["register:0:8"]]
+ 004a5500 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a5500 ["INT_ADD", "register:40f0:8", ["const:4a5500:8", "const:4:8"]]
+ 004a5500 ["CALLIND", null, ["register:0:8"]]
- 004a54c0 bytes 20013fd6
+ 004a5500 bytes 20013fd6
- 004a53c4 ["INT_ADD", "register:40f0:8", ["const:4a53c4:8", "const:4:8"]]
- 004a53c4 ["CALL", null, ["callee:00c586e0:8"]]
+ 004a5404 ["INT_ADD", "register:40f0:8", ["const:4a5404:8", "const:4:8"]]
+ 004a5404 ["CALL", null, ["callee:00c586e0:8"]]
- 004a53c4 bytes c7cb1e94
+ 004a5404 bytes b7cc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc89c06673908bfd3aec08b574f4b51b"></a>

### [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) → [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) _ZN5Botan11DER_Encoder8end_consEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c582d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582d0.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)
- 新版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.94% / 新版 97.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a568c",
      "incomplete_value": true,
      "site": "004a568c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a564c",
      "incomplete_value": true,
      "site": "004a564c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a56d4",
      "incomplete_value": false,
      "site": "004a56dc",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5694",
      "incomplete_value": false,
      "site": "004a569c",
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
            "const:e98:8"
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
      "definition_site": "004a570c",
      "incomplete_value": true,
      "site": "004a5718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a56cc",
      "incomplete_value": true,
      "site": "004a56d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "004a567c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a56d4",
      "PARAM",
      [
        "storage",
        "002b5e98",
        null,
        "string"
      ]
    ],
    [
      "004a5708",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a567c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a56d4",
      "PARAM",
      [
        "storage",
        "002b5ed8",
        null,
        "string"
      ]
    ],
    [
      "004a5708",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a564c) · [`004a569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a569c) · [`004a56d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md#insn-004a56d8)
- 新版 `004a568c`（命令位置の公開資料なし） · `004a56dc`（命令位置の公開資料なし） · `004a5718`（命令位置の公開資料なし）

~~~diff
- 004a564c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a564c ["INT_ADD", "register:40f0:8", ["const:4a564c:8", "const:4:8"]]
- 004a564c ["CALLIND", null, ["register:0:8"]]
+ 004a568c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a568c ["INT_ADD", "register:40f0:8", ["const:4a568c:8", "const:4:8"]]
+ 004a568c ["CALLIND", null, ["register:0:8"]]
- 004a564c bytes 20013fd6
+ 004a568c bytes 20013fd6
- 004a569c ["INT_ADD", "register:40f0:8", ["const:4a569c:8", "const:4:8"]]
- 004a569c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a56dc ["INT_ADD", "register:40f0:8", ["const:4a56dc:8", "const:4:8"]]
+ 004a56dc ["CALL", null, ["callee:0043ddd8:8"]]
- 004a569c bytes bf61fe97
+ 004a56dc bytes bf61fe97
- 004a56d8 ["INT_ADD", "register:40f0:8", ["const:4a56d8:8", "const:4:8"]]
- 004a56d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a5718 ["INT_ADD", "register:40f0:8", ["const:4a5718:8", "const:4:8"]]
+ 004a5718 ["CALL", null, ["callee:00c57f10:8"]]
- 004a56d8 bytes 0ec91e94
+ 004a5718 bytes fec91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15cf5aa1c1bc1f476276d718d099267c"></a>

### [`004a5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md) → [`004a5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) _ZN5Botan11BER_Decoder8end_consEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a5b5c",
      "incomplete_value": false,
      "site": "004a5b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:b72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5b1c",
      "incomplete_value": false,
      "site": "004a5b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:b32:8"
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
      "definition_site": "004a5b98",
      "incomplete_value": true,
      "site": "004a5ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5b58",
      "incomplete_value": true,
      "site": "004a5b64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "definition_site": "004a5b94",
      "incomplete_value": false,
      "site": "004a5ba4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a5b54",
      "incomplete_value": false,
      "site": "004a5b64",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a5b5c",
      "PARAM",
      [
        "storage",
        "002beb32",
        null,
        "string"
      ]
    ],
    [
      "004a5b94",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a5b98",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5b5c",
      "PARAM",
      [
        "storage",
        "002beb72",
        null,
        "string"
      ]
    ],
    [
      "004a5b94",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a5b98",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b24) · [`004a5b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b64) · [`004a5b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md#insn-004a5b88)
- 新版 `004a5b64`（命令位置の公開資料なし） · `004a5ba4`（命令位置の公開資料なし） · `004a5bc8`（命令位置の公開資料なし）

~~~diff
- 004a5b24 ["INT_ADD", "register:40f0:8", ["const:4a5b24:8", "const:4:8"]]
- 004a5b24 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a5b64 ["INT_ADD", "register:40f0:8", ["const:4a5b64:8", "const:4:8"]]
+ 004a5b64 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a5b24 bytes 9d60fe97
+ 004a5b64 bytes 9d60fe97
- 004a5b64 ["INT_ADD", "register:40f0:8", ["const:4a5b64:8", "const:4:8"]]
- 004a5b64 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a5ba4 ["INT_ADD", "register:40f0:8", ["const:4a5ba4:8", "const:4:8"]]
+ 004a5ba4 ["CALL", null, ["callee:00c57f10:8"]]
- 004a5b64 bytes ebc71e94
+ 004a5ba4 bytes dbc81e94
- 004a5b88 ["INT_ADD", "register:40f0:8", ["const:4a5b88:8", "const:4:8"]]
- 004a5b88 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a5bc8 ["INT_ADD", "register:40f0:8", ["const:4a5bc8:8", "const:4:8"]]
+ 004a5bc8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a5b88 bytes 8460fe97
+ 004a5bc8 bytes 8460fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da86ab0739d4d016cc427523f0de20e"></a>

### [`004a5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md) → [`004a5ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md) _ZN5Botan9AttributeC2ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5d14",
      "incomplete_value": true,
      "site": "004a5d14",
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
      "definition_site": "004a5cd4",
      "incomplete_value": true,
      "site": "004a5cd4",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5d14",
      "incomplete_value": true,
      "site": "004a5d14",
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
      "definition_site": "004a5cd4",
      "incomplete_value": true,
      "site": "004a5cd4",
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
      "004a5cf4",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d00",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d14",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5cf4",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d00",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d14",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5cb4) · [`004a5cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5cbc) · [`004a5cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5c8c.md#insn-004a5cc0)
- 新版 `004a5cf4`（命令位置の公開資料なし） · `004a5d00`（命令位置の公開資料なし）

~~~diff
- 004a5cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:958:8"]]
- 004a5cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 004a5cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5cb4 bytes 08ad44f9
+ 004a5cf4 bytes 08ad46f9
- 004a5cbc ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a5cbc bytes f30300aa
- 004a5cc0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:940:8"]]
- 004a5cc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5d00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a5d00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5cc0 bytes 29a144f9
+ 004a5d00 bytes 29a146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cc04196669e961f58e334192232b03f"></a>

### [`004a5db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md) → [`004a5df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md) _ZN5Botan9AttributeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b60.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 1件 [`00c59f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f60.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5e1c",
      "incomplete_value": true,
      "site": "004a5e1c",
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
      "definition_site": "004a5ddc",
      "incomplete_value": true,
      "site": "004a5ddc",
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
      "004a5e0c",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ],
    [
      "004a5e1c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5e0c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a5e1c",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md#insn-004a5e1c) · [`004a5dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md#insn-004a5dcc) · [`004a5dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5db0.md#insn-004a5dd4)
- 新版 `004a5e5c`（命令位置の公開資料なし） · `004a5e0c`（命令位置の公開資料なし）

~~~diff
- 004a5e1c ["INT_ADD", "register:40f0:8", ["const:4a5e1c:8", "const:4:8"]]
- 004a5e1c ["CALL", null, ["callee:00c58000:8"]]
+ 004a5e5c ["INT_ADD", "register:40f0:8", ["const:4a5e5c:8", "const:4:8"]]
+ 004a5e5c ["CALL", null, ["callee:00c58000:8"]]
- 004a5e1c bytes 79c71e94
+ 004a5e5c bytes 69c81e94
- 004a5dcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:958:8"]]
- 004a5dcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5e0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 004a5e0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5dcc bytes 08ad44f9
+ 004a5e0c bytes 08ad46f9
- 004a5dd4 ["COPY", "register:4040:8", ["register:4000:8"]]
- 004a5dd4 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2486a5fe64efea7a30b632cd508600e6"></a>

### [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) → [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) _ZN5Botan9Attribute11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) · 呼出先 6件 [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md)
- 新版 呼出元 1件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) · 呼出先 6件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6050",
      "incomplete_value": true,
      "site": "004a6050",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6010",
      "incomplete_value": true,
      "site": "004a6010",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6094",
      "incomplete_value": true,
      "site": "004a6094",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6054",
      "incomplete_value": true,
      "site": "004a6054",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "004a6040",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a6084",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6040",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a6084",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a5fd0) · [`004a6010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a6010) · [`004a6054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md#insn-004a6054)
- 新版 `004a6010`（命令位置の公開資料なし） · `004a6050`（命令位置の公開資料なし） · `004a6094`（命令位置の公開資料なし）

~~~diff
- 004a5fd0 ["INT_ADD", "register:40f0:8", ["const:4a5fd0:8", "const:4:8"]]
- 004a5fd0 ["CALL", null, ["callee:00c58710:8"]]
+ 004a6010 ["INT_ADD", "register:40f0:8", ["const:4a6010:8", "const:4:8"]]
+ 004a6010 ["CALL", null, ["callee:00c58710:8"]]
- 004a5fd0 bytes d0c81e94
+ 004a6010 bytes c0c91e94
- 004a6010 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6010 ["INT_ADD", "register:40f0:8", ["const:4a6010:8", "const:4:8"]]
- 004a6010 ["CALLIND", null, ["register:0:8"]]
+ 004a6050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a6050 ["INT_ADD", "register:40f0:8", ["const:4a6050:8", "const:4:8"]]
+ 004a6050 ["CALLIND", null, ["register:0:8"]]
- 004a6010 bytes 20013fd6
+ 004a6050 bytes 20013fd6
- 004a6054 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6054 ["INT_ADD", "register:40f0:8", ["const:4a6054:8", "const:4:8"]]
- 004a6054 ["CALLIND", null, ["register:0:8"]]
+ 004a6094 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a6094 ["INT_ADD", "register:40f0:8", ["const:4a6094:8", "const:4:8"]]
+ 004a6094 ["CALLIND", null, ["register:0:8"]]
- 004a6054 bytes 20013fd6
+ 004a6094 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95b3342d2a89685726b42d22b02cadb4"></a>

### [`004a60c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md) → [`004a6104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58360.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d60.md)
- 新版 呼出元 1件 [`00c58760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58760.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c58160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6220",
      "incomplete_value": true,
      "site": "004a6220",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a61e0",
      "incomplete_value": true,
      "site": "004a61e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:383:8"
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
      "definition_site": "004a62f8",
      "incomplete_value": true,
      "site": "004a62f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:964:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a62b8",
      "incomplete_value": true,
      "site": "004a62b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:924:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6240",
      "incomplete_value": false,
      "site": "004a624c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6200",
      "incomplete_value": false,
      "site": "004a620c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "004a6138",
      "DATA",
      [
        "storage",
        "002ca718",
        "switchD_004a6100::switchdataD_002ca718",
        "byte"
      ]
    ],
    [
      "004a620c",
      "READ",
      [
        "storage",
        "002a6383",
        null,
        "string"
      ]
    ],
    [
      "004a6240",
      "PARAM",
      [
        "storage",
        "002b8df8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a6138",
      "DATA",
      [
        "storage",
        "002ca758",
        "switchD_004a6140::switchdataD_002ca758",
        "byte"
      ]
    ],
    [
      "004a620c",
      "READ",
      [
        "storage",
        "002a645f",
        null,
        "string"
      ]
    ],
    [
      "004a6240",
      "PARAM",
      [
        "storage",
        "002b8e38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a620c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a620c) · [`004a6234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a6234) · [`004a60f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a60c4.md#insn-004a60f0)
- 新版 `004a624c`（命令位置の公開資料なし） · `004a6274`（命令位置の公開資料なし） · `004a6130`（命令位置の公開資料なし）

~~~diff
- 004a620c ["INT_ADD", "register:40f0:8", ["const:4a620c:8", "const:4:8"]]
- 004a620c ["CALL", null, ["callee:00c57f60:8"]]
+ 004a624c ["INT_ADD", "register:40f0:8", ["const:4a624c:8", "const:4:8"]]
+ 004a624c ["CALL", null, ["callee:00c57f60:8"]]
- 004a620c bytes 55c61e94
+ 004a624c bytes 45c71e94
- 004a6234 ["INT_ADD", "register:40f0:8", ["const:4a6234:8", "const:4:8"]]
- 004a6234 ["CALL", null, ["callee:00c57f70:8"]]
+ 004a6274 ["INT_ADD", "register:40f0:8", ["const:4a6274:8", "const:4:8"]]
+ 004a6274 ["CALL", null, ["callee:00c57f70:8"]]
- 004a6234 bytes 4fc61e94
+ 004a6274 bytes 3fc71e94
- 004a60f0 ["COPY", "tmp:0:8", ["const:718:8"]]
- 004a60f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a60f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a60f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004a6130 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 004a6130 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004a6130 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004a6130 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a60f0 bytes 4a611c91
+ 004a6130 bytes 4a611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f64f57637a927cf63a99f5e7d90daad0"></a>

### [`004a63ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md) → [`004a642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md) _ZN5Botan18BER_Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58370.md) [`00c58450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58450.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 2件 [`00c58770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58770.md) [`00c58850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58850.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6490",
      "incomplete_value": true,
      "site": "004a6494",
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
      "definition_site": "004a6450",
      "incomplete_value": true,
      "site": "004a6454",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a64b0",
      "incomplete_value": true,
      "site": "004a64b4",
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
      "definition_site": "004a6470",
      "incomplete_value": true,
      "site": "004a6474",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a64cc",
      "incomplete_value": true,
      "site": "004a64d0",
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
      "definition_site": "004a648c",
      "incomplete_value": true,
      "site": "004a6490",
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
      "004a6448",
      "PARAM",
      [
        "storage",
        "002a2f5b",
        null,
        "string"
      ]
    ],
    [
      "004a6460",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004a6474",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a6448",
      "PARAM",
      [
        "storage",
        "002a3028",
        null,
        "string"
      ]
    ],
    [
      "004a6460",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004a6474",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a6418) · [`004a642c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a642c) · [`004a6434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a63ec.md#insn-004a6434)
- 新版 `004a6458`（命令位置の公開資料なし） · `004a646c`（命令位置の公開資料なし） · `004a6474`（命令位置の公開資料なし）

~~~diff
- 004a6418 ["INT_ADD", "register:40f0:8", ["const:4a6418:8", "const:4:8"]]
- 004a6418 ["CALL", null, ["callee:00c580b0:8"]]
+ 004a6458 ["INT_ADD", "register:40f0:8", ["const:4a6458:8", "const:4:8"]]
+ 004a6458 ["CALL", null, ["callee:00c580b0:8"]]
- 004a6418 bytes 26c61e94
+ 004a6458 bytes 16c71e94
- 004a642c ["INT_ADD", "register:40f0:8", ["const:4a642c:8", "const:4:8"]]
- 004a642c ["CALL", null, ["callee:00c580b0:8"]]
+ 004a646c ["INT_ADD", "register:40f0:8", ["const:4a646c:8", "const:4:8"]]
+ 004a646c ["CALL", null, ["callee:00c580b0:8"]]
- 004a642c bytes 21c61e94
+ 004a646c bytes 11c71e94
- 004a6434 ["COPY", "tmp:0:8", ["const:372:8"]]
- 004a6434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a6434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a6434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a6474 ["COPY", "tmp:0:8", ["const:44e:8"]]
+ 004a6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a6434 bytes 21c80d91
+ 004a6474 bytes 21381191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5caa76efa935d7204774d8d7bdc52bd"></a>

### [`004a64fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md) → [`004a653c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58350.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c58750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58750.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a658c",
      "incomplete_value": true,
      "site": "004a6590",
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
      "definition_site": "004a654c",
      "incomplete_value": true,
      "site": "004a6550",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a65a8",
      "incomplete_value": true,
      "site": "004a65ac",
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
      "definition_site": "004a6568",
      "incomplete_value": true,
      "site": "004a656c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6558",
      "incomplete_value": false,
      "site": "004a6568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:e24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6518",
      "incomplete_value": false,
      "site": "004a6528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:de4:8"
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
      "004a6558",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004a6570",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004a6584",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6558",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004a6570",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004a6584",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a6528) · [`004a653c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a653c) · [`004a6518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a64fc.md#insn-004a6518)
- 新版 `004a6568`（命令位置の公開資料なし） · `004a657c`（命令位置の公開資料なし） · `004a6558`（命令位置の公開資料なし）

~~~diff
- 004a6528 ["INT_ADD", "register:40f0:8", ["const:4a6528:8", "const:4:8"]]
- 004a6528 ["CALL", null, ["callee:00c580b0:8"]]
+ 004a6568 ["INT_ADD", "register:40f0:8", ["const:4a6568:8", "const:4:8"]]
+ 004a6568 ["CALL", null, ["callee:00c580b0:8"]]
- 004a6528 bytes e2c51e94
+ 004a6568 bytes d2c61e94
- 004a653c ["INT_ADD", "register:40f0:8", ["const:4a653c:8", "const:4:8"]]
- 004a653c ["CALL", null, ["callee:00c58780:8"]]
+ 004a657c ["INT_ADD", "register:40f0:8", ["const:4a657c:8", "const:4:8"]]
+ 004a657c ["CALL", null, ["callee:00c58780:8"]]
- 004a653c bytes 91c71e94
+ 004a657c bytes 81c81e94
- 004a6518 ["COPY", "tmp:0:8", ["const:de4:8"]]
- 004a6518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a6518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a6518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a6558 ["COPY", "tmp:0:8", ["const:e24:8"]]
+ 004a6558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a6558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a6558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a6518 bytes 00903791
+ 004a6558 bytes 00903891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a842f8920d165b116dc1bf3e574e448"></a>

### [`004a685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md) → [`004a689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md) _ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagESA_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58440.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c58840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58840.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6a7c",
      "incomplete_value": true,
      "site": "004a6a80",
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
      "definition_site": "004a6a3c",
      "incomplete_value": true,
      "site": "004a6a40",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a69c4",
      "incomplete_value": false,
      "site": "004a69cc",
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
            "const:352:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6984",
      "incomplete_value": false,
      "site": "004a698c",
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
            "const:276:8"
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
      "004a69c4",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004a6a78",
      "READ",
      [
        "storage",
        "00c9a978",
        null,
        "pointer"
      ]
    ],
    [
      "004a6a80",
      "DATA",
      [
        "storage",
        "00c65e30",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004a69c4",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      "004a6a78",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004a6a80",
      "DATA",
      [
        "storage",
        "00c66230",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a698c) · [`004a68fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a68fc) · [`004a6924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a685c.md#insn-004a6924)
- 新版 `004a69cc`（命令位置の公開資料なし） · `004a693c`（命令位置の公開資料なし） · `004a6964`（命令位置の公開資料なし）

~~~diff
- 004a698c ["INT_ADD", "register:40f0:8", ["const:4a698c:8", "const:4:8"]]
- 004a698c ["CALL", null, ["callee:00c57f70:8"]]
+ 004a69cc ["INT_ADD", "register:40f0:8", ["const:4a69cc:8", "const:4:8"]]
+ 004a69cc ["CALL", null, ["callee:00c57f70:8"]]
- 004a698c bytes 79c41e94
+ 004a69cc bytes 69c51e94
- 004a68fc ["INT_ADD", "register:40f0:8", ["const:4a68fc:8", "const:4:8"]]
- 004a68fc ["CALL", null, ["callee:00c57e90:8"]]
+ 004a693c ["INT_ADD", "register:40f0:8", ["const:4a693c:8", "const:4:8"]]
+ 004a693c ["CALL", null, ["callee:00c57e90:8"]]
- 004a68fc bytes 65c41e94
+ 004a693c bytes 55c51e94
- 004a6924 ["INT_ADD", "register:40f0:8", ["const:4a6924:8", "const:4:8"]]
- 004a6924 ["CALL", null, ["callee:00c57f40:8"]]
+ 004a6964 ["INT_ADD", "register:40f0:8", ["const:4a6964:8", "const:4:8"]]
+ 004a6964 ["CALL", null, ["callee:00c57f40:8"]]
- 004a6924 bytes 87c41e94
+ 004a6964 bytes 77c51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18da8765e1f18661b83fd12c1ee423f"></a>

### [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) → [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) FUN_004a6f9c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 3件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`004f0edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md) [`0050d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a703c",
      "incomplete_value": false,
      "site": "004a7044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:bbe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6ffc",
      "incomplete_value": false,
      "site": "004a7004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:b7e:8"
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
      "definition_site": "004a7078",
      "incomplete_value": true,
      "site": "004a7084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7038",
      "incomplete_value": true,
      "site": "004a7044",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
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
      "definition_site": "004a7074",
      "incomplete_value": false,
      "site": "004a7084",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a7034",
      "incomplete_value": false,
      "site": "004a7044",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a703c",
      "PARAM",
      [
        "storage",
        "002b4b7e",
        null,
        "string"
      ]
    ],
    [
      "004a7074",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a7078",
      "READ",
      [
        "storage",
        "00c9a980",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a703c",
      "PARAM",
      [
        "storage",
        "002b4bbe",
        null,
        "string"
      ]
    ],
    [
      "004a7074",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a7078",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7004) · [`004a7044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7044) · [`004a7080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md#insn-004a7080)
- 新版 `004a7044`（命令位置の公開資料なし） · `004a7084`（命令位置の公開資料なし） · `004a70c0`（命令位置の公開資料なし）

~~~diff
- 004a7004 ["INT_ADD", "register:40f0:8", ["const:4a7004:8", "const:4:8"]]
- 004a7004 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a7044 ["INT_ADD", "register:40f0:8", ["const:4a7044:8", "const:4:8"]]
+ 004a7044 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a7004 bytes 655bfe97
+ 004a7044 bytes 655bfe97
- 004a7044 ["INT_ADD", "register:40f0:8", ["const:4a7044:8", "const:4:8"]]
- 004a7044 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a7084 ["INT_ADD", "register:40f0:8", ["const:4a7084:8", "const:4:8"]]
+ 004a7084 ["CALL", null, ["callee:00c57f10:8"]]
- 004a7044 bytes b3c21e94
+ 004a7084 bytes a3c31e94
- 004a7080 ["INT_ADD", "register:40f0:8", ["const:4a7080:8", "const:4:8"]]
- 004a7080 ["CALL", null, ["callee:00c58650:8"]]
+ 004a70c0 ["INT_ADD", "register:40f0:8", ["const:4a70c0:8", "const:4:8"]]
+ 004a70c0 ["CALL", null, ["callee:00c58650:8"]]
- 004a7080 bytes 74c41e94
+ 004a70c0 bytes 64c51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5068854e1e4c8286e6bd3ac858852977"></a>

### [`004a70f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md) → [`004a7138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md) _ZN5Botan17assertion_failureEPKcS1_S1_S1_i

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md) · 呼出先 11件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md) · 呼出先 11件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.62% / 新版 85.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7180",
      "incomplete_value": true,
      "site": "004a7190",
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
      "definition_site": "004a7140",
      "incomplete_value": true,
      "site": "004a7150",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7188",
      "incomplete_value": true,
      "site": "004a719c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a7148",
      "incomplete_value": true,
      "site": "004a715c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004a71a4",
      "incomplete_value": true,
      "site": "004a71a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "004a7164",
      "incomplete_value": true,
      "site": "004a7164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a716c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004a7170",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7188",
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
      "004a716c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004a7170",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a7188",
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

- 旧版 [`004a719c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a719c) · [`004a71d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a71d0) · [`004a7210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a70f8.md#insn-004a7210)
- 新版 `004a71dc`（命令位置の公開資料なし） · `004a7210`（命令位置の公開資料なし） · `004a7250`（命令位置の公開資料なし）

~~~diff
- 004a719c ["INT_ADD", "register:40f0:8", ["const:4a719c:8", "const:4:8"]]
- 004a719c ["CALL", null, ["callee:00c581f0:8"]]
+ 004a71dc ["INT_ADD", "register:40f0:8", ["const:4a71dc:8", "const:4:8"]]
+ 004a71dc ["CALL", null, ["callee:00c581f0:8"]]
- 004a719c bytes 15c31e94
+ 004a71dc bytes 05c41e94
- 004a71d0 ["INT_ADD", "register:40f0:8", ["const:4a71d0:8", "const:4:8"]]
- 004a71d0 ["CALL", null, ["callee:004594d0:8"]]
+ 004a7210 ["INT_ADD", "register:40f0:8", ["const:4a7210:8", "const:4:8"]]
+ 004a7210 ["CALL", null, ["callee:004594d0:8"]]
- 004a71d0 bytes b0c8fe97
+ 004a7210 bytes b0c8fe97
- 004a7210 ["COPY", "tmp:0:8", ["const:890:8"]]
- 004a7210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a7210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a7210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a7250 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 004a7250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a7250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a7250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a7210 bytes 21402291
+ 004a7250 bytes 21402391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a46b3f20930c74957c8e5f8e2f99aa2"></a>

### [`004a7408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md) → [`004a7448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md) _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

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
      "definition_site": "004a7474",
      "incomplete_value": true,
      "site": "004a747c",
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
      "definition_site": "004a7434",
      "incomplete_value": true,
      "site": "004a743c",
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
      "definition_site": "004a7564",
      "incomplete_value": true,
      "site": "004a756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7524",
      "incomplete_value": true,
      "site": "004a752c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:990:8"
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
      "definition_site": "004a7560",
      "incomplete_value": false,
      "site": "004a756c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a7520",
      "incomplete_value": false,
      "site": "004a752c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004a746c",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a747c",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a7560",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a746c",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a747c",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a7560",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a752c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a752c) · [`004a742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a742c) · [`004a7470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a7470)
- 新版 `004a756c`（命令位置の公開資料なし） · `004a746c`（命令位置の公開資料なし） · `004a74b0`（命令位置の公開資料なし）

~~~diff
- 004a752c ["INT_ADD", "register:40f0:8", ["const:4a752c:8", "const:4:8"]]
- 004a752c ["CALL", null, ["callee:00c57f10:8"]]
+ 004a756c ["INT_ADD", "register:40f0:8", ["const:4a756c:8", "const:4:8"]]
+ 004a756c ["CALL", null, ["callee:00c57f10:8"]]
- 004a752c bytes 79c11e94
+ 004a756c bytes 69c21e94
- 004a742c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 004a742c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a746c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 004a746c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a742c bytes 08a144f9
+ 004a746c bytes 08a146f9
- 004a7470 ["INT_ADD", "register:40f0:8", ["const:4a7470:8", "const:4:8"]]
- 004a7470 ["CALL", null, ["callee:00c587d0:8"]]
+ 004a74b0 ["INT_ADD", "register:40f0:8", ["const:4a74b0:8", "const:4:8"]]
+ 004a74b0 ["CALL", null, ["callee:00c587d0:8"]]
- 004a7470 bytes d8c31e94
+ 004a74b0 bytes c8c41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e56dd9e9f993cef0a028f8b160e7e233"></a>

### [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) → [`004a762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583d0.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c587d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587d0.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a791c",
      "incomplete_value": true,
      "site": "004a7924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a78dc",
      "incomplete_value": true,
      "site": "004a78e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:990:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a7918",
      "incomplete_value": false,
      "site": "004a7924",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a78d8",
      "incomplete_value": false,
      "site": "004a78e4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 12,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a79a8",
      "incomplete_value": true,
      "site": "004a79b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7968",
      "incomplete_value": true,
      "site": "004a7970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:990:8"
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
      "004a7918",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a791c",
      "READ",
      [
        "storage",
        "00c9a990",
        null,
        "pointer"
      ]
    ],
    [
      "004a791c",
      "PARAM",
      [
        "storage",
        "00c65ed8",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a7918",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a791c",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      "004a791c",
      "PARAM",
      [
        "storage",
        "00c662d8",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a78e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a78e4) · [`004a7970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a7970) · [`004a7664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a7664)
- 新版 `004a7924`（命令位置の公開資料なし） · `004a79b0`（命令位置の公開資料なし） · `004a76a4`（命令位置の公開資料なし）

~~~diff
- 004a78e4 ["INT_ADD", "register:40f0:8", ["const:4a78e4:8", "const:4:8"]]
- 004a78e4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a7924 ["INT_ADD", "register:40f0:8", ["const:4a7924:8", "const:4:8"]]
+ 004a7924 ["CALL", null, ["callee:00c57f10:8"]]
- 004a78e4 bytes 8bc01e94
+ 004a7924 bytes 7bc11e94
- 004a7970 ["INT_ADD", "register:40f0:8", ["const:4a7970:8", "const:4:8"]]
- 004a7970 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a79b0 ["INT_ADD", "register:40f0:8", ["const:4a79b0:8", "const:4:8"]]
+ 004a79b0 ["CALL", null, ["callee:00c57f10:8"]]
- 004a7970 bytes 68c01e94
+ 004a79b0 bytes 58c11e94
- 004a7664 ["INT_ADD", "register:40f0:8", ["const:4a7664:8", "const:4:8"]]
- 004a7664 ["CALL", null, ["callee:00c58600:8"]]
+ 004a76a4 ["INT_ADD", "register:40f0:8", ["const:4a76a4:8", "const:4:8"]]
+ 004a76a4 ["CALL", null, ["callee:00c58600:8"]]
- 004a7664 bytes e7c21e94
+ 004a76a4 bytes d7c31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d6df9bf3d74e21e239c859706f74925"></a>

### [`004a7cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md) → [`004a7cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md) _ZN5BotanplERKNS_3OIDEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7d24",
      "incomplete_value": true,
      "site": "004a7d30",
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
      "definition_site": "004a7ce4",
      "incomplete_value": true,
      "site": "004a7cf0",
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
      "004a7d14",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a7d30",
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
      "004a7d14",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a7d30",
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

- 旧版 [`004a7cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7cd4) · [`004a7d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7d00) · [`004a7d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7d18)
- 新版 `004a7d14`（命令位置の公開資料なし） · `004a7d40`（命令位置の公開資料なし） · `004a7d58`（命令位置の公開資料なし）

~~~diff
- 004a7cd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 004a7cd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7d14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 004a7d14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7cd4 bytes 08a144f9
+ 004a7d14 bytes 08a146f9
- 004a7d00 ["INT_ADD", "register:40f0:8", ["const:4a7d00:8", "const:4:8"]]
- 004a7d00 ["CALL", null, ["callee:00c57e90:8"]]
+ 004a7d40 ["INT_ADD", "register:40f0:8", ["const:4a7d40:8", "const:4:8"]]
+ 004a7d40 ["CALL", null, ["callee:00c57e90:8"]]
- 004a7d00 bytes 64bf1e94
+ 004a7d40 bytes 54c01e94
- 004a7d18 ["INT_ADD", "register:40f0:8", ["const:4a7d18:8", "const:4:8"]]
- 004a7d18 ["CALL", null, ["callee:00c58000:8"]]
+ 004a7d58 ["INT_ADD", "register:40f0:8", ["const:4a7d58:8", "const:4:8"]]
+ 004a7d58 ["CALL", null, ["callee:00c58000:8"]]
- 004a7d18 bytes babf1e94
+ 004a7d58 bytes aac01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7bed03f559bc81316c5e8d523d33bb8"></a>

### [`004a7de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md) → [`004a7e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md) _ZNK5Botan3OID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8184",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:26e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8144",
      "incomplete_value": false,
      "site": "004a8164",
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
            "const:22e:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a818c",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a814c",
      "incomplete_value": false,
      "site": "004a8164",
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
            "const:e03:8"
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
      "definition_site": "004a8194",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8154",
      "incomplete_value": false,
      "site": "004a8164",
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
            "const:53:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a8184",
      "PARAM",
      [
        "storage",
        "002bb22e",
        null,
        "string"
      ]
    ],
    [
      "004a818c",
      "PARAM",
      [
        "storage",
        "002a1e03",
        null,
        "string"
      ]
    ],
    [
      "004a8194",
      "PARAM",
      [
        "storage",
        "002ba053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a8184",
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      "004a818c",
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      "004a8194",
      "PARAM",
      [
        "storage",
        "002ba093",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a8164) · [`004a81d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a81d4) · [`004a8214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a8214)
- 新版 `004a81a4`（命令位置の公開資料なし） · `004a8214`（命令位置の公開資料なし） · `004a8254`（命令位置の公開資料なし）

~~~diff
- 004a8164 ["INT_ADD", "register:40f0:8", ["const:4a8164:8", "const:4:8"]]
- 004a8164 ["CALL", null, ["callee:00c58650:8"]]
+ 004a81a4 ["INT_ADD", "register:40f0:8", ["const:4a81a4:8", "const:4:8"]]
+ 004a81a4 ["CALL", null, ["callee:00c58650:8"]]
- 004a8164 bytes 3bc01e94
+ 004a81a4 bytes 2bc11e94
- 004a81d4 ["INT_ADD", "register:40f0:8", ["const:4a81d4:8", "const:4:8"]]
- 004a81d4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a8214 ["INT_ADD", "register:40f0:8", ["const:4a8214:8", "const:4:8"]]
+ 004a8214 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a81d4 bytes f156fe97
+ 004a8214 bytes f156fe97
- 004a8214 ["INT_ADD", "register:40f0:8", ["const:4a8214:8", "const:4:8"]]
- 004a8214 ["CALL", null, ["callee:00c57f10:8"]]
+ 004a8254 ["INT_ADD", "register:40f0:8", ["const:4a8254:8", "const:4:8"]]
+ 004a8254 ["CALL", null, ["callee:00c57f10:8"]]
- 004a8214 bytes 3fbe1e94
+ 004a8254 bytes 2fbf1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c50a64f6c39f2752aa9c0eeb9b648d20"></a>

### [`004a8360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md) → [`004a83a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md) _ZN5Botan3OID11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a8690",
      "incomplete_value": true,
      "site": "004a8690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8650",
      "incomplete_value": true,
      "site": "004a8650",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a86dc",
      "incomplete_value": false,
      "site": "004a86e4",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a869c",
      "incomplete_value": false,
      "site": "004a86a4",
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
            "const:d8b:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8718",
      "incomplete_value": true,
      "site": "004a8724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a86d8",
      "incomplete_value": true,
      "site": "004a86e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "004a8680",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a86dc",
      "PARAM",
      [
        "storage",
        "0029ed8b",
        null,
        "string"
      ]
    ],
    [
      "004a8714",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a8680",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a86dc",
      "PARAM",
      [
        "storage",
        "0029ee58",
        null,
        "string"
      ]
    ],
    [
      "004a8714",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a8650) · [`004a8690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a8690) · [`004a86a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a86a4)
- 新版 `004a8690`（命令位置の公開資料なし） · `004a86d0`（命令位置の公開資料なし） · `004a86e4`（命令位置の公開資料なし）

~~~diff
- 004a8650 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a8650 ["INT_ADD", "register:40f0:8", ["const:4a8650:8", "const:4:8"]]
- 004a8650 ["CALLIND", null, ["register:0:8"]]
+ 004a8690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8690 ["INT_ADD", "register:40f0:8", ["const:4a8690:8", "const:4:8"]]
+ 004a8690 ["CALLIND", null, ["register:0:8"]]
- 004a8650 bytes 20013fd6
+ 004a8690 bytes 20013fd6
- 004a8690 ["INT_ADD", "register:40f0:8", ["const:4a8690:8", "const:4:8"]]
- 004a8690 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004a86d0 ["INT_ADD", "register:40f0:8", ["const:4a86d0:8", "const:4:8"]]
+ 004a86d0 ["CALL", null, ["callee:00c57ef0:8"]]
- 004a8690 bytes 18bd1e94
+ 004a86d0 bytes 08be1e94
- 004a86a4 ["INT_ADD", "register:40f0:8", ["const:4a86a4:8", "const:4:8"]]
- 004a86a4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a86e4 ["INT_ADD", "register:40f0:8", ["const:4a86e4:8", "const:4:8"]]
+ 004a86e4 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a86a4 bytes bd55fe97
+ 004a86e4 bytes bd55fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e8d2d84d8893d8a5cf633d25619c82"></a>

### [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) → [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) _ZN5Botan11BER_Decoder15get_next_objectEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)
- 新版 呼出元 1件 [`00c58720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8a38",
      "incomplete_value": false,
      "site": "004a8a40",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a89f8",
      "incomplete_value": false,
      "site": "004a8a00",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a8a70",
      "incomplete_value": true,
      "site": "004a8a7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8a30",
      "incomplete_value": true,
      "site": "004a8a3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "definition_site": "004a8a6c",
      "incomplete_value": false,
      "site": "004a8a7c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004a8a2c",
      "incomplete_value": false,
      "site": "004a8a3c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a8a38",
      "PARAM",
      [
        "storage",
        "002b19d0",
        null,
        "string"
      ]
    ],
    [
      "004a8a6c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a8a70",
      "READ",
      [
        "storage",
        "00c9a9a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8a38",
      "PARAM",
      [
        "storage",
        "002b1a10",
        null,
        "string"
      ]
    ],
    [
      "004a8a6c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a8a70",
      "READ",
      [
        "storage",
        "00c9ada8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a00) · [`004a8a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a3c) · [`004a8a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a5c)
- 新版 `004a8a40`（命令位置の公開資料なし） · `004a8a7c`（命令位置の公開資料なし） · `004a8a9c`（命令位置の公開資料なし）

~~~diff
- 004a8a00 ["INT_ADD", "register:40f0:8", ["const:4a8a00:8", "const:4:8"]]
- 004a8a00 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a8a40 ["INT_ADD", "register:40f0:8", ["const:4a8a40:8", "const:4:8"]]
+ 004a8a40 ["CALL", null, ["callee:0043ddd8:8"]]
- 004a8a00 bytes e654fe97
+ 004a8a40 bytes e654fe97
- 004a8a3c ["INT_ADD", "register:40f0:8", ["const:4a8a3c:8", "const:4:8"]]
- 004a8a3c ["CALL", null, ["callee:00c57f10:8"]]
+ 004a8a7c ["INT_ADD", "register:40f0:8", ["const:4a8a7c:8", "const:4:8"]]
+ 004a8a7c ["CALL", null, ["callee:00c57f10:8"]]
- 004a8a3c bytes 35bc1e94
+ 004a8a7c bytes 25bd1e94
- 004a8a5c ["INT_ADD", "register:40f0:8", ["const:4a8a5c:8", "const:4:8"]]
- 004a8a5c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004a8a9c ["INT_ADD", "register:40f0:8", ["const:4a8a9c:8", "const:4:8"]]
+ 004a8a9c ["CALL", null, ["callee:0043ddd8:8"]]
- 004a8a5c bytes cf54fe97
+ 004a8a9c bytes cf54fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad386214f6adc34e7cb2edb2ba673bd"></a>

### [`004a8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md) → [`004a8b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md) _ZNK5Botan14ASN1_Formatter5printEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.64% / 新版 87.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8be4",
      "incomplete_value": true,
      "site": "004a8bf4",
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
      "definition_site": "004a8ba4",
      "incomplete_value": true,
      "site": "004a8bb4",
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
      "definition_site": "004a8bec",
      "incomplete_value": true,
      "site": "004a8bfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8bac",
      "incomplete_value": true,
      "site": "004a8bbc",
      "value": [
        "LOAD",
        "8",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004a8c04",
      "incomplete_value": true,
      "site": "004a8c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:8:8"
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
      "definition_site": "004a8bc4",
      "incomplete_value": true,
      "site": "004a8bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:8:8"
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
      "004a8bd0",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bd4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bec",
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
      "004a8bd0",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bd4",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bec",
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

- 旧版 [`004a8bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8bfc) · [`004a8b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8b90) · [`004a8b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8b94)
- 新版 `004a8c3c`（命令位置の公開資料なし） · `004a8bd0`（命令位置の公開資料なし） · `004a8bd4`（命令位置の公開資料なし）

~~~diff
- 004a8bfc ["INT_ADD", "register:40f0:8", ["const:4a8bfc:8", "const:4:8"]]
- 004a8bfc ["CALL", null, ["callee:00c581f0:8"]]
+ 004a8c3c ["INT_ADD", "register:40f0:8", ["const:4a8c3c:8", "const:4:8"]]
+ 004a8c3c ["CALL", null, ["callee:00c581f0:8"]]
- 004a8bfc bytes 7dbc1e94
+ 004a8c3c bytes 6dbd1e94
- 004a8b90 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:888:8"]]
- 004a8b90 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8bd0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c88:8"]]
+ 004a8bd0 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8b90 bytes 7b4744f9
+ 004a8bd0 bytes 7b4746f9
- 004a8b94 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:7b8:8"]]
- 004a8b94 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8bd4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:bb8:8"]]
+ 004a8bd4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8b94 bytes 5adf43f9
+ 004a8bd4 bytes 5adf45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab7e618a71615362b969c82f516368f"></a>

### [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) → [`004a8e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58470.md) · 呼出先 36件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c58870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58870.md) · 呼出先 36件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.82% / 新版 93.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 8件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f0c",
      "incomplete_value": true,
      "site": "004a8f20",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8ecc",
      "incomplete_value": true,
      "site": "004a8ee0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f30",
      "incomplete_value": true,
      "site": "004a8f30",
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
      "definition_site": "004a8ef0",
      "incomplete_value": true,
      "site": "004a8ef0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f30",
      "incomplete_value": true,
      "site": "004a8f30",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8ef0",
      "incomplete_value": true,
      "site": "004a8ef0",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
      "004a8e98",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a8ef4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f0c",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a8e98",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a8ef4",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f0c",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a8e68) · [`004a90a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a90a8) · [`004a9264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a9264)
- 新版 `004a8ea8`（命令位置の公開資料なし） · `004a90e8`（命令位置の公開資料なし） · `004a92a4`（命令位置の公開資料なし）

~~~diff
- 004a8e68 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a8e68 ["INT_ADD", "register:40f0:8", ["const:4a8e68:8", "const:4:8"]]
- 004a8e68 ["CALLIND", null, ["register:0:8"]]
+ 004a8ea8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8ea8 ["INT_ADD", "register:40f0:8", ["const:4a8ea8:8", "const:4:8"]]
+ 004a8ea8 ["CALLIND", null, ["register:0:8"]]
- 004a8e68 bytes 20013fd6
+ 004a8ea8 bytes 20013fd6
- 004a90a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a90a8 ["INT_ADD", "register:40f0:8", ["const:4a90a8:8", "const:4:8"]]
- 004a90a8 ["CALLIND", null, ["register:0:8"]]
+ 004a90e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a90e8 ["INT_ADD", "register:40f0:8", ["const:4a90e8:8", "const:4:8"]]
+ 004a90e8 ["CALLIND", null, ["register:0:8"]]
- 004a90a8 bytes 20013fd6
+ 004a90e8 bytes 20013fd6
- 004a9264 ["INT_ADD", "register:40f0:8", ["const:4a9264:8", "const:4:8"]]
- 004a9264 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004a92a4 ["INT_ADD", "register:40f0:8", ["const:4a92a4:8", "const:4:8"]]
+ 004a92a4 ["CALL", null, ["callee:00c57fb0:8"]]
- 004a9264 bytes 53ba1e94
+ 004a92a4 bytes 43bb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe1d7e9ea352463ec674db0b9391b3b"></a>

### [`004aa23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md) → [`004aa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004aa/004aa27c.md) _ZN5Botan4OIDS6lookupERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md) · 呼出先 5件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md)
- 新版 呼出元 1件 [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md) · 呼出先 5件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 34.56% / 新版 34.56%

CFGの説明率　旧版 29.62% / 新版 29.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 65件, `store_value` 1件, `unresolved_branch_alignment` 117件, `unresolved_call_alignment` 117件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004aa4e4",
      "incomplete_value": true,
      "site": "004aa4e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3dd:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004aa458"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004aa478"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004aa3bc",
      "PARAM",
      [
        "storage",
        "002a63e7",
        null,
        null
      ]
    ],
    [
      "004aa46c",
      "PARAM",
      [
        "storage",
        "002ac611",
        null,
        "string"
      ]
    ],
    [
      "004aa478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:004aa448"
      ]
    ]
  ],
  "added": [
    [
      "004aa3bc",
      "PARAM",
      [
        "storage",
        "002a64c3",
        null,
        null
      ]
    ],
    [
      "004aa46c",
      "PARAM",
      [
        "storage",
        "002ac651",
        null,
        "string"
      ]
    ],
    [
      "004aa478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004aa488"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md#insn-004aa458) · [`004aa478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md#insn-004aa478) · [`004aa4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md#insn-004aa4e0)

~~~diff
- 004aa458 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004aa458 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004aa458 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004aa458 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004aa458 bytes 80000036
- 004aa478 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004aa478 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004aa478 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004aa478 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004aa478 bytes c0020036
- 004aa4e0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004aa4e0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004aa4e0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004aa4e0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004aa4e0 bytes e0020036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9179f39b2400ce137bbc142d38cd30"></a>

### [`004abd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md) → [`004abd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md) _ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c584c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584c0.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58330.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)
- 新版 呼出元 1件 [`00c588c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588c0.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) [`00c58730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.27% / 新版 96.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abe9c",
      "incomplete_value": true,
      "site": "004abe9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004abe5c",
      "incomplete_value": true,
      "site": "004abe5c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abf24",
      "incomplete_value": true,
      "site": "004abf24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004abee4",
      "incomplete_value": true,
      "site": "004abee4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abf54",
      "incomplete_value": true,
      "site": "004abf54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004abf14",
      "incomplete_value": true,
      "site": "004abf14",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "004abe8c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004abf14",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004abf44",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004abe8c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004abf14",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004abf44",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004abe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abe5c) · [`004abed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abed4) · [`004abee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abee4)
- 新版 `004abe9c`（命令位置の公開資料なし） · `004abf14`（命令位置の公開資料なし） · `004abf24`（命令位置の公開資料なし）

~~~diff
- 004abe5c ["COPY", "register:0:8", ["register:4048:8"]]
- 004abe5c ["INT_ADD", "register:40f0:8", ["const:4abe5c:8", "const:4:8"]]
- 004abe5c ["CALLIND", null, ["register:0:8"]]
+ 004abe9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abe9c ["INT_ADD", "register:40f0:8", ["const:4abe9c:8", "const:4:8"]]
+ 004abe9c ["CALLIND", null, ["register:0:8"]]
- 004abe5c bytes 20013fd6
+ 004abe9c bytes 20013fd6
- 004abed4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:338:8"]]
- 004abed4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004abf14 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:738:8"]]
+ 004abf14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004abed4 bytes c99e41f9
+ 004abf14 bytes c99e43f9
- 004abee4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004abee4 ["INT_ADD", "register:40f0:8", ["const:4abee4:8", "const:4:8"]]
- 004abee4 ["CALLIND", null, ["register:0:8"]]
+ 004abf24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abf24 ["INT_ADD", "register:40f0:8", ["const:4abf24:8", "const:4:8"]]
+ 004abf24 ["CALLIND", null, ["register:0:8"]]
- 004abee4 bytes 20013fd6
+ 004abf24 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab33883d560440185f217582d6d06d6"></a>

### [`004ac1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md) → [`004ac1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) _ZNK5Botan9X509_Time15readable_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58510.md) · 呼出先 17件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`00c58910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58910.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac3a0",
      "incomplete_value": true,
      "site": "004ac3a8",
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
      "definition_site": "004ac360",
      "incomplete_value": true,
      "site": "004ac368",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004ac3b0",
      "incomplete_value": true,
      "site": "004ac3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "004ac370",
      "incomplete_value": true,
      "site": "004ac370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac3b0",
      "incomplete_value": true,
      "site": "004ac3b0",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ac370",
      "incomplete_value": true,
      "site": "004ac370",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "004ac254",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004ac254",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac2a0",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ac254",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004ac254",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac2a0",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac218) · [`004ac228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac228) · [`004ac258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac258)
- 新版 `004ac258`（命令位置の公開資料なし） · `004ac268`（命令位置の公開資料なし） · `004ac298`（命令位置の公開資料なし）

~~~diff
- 004ac218 ["INT_ADD", "register:40f0:8", ["const:4ac218:8", "const:4:8"]]
- 004ac218 ["CALL", null, ["callee:00c58280:8"]]
+ 004ac258 ["INT_ADD", "register:40f0:8", ["const:4ac258:8", "const:4:8"]]
+ 004ac258 ["CALL", null, ["callee:00c58280:8"]]
- 004ac218 bytes 1aaf1e94
+ 004ac258 bytes 0ab01e94
- 004ac228 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ac228 ["INT_ADD", "register:40f0:8", ["const:4ac228:8", "const:4:8"]]
- 004ac228 ["CALLIND", null, ["register:0:8"]]
+ 004ac268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ac268 ["INT_ADD", "register:40f0:8", ["const:4ac268:8", "const:4:8"]]
+ 004ac268 ["CALLIND", null, ["register:0:8"]]
- 004ac228 bytes 00013fd6
+ 004ac268 bytes 00013fd6
- 004ac258 ["INT_ADD", "register:40f0:8", ["const:4ac258:8", "const:4:8"]]
- 004ac258 ["CALL", null, ["callee:00c58960:8"]]
+ 004ac298 ["INT_ADD", "register:40f0:8", ["const:4ac298:8", "const:4:8"]]
+ 004ac298 ["CALL", null, ["callee:00c58960:8"]]
- 004ac258 bytes c2b01e94
+ 004ac298 bytes b2b11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696e132732fe005d817e07408520686a"></a>

### [`004ac4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md) → [`004ac500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md) _ZNK5Botan19ASN1_Pretty_Printer6formatENS_8ASN1_TagES1_mmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.12% / 新版 93.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac5b4",
      "incomplete_value": true,
      "site": "004ac5b8",
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
      "definition_site": "004ac574",
      "incomplete_value": true,
      "site": "004ac578",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac5b0",
      "incomplete_value": true,
      "site": "004ac5bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ac570",
      "incomplete_value": true,
      "site": "004ac57c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004ac5c4",
      "incomplete_value": true,
      "site": "004ac5c4",
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
                "const:b0:8"
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
      "definition_site": "004ac584",
      "incomplete_value": true,
      "site": "004ac584",
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
                "const:b0:8"
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
    "ordinal": 21,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ac59c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5a0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5b0",
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
      "004ac59c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5a0",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5b0",
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

- 旧版 [`004ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac5f8) · [`004ac628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac628) · [`004ac654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac654)
- 新版 `004ac638`（命令位置の公開資料なし） · `004ac668`（命令位置の公開資料なし） · `004ac694`（命令位置の公開資料なし）

~~~diff
- 004ac5f8 ["INT_ADD", "register:40f0:8", ["const:4ac5f8:8", "const:4:8"]]
- 004ac5f8 ["CALL", null, ["callee:004594d0:8"]]
+ 004ac638 ["INT_ADD", "register:40f0:8", ["const:4ac638:8", "const:4:8"]]
+ 004ac638 ["CALL", null, ["callee:004594d0:8"]]
- 004ac5f8 bytes a6b3fe97
+ 004ac638 bytes a6b3fe97
- 004ac628 ["INT_ADD", "register:40f0:8", ["const:4ac628:8", "const:4:8"]]
- 004ac628 ["CALL", null, ["callee:004594d0:8"]]
+ 004ac668 ["INT_ADD", "register:40f0:8", ["const:4ac668:8", "const:4:8"]]
+ 004ac668 ["CALL", null, ["callee:004594d0:8"]]
- 004ac628 bytes 9ab3fe97
+ 004ac668 bytes 9ab3fe97
- 004ac654 ["INT_ADD", "register:40f0:8", ["const:4ac654:8", "const:4:8"]]
- 004ac654 ["CALL", null, ["callee:004594d0:8"]]
+ 004ac694 ["INT_ADD", "register:40f0:8", ["const:4ac694:8", "const:4:8"]]
+ 004ac694 ["CALL", null, ["callee:004594d0:8"]]
- 004ac654 bytes 8fb3fe97
+ 004ac694 bytes 8fb3fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b81b8c75d71f825bc661ae705437428b"></a>

### [`004ace10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md) → [`004ace50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59560.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004acf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md)
- 新版 呼出元 1件 [`00c59960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59960.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004acf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ace7c",
      "incomplete_value": true,
      "site": "004ace80",
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
      "definition_site": "004ace3c",
      "incomplete_value": true,
      "site": "004ace40",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ace6c",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ace80",
      "DATA",
      [
        "storage",
        "00c65f48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004acef4",
      "DATA",
      [
        "storage",
        "002cf528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ace6c",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ace80",
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004acef4",
      "DATA",
      [
        "storage",
        "002cf568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ace2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004ace2c) · [`004ace6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004ace6c) · [`004aceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004aceac)
- 新版 `004ace6c`（命令位置の公開資料なし） · `004aceac`（命令位置の公開資料なし） · `004aceec`（命令位置の公開資料なし）

~~~diff
- 004ace2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 004ace2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ace6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 004ace6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ace2c bytes 08dd44f9
+ 004ace6c bytes 08dd46f9
- 004ace6c ["INT_ADD", "register:40f0:8", ["const:4ace6c:8", "const:4:8"]]
- 004ace6c ["CALL", null, ["callee:0043bb20:8"]]
+ 004aceac ["INT_ADD", "register:40f0:8", ["const:4aceac:8", "const:4:8"]]
+ 004aceac ["CALL", null, ["callee:0043bb20:8"]]
- 004ace6c bytes 1d3bfe97
+ 004aceac bytes 1d3bfe97
- 004aceac ["COPY", "tmp:0:8", ["const:528:8"]]
- 004aceac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004aceac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004aceac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004aceec ["COPY", "tmp:0:8", ["const:568:8"]]
+ 004aceec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004aceec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004aceec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004aceac bytes 4aa11491
+ 004aceec bytes 4aa11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b63bf0c740992c33b95022a2b09c79"></a>

### [`004acf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md) → [`004acf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md) FUN_004acf78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ace10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md) [`004ad734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad734.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 2件 [`004ace50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) [`004ad774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad774.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad000",
      "incomplete_value": false,
      "site": "004ad00c",
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
            "const:9cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004acfc0",
      "incomplete_value": false,
      "site": "004acfcc",
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
            "const:98f:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad058",
      "incomplete_value": true,
      "site": "004ad064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad018",
      "incomplete_value": true,
      "site": "004ad024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "definition_site": "004ad054",
      "incomplete_value": false,
      "site": "004ad064",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ad014",
      "incomplete_value": false,
      "site": "004ad024",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004ad000",
      "PARAM",
      [
        "storage",
        "002ae98f",
        null,
        "string"
      ]
    ],
    [
      "004ad054",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ad058",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad000",
      "PARAM",
      [
        "storage",
        "002ae9cf",
        null,
        "string"
      ]
    ],
    [
      "004ad054",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ad058",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004acfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004acfcc) · [`004ad024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004ad024) · [`004acfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004acfa8)
- 新版 `004ad00c`（命令位置の公開資料なし） · `004ad064`（命令位置の公開資料なし） · `004acfe8`（命令位置の公開資料なし）

~~~diff
- 004acfcc ["INT_ADD", "register:40f0:8", ["const:4acfcc:8", "const:4:8"]]
- 004acfcc ["CALL", null, ["callee:00c57f60:8"]]
+ 004ad00c ["INT_ADD", "register:40f0:8", ["const:4ad00c:8", "const:4:8"]]
+ 004ad00c ["CALL", null, ["callee:00c57f60:8"]]
- 004acfcc bytes e5aa1e94
+ 004ad00c bytes d5ab1e94
- 004ad024 ["INT_ADD", "register:40f0:8", ["const:4ad024:8", "const:4:8"]]
- 004ad024 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ad064 ["INT_ADD", "register:40f0:8", ["const:4ad064:8", "const:4:8"]]
+ 004ad064 ["CALL", null, ["callee:00c57f10:8"]]
- 004ad024 bytes bbaa1e94
+ 004ad064 bytes abab1e94
- 004acfa8 ["INT_ADD", "register:40f0:8", ["const:4acfa8:8", "const:4:8"]]
- 004acfa8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004acfe8 ["INT_ADD", "register:40f0:8", ["const:4acfe8:8", "const:4:8"]]
+ 004acfe8 ["CALL", null, ["callee:00c57ef0:8"]]
- 004acfa8 bytes d2aa1e94
+ 004acfe8 bytes c2ab1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f5fe068b88f9ce0d0cdde5308bf89f5"></a>

### [`004ad0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md) → [`004ad0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c584f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584f0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00c588f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588f0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ad104",
      "incomplete_value": true,
      "site": "004ad108",
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
      "definition_site": "004ad0c4",
      "incomplete_value": true,
      "site": "004ad0c8",
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
      "004ad0f8",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ad108",
      "DATA",
      [
        "storage",
        "00c65f48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad16c",
      "DATA",
      [
        "storage",
        "002cf528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ad0f8",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ad108",
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad16c",
      "DATA",
      [
        "storage",
        "002cf568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad0b8) · [`004ad0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad0f4) · [`004ad124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad124)
- 新版 `004ad0f8`（命令位置の公開資料なし） · `004ad134`（命令位置の公開資料なし） · `004ad164`（命令位置の公開資料なし）

~~~diff
- 004ad0b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 004ad0b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ad0f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 004ad0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ad0b8 bytes 08dd44f9
+ 004ad0f8 bytes 08dd46f9
- 004ad0f4 ["INT_ADD", "register:40f0:8", ["const:4ad0f4:8", "const:4:8"]]
- 004ad0f4 ["CALL", null, ["callee:0043bb20:8"]]
+ 004ad134 ["INT_ADD", "register:40f0:8", ["const:4ad134:8", "const:4:8"]]
+ 004ad134 ["CALL", null, ["callee:0043bb20:8"]]
- 004ad0f4 bytes 7b3afe97
+ 004ad134 bytes 7b3afe97
- 004ad124 ["COPY", "tmp:0:8", ["const:528:8"]]
- 004ad124 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004ad124 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004ad124 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004ad164 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 004ad164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004ad164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004ad164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004ad124 bytes 4aa11491
+ 004ad164 bytes 4aa11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c011b5899c519e559e5d3027ad3a5b63"></a>

### [`004ad180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md) → [`004ad1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md) _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58570.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58970.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad2d4",
      "incomplete_value": false,
      "site": "004ad2dc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad294",
      "incomplete_value": false,
      "site": "004ad29c",
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
            "const:f3b:8"
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
      "definition_site": "004ad30c",
      "incomplete_value": true,
      "site": "004ad318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad2cc",
      "incomplete_value": true,
      "site": "004ad2d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "definition_site": "004ad308",
      "incomplete_value": false,
      "site": "004ad318",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ad2c8",
      "incomplete_value": false,
      "site": "004ad2d8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ad2d4",
      "PARAM",
      [
        "storage",
        "002a1f3b",
        null,
        "string"
      ]
    ],
    [
      "004ad308",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ad30c",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad2d4",
      "PARAM",
      [
        "storage",
        "002a2008",
        null,
        "string"
      ]
    ],
    [
      "004ad308",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ad30c",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad29c) · [`004ad2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad2d8) · [`004ad2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad2f8)
- 新版 `004ad2dc`（命令位置の公開資料なし） · `004ad318`（命令位置の公開資料なし） · `004ad338`（命令位置の公開資料なし）

~~~diff
- 004ad29c ["INT_ADD", "register:40f0:8", ["const:4ad29c:8", "const:4:8"]]
- 004ad29c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ad2dc ["INT_ADD", "register:40f0:8", ["const:4ad2dc:8", "const:4:8"]]
+ 004ad2dc ["CALL", null, ["callee:0043ddd8:8"]]
- 004ad29c bytes bf42fe97
+ 004ad2dc bytes bf42fe97
- 004ad2d8 ["INT_ADD", "register:40f0:8", ["const:4ad2d8:8", "const:4:8"]]
- 004ad2d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ad318 ["INT_ADD", "register:40f0:8", ["const:4ad318:8", "const:4:8"]]
+ 004ad318 ["CALL", null, ["callee:00c57f10:8"]]
- 004ad2d8 bytes 0eaa1e94
+ 004ad318 bytes feaa1e94
- 004ad2f8 ["INT_ADD", "register:40f0:8", ["const:4ad2f8:8", "const:4:8"]]
- 004ad2f8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ad338 ["INT_ADD", "register:40f0:8", ["const:4ad338:8", "const:4:8"]]
+ 004ad338 ["CALL", null, ["callee:0043ddd8:8"]]
- 004ad2f8 bytes a842fe97
+ 004ad338 bytes a842fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6383a471f1a316f64def578250e82f31"></a>

### [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md) → [`004ad4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) · 呼出先 8件 [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) [`004b2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) · 呼出先 8件 [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad570",
      "incomplete_value": true,
      "site": "004ad570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad530",
      "incomplete_value": true,
      "site": "004ad530",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad5f8",
      "incomplete_value": true,
      "site": "004ad5f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad5b8",
      "incomplete_value": true,
      "site": "004ad5b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad6e4",
      "incomplete_value": true,
      "site": "004ad6e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad6a4",
      "incomplete_value": true,
      "site": "004ad6a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "004ad560",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ad5e8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ad6d4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad560",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ad5e8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ad6d4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad530) · [`004ad5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad5b8) · [`004ad6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad6a4)
- 新版 `004ad570`（命令位置の公開資料なし） · `004ad5f8`（命令位置の公開資料なし） · `004ad6e4`（命令位置の公開資料なし）

~~~diff
- 004ad530 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad530 ["INT_ADD", "register:40f0:8", ["const:4ad530:8", "const:4:8"]]
- 004ad530 ["CALLIND", null, ["register:0:8"]]
+ 004ad570 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad570 ["INT_ADD", "register:40f0:8", ["const:4ad570:8", "const:4:8"]]
+ 004ad570 ["CALLIND", null, ["register:0:8"]]
- 004ad530 bytes 20013fd6
+ 004ad570 bytes 20013fd6
- 004ad5b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad5b8 ["INT_ADD", "register:40f0:8", ["const:4ad5b8:8", "const:4:8"]]
- 004ad5b8 ["CALLIND", null, ["register:0:8"]]
+ 004ad5f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad5f8 ["INT_ADD", "register:40f0:8", ["const:4ad5f8:8", "const:4:8"]]
+ 004ad5f8 ["CALLIND", null, ["register:0:8"]]
- 004ad5b8 bytes 20013fd6
+ 004ad5f8 bytes 20013fd6
- 004ad6a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad6a4 ["INT_ADD", "register:40f0:8", ["const:4ad6a4:8", "const:4:8"]]
- 004ad6a4 ["CALLIND", null, ["register:0:8"]]
+ 004ad6e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad6e4 ["INT_ADD", "register:40f0:8", ["const:4ad6e4:8", "const:4:8"]]
+ 004ad6e4 ["CALLIND", null, ["register:0:8"]]
- 004ad6a4 bytes 20013fd6
+ 004ad6e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753072f82e6293355ad862445905fa3c"></a>

### [`004ad96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md) → [`004ad9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md) _ZN5Botan12ucs2_to_utf8EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58580.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58980.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ada38",
      "incomplete_value": false,
      "site": "004ada40",
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
            "const:2c2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad9f8",
      "incomplete_value": false,
      "site": "004ada00",
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
            "const:282:8"
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
      "definition_site": "004ada70",
      "incomplete_value": true,
      "site": "004ada7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ada30",
      "incomplete_value": true,
      "site": "004ada3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "definition_site": "004ada6c",
      "incomplete_value": false,
      "site": "004ada7c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ada2c",
      "incomplete_value": false,
      "site": "004ada3c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004ada38",
      "PARAM",
      [
        "storage",
        "002ba282",
        null,
        "string"
      ]
    ],
    [
      "004ada6c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ada70",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ada38",
      "PARAM",
      [
        "storage",
        "002ba2c2",
        null,
        "string"
      ]
    ],
    [
      "004ada6c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ada70",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ada00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ada00) · [`004ada3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ada3c) · [`004ad9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ad9b8)
- 新版 `004ada40`（命令位置の公開資料なし） · `004ada7c`（命令位置の公開資料なし） · `004ad9f8`（命令位置の公開資料なし）

~~~diff
- 004ada00 ["INT_ADD", "register:40f0:8", ["const:4ada00:8", "const:4:8"]]
- 004ada00 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ada40 ["INT_ADD", "register:40f0:8", ["const:4ada40:8", "const:4:8"]]
+ 004ada40 ["CALL", null, ["callee:0043ddd8:8"]]
- 004ada00 bytes e640fe97
+ 004ada40 bytes e640fe97
- 004ada3c ["INT_ADD", "register:40f0:8", ["const:4ada3c:8", "const:4:8"]]
- 004ada3c ["CALL", null, ["callee:00c57f10:8"]]
+ 004ada7c ["INT_ADD", "register:40f0:8", ["const:4ada7c:8", "const:4:8"]]
+ 004ada7c ["CALL", null, ["callee:00c57f10:8"]]
- 004ada3c bytes 35a81e94
+ 004ada7c bytes 25a91e94
- 004ad9b8 ["INT_ADD", "register:40f0:8", ["const:4ad9b8:8", "const:4:8"]]
- 004ad9b8 ["CALL", null, ["callee:004f9210:8"]]
+ 004ad9f8 ["INT_ADD", "register:40f0:8", ["const:4ad9f8:8", "const:4:8"]]
+ 004ad9f8 ["CALL", null, ["callee:004f9210:8"]]
- 004ad9b8 bytes 062e0194
+ 004ad9f8 bytes 062e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-707978949e1986a4b8b6fea9bcc2bfff"></a>

### [`004adaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md) → [`004adae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md) _ZN5Botan12ucs4_to_utf8EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58590.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58990.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004adb70",
      "incomplete_value": false,
      "site": "004adb78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004adb30",
      "incomplete_value": false,
      "site": "004adb38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:e5:8"
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
      "definition_site": "004adba8",
      "incomplete_value": true,
      "site": "004adbb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004adb68",
      "incomplete_value": true,
      "site": "004adb74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "definition_site": "004adba4",
      "incomplete_value": false,
      "site": "004adbb4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004adb64",
      "incomplete_value": false,
      "site": "004adb74",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004adb70",
      "PARAM",
      [
        "storage",
        "002a40e5",
        null,
        "string"
      ]
    ],
    [
      "004adba4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004adba8",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004adb70",
      "PARAM",
      [
        "storage",
        "002a41b2",
        null,
        "string"
      ]
    ],
    [
      "004adba4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004adba8",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adb38) · [`004adb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adb74) · [`004adaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adaf0)
- 新版 `004adb78`（命令位置の公開資料なし） · `004adbb4`（命令位置の公開資料なし） · `004adb30`（命令位置の公開資料なし）

~~~diff
- 004adb38 ["INT_ADD", "register:40f0:8", ["const:4adb38:8", "const:4:8"]]
- 004adb38 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004adb78 ["INT_ADD", "register:40f0:8", ["const:4adb78:8", "const:4:8"]]
+ 004adb78 ["CALL", null, ["callee:0043ddd8:8"]]
- 004adb38 bytes 9840fe97
+ 004adb78 bytes 9840fe97
- 004adb74 ["INT_ADD", "register:40f0:8", ["const:4adb74:8", "const:4:8"]]
- 004adb74 ["CALL", null, ["callee:00c57f10:8"]]
+ 004adbb4 ["INT_ADD", "register:40f0:8", ["const:4adbb4:8", "const:4:8"]]
+ 004adbb4 ["CALL", null, ["callee:00c57f10:8"]]
- 004adb74 bytes e7a71e94
+ 004adbb4 bytes d7a81e94
- 004adaf0 ["INT_ADD", "register:40f0:8", ["const:4adaf0:8", "const:4:8"]]
- 004adaf0 ["CALL", null, ["callee:004f9210:8"]]
+ 004adb30 ["INT_ADD", "register:40f0:8", ["const:4adb30:8", "const:4:8"]]
+ 004adb30 ["CALL", null, ["callee:004f9210:8"]]
- 004adaf0 bytes b82d0194
+ 004adb30 bytes b82d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1597f25c2a73a9353a32cbc40eb5d8"></a>

### [`004adbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md) → [`004adc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md) _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59670.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585a0.md) [`00c585b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585b0.md)
- 新版 呼出元 1件 [`00c59a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a70.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589a0.md) [`00c589b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004adc48",
      "incomplete_value": true,
      "site": "004adc48",
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
      "definition_site": "004adc08",
      "incomplete_value": true,
      "site": "004adc08",
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
      "004adc38",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "004adc48",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004adc38",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "004adc48",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adbf8) · [`004adc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adc1c) · [`004adc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adc2c)
- 新版 `004adc38`（命令位置の公開資料なし） · `004adc5c`（命令位置の公開資料なし） · `004adc6c`（命令位置の公開資料なし）

~~~diff
- 004adbf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
- 004adbf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004adc38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
+ 004adc38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004adbf8 bytes 08d944f9
+ 004adc38 bytes 08d946f9
- 004adc1c ["INT_ADD", "register:40f0:8", ["const:4adc1c:8", "const:4:8"]]
- 004adc1c ["CALL", null, ["callee:00c589a0:8"]]
+ 004adc5c ["INT_ADD", "register:40f0:8", ["const:4adc5c:8", "const:4:8"]]
+ 004adc5c ["CALL", null, ["callee:00c589a0:8"]]
- 004adc1c bytes 61aa1e94
+ 004adc5c bytes 51ab1e94
- 004adc2c ["INT_ADD", "register:40f0:8", ["const:4adc2c:8", "const:4:8"]]
- 004adc2c ["CALL", null, ["callee:00c589b0:8"]]
+ 004adc6c ["INT_ADD", "register:40f0:8", ["const:4adc6c:8", "const:4:8"]]
+ 004adc6c ["CALL", null, ["callee:00c589b0:8"]]
- 004adc2c bytes 61aa1e94
+ 004adc6c bytes 51ab1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3b3646380ec27fbe4729104d7f8fba"></a>

### [`004add24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md) → [`004add64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md) _ZN5Botan9X509_Time6set_toERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585c0.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c589c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589c0.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件

アドレスに依存する影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ae2e4",
      "incomplete_value": true,
      "site": "004ae2e8",
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
      "definition_site": "004ae2a4",
      "incomplete_value": true,
      "site": "004ae2a8",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ade14",
      "incomplete_value": false,
      "site": "004ade20",
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
            "const:b15:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004addd4",
      "incomplete_value": false,
      "site": "004adde0",
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
            "const:a48:8"
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
      "definition_site": "004ade28",
      "incomplete_value": false,
      "site": "004ade30",
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
            "const:48c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004adde8",
      "incomplete_value": false,
      "site": "004addf0",
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
      "004ade14",
      "PARAM",
      [
        "storage",
        "002a8a48",
        null,
        "string"
      ]
    ],
    [
      "004ade28",
      "PARAM",
      [
        "storage",
        "002a63b0",
        null,
        null
      ]
    ],
    [
      "004ade74",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ade14",
      "PARAM",
      [
        "storage",
        "002a8b15",
        null,
        "string"
      ]
    ],
    [
      "004ade28",
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ],
    [
      "004ade74",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004adde0) · [`004addf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004addf0) · [`004ade44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004ade44)
- 新版 `004ade20`（命令位置の公開資料なし） · `004ade30`（命令位置の公開資料なし） · `004ade84`（命令位置の公開資料なし）

~~~diff
- 004adde0 ["INT_ADD", "register:40f0:8", ["const:4adde0:8", "const:4:8"]]
- 004adde0 ["CALL", null, ["callee:00c580b0:8"]]
+ 004ade20 ["INT_ADD", "register:40f0:8", ["const:4ade20:8", "const:4:8"]]
+ 004ade20 ["CALL", null, ["callee:00c580b0:8"]]
- 004adde0 bytes b4a71e94
+ 004ade20 bytes a4a81e94
- 004addf0 ["INT_ADD", "register:40f0:8", ["const:4addf0:8", "const:4:8"]]
- 004addf0 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ade30 ["INT_ADD", "register:40f0:8", ["const:4ade30:8", "const:4:8"]]
+ 004ade30 ["CALL", null, ["callee:00c57f70:8"]]
- 004addf0 bytes 60a71e94
+ 004ade30 bytes 50a81e94
- 004ade44 ["INT_ADD", "register:40f0:8", ["const:4ade44:8", "const:4:8"]]
- 004ade44 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ade84 ["INT_ADD", "register:40f0:8", ["const:4ade84:8", "const:4:8"]]
+ 004ade84 ["CALL", null, ["callee:00c57f10:8"]]
- 004ade44 bytes 33a71e94
+ 004ade84 bytes 23a81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fdeb5ab57e31f20ba277dd2022d4984"></a>

### [`004ae544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md) → [`004ae584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md) _ZNK5Botan9X509_Time11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ae630",
      "incomplete_value": false,
      "site": "004ae638",
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
            "const:2e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae5f0",
      "incomplete_value": false,
      "site": "004ae5f8",
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
            "const:f61:8"
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
      "definition_site": "004ae668",
      "incomplete_value": true,
      "site": "004ae674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae628",
      "incomplete_value": true,
      "site": "004ae634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ae664",
      "incomplete_value": false,
      "site": "004ae674",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ae624",
      "incomplete_value": false,
      "site": "004ae634",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ae630",
      "PARAM",
      [
        "storage",
        "002a2f61",
        null,
        "string"
      ]
    ],
    [
      "004ae664",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ae668",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ae630",
      "PARAM",
      [
        "storage",
        "002a302e",
        null,
        "string"
      ]
    ],
    [
      "004ae664",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ae668",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae5b8) · [`004ae5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae5f8) · [`004ae634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae634)
- 新版 `004ae5f8`（命令位置の公開資料なし） · `004ae638`（命令位置の公開資料なし） · `004ae674`（命令位置の公開資料なし）

~~~diff
- 004ae5b8 ["INT_ADD", "register:40f0:8", ["const:4ae5b8:8", "const:4:8"]]
- 004ae5b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ae5f8 ["INT_ADD", "register:40f0:8", ["const:4ae5f8:8", "const:4:8"]]
+ 004ae5f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ae5b8 bytes 3ea51e94
+ 004ae5f8 bytes 2ea61e94
- 004ae5f8 ["INT_ADD", "register:40f0:8", ["const:4ae5f8:8", "const:4:8"]]
- 004ae5f8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ae638 ["INT_ADD", "register:40f0:8", ["const:4ae638:8", "const:4:8"]]
+ 004ae638 ["CALL", null, ["callee:0043ddd8:8"]]
- 004ae5f8 bytes e83dfe97
+ 004ae638 bytes e83dfe97
- 004ae634 ["INT_ADD", "register:40f0:8", ["const:4ae634:8", "const:4:8"]]
- 004ae634 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ae674 ["INT_ADD", "register:40f0:8", ["const:4ae674:8", "const:4:8"]]
+ 004ae674 ["CALL", null, ["callee:00c57f10:8"]]
- 004ae634 bytes 37a51e94
+ 004ae674 bytes 27a61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af1a1e5af66050cb3f3c7f866baaf4b"></a>

### [`004ae69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md) → [`004ae6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) _ZNK5Botan9X509_Time9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585d0.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c589d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589d0.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

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
      "definition_site": "004ae79c",
      "incomplete_value": false,
      "site": "004ae7a4",
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
            "const:9cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae75c",
      "incomplete_value": false,
      "site": "004ae764",
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
            "const:98f:8"
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
      "definition_site": "004ae890",
      "incomplete_value": false,
      "site": "004ae898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:865:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae850",
      "incomplete_value": false,
      "site": "004ae858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:825:8"
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
      "definition_site": "004ae8c8",
      "incomplete_value": true,
      "site": "004ae8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae888",
      "incomplete_value": true,
      "site": "004ae894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "004ae79c",
      "PARAM",
      [
        "storage",
        "002b198f",
        null,
        null
      ]
    ],
    [
      "004ae83c",
      "PARAM",
      [
        "storage",
        "002b803b",
        null,
        null
      ]
    ],
    [
      "004ae890",
      "PARAM",
      [
        "storage",
        "002af825",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ae79c",
      "PARAM",
      [
        "storage",
        "002b19cf",
        null,
        null
      ]
    ],
    [
      "004ae83c",
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ],
    [
      "004ae890",
      "PARAM",
      [
        "storage",
        "002af865",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae764) · [`004ae858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae858) · [`004ae884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae884)
- 新版 `004ae7a4`（命令位置の公開資料なし） · `004ae898`（命令位置の公開資料なし） · `004ae8c4`（命令位置の公開資料なし）

~~~diff
- 004ae764 ["INT_ADD", "register:40f0:8", ["const:4ae764:8", "const:4:8"]]
- 004ae764 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ae7a4 ["INT_ADD", "register:40f0:8", ["const:4ae7a4:8", "const:4:8"]]
+ 004ae7a4 ["CALL", null, ["callee:00c57f70:8"]]
- 004ae764 bytes 03a51e94
+ 004ae7a4 bytes f3a51e94
- 004ae858 ["INT_ADD", "register:40f0:8", ["const:4ae858:8", "const:4:8"]]
- 004ae858 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ae898 ["INT_ADD", "register:40f0:8", ["const:4ae898:8", "const:4:8"]]
+ 004ae898 ["CALL", null, ["callee:0043ddd8:8"]]
- 004ae858 bytes 503dfe97
+ 004ae898 bytes 503dfe97
- 004ae884 ["COPY", "register:4010:8", ["const:535828:8"]]
+ 004ae8c4 ["COPY", "register:4010:8", ["const:535868:8"]]
- 004ae884 bytes 227d4310
+ 004ae8c4 bytes 227d4310
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6011e5d4979ad30317d720be1f3fb48"></a>

### [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) → [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) FUN_004aec64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 29件 [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) [`004a5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md) [`004ac1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md) [`004ae69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md) [`004aec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 29件 [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) [`004a5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) [`004ac1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) [`004ae6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) [`004aecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004aec80",
      "incomplete_value": true,
      "site": "004aec80",
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
      "definition_site": "004aec40",
      "incomplete_value": true,
      "site": "004aec40",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004aecb4",
      "incomplete_value": true,
      "site": "004aecb8",
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
      "definition_site": "004aec74",
      "incomplete_value": true,
      "site": "004aec78",
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
      "004aec78",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004aec80",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aecb0",
      "READ",
      [
        "storage",
        "00c9a9d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aec78",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004aec80",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aecb0",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aec38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec38) · [`004aec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec68) · [`004aec70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec70)
- 新版 `004aec78`（命令位置の公開資料なし） · `004aeca8`（命令位置の公開資料なし） · `004aecb0`（命令位置の公開資料なし）

~~~diff
- 004aec38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004aec38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aec78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004aec78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004aec38 bytes 08e944f9
+ 004aec78 bytes 08e946f9
- 004aec68 ["INT_ADD", "register:40f0:8", ["const:4aec68:8", "const:4:8"]]
- 004aec68 ["CALL", null, ["callee:0043bb20:8"]]
+ 004aeca8 ["INT_ADD", "register:40f0:8", ["const:4aeca8:8", "const:4:8"]]
+ 004aeca8 ["CALL", null, ["callee:0043bb20:8"]]
- 004aec68 bytes 9e33fe97
+ 004aeca8 bytes 9e33fe97
- 004aec70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
- 004aec70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aecb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 004aecb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004aec70 bytes 08ed44f9
+ 004aecb0 bytes 08ed46f9
~~~


<a id="compare-fada4b6f053ad4920b6b439a92198fd4"></a>

### [`004aec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md) → [`004aecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) _ZNK5Botan9X509_Time3cmpERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aedc0",
      "incomplete_value": false,
      "site": "004aedc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aed80",
      "incomplete_value": false,
      "site": "004aed88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e02:8"
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
      "definition_site": "004aedfc",
      "incomplete_value": true,
      "site": "004aee08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aedbc",
      "incomplete_value": true,
      "site": "004aedc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
              ]
            ]
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
      "definition_site": "004aedf8",
      "incomplete_value": false,
      "site": "004aee08",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004aedb8",
      "incomplete_value": false,
      "site": "004aedc8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004aedc0",
      "PARAM",
      [
        "storage",
        "002b8e02",
        null,
        "string"
      ]
    ],
    [
      "004aedf8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004aedfc",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aedc0",
      "PARAM",
      [
        "storage",
        "002b8e42",
        null,
        "string"
      ]
    ],
    [
      "004aedf8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004aedfc",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aed88) · [`004aedc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aedc8) · [`004aed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aed74)
- 新版 `004aedc8`（命令位置の公開資料なし） · `004aee08`（命令位置の公開資料なし） · `004aedb4`（命令位置の公開資料なし）

~~~diff
- 004aed88 ["INT_ADD", "register:40f0:8", ["const:4aed88:8", "const:4:8"]]
- 004aed88 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004aedc8 ["INT_ADD", "register:40f0:8", ["const:4aedc8:8", "const:4:8"]]
+ 004aedc8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004aed88 bytes 043cfe97
+ 004aedc8 bytes 043cfe97
- 004aedc8 ["INT_ADD", "register:40f0:8", ["const:4aedc8:8", "const:4:8"]]
- 004aedc8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004aee08 ["INT_ADD", "register:40f0:8", ["const:4aee08:8", "const:4:8"]]
+ 004aee08 ["CALL", null, ["callee:00c57f10:8"]]
- 004aedc8 bytes 52a31e94
+ 004aee08 bytes 42a41e94
- 004aed74 ["INT_ADD", "register:40f0:8", ["const:4aed74:8", "const:4:8"]]
- 004aed74 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004aedb4 ["INT_ADD", "register:40f0:8", ["const:4aedb4:8", "const:4:8"]]
+ 004aedb4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004aed74 bytes 5fa31e94
+ 004aedb4 bytes 4fa41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df20f9d54308f16a2e1a5eae1b18e26f"></a>

### [`004aee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md) → [`004aee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00c587f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aef1c",
      "incomplete_value": false,
      "site": "004aef28",
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
            "const:309:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aeedc",
      "incomplete_value": false,
      "site": "004aeee8",
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
            "const:2c9:8"
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
      "definition_site": "004aef5c",
      "incomplete_value": true,
      "site": "004aef68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aef1c",
      "incomplete_value": true,
      "site": "004aef28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "definition_site": "004aef58",
      "incomplete_value": false,
      "site": "004aef68",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004aef18",
      "incomplete_value": false,
      "site": "004aef28",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004aef1c",
      "PARAM",
      [
        "storage",
        "002ba2c9",
        null,
        "string"
      ]
    ],
    [
      "004aef58",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004aef5c",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aef1c",
      "PARAM",
      [
        "storage",
        "002ba309",
        null,
        "string"
      ]
    ],
    [
      "004aef58",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004aef5c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aeee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aeee8) · [`004aef28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aef28) · [`004aef50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aef50)
- 新版 `004aef28`（命令位置の公開資料なし） · `004aef68`（命令位置の公開資料なし） · `004aef90`（命令位置の公開資料なし）

~~~diff
- 004aeee8 ["INT_ADD", "register:40f0:8", ["const:4aeee8:8", "const:4:8"]]
- 004aeee8 ["CALL", null, ["callee:00c580b0:8"]]
+ 004aef28 ["INT_ADD", "register:40f0:8", ["const:4aef28:8", "const:4:8"]]
+ 004aef28 ["CALL", null, ["callee:00c580b0:8"]]
- 004aeee8 bytes 72a31e94
+ 004aef28 bytes 62a41e94
- 004aef28 ["INT_ADD", "register:40f0:8", ["const:4aef28:8", "const:4:8"]]
- 004aef28 ["CALL", null, ["callee:00c57f10:8"]]
+ 004aef68 ["INT_ADD", "register:40f0:8", ["const:4aef68:8", "const:4:8"]]
+ 004aef68 ["CALL", null, ["callee:00c57f10:8"]]
- 004aef28 bytes faa21e94
+ 004aef68 bytes eaa31e94
- 004aef50 ["INT_ADD", "register:40f0:8", ["const:4aef50:8", "const:4:8"]]
- 004aef50 ["CALL", null, ["callee:00c580b0:8"]]
+ 004aef90 ["INT_ADD", "register:40f0:8", ["const:4aef90:8", "const:4:8"]]
+ 004aef90 ["CALL", null, ["callee:00c580b0:8"]]
- 004aef50 bytes 58a31e94
+ 004aef90 bytes 48a41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6804a2e34d5f1b487c02bb434cb1104"></a>

### [`004af178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md) → [`004af1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md) _ZNK5Botan14calendar_point16to_std_timepointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58600.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a00.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af2e0",
      "incomplete_value": false,
      "site": "004af2e8",
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
            "const:bec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af2a0",
      "incomplete_value": false,
      "site": "004af2a8",
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
            "const:bac:8"
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
      "definition_site": "004af31c",
      "incomplete_value": true,
      "site": "004af328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af2dc",
      "incomplete_value": true,
      "site": "004af2e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
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
      "definition_site": "004af318",
      "incomplete_value": false,
      "site": "004af328",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004af2d8",
      "incomplete_value": false,
      "site": "004af2e8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004af2e0",
      "PARAM",
      [
        "storage",
        "002b0bac",
        null,
        "string"
      ]
    ],
    [
      "004af318",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004af31c",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004af2e0",
      "PARAM",
      [
        "storage",
        "002b0bec",
        null,
        "string"
      ]
    ],
    [
      "004af318",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004af31c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af2a8) · [`004af2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af2e8) · [`004af30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af30c)
- 新版 `004af2e8`（命令位置の公開資料なし） · `004af328`（命令位置の公開資料なし） · `004af34c`（命令位置の公開資料なし）

~~~diff
- 004af2a8 ["INT_ADD", "register:40f0:8", ["const:4af2a8:8", "const:4:8"]]
- 004af2a8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004af2e8 ["INT_ADD", "register:40f0:8", ["const:4af2e8:8", "const:4:8"]]
+ 004af2e8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004af2a8 bytes bc3afe97
+ 004af2e8 bytes bc3afe97
- 004af2e8 ["INT_ADD", "register:40f0:8", ["const:4af2e8:8", "const:4:8"]]
- 004af2e8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004af328 ["INT_ADD", "register:40f0:8", ["const:4af328:8", "const:4:8"]]
+ 004af328 ["CALL", null, ["callee:00c57f10:8"]]
- 004af2e8 bytes 0aa21e94
+ 004af328 bytes faa21e94
- 004af30c ["INT_ADD", "register:40f0:8", ["const:4af30c:8", "const:4:8"]]
- 004af30c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004af34c ["INT_ADD", "register:40f0:8", ["const:4af34c:8", "const:4:8"]]
+ 004af34c ["CALL", null, ["callee:0043ddd8:8"]]
- 004af30c bytes a33afe97
+ 004af34c bytes a33afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aa41589635e0490a6ba3268165789b5"></a>

### [`004af444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md) → [`004af484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md) _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58330.md) · 呼出先 9件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) · 呼出先 9件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.61% / 新版 95.61%

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
      "definition_site": "004af518",
      "incomplete_value": false,
      "site": "004af524",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af4d8",
      "incomplete_value": false,
      "site": "004af4e4",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af544",
      "incomplete_value": false,
      "site": "004af54c",
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
            "const:352:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af504",
      "incomplete_value": false,
      "site": "004af50c",
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
            "const:276:8"
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
      "definition_site": "004af588",
      "incomplete_value": false,
      "site": "004af590",
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
            "const:279:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af548",
      "incomplete_value": false,
      "site": "004af550",
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
            "const:239:8"
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
      "004af518",
      "PARAM",
      [
        "storage",
        "002b19b0",
        null,
        "string"
      ]
    ],
    [
      "004af544",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004af588",
      "PARAM",
      [
        "storage",
        "002bb239",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004af518",
      "PARAM",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      "004af544",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      "004af588",
      "PARAM",
      [
        "storage",
        "002bb279",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af4e4) · [`004af50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af50c) · [`004af550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af550)
- 新版 `004af524`（命令位置の公開資料なし） · `004af54c`（命令位置の公開資料なし） · `004af590`（命令位置の公開資料なし）

~~~diff
- 004af4e4 ["INT_ADD", "register:40f0:8", ["const:4af4e4:8", "const:4:8"]]
- 004af4e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004af524 ["INT_ADD", "register:40f0:8", ["const:4af524:8", "const:4:8"]]
+ 004af524 ["CALL", null, ["callee:00c57f60:8"]]
- 004af4e4 bytes 9fa11e94
+ 004af524 bytes 8fa21e94
- 004af50c ["INT_ADD", "register:40f0:8", ["const:4af50c:8", "const:4:8"]]
- 004af50c ["CALL", null, ["callee:00c57f70:8"]]
+ 004af54c ["INT_ADD", "register:40f0:8", ["const:4af54c:8", "const:4:8"]]
+ 004af54c ["CALL", null, ["callee:00c57f70:8"]]
- 004af50c bytes 99a11e94
+ 004af54c bytes 89a21e94
- 004af550 ["INT_ADD", "register:40f0:8", ["const:4af550:8", "const:4:8"]]
- 004af550 ["CALL", null, ["callee:00c57f70:8"]]
+ 004af590 ["INT_ADD", "register:40f0:8", ["const:4af590:8", "const:4:8"]]
+ 004af590 ["CALL", null, ["callee:00c57f70:8"]]
- 004af550 bytes 88a11e94
+ 004af590 bytes 78a21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc25b633d0905a5f989232684bbd94f"></a>

### [`004af854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md) → [`004af894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md) _ZN5Botan11BER_Decoder10verify_endEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a20.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af918",
      "incomplete_value": false,
      "site": "004af920",
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
            "const:e76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af8d8",
      "incomplete_value": false,
      "site": "004af8e0",
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
            "const:da9:8"
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
      "definition_site": "004af954",
      "incomplete_value": true,
      "site": "004af960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af914",
      "incomplete_value": true,
      "site": "004af920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
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
      "definition_site": "004af950",
      "incomplete_value": false,
      "site": "004af960",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004af910",
      "incomplete_value": false,
      "site": "004af920",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004af918",
      "PARAM",
      [
        "storage",
        "0029eda9",
        null,
        "string"
      ]
    ],
    [
      "004af950",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004af954",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004af918",
      "PARAM",
      [
        "storage",
        "0029ee76",
        null,
        "string"
      ]
    ],
    [
      "004af950",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004af954",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af8e0) · [`004af920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af920) · [`004af884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af884)
- 新版 `004af920`（命令位置の公開資料なし） · `004af960`（命令位置の公開資料なし） · `004af8c4`（命令位置の公開資料なし）

~~~diff
- 004af8e0 ["INT_ADD", "register:40f0:8", ["const:4af8e0:8", "const:4:8"]]
- 004af8e0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004af920 ["INT_ADD", "register:40f0:8", ["const:4af920:8", "const:4:8"]]
+ 004af920 ["CALL", null, ["callee:0043ddd8:8"]]
- 004af8e0 bytes 2e39fe97
+ 004af920 bytes 2e39fe97
- 004af920 ["INT_ADD", "register:40f0:8", ["const:4af920:8", "const:4:8"]]
- 004af920 ["CALL", null, ["callee:00c57f10:8"]]
+ 004af960 ["INT_ADD", "register:40f0:8", ["const:4af960:8", "const:4:8"]]
+ 004af960 ["CALL", null, ["callee:00c57f10:8"]]
- 004af920 bytes 7ca01e94
+ 004af960 bytes 6ca11e94
- 004af884 ["COPY", "register:0:8", ["register:4040:8"]]
- 004af884 ["INT_ADD", "register:40f0:8", ["const:4af884:8", "const:4:8"]]
- 004af884 ["CALLIND", null, ["register:0:8"]]
+ 004af8c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af8c4 ["INT_ADD", "register:40f0:8", ["const:4af8c4:8", "const:4:8"]]
+ 004af8c4 ["CALLIND", null, ["register:0:8"]]
- 004af884 bytes 00013fd6
+ 004af8c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16a743282fc3bd80937e9c00e77daacf"></a>

### [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) → [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) FUN_004afa18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004afb20",
      "incomplete_value": false,
      "site": "004afb28",
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
            "const:243:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afae0",
      "incomplete_value": false,
      "site": "004afae8",
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
            "const:176:8"
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
      "definition_site": "004afb58",
      "incomplete_value": true,
      "site": "004afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afb18",
      "incomplete_value": true,
      "site": "004afb24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "definition_site": "004afb54",
      "incomplete_value": false,
      "site": "004afb64",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004afb14",
      "incomplete_value": false,
      "site": "004afb24",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004afb20",
      "PARAM",
      [
        "storage",
        "002a1176",
        null,
        "string"
      ]
    ],
    [
      "004afb54",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004afb58",
      "READ",
      [
        "storage",
        "00c9a9a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004afb20",
      "PARAM",
      [
        "storage",
        "002a1243",
        null,
        "string"
      ]
    ],
    [
      "004afb54",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004afb58",
      "READ",
      [
        "storage",
        "00c9ada8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004afae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afae8) · [`004afb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afb24) · [`004afb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afb44)
- 新版 `004afb28`（命令位置の公開資料なし） · `004afb64`（命令位置の公開資料なし） · `004afb84`（命令位置の公開資料なし）

~~~diff
- 004afae8 ["INT_ADD", "register:40f0:8", ["const:4afae8:8", "const:4:8"]]
- 004afae8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004afb28 ["INT_ADD", "register:40f0:8", ["const:4afb28:8", "const:4:8"]]
+ 004afb28 ["CALL", null, ["callee:0043ddd8:8"]]
- 004afae8 bytes ac38fe97
+ 004afb28 bytes ac38fe97
- 004afb24 ["INT_ADD", "register:40f0:8", ["const:4afb24:8", "const:4:8"]]
- 004afb24 ["CALL", null, ["callee:00c57f10:8"]]
+ 004afb64 ["INT_ADD", "register:40f0:8", ["const:4afb64:8", "const:4:8"]]
+ 004afb64 ["CALL", null, ["callee:00c57f10:8"]]
- 004afb24 bytes fb9f1e94
+ 004afb64 bytes eba01e94
- 004afb44 ["INT_ADD", "register:40f0:8", ["const:4afb44:8", "const:4:8"]]
- 004afb44 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004afb84 ["INT_ADD", "register:40f0:8", ["const:4afb84:8", "const:4:8"]]
+ 004afb84 ["CALL", null, ["callee:0043ddd8:8"]]
- 004afb44 bytes 9538fe97
+ 004afb84 bytes 9538fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-befe03a1ec64b32eff320b623a19afd0"></a>

### [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) → [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) FUN_004afc10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 18件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) [`004f99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f99e0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 2件 [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`004f9a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004afdb0",
      "incomplete_value": true,
      "site": "004afdb0",
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
      "definition_site": "004afd70",
      "incomplete_value": true,
      "site": "004afd70",
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004afe98",
      "incomplete_value": true,
      "site": "004afe98",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afe58",
      "incomplete_value": true,
      "site": "004afe58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004afec4",
      "incomplete_value": true,
      "site": "004afec4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afe84",
      "incomplete_value": true,
      "site": "004afe84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
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
      "004afda0",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004afdb0",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afe34",
      "READ",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004afda0",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004afdb0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afe34",
      "READ",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004afe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afe58) · [`004afe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afe84) · [`004afeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afeb0)
- 新版 `004afe98`（命令位置の公開資料なし） · `004afec4`（命令位置の公開資料なし） · `004afef0`（命令位置の公開資料なし）

~~~diff
- 004afe58 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afe58 ["INT_ADD", "register:40f0:8", ["const:4afe58:8", "const:4:8"]]
- 004afe58 ["CALLIND", null, ["register:0:8"]]
+ 004afe98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afe98 ["INT_ADD", "register:40f0:8", ["const:4afe98:8", "const:4:8"]]
+ 004afe98 ["CALLIND", null, ["register:0:8"]]
- 004afe58 bytes 20013fd6
+ 004afe98 bytes 20013fd6
- 004afe84 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afe84 ["INT_ADD", "register:40f0:8", ["const:4afe84:8", "const:4:8"]]
- 004afe84 ["CALLIND", null, ["register:0:8"]]
+ 004afec4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afec4 ["INT_ADD", "register:40f0:8", ["const:4afec4:8", "const:4:8"]]
+ 004afec4 ["CALLIND", null, ["register:0:8"]]
- 004afe84 bytes 20013fd6
+ 004afec4 bytes 20013fd6
- 004afeb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afeb0 ["INT_ADD", "register:40f0:8", ["const:4afeb0:8", "const:4:8"]]
- 004afeb0 ["CALLIND", null, ["register:0:8"]]
+ 004afef0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afef0 ["INT_ADD", "register:40f0:8", ["const:4afef0:8", "const:4:8"]]
+ 004afef0 ["CALLIND", null, ["register:0:8"]]
- 004afeb0 bytes 20013fd6
+ 004afef0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e6d1fbf3de3dc033d8aafc802980f06"></a>

### [`004b03b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md) → [`004b03f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58660.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a60.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b04a4",
      "incomplete_value": false,
      "site": "004b04ac",
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
            "const:a8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0464",
      "incomplete_value": false,
      "site": "004b046c",
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
            "const:9be:8"
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
      "definition_site": "004b04e0",
      "incomplete_value": true,
      "site": "004b04ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b04a0",
      "incomplete_value": true,
      "site": "004b04ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
              ]
            ]
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
      "definition_site": "004b04dc",
      "incomplete_value": false,
      "site": "004b04ec",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b049c",
      "incomplete_value": false,
      "site": "004b04ac",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b04a4",
      "PARAM",
      [
        "storage",
        "002a99be",
        null,
        "string"
      ]
    ],
    [
      "004b04dc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b04e0",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b04a4",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        "string"
      ]
    ],
    [
      "004b04dc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b04e0",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b046c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b046c) · [`004b04ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b04ac) · [`004b0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b0458)
- 新版 `004b04ac`（命令位置の公開資料なし） · `004b04ec`（命令位置の公開資料なし） · `004b0498`（命令位置の公開資料なし）

~~~diff
- 004b046c ["INT_ADD", "register:40f0:8", ["const:4b046c:8", "const:4:8"]]
- 004b046c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b04ac ["INT_ADD", "register:40f0:8", ["const:4b04ac:8", "const:4:8"]]
+ 004b04ac ["CALL", null, ["callee:0043ddd8:8"]]
- 004b046c bytes 4b36fe97
+ 004b04ac bytes 4b36fe97
- 004b04ac ["INT_ADD", "register:40f0:8", ["const:4b04ac:8", "const:4:8"]]
- 004b04ac ["CALL", null, ["callee:00c57f10:8"]]
+ 004b04ec ["INT_ADD", "register:40f0:8", ["const:4b04ec:8", "const:4:8"]]
+ 004b04ec ["CALL", null, ["callee:00c57f10:8"]]
- 004b04ac bytes 999d1e94
+ 004b04ec bytes 899e1e94
- 004b0458 ["INT_ADD", "register:40f0:8", ["const:4b0458:8", "const:4:8"]]
- 004b0458 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b0498 ["INT_ADD", "register:40f0:8", ["const:4b0498:8", "const:4:8"]]
+ 004b0498 ["CALL", null, ["callee:00c57ef0:8"]]
- 004b0458 bytes a69d1e94
+ 004b0498 bytes 969e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed93ffb92ffd82350369b7c03c8eaad1"></a>

### [`004b051c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md) → [`004b055c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b055c.md) _ZN5Botan11BER_DecoderC1EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58340.md) · 呼出先 2件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c58740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58740.md) · 呼出先 2件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b059c",
      "incomplete_value": true,
      "site": "004b05a0",
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
      "definition_site": "004b055c",
      "incomplete_value": true,
      "site": "004b0560",
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
      "004b0594",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b05a0",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b0594",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b05a0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md#insn-004b0558) · [`004b0548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md#insn-004b0548)
- 新版 `004b0598`（命令位置の公開資料なし） · `004b0588`（命令位置の公開資料なし）

~~~diff
- 004b0558 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0558 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0558 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0558 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0558 bytes 1f7c01a9
+ 004b0598 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0598 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0598 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0598 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0598 bytes 1f7c01a9
- 004b0548 ["INT_ADD", "register:40f0:8", ["const:4b0548:8", "const:4:8"]]
- 004b0548 ["CALL", null, ["callee:00c57e90:8"]]
+ 004b0588 ["INT_ADD", "register:40f0:8", ["const:4b0588:8", "const:4:8"]]
+ 004b0588 ["CALL", null, ["callee:00c57e90:8"]]
- 004b0548 bytes 529d1e94
+ 004b0588 bytes 429e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec4f935767be9b3a0b440d5cfdf8fdc"></a>

### [`004b05f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md) → [`004b0638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0638.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58490.md) · 呼出先 2件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c58890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58890.md) · 呼出先 2件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b0678",
      "incomplete_value": true,
      "site": "004b067c",
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
      "definition_site": "004b0638",
      "incomplete_value": true,
      "site": "004b063c",
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
      "004b066c",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b067c",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b066c",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b067c",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md#insn-004b0634) · [`004b0620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md#insn-004b0620)
- 新版 `004b0674`（命令位置の公開資料なし） · `004b0660`（命令位置の公開資料なし）

~~~diff
- 004b0634 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0634 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0634 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0634 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0634 bytes 1f7c01a9
+ 004b0674 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0674 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0674 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0674 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0674 bytes 1f7c01a9
- 004b0620 ["INT_ADD", "register:40f0:8", ["const:4b0620:8", "const:4:8"]]
- 004b0620 ["CALL", null, ["callee:00c57e90:8"]]
+ 004b0660 ["INT_ADD", "register:40f0:8", ["const:4b0660:8", "const:4:8"]]
+ 004b0660 ["CALL", null, ["callee:00c57e90:8"]]
- 004b0620 bytes 1c9d1e94
+ 004b0660 bytes 0c9e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442b011c209699964e86546d2e6357b6"></a>

### [`004b06cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md) → [`004b070c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b070c.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md) · 呼出先 2件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md) · 呼出先 2件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b074c",
      "incomplete_value": true,
      "site": "004b0750",
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
      "definition_site": "004b070c",
      "incomplete_value": true,
      "site": "004b0710",
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
      "004b0740",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0750",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b0740",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0750",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md#insn-004b0708) · [`004b06f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md#insn-004b06f4)
- 新版 `004b0748`（命令位置の公開資料なし） · `004b0734`（命令位置の公開資料なし）

~~~diff
- 004b0708 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0708 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0708 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0708 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0708 bytes 1f7c01a9
+ 004b0748 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0748 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0748 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0748 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0748 bytes 1f7c01a9
- 004b06f4 ["INT_ADD", "register:40f0:8", ["const:4b06f4:8", "const:4:8"]]
- 004b06f4 ["CALL", null, ["callee:00c57e90:8"]]
+ 004b0734 ["INT_ADD", "register:40f0:8", ["const:4b0734:8", "const:4:8"]]
+ 004b0734 ["CALL", null, ["callee:00c57e90:8"]]
- 004b06f4 bytes e79c1e94
+ 004b0734 bytes d79d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f5cb248952c79a79773fd6a9476f5d"></a>

### [`004b07d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md) → [`004b0818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md) _ZN5Botan11BER_Decoder11decode_nullEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b087c",
      "incomplete_value": true,
      "site": "004b087c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b083c",
      "incomplete_value": true,
      "site": "004b083c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b08c0",
      "incomplete_value": false,
      "site": "004b08c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:c29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0880",
      "incomplete_value": false,
      "site": "004b0888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:be9:8"
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
      "definition_site": "004b08f8",
      "incomplete_value": true,
      "site": "004b0904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b08b8",
      "incomplete_value": true,
      "site": "004b08c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "004b086c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b08c0",
      "PARAM",
      [
        "storage",
        "002bfbe9",
        null,
        "string"
      ]
    ],
    [
      "004b08f4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b086c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b08c0",
      "PARAM",
      [
        "storage",
        "002bfc29",
        null,
        "string"
      ]
    ],
    [
      "004b08f4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b083c) · [`004b0888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b0888) · [`004b08c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b08c4)
- 新版 `004b087c`（命令位置の公開資料なし） · `004b08c8`（命令位置の公開資料なし） · `004b0904`（命令位置の公開資料なし）

~~~diff
- 004b083c ["COPY", "register:0:8", ["register:4050:8"]]
- 004b083c ["INT_ADD", "register:40f0:8", ["const:4b083c:8", "const:4:8"]]
- 004b083c ["CALLIND", null, ["register:0:8"]]
+ 004b087c ["COPY", "register:0:8", ["register:4050:8"]]
+ 004b087c ["INT_ADD", "register:40f0:8", ["const:4b087c:8", "const:4:8"]]
+ 004b087c ["CALLIND", null, ["register:0:8"]]
- 004b083c bytes 40013fd6
+ 004b087c bytes 40013fd6
- 004b0888 ["INT_ADD", "register:40f0:8", ["const:4b0888:8", "const:4:8"]]
- 004b0888 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b08c8 ["INT_ADD", "register:40f0:8", ["const:4b08c8:8", "const:4:8"]]
+ 004b08c8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b0888 bytes 4435fe97
+ 004b08c8 bytes 4435fe97
- 004b08c4 ["INT_ADD", "register:40f0:8", ["const:4b08c4:8", "const:4:8"]]
- 004b08c4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b0904 ["INT_ADD", "register:40f0:8", ["const:4b0904:8", "const:4:8"]]
+ 004b0904 ["CALL", null, ["callee:00c57f10:8"]]
- 004b08c4 bytes 939c1e94
+ 004b0904 bytes 839d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c7b9999f080e5ec8a6fe4f6c5c8e4e"></a>

### [`004b0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md) → [`004b0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md) _ZN5Botan11BER_Decoder6decodeERbNS_8ASN1_TagES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c584e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584e0.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c588e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588e0.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b09f0",
      "incomplete_value": true,
      "site": "004b09f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b09b0",
      "incomplete_value": true,
      "site": "004b09b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b0a38",
      "incomplete_value": false,
      "site": "004b0a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:c46:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b09f8",
      "incomplete_value": false,
      "site": "004b0a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:c06:8"
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
      "definition_site": "004b0a70",
      "incomplete_value": true,
      "site": "004b0a7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0a30",
      "incomplete_value": true,
      "site": "004b0a3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "004b09e0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0a38",
      "PARAM",
      [
        "storage",
        "002bfc06",
        null,
        "string"
      ]
    ],
    [
      "004b0a6c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b09e0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0a38",
      "PARAM",
      [
        "storage",
        "002bfc46",
        null,
        "string"
      ]
    ],
    [
      "004b0a6c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b0970) · [`004b09b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b09b0) · [`004b0a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b0a00)
- 新版 `004b09b0`（命令位置の公開資料なし） · `004b09f0`（命令位置の公開資料なし） · `004b0a40`（命令位置の公開資料なし）

~~~diff
- 004b0970 ["INT_ADD", "register:40f0:8", ["const:4b0970:8", "const:4:8"]]
- 004b0970 ["CALL", null, ["callee:00c58730:8"]]
+ 004b09b0 ["INT_ADD", "register:40f0:8", ["const:4b09b0:8", "const:4:8"]]
+ 004b09b0 ["CALL", null, ["callee:00c58730:8"]]
- 004b0970 bytes 709e1e94
+ 004b09b0 bytes 609f1e94
- 004b09b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b09b0 ["INT_ADD", "register:40f0:8", ["const:4b09b0:8", "const:4:8"]]
- 004b09b0 ["CALLIND", null, ["register:0:8"]]
+ 004b09f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b09f0 ["INT_ADD", "register:40f0:8", ["const:4b09f0:8", "const:4:8"]]
+ 004b09f0 ["CALLIND", null, ["register:0:8"]]
- 004b09b0 bytes 20013fd6
+ 004b09f0 bytes 20013fd6
- 004b0a00 ["INT_ADD", "register:40f0:8", ["const:4b0a00:8", "const:4:8"]]
- 004b0a00 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b0a40 ["INT_ADD", "register:40f0:8", ["const:4b0a40:8", "const:4:8"]]
+ 004b0a40 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b0a00 bytes e634fe97
+ 004b0a40 bytes e634fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729081c3e59238444ffc4c71c5bdb9de"></a>

### [`004b0aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md) → [`004b0aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58670.md) · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a70.md) · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0bdc",
      "incomplete_value": true,
      "site": "004b0bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0b9c",
      "incomplete_value": true,
      "site": "004b0b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "definition_site": "004b0c20",
      "incomplete_value": false,
      "site": "004b0c28",
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
            "const:48e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0be0",
      "incomplete_value": false,
      "site": "004b0be8",
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
            "const:3b2:8"
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
      "definition_site": "004b0c58",
      "incomplete_value": true,
      "site": "004b0c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0c18",
      "incomplete_value": true,
      "site": "004b0c24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
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
      "004b0bcc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0c20",
      "PARAM",
      [
        "storage",
        "002a63b2",
        null,
        "string"
      ]
    ],
    [
      "004b0c54",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b0bcc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0c20",
      "PARAM",
      [
        "storage",
        "002a648e",
        null,
        "string"
      ]
    ],
    [
      "004b0c54",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0b9c) · [`004b0be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0be8) · [`004b0c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0c24)
- 新版 `004b0bdc`（命令位置の公開資料なし） · `004b0c28`（命令位置の公開資料なし） · `004b0c64`（命令位置の公開資料なし）

~~~diff
- 004b0b9c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0b9c ["INT_ADD", "register:40f0:8", ["const:4b0b9c:8", "const:4:8"]]
- 004b0b9c ["CALLIND", null, ["register:0:8"]]
+ 004b0bdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0bdc ["INT_ADD", "register:40f0:8", ["const:4b0bdc:8", "const:4:8"]]
+ 004b0bdc ["CALLIND", null, ["register:0:8"]]
- 004b0b9c bytes 20013fd6
+ 004b0bdc bytes 20013fd6
- 004b0be8 ["INT_ADD", "register:40f0:8", ["const:4b0be8:8", "const:4:8"]]
- 004b0be8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b0c28 ["INT_ADD", "register:40f0:8", ["const:4b0c28:8", "const:4:8"]]
+ 004b0c28 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b0be8 bytes 6c34fe97
+ 004b0c28 bytes 6c34fe97
- 004b0c24 ["INT_ADD", "register:40f0:8", ["const:4b0c24:8", "const:4:8"]]
- 004b0c24 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b0c64 ["INT_ADD", "register:40f0:8", ["const:4b0c64:8", "const:4:8"]]
+ 004b0c64 ["CALL", null, ["callee:00c57f10:8"]]
- 004b0c24 bytes bb9b1e94
+ 004b0c64 bytes ab9c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4d81a51f8b03451229c51ef75328d2"></a>

### [`004b0c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md) → [`004b0cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md) _ZN5Botan11BER_Decoder26decode_octet_string_bigintERNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58680.md) [`00c58690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58690.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) [`00c58a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a90.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0d90",
      "incomplete_value": true,
      "site": "004b0d90",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0d50",
      "incomplete_value": true,
      "site": "004b0d50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0dbc",
      "incomplete_value": true,
      "site": "004b0dbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0d7c",
      "incomplete_value": true,
      "site": "004b0d7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
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
      "004b0d80",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0dac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b0d80",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0dac",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0d50) · [`004b0d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0d7c) · [`004b0ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0ccc)
- 新版 `004b0d90`（命令位置の公開資料なし） · `004b0dbc`（命令位置の公開資料なし） · `004b0d0c`（命令位置の公開資料なし）

~~~diff
- 004b0d50 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0d50 ["INT_ADD", "register:40f0:8", ["const:4b0d50:8", "const:4:8"]]
- 004b0d50 ["CALLIND", null, ["register:0:8"]]
+ 004b0d90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0d90 ["INT_ADD", "register:40f0:8", ["const:4b0d90:8", "const:4:8"]]
+ 004b0d90 ["CALLIND", null, ["register:0:8"]]
- 004b0d50 bytes 20013fd6
+ 004b0d90 bytes 20013fd6
- 004b0d7c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0d7c ["INT_ADD", "register:40f0:8", ["const:4b0d7c:8", "const:4:8"]]
- 004b0d7c ["CALLIND", null, ["register:0:8"]]
+ 004b0dbc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0dbc ["INT_ADD", "register:40f0:8", ["const:4b0dbc:8", "const:4:8"]]
+ 004b0dbc ["CALLIND", null, ["register:0:8"]]
- 004b0d7c bytes 20013fd6
+ 004b0dbc bytes 20013fd6
- 004b0ccc ["INT_ADD", "register:40f0:8", ["const:4b0ccc:8", "const:4:8"]]
- 004b0ccc ["CALL", null, ["callee:00c58a80:8"]]
+ 004b0d0c ["INT_ADD", "register:40f0:8", ["const:4b0d0c:8", "const:4:8"]]
+ 004b0d0c ["CALL", null, ["callee:00c58a80:8"]]
- 004b0ccc bytes 6d9e1e94
+ 004b0d0c bytes 5d9f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098f51e54a7ec8e9b61e762e3bd9b6bb"></a>

### [`004b0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md) → [`004b0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) _ZN5Botan6BigInt6decodeEPKhmNS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586a0.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md)
- 新版 呼出元 1件 [`00c58aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58aa0.md) · 呼出先 20件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0f2c",
      "incomplete_value": true,
      "site": "004b0f2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0eec",
      "incomplete_value": true,
      "site": "004b0eec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
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
    "kind": "call_target",
    "new": {
      "definition_site": "004b0f70",
      "incomplete_value": true,
      "site": "004b0f70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0f30",
      "incomplete_value": true,
      "site": "004b0f30",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b1074",
      "incomplete_value": true,
      "site": "004b1074",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1034",
      "incomplete_value": true,
      "site": "004b1034",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
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
      "004b0f1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0f60",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1064",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b0f1c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0f60",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b1064",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b0eac) · [`004b0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b0eec) · [`004b0f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b0f30)
- 新版 `004b0eec`（命令位置の公開資料なし） · `004b0f2c`（命令位置の公開資料なし） · `004b0f70`（命令位置の公開資料なし）

~~~diff
- 004b0eac ["INT_ADD", "register:40f0:8", ["const:4b0eac:8", "const:4:8"]]
- 004b0eac ["CALL", null, ["callee:00c58ab0:8"]]
+ 004b0eec ["INT_ADD", "register:40f0:8", ["const:4b0eec:8", "const:4:8"]]
+ 004b0eec ["CALL", null, ["callee:00c58ab0:8"]]
- 004b0eac bytes 019e1e94
+ 004b0eec bytes f19e1e94
- 004b0eec ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0eec ["INT_ADD", "register:40f0:8", ["const:4b0eec:8", "const:4:8"]]
- 004b0eec ["CALLIND", null, ["register:0:8"]]
+ 004b0f2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0f2c ["INT_ADD", "register:40f0:8", ["const:4b0f2c:8", "const:4:8"]]
+ 004b0f2c ["CALLIND", null, ["register:0:8"]]
- 004b0eec bytes 20013fd6
+ 004b0f2c bytes 20013fd6
- 004b0f30 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0f30 ["INT_ADD", "register:40f0:8", ["const:4b0f30:8", "const:4:8"]]
- 004b0f30 ["CALLIND", null, ["register:0:8"]]
+ 004b0f70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0f70 ["INT_ADD", "register:40f0:8", ["const:4b0f70:8", "const:4:8"]]
+ 004b0f70 ["CALLIND", null, ["register:0:8"]]
- 004b0f30 bytes 20013fd6
+ 004b0f70 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d415b36c9ad27300a03a9ca42d7d3b64"></a>

### [`004b14d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md) → [`004b1518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md) _ZN5Botan11BER_Decoder26decode_constrained_integerENS_8ASN1_TagES1_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b1670",
      "incomplete_value": true,
      "site": "004b1670",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1630",
      "incomplete_value": true,
      "site": "004b1630",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "definition_site": "004b16d8",
      "incomplete_value": false,
      "site": "004b16e0",
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
            "const:6dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1698",
      "incomplete_value": false,
      "site": "004b16a0",
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
            "const:601:8"
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
      "definition_site": "004b1710",
      "incomplete_value": true,
      "site": "004b171c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b16d0",
      "incomplete_value": true,
      "site": "004b16dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
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
      "004b1660",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b16d8",
      "PARAM",
      [
        "storage",
        "002a7601",
        null,
        "string"
      ]
    ],
    [
      "004b170c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b1660",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b16d8",
      "PARAM",
      [
        "storage",
        "002a76dd",
        null,
        "string"
      ]
    ],
    [
      "004b170c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b1630) · [`004b16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b16a0) · [`004b16dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b16dc)
- 新版 `004b1670`（命令位置の公開資料なし） · `004b16e0`（命令位置の公開資料なし） · `004b171c`（命令位置の公開資料なし）

~~~diff
- 004b1630 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1630 ["INT_ADD", "register:40f0:8", ["const:4b1630:8", "const:4:8"]]
- 004b1630 ["CALLIND", null, ["register:0:8"]]
+ 004b1670 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1670 ["INT_ADD", "register:40f0:8", ["const:4b1670:8", "const:4:8"]]
+ 004b1670 ["CALLIND", null, ["register:0:8"]]
- 004b1630 bytes 20013fd6
+ 004b1670 bytes 20013fd6
- 004b16a0 ["INT_ADD", "register:40f0:8", ["const:4b16a0:8", "const:4:8"]]
- 004b16a0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b16e0 ["INT_ADD", "register:40f0:8", ["const:4b16e0:8", "const:4:8"]]
+ 004b16e0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b16a0 bytes be31fe97
+ 004b16e0 bytes be31fe97
- 004b16dc ["INT_ADD", "register:40f0:8", ["const:4b16dc:8", "const:4:8"]]
- 004b16dc ["CALL", null, ["callee:00c57f10:8"]]
+ 004b171c ["INT_ADD", "register:40f0:8", ["const:4b171c:8", "const:4:8"]]
+ 004b171c ["CALL", null, ["callee:00c57f10:8"]]
- 004b16dc bytes 0d991e94
+ 004b171c bytes fd991e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80069d6b4772137d909540b835d26319"></a>

### [`004b182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md) → [`004b186c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58680.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00540eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540eec.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00540f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540f2c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.97% / 新版 95.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b1978",
      "incomplete_value": true,
      "site": "004b1978",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1938",
      "incomplete_value": true,
      "site": "004b1938",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b19c0",
      "incomplete_value": false,
      "site": "004b19c8",
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
            "const:3be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1980",
      "incomplete_value": false,
      "site": "004b1988",
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
            "const:2e2:8"
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
      "definition_site": "004b19fc",
      "incomplete_value": true,
      "site": "004b1a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b19bc",
      "incomplete_value": true,
      "site": "004b19c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a0:8"
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
      "004b1968",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b19c0",
      "PARAM",
      [
        "storage",
        "002a52e2",
        null,
        "string"
      ]
    ],
    [
      "004b19f8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b1968",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b19c0",
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      "004b19f8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b1938) · [`004b1988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b1988) · [`004b19c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b19c8)
- 新版 `004b1978`（命令位置の公開資料なし） · `004b19c8`（命令位置の公開資料なし） · `004b1a08`（命令位置の公開資料なし）

~~~diff
- 004b1938 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1938 ["INT_ADD", "register:40f0:8", ["const:4b1938:8", "const:4:8"]]
- 004b1938 ["CALLIND", null, ["register:0:8"]]
+ 004b1978 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1978 ["INT_ADD", "register:40f0:8", ["const:4b1978:8", "const:4:8"]]
+ 004b1978 ["CALLIND", null, ["register:0:8"]]
- 004b1938 bytes 20013fd6
+ 004b1978 bytes 20013fd6
- 004b1988 ["INT_ADD", "register:40f0:8", ["const:4b1988:8", "const:4:8"]]
- 004b1988 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b19c8 ["INT_ADD", "register:40f0:8", ["const:4b19c8:8", "const:4:8"]]
+ 004b19c8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b1988 bytes 0431fe97
+ 004b19c8 bytes 0431fe97
- 004b19c8 ["INT_ADD", "register:40f0:8", ["const:4b19c8:8", "const:4:8"]]
- 004b19c8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b1a08 ["INT_ADD", "register:40f0:8", ["const:4b1a08:8", "const:4:8"]]
+ 004b1a08 ["CALL", null, ["callee:00c57f10:8"]]
- 004b19c8 bytes 52981e94
+ 004b1a08 bytes 42991e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0de61f2518a7d741f0b18c70fe4cbf75"></a>

### [`004b1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md) → [`004b1b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS1_9allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c584a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584a0.md) · 呼出先 18件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0054104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c588a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588a0.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0054108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/0054108c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.89% / 新版 96.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b1cf0",
      "incomplete_value": true,
      "site": "004b1cf0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1cb0",
      "incomplete_value": true,
      "site": "004b1cb0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b1d40",
      "incomplete_value": false,
      "site": "004b1d48",
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
            "const:3be:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1d00",
      "incomplete_value": false,
      "site": "004b1d08",
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
            "const:2e2:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b1d7c",
      "incomplete_value": true,
      "site": "004b1d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1d3c",
      "incomplete_value": true,
      "site": "004b1d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a0:8"
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
      "004b1ce0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d40",
      "PARAM",
      [
        "storage",
        "002a52e2",
        null,
        "string"
      ]
    ],
    [
      "004b1d78",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b1ce0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d40",
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      "004b1d78",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1cb0) · [`004b1d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1d08) · [`004b1d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1d48)
- 新版 `004b1cf0`（命令位置の公開資料なし） · `004b1d48`（命令位置の公開資料なし） · `004b1d88`（命令位置の公開資料なし）

~~~diff
- 004b1cb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1cb0 ["INT_ADD", "register:40f0:8", ["const:4b1cb0:8", "const:4:8"]]
- 004b1cb0 ["CALLIND", null, ["register:0:8"]]
+ 004b1cf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1cf0 ["INT_ADD", "register:40f0:8", ["const:4b1cf0:8", "const:4:8"]]
+ 004b1cf0 ["CALLIND", null, ["register:0:8"]]
- 004b1cb0 bytes 20013fd6
+ 004b1cf0 bytes 20013fd6
- 004b1d08 ["INT_ADD", "register:40f0:8", ["const:4b1d08:8", "const:4:8"]]
- 004b1d08 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b1d48 ["INT_ADD", "register:40f0:8", ["const:4b1d48:8", "const:4:8"]]
+ 004b1d48 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b1d08 bytes 2430fe97
+ 004b1d48 bytes 2430fe97
- 004b1d48 ["INT_ADD", "register:40f0:8", ["const:4b1d48:8", "const:4:8"]]
- 004b1d48 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b1d88 ["INT_ADD", "register:40f0:8", ["const:4b1d88:8", "const:4:8"]]
+ 004b1d88 ["CALL", null, ["callee:00c57f10:8"]]
- 004b1d48 bytes 72971e94
+ 004b1d88 bytes 62981e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0fd167c832a57ad0ea9ea1039865e4c"></a>

### [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) → [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c582f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582f0.md) · 呼出先 8件 [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) [`004b2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c586f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586f0.md) · 呼出先 8件 [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b204c",
      "incomplete_value": true,
      "site": "004b204c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b200c",
      "incomplete_value": true,
      "site": "004b200c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
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
    "kind": "call_target",
    "new": {
      "definition_site": "004b20e4",
      "incomplete_value": true,
      "site": "004b20e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b20a4",
      "incomplete_value": true,
      "site": "004b20a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2170",
      "incomplete_value": true,
      "site": "004b2170",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2130",
      "incomplete_value": true,
      "site": "004b2130",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "004b203c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b20d4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2160",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b203c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b20d4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b2160",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b200c) · [`004b20a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b20a4) · [`004b20e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b20e4)
- 新版 `004b204c`（命令位置の公開資料なし） · `004b20e4`（命令位置の公開資料なし） · `004b2124`（命令位置の公開資料なし）

~~~diff
- 004b200c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b200c ["INT_ADD", "register:40f0:8", ["const:4b200c:8", "const:4:8"]]
- 004b200c ["CALLIND", null, ["register:0:8"]]
+ 004b204c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b204c ["INT_ADD", "register:40f0:8", ["const:4b204c:8", "const:4:8"]]
+ 004b204c ["CALLIND", null, ["register:0:8"]]
- 004b200c bytes 20013fd6
+ 004b204c bytes 20013fd6
- 004b20a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b20a4 ["INT_ADD", "register:40f0:8", ["const:4b20a4:8", "const:4:8"]]
- 004b20a4 ["CALLIND", null, ["register:0:8"]]
+ 004b20e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b20e4 ["INT_ADD", "register:40f0:8", ["const:4b20e4:8", "const:4:8"]]
+ 004b20e4 ["CALLIND", null, ["register:0:8"]]
- 004b20a4 bytes 20013fd6
+ 004b20e4 bytes 20013fd6
- 004b20e4 ["INT_ADD", "register:40f0:8", ["const:4b20e4:8", "const:4:8"]]
- 004b20e4 ["CALL", null, ["callee:005404ec:8"]]
+ 004b2124 ["INT_ADD", "register:40f0:8", ["const:4b2124:8", "const:4:8"]]
+ 004b2124 ["CALL", null, ["callee:005404ec:8"]]
- 004b20e4 bytes f2380294
+ 004b2124 bytes f2380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7f486aab12108082001d1eb89ed336"></a>

### [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) → [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) FUN_004b2254

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md) [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`004ad4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b22e0",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:26e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22a0",
      "incomplete_value": false,
      "site": "004b22c0",
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
            "const:22e:8"
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
      "definition_site": "004b22e8",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22a8",
      "incomplete_value": false,
      "site": "004b22c0",
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
            "const:e03:8"
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
      "definition_site": "004b22f0",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:d13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22b0",
      "incomplete_value": false,
      "site": "004b22c0",
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
            "const:c46:8"
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
      "004b22e0",
      "PARAM",
      [
        "storage",
        "002bb22e",
        null,
        "string"
      ]
    ],
    [
      "004b22e8",
      "PARAM",
      [
        "storage",
        "002a1e03",
        null,
        "string"
      ]
    ],
    [
      "004b22f0",
      "PARAM",
      [
        "storage",
        "002a8c46",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b22e0",
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      "004b22e8",
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      "004b22f0",
      "PARAM",
      [
        "storage",
        "002a8d13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b22c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b22c0) · [`004b2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b2494) · [`004b24e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b24e8)
- 新版 `004b2300`（命令位置の公開資料なし） · `004b24d4`（命令位置の公開資料なし） · `004b2528`（命令位置の公開資料なし）

~~~diff
- 004b22c0 ["INT_ADD", "register:40f0:8", ["const:4b22c0:8", "const:4:8"]]
- 004b22c0 ["CALL", null, ["callee:00c58650:8"]]
+ 004b2300 ["INT_ADD", "register:40f0:8", ["const:4b2300:8", "const:4:8"]]
+ 004b2300 ["CALL", null, ["callee:00c58650:8"]]
- 004b22c0 bytes e4971e94
+ 004b2300 bytes d4981e94
- 004b2494 ["INT_ADD", "register:40f0:8", ["const:4b2494:8", "const:4:8"]]
- 004b2494 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b24d4 ["INT_ADD", "register:40f0:8", ["const:4b24d4:8", "const:4:8"]]
+ 004b24d4 ["CALL", null, ["callee:00c57f60:8"]]
- 004b2494 bytes b3951e94
+ 004b24d4 bytes a3961e94
- 004b24e8 ["INT_ADD", "register:40f0:8", ["const:4b24e8:8", "const:4:8"]]
- 004b24e8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b2528 ["INT_ADD", "register:40f0:8", ["const:4b2528:8", "const:4:8"]]
+ 004b2528 ["CALL", null, ["callee:00c57f10:8"]]
- 004b24e8 bytes 8a951e94
+ 004b2528 bytes 7a961e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e10ae5cc96860d30cce936c93c16059"></a>

### [`004b28a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md) → [`004b28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583a0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c587a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587a0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b2960",
      "incomplete_value": false,
      "site": "004b2968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2920",
      "incomplete_value": false,
      "site": "004b2928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e1e:8"
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
      "definition_site": "004b299c",
      "incomplete_value": true,
      "site": "004b29a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b295c",
      "incomplete_value": true,
      "site": "004b2968",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
              ]
            ]
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
      "definition_site": "004b2998",
      "incomplete_value": false,
      "site": "004b29a8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b2958",
      "incomplete_value": false,
      "site": "004b2968",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b2960",
      "PARAM",
      [
        "storage",
        "002b8e1e",
        null,
        "string"
      ]
    ],
    [
      "004b2998",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b299c",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2960",
      "PARAM",
      [
        "storage",
        "002b8e5e",
        null,
        "string"
      ]
    ],
    [
      "004b2998",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b299c",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2928) · [`004b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2968) · [`004b2914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2914)
- 新版 `004b2968`（命令位置の公開資料なし） · `004b29a8`（命令位置の公開資料なし） · `004b2954`（命令位置の公開資料なし）

~~~diff
- 004b2928 ["INT_ADD", "register:40f0:8", ["const:4b2928:8", "const:4:8"]]
- 004b2928 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
+ 004b2968 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b2928 bytes 1c2dfe97
+ 004b2968 bytes 1c2dfe97
- 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
- 004b2968 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b29a8 ["INT_ADD", "register:40f0:8", ["const:4b29a8:8", "const:4:8"]]
+ 004b29a8 ["CALL", null, ["callee:00c57f10:8"]]
- 004b2968 bytes 6a941e94
+ 004b29a8 bytes 5a951e94
- 004b2914 ["INT_ADD", "register:40f0:8", ["const:4b2914:8", "const:4:8"]]
- 004b2914 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b2954 ["INT_ADD", "register:40f0:8", ["const:4b2954:8", "const:4:8"]]
+ 004b2954 ["CALL", null, ["callee:00c57ef0:8"]]
- 004b2914 bytes 77941e94
+ 004b2954 bytes 67951e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6514620647983b9f48af602f8a09629"></a>

### [`004b29bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md) → [`004b29fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md) FUN_004b29fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2a64",
      "incomplete_value": true,
      "site": "004b2a64",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2a24",
      "incomplete_value": true,
      "site": "004b2a24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2aa0",
      "incomplete_value": true,
      "site": "004b2aa0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2a60",
      "incomplete_value": true,
      "site": "004b2a60",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
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
      "004b2a54",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2a90",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2a54",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b2a90",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b2a24) · [`004b2a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b2a60) · [`004b2a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b2a14)
- 新版 `004b2a64`（命令位置の公開資料なし） · `004b2aa0`（命令位置の公開資料なし） · `004b2a54`（命令位置の公開資料なし）

~~~diff
- 004b2a24 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2a24 ["INT_ADD", "register:40f0:8", ["const:4b2a24:8", "const:4:8"]]
- 004b2a24 ["CALLIND", null, ["register:0:8"]]
+ 004b2a64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2a64 ["INT_ADD", "register:40f0:8", ["const:4b2a64:8", "const:4:8"]]
+ 004b2a64 ["CALLIND", null, ["register:0:8"]]
- 004b2a24 bytes 20013fd6
+ 004b2a64 bytes 20013fd6
- 004b2a60 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2a60 ["INT_ADD", "register:40f0:8", ["const:4b2a60:8", "const:4:8"]]
- 004b2a60 ["CALLIND", null, ["register:0:8"]]
+ 004b2aa0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2aa0 ["INT_ADD", "register:40f0:8", ["const:4b2aa0:8", "const:4:8"]]
+ 004b2aa0 ["CALLIND", null, ["register:0:8"]]
- 004b2a60 bytes 20013fd6
+ 004b2aa0 bytes 20013fd6
- 004b2a14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 004b2a14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b2a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 004b2a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b2a14 bytes a99e41f9
+ 004b2a54 bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af829953da05f0766406382e1a264abe"></a>

### [`004b2a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md) → [`004b2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md) _ZN5Botan11DER_Encoder14start_explicitEt

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b2b40",
      "incomplete_value": false,
      "site": "004b2b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:8a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2b00",
      "incomplete_value": false,
      "site": "004b2b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:867:8"
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
      "definition_site": "004b2b7c",
      "incomplete_value": true,
      "site": "004b2b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2b3c",
      "incomplete_value": true,
      "site": "004b2b48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f8:8"
              ]
            ]
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
      "definition_site": "004b2b78",
      "incomplete_value": false,
      "site": "004b2b88",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b2b38",
      "incomplete_value": false,
      "site": "004b2b48",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b2b40",
      "PARAM",
      [
        "storage",
        "002af867",
        null,
        "string"
      ]
    ],
    [
      "004b2b78",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b2b7c",
      "READ",
      [
        "storage",
        "00c9a9f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2b40",
      "PARAM",
      [
        "storage",
        "002af8a7",
        null,
        "string"
      ]
    ],
    [
      "004b2b78",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b2b7c",
      "READ",
      [
        "storage",
        "00c9adf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2b08) · [`004b2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2b48) · [`004b2af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2af4)
- 新版 `004b2b48`（命令位置の公開資料なし） · `004b2b88`（命令位置の公開資料なし） · `004b2b34`（命令位置の公開資料なし）

~~~diff
- 004b2b08 ["INT_ADD", "register:40f0:8", ["const:4b2b08:8", "const:4:8"]]
- 004b2b08 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b2b48 ["INT_ADD", "register:40f0:8", ["const:4b2b48:8", "const:4:8"]]
+ 004b2b48 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b2b08 bytes a42cfe97
+ 004b2b48 bytes a42cfe97
- 004b2b48 ["INT_ADD", "register:40f0:8", ["const:4b2b48:8", "const:4:8"]]
- 004b2b48 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b2b88 ["INT_ADD", "register:40f0:8", ["const:4b2b88:8", "const:4:8"]]
+ 004b2b88 ["CALL", null, ["callee:00c57f10:8"]]
- 004b2b48 bytes f2931e94
+ 004b2b88 bytes e2941e94
- 004b2af4 ["INT_ADD", "register:40f0:8", ["const:4b2af4:8", "const:4:8"]]
- 004b2af4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b2b34 ["INT_ADD", "register:40f0:8", ["const:4b2b34:8", "const:4:8"]]
+ 004b2b34 ["CALL", null, ["callee:00c57ef0:8"]]
- 004b2af4 bytes ff931e94
+ 004b2b34 bytes ef941e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c41d1586cc35a7a0581511f417afa7e0"></a>

### [`004b2dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md) → [`004b2e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58710.md) · 呼出先 8件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)
- 新版 呼出元 1件 [`00c58b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b10.md) · 呼出先 8件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.86% / 新版 96.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2e80",
      "incomplete_value": true,
      "site": "004b2e80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2e40",
      "incomplete_value": true,
      "site": "004b2e40",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b3014",
      "incomplete_value": true,
      "site": "004b3014",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2fd4",
      "incomplete_value": true,
      "site": "004b2fd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b30c0",
      "incomplete_value": true,
      "site": "004b30c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3080",
      "incomplete_value": true,
      "site": "004b3080",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
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
      "004b2e70",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b3004",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b30b0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2e70",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b3004",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b30b0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b2e40) · [`004b2fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b2fd4) · [`004b3080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b3080)
- 新版 `004b2e80`（命令位置の公開資料なし） · `004b3014`（命令位置の公開資料なし） · `004b30c0`（命令位置の公開資料なし）

~~~diff
- 004b2e40 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2e40 ["INT_ADD", "register:40f0:8", ["const:4b2e40:8", "const:4:8"]]
- 004b2e40 ["CALLIND", null, ["register:0:8"]]
+ 004b2e80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2e80 ["INT_ADD", "register:40f0:8", ["const:4b2e80:8", "const:4:8"]]
+ 004b2e80 ["CALLIND", null, ["register:0:8"]]
- 004b2e40 bytes 20013fd6
+ 004b2e80 bytes 20013fd6
- 004b2fd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2fd4 ["INT_ADD", "register:40f0:8", ["const:4b2fd4:8", "const:4:8"]]
- 004b2fd4 ["CALLIND", null, ["register:0:8"]]
+ 004b3014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3014 ["INT_ADD", "register:40f0:8", ["const:4b3014:8", "const:4:8"]]
+ 004b3014 ["CALLIND", null, ["register:0:8"]]
- 004b2fd4 bytes 20013fd6
+ 004b3014 bytes 20013fd6
- 004b3080 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b3080 ["INT_ADD", "register:40f0:8", ["const:4b3080:8", "const:4:8"]]
- 004b3080 ["CALLIND", null, ["register:0:8"]]
+ 004b30c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b30c0 ["INT_ADD", "register:40f0:8", ["const:4b30c0:8", "const:4:8"]]
+ 004b30c0 ["CALLIND", null, ["register:0:8"]]
- 004b3080 bytes 20013fd6
+ 004b30c0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acab07fdfb837cdbec41da433a4cee94"></a>

### [`004b310c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md) → [`004b314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md) _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58730.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b30.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b325c",
      "incomplete_value": true,
      "site": "004b325c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b321c",
      "incomplete_value": true,
      "site": "004b321c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b32a8",
      "incomplete_value": false,
      "site": "004b32b0",
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
            "const:fba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3268",
      "incomplete_value": false,
      "site": "004b3270",
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
            "const:eed:8"
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
      "definition_site": "004b32e0",
      "incomplete_value": true,
      "site": "004b32ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b32a0",
      "incomplete_value": true,
      "site": "004b32ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "004b324c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b32a8",
      "PARAM",
      [
        "storage",
        "002a3eed",
        null,
        "string"
      ]
    ],
    [
      "004b32dc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b324c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b32a8",
      "PARAM",
      [
        "storage",
        "002a3fba",
        null,
        "string"
      ]
    ],
    [
      "004b32dc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b321c) · [`004b325c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b325c) · [`004b3270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b3270)
- 新版 `004b325c`（命令位置の公開資料なし） · `004b329c`（命令位置の公開資料なし） · `004b32b0`（命令位置の公開資料なし）

~~~diff
- 004b321c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b321c ["INT_ADD", "register:40f0:8", ["const:4b321c:8", "const:4:8"]]
- 004b321c ["CALLIND", null, ["register:0:8"]]
+ 004b325c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b325c ["INT_ADD", "register:40f0:8", ["const:4b325c:8", "const:4:8"]]
+ 004b325c ["CALLIND", null, ["register:0:8"]]
- 004b321c bytes 20013fd6
+ 004b325c bytes 20013fd6
- 004b325c ["INT_ADD", "register:40f0:8", ["const:4b325c:8", "const:4:8"]]
- 004b325c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b329c ["INT_ADD", "register:40f0:8", ["const:4b329c:8", "const:4:8"]]
+ 004b329c ["CALL", null, ["callee:00c57ef0:8"]]
- 004b325c bytes 25921e94
+ 004b329c bytes 15931e94
- 004b3270 ["INT_ADD", "register:40f0:8", ["const:4b3270:8", "const:4:8"]]
- 004b3270 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b32b0 ["INT_ADD", "register:40f0:8", ["const:4b32b0:8", "const:4:8"]]
+ 004b32b0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b3270 bytes ca2afe97
+ 004b32b0 bytes ca2afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d908e0fea9f918c5e04c686b428acaf"></a>

### [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) → [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) FUN_004b3508

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 55件 [`004b0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md) [`004b2dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md) [`004b35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md) [`004b4dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4dcc.md) [`004b569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b569c.md) · 呼出先 7件 [`00536e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536e48.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 55件 [`004b0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) [`004b2e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) [`004b3600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) [`004b4e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4e0c.md) [`004b56dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b56dc.md) · 呼出先 7件 [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b35cc",
      "incomplete_value": true,
      "site": "004b35d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b358c",
      "incomplete_value": true,
      "site": "004b3594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e8:8"
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
      "definition_site": "004b35d0",
      "incomplete_value": true,
      "site": "004b35d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3590",
      "incomplete_value": true,
      "site": "004b3594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
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
      "004b35cc",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004b35cc",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b35d0",
      "READ",
      [
        "storage",
        "00c9a9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b35cc",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004b35cc",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b35d0",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b3594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b3594) · [`004b3510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b3510) · [`004b355c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b355c)
- 新版 `004b35d4`（命令位置の公開資料なし） · `004b3550`（命令位置の公開資料なし） · `004b359c`（命令位置の公開資料なし）

~~~diff
- 004b3594 ["INT_ADD", "register:40f0:8", ["const:4b3594:8", "const:4:8"]]
- 004b3594 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b35d4 ["INT_ADD", "register:40f0:8", ["const:4b35d4:8", "const:4:8"]]
+ 004b35d4 ["CALL", null, ["callee:00c57f10:8"]]
- 004b3594 bytes 5f911e94
+ 004b35d4 bytes 4f921e94
- 004b3510 ["INT_ADD", "register:40f0:8", ["const:4b3510:8", "const:4:8"]]
- 004b3510 ["CALL", null, ["callee:00c58a30:8"]]
+ 004b3550 ["INT_ADD", "register:40f0:8", ["const:4b3550:8", "const:4:8"]]
+ 004b3550 ["CALL", null, ["callee:00c58a30:8"]]
- 004b3510 bytes 48941e94
+ 004b3550 bytes 38951e94
- 004b355c ["INT_ADD", "register:40f0:8", ["const:4b355c:8", "const:4:8"]]
- 004b355c ["CALL", null, ["callee:00536e88:8"]]
+ 004b359c ["INT_ADD", "register:40f0:8", ["const:4b359c:8", "const:4:8"]]
+ 004b359c ["CALL", null, ["callee:00536e88:8"]]
- 004b355c bytes 3b0e0294
+ 004b359c bytes 3b0e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c0ea81f20b1a082cb0ea6d38de13c1c"></a>

### [`004b35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md) → [`004b3600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004b3940",
      "incomplete_value": true,
      "site": "004b3940",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "TRUNC",
            "8",
            [
              "FLOAT_ADD"
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
      "definition_site": "004b3900",
      "incomplete_value": true,
      "site": "004b3900",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "TRUNC",
            "8",
            [
              "FLOAT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b38f4",
      "incomplete_value": true,
      "site": "004b38f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b38b4",
      "incomplete_value": true,
      "site": "004b38b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b3990",
      "incomplete_value": true,
      "site": "004b3990",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3950",
      "incomplete_value": true,
      "site": "004b3950",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:338:8"
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
      "004b38bc",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b38c4",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b38e4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b38bc",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b38c4",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b38e4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b38b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b38b4) · [`004b38f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b38f4) · [`004b3940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b3940)
- 新版 `004b38f4`（命令位置の公開資料なし） · `004b3934`（命令位置の公開資料なし） · `004b3980`（命令位置の公開資料なし）

~~~diff
- 004b38b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b38b4 ["INT_ADD", "register:40f0:8", ["const:4b38b4:8", "const:4:8"]]
- 004b38b4 ["CALLIND", null, ["register:0:8"]]
+ 004b38f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b38f4 ["INT_ADD", "register:40f0:8", ["const:4b38f4:8", "const:4:8"]]
+ 004b38f4 ["CALLIND", null, ["register:0:8"]]
- 004b38b4 bytes 20013fd6
+ 004b38f4 bytes 20013fd6
- 004b38f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:248:8"]]
- 004b38f4 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 004b38f4 ["COPY", "register:5048:8", ["const:0:8"]]
- 004b38f4 ["COPY", "register:5050:8", ["const:0:8"]]
+ 004b3934 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
+ 004b3934 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b3934 ["COPY", "register:5048:8", ["const:0:8"]]
+ 004b3934 ["COPY", "register:5050:8", ["const:0:8"]]
- 004b38f4 bytes 022541fd
+ 004b3934 bytes 024541fd
- 004b3940 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:338:8"]]
- 004b3940 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b3980 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
+ 004b3980 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b3940 bytes 299f41f9
+ 004b3980 bytes 299f43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d998312e333fb8e3076e9aaf76f07528"></a>

### [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) → [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58780.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`004b476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md)
- 新版 呼出元 2件 [`00c58b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b80.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`004b47ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b3f78",
      "incomplete_value": false,
      "site": "004b3f84",
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
            "const:4b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3f38",
      "incomplete_value": false,
      "site": "004b3f44",
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
            "const:3db:8"
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
      "definition_site": "004b3f8c",
      "incomplete_value": false,
      "site": "004b3f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:899:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3f4c",
      "incomplete_value": false,
      "site": "004b3f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:859:8"
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
      "definition_site": "004b44fc",
      "incomplete_value": false,
      "site": "004b4508",
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
            "const:337:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b44bc",
      "incomplete_value": false,
      "site": "004b44c8",
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
            "const:2f7:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b3f78",
      "PARAM",
      [
        "storage",
        "002a53db",
        null,
        "string"
      ]
    ],
    [
      "004b3f8c",
      "PARAM",
      [
        "storage",
        "002bd859",
        null,
        null
      ]
    ],
    [
      "004b4010",
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
      "004b3f78",
      "PARAM",
      [
        "storage",
        "002a54b7",
        null,
        "string"
      ]
    ],
    [
      "004b3f8c",
      "PARAM",
      [
        "storage",
        "002bd899",
        null,
        null
      ]
    ],
    [
      "004b4010",
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

- 旧版 [`004b3f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b3f44) · [`004b3f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b3f54) · [`004b44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b44c8)
- 新版 `004b3f84`（命令位置の公開資料なし） · `004b3f94`（命令位置の公開資料なし） · `004b4508`（命令位置の公開資料なし）

~~~diff
- 004b3f44 ["INT_ADD", "register:40f0:8", ["const:4b3f44:8", "const:4:8"]]
- 004b3f44 ["CALL", null, ["callee:00c580b0:8"]]
+ 004b3f84 ["INT_ADD", "register:40f0:8", ["const:4b3f84:8", "const:4:8"]]
+ 004b3f84 ["CALL", null, ["callee:00c580b0:8"]]
- 004b3f44 bytes 5b8f1e94
+ 004b3f84 bytes 4b901e94
- 004b3f54 ["INT_ADD", "register:40f0:8", ["const:4b3f54:8", "const:4:8"]]
- 004b3f54 ["CALL", null, ["callee:00c57f70:8"]]
+ 004b3f94 ["INT_ADD", "register:40f0:8", ["const:4b3f94:8", "const:4:8"]]
+ 004b3f94 ["CALL", null, ["callee:00c57f70:8"]]
- 004b3f54 bytes 078f1e94
+ 004b3f94 bytes f78f1e94
- 004b44c8 ["INT_ADD", "register:40f0:8", ["const:4b44c8:8", "const:4:8"]]
- 004b44c8 ["CALL", null, ["callee:00481e80:8"]]
+ 004b4508 ["INT_ADD", "register:40f0:8", ["const:4b4508:8", "const:4:8"]]
+ 004b4508 ["CALL", null, ["callee:00481e80:8"]]
- 004b44c8 bytes 5e36ff97
+ 004b4508 bytes 5e36ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a88ee4953fac171684d549dd6c543c20"></a>

### [`004b476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md) → [`004b47ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md) FUN_004b47ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b48f0",
      "incomplete_value": false,
      "site": "004b48f4",
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
            "const:cca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b48b0",
      "incomplete_value": false,
      "site": "004b48b4",
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
            "const:c8a:8"
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
      "definition_site": "004b4960",
      "incomplete_value": false,
      "site": "004b4964",
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
            "const:a5c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4920",
      "incomplete_value": false,
      "site": "004b4924",
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
            "const:98f:8"
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
      "004b48a0",
      "PARAM",
      [
        "storage",
        "002af9e2",
        null,
        null
      ]
    ],
    [
      "004b48f0",
      "PARAM",
      [
        "storage",
        "002b2c8a",
        null,
        null
      ]
    ],
    [
      "004b4960",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b48a0",
      "PARAM",
      [
        "storage",
        "002afa22",
        null,
        null
      ]
    ],
    [
      "004b48f0",
      "PARAM",
      [
        "storage",
        "002b2cca",
        null,
        null
      ]
    ],
    [
      "004b4960",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b48b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b48b4) · [`004b48e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b48e4) · [`004b4924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b4924)
- 新版 `004b48f4`（命令位置の公開資料なし） · `004b4924`（命令位置の公開資料なし） · `004b4964`（命令位置の公開資料なし）

~~~diff
- 004b48b4 ["INT_ADD", "register:40f0:8", ["const:4b48b4:8", "const:4:8"]]
- 004b48b4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004b48f4 ["INT_ADD", "register:40f0:8", ["const:4b48f4:8", "const:4:8"]]
+ 004b48f4 ["CALL", null, ["callee:00c580b0:8"]]
- 004b48b4 bytes ff8c1e94
+ 004b48f4 bytes ef8d1e94
- 004b48e4 ["INT_ADD", "register:40f0:8", ["const:4b48e4:8", "const:4:8"]]
- 004b48e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004b4924 ["INT_ADD", "register:40f0:8", ["const:4b4924:8", "const:4:8"]]
+ 004b4924 ["CALL", null, ["callee:00c57eb0:8"]]
- 004b48e4 bytes 738c1e94
+ 004b4924 bytes 638d1e94
- 004b4924 ["INT_ADD", "register:40f0:8", ["const:4b4924:8", "const:4:8"]]
- 004b4924 ["CALL", null, ["callee:00c57f70:8"]]
+ 004b4964 ["INT_ADD", "register:40f0:8", ["const:4b4964:8", "const:4:8"]]
+ 004b4964 ["CALL", null, ["callee:00c57f70:8"]]
- 004b4924 bytes 938c1e94
+ 004b4964 bytes 838d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ee92a46b0b6648d40bf4072c04cd50"></a>

### [`004b4a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md) → [`004b4ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md) _ZNK5Botan9SCAN_Name3argEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.12% / 新版 96.12%

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
      "definition_site": "004b4b8c",
      "incomplete_value": false,
      "site": "004b4b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:505:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4b4c",
      "incomplete_value": false,
      "site": "004b4b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:4c5:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b4bb8",
      "incomplete_value": false,
      "site": "004b4bc0",
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
            "const:a51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4b78",
      "incomplete_value": false,
      "site": "004b4b80",
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
            "const:a11:8"
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
      "definition_site": "004b4bf0",
      "incomplete_value": false,
      "site": "004b4bf8",
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
            "const:48c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4bb0",
      "incomplete_value": false,
      "site": "004b4bb8",
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
            "const:3b0:8"
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
      "004b4b8c",
      "PARAM",
      [
        "storage",
        "002bc4c5",
        null,
        "string"
      ]
    ],
    [
      "004b4bb8",
      "PARAM",
      [
        "storage",
        "002b3a11",
        null,
        "string"
      ]
    ],
    [
      "004b4bf0",
      "PARAM",
      [
        "storage",
        "002a63b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b4b8c",
      "PARAM",
      [
        "storage",
        "002bc505",
        null,
        "string"
      ]
    ],
    [
      "004b4bb8",
      "PARAM",
      [
        "storage",
        "002b3a51",
        null,
        "string"
      ]
    ],
    [
      "004b4bf0",
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b4b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4b58) · [`004b4b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4b78) · [`004b4b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4b80)
- 新版 `004b4b98`（命令位置の公開資料なし） · `004b4bb8`（命令位置の公開資料なし） · `004b4bc0`（命令位置の公開資料なし）

~~~diff
- 004b4b58 ["INT_ADD", "register:40f0:8", ["const:4b4b58:8", "const:4:8"]]
- 004b4b58 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b4b98 ["INT_ADD", "register:40f0:8", ["const:4b4b98:8", "const:4:8"]]
+ 004b4b98 ["CALL", null, ["callee:00c57f60:8"]]
- 004b4b58 bytes 028c1e94
+ 004b4b98 bytes f28c1e94
- 004b4b78 ["COPY", "tmp:0:8", ["const:a11:8"]]
- 004b4b78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b4b78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b4b78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b4bb8 ["COPY", "tmp:0:8", ["const:a51:8"]]
+ 004b4bb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4bb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4bb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b4b78 bytes 21442891
+ 004b4bb8 bytes 21442991
- 004b4b80 ["INT_ADD", "register:40f0:8", ["const:4b4b80:8", "const:4:8"]]
- 004b4b80 ["CALL", null, ["callee:00c57f70:8"]]
+ 004b4bc0 ["INT_ADD", "register:40f0:8", ["const:4b4bc0:8", "const:4:8"]]
+ 004b4bc0 ["CALL", null, ["callee:00c57f70:8"]]
- 004b4b80 bytes fc8b1e94
+ 004b4bc0 bytes ec8c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b93a30983f1298290ad5dbf03ed5acf"></a>

### [`004b5318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md) → [`004b5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md) _ZN5BotaneqERKNS_11OctetStringES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587b0.md) · 呼出先 5件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c58bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bb0.md) · 呼出先 5件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5410",
      "incomplete_value": true,
      "site": "004b5410",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b53d0",
      "incomplete_value": true,
      "site": "004b53d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b543c",
      "incomplete_value": true,
      "site": "004b543c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b53fc",
      "incomplete_value": true,
      "site": "004b53fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
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
      "004b5400",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b542c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b5400",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b542c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b5390) · [`004b53d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b53d0) · [`004b53fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b53fc)
- 新版 `004b53d0`（命令位置の公開資料なし） · `004b5410`（命令位置の公開資料なし） · `004b543c`（命令位置の公開資料なし）

~~~diff
- 004b5390 ["INT_ADD", "register:40f0:8", ["const:4b5390:8", "const:4:8"]]
- 004b5390 ["CALL", null, ["callee:00c58050:8"]]
+ 004b53d0 ["INT_ADD", "register:40f0:8", ["const:4b53d0:8", "const:4:8"]]
+ 004b53d0 ["CALL", null, ["callee:00c58050:8"]]
- 004b5390 bytes 308a1e94
+ 004b53d0 bytes 208b1e94
- 004b53d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b53d0 ["INT_ADD", "register:40f0:8", ["const:4b53d0:8", "const:4:8"]]
- 004b53d0 ["CALLIND", null, ["register:0:8"]]
+ 004b5410 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5410 ["INT_ADD", "register:40f0:8", ["const:4b5410:8", "const:4:8"]]
+ 004b5410 ["CALLIND", null, ["register:0:8"]]
- 004b53d0 bytes 20013fd6
+ 004b5410 bytes 20013fd6
- 004b53fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b53fc ["INT_ADD", "register:40f0:8", ["const:4b53fc:8", "const:4:8"]]
- 004b53fc ["CALLIND", null, ["register:0:8"]]
+ 004b543c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b543c ["INT_ADD", "register:40f0:8", ["const:4b543c:8", "const:4:8"]]
+ 004b543c ["CALLIND", null, ["register:0:8"]]
- 004b53fc bytes 20013fd6
+ 004b543c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89171f0942ccfaba8bade80c597fbdd"></a>

### [`004b5480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md) → [`004b54c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md) _ZN5BotanplERKNS_11OctetStringES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5580",
      "incomplete_value": true,
      "site": "004b5580",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5540",
      "incomplete_value": true,
      "site": "004b5540",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5614",
      "incomplete_value": true,
      "site": "004b5614",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b55d4",
      "incomplete_value": true,
      "site": "004b55d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5658",
      "incomplete_value": true,
      "site": "004b5658",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5618",
      "incomplete_value": true,
      "site": "004b5618",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b5570",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b5604",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b5648",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b5570",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b5604",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b5648",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b5540) · [`004b55d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b55d4) · [`004b5618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b5618)
- 新版 `004b5580`（命令位置の公開資料なし） · `004b5614`（命令位置の公開資料なし） · `004b5658`（命令位置の公開資料なし）

~~~diff
- 004b5540 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5540 ["INT_ADD", "register:40f0:8", ["const:4b5540:8", "const:4:8"]]
- 004b5540 ["CALLIND", null, ["register:0:8"]]
+ 004b5580 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5580 ["INT_ADD", "register:40f0:8", ["const:4b5580:8", "const:4:8"]]
+ 004b5580 ["CALLIND", null, ["register:0:8"]]
- 004b5540 bytes 20013fd6
+ 004b5580 bytes 20013fd6
- 004b55d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b55d4 ["INT_ADD", "register:40f0:8", ["const:4b55d4:8", "const:4:8"]]
- 004b55d4 ["CALLIND", null, ["register:0:8"]]
+ 004b5614 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5614 ["INT_ADD", "register:40f0:8", ["const:4b5614:8", "const:4:8"]]
+ 004b5614 ["CALLIND", null, ["register:0:8"]]
- 004b55d4 bytes 20013fd6
+ 004b5614 bytes 20013fd6
- 004b5618 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5618 ["INT_ADD", "register:40f0:8", ["const:4b5618:8", "const:4:8"]]
- 004b5618 ["CALLIND", null, ["register:0:8"]]
+ 004b5658 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5658 ["INT_ADD", "register:40f0:8", ["const:4b5658:8", "const:4:8"]]
+ 004b5658 ["CALLIND", null, ["register:0:8"]]
- 004b5618 bytes 20013fd6
+ 004b5658 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f1a1299c74e8ad5010170274e900396"></a>

### [`004b5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md) → [`004b5a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md) _ZN5Botan13base64_encodeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5c14",
      "incomplete_value": false,
      "site": "004b5c20",
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
            "const:599:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5bd4",
      "incomplete_value": false,
      "site": "004b5be0",
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
            "const:4bd:8"
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
      "definition_site": "004b5c1c",
      "incomplete_value": false,
      "site": "004b5c20",
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
            "const:dcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5bdc",
      "incomplete_value": false,
      "site": "004b5be0",
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
            "const:267:8"
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
      "004b5bd8",
      "PARAM",
      [
        "storage",
        "002b8131",
        null,
        "string"
      ]
    ],
    [
      "004b5be4",
      "PARAM",
      [
        "storage",
        "002a9aa5",
        null,
        "string"
      ]
    ],
    [
      "004b5bf0",
      "PARAM",
      [
        "storage",
        "002bb309",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5bd8",
      "PARAM",
      [
        "storage",
        "002b8171",
        null,
        "string"
      ]
    ],
    [
      "004b5be4",
      "PARAM",
      [
        "storage",
        "002a9b72",
        null,
        "string"
      ]
    ],
    [
      "004b5bf0",
      "PARAM",
      [
        "storage",
        "002bb349",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5be0) · [`004b5ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5ad8) · [`004b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5af8)
- 新版 `004b5c20`（命令位置の公開資料なし） · `004b5b18`（命令位置の公開資料なし） · `004b5b38`（命令位置の公開資料なし）

~~~diff
- 004b5be0 ["INT_ADD", "register:40f0:8", ["const:4b5be0:8", "const:4:8"]]
- 004b5be0 ["CALL", null, ["callee:00c58650:8"]]
+ 004b5c20 ["INT_ADD", "register:40f0:8", ["const:4b5c20:8", "const:4:8"]]
+ 004b5c20 ["CALL", null, ["callee:00c58650:8"]]
- 004b5be0 bytes 9c891e94
+ 004b5c20 bytes 8c8a1e94
- 004b5ad8 ["INT_ADD", "register:40f0:8", ["const:4b5ad8:8", "const:4:8"]]
- 004b5ad8 ["CALL", null, ["callee:00c57e90:8"]]
+ 004b5b18 ["INT_ADD", "register:40f0:8", ["const:4b5b18:8", "const:4:8"]]
+ 004b5b18 ["CALL", null, ["callee:00c57e90:8"]]
- 004b5ad8 bytes ee871e94
+ 004b5b18 bytes de881e94
- 004b5af8 ["INT_ADD", "register:40f0:8", ["const:4b5af8:8", "const:4:8"]]
- 004b5af8 ["CALL", null, ["callee:00c58090:8"]]
+ 004b5b38 ["INT_ADD", "register:40f0:8", ["const:4b5b38:8", "const:4:8"]]
+ 004b5b38 ["CALL", null, ["callee:00c58090:8"]]
- 004b5af8 bytes 66881e94
+ 004b5b38 bytes 56891e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32319943477c852106ccabdc13490ebb"></a>

### [`004b5c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md) → [`004b5c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md) _ZN5Botan13base64_decodeEPhPKcmRmbb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587e0.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58be0.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5e64",
      "incomplete_value": false,
      "site": "004b5e78",
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
            "const:81c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5e24",
      "incomplete_value": false,
      "site": "004b5e38",
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
            "const:7dc:8"
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
      "definition_site": "004b5e90",
      "incomplete_value": false,
      "site": "004b5e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5e50",
      "incomplete_value": false,
      "site": "004b5e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5eb0",
      "incomplete_value": false,
      "site": "004b5eb8",
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
            "const:6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5e70",
      "incomplete_value": false,
      "site": "004b5e78",
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
            "const:f9f:8"
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
      "004b5d80",
      "DATA",
      [
        "storage",
        "002cacdc",
        null,
        null
      ]
    ],
    [
      "004b5e00",
      "DATA",
      [
        "storage",
        "002cacdc",
        null,
        null
      ]
    ],
    [
      "004b5e64",
      "PARAM",
      [
        "storage",
        "002ae7dc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b5d80",
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      "004b5e00",
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      "004b5e64",
      "PARAM",
      [
        "storage",
        "002ae81c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e38) · [`004b5e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e58) · [`004b5e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e78)
- 新版 `004b5e78`（命令位置の公開資料なし） · `004b5e98`（命令位置の公開資料なし） · `004b5eb8`（命令位置の公開資料なし）

~~~diff
- 004b5e38 ["INT_ADD", "register:40f0:8", ["const:4b5e38:8", "const:4:8"]]
- 004b5e38 ["CALL", null, ["callee:00441e94:8"]]
+ 004b5e78 ["INT_ADD", "register:40f0:8", ["const:4b5e78:8", "const:4:8"]]
+ 004b5e78 ["CALL", null, ["callee:00441e94:8"]]
- 004b5e38 bytes 0730fe97
+ 004b5e78 bytes 0730fe97
- 004b5e58 ["INT_ADD", "register:40f0:8", ["const:4b5e58:8", "const:4:8"]]
- 004b5e58 ["CALL", null, ["callee:00441e94:8"]]
+ 004b5e98 ["INT_ADD", "register:40f0:8", ["const:4b5e98:8", "const:4:8"]]
+ 004b5e98 ["CALL", null, ["callee:00441e94:8"]]
- 004b5e58 bytes ff2ffe97
+ 004b5e98 bytes ff2ffe97
- 004b5e78 ["INT_ADD", "register:40f0:8", ["const:4b5e78:8", "const:4:8"]]
- 004b5e78 ["CALL", null, ["callee:00441e94:8"]]
+ 004b5eb8 ["INT_ADD", "register:40f0:8", ["const:4b5eb8:8", "const:4:8"]]
+ 004b5eb8 ["CALL", null, ["callee:00441e94:8"]]
- 004b5e78 bytes f72ffe97
+ 004b5eb8 bytes f72ffe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-837eff27ce3e0a0a8b9b9e1d4081d2cd"></a>

### [`004b5fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md) → [`004b6028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md) _ZN5Botan13base64_decodeEPhPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bf0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b60a4",
      "incomplete_value": false,
      "site": "004b60ac",
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
            "const:bf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b6064",
      "incomplete_value": false,
      "site": "004b606c",
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
            "const:b26:8"
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
      "definition_site": "004b60e0",
      "incomplete_value": true,
      "site": "004b60ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b60a0",
      "incomplete_value": true,
      "site": "004b60ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "definition_site": "004b60dc",
      "incomplete_value": false,
      "site": "004b60ec",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b609c",
      "incomplete_value": false,
      "site": "004b60ac",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b60a4",
      "PARAM",
      [
        "storage",
        "002a8b26",
        null,
        "string"
      ]
    ],
    [
      "004b60dc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b60e0",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b60a4",
      "PARAM",
      [
        "storage",
        "002a8bf3",
        null,
        "string"
      ]
    ],
    [
      "004b60dc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b60e0",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b606c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b606c) · [`004b60ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b60ac) · [`004b601c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b601c)
- 新版 `004b60ac`（命令位置の公開資料なし） · `004b60ec`（命令位置の公開資料なし） · `004b605c`（命令位置の公開資料なし）

~~~diff
- 004b606c ["INT_ADD", "register:40f0:8", ["const:4b606c:8", "const:4:8"]]
- 004b606c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b60ac ["INT_ADD", "register:40f0:8", ["const:4b60ac:8", "const:4:8"]]
+ 004b60ac ["CALL", null, ["callee:0043ddd8:8"]]
- 004b606c bytes 4b1ffe97
+ 004b60ac bytes 4b1ffe97
- 004b60ac ["INT_ADD", "register:40f0:8", ["const:4b60ac:8", "const:4:8"]]
- 004b60ac ["CALL", null, ["callee:00c57f10:8"]]
+ 004b60ec ["INT_ADD", "register:40f0:8", ["const:4b60ec:8", "const:4:8"]]
+ 004b60ec ["CALL", null, ["callee:00c57f10:8"]]
- 004b60ac bytes 99861e94
+ 004b60ec bytes 89871e94
- 004b601c ["INT_ADD", "register:40f0:8", ["const:4b601c:8", "const:4:8"]]
- 004b601c ["CALL", null, ["callee:00c58be0:8"]]
+ 004b605c ["INT_ADD", "register:40f0:8", ["const:4b605c:8", "const:4:8"]]
+ 004b605c ["CALL", null, ["callee:00c58be0:8"]]
- 004b601c bytes f1891e94
+ 004b605c bytes e18a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b3156fd5d2117817b51b0279c02215"></a>

### [`004b638c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md) → [`004b63cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md) _ZNK5Botan6BigInt12encoded_sizeENS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b65f4",
      "incomplete_value": false,
      "site": "004b65fc",
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
            "const:fa3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b65b4",
      "incomplete_value": false,
      "site": "004b65bc",
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
            "const:f63:8"
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
      "definition_site": "004b6630",
      "incomplete_value": true,
      "site": "004b663c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b65f0",
      "incomplete_value": true,
      "site": "004b65fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
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
      "definition_site": "004b662c",
      "incomplete_value": false,
      "site": "004b663c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b65ec",
      "incomplete_value": false,
      "site": "004b65fc",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b656c",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "004b65f4",
      "PARAM",
      [
        "storage",
        "002b5f63",
        null,
        "string"
      ]
    ],
    [
      "004b662c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b656c",
      "READ",
      [
        "storage",
        "002c4288",
        null,
        "undefined8"
      ]
    ],
    [
      "004b65f4",
      "PARAM",
      [
        "storage",
        "002b5fa3",
        null,
        "string"
      ]
    ],
    [
      "004b662c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b65bc) · [`004b65fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b65fc) · [`004b652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b652c)
- 新版 `004b65fc`（命令位置の公開資料なし） · `004b663c`（命令位置の公開資料なし） · `004b656c`（命令位置の公開資料なし）

~~~diff
- 004b65bc ["INT_ADD", "register:40f0:8", ["const:4b65bc:8", "const:4:8"]]
- 004b65bc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b65fc ["INT_ADD", "register:40f0:8", ["const:4b65fc:8", "const:4:8"]]
+ 004b65fc ["CALL", null, ["callee:0043ddd8:8"]]
- 004b65bc bytes f71dfe97
+ 004b65fc bytes f71dfe97
- 004b65fc ["INT_ADD", "register:40f0:8", ["const:4b65fc:8", "const:4:8"]]
- 004b65fc ["CALL", null, ["callee:00c57f10:8"]]
+ 004b663c ["INT_ADD", "register:40f0:8", ["const:4b663c:8", "const:4:8"]]
+ 004b663c ["CALL", null, ["callee:00c57f10:8"]]
- 004b65fc bytes 45851e94
+ 004b663c bytes 35861e94
- 004b652c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:248:8"]]
- 004b652c ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 004b652c ["COPY", "register:5048:8", ["const:0:8"]]
- 004b652c ["COPY", "register:5050:8", ["const:0:8"]]
+ 004b656c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
+ 004b656c ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b656c ["COPY", "register:5048:8", ["const:0:8"]]
+ 004b656c ["COPY", "register:5050:8", ["const:0:8"]]
- 004b652c bytes 222541fd
+ 004b656c bytes 224541fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88268420bc81c9c16c58b4a0aefc6c3"></a>

### [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) → [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) _ZN5Botan6divideERKNS_6BigIntES2_RS0_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58750.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md) [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 1件 [`00c58b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b50.md) · 呼出先 21件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bb8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md) [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b67f4",
      "incomplete_value": true,
      "site": "004b67f8",
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
      "definition_site": "004b67b4",
      "incomplete_value": true,
      "site": "004b67b8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b6818",
      "incomplete_value": true,
      "site": "004b681c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b67d8",
      "incomplete_value": true,
      "site": "004b67dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
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
      "definition_site": "004b6814",
      "incomplete_value": false,
      "site": "004b681c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b67d4",
      "incomplete_value": false,
      "site": "004b67dc",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b67e0",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b67f8",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b6814",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b67e0",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b67f8",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b6814",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b67dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b67dc) · [`004b68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b68a4) · [`004b6978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b6978)
- 新版 `004b681c`（命令位置の公開資料なし） · `004b68e4`（命令位置の公開資料なし） · `004b69b8`（命令位置の公開資料なし）

~~~diff
- 004b67dc ["INT_ADD", "register:40f0:8", ["const:4b67dc:8", "const:4:8"]]
- 004b67dc ["CALL", null, ["callee:00c57f10:8"]]
+ 004b681c ["INT_ADD", "register:40f0:8", ["const:4b681c:8", "const:4:8"]]
+ 004b681c ["CALL", null, ["callee:00c57f10:8"]]
- 004b67dc bytes cd841e94
+ 004b681c bytes bd851e94
- 004b68a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b68a4 ["INT_ADD", "register:40f0:8", ["const:4b68a4:8", "const:4:8"]]
- 004b68a4 ["CALLIND", null, ["register:0:8"]]
+ 004b68e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b68e4 ["INT_ADD", "register:40f0:8", ["const:4b68e4:8", "const:4:8"]]
+ 004b68e4 ["CALLIND", null, ["register:0:8"]]
- 004b68a4 bytes 20013fd6
+ 004b68e4 bytes 20013fd6
- 004b6978 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b6978 ["INT_ADD", "register:40f0:8", ["const:4b6978:8", "const:4:8"]]
- 004b6978 ["CALLIND", null, ["register:0:8"]]
+ 004b69b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b69b8 ["INT_ADD", "register:40f0:8", ["const:4b69b8:8", "const:4:8"]]
+ 004b69b8 ["CALLIND", null, ["register:0:8"]]
- 004b6978 bytes 20013fd6
+ 004b69b8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240abc231d9596a16dfae9c4199fdbfd"></a>

### [`004b72d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md) → [`004b7318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md) _ZN5Botan7Charset10digit2charEh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58760.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b60.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b7380",
      "incomplete_value": false,
      "site": "004b7388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:1d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7340",
      "incomplete_value": false,
      "site": "004b7348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:105:8"
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
      "definition_site": "004b73bc",
      "incomplete_value": true,
      "site": "004b73c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b737c",
      "incomplete_value": true,
      "site": "004b7388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
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
      "definition_site": "004b73b8",
      "incomplete_value": false,
      "site": "004b73c8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b7378",
      "incomplete_value": false,
      "site": "004b7388",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b7380",
      "PARAM",
      [
        "storage",
        "002a4105",
        null,
        "string"
      ]
    ],
    [
      "004b73b8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b73bc",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7380",
      "PARAM",
      [
        "storage",
        "002a41d2",
        null,
        "string"
      ]
    ],
    [
      "004b73b8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b73bc",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7348) · [`004b7388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7388) · [`004b7334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7334)
- 新版 `004b7388`（命令位置の公開資料なし） · `004b73c8`（命令位置の公開資料なし） · `004b7374`（命令位置の公開資料なし）

~~~diff
- 004b7348 ["INT_ADD", "register:40f0:8", ["const:4b7348:8", "const:4:8"]]
- 004b7348 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b7388 ["INT_ADD", "register:40f0:8", ["const:4b7388:8", "const:4:8"]]
+ 004b7388 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b7348 bytes 941afe97
+ 004b7388 bytes 941afe97
- 004b7388 ["INT_ADD", "register:40f0:8", ["const:4b7388:8", "const:4:8"]]
- 004b7388 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b73c8 ["INT_ADD", "register:40f0:8", ["const:4b73c8:8", "const:4:8"]]
+ 004b73c8 ["CALL", null, ["callee:00c57f10:8"]]
- 004b7388 bytes e2811e94
+ 004b73c8 bytes d2821e94
- 004b7334 ["INT_ADD", "register:40f0:8", ["const:4b7334:8", "const:4:8"]]
- 004b7334 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b7374 ["INT_ADD", "register:40f0:8", ["const:4b7374:8", "const:4:8"]]
+ 004b7374 ["CALL", null, ["callee:00c57ef0:8"]]
- 004b7334 bytes ef811e94
+ 004b7374 bytes df821e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f333b48a5e41d143f9e4dc6c4e955a77"></a>

### [`004b74cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md) → [`004b750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md) _ZN5Botan6BigInt11encode_1363EPhmRKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c60.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b7608",
      "incomplete_value": false,
      "site": "004b7610",
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
            "const:f74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b75c8",
      "incomplete_value": false,
      "site": "004b75d0",
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
            "const:f34:8"
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
      "definition_site": "004b7644",
      "incomplete_value": true,
      "site": "004b7650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7604",
      "incomplete_value": true,
      "site": "004b7610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:998:8"
              ]
            ]
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
      "definition_site": "004b7640",
      "incomplete_value": false,
      "site": "004b7650",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b7600",
      "incomplete_value": false,
      "site": "004b7610",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004b7608",
      "PARAM",
      [
        "storage",
        "002b5f34",
        null,
        "string"
      ]
    ],
    [
      "004b7640",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b7644",
      "READ",
      [
        "storage",
        "00c9a998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7608",
      "PARAM",
      [
        "storage",
        "002b5f74",
        null,
        "string"
      ]
    ],
    [
      "004b7640",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b7644",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b75d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b75d0) · [`004b7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b7610) · [`004b75bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b75bc)
- 新版 `004b7610`（命令位置の公開資料なし） · `004b7650`（命令位置の公開資料なし） · `004b75fc`（命令位置の公開資料なし）

~~~diff
- 004b75d0 ["INT_ADD", "register:40f0:8", ["const:4b75d0:8", "const:4:8"]]
- 004b75d0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b7610 ["INT_ADD", "register:40f0:8", ["const:4b7610:8", "const:4:8"]]
+ 004b7610 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b75d0 bytes f219fe97
+ 004b7610 bytes f219fe97
- 004b7610 ["INT_ADD", "register:40f0:8", ["const:4b7610:8", "const:4:8"]]
- 004b7610 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b7650 ["INT_ADD", "register:40f0:8", ["const:4b7650:8", "const:4:8"]]
+ 004b7650 ["CALL", null, ["callee:00c57f10:8"]]
- 004b7610 bytes 40811e94
+ 004b7650 bytes 30821e94
- 004b75bc ["INT_ADD", "register:40f0:8", ["const:4b75bc:8", "const:4:8"]]
- 004b75bc ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b75fc ["INT_ADD", "register:40f0:8", ["const:4b75fc:8", "const:4:8"]]
+ 004b75fc ["CALL", null, ["callee:00c57ef0:8"]]
- 004b75bc bytes 4d811e94
+ 004b75fc bytes 3d821e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

