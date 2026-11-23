# v16.0.0 → v16.0.1 · 最優先の変更候補 (28)

[一覧の目次](README.md)

<a id="compare-933247b9b0d356980436ffd844db858f"></a>

### [`00638dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00638/00638dac.md) → [`00638dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00638/00638dec.md) FUN_00638dec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00550bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00550c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c1c.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00638f18",
      "incomplete_value": false,
      "site": "00638f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638ed8",
      "incomplete_value": false,
      "site": "00638ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "definition_site": "00638f40",
      "incomplete_value": false,
      "site": "00638f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638f00",
      "incomplete_value": false,
      "site": "00638f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "definition_site": "00638ef4",
      "incomplete_value": true,
      "site": "00638efc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638eb4",
      "incomplete_value": true,
      "site": "00638ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
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
      "00638ef4",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00638ef4",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00638f18",
      "DATA",
      [
        "storage",
        "00c732a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638ef4",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "00638ef4",
      "PARAM",
      [
        "storage",
        "00ca5cd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00638f18",
      "DATA",
      [
        "storage",
        "00c736a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00638/00638dac.md#insn-00638ebc) · [`00638de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00638/00638dac.md#insn-00638de4) · [`00638dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00638/00638dac.md#insn-00638dec)
- 新版 `00638efc`（命令位置の公開資料なし） · `00638e24`（命令位置の公開資料なし） · `00638e2c`（命令位置の公開資料なし）

~~~diff
- 00638ebc ["INT_ADD", "register:40f0:8", ["const:638ebc:8", "const:4:8"]]
- 00638ebc ["CALL", null, ["callee:00561d34:8"]]
+ 00638efc ["INT_ADD", "register:40f0:8", ["const:638efc:8", "const:4:8"]]
+ 00638efc ["CALL", null, ["callee:00561d34:8"]]
- 00638ebc bytes 8ea3fc97
+ 00638efc bytes 8ea3fc97
- 00638de4 ["INT_ADD", "register:40f0:8", ["const:638de4:8", "const:4:8"]]
- 00638de4 ["CALL", null, ["callee:006376e8:8"]]
+ 00638e24 ["INT_ADD", "register:40f0:8", ["const:638e24:8", "const:4:8"]]
+ 00638e24 ["CALL", null, ["callee:006376e8:8"]]
- 00638de4 bytes 31faff97
+ 00638e24 bytes 31faff97
- 00638dec ["INT_ADD", "register:40f0:8", ["const:638dec:8", "const:4:8"]]
- 00638dec ["CALL", null, ["callee:00550c20:8"]]
+ 00638e2c ["INT_ADD", "register:40f0:8", ["const:638e2c:8", "const:4:8"]]
+ 00638e2c ["CALL", null, ["callee:00550c20:8"]]
- 00638dec bytes 7d5ffc97
+ 00638e2c bytes 7d5ffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d39f688cfe5e591054b1d3681558fc1"></a>

### [`006399f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/006399f8.md) → [`00639a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639a38.md) FUN_00639a38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006395d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/006395d0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00639610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639610.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00639a44",
      "incomplete_value": false,
      "site": "00639a48",
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
      "definition_site": "00639a04",
      "incomplete_value": false,
      "site": "00639a08",
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
      "00639a44",
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
      "00639a44",
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

- 旧版 [`00639a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/006399f8.md#insn-00639a08) · [`00639a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/006399f8.md#insn-00639a04)
- 新版 `00639a48`（命令位置の公開資料なし） · `00639a44`（命令位置の公開資料なし）

~~~diff
- 00639a08 ["INT_ADD", "register:40f0:8", ["const:639a08:8", "const:4:8"]]
- 00639a08 ["CALL", null, ["callee:0043b778:8"]]
+ 00639a48 ["INT_ADD", "register:40f0:8", ["const:639a48:8", "const:4:8"]]
+ 00639a48 ["CALL", null, ["callee:0043b778:8"]]
- 00639a08 bytes 4c07f897
+ 00639a48 bytes 4c07f897
- 00639a04 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00639a04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00639a04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00639a04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00639a44 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00639a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00639a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00639a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00639a04 bytes 00303c91
+ 00639a44 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9265cba435c59f9ae5f0fd97a522dae6"></a>

### [`00639bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639bbc.md) → [`00639bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639bfc.md) FUN_00639bfc

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
      "definition_site": "00639c10",
      "incomplete_value": false,
      "site": "00639c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639bd0",
      "incomplete_value": false,
      "site": "00639bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "00639c14",
      "DATA",
      [
        "storage",
        "00c732a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639c14",
      "DATA",
      [
        "storage",
        "00c736a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639bbc.md#insn-00639bc8) · [`00639bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639bbc.md#insn-00639bd0)
- 新版 `00639c08`（命令位置の公開資料なし） · `00639c10`（命令位置の公開資料なし）

~~~diff
- 00639bc8 ["INT_ADD", "register:40f0:8", ["const:639bc8:8", "const:4:8"]]
- 00639bc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00639c08 ["INT_ADD", "register:40f0:8", ["const:639c08:8", "const:4:8"]]
+ 00639c08 ["CALL", null, ["callee:00c57e90:8"]]
- 00639bc8 bytes b2771894
+ 00639c08 bytes a2781894
- 00639bd0 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00639bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639c10 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00639c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639bd0 bytes 08810a91
+ 00639c10 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e962b97c7d165487b4b6d2333d06b5"></a>

### [`00639c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c24.md) → [`00639c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639c64.md) FUN_00639c64

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
      "definition_site": "00639c78",
      "incomplete_value": false,
      "site": "00639c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639c38",
      "incomplete_value": false,
      "site": "00639c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "00639c7c",
      "DATA",
      [
        "storage",
        "00c73320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639c7c",
      "DATA",
      [
        "storage",
        "00c73720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c24.md#insn-00639c38) · [`00639c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c24.md#insn-00639c4c) · [`00639c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c24.md#insn-00639c6c)
- 新版 `00639c78`（命令位置の公開資料なし） · `00639c8c`（命令位置の公開資料なし） · `00639cac`（命令位置の公開資料なし）

~~~diff
- 00639c38 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00639c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639c78 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00639c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639c38 bytes 08810c91
+ 00639c78 bytes 08811c91
- 00639c4c ["INT_ADD", "register:40f0:8", ["const:639c4c:8", "const:4:8"]]
- 00639c4c ["CALL", null, ["callee:00c53d00:8"]]
+ 00639c8c ["INT_ADD", "register:40f0:8", ["const:639c8c:8", "const:4:8"]]
+ 00639c8c ["CALL", null, ["callee:00c53d00:8"]]
- 00639c4c bytes 25671894
+ 00639c8c bytes 1d681894
- 00639c6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00639c6c ["INT_ADD", "register:40f0:8", ["const:639c6c:8", "const:4:8"]]
- 00639c6c ["CALLIND", null, ["register:0:8"]]
+ 00639cac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00639cac ["INT_ADD", "register:40f0:8", ["const:639cac:8", "const:4:8"]]
+ 00639cac ["CALLIND", null, ["register:0:8"]]
- 00639c6c bytes 00013fd6
+ 00639cac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb2f4abe10b5c3a4ffca4d7a295f121a"></a>

### [`00639c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c80.md) → [`00639cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639cc0.md) FUN_00639cc0

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
      "definition_site": "00639cd8",
      "incomplete_value": false,
      "site": "00639cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639c98",
      "incomplete_value": false,
      "site": "00639c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "00639cdc",
      "DATA",
      [
        "storage",
        "00c73320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639cdc",
      "DATA",
      [
        "storage",
        "00c73720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c80.md#insn-00639c98) · [`00639cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c80.md#insn-00639cac) · [`00639cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639c80.md#insn-00639cc0)
- 新版 `00639cd8`（命令位置の公開資料なし） · `00639cec`（命令位置の公開資料なし） · `00639d00`（命令位置の公開資料なし）

~~~diff
- 00639c98 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00639c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639cd8 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00639cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639c98 bytes 08810c91
+ 00639cd8 bytes 08811c91
- 00639cac ["INT_ADD", "register:40f0:8", ["const:639cac:8", "const:4:8"]]
- 00639cac ["CALL", null, ["callee:00c53d00:8"]]
+ 00639cec ["INT_ADD", "register:40f0:8", ["const:639cec:8", "const:4:8"]]
+ 00639cec ["CALL", null, ["callee:00c53d00:8"]]
- 00639cac bytes 0d671894
+ 00639cec bytes 05681894
- 00639cc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00639cc0 ["INT_ADD", "register:40f0:8", ["const:639cc0:8", "const:4:8"]]
- 00639cc0 ["CALLIND", null, ["register:0:8"]]
+ 00639d00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00639d00 ["INT_ADD", "register:40f0:8", ["const:639d00:8", "const:4:8"]]
+ 00639d00 ["CALLIND", null, ["register:0:8"]]
- 00639cc0 bytes 00013fd6
+ 00639d00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f2ff4b7d4a50dacfed48eef7c6a11c"></a>

### [`00639cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639cdc.md) → [`00639d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639d1c.md) FUN_00639d1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00639d40",
      "incomplete_value": true,
      "site": "00639d40",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639d00",
      "incomplete_value": true,
      "site": "00639d00",
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
      "00639d40",
      "DATA",
      [
        "storage",
        "00c73320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639d40",
      "DATA",
      [
        "storage",
        "00c73720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639cdc.md#insn-00639cf0) · [`00639cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639cdc.md#insn-00639cfc) · [`00639d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639cdc.md#insn-00639d18)
- 新版 `00639d30`（命令位置の公開資料なし） · `00639d3c`（命令位置の公開資料なし） · `00639d58`（命令位置の公開資料なし）

~~~diff
- 00639cf0 ["INT_ADD", "register:40f0:8", ["const:639cf0:8", "const:4:8"]]
- 00639cf0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00639d30 ["INT_ADD", "register:40f0:8", ["const:639d30:8", "const:4:8"]]
+ 00639d30 ["CALL", null, ["callee:00c57e90:8"]]
- 00639cf0 bytes 68771894
+ 00639d30 bytes 58781894
- 00639cfc ["COPY", "tmp:0:8", ["const:320:8"]]
- 00639cfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00639cfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00639cfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00639d3c ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00639d3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00639d3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00639d3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00639cfc bytes 29810c91
+ 00639d3c bytes 29811c91
- 00639d18 ["INT_ADD", "register:40f0:8", ["const:639d18:8", "const:4:8"]]
- 00639d18 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00639d58 ["INT_ADD", "register:40f0:8", ["const:639d58:8", "const:4:8"]]
+ 00639d58 ["CALL", null, ["callee:00c53cd0:8"]]
- 00639d18 bytes e6661894
+ 00639d58 bytes de671894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21850ec4f1b2a8c11e8bdf3401cc974b"></a>

### [`00639d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639d2c.md) → [`00639d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639d6c.md) FUN_00639d6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00639d78",
      "incomplete_value": true,
      "site": "00639d78",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639d38",
      "incomplete_value": true,
      "site": "00639d38",
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
      "00639d78",
      "DATA",
      [
        "storage",
        "00c73320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639d78",
      "DATA",
      [
        "storage",
        "00c73720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639d2c.md#insn-00639d34) · [`00639d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639d2c.md#insn-00639d54)
- 新版 `00639d74`（命令位置の公開資料なし） · `00639d94`（命令位置の公開資料なし）

~~~diff
- 00639d34 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00639d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00639d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00639d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00639d74 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00639d74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00639d74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00639d74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00639d34 bytes 29810c91
+ 00639d74 bytes 29811c91
- 00639d54 ["INT_ADD", "register:40f0:8", ["const:639d54:8", "const:4:8"]]
- 00639d54 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00639d94 ["INT_ADD", "register:40f0:8", ["const:639d94:8", "const:4:8"]]
+ 00639d94 ["CALL", null, ["callee:00c53cd0:8"]]
- 00639d54 bytes d7661894
+ 00639d94 bytes cf671894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f659d069316dc4ee988a2a43aea0f4f4"></a>

### [`00639ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ef0.md) → [`00639f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639f30.md) FUN_00639f30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00639f48",
      "incomplete_value": false,
      "site": "00639f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639f08",
      "incomplete_value": false,
      "site": "00639f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "00639f4c",
      "DATA",
      [
        "storage",
        "00c733a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639f4c",
      "DATA",
      [
        "storage",
        "00c737a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ef0.md#insn-00639f4c) · [`00639f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ef0.md#insn-00639f08) · [`00639f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639ef0.md#insn-00639f1c)
- 新版 `00639f8c`（命令位置の公開資料なし） · `00639f48`（命令位置の公開資料なし） · `00639f5c`（命令位置の公開資料なし）

~~~diff
- 00639f4c ["INT_ADD", "register:40f0:8", ["const:639f4c:8", "const:4:8"]]
- 00639f4c ["CALL", null, ["callee:00c57e80:8"]]
+ 00639f8c ["INT_ADD", "register:40f0:8", ["const:639f8c:8", "const:4:8"]]
+ 00639f8c ["CALL", null, ["callee:00c57e80:8"]]
- 00639f4c bytes cd761894
+ 00639f8c bytes bd771894
- 00639f08 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00639f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639f48 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00639f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639f08 bytes 08810e91
+ 00639f48 bytes 08811e91
- 00639f1c ["INT_ADD", "register:40f0:8", ["const:639f1c:8", "const:4:8"]]
- 00639f1c ["CALL", null, ["callee:00c53d00:8"]]
+ 00639f5c ["INT_ADD", "register:40f0:8", ["const:639f5c:8", "const:4:8"]]
+ 00639f5c ["CALL", null, ["callee:00c53d00:8"]]
- 00639f1c bytes 71661894
+ 00639f5c bytes 69671894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b433738bc217d245b3550c1fd322b86e"></a>

### [`00639f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639f68.md) → [`00639fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639fa8.md) FUN_00639fa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00639fc0",
      "incomplete_value": false,
      "site": "00639fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639f80",
      "incomplete_value": false,
      "site": "00639f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "00639fc4",
      "DATA",
      [
        "storage",
        "00c733a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00639fc4",
      "DATA",
      [
        "storage",
        "00c737a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639f68.md#insn-00639f80) · [`00639f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639f68.md#insn-00639f94) · [`00639fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639f68.md#insn-00639fa8)
- 新版 `00639fc0`（命令位置の公開資料なし） · `00639fd4`（命令位置の公開資料なし） · `00639fe8`（命令位置の公開資料なし）

~~~diff
- 00639f80 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00639f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639fc0 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00639fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639f80 bytes 08810e91
+ 00639fc0 bytes 08811e91
- 00639f94 ["INT_ADD", "register:40f0:8", ["const:639f94:8", "const:4:8"]]
- 00639f94 ["CALL", null, ["callee:00c53d00:8"]]
+ 00639fd4 ["INT_ADD", "register:40f0:8", ["const:639fd4:8", "const:4:8"]]
+ 00639fd4 ["CALL", null, ["callee:00c53d00:8"]]
- 00639f94 bytes 53661894
+ 00639fd4 bytes 4b671894
- 00639fa8 ["INT_ADD", "register:40f0:8", ["const:639fa8:8", "const:4:8"]]
- 00639fa8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00639fe8 ["INT_ADD", "register:40f0:8", ["const:639fe8:8", "const:4:8"]]
+ 00639fe8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00639fa8 bytes c2761894
+ 00639fe8 bytes b2771894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1127c84c95d383ded92132bb6a96b88"></a>

### [`00639fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639fe0.md) → [`0063a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a020.md) FUN_0063a020

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0063a050",
      "incomplete_value": false,
      "site": "0063a050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a010",
      "incomplete_value": false,
      "site": "0063a010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "0063a050",
      "DATA",
      [
        "storage",
        "00c733a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a050",
      "DATA",
      [
        "storage",
        "00c737a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639fe0.md#insn-00639ff4) · [`0063a004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639fe0.md#insn-0063a004) · [`0063a034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639fe0.md#insn-0063a034)
- 新版 `0063a034`（命令位置の公開資料なし） · `0063a044`（命令位置の公開資料なし） · `0063a074`（命令位置の公開資料なし）

~~~diff
- 00639ff4 ["INT_ADD", "register:40f0:8", ["const:639ff4:8", "const:4:8"]]
- 00639ff4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0063a034 ["INT_ADD", "register:40f0:8", ["const:63a034:8", "const:4:8"]]
+ 0063a034 ["CALL", null, ["callee:00c57e90:8"]]
- 00639ff4 bytes a7761894
+ 0063a034 bytes 97771894
- 0063a004 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0063a004 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0063a004 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0063a004 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0063a044 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0063a044 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0063a044 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0063a044 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0063a004 bytes 6b810e91
+ 0063a044 bytes 6b811e91
- 0063a034 ["INT_ADD", "register:40f0:8", ["const:63a034:8", "const:4:8"]]
- 0063a034 ["CALL", null, ["callee:0043bb20:8"]]
+ 0063a074 ["INT_ADD", "register:40f0:8", ["const:63a074:8", "const:4:8"]]
+ 0063a074 ["CALL", null, ["callee:0043bb20:8"]]
- 0063a034 bytes ab06f897
+ 0063a074 bytes ab06f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccf38e9c80c1ee6a7eddd404d0f11c6"></a>

### [`0063a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a074.md) → [`0063a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a0b4.md) FUN_0063a0b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0063a0d4",
      "incomplete_value": false,
      "site": "0063a0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a094",
      "incomplete_value": false,
      "site": "0063a094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "0063a0d4",
      "DATA",
      [
        "storage",
        "00c733a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a0d4",
      "DATA",
      [
        "storage",
        "00c737a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a074.md#insn-0063a088) · [`0063a090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a074.md#insn-0063a090) · [`0063a0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a074.md#insn-0063a0c0)
- 新版 `0063a0c8`（命令位置の公開資料なし） · `0063a100`（命令位置の公開資料なし）

~~~diff
- 0063a088 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0063a088 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0063a088 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0063a088 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0063a0c8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0063a0c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0063a0c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0063a0c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0063a088 bytes 29810e91
+ 0063a0c8 bytes 29811e91
- 0063a090 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0063a090 bytes f40300aa
- 0063a0c0 ["INT_ADD", "register:40f0:8", ["const:63a0c0:8", "const:4:8"]]
- 0063a0c0 ["CALL", null, ["callee:0043bb20:8"]]
+ 0063a100 ["INT_ADD", "register:40f0:8", ["const:63a100:8", "const:4:8"]]
+ 0063a100 ["CALL", null, ["callee:0043bb20:8"]]
- 0063a0c0 bytes 8806f897
+ 0063a100 bytes 8806f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efaa19f6927e44271e1bdd955ccb25ff"></a>

### [`0063a1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md) → [`0063a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a200.md) FUN_0063a200

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) [`004823bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004823bc.md) [`004824f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004824f8.md) [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) [`004823fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/004823fc.md) [`00482538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482538.md) [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a2b0",
      "incomplete_value": false,
      "site": "0063a2b4",
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
      "definition_site": "0063a270",
      "incomplete_value": false,
      "site": "0063a274",
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
      "0063a2b4",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a2b4",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md#insn-0063a1ec) · [`0063a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md#insn-0063a1fc) · [`0063a218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a1c0.md#insn-0063a218)
- 新版 `0063a22c`（命令位置の公開資料なし） · `0063a23c`（命令位置の公開資料なし） · `0063a258`（命令位置の公開資料なし）

~~~diff
- 0063a1ec ["INT_ADD", "register:40f0:8", ["const:63a1ec:8", "const:4:8"]]
- 0063a1ec ["CALL", null, ["callee:00481430:8"]]
+ 0063a22c ["INT_ADD", "register:40f0:8", ["const:63a22c:8", "const:4:8"]]
+ 0063a22c ["CALL", null, ["callee:00481430:8"]]
- 0063a1ec bytes 811cf997
+ 0063a22c bytes 811cf997
- 0063a1fc ["INT_ADD", "register:40f0:8", ["const:63a1fc:8", "const:4:8"]]
- 0063a1fc ["CALL", null, ["callee:004823fc:8"]]
+ 0063a23c ["INT_ADD", "register:40f0:8", ["const:63a23c:8", "const:4:8"]]
+ 0063a23c ["CALL", null, ["callee:004823fc:8"]]
- 0063a1fc bytes 7020f997
+ 0063a23c bytes 7020f997
- 0063a218 ["INT_ADD", "register:40f0:8", ["const:63a218:8", "const:4:8"]]
- 0063a218 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0063a258 ["INT_ADD", "register:40f0:8", ["const:63a258:8", "const:4:8"]]
+ 0063a258 ["CALL", null, ["callee:00c53cd0:8"]]
- 0063a218 bytes a6651894
+ 0063a258 bytes 9e661894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2207d40c4825cc8f9bea3d6a74619b"></a>

### [`0063a398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a398.md) → [`0063a3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a3d8.md) _INIT_81

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a414",
      "incomplete_value": true,
      "site": "0063a430",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a3d4",
      "incomplete_value": true,
      "site": "0063a3f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a438",
      "incomplete_value": true,
      "site": "0063a454",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a3f8",
      "incomplete_value": true,
      "site": "0063a414",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a458",
      "incomplete_value": true,
      "site": "0063a474",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a418",
      "incomplete_value": true,
      "site": "0063a434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0063a414",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0063a438",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0063a458",
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
      "0063a414",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0063a438",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0063a458",
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

- 旧版 [`0063a410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a398.md#insn-0063a410) · [`0063a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a398.md#insn-0063a430) · [`0063a5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a398.md#insn-0063a5cc)
- 新版 `0063a450`（命令位置の公開資料なし） · `0063a470`（命令位置の公開資料なし） · `0063a60c`（命令位置の公開資料なし）

~~~diff
- 0063a410 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0063a410 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0063a410 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0063a410 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0063a450 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0063a450 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0063a450 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0063a450 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0063a410 bytes 4a093691
+ 0063a450 bytes 4a093791
- 0063a430 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0063a430 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0063a430 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0063a430 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0063a470 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0063a470 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0063a470 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0063a470 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0063a430 bytes 4a553a91
+ 0063a470 bytes 4a893d91
- 0063a5cc ["INT_ADD", "register:40f0:8", ["const:63a5cc:8", "const:4:8"]]
- 0063a5cc ["CALL", null, ["callee:00c57e30:8"]]
+ 0063a60c ["INT_ADD", "register:40f0:8", ["const:63a60c:8", "const:4:8"]]
+ 0063a60c ["CALL", null, ["callee:00c57e30:8"]]
- 0063a5cc bytes 19751894
+ 0063a60c bytes 09761894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4942c5575d57210b5174c883807371e5"></a>

### [`0063a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md) → [`0063a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a7a4.md) FUN_0063a7a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0064d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md) · 呼出先 17件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md) [`0046f704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f704.md)
- 新版 呼出元 1件 [`0064d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064d9ec.md) · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md) [`0046f744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f744.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a7ec",
      "incomplete_value": true,
      "site": "0063a7fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:355:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a7ac",
      "incomplete_value": true,
      "site": "0063a7bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:288:8"
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
      "definition_site": "0063a7f0",
      "incomplete_value": true,
      "site": "0063a800",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0063a7b0",
      "incomplete_value": true,
      "site": "0063a7c0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a7f4",
      "incomplete_value": true,
      "site": "0063a804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063a7b4",
      "incomplete_value": true,
      "site": "0063a7c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0063a7d0",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0063a7ec",
      "READ",
      [
        "storage",
        "002a1288",
        null,
        "string"
      ]
    ],
    [
      "0063a7f0",
      "READ",
      [
        "storage",
        "002a1297",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063a7d0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0063a7ec",
      "READ",
      [
        "storage",
        "002a1355",
        null,
        "string"
      ]
    ],
    [
      "0063a7f0",
      "READ",
      [
        "storage",
        "002a1364",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md#insn-0063a840) · [`0063a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md#insn-0063a974) · [`0063a9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md#insn-0063a9b4)
- 新版 `0063a880`（命令位置の公開資料なし） · `0063a9b4`（命令位置の公開資料なし） · `0063a9f4`（命令位置の公開資料なし）

~~~diff
- 0063a840 ["INT_ADD", "register:40f0:8", ["const:63a840:8", "const:4:8"]]
- 0063a840 ["CALL", null, ["callee:0047e60c:8"]]
+ 0063a880 ["INT_ADD", "register:40f0:8", ["const:63a880:8", "const:4:8"]]
+ 0063a880 ["CALL", null, ["callee:0047e60c:8"]]
- 0063a840 bytes 630ff997
+ 0063a880 bytes 630ff997
- 0063a974 ["INT_ADD", "register:40f0:8", ["const:63a974:8", "const:4:8"]]
- 0063a974 ["CALL", null, ["callee:0046e970:8"]]
+ 0063a9b4 ["INT_ADD", "register:40f0:8", ["const:63a9b4:8", "const:4:8"]]
+ 0063a9b4 ["CALL", null, ["callee:0046e970:8"]]
- 0063a974 bytes efcff897
+ 0063a9b4 bytes efcff897
- 0063a9b4 ["INT_ADD", "register:40f0:8", ["const:63a9b4:8", "const:4:8"]]
- 0063a9b4 ["CALL", null, ["callee:008514f8:8"]]
+ 0063a9f4 ["INT_ADD", "register:40f0:8", ["const:63a9f4:8", "const:4:8"]]
+ 0063a9f4 ["CALL", null, ["callee:008514f8:8"]]
- 0063a9b4 bytes c15a0894
+ 0063a9f4 bytes c15a0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a9b43e2246218b84b6d127b043e05a"></a>

### [`0063ad98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063ad98.md) → [`0063add8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063add8.md) FUN_0063add8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) · 呼出先 7件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`0063a728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a728.md) [`006dc824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc824.md)
- 新版 呼出元 2件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006b2b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2b5c.md) · 呼出先 7件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`0063a768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a768.md) [`006dc864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc864.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.40% / 新版 94.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063af34",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063aef4",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "0063b044",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b004",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b054",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b014",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063adf8",
      "DATA",
      [
        "storage",
        "00434780",
        null,
        "byte[47]"
      ]
    ],
    [
      "0063ae10",
      "DATA",
      [
        "storage",
        "00435340",
        null,
        "dword"
      ]
    ],
    [
      "0063ae24",
      "DATA",
      [
        "storage",
        "00434780",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0063adf8",
      "DATA",
      [
        "storage",
        "00434780",
        null,
        "byte[43]"
      ]
    ],
    [
      "0063ae10",
      "DATA",
      [
        "storage",
        "00435340",
        null,
        "uleb128"
      ]
    ],
    [
      "0063ae24",
      "DATA",
      [
        "storage",
        "00434780",
        null,
        "byte[43]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063aef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063ad98.md#insn-0063aef4) · [`0063afd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063ad98.md#insn-0063afd4) · [`0063b004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063ad98.md#insn-0063b004)
- 新版 `0063af34`（命令位置の公開資料なし） · `0063b014`（命令位置の公開資料なし） · `0063b044`（命令位置の公開資料なし）

~~~diff
- 0063aef4 ["INT_ADD", "register:40f0:8", ["const:63aef4:8", "const:4:8"]]
- 0063aef4 ["CALL", null, ["ram:46c984:8"]]
+ 0063af34 ["INT_ADD", "register:40f0:8", ["const:63af34:8", "const:4:8"]]
+ 0063af34 ["CALL", null, ["ram:46c9c4:8"]]
- 0063aef4 bytes a4c6f897
+ 0063af34 bytes a4c6f897
- 0063afd4 ["INT_ADD", "register:40f0:8", ["const:63afd4:8", "const:4:8"]]
- 0063afd4 ["CALL", null, ["callee:008514f8:8"]]
+ 0063b014 ["INT_ADD", "register:40f0:8", ["const:63b014:8", "const:4:8"]]
+ 0063b014 ["CALL", null, ["callee:008514f8:8"]]
- 0063afd4 bytes 39590894
+ 0063b014 bytes 39590894
- 0063b004 ["INT_ADD", "register:40f0:8", ["const:63b004:8", "const:4:8"]]
- 0063b004 ["CALL", null, ["ram:46c984:8"]]
+ 0063b044 ["INT_ADD", "register:40f0:8", ["const:63b044:8", "const:4:8"]]
+ 0063b044 ["CALL", null, ["ram:46c9c4:8"]]
- 0063b004 bytes 60c6f897
+ 0063b044 bytes 60c6f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b9579e64ab6a4a84fdcb62bfd513e0"></a>

### [`0063b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md) → [`0063b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b634.md) FUN_0063b634

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0063c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md) [`0063ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`0063b784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md)
- 新版 呼出元 2件 [`0063c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5cc.md) [`0063cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063cd1c.md) · 呼出先 6件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`0063b7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b7c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b67c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b63c",
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
      "site": "0063b698",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b658",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b78c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b74c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "0063b658",
      "DATA",
      [
        "storage",
        "00434fd0",
        null,
        "dword"
      ]
    ],
    [
      "0063b67c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0063b698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0063b658",
      "DATA",
      [
        "storage",
        "00434fd0",
        "fde_00434fd0",
        "dword"
      ]
    ],
    [
      "0063b67c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0063b698",
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

- 旧版 [`0063b63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md#insn-0063b63c) · [`0063b658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md#insn-0063b658) · [`0063b67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md#insn-0063b67c)
- 新版 `0063b67c`（命令位置の公開資料なし） · `0063b698`（命令位置の公開資料なし） · `0063b6bc`（命令位置の公開資料なし）

~~~diff
- 0063b63c ["INT_ADD", "register:40f0:8", ["const:63b63c:8", "const:4:8"]]
- 0063b63c ["CALL", null, ["ram:46c984:8"]]
+ 0063b67c ["INT_ADD", "register:40f0:8", ["const:63b67c:8", "const:4:8"]]
+ 0063b67c ["CALL", null, ["ram:46c9c4:8"]]
- 0063b63c bytes d2c4f897
+ 0063b67c bytes d2c4f897
- 0063b658 ["INT_ADD", "register:40f0:8", ["const:63b658:8", "const:4:8"]]
- 0063b658 ["CALL", null, ["ram:46c984:8"]]
+ 0063b698 ["INT_ADD", "register:40f0:8", ["const:63b698:8", "const:4:8"]]
+ 0063b698 ["CALL", null, ["ram:46c9c4:8"]]
- 0063b658 bytes cbc4f897
+ 0063b698 bytes cbc4f897
- 0063b67c ["INT_ADD", "register:40f0:8", ["const:63b67c:8", "const:4:8"]]
- 0063b67c ["CALL", null, ["callee:0046d7b0:8"]]
+ 0063b6bc ["INT_ADD", "register:40f0:8", ["const:63b6bc:8", "const:4:8"]]
+ 0063b6bc ["CALL", null, ["callee:0046d7b0:8"]]
- 0063b67c bytes 3dc8f897
+ 0063b6bc bytes 3dc8f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c468335bcb0733cf5fec29b82602da16"></a>

### [`0063b784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md) → [`0063b7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b7c4.md) FUN_0063b7c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0063b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md) [`0064d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md) · 呼出先 16件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md) [`0046f704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f704.md)
- 新版 呼出元 2件 [`0063b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b634.md) [`0064d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064d9ec.md) · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md) [`0046f744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f744.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.12% / 新版 92.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063b814",
      "incomplete_value": true,
      "site": "0063b82c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063b7d4",
      "incomplete_value": true,
      "site": "0063b7ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:740:8"
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
      "definition_site": "0063b830",
      "incomplete_value": true,
      "site": "0063b83c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0063b7f0",
      "incomplete_value": true,
      "site": "0063b7fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:620:8"
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
      "definition_site": "0063ba1c",
      "incomplete_value": true,
      "site": "0063ba34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063b9dc",
      "incomplete_value": true,
      "site": "0063b9f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0063b814",
      "READ",
      [
        "storage",
        "002c2740",
        null,
        null
      ]
    ],
    [
      "0063b830",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ],
    [
      "0063b85c",
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
      "0063b814",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ],
    [
      "0063b830",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ],
    [
      "0063b85c",
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

- 旧版 [`0063b9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md#insn-0063b9b8) · [`0063ba74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b784.md#insn-0063ba74)
- 新版 `0063b7fc`（命令位置の公開資料なし） · `0063b9f8`（命令位置の公開資料なし） · `0063bab4`（命令位置の公開資料なし）

~~~diff
+ 0063b7fc ["COPY", "register:40a8:8", ["const:ca4000:8"]]
+ 0063b7fc bytes 553300b0
- 0063b9b8 ["INT_ADD", "register:40f0:8", ["const:63b9b8:8", "const:4:8"]]
- 0063b9b8 ["CALL", null, ["callee:00c57e30:8"]]
+ 0063b9f8 ["INT_ADD", "register:40f0:8", ["const:63b9f8:8", "const:4:8"]]
+ 0063b9f8 ["CALL", null, ["callee:00c57e30:8"]]
- 0063b9b8 bytes 1e701894
+ 0063b9f8 bytes 0e711894
- 0063ba74 ["INT_ADD", "register:40f0:8", ["const:63ba74:8", "const:4:8"]]
- 0063ba74 ["CALL", null, ["callee:0046e970:8"]]
+ 0063bab4 ["INT_ADD", "register:40f0:8", ["const:63bab4:8", "const:4:8"]]
+ 0063bab4 ["CALL", null, ["callee:0046e970:8"]]
- 0063ba74 bytes afcbf897
+ 0063bab4 bytes afcbf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c5015f58fdee8720dc504f02bb93f1"></a>

### [`0063c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md) → [`0063c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5cc.md) FUN_0063c5cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`006fb1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md) [`006fd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0063b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md) [`0063ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md) [`00652acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652acc.md)
- 新版 呼出元 5件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006ee740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md) [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) [`006fb1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1f4.md) [`006fda2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md) · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0063b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b634.md) [`0063cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063cd1c.md) [`00652b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652b0c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063c5f4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063c5b4",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0063c660",
      "value": [
        "leaf",
        "ram:71c460:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063c620",
      "value": [
        "leaf",
        "ram:71c420:8"
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
      "site": "0063c680",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063c640",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "0063c5f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0063c660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "0063c680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "0063c5f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0063c660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "0063c680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063c5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md#insn-0063c5b4) · [`0063c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md#insn-0063c5e0) · [`0063c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md#insn-0063c620)
- 新版 `0063c5f4`（命令位置の公開資料なし） · `0063c620`（命令位置の公開資料なし） · `0063c660`（命令位置の公開資料なし）

~~~diff
- 0063c5b4 ["INT_ADD", "register:40f0:8", ["const:63c5b4:8", "const:4:8"]]
- 0063c5b4 ["CALL", null, ["ram:71be98:8"]]
+ 0063c5f4 ["INT_ADD", "register:40f0:8", ["const:63c5f4:8", "const:4:8"]]
+ 0063c5f4 ["CALL", null, ["ram:71bed8:8"]]
- 0063c5b4 bytes 397e0394
+ 0063c5f4 bytes 397e0394
- 0063c5e0 ["INT_ADD", "register:40f0:8", ["const:63c5e0:8", "const:4:8"]]
- 0063c5e0 ["CALL", null, ["callee:00c57f40:8"]]
+ 0063c620 ["INT_ADD", "register:40f0:8", ["const:63c620:8", "const:4:8"]]
+ 0063c620 ["CALL", null, ["callee:00c57f40:8"]]
- 0063c5e0 bytes 586d1894
+ 0063c620 bytes 486e1894
- 0063c620 ["INT_ADD", "register:40f0:8", ["const:63c620:8", "const:4:8"]]
- 0063c620 ["CALL", null, ["ram:71c420:8"]]
+ 0063c660 ["INT_ADD", "register:40f0:8", ["const:63c660:8", "const:4:8"]]
+ 0063c660 ["CALL", null, ["ram:71c460:8"]]
- 0063c620 bytes 807f0394
+ 0063c660 bytes 807f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eea99371d3822cf4294b587745fff9e"></a>

### [`0063ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md) → [`0063cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063cd1c.md) FUN_0063cd1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0063c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md) [`0064e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md) [`0064e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0063b5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b5f4.md) [`00652acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652acc.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md)
- 新版 呼出元 4件 [`0063c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5cc.md) [`0064e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e37c.md) [`0064e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e540.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0063b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b634.md) [`00652b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652b0c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063cd48",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063cd08",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0063cdb4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063cd74",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0063cea4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063ce64",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "0063cd48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0063cdb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0063cea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "0063cd48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0063cdb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0063cea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063cd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md#insn-0063cd08) · [`0063cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md#insn-0063cd74) · [`0063ce64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md#insn-0063ce64)
- 新版 `0063cd48`（命令位置の公開資料なし） · `0063cdb4`（命令位置の公開資料なし） · `0063cea4`（命令位置の公開資料なし）

~~~diff
- 0063cd08 ["INT_ADD", "register:40f0:8", ["const:63cd08:8", "const:4:8"]]
- 0063cd08 ["CALL", null, ["ram:71be98:8"]]
+ 0063cd48 ["INT_ADD", "register:40f0:8", ["const:63cd48:8", "const:4:8"]]
+ 0063cd48 ["CALL", null, ["ram:71bed8:8"]]
- 0063cd08 bytes 647c0394
+ 0063cd48 bytes 647c0394
- 0063cd74 ["INT_ADD", "register:40f0:8", ["const:63cd74:8", "const:4:8"]]
- 0063cd74 ["CALL", null, ["ram:71be98:8"]]
+ 0063cdb4 ["INT_ADD", "register:40f0:8", ["const:63cdb4:8", "const:4:8"]]
+ 0063cdb4 ["CALL", null, ["ram:71bed8:8"]]
- 0063cd74 bytes 497c0394
+ 0063cdb4 bytes 497c0394
- 0063ce64 ["INT_ADD", "register:40f0:8", ["const:63ce64:8", "const:4:8"]]
- 0063ce64 ["CALL", null, ["ram:71be98:8"]]
+ 0063cea4 ["INT_ADD", "register:40f0:8", ["const:63cea4:8", "const:4:8"]]
+ 0063cea4 ["CALL", null, ["ram:71bed8:8"]]
- 0063ce64 bytes 0d7c0394
+ 0063cea4 bytes 0d7c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ce3eb72d63e306d08679cf5f024d973"></a>

### [`0063d20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d20c.md) → [`0063d24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d24c.md) FUN_0063d24c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`0063dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dd10.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063d288",
      "incomplete_value": false,
      "site": "0063d28c",
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
      "definition_site": "0063d248",
      "incomplete_value": false,
      "site": "0063d24c",
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
      "definition_site": "0063d2a4",
      "incomplete_value": true,
      "site": "0063d2b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:630:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063d264",
      "incomplete_value": true,
      "site": "0063d274",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5f0:8"
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
      "definition_site": "0063d2a8",
      "incomplete_value": true,
      "site": "0063d2b8",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063d268",
      "incomplete_value": true,
      "site": "0063d278",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "0063d28c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0063d2a4",
      "READ",
      [
        "storage",
        "002bb5f0",
        null,
        "string"
      ]
    ],
    [
      "0063d2a8",
      "READ",
      [
        "storage",
        "002bb5fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063d28c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0063d2a4",
      "READ",
      [
        "storage",
        "002bb630",
        null,
        "string"
      ]
    ],
    [
      "0063d2a8",
      "READ",
      [
        "storage",
        "002bb63a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063d2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d20c.md#insn-0063d2b4) · [`0063d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d20c.md#insn-0063d7e0) · [`0063d7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d20c.md#insn-0063d7e4)
- 新版 `0063d2f4`（命令位置の公開資料なし）

~~~diff
- 0063d2b4 ["INT_ADD", "register:40f0:8", ["const:63d2b4:8", "const:4:8"]]
- 0063d2b4 ["CALL", null, ["callee:0048791c:8"]]
+ 0063d2f4 ["INT_ADD", "register:40f0:8", ["const:63d2f4:8", "const:4:8"]]
+ 0063d2f4 ["CALL", null, ["callee:0048791c:8"]]
- 0063d2b4 bytes 8a29f997
+ 0063d2f4 bytes 8a29f997
- 0063d7e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 0063d7e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0063d7e0 bytes e81300f9
- 0063d7e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 0063d7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0063d7e4 bytes e93700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3da95f25ae5575d485739deab9711b5d"></a>

### [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) → [`0063dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dd10.md) FUN_0063dd10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 28件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 28件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.79% / 新版 98.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063dd50",
      "incomplete_value": false,
      "site": "0063dd54",
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
      "definition_site": "0063dd10",
      "incomplete_value": false,
      "site": "0063dd14",
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
      "definition_site": "0063dd7c",
      "incomplete_value": true,
      "site": "0063dd98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063dd3c",
      "incomplete_value": true,
      "site": "0063dd58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:297:8"
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
      "definition_site": "0063dd9c",
      "incomplete_value": true,
      "site": "0063dd9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0063dd5c",
      "incomplete_value": true,
      "site": "0063dd5c",
      "value": [
        "LOAD",
        "8",
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
      "0063dd54",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0063dd7c",
      "READ",
      [
        "storage",
        "002b6297",
        null,
        "string"
      ]
    ],
    [
      "0063dd84",
      "READ",
      [
        "storage",
        "002b62a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063dd54",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0063dd7c",
      "READ",
      [
        "storage",
        "002b62d7",
        null,
        "string"
      ]
    ],
    [
      "0063dd84",
      "READ",
      [
        "storage",
        "002b62e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063dd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md#insn-0063dd1c) · [`0063dd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md#insn-0063dd9c) · [`0064026c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md#insn-0064026c)
- 新版 `0063dd5c`（命令位置の公開資料なし） · `0063dddc`（命令位置の公開資料なし） · `006402ac`（命令位置の公開資料なし）

~~~diff
- 0063dd1c ["INT_ADD", "register:40f0:8", ["const:63dd1c:8", "const:4:8"]]
- 0063dd1c ["CALL", null, ["callee:0063d24c:8"]]
+ 0063dd5c ["INT_ADD", "register:40f0:8", ["const:63dd5c:8", "const:4:8"]]
+ 0063dd5c ["CALL", null, ["callee:0063d24c:8"]]
- 0063dd1c bytes 3cfdff97
+ 0063dd5c bytes 3cfdff97
- 0063dd9c ["INT_ADD", "register:40f0:8", ["const:63dd9c:8", "const:4:8"]]
- 0063dd9c ["CALL", null, ["callee:0048791c:8"]]
+ 0063dddc ["INT_ADD", "register:40f0:8", ["const:63dddc:8", "const:4:8"]]
+ 0063dddc ["CALL", null, ["callee:0048791c:8"]]
- 0063dd9c bytes d026f997
+ 0063dddc bytes d026f997
- 0064026c ["INT_ADD", "register:40f0:8", ["const:64026c:8", "const:4:8"]]
- 0064026c ["CALL", null, ["ram:640970:8"]]
+ 006402ac ["INT_ADD", "register:40f0:8", ["const:6402ac:8", "const:4:8"]]
+ 006402ac ["CALL", null, ["ram:6409b0:8"]]
- 0064026c bytes c1010094
+ 006402ac bytes c1010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b0c7f80f50c7a9c789646b4b57870f"></a>

### [`006415c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006415c4.md) → [`00641604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641604.md) FUN_00641604

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006430b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00643/006430b0.md) · 呼出先 4件 [`0063d8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d8d4.md) [`006416ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`006430f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00643/006430f0.md) · 呼出先 4件 [`0063d914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d914.md) [`006416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006416ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "site": "0064169c",
      "value": [
        "leaf",
        "ram:63d914:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064165c",
      "value": [
        "leaf",
        "ram:63d8d4:8"
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
      "0064169c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063d8d4"
      ]
    ]
  ],
  "added": [
    [
      "0064169c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063d914"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064165c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006415c4.md#insn-0064165c) · [`0064164c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006415c4.md#insn-0064164c) · [`00641670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006415c4.md#insn-00641670)
- 新版 `0064169c`（命令位置の公開資料なし） · `0064168c`（命令位置の公開資料なし） · `006416b0`（命令位置の公開資料なし）

~~~diff
- 0064165c ["INT_ADD", "register:40f0:8", ["const:64165c:8", "const:4:8"]]
- 0064165c ["CALL", null, ["ram:63d8d4:8"]]
+ 0064169c ["INT_ADD", "register:40f0:8", ["const:64169c:8", "const:4:8"]]
+ 0064169c ["CALL", null, ["ram:63d914:8"]]
- 0064165c bytes 9ef0ff97
+ 0064169c bytes 9ef0ff97
- 0064164c ["INT_ADD", "register:40f0:8", ["const:64164c:8", "const:4:8"]]
- 0064164c ["CALL", null, ["callee:006416ec:8"]]
+ 0064168c ["INT_ADD", "register:40f0:8", ["const:64168c:8", "const:4:8"]]
+ 0064168c ["CALL", null, ["callee:006416ec:8"]]
- 0064164c bytes 18000094
+ 0064168c bytes 18000094
- 00641670 ["INT_ADD", "register:40f0:8", ["const:641670:8", "const:4:8"]]
- 00641670 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006416b0 ["INT_ADD", "register:40f0:8", ["const:6416b0:8", "const:4:8"]]
+ 006416b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00641670 bytes 10591894
+ 006416b0 bytes 005a1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1138d67ecf0672829fa582c5d4a3df"></a>

### [`006416ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md) → [`006416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006416ec.md) FUN_006416ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`006415c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006415c4.md) [`006418c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006418c4.md) [`00641d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641d9c.md) [`00645254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645254.md) [`00645fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md) · 呼出先 2件 [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`00641b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641b20.md)
- 新版 呼出元 9件 [`00641604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641604.md) [`00641904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641904.md) [`00641ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641ddc.md) [`00645294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645294.md) [`00645fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645fe4.md) · 呼出先 2件 [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`00641b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641b60.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

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
      "site": "006417ec",
      "value": [
        "leaf",
        "ram:641b60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006417ac",
      "value": [
        "leaf",
        "ram:641b20:8"
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
      "site": "00641834",
      "value": [
        "leaf",
        "ram:641b60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006417f4",
      "value": [
        "leaf",
        "ram:641b20:8"
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
      "006417ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b20"
      ]
    ],
    [
      "00641834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b20"
      ]
    ]
  ],
  "added": [
    [
      "006417ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b60"
      ]
    ],
    [
      "00641834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006417ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md#insn-006417ac) · [`006417f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md#insn-006417f4) · [`006417d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md#insn-006417d8)
- 新版 `006417ec`（命令位置の公開資料なし） · `00641834`（命令位置の公開資料なし） · `00641818`（命令位置の公開資料なし）

~~~diff
- 006417ac ["INT_ADD", "register:40f0:8", ["const:6417ac:8", "const:4:8"]]
- 006417ac ["CALL", null, ["ram:641b20:8"]]
+ 006417ec ["INT_ADD", "register:40f0:8", ["const:6417ec:8", "const:4:8"]]
+ 006417ec ["CALL", null, ["ram:641b60:8"]]
- 006417ac bytes dd000094
+ 006417ec bytes dd000094
- 006417f4 ["INT_ADD", "register:40f0:8", ["const:6417f4:8", "const:4:8"]]
- 006417f4 ["CALL", null, ["ram:641b20:8"]]
+ 00641834 ["INT_ADD", "register:40f0:8", ["const:641834:8", "const:4:8"]]
+ 00641834 ["CALL", null, ["ram:641b60:8"]]
- 006417f4 bytes cb000094
+ 00641834 bytes cb000094
- 006417d8 ["INT_ADD", "register:40f0:8", ["const:6417d8:8", "const:4:8"]]
- 006417d8 ["CALL", null, ["callee:00470994:8"]]
+ 00641818 ["INT_ADD", "register:40f0:8", ["const:641818:8", "const:4:8"]]
+ 00641818 ["CALL", null, ["callee:00470994:8"]]
- 006417d8 bytes 5fbcf897
+ 00641818 bytes 5fbcf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd2eb2a7184863fbf6188344dc543a8c"></a>

### [`00641fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md) → [`00642010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00642/00642010.md) FUN_00642010

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006430b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00643/006430b0.md) [`00645254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645254.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md)
- 新版 呼出元 2件 [`006430f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00643/006430f0.md) [`00645294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645294.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.74% / 新版 88.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件, `store_destination` 14件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00642188",
      "incomplete_value": true,
      "site": "00642198",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00642148",
      "incomplete_value": true,
      "site": "00642158",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064219c",
      "incomplete_value": true,
      "site": "006421a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064215c",
      "incomplete_value": true,
      "site": "00642160",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00642354",
      "incomplete_value": true,
      "site": "00642360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:15d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00642314",
      "incomplete_value": true,
      "site": "00642320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:11d:8"
              ]
            ]
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
      "00642188",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "0064219c",
      "READ",
      [
        "storage",
        "002c3250",
        null,
        null
      ]
    ],
    [
      "00642264",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[39]"
      ]
    ]
  ],
  "added": [
    [
      "00642188",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "0064219c",
      "READ",
      [
        "storage",
        "002c3290",
        null,
        null
      ]
    ],
    [
      "00642264",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00642118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md#insn-00642118) · [`00642120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md#insn-00642120) · [`00642198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641fd0.md#insn-00642198)
- 新版 `00642158`（命令位置の公開資料なし） · `00642160`（命令位置の公開資料なし） · `006421d8`（命令位置の公開資料なし）

~~~diff
- 00642118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00642118 ["INT_ADD", "register:40f0:8", ["const:642118:8", "const:4:8"]]
- 00642118 ["CALLIND", null, ["register:0:8"]]
+ 00642158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00642158 ["INT_ADD", "register:40f0:8", ["const:642158:8", "const:4:8"]]
+ 00642158 ["CALLIND", null, ["register:0:8"]]
- 00642118 bytes 00013fd6
+ 00642158 bytes 00013fd6
- 00642120 ["INT_ADD", "register:40f0:8", ["const:642120:8", "const:4:8"]]
- 00642120 ["CALL", null, ["callee:00c57e80:8"]]
+ 00642160 ["INT_ADD", "register:40f0:8", ["const:642160:8", "const:4:8"]]
+ 00642160 ["CALL", null, ["callee:00c57e80:8"]]
- 00642120 bytes 58561894
+ 00642160 bytes 48571894
- 00642198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00642198 ["INT_ADD", "register:40f0:8", ["const:642198:8", "const:4:8"]]
- 00642198 ["CALLIND", null, ["register:0:8"]]
+ 006421d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006421d8 ["INT_ADD", "register:40f0:8", ["const:6421d8:8", "const:4:8"]]
+ 006421d8 ["CALLIND", null, ["register:0:8"]]
- 00642198 bytes 00013fd6
+ 006421d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2bf61aefbced7a3f26d59aaf405150c"></a>

### [`00645fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md) → [`00645fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645fe4.md) FUN_00645fe4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) · 呼出先 5件 [`006416ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006416ac.md) [`00641b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641b20.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) · 呼出先 5件 [`006416ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006416ec.md) [`00641b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641b60.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "site": "00646018",
      "value": [
        "leaf",
        "ram:641b60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00645fd8",
      "value": [
        "leaf",
        "ram:641b20:8"
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
      "00646018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b20"
      ]
    ]
  ],
  "added": [
    [
      "00646018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00645fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md#insn-00645fd8) · [`00645fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md#insn-00645fcc) · [`00645fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md#insn-00645fe0)
- 新版 `00646018`（命令位置の公開資料なし） · `0064600c`（命令位置の公開資料なし） · `00646020`（命令位置の公開資料なし）

~~~diff
- 00645fd8 ["INT_ADD", "register:40f0:8", ["const:645fd8:8", "const:4:8"]]
- 00645fd8 ["CALL", null, ["ram:641b20:8"]]
+ 00646018 ["INT_ADD", "register:40f0:8", ["const:646018:8", "const:4:8"]]
+ 00646018 ["CALL", null, ["ram:641b60:8"]]
- 00645fd8 bytes d2eeff97
+ 00646018 bytes d2eeff97
- 00645fcc ["INT_ADD", "register:40f0:8", ["const:645fcc:8", "const:4:8"]]
- 00645fcc ["CALL", null, ["callee:008514f8:8"]]
+ 0064600c ["INT_ADD", "register:40f0:8", ["const:64600c:8", "const:4:8"]]
+ 0064600c ["CALL", null, ["callee:008514f8:8"]]
- 00645fcc bytes 3b2d0894
+ 0064600c bytes 3b2d0894
- 00645fe0 ["INT_ADD", "register:40f0:8", ["const:645fe0:8", "const:4:8"]]
- 00645fe0 ["CALL", null, ["callee:008514f8:8"]]
+ 00646020 ["INT_ADD", "register:40f0:8", ["const:646020:8", "const:4:8"]]
+ 00646020 ["CALL", null, ["callee:008514f8:8"]]
- 00645fe0 bytes 362d0894
+ 00646020 bytes 362d0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8465ef7697c4ab0bcb7d099161df4e8"></a>

### [`00646040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md) → [`00646080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/00646080.md) FUN_00646080

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) · 呼出先 13件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00651aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651aa4.md) · 呼出先 13件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.48% / 新版 95.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 10件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006460b8",
      "incomplete_value": true,
      "site": "006460b8",
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
      "definition_site": "00646078",
      "incomplete_value": true,
      "site": "00646078",
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
      "definition_site": "006460c0",
      "incomplete_value": false,
      "site": "006460d0",
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
      "definition_site": "00646080",
      "incomplete_value": false,
      "site": "00646090",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006460c8",
      "incomplete_value": false,
      "site": "006460d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00646088",
      "incomplete_value": false,
      "site": "00646090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "006460b0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006460c0",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006460c8",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006460b0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006460c0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006460c8",
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00646090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md#insn-00646090) · [`006460b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md#insn-006460b8) · [`006460d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md#insn-006460d0)
- 新版 `006460d0`（命令位置の公開資料なし） · `006460f8`（命令位置の公開資料なし） · `00646110`（命令位置の公開資料なし）

~~~diff
- 00646090 ["INT_ADD", "register:40f0:8", ["const:646090:8", "const:4:8"]]
- 00646090 ["CALL", null, ["callee:00c58610:8"]]
+ 006460d0 ["INT_ADD", "register:40f0:8", ["const:6460d0:8", "const:4:8"]]
+ 006460d0 ["CALL", null, ["callee:00c58610:8"]]
- 00646090 bytes 60481894
+ 006460d0 bytes 50491894
- 006460b8 ["INT_ADD", "register:40f0:8", ["const:6460b8:8", "const:4:8"]]
- 006460b8 ["CALL", null, ["callee:00467b2c:8"]]
+ 006460f8 ["INT_ADD", "register:40f0:8", ["const:6460f8:8", "const:4:8"]]
+ 006460f8 ["CALL", null, ["callee:00467b2c:8"]]
- 006460b8 bytes 8d86f897
+ 006460f8 bytes 8d86f897
- 006460d0 ["INT_ADD", "register:40f0:8", ["const:6460d0:8", "const:4:8"]]
- 006460d0 ["CALL", null, ["callee:008514f8:8"]]
+ 00646110 ["INT_ADD", "register:40f0:8", ["const:646110:8", "const:4:8"]]
+ 00646110 ["CALL", null, ["callee:008514f8:8"]]
- 006460d0 bytes fa2c0894
+ 00646110 bytes fa2c0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf91d26df65f86b713e31325d0c5563"></a>

### [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) → [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) FUN_0064a530

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00646570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646570.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 6件 [`006418c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006418c4.md) [`00645fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00645/00645fa4.md) [`0064ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064ded0.md) [`0064e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e15c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/006465b0.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 6件 [`00641904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641904.md) [`00645fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00645/00645fe4.md) [`0064df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064df10.md) [`0064e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "site": "0064a5e4",
      "value": [
        "leaf",
        "ram:641904:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064a5a4",
      "value": [
        "leaf",
        "ram:6418c4:8"
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
      "0064a5e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006418c4"
      ]
    ]
  ],
  "added": [
    [
      "0064a5e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641904"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md#insn-0064a564) · [`0064a5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md#insn-0064a5a4) · [`0064a524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md#insn-0064a524)
- 新版 `0064a5a4`（命令位置の公開資料なし） · `0064a5e4`（命令位置の公開資料なし） · `0064a564`（命令位置の公開資料なし）

~~~diff
- 0064a564 ["INT_ADD", "register:40f0:8", ["const:64a564:8", "const:4:8"]]
- 0064a564 ["CALL", null, ["callee:008514f8:8"]]
+ 0064a5a4 ["INT_ADD", "register:40f0:8", ["const:64a5a4:8", "const:4:8"]]
+ 0064a5a4 ["CALL", null, ["callee:008514f8:8"]]
- 0064a564 bytes d51b0894
+ 0064a5a4 bytes d51b0894
- 0064a5a4 ["INT_ADD", "register:40f0:8", ["const:64a5a4:8", "const:4:8"]]
- 0064a5a4 ["CALL", null, ["ram:6418c4:8"]]
+ 0064a5e4 ["INT_ADD", "register:40f0:8", ["const:64a5e4:8", "const:4:8"]]
+ 0064a5e4 ["CALL", null, ["ram:641904:8"]]
- 0064a5a4 bytes c8dcff97
+ 0064a5e4 bytes c8dcff97
- 0064a524 ["INT_ADD", "register:40f0:8", ["const:64a524:8", "const:4:8"]]
- 0064a524 ["CALL", null, ["callee:0064df10:8"]]
+ 0064a564 ["INT_ADD", "register:40f0:8", ["const:64a564:8", "const:4:8"]]
+ 0064a564 ["CALL", null, ["callee:0064df10:8"]]
- 0064a524 bytes 6b0e0094
+ 0064a564 bytes 6b0e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90933c3731e6388cdf02f002ca46a717"></a>

### [`0064b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md) → [`0064b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064b/0064b1a8.md) FUN_0064b1a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 29件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md)
- 新版 呼出元 1件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) · 呼出先 29件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 9件, `store_value` 2件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b48c",
      "incomplete_value": true,
      "site": "0064b48c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064b44c",
      "incomplete_value": true,
      "site": "0064b44c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b490",
      "incomplete_value": true,
      "site": "0064b490",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0064b450",
      "incomplete_value": true,
      "site": "0064b450",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0064b634",
      "incomplete_value": true,
      "site": "0064b634",
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
      "definition_site": "0064b5f4",
      "incomplete_value": true,
      "site": "0064b5f4",
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
      "0064b218",
      "DATA",
      [
        "storage",
        "0043479c",
        null,
        "dword"
      ]
    ],
    [
      "0064b228",
      "DATA",
      [
        "storage",
        "0042ef78",
        "fde_0042ef78",
        "dword"
      ]
    ],
    [
      "0064b280",
      "DATA",
      [
        "storage",
        "00432898",
        null,
        "byte[31]"
      ]
    ]
  ],
  "added": [
    [
      "0064b218",
      "DATA",
      [
        "storage",
        "0043479c",
        null,
        "uleb128"
      ]
    ],
    [
      "0064b228",
      "DATA",
      [
        "storage",
        "0042ef78",
        null,
        "dword"
      ]
    ],
    [
      "0064b280",
      "DATA",
      [
        "storage",
        "00432898",
        null,
        "byte[27]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md#insn-0064b370) · [`0064b380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md#insn-0064b380) · [`0064b490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064b/0064b168.md#insn-0064b490)
- 新版 `0064b3b0`（命令位置の公開資料なし） · `0064b3c0`（命令位置の公開資料なし） · `0064b4d0`（命令位置の公開資料なし）

~~~diff
- 0064b370 ["INT_ADD", "register:40f0:8", ["const:64b370:8", "const:4:8"]]
- 0064b370 ["CALL", null, ["ram:71be98:8"]]
+ 0064b3b0 ["INT_ADD", "register:40f0:8", ["const:64b3b0:8", "const:4:8"]]
+ 0064b3b0 ["CALL", null, ["ram:71bed8:8"]]
- 0064b370 bytes ca420394
+ 0064b3b0 bytes ca420394
- 0064b380 ["INT_ADD", "register:40f0:8", ["const:64b380:8", "const:4:8"]]
- 0064b380 ["CALL", null, ["ram:71d1bc:8"]]
+ 0064b3c0 ["INT_ADD", "register:40f0:8", ["const:64b3c0:8", "const:4:8"]]
+ 0064b3c0 ["CALL", null, ["ram:71d1fc:8"]]
- 0064b380 bytes 8f470394
+ 0064b3c0 bytes 8f470394
- 0064b490 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0064b490 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0064b490 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0064b490 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0064b4d0 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0064b4d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0064b4d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0064b4d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0064b490 bytes 21602991
+ 0064b4d0 bytes 21603991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eeaa74c7f20c1bfb03a80aed4ad5ff0"></a>

### [`0064c9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064c/0064c9c8.md) → [`0064ca08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064c/0064ca08.md) FUN_0064ca08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0064cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064c/0064cc30.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0064cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064c/0064cc70.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064ca20",
      "incomplete_value": true,
      "site": "0064ca24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064c9e0",
      "incomplete_value": true,
      "site": "0064c9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064ca38",
      "incomplete_value": true,
      "site": "0064ca3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064c9f8",
      "incomplete_value": true,
      "site": "0064c9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
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
      "definition_site": "0064ca50",
      "incomplete_value": true,
      "site": "0064ca54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ca10",
      "incomplete_value": true,
      "site": "0064ca14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:770:8"
              ]
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
      "0064ca14",
      "READ",
      [
        "storage",
        "00ca6790",
        null,
        "undefined1"
      ]
    ],
    [
      "0064ca20",
      "READ",
      [
        "storage",
        "00ca67a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0064ca2c",
      "READ",
      [
        "storage",
        "00ca6778",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0064ca14",
      "READ",
      [
        "storage",
        "00ca6b90",
        null,
        "undefined1"
      ]
    ],
    [
      "0064ca20",
      "READ",
      [
        "storage",
        "00ca6ba0",
        null,
        "undefined8"
      ]
    ],
    [
      "0064ca2c",
      "READ",
      [
        "storage",
        "00ca6b78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064c9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064c/0064c9c8.md#insn-0064c9d4) · [`0064c9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064c/0064c9c8.md#insn-0064c9e4) · [`0064c9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064c/0064c9c8.md#insn-0064c9ec)
- 新版 `0064ca14`（命令位置の公開資料なし） · `0064ca24`（命令位置の公開資料なし） · `0064ca2c`（命令位置の公開資料なし）

~~~diff
- 0064c9d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:790:8"]]
- 0064c9d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0064c9d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0064ca14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b90:8"]]
+ 0064ca14 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0064ca14 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0064c9d4 bytes 08415e39
+ 0064ca14 bytes 08416e39
- 0064c9e4 ["INT_ADD", "register:40f0:8", ["const:64c9e4:8", "const:4:8"]]
- 0064c9e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0064ca24 ["INT_ADD", "register:40f0:8", ["const:64ca24:8", "const:4:8"]]
+ 0064ca24 ["CALL", null, ["callee:00c57eb0:8"]]
- 0064c9e4 bytes 332c1894
+ 0064ca24 bytes 232d1894
- 0064c9ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:778:8"]]
- 0064c9ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0064c9ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0064ca2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b78:8"]]
+ 0064ca2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0064ca2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0064c9ec bytes 08e15d39
+ 0064ca2c bytes 08e16d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec5435da145a99a1badd16a8d0cca02"></a>

### [`0064d7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d7f4.md) → [`0064d834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064d834.md) FUN_0064d834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 10件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md)
- 新版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 10件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.11% / 新版 81.11%

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
      "definition_site": "0064d868",
      "incomplete_value": false,
      "site": "0064d874",
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
      "definition_site": "0064d828",
      "incomplete_value": false,
      "site": "0064d834",
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
      "definition_site": "0064d87c",
      "incomplete_value": true,
      "site": "0064d88c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064d83c",
      "incomplete_value": true,
      "site": "0064d84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e9d:8"
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
      "definition_site": "0064d890",
      "incomplete_value": true,
      "site": "0064d890",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0064d850",
      "incomplete_value": true,
      "site": "0064d850",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064d874",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0064d87c",
      "READ",
      [
        "storage",
        "002a9e9d",
        null,
        "string"
      ]
    ],
    [
      "0064d884",
      "READ",
      [
        "storage",
        "002a9eaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0064d874",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0064d87c",
      "READ",
      [
        "storage",
        "002a9f6a",
        null,
        "string"
      ]
    ],
    [
      "0064d884",
      "READ",
      [
        "storage",
        "002a9f77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064d884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d7f4.md#insn-0064d884) · [`0064d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d7f4.md#insn-0064d890) · [`0064d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d7f4.md#insn-0064d904)
- 新版 `0064d8c4`（命令位置の公開資料なし） · `0064d8d0`（命令位置の公開資料なし） · `0064d944`（命令位置の公開資料なし）

~~~diff
- 0064d884 ["INT_ADD", "register:40f0:8", ["const:64d884:8", "const:4:8"]]
- 0064d884 ["CALL", null, ["callee:0048791c:8"]]
+ 0064d8c4 ["INT_ADD", "register:40f0:8", ["const:64d8c4:8", "const:4:8"]]
+ 0064d8c4 ["CALL", null, ["callee:0048791c:8"]]
- 0064d884 bytes 16e8f897
+ 0064d8c4 bytes 16e8f897
- 0064d890 ["INT_ADD", "register:40f0:8", ["const:64d890:8", "const:4:8"]]
- 0064d890 ["CALL", null, ["callee:0048793c:8"]]
+ 0064d8d0 ["INT_ADD", "register:40f0:8", ["const:64d8d0:8", "const:4:8"]]
+ 0064d8d0 ["CALL", null, ["callee:0048793c:8"]]
- 0064d890 bytes 1be8f897
+ 0064d8d0 bytes 1be8f897
- 0064d904 ["INT_ADD", "register:40f0:8", ["const:64d904:8", "const:4:8"]]
- 0064d904 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0064d944 ["INT_ADD", "register:40f0:8", ["const:64d944:8", "const:4:8"]]
+ 0064d944 ["CALL", null, ["callee:00c57fb0:8"]]
- 0064d904 bytes ab281894
+ 0064d944 bytes 9b291894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ce4985697b25b5ba8cae90ba1d25c6"></a>

### [`0064d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md) → [`0064d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064d9ec.md) FUN_0064d9ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0064e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md) · 呼出先 13件 [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md)
- 新版 呼出元 1件 [`0064e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e540.md) · 呼出先 13件 [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0046f6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f6e4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.85% / 新版 85.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064da3c",
      "incomplete_value": true,
      "site": "0064da3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:24b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064d9fc",
      "incomplete_value": true,
      "site": "0064d9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:17e:8"
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
      "definition_site": "0064da30",
      "incomplete_value": true,
      "site": "0064da40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0064d9f0",
      "incomplete_value": true,
      "site": "0064da00",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064daf0",
      "incomplete_value": true,
      "site": "0064db04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064dab0",
      "incomplete_value": true,
      "site": "0064dac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dac:8"
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
      "0064da2c",
      "READ",
      [
        "storage",
        "0029f17e",
        null,
        "string"
      ]
    ],
    [
      "0064da30",
      "READ",
      [
        "storage",
        "0029f185",
        null,
        "string"
      ]
    ],
    [
      "0064daf0",
      "READ",
      [
        "storage",
        "002b3dac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0064da2c",
      "READ",
      [
        "storage",
        "0029f24b",
        null,
        "string"
      ]
    ],
    [
      "0064da30",
      "READ",
      [
        "storage",
        "0029f252",
        null,
        "string"
      ]
    ],
    [
      "0064daf0",
      "READ",
      [
        "storage",
        "002b3dec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064da40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md#insn-0064da40) · [`0064da88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md#insn-0064da88) · [`0064d9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064d9ac.md#insn-0064d9d4)
- 新版 `0064da80`（命令位置の公開資料なし） · `0064dac8`（命令位置の公開資料なし） · `0064da14`（命令位置の公開資料なし）

~~~diff
- 0064da40 ["INT_ADD", "register:40f0:8", ["const:64da40:8", "const:4:8"]]
- 0064da40 ["CALL", null, ["callee:004700c4:8"]]
+ 0064da80 ["INT_ADD", "register:40f0:8", ["const:64da80:8", "const:4:8"]]
+ 0064da80 ["CALL", null, ["callee:004700c4:8"]]
- 0064da40 bytes 9189f897
+ 0064da80 bytes 9189f897
- 0064da88 ["INT_ADD", "register:40f0:8", ["const:64da88:8", "const:4:8"]]
- 0064da88 ["CALL", null, ["callee:004700e0:8"]]
+ 0064dac8 ["INT_ADD", "register:40f0:8", ["const:64dac8:8", "const:4:8"]]
+ 0064dac8 ["CALL", null, ["callee:004700e0:8"]]
- 0064da88 bytes 8689f897
+ 0064dac8 bytes 8689f897
- 0064d9d4 ["INT_ADD", "register:40f0:8", ["const:64d9d4:8", "const:4:8"]]
- 0064d9d4 ["CALL", null, ["callee:0063a7a4:8"]]
+ 0064da14 ["INT_ADD", "register:40f0:8", ["const:64da14:8", "const:4:8"]]
+ 0064da14 ["CALL", null, ["callee:0063a7a4:8"]]
- 0064d9d4 bytes 64b3ff97
+ 0064da14 bytes 64b3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715b0004824b55a809a580eee99c74ff"></a>

### [`0064ded0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064ded0.md) → [`0064df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064df10.md) FUN_0064df10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00641134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641134.md) [`00641c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641c28.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d0f4.md)
- 新版 呼出元 2件 [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00641174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641174.md) [`00641c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641c68.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`0071d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dfe8",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dfa8",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0064e008",
      "value": [
        "leaf",
        "ram:641c68:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dfc8",
      "value": [
        "leaf",
        "ram:641c28:8"
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
      "site": "0064e0c8",
      "value": [
        "leaf",
        "ram:71d134:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e088",
      "value": [
        "leaf",
        "ram:71d0f4:8"
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
      "0064dfe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0064e008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641c28"
      ]
    ],
    [
      "0064e0c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d0f4"
      ]
    ]
  ],
  "added": [
    [
      "0064dfe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0064e008",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641c68"
      ]
    ],
    [
      "0064e0c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d134"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064dfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064ded0.md#insn-0064dfa8) · [`0064dfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064ded0.md#insn-0064dfc8) · [`0064e04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064ded0.md#insn-0064e04c)
- 新版 `0064dfe8`（命令位置の公開資料なし） · `0064e008`（命令位置の公開資料なし） · `0064e08c`（命令位置の公開資料なし）

~~~diff
- 0064dfa8 ["INT_ADD", "register:40f0:8", ["const:64dfa8:8", "const:4:8"]]
- 0064dfa8 ["CALL", null, ["ram:71be98:8"]]
+ 0064dfe8 ["INT_ADD", "register:40f0:8", ["const:64dfe8:8", "const:4:8"]]
+ 0064dfe8 ["CALL", null, ["ram:71bed8:8"]]
- 0064dfa8 bytes bc370394
+ 0064dfe8 bytes bc370394
- 0064dfc8 ["INT_ADD", "register:40f0:8", ["const:64dfc8:8", "const:4:8"]]
- 0064dfc8 ["CALL", null, ["ram:641c28:8"]]
+ 0064e008 ["INT_ADD", "register:40f0:8", ["const:64e008:8", "const:4:8"]]
+ 0064e008 ["CALL", null, ["ram:641c68:8"]]
- 0064dfc8 bytes 18cfff97
+ 0064e008 bytes 18cfff97
- 0064e04c ["INT_ADD", "register:40f0:8", ["const:64e04c:8", "const:4:8"]]
- 0064e04c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0064e08c ["INT_ADD", "register:40f0:8", ["const:64e08c:8", "const:4:8"]]
+ 0064e08c ["CALL", null, ["callee:00c57eb0:8"]]
- 0064e04c bytes 99261894
+ 0064e08c bytes 89271894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9508741e3fcc39823a5f8465a3649397"></a>

### [`0064e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md) → [`0064e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e37c.md) FUN_0064e37c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0064e334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e334.md) [`0064e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · 呼出先 12件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0063ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md)
- 新版 呼出元 4件 [`0064e374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e374.md) [`0064e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e540.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) · 呼出先 12件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0063cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063cd1c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.27% / 新版 90.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e424",
      "incomplete_value": true,
      "site": "0064e434",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e3e4",
      "incomplete_value": true,
      "site": "0064e3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e3bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e37c",
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
      "site": "0064e3c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e388",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0064e3bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0064e3c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0064e3fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0064e3bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0064e3c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0064e3fc",
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

- 旧版 [`0064e37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md#insn-0064e37c) · [`0064e388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md#insn-0064e388) · [`0064e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e33c.md#insn-0064e3bc)
- 新版 `0064e3bc`（命令位置の公開資料なし） · `0064e3c8`（命令位置の公開資料なし） · `0064e3fc`（命令位置の公開資料なし）

~~~diff
- 0064e37c ["INT_ADD", "register:40f0:8", ["const:64e37c:8", "const:4:8"]]
- 0064e37c ["CALL", null, ["ram:47acb4:8"]]
+ 0064e3bc ["INT_ADD", "register:40f0:8", ["const:64e3bc:8", "const:4:8"]]
+ 0064e3bc ["CALL", null, ["ram:47acf4:8"]]
- 0064e37c bytes 4eb2f897
+ 0064e3bc bytes 4eb2f897
- 0064e388 ["INT_ADD", "register:40f0:8", ["const:64e388:8", "const:4:8"]]
- 0064e388 ["CALL", null, ["ram:47acb4:8"]]
+ 0064e3c8 ["INT_ADD", "register:40f0:8", ["const:64e3c8:8", "const:4:8"]]
+ 0064e3c8 ["CALL", null, ["ram:47acf4:8"]]
- 0064e388 bytes 4bb2f897
+ 0064e3c8 bytes 4bb2f897
- 0064e3bc ["INT_ADD", "register:40f0:8", ["const:64e3bc:8", "const:4:8"]]
- 0064e3bc ["CALL", null, ["ram:46c984:8"]]
+ 0064e3fc ["INT_ADD", "register:40f0:8", ["const:64e3fc:8", "const:4:8"]]
+ 0064e3fc ["CALL", null, ["ram:46c9c4:8"]]
- 0064e3bc bytes 7279f897
+ 0064e3fc bytes 7279f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdafdeb8fdf3fca52bacae2e3c7666d0"></a>

### [`0064e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md) → [`0064e540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e540.md) FUN_0064e540

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2968.md) · 呼出先 31件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`0048ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md)
- 新版 呼出元 1件 [`006b29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b29a8.md) · 呼出先 31件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`0048ce4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.96% / 新版 95.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 8件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e810",
      "incomplete_value": true,
      "site": "0064e818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e7d0",
      "incomplete_value": true,
      "site": "0064e7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e8f0",
      "incomplete_value": false,
      "site": "0064e8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e8b0",
      "incomplete_value": false,
      "site": "0064e8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b48:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064ea74",
      "incomplete_value": false,
      "site": "0064ea74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ea34",
      "incomplete_value": false,
      "site": "0064ea34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064e578",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0064e58c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064e594",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0064e578",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0064e58c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064e594",
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md#insn-0064e55c) · [`0064e598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md#insn-0064e598) · [`0064e610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e500.md#insn-0064e610)
- 新版 `0064e59c`（命令位置の公開資料なし） · `0064e5d8`（命令位置の公開資料なし） · `0064e650`（命令位置の公開資料なし）

~~~diff
- 0064e55c ["INT_ADD", "register:40f0:8", ["const:64e55c:8", "const:4:8"]]
- 0064e55c ["CALL", null, ["callee:00c58610:8"]]
+ 0064e59c ["INT_ADD", "register:40f0:8", ["const:64e59c:8", "const:4:8"]]
+ 0064e59c ["CALL", null, ["callee:00c58610:8"]]
- 0064e55c bytes 2d271894
+ 0064e59c bytes 1d281894
- 0064e598 ["INT_ADD", "register:40f0:8", ["const:64e598:8", "const:4:8"]]
- 0064e598 ["CALL", null, ["ram:46c984:8"]]
+ 0064e5d8 ["INT_ADD", "register:40f0:8", ["const:64e5d8:8", "const:4:8"]]
+ 0064e5d8 ["CALL", null, ["ram:46c9c4:8"]]
- 0064e598 bytes fb78f897
+ 0064e5d8 bytes fb78f897
- 0064e610 ["INT_ADD", "register:40f0:8", ["const:64e610:8", "const:4:8"]]
- 0064e610 ["CALL", null, ["ram:64d600:8"]]
+ 0064e650 ["INT_ADD", "register:40f0:8", ["const:64e650:8", "const:4:8"]]
+ 0064e650 ["CALL", null, ["ram:64d640:8"]]
- 0064e610 bytes fcfbff97
+ 0064e650 bytes fcfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79413f4a71215af70cda8904678f55e8"></a>

### [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) → [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) FUN_0064ecb8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) · 呼出先 99件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)
- 新版 呼出元 1件 [`006b2b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2b5c.md) · 呼出先 99件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 40件, `call_target` 38件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064ee64",
      "incomplete_value": true,
      "site": "0064ee64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ee24",
      "incomplete_value": true,
      "site": "0064ee24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064f1d0",
      "incomplete_value": false,
      "site": "0064f1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064f190",
      "incomplete_value": false,
      "site": "0064f19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064fdc8",
      "incomplete_value": false,
      "site": "0064fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064fd88",
      "incomplete_value": false,
      "site": "0064fd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "ordinal": 75,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064edac",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "0064ede0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "0064edf8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "0064edac",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "0064ede0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "0064edf8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064edf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md#insn-0064edf8) · [`0064eee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md#insn-0064eee4) · [`0064f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md#insn-0064f064)
- 新版 `0064ee38`（命令位置の公開資料なし） · `0064ef24`（命令位置の公開資料なし） · `0064f0a4`（命令位置の公開資料なし）

~~~diff
- 0064edf8 ["INT_ADD", "register:40f0:8", ["const:64edf8:8", "const:4:8"]]
- 0064edf8 ["CALL", null, ["ram:48ccb8:8"]]
+ 0064ee38 ["INT_ADD", "register:40f0:8", ["const:64ee38:8", "const:4:8"]]
+ 0064ee38 ["CALL", null, ["ram:48ccf8:8"]]
- 0064edf8 bytes b0f7f897
+ 0064ee38 bytes b0f7f897
- 0064eee4 ["INT_ADD", "register:40f0:8", ["const:64eee4:8", "const:4:8"]]
- 0064eee4 ["CALL", null, ["ram:645254:8"]]
+ 0064ef24 ["INT_ADD", "register:40f0:8", ["const:64ef24:8", "const:4:8"]]
+ 0064ef24 ["CALL", null, ["ram:645294:8"]]
- 0064eee4 bytes dcd8ff97
+ 0064ef24 bytes dcd8ff97
- 0064f064 ["INT_ADD", "register:40f0:8", ["const:64f064:8", "const:4:8"]]
- 0064f064 ["CALL", null, ["ram:46c984:8"]]
+ 0064f0a4 ["INT_ADD", "register:40f0:8", ["const:64f0a4:8", "const:4:8"]]
+ 0064f0a4 ["CALL", null, ["ram:46c9c4:8"]]
- 0064f064 bytes 4876f897
+ 0064f0a4 bytes 4876f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd7875451d5c2ec3007031b43956d6d"></a>

### [`00651730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651730.md) → [`00651770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651770.md) FUN_00651770

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) · 呼出先 10件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00651aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651aa4.md) · 呼出先 10件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

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
      "site": "006517e0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006517a0",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00651808",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006517c8",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065184c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065180c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006517e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00651808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065184c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006517e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00651808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065184c",
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

- 旧版 [`006517a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651730.md#insn-006517a0) · [`006517c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651730.md#insn-006517c8) · [`00651808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651730.md#insn-00651808)
- 新版 `006517e0`（命令位置の公開資料なし） · `00651808`（命令位置の公開資料なし） · `00651848`（命令位置の公開資料なし）

~~~diff
- 006517a0 ["INT_ADD", "register:40f0:8", ["const:6517a0:8", "const:4:8"]]
- 006517a0 ["CALL", null, ["ram:46c984:8"]]
+ 006517e0 ["INT_ADD", "register:40f0:8", ["const:6517e0:8", "const:4:8"]]
+ 006517e0 ["CALL", null, ["ram:46c9c4:8"]]
- 006517a0 bytes 796cf897
+ 006517e0 bytes 796cf897
- 006517c8 ["INT_ADD", "register:40f0:8", ["const:6517c8:8", "const:4:8"]]
- 006517c8 ["CALL", null, ["ram:46c984:8"]]
+ 00651808 ["INT_ADD", "register:40f0:8", ["const:651808:8", "const:4:8"]]
+ 00651808 ["CALL", null, ["ram:46c9c4:8"]]
- 006517c8 bytes 6f6cf897
+ 00651808 bytes 6f6cf897
- 00651808 ["INT_ADD", "register:40f0:8", ["const:651808:8", "const:4:8"]]
- 00651808 ["CALL", null, ["callee:008514f8:8"]]
+ 00651848 ["INT_ADD", "register:40f0:8", ["const:651848:8", "const:4:8"]]
+ 00651848 ["CALL", null, ["callee:008514f8:8"]]
- 00651808 bytes 2cff0794
+ 00651848 bytes 2cff0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ed9ff031e5d938b26975366090b5c8"></a>

### [`006519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006519cc.md) → [`00651a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651a0c.md) FUN_00651a0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 3件 [`0063b374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063b374.md) [`0063d104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d104.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 3件 [`0063b3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063b3b4.md) [`0063d144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d144.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 89.47% / 新版 89.47%

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
      "site": "00651a20",
      "value": [
        "leaf",
        "ram:63d144:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006519e0",
      "value": [
        "leaf",
        "ram:63d104:8"
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
      "00651a20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063d104"
      ]
    ],
    [
      "00651a3c",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[43]"
      ]
    ],
    [
      "00651a74",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00651a20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063d144"
      ]
    ],
    [
      "00651a3c",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[39]"
      ]
    ],
    [
      "00651a74",
      "READ",
      [
        "storage",
        "00c9b4a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006519e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006519cc.md#insn-006519e0) · [`006519f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006519cc.md#insn-006519f0) · [`00651a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006519cc.md#insn-00651a04)
- 新版 `00651a20`（命令位置の公開資料なし） · `00651a30`（命令位置の公開資料なし） · `00651a44`（命令位置の公開資料なし）

~~~diff
- 006519e0 ["INT_ADD", "register:40f0:8", ["const:6519e0:8", "const:4:8"]]
- 006519e0 ["CALL", null, ["ram:63d104:8"]]
+ 00651a20 ["INT_ADD", "register:40f0:8", ["const:651a20:8", "const:4:8"]]
+ 00651a20 ["CALL", null, ["ram:63d144:8"]]
- 006519e0 bytes c9adff97
+ 00651a20 bytes c9adff97
- 006519f0 ["INT_ADD", "register:40f0:8", ["const:6519f0:8", "const:4:8"]]
- 006519f0 ["CALL", null, ["callee:008514f8:8"]]
+ 00651a30 ["INT_ADD", "register:40f0:8", ["const:651a30:8", "const:4:8"]]
+ 00651a30 ["CALL", null, ["callee:008514f8:8"]]
- 006519f0 bytes b2fe0794
+ 00651a30 bytes b2fe0794
- 00651a04 ["INT_ADD", "register:40f0:8", ["const:651a04:8", "const:4:8"]]
- 00651a04 ["CALL", null, ["callee:008514f8:8"]]
+ 00651a44 ["INT_ADD", "register:40f0:8", ["const:651a44:8", "const:4:8"]]
+ 00651a44 ["CALL", null, ["callee:008514f8:8"]]
- 00651a04 bytes adfe0794
+ 00651a44 bytes adfe0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4774e5dd6477c52688448e669c7dd0e9"></a>

### [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) → [`00651aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651aa4.md) FUN_00651aa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 24件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 24件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006523c8",
      "incomplete_value": true,
      "site": "006523c8",
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
      "definition_site": "00652388",
      "incomplete_value": true,
      "site": "00652388",
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
    "ordinal": 56,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00651ba4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00651b64",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00651e00",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00651dc0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 62,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00651b34",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[43]"
      ]
    ],
    [
      "00651ba4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00651e00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00651b34",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[39]"
      ]
    ],
    [
      "00651ba4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00651e00",
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

- 旧版 [`00651b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md#insn-00651b64) · [`00651dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md#insn-00651dc0) · [`00651e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md#insn-00651e40)
- 新版 `00651ba4`（命令位置の公開資料なし） · `00651e00`（命令位置の公開資料なし） · `00651e80`（命令位置の公開資料なし）

~~~diff
- 00651b64 ["INT_ADD", "register:40f0:8", ["const:651b64:8", "const:4:8"]]
- 00651b64 ["CALL", null, ["ram:46c984:8"]]
+ 00651ba4 ["INT_ADD", "register:40f0:8", ["const:651ba4:8", "const:4:8"]]
+ 00651ba4 ["CALL", null, ["ram:46c9c4:8"]]
- 00651b64 bytes 886bf897
+ 00651ba4 bytes 886bf897
- 00651dc0 ["INT_ADD", "register:40f0:8", ["const:651dc0:8", "const:4:8"]]
- 00651dc0 ["CALL", null, ["ram:46c984:8"]]
+ 00651e00 ["INT_ADD", "register:40f0:8", ["const:651e00:8", "const:4:8"]]
+ 00651e00 ["CALL", null, ["ram:46c9c4:8"]]
- 00651dc0 bytes f16af897
+ 00651e00 bytes f16af897
- 00651e40 ["INT_ADD", "register:40f0:8", ["const:651e40:8", "const:4:8"]]
- 00651e40 ["CALL", null, ["callee:008b79c8:8"]]
+ 00651e80 ["INT_ADD", "register:40f0:8", ["const:651e80:8", "const:4:8"]]
+ 00651e80 ["CALL", null, ["callee:008b79c8:8"]]
- 00651e40 bytes d1960994
+ 00651e80 bytes d2960994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10fd1a744c829b1897018c24dbdcbe92"></a>

### [`00652acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652acc.md) → [`00652b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652b0c.md) FUN_00652b0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0063c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md) [`0063ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063ccdc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`0063c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5cc.md) [`0063cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063cd1c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00652b18",
      "incomplete_value": false,
      "site": "00652b1c",
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
      "definition_site": "00652ad8",
      "incomplete_value": false,
      "site": "00652adc",
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
      "00652b18",
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
      "00652b18",
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

- 旧版 [`00652adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652acc.md#insn-00652adc) · [`00652ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652acc.md#insn-00652ad8)
- 新版 `00652b1c`（命令位置の公開資料なし） · `00652b18`（命令位置の公開資料なし）

~~~diff
- 00652adc ["INT_ADD", "register:40f0:8", ["const:652adc:8", "const:4:8"]]
- 00652adc ["CALL", null, ["callee:0043b778:8"]]
+ 00652b1c ["INT_ADD", "register:40f0:8", ["const:652b1c:8", "const:4:8"]]
+ 00652b1c ["CALL", null, ["callee:0043b778:8"]]
- 00652adc bytes 17a3f797
+ 00652b1c bytes 17a3f797
- 00652ad8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00652ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00652ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00652ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00652b18 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00652b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00652b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00652b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00652ad8 bytes 00303c91
+ 00652b18 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33010187c7936044a40580737414684a"></a>

### [`006530f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006530f4.md) → [`00653134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/00653134.md) FUN_00653134

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00644f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00644/00644f90.md) [`00652e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652e60.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00644fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00644/00644fd0.md) [`00652ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652ea0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00653140",
      "incomplete_value": false,
      "site": "00653144",
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
      "definition_site": "00653100",
      "incomplete_value": false,
      "site": "00653104",
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
      "00653140",
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
      "00653140",
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

- 旧版 [`00653104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006530f4.md#insn-00653104) · [`00653100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006530f4.md#insn-00653100)
- 新版 `00653144`（命令位置の公開資料なし） · `00653140`（命令位置の公開資料なし）

~~~diff
- 00653104 ["INT_ADD", "register:40f0:8", ["const:653104:8", "const:4:8"]]
- 00653104 ["CALL", null, ["callee:0043b778:8"]]
+ 00653144 ["INT_ADD", "register:40f0:8", ["const:653144:8", "const:4:8"]]
+ 00653144 ["CALL", null, ["callee:0043b778:8"]]
- 00653104 bytes 8da1f797
+ 00653144 bytes 8da1f797
- 00653100 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00653100 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00653100 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00653100 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00653140 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00653140 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00653140 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00653140 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00653100 bytes 00303c91
+ 00653140 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57034e937ac0d38feac72f6b97776ea4"></a>

### [`00653468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653468.md) → [`006534a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534a8.md) FUN_006534a8

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
      "definition_site": "006534bc",
      "incomplete_value": false,
      "site": "006534c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065347c",
      "incomplete_value": false,
      "site": "00653480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "006534c0",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006534c0",
      "DATA",
      [
        "storage",
        "00c73838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653468.md#insn-00653474) · [`0065347c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653468.md#insn-0065347c)
- 新版 `006534b4`（命令位置の公開資料なし） · `006534bc`（命令位置の公開資料なし）

~~~diff
- 00653474 ["INT_ADD", "register:40f0:8", ["const:653474:8", "const:4:8"]]
- 00653474 ["CALL", null, ["callee:00c57e90:8"]]
+ 006534b4 ["INT_ADD", "register:40f0:8", ["const:6534b4:8", "const:4:8"]]
+ 006534b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00653474 bytes 87111894
+ 006534b4 bytes 77121894
- 0065347c ["COPY", "tmp:0:8", ["const:438:8"]]
- 0065347c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065347c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065347c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006534bc ["COPY", "tmp:0:8", ["const:838:8"]]
+ 006534bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006534bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006534bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065347c bytes 08e11091
+ 006534bc bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d08f2ec13e933118af0db151ba1586f"></a>

### [`0065348c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065348c.md) → [`006534cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534cc.md) FUN_006534cc

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
      "definition_site": "006534d0",
      "incomplete_value": false,
      "site": "006534d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653490",
      "incomplete_value": false,
      "site": "00653494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "006534d4",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006534d4",
      "DATA",
      [
        "storage",
        "00c73838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065348c.md#insn-00653490)
- 新版 `006534d0`（命令位置の公開資料なし）

~~~diff
- 00653490 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00653490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00653490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00653490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006534d0 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 006534d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006534d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006534d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00653490 bytes 08e11091
+ 006534d0 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c657a8f689c2f5e02637f264ea087bb1"></a>

### [`006534d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534d8.md) → [`00653518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/00653518.md) FUN_00653518

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
      "definition_site": "0065353c",
      "incomplete_value": false,
      "site": "0065353c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006534fc",
      "incomplete_value": false,
      "site": "006534fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
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
      "0065353c",
      "DATA",
      [
        "storage",
        "00c734c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065353c",
      "DATA",
      [
        "storage",
        "00c738c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006534ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534d8.md#insn-006534ec) · [`006534f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534d8.md#insn-006534f8)
- 新版 `0065352c`（命令位置の公開資料なし） · `00653538`（命令位置の公開資料なし）

~~~diff
- 006534ec ["INT_ADD", "register:40f0:8", ["const:6534ec:8", "const:4:8"]]
- 006534ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0065352c ["INT_ADD", "register:40f0:8", ["const:65352c:8", "const:4:8"]]
+ 0065352c ["CALL", null, ["callee:00c57e90:8"]]
- 006534ec bytes 69111894
+ 0065352c bytes 59121894
- 006534f8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 006534f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006534f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006534f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00653538 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00653538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00653538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00653538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006534f8 bytes 08211391
+ 00653538 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de17ada0536a8bb929560269f1e067cb"></a>

### [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) → [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) FUN_006535a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00653528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653528.md) · 呼出先 45件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00653568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/00653568.md) · 呼出先 45件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.07% / 新版 95.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `call_target` 18件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00653b8c",
      "incomplete_value": true,
      "site": "00653b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653b4c",
      "incomplete_value": true,
      "site": "00653b5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00653ba0",
      "incomplete_value": true,
      "site": "00653ba0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00653b60",
      "incomplete_value": true,
      "site": "00653b60",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00653d70",
      "incomplete_value": false,
      "site": "00653d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653d30",
      "incomplete_value": false,
      "site": "00653d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "00653654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006536d0",
      "DATA",
      [
        "storage",
        "00435360",
        null,
        "byte[43]"
      ]
    ],
    [
      "00653700",
      "DATA",
      [
        "storage",
        "00435344",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00653654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006536d0",
      "DATA",
      [
        "storage",
        "00435360",
        null,
        "byte[47]"
      ]
    ],
    [
      "00653700",
      "DATA",
      [
        "storage",
        "00435344",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md#insn-00653614) · [`00653ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md#insn-00653ab0) · [`00653bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md#insn-00653bc8)
- 新版 `00653654`（命令位置の公開資料なし） · `00653af0`（命令位置の公開資料なし） · `00653c08`（命令位置の公開資料なし）

~~~diff
- 00653614 ["INT_ADD", "register:40f0:8", ["const:653614:8", "const:4:8"]]
- 00653614 ["CALL", null, ["ram:47acb4:8"]]
+ 00653654 ["INT_ADD", "register:40f0:8", ["const:653654:8", "const:4:8"]]
+ 00653654 ["CALL", null, ["ram:47acf4:8"]]
- 00653614 bytes a89df897
+ 00653654 bytes a89df897
- 00653ab0 ["INT_ADD", "register:40f0:8", ["const:653ab0:8", "const:4:8"]]
- 00653ab0 ["CALL", null, ["ram:6418c4:8"]]
+ 00653af0 ["INT_ADD", "register:40f0:8", ["const:653af0:8", "const:4:8"]]
+ 00653af0 ["CALL", null, ["ram:641904:8"]]
- 00653ab0 bytes 85b7ff97
+ 00653af0 bytes 85b7ff97
- 00653bc8 ["INT_ADD", "register:40f0:8", ["const:653bc8:8", "const:4:8"]]
- 00653bc8 ["CALL", null, ["ram:47acb4:8"]]
+ 00653c08 ["INT_ADD", "register:40f0:8", ["const:653c08:8", "const:4:8"]]
+ 00653c08 ["CALL", null, ["ram:47acf4:8"]]
- 00653bc8 bytes 3b9cf897
+ 00653c08 bytes 3b9cf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf00bfdbc4ea3a02e20fe643b700170f"></a>

### [`00655078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655078.md) → [`006550b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006550b8.md) FUN_006550b8

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
      "definition_site": "006550cc",
      "incomplete_value": false,
      "site": "006550d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065508c",
      "incomplete_value": false,
      "site": "00655090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "006550d0",
      "DATA",
      [
        "storage",
        "00c73538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006550d0",
      "DATA",
      [
        "storage",
        "00c73938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655078.md#insn-00655084) · [`0065508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655078.md#insn-0065508c)
- 新版 `006550c4`（命令位置の公開資料なし） · `006550cc`（命令位置の公開資料なし）

~~~diff
- 00655084 ["INT_ADD", "register:40f0:8", ["const:655084:8", "const:4:8"]]
- 00655084 ["CALL", null, ["callee:00c57e90:8"]]
+ 006550c4 ["INT_ADD", "register:40f0:8", ["const:6550c4:8", "const:4:8"]]
+ 006550c4 ["CALL", null, ["callee:00c57e90:8"]]
- 00655084 bytes 830a1894
+ 006550c4 bytes 730b1894
- 0065508c ["COPY", "tmp:0:8", ["const:538:8"]]
- 0065508c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065508c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065508c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006550cc ["COPY", "tmp:0:8", ["const:938:8"]]
+ 006550cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006550cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006550cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065508c bytes 08e11491
+ 006550cc bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a607edf6aa1e9c575f58adbc3f86363"></a>

### [`00655140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655140.md) → [`00655180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655180.md) FUN_00655180

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
      "definition_site": "00655194",
      "incomplete_value": false,
      "site": "00655198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655154",
      "incomplete_value": false,
      "site": "00655158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "00655198",
      "DATA",
      [
        "storage",
        "00c735b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655198",
      "DATA",
      [
        "storage",
        "00c739b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065514c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655140.md#insn-0065514c) · [`00655154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655140.md#insn-00655154)
- 新版 `0065518c`（命令位置の公開資料なし） · `00655194`（命令位置の公開資料なし）

~~~diff
- 0065514c ["INT_ADD", "register:40f0:8", ["const:65514c:8", "const:4:8"]]
- 0065514c ["CALL", null, ["callee:00c57e90:8"]]
+ 0065518c ["INT_ADD", "register:40f0:8", ["const:65518c:8", "const:4:8"]]
+ 0065518c ["CALL", null, ["callee:00c57e90:8"]]
- 0065514c bytes 510a1894
+ 0065518c bytes 410b1894
- 00655154 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00655154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655194 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00655194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655154 bytes 08e11691
+ 00655194 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d45d8169b174e4d12f6740a95a686a9"></a>

### [`00655164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655164.md) → [`006551a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006551a4.md) FUN_006551a4

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
      "definition_site": "006551a8",
      "incomplete_value": false,
      "site": "006551ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655168",
      "incomplete_value": false,
      "site": "0065516c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "006551ac",
      "DATA",
      [
        "storage",
        "00c735b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006551ac",
      "DATA",
      [
        "storage",
        "00c739b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655164.md#insn-00655168)
- 新版 `006551a8`（命令位置の公開資料なし）

~~~diff
- 00655168 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00655168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006551a8 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 006551a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006551a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006551a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655168 bytes 08e11691
+ 006551a8 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f3da4d39ded837206a9bdc1e03f80d4"></a>

### [`00655208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655208.md) → [`00655248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655248.md) FUN_00655248

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
      "definition_site": "0065525c",
      "incomplete_value": false,
      "site": "00655260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065521c",
      "incomplete_value": false,
      "site": "00655220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "00655260",
      "DATA",
      [
        "storage",
        "00c73638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655260",
      "DATA",
      [
        "storage",
        "00c73a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655208.md#insn-00655214) · [`0065521c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655208.md#insn-0065521c)
- 新版 `00655254`（命令位置の公開資料なし） · `0065525c`（命令位置の公開資料なし）

~~~diff
- 00655214 ["INT_ADD", "register:40f0:8", ["const:655214:8", "const:4:8"]]
- 00655214 ["CALL", null, ["callee:00c57e90:8"]]
+ 00655254 ["INT_ADD", "register:40f0:8", ["const:655254:8", "const:4:8"]]
+ 00655254 ["CALL", null, ["callee:00c57e90:8"]]
- 00655214 bytes 1f0a1894
+ 00655254 bytes 0f0b1894
- 0065521c ["COPY", "tmp:0:8", ["const:638:8"]]
- 0065521c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065521c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065521c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065525c ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 0065525c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065525c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065525c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065521c bytes 08e11891
+ 0065525c bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02500000bed12b8ae710b683f03ac3aa"></a>

### [`0065522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/0065522c.md) → [`0065526c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/0065526c.md) FUN_0065526c

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
      "definition_site": "00655270",
      "incomplete_value": false,
      "site": "00655274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655230",
      "incomplete_value": false,
      "site": "00655234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "00655274",
      "DATA",
      [
        "storage",
        "00c73638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655274",
      "DATA",
      [
        "storage",
        "00c73a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/0065522c.md#insn-00655230)
- 新版 `00655270`（命令位置の公開資料なし）

~~~diff
- 00655230 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00655230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655270 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00655270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655230 bytes 08e11891
+ 00655270 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497cbf01cb2da6f6b1adb768525cb865"></a>

### [`006552d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006552d0.md) → [`00655310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655310.md) FUN_00655310

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
      "definition_site": "00655324",
      "incomplete_value": false,
      "site": "00655328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006552e4",
      "incomplete_value": false,
      "site": "006552e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
      "00655328",
      "DATA",
      [
        "storage",
        "00c736b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655328",
      "DATA",
      [
        "storage",
        "00c73ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006552dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006552d0.md#insn-006552dc) · [`006552e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006552d0.md#insn-006552e4)
- 新版 `0065531c`（命令位置の公開資料なし） · `00655324`（命令位置の公開資料なし）

~~~diff
- 006552dc ["INT_ADD", "register:40f0:8", ["const:6552dc:8", "const:4:8"]]
- 006552dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0065531c ["INT_ADD", "register:40f0:8", ["const:65531c:8", "const:4:8"]]
+ 0065531c ["CALL", null, ["callee:00c57e90:8"]]
- 006552dc bytes ed091894
+ 0065531c bytes dd0a1894
- 006552e4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 006552e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006552e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006552e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655324 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00655324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006552e4 bytes 08e11a91
+ 00655324 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2683c19d7664e05dd6e9f573c1b66294"></a>

### [`006552f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006552f4.md) → [`00655334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655334.md) FUN_00655334

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
      "definition_site": "00655338",
      "incomplete_value": false,
      "site": "0065533c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006552f8",
      "incomplete_value": false,
      "site": "006552fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
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
      "0065533c",
      "DATA",
      [
        "storage",
        "00c736b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065533c",
      "DATA",
      [
        "storage",
        "00c73ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006552f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006552f4.md#insn-006552f8)
- 新版 `00655338`（命令位置の公開資料なし）

~~~diff
- 006552f8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 006552f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006552f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006552f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655338 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00655338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006552f8 bytes 08e11a91
+ 00655338 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d291d68472eadc706f4b4e6ad78514a"></a>

### [`00655398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655398.md) → [`006553d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006553d8.md) FUN_006553d8

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
      "definition_site": "006553ec",
      "incomplete_value": false,
      "site": "006553f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006553ac",
      "incomplete_value": false,
      "site": "006553b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "006553f0",
      "DATA",
      [
        "storage",
        "00c73738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006553f0",
      "DATA",
      [
        "storage",
        "00c73b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006553a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655398.md#insn-006553a4) · [`006553ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655398.md#insn-006553ac)
- 新版 `006553e4`（命令位置の公開資料なし） · `006553ec`（命令位置の公開資料なし）

~~~diff
- 006553a4 ["INT_ADD", "register:40f0:8", ["const:6553a4:8", "const:4:8"]]
- 006553a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 006553e4 ["INT_ADD", "register:40f0:8", ["const:6553e4:8", "const:4:8"]]
+ 006553e4 ["CALL", null, ["callee:00c57e90:8"]]
- 006553a4 bytes bb091894
+ 006553e4 bytes ab0a1894
- 006553ac ["COPY", "tmp:0:8", ["const:738:8"]]
- 006553ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006553ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006553ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006553ec ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 006553ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006553ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006553ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006553ac bytes 08e11c91
+ 006553ec bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88d2b13420d0d75a2cd95d256e4f29af"></a>

### [`006553bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006553bc.md) → [`006553fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006553fc.md) FUN_006553fc

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
      "definition_site": "00655400",
      "incomplete_value": false,
      "site": "00655404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006553c0",
      "incomplete_value": false,
      "site": "006553c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "00655404",
      "DATA",
      [
        "storage",
        "00c73738",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655404",
      "DATA",
      [
        "storage",
        "00c73b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006553c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006553bc.md#insn-006553c0)
- 新版 `00655400`（命令位置の公開資料なし）

~~~diff
- 006553c0 ["COPY", "tmp:0:8", ["const:738:8"]]
- 006553c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006553c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006553c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655400 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00655400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006553c0 bytes 08e11c91
+ 00655400 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c8b4fc7d5693dc01f57bd0b48cbb33"></a>

### [`00655460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655460.md) → [`006554a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006554a0.md) FUN_006554a0

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
      "definition_site": "006554c4",
      "incomplete_value": false,
      "site": "006554c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655484",
      "incomplete_value": false,
      "site": "00655484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "006554c4",
      "DATA",
      [
        "storage",
        "00c737b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006554c4",
      "DATA",
      [
        "storage",
        "00c73bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655460.md#insn-00655474) · [`00655480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655460.md#insn-00655480)
- 新版 `006554b4`（命令位置の公開資料なし） · `006554c0`（命令位置の公開資料なし）

~~~diff
- 00655474 ["INT_ADD", "register:40f0:8", ["const:655474:8", "const:4:8"]]
- 00655474 ["CALL", null, ["callee:00c57e90:8"]]
+ 006554b4 ["INT_ADD", "register:40f0:8", ["const:6554b4:8", "const:4:8"]]
+ 006554b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00655474 bytes 87091894
+ 006554b4 bytes 770a1894
- 00655480 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00655480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006554c0 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 006554c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006554c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006554c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655480 bytes 08e11e91
+ 006554c0 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-260593290d690351d27a486310f18c69"></a>

### [`00655494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655494.md) → [`006554d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006554d4.md) FUN_006554d4

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
      "definition_site": "006554e0",
      "incomplete_value": false,
      "site": "006554e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006554a0",
      "incomplete_value": false,
      "site": "006554a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
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
      "006554e0",
      "DATA",
      [
        "storage",
        "00c737b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006554e0",
      "DATA",
      [
        "storage",
        "00c73bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065549c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655494.md#insn-0065549c)
- 新版 `006554dc`（命令位置の公開資料なし）

~~~diff
- 0065549c ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 0065549c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065549c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065549c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006554dc ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 006554dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006554dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006554dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065549c bytes 29e11e91
+ 006554dc bytes 29e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d4ae5e8d5aef9dcf0a92a5ab5f9913"></a>

### [`006554b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006554b0.md) → [`006554f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006554f0.md) FUN_006554f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00641f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641f00.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00641f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641f40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00655524",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006554e4",
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
      "site": "006557ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006557ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006557f8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006557b8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00655524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00655564",
      "DATA",
      [
        "storage",
        "00435360",
        null,
        "byte[43]"
      ]
    ],
    [
      "00655590",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[39]"
      ]
    ]
  ],
  "added": [
    [
      "00655524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00655564",
      "DATA",
      [
        "storage",
        "00435360",
        null,
        "byte[47]"
      ]
    ],
    [
      "00655590",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006554e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006554b0.md#insn-006554e4) · [`00655778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006554b0.md#insn-00655778) · [`006557ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006554b0.md#insn-006557ac)
- 新版 `00655524`（命令位置の公開資料なし） · `006557b8`（命令位置の公開資料なし） · `006557ec`（命令位置の公開資料なし）

~~~diff
- 006554e4 ["INT_ADD", "register:40f0:8", ["const:6554e4:8", "const:4:8"]]
- 006554e4 ["CALL", null, ["ram:47acb4:8"]]
+ 00655524 ["INT_ADD", "register:40f0:8", ["const:655524:8", "const:4:8"]]
+ 00655524 ["CALL", null, ["ram:47acf4:8"]]
- 006554e4 bytes f495f897
+ 00655524 bytes f495f897
- 00655778 ["INT_ADD", "register:40f0:8", ["const:655778:8", "const:4:8"]]
- 00655778 ["CALL", null, ["callee:008514f8:8"]]
+ 006557b8 ["INT_ADD", "register:40f0:8", ["const:6557b8:8", "const:4:8"]]
+ 006557b8 ["CALL", null, ["callee:008514f8:8"]]
- 00655778 bytes 50ef0794
+ 006557b8 bytes 50ef0794
- 006557ac ["INT_ADD", "register:40f0:8", ["const:6557ac:8", "const:4:8"]]
- 006557ac ["CALL", null, ["ram:47acb4:8"]]
+ 006557ec ["INT_ADD", "register:40f0:8", ["const:6557ec:8", "const:4:8"]]
+ 006557ec ["CALL", null, ["ram:47acf4:8"]]
- 006557ac bytes 4295f897
+ 006557ec bytes 4295f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-785c445b171ad7198ca76481685fcb80"></a>

### [`00655804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655804.md) → [`00655844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655844.md) FUN_00655844

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
      "definition_site": "00655858",
      "incomplete_value": false,
      "site": "0065585c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655818",
      "incomplete_value": false,
      "site": "0065581c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "0065585c",
      "DATA",
      [
        "storage",
        "00c73848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065585c",
      "DATA",
      [
        "storage",
        "00c73c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655804.md#insn-00655810) · [`00655818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655804.md#insn-00655818)
- 新版 `00655850`（命令位置の公開資料なし） · `00655858`（命令位置の公開資料なし）

~~~diff
- 00655810 ["INT_ADD", "register:40f0:8", ["const:655810:8", "const:4:8"]]
- 00655810 ["CALL", null, ["callee:00c57e90:8"]]
+ 00655850 ["INT_ADD", "register:40f0:8", ["const:655850:8", "const:4:8"]]
+ 00655850 ["CALL", null, ["callee:00c57e90:8"]]
- 00655810 bytes a0081894
+ 00655850 bytes 90091894
- 00655818 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00655818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655858 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00655858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655818 bytes 08212191
+ 00655858 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df4e92ee7c30a48a5433e702efdc7d4"></a>

### [`00655840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655840.md) → [`00655880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655880.md) FUN_00655880

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00641f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641f00.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00641f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641f40.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

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
      "site": "0065592c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006558ec",
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
      "site": "00655938",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006558f8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0065592c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00655938",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0065592c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00655938",
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

- 旧版 [`006558ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655840.md#insn-006558ac) · [`006558ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655840.md#insn-006558ec) · [`006558f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655840.md#insn-006558f8)
- 新版 `006558ec`（命令位置の公開資料なし） · `0065592c`（命令位置の公開資料なし） · `00655938`（命令位置の公開資料なし）

~~~diff
- 006558ac ["INT_ADD", "register:40f0:8", ["const:6558ac:8", "const:4:8"]]
- 006558ac ["CALL", null, ["callee:00a46bb8:8"]]
+ 006558ec ["INT_ADD", "register:40f0:8", ["const:6558ec:8", "const:4:8"]]
+ 006558ec ["CALL", null, ["callee:00a46bb8:8"]]
- 006558ac bytes 45c40f94
+ 006558ec bytes b3c40f94
- 006558ec ["INT_ADD", "register:40f0:8", ["const:6558ec:8", "const:4:8"]]
- 006558ec ["CALL", null, ["ram:47acb4:8"]]
+ 0065592c ["INT_ADD", "register:40f0:8", ["const:65592c:8", "const:4:8"]]
+ 0065592c ["CALL", null, ["ram:47acf4:8"]]
- 006558ec bytes f294f897
+ 0065592c bytes f294f897
- 006558f8 ["INT_ADD", "register:40f0:8", ["const:6558f8:8", "const:4:8"]]
- 006558f8 ["CALL", null, ["ram:47acb4:8"]]
+ 00655938 ["INT_ADD", "register:40f0:8", ["const:655938:8", "const:4:8"]]
+ 00655938 ["CALL", null, ["ram:47acf4:8"]]
- 006558f8 bytes ef94f897
+ 00655938 bytes ef94f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719a0f2616c9d4aa77bdb3f5ad4a5669"></a>

### [`00655960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655960.md) → [`006559a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006559a0.md) FUN_006559a0

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
      "definition_site": "006559c4",
      "incomplete_value": false,
      "site": "006559c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655984",
      "incomplete_value": false,
      "site": "00655984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "006559c4",
      "DATA",
      [
        "storage",
        "00c738c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006559c4",
      "DATA",
      [
        "storage",
        "00c73cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655960.md#insn-00655974) · [`00655980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655960.md#insn-00655980)
- 新版 `006559b4`（命令位置の公開資料なし） · `006559c0`（命令位置の公開資料なし）

~~~diff
- 00655974 ["INT_ADD", "register:40f0:8", ["const:655974:8", "const:4:8"]]
- 00655974 ["CALL", null, ["callee:00c57e90:8"]]
+ 006559b4 ["INT_ADD", "register:40f0:8", ["const:6559b4:8", "const:4:8"]]
+ 006559b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00655974 bytes 47081894
+ 006559b4 bytes 37091894
- 00655980 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00655980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006559c0 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 006559c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006559c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006559c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655980 bytes 08212391
+ 006559c0 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53cde9a532404a1ccfe8c9f5790b6653"></a>

### [`00655d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655d7c.md) → [`00655dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655dbc.md) FUN_00655dbc

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
      "definition_site": "00655dd0",
      "incomplete_value": false,
      "site": "00655dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655d90",
      "incomplete_value": false,
      "site": "00655d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "00655dd4",
      "DATA",
      [
        "storage",
        "00c73938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655dd4",
      "DATA",
      [
        "storage",
        "00c73d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655d7c.md#insn-00655d88) · [`00655d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655d7c.md#insn-00655d90)
- 新版 `00655dc8`（命令位置の公開資料なし） · `00655dd0`（命令位置の公開資料なし）

~~~diff
- 00655d88 ["INT_ADD", "register:40f0:8", ["const:655d88:8", "const:4:8"]]
- 00655d88 ["CALL", null, ["callee:00c57e90:8"]]
+ 00655dc8 ["INT_ADD", "register:40f0:8", ["const:655dc8:8", "const:4:8"]]
+ 00655dc8 ["CALL", null, ["callee:00c57e90:8"]]
- 00655d88 bytes 42071894
+ 00655dc8 bytes 32081894
- 00655d90 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00655d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655dd0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00655dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655d90 bytes 08e12491
+ 00655dd0 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6429222aba562f22e6dbc2d9355fe3fb"></a>

### [`00655db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655db8.md) → [`00655df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655df8.md) FUN_00655df8

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
      "site": "00655e14",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00655dd4",
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
      "00655e14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00655e14",
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

- 旧版 [`00655dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655db8.md#insn-00655dd4) · [`00655de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655db8.md#insn-00655de0)
- 新版 `00655e14`（命令位置の公開資料なし） · `00655e20`（命令位置の公開資料なし）

~~~diff
- 00655dd4 ["INT_ADD", "register:40f0:8", ["const:655dd4:8", "const:4:8"]]
- 00655dd4 ["CALL", null, ["ram:47acb4:8"]]
+ 00655e14 ["INT_ADD", "register:40f0:8", ["const:655e14:8", "const:4:8"]]
+ 00655e14 ["CALL", null, ["ram:47acf4:8"]]
- 00655dd4 bytes b893f897
+ 00655e14 bytes b893f897
- 00655de0 ["INT_ADD", "register:40f0:8", ["const:655de0:8", "const:4:8"]]
- 00655de0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00655e20 ["INT_ADD", "register:40f0:8", ["const:655e20:8", "const:4:8"]]
+ 00655e20 ["CALL", null, ["callee:0047cdd4:8"]]
- 00655de0 bytes ed9bf897
+ 00655e20 bytes ed9bf897
~~~


<a id="compare-decf6bd0d63fd6b412e1b9528f4abdf1"></a>

### [`00655e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655e24.md) → [`00655e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/00655e64.md) FUN_00655e64

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
      "definition_site": "00655e88",
      "incomplete_value": false,
      "site": "00655e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655e48",
      "incomplete_value": false,
      "site": "00655e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "00655e88",
      "DATA",
      [
        "storage",
        "00c739c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655e88",
      "DATA",
      [
        "storage",
        "00c73dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655e24.md#insn-00655e38) · [`00655e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/00655e24.md#insn-00655e44)
- 新版 `00655e78`（命令位置の公開資料なし） · `00655e84`（命令位置の公開資料なし）

~~~diff
- 00655e38 ["INT_ADD", "register:40f0:8", ["const:655e38:8", "const:4:8"]]
- 00655e38 ["CALL", null, ["callee:00c57e90:8"]]
+ 00655e78 ["INT_ADD", "register:40f0:8", ["const:655e78:8", "const:4:8"]]
+ 00655e78 ["CALL", null, ["callee:00c57e90:8"]]
- 00655e38 bytes 16071894
+ 00655e78 bytes 06081894
- 00655e44 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00655e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655e84 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00655e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655e44 bytes 08212791
+ 00655e84 bytes 08213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d6c41283f0f53eb143f8235ef4da8c"></a>

### [`0065650c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/0065650c.md) → [`0065654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/0065654c.md) FUN_0065654c

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
      "definition_site": "00656570",
      "incomplete_value": false,
      "site": "00656570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00656530",
      "incomplete_value": false,
      "site": "00656530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00656570",
      "DATA",
      [
        "storage",
        "00c73a48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00656570",
      "DATA",
      [
        "storage",
        "00c73e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00656520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/0065650c.md#insn-00656520) · [`0065652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/0065650c.md#insn-0065652c)
- 新版 `00656560`（命令位置の公開資料なし） · `0065656c`（命令位置の公開資料なし）

~~~diff
- 00656520 ["INT_ADD", "register:40f0:8", ["const:656520:8", "const:4:8"]]
- 00656520 ["CALL", null, ["callee:00c57e90:8"]]
+ 00656560 ["INT_ADD", "register:40f0:8", ["const:656560:8", "const:4:8"]]
+ 00656560 ["CALL", null, ["callee:00c57e90:8"]]
- 00656520 bytes 5c051894
+ 00656560 bytes 4c061894
- 0065652c ["COPY", "tmp:0:8", ["const:a48:8"]]
- 0065652c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065652c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065652c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065656c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0065656c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065656c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065656c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065652c bytes 08212991
+ 0065656c bytes 08213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8806c68bcd1f3507831b2dfa86a95c1e"></a>

### [`00656c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c20.md) → [`00656c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656c60.md) FUN_00656c60

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
      "definition_site": "00656c84",
      "incomplete_value": false,
      "site": "00656c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00656c44",
      "incomplete_value": false,
      "site": "00656c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00656c84",
      "DATA",
      [
        "storage",
        "00c73ac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00656c84",
      "DATA",
      [
        "storage",
        "00c73ec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00656c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c20.md#insn-00656c34) · [`00656c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c20.md#insn-00656c40)
- 新版 `00656c74`（命令位置の公開資料なし） · `00656c80`（命令位置の公開資料なし）

~~~diff
- 00656c34 ["INT_ADD", "register:40f0:8", ["const:656c34:8", "const:4:8"]]
- 00656c34 ["CALL", null, ["callee:00c57e90:8"]]
+ 00656c74 ["INT_ADD", "register:40f0:8", ["const:656c74:8", "const:4:8"]]
+ 00656c74 ["CALL", null, ["callee:00c57e90:8"]]
- 00656c34 bytes 97031894
+ 00656c74 bytes 87041894
- 00656c40 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00656c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00656c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00656c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00656c80 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00656c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00656c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00656c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00656c40 bytes 08212b91
+ 00656c80 bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c92a3cf3e11af67d5d8224cac2cfa241"></a>

### [`00656c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c70.md) → [`00656cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656cb0.md) FUN_00656cb0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00656cd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00656c90",
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
      "site": "00656cdc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00656c9c",
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
      "00656cd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00656cdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00656d00",
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
      "00656cd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00656cdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00656d00",
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

- 旧版 [`00656c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c70.md#insn-00656c90) · [`00656c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c70.md#insn-00656c9c) · [`00656cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656c70.md#insn-00656cd0)
- 新版 `00656cd0`（命令位置の公開資料なし） · `00656cdc`（命令位置の公開資料なし） · `00656d10`（命令位置の公開資料なし）

~~~diff
- 00656c90 ["INT_ADD", "register:40f0:8", ["const:656c90:8", "const:4:8"]]
- 00656c90 ["CALL", null, ["ram:47acb4:8"]]
+ 00656cd0 ["INT_ADD", "register:40f0:8", ["const:656cd0:8", "const:4:8"]]
+ 00656cd0 ["CALL", null, ["ram:47acf4:8"]]
- 00656c90 bytes 0990f897
+ 00656cd0 bytes 0990f897
- 00656c9c ["INT_ADD", "register:40f0:8", ["const:656c9c:8", "const:4:8"]]
- 00656c9c ["CALL", null, ["ram:47acb4:8"]]
+ 00656cdc ["INT_ADD", "register:40f0:8", ["const:656cdc:8", "const:4:8"]]
+ 00656cdc ["CALL", null, ["ram:47acf4:8"]]
- 00656c9c bytes 0690f897
+ 00656cdc bytes 0690f897
- 00656cd0 ["INT_ADD", "register:40f0:8", ["const:656cd0:8", "const:4:8"]]
- 00656cd0 ["CALL", null, ["callee:008514f8:8"]]
+ 00656d10 ["INT_ADD", "register:40f0:8", ["const:656d10:8", "const:4:8"]]
+ 00656d10 ["CALL", null, ["callee:008514f8:8"]]
- 00656cd0 bytes fae90794
+ 00656d10 bytes fae90794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec52d536bfed67c647342c357e754642"></a>

### [`00656e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md) → [`00656e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656e90.md) FUN_00656e90

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00656d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656d18.md) [`00656e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00656d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656d58.md) [`00656e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656e90.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00657004",
      "incomplete_value": false,
      "site": "0065700c",
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
      "definition_site": "00656fc4",
      "incomplete_value": false,
      "site": "00656fcc",
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
      "definition_site": "006570c4",
      "incomplete_value": false,
      "site": "006570cc",
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
      "definition_site": "00657084",
      "incomplete_value": false,
      "site": "0065708c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006570e0",
      "incomplete_value": false,
      "site": "006570ec",
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
      "definition_site": "006570a0",
      "incomplete_value": false,
      "site": "006570ac",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00657004",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "006570c4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "006570e0",
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
      "00657004",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006570c4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006570e0",
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

- 旧版 [`00656fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md#insn-00656fcc) · [`0065708c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md#insn-0065708c) · [`006570ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md#insn-006570ac)
- 新版 `0065700c`（命令位置の公開資料なし） · `006570cc`（命令位置の公開資料なし） · `006570ec`（命令位置の公開資料なし）

~~~diff
- 00656fcc ["INT_ADD", "register:40f0:8", ["const:656fcc:8", "const:4:8"]]
- 00656fcc ["CALL", null, ["callee:00441e94:8"]]
+ 0065700c ["INT_ADD", "register:40f0:8", ["const:65700c:8", "const:4:8"]]
+ 0065700c ["CALL", null, ["callee:00441e94:8"]]
- 00656fcc bytes a2abf797
+ 0065700c bytes a2abf797
- 0065708c ["INT_ADD", "register:40f0:8", ["const:65708c:8", "const:4:8"]]
- 0065708c ["CALL", null, ["callee:00441e94:8"]]
+ 006570cc ["INT_ADD", "register:40f0:8", ["const:6570cc:8", "const:4:8"]]
+ 006570cc ["CALL", null, ["callee:00441e94:8"]]
- 0065708c bytes 72abf797
+ 006570cc bytes 72abf797
- 006570ac ["INT_ADD", "register:40f0:8", ["const:6570ac:8", "const:4:8"]]
- 006570ac ["CALL", null, ["callee:004427f4:8"]]
+ 006570ec ["INT_ADD", "register:40f0:8", ["const:6570ec:8", "const:4:8"]]
+ 006570ec ["CALL", null, ["callee:004427f4:8"]]
- 006570ac bytes c2adf797
+ 006570ec bytes c2adf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9259e7c88a6613acdeac94e50c2da2c1"></a>

### [`006578a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/006578a8.md) → [`006578e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/006578e8.md) FUN_006578e8

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
      "definition_site": "00657908",
      "incomplete_value": false,
      "site": "0065790c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006578c8",
      "incomplete_value": false,
      "site": "006578cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "0065790c",
      "DATA",
      [
        "storage",
        "00c73b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065790c",
      "DATA",
      [
        "storage",
        "00c73f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006578bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/006578a8.md#insn-006578bc) · [`006578c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/006578a8.md#insn-006578c8)
- 新版 `006578fc`（命令位置の公開資料なし） · `00657908`（命令位置の公開資料なし）

~~~diff
- 006578bc ["INT_ADD", "register:40f0:8", ["const:6578bc:8", "const:4:8"]]
- 006578bc ["CALL", null, ["callee:00c57e90:8"]]
+ 006578fc ["INT_ADD", "register:40f0:8", ["const:6578fc:8", "const:4:8"]]
+ 006578fc ["CALL", null, ["callee:00c57e90:8"]]
- 006578bc bytes 75001894
+ 006578fc bytes 65011894
- 006578c8 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 006578c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006578c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006578c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657908 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00657908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006578c8 bytes 08212d91
+ 00657908 bytes 08213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec7c1a0545494420356d81e1fcfe786"></a>

### [`006578e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/006578e0.md) → [`00657920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657920.md) FUN_00657920

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
      "definition_site": "00657924",
      "incomplete_value": false,
      "site": "00657928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006578e4",
      "incomplete_value": false,
      "site": "006578e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00657928",
      "DATA",
      [
        "storage",
        "00c73b48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657928",
      "DATA",
      [
        "storage",
        "00c73f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006578e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/006578e0.md#insn-006578e4)
- 新版 `00657924`（命令位置の公開資料なし）

~~~diff
- 006578e4 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 006578e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006578e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006578e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657924 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00657924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006578e4 bytes 08212d91
+ 00657924 bytes 08213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a625591b39ed38c8fdb856cd1e8681a8"></a>

### [`00657900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657900.md) → [`00657940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657940.md) FUN_00657940

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00657afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657afc.md) [`00657b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657b00.md) [`0065ad00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065a/0065ad00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00657b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657b3c.md) [`00657b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657b40.md) [`0065ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065a/0065ad40.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00657a00",
      "incomplete_value": false,
      "site": "00657a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006579c0",
      "incomplete_value": false,
      "site": "006579c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065797c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065793c",
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
      "site": "006579b4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00657974",
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
      "0065797c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006579b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006579d0",
      "DATA",
      [
        "storage",
        "004347b0",
        null,
        "byte[39]"
      ]
    ]
  ],
  "added": [
    [
      "0065797c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006579b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006579d0",
      "DATA",
      [
        "storage",
        "004347b0",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065793c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657900.md#insn-0065793c) · [`00657974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657900.md#insn-00657974) · [`00657980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657900.md#insn-00657980)
- 新版 `0065797c`（命令位置の公開資料なし） · `006579b4`（命令位置の公開資料なし） · `006579c0`（命令位置の公開資料なし）

~~~diff
- 0065793c ["INT_ADD", "register:40f0:8", ["const:65793c:8", "const:4:8"]]
- 0065793c ["CALL", null, ["ram:47acb4:8"]]
+ 0065797c ["INT_ADD", "register:40f0:8", ["const:65797c:8", "const:4:8"]]
+ 0065797c ["CALL", null, ["ram:47acf4:8"]]
- 0065793c bytes de8cf897
+ 0065797c bytes de8cf897
- 00657974 ["INT_ADD", "register:40f0:8", ["const:657974:8", "const:4:8"]]
- 00657974 ["CALL", null, ["ram:47acb4:8"]]
+ 006579b4 ["INT_ADD", "register:40f0:8", ["const:6579b4:8", "const:4:8"]]
+ 006579b4 ["CALL", null, ["ram:47acf4:8"]]
- 00657974 bytes d08cf897
+ 006579b4 bytes d08cf897
- 00657980 ["INT_ADD", "register:40f0:8", ["const:657980:8", "const:4:8"]]
- 00657980 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006579c0 ["INT_ADD", "register:40f0:8", ["const:6579c0:8", "const:4:8"]]
+ 006579c0 ["CALL", null, ["callee:0047cdd4:8"]]
- 00657980 bytes 0595f897
+ 006579c0 bytes 0595f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c4c95077238825d6c02ed66e065414"></a>

### [`00657aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657aac.md) → [`00657aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657aec.md) FUN_00657aec

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
      "definition_site": "00657b0c",
      "incomplete_value": false,
      "site": "00657b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657acc",
      "incomplete_value": false,
      "site": "00657ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00657b10",
      "DATA",
      [
        "storage",
        "00c73bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657b10",
      "DATA",
      [
        "storage",
        "00c73fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657aac.md#insn-00657ac0) · [`00657acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657aac.md#insn-00657acc)
- 新版 `00657b00`（命令位置の公開資料なし） · `00657b0c`（命令位置の公開資料なし）

~~~diff
- 00657ac0 ["INT_ADD", "register:40f0:8", ["const:657ac0:8", "const:4:8"]]
- 00657ac0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00657b00 ["INT_ADD", "register:40f0:8", ["const:657b00:8", "const:4:8"]]
+ 00657b00 ["CALL", null, ["callee:00c57e90:8"]]
- 00657ac0 bytes f4ff1794
+ 00657b00 bytes e4001894
- 00657acc ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00657acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657b0c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00657b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657acc bytes 08e12e91
+ 00657b0c bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e211905feb916a3070d511029b0867c"></a>

### [`00657ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ae4.md) → [`00657b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657b24.md) FUN_00657b24

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
      "definition_site": "00657b28",
      "incomplete_value": false,
      "site": "00657b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657ae8",
      "incomplete_value": false,
      "site": "00657aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00657b2c",
      "DATA",
      [
        "storage",
        "00c73bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657b2c",
      "DATA",
      [
        "storage",
        "00c73fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ae4.md#insn-00657ae8)
- 新版 `00657b28`（命令位置の公開資料なし）

~~~diff
- 00657ae8 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00657ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657b28 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00657b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657ae8 bytes 08e12e91
+ 00657b28 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f519775f156aa79bd439a31533f03f94"></a>

### [`00657ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ba8.md) → [`00657be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657be8.md) FUN_00657be8

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
      "definition_site": "00657c08",
      "incomplete_value": false,
      "site": "00657c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657bc8",
      "incomplete_value": false,
      "site": "00657bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00657c0c",
      "DATA",
      [
        "storage",
        "00c73c48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657c0c",
      "DATA",
      [
        "storage",
        "00c74048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ba8.md#insn-00657bbc) · [`00657bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ba8.md#insn-00657bc4) · [`00657bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ba8.md#insn-00657bc8)
- 新版 `00657bfc`（命令位置の公開資料なし） · `00657c04`（命令位置の公開資料なし） · `00657c08`（命令位置の公開資料なし）

~~~diff
- 00657bbc ["INT_ADD", "register:40f0:8", ["const:657bbc:8", "const:4:8"]]
- 00657bbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00657bfc ["INT_ADD", "register:40f0:8", ["const:657bfc:8", "const:4:8"]]
+ 00657bfc ["CALL", null, ["callee:00c57e90:8"]]
- 00657bbc bytes b5ff1794
+ 00657bfc bytes a5001894
- 00657bc4 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657c04 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657bc4 bytes e8300090
+ 00657c04 bytes e83000b0
- 00657bc8 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00657bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657c08 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00657c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657bc8 bytes 08213191
+ 00657c08 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4729b0ac7a84ef985622cf4d29cec8de"></a>

### [`00657c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c00.md) → [`00657c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657c40.md) FUN_00657c40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

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
      "site": "00657c60",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00657c20",
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
      "site": "00657c6c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00657c2c",
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
      "00657c60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00657c6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00657c60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00657c6c",
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

- 旧版 [`00657c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c00.md#insn-00657c20) · [`00657c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c00.md#insn-00657c2c)
- 新版 `00657c60`（命令位置の公開資料なし） · `00657c6c`（命令位置の公開資料なし）

~~~diff
- 00657c20 ["INT_ADD", "register:40f0:8", ["const:657c20:8", "const:4:8"]]
- 00657c20 ["CALL", null, ["ram:47acb4:8"]]
+ 00657c60 ["INT_ADD", "register:40f0:8", ["const:657c60:8", "const:4:8"]]
+ 00657c60 ["CALL", null, ["ram:47acf4:8"]]
- 00657c20 bytes 258cf897
+ 00657c60 bytes 258cf897
- 00657c2c ["INT_ADD", "register:40f0:8", ["const:657c2c:8", "const:4:8"]]
- 00657c2c ["CALL", null, ["ram:47acb4:8"]]
+ 00657c6c ["INT_ADD", "register:40f0:8", ["const:657c6c:8", "const:4:8"]]
+ 00657c6c ["CALL", null, ["ram:47acf4:8"]]
- 00657c2c bytes 228cf897
+ 00657c6c bytes 228cf897
~~~


<a id="compare-e92d23be892d1fd55bf0235848082c00"></a>

### [`00657c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c90.md) → [`00657cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657cd0.md) FUN_00657cd0

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
      "definition_site": "00657ce4",
      "incomplete_value": false,
      "site": "00657ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657ca4",
      "incomplete_value": false,
      "site": "00657ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00657ce8",
      "DATA",
      [
        "storage",
        "00c73cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657ce8",
      "DATA",
      [
        "storage",
        "00c740c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c90.md#insn-00657c9c) · [`00657ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c90.md#insn-00657ca0) · [`00657ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657c90.md#insn-00657ca4)
- 新版 `00657cdc`（命令位置の公開資料なし） · `00657ce0`（命令位置の公開資料なし） · `00657ce4`（命令位置の公開資料なし）

~~~diff
- 00657c9c ["INT_ADD", "register:40f0:8", ["const:657c9c:8", "const:4:8"]]
- 00657c9c ["CALL", null, ["callee:00c57e90:8"]]
+ 00657cdc ["INT_ADD", "register:40f0:8", ["const:657cdc:8", "const:4:8"]]
+ 00657cdc ["CALL", null, ["callee:00c57e90:8"]]
- 00657c9c bytes 7dff1794
+ 00657cdc bytes 6d001894
- 00657ca0 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657ce0 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657ca0 bytes e8300090
+ 00657ce0 bytes e83000b0
- 00657ca4 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00657ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657ce4 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00657ce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657ca4 bytes 08213391
+ 00657ce4 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a4d69dc04761ad0e801300e5b16e25c"></a>

### [`00657cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657cb4.md) → [`00657cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657cf4.md) FUN_00657cf4

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
      "definition_site": "00657cf8",
      "incomplete_value": false,
      "site": "00657cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657cb8",
      "incomplete_value": false,
      "site": "00657cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00657cfc",
      "DATA",
      [
        "storage",
        "00c73cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657cfc",
      "DATA",
      [
        "storage",
        "00c740c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657cb4.md#insn-00657cb4) · [`00657cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657cb4.md#insn-00657cb8)
- 新版 `00657cf4`（命令位置の公開資料なし） · `00657cf8`（命令位置の公開資料なし）

~~~diff
- 00657cb4 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657cf4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657cb4 bytes e8300090
+ 00657cf4 bytes e83000b0
- 00657cb8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00657cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00657cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657cb8 bytes 08213391
+ 00657cf8 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1de24751f4caba871c458a5ad38387e1"></a>

### [`00657db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657db8.md) → [`00657df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657df8.md) FUN_00657df8

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
      "definition_site": "00657e0c",
      "incomplete_value": false,
      "site": "00657e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657dcc",
      "incomplete_value": false,
      "site": "00657dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "00657e10",
      "DATA",
      [
        "storage",
        "00c73d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657e10",
      "DATA",
      [
        "storage",
        "00c74148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657db8.md#insn-00657dc4) · [`00657dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657db8.md#insn-00657dc8) · [`00657dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657db8.md#insn-00657dcc)
- 新版 `00657e04`（命令位置の公開資料なし） · `00657e08`（命令位置の公開資料なし） · `00657e0c`（命令位置の公開資料なし）

~~~diff
- 00657dc4 ["INT_ADD", "register:40f0:8", ["const:657dc4:8", "const:4:8"]]
- 00657dc4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00657e04 ["INT_ADD", "register:40f0:8", ["const:657e04:8", "const:4:8"]]
+ 00657e04 ["CALL", null, ["callee:00c57e90:8"]]
- 00657dc4 bytes 33ff1794
+ 00657e04 bytes 23001894
- 00657dc8 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657e08 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657dc8 bytes e8300090
+ 00657e08 bytes e83000b0
- 00657dcc ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00657dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657e0c ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00657e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657dcc bytes 08213591
+ 00657e0c bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd17b91ca5afe398e4e4328201371067"></a>

### [`00657ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ddc.md) → [`00657e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657e1c.md) FUN_00657e1c

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
      "definition_site": "00657e20",
      "incomplete_value": false,
      "site": "00657e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657de0",
      "incomplete_value": false,
      "site": "00657de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
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
      "00657e24",
      "DATA",
      [
        "storage",
        "00c73d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657e24",
      "DATA",
      [
        "storage",
        "00c74148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ddc.md#insn-00657ddc) · [`00657de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ddc.md#insn-00657de0)
- 新版 `00657e1c`（命令位置の公開資料なし） · `00657e20`（命令位置の公開資料なし）

~~~diff
- 00657ddc ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657e1c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657ddc bytes e8300090
+ 00657e1c bytes e83000b0
- 00657de0 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00657de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657e20 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00657e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657de0 bytes 08213591
+ 00657e20 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9a954b8819ff84deb0fc0065bc46c1d"></a>

### [`00657e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657e84.md) → [`00657ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657ec4.md) FUN_00657ec4

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
      "definition_site": "00657ed8",
      "incomplete_value": false,
      "site": "00657edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657e98",
      "incomplete_value": false,
      "site": "00657e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00657edc",
      "DATA",
      [
        "storage",
        "00c73dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657edc",
      "DATA",
      [
        "storage",
        "00c741c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657e84.md#insn-00657e90) · [`00657e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657e84.md#insn-00657e94) · [`00657e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657e84.md#insn-00657e98)
- 新版 `00657ed0`（命令位置の公開資料なし） · `00657ed4`（命令位置の公開資料なし） · `00657ed8`（命令位置の公開資料なし）

~~~diff
- 00657e90 ["INT_ADD", "register:40f0:8", ["const:657e90:8", "const:4:8"]]
- 00657e90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00657ed0 ["INT_ADD", "register:40f0:8", ["const:657ed0:8", "const:4:8"]]
+ 00657ed0 ["CALL", null, ["callee:00c57e90:8"]]
- 00657e90 bytes 00ff1794
+ 00657ed0 bytes f0ff1794
- 00657e94 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657ed4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657e94 bytes e8300090
+ 00657ed4 bytes e83000b0
- 00657e98 ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00657e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657ed8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00657ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657e98 bytes 08213791
+ 00657ed8 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-125c6be049a623e9cd103eeb77c6e7e9"></a>

### [`00657ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ea8.md) → [`00657ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657ee8.md) FUN_00657ee8

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
      "definition_site": "00657eec",
      "incomplete_value": false,
      "site": "00657ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657eac",
      "incomplete_value": false,
      "site": "00657eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:dc8:8"
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
      "00657ef0",
      "DATA",
      [
        "storage",
        "00c73dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657ef0",
      "DATA",
      [
        "storage",
        "00c741c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ea8.md#insn-00657ea8) · [`00657eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657ea8.md#insn-00657eac)
- 新版 `00657ee8`（命令位置の公開資料なし） · `00657eec`（命令位置の公開資料なし）

~~~diff
- 00657ea8 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00657ee8 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00657ea8 bytes e8300090
+ 00657ee8 bytes e83000b0
- 00657eac ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 00657eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657eec ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00657eec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657eec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657eec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657eac bytes 08213791
+ 00657eec bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c0f499614095e36a67e8f40e80c316b"></a>

### [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) → [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) FUN_00657f8c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 21件 [`0044db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044d/0044db10.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md)
- 新版 呼出元 2件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 21件 [`0044db50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da48.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.50% / 新版 91.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_destination` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065804c",
      "incomplete_value": true,
      "site": "0065804c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065800c",
      "incomplete_value": true,
      "site": "0065800c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
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
      "definition_site": "00658178",
      "incomplete_value": true,
      "site": "00658178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00658138",
      "incomplete_value": true,
      "site": "00658138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "006581e4",
      "incomplete_value": true,
      "site": "006581e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:cd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006581a4",
      "incomplete_value": true,
      "site": "006581a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:8d4:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00657fcc",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "00657fe4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "00657ffc",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00657fcc",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "00657fe4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "00657ffc",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md#insn-00657fe0) · [`00658074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md#insn-00658074) · [`00658138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md#insn-00658138)
- 新版 `00658020`（命令位置の公開資料なし） · `006580b4`（命令位置の公開資料なし） · `00658178`（命令位置の公開資料なし）

~~~diff
- 00657fe0 ["INT_ADD", "register:40f0:8", ["const:657fe0:8", "const:4:8"]]
- 00657fe0 ["CALL", null, ["ram:48ccb8:8"]]
+ 00658020 ["INT_ADD", "register:40f0:8", ["const:658020:8", "const:4:8"]]
+ 00658020 ["CALL", null, ["ram:48ccf8:8"]]
- 00657fe0 bytes 36d3f897
+ 00658020 bytes 36d3f897
- 00658074 ["INT_ADD", "register:40f0:8", ["const:658074:8", "const:4:8"]]
- 00658074 ["CALL", null, ["ram:46c984:8"]]
+ 006580b4 ["INT_ADD", "register:40f0:8", ["const:6580b4:8", "const:4:8"]]
+ 006580b4 ["CALL", null, ["ram:46c9c4:8"]]
- 00658074 bytes 4452f897
+ 006580b4 bytes 4452f897
- 00658138 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00658138 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "const:8d0:8"]]
- 00658138 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00658178 ["COPY", "tmp:0:4", ["register:40a8:4"]]
+ 00658178 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "const:cd0:8"]]
+ 00658178 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00658138 bytes 15432339
+ 00658178 bytes 15433339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0eaa65eea152bb52008ee1cbf831650"></a>

### [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) → [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md) FUN_00659e9c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00658d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658d6c.md) [`0065ebb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ebb8.md) · 呼出先 32件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md)
- 新版 呼出元 2件 [`00658dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658dac.md) [`0065ebf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ebf8.md) · 呼出先 32件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 2件, `store_destination` 11件, `store_value` 20件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00659f04",
      "incomplete_value": false,
      "site": "00659f04",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00659ec4",
      "incomplete_value": false,
      "site": "00659ec4",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00659f10",
      "incomplete_value": true,
      "site": "00659f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00659ed0",
      "incomplete_value": true,
      "site": "00659ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00659f18",
      "incomplete_value": false,
      "site": "00659f18",
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
            "const:cd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00659ed8",
      "incomplete_value": false,
      "site": "00659ed8",
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
            "const:8d4:8"
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
      "00659edc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00659f04",
      "WRITE",
      [
        "storage",
        "00ca68d8",
        null,
        "undefined4"
      ]
    ],
    [
      "00659f10",
      "WRITE",
      [
        "storage",
        "00ca68d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00659edc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00659f04",
      "WRITE",
      [
        "storage",
        "00ca6cd8",
        null,
        "undefined4"
      ]
    ],
    [
      "00659f10",
      "WRITE",
      [
        "storage",
        "00ca6cd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00659e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md#insn-00659e98) · [`00659ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md#insn-00659ec4) · [`00659ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md#insn-00659ed0)
- 新版 `00659ed8`（命令位置の公開資料なし） · `00659f04`（命令位置の公開資料なし） · `00659f10`（命令位置の公開資料なし）

~~~diff
- 00659e98 ["INT_ADD", "register:40f0:8", ["const:659e98:8", "const:4:8"]]
- 00659e98 ["CALL", null, ["callee:008514f8:8"]]
+ 00659ed8 ["INT_ADD", "register:40f0:8", ["const:659ed8:8", "const:4:8"]]
+ 00659ed8 ["CALL", null, ["callee:008514f8:8"]]
- 00659e98 bytes 88dd0794
+ 00659ed8 bytes 88dd0794
- 00659ec4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8d8:8"]]
- 00659ec4 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00659ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00659f04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:cd8:8"]]
+ 00659f04 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00659f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00659ec4 bytes 5fd908b9
+ 00659f04 bytes 5fd90cb9
- 00659ed0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00659ed0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00659ed0 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:8d0:8"]]
- 00659ed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00659f10 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00659f10 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00659f10 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:cd0:8"]]
+ 00659f10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00659ed0 bytes 7f412339
+ 00659f10 bytes 7f413339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-264c9276d62e80269b7491cb433013c9"></a>

### [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) → [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md) FUN_0065be2c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0065ad00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065a/0065ad00.md) [`0065f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065f630.md) · 呼出先 32件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md)
- 新版 呼出元 2件 [`0065ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065a/0065ad40.md) [`0065f670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065f/0065f670.md) · 呼出先 32件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.49% / 新版 89.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 2件, `store_destination` 11件, `store_value` 20件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065be94",
      "incomplete_value": false,
      "site": "0065be94",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065be54",
      "incomplete_value": false,
      "site": "0065be54",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065bea0",
      "incomplete_value": true,
      "site": "0065bea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065be60",
      "incomplete_value": true,
      "site": "0065be60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:8d0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065bea8",
      "incomplete_value": false,
      "site": "0065bea8",
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
            "const:cd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065be68",
      "incomplete_value": false,
      "site": "0065be68",
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
            "const:8d4:8"
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
      "0065be6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065be94",
      "WRITE",
      [
        "storage",
        "00ca68d8",
        null,
        "undefined4"
      ]
    ],
    [
      "0065bea0",
      "WRITE",
      [
        "storage",
        "00ca68d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0065be6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065be94",
      "WRITE",
      [
        "storage",
        "00ca6cd8",
        null,
        "undefined4"
      ]
    ],
    [
      "0065bea0",
      "WRITE",
      [
        "storage",
        "00ca6cd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md#insn-0065be28) · [`0065be54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md#insn-0065be54) · [`0065be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md#insn-0065be60)
- 新版 `0065be68`（命令位置の公開資料なし） · `0065be94`（命令位置の公開資料なし） · `0065bea0`（命令位置の公開資料なし）

~~~diff
- 0065be28 ["INT_ADD", "register:40f0:8", ["const:65be28:8", "const:4:8"]]
- 0065be28 ["CALL", null, ["callee:008514f8:8"]]
+ 0065be68 ["INT_ADD", "register:40f0:8", ["const:65be68:8", "const:4:8"]]
+ 0065be68 ["CALL", null, ["callee:008514f8:8"]]
- 0065be28 bytes a4d50794
+ 0065be68 bytes a4d50794
- 0065be54 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8d8:8"]]
- 0065be54 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0065be54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 0065be94 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:cd8:8"]]
+ 0065be94 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0065be94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 0065be54 bytes 5fd908b9
+ 0065be94 bytes 5fd90cb9
- 0065be60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0065be60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0065be60 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:8d0:8"]]
- 0065be60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0065bea0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0065bea0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0065bea0 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:cd0:8"]]
+ 0065bea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0065be60 bytes 7f412339
+ 0065bea0 bytes 7f413339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a046409e234fc7b4094f8957569ec3ca"></a>

### [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) → [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) FUN_0065cccc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 31件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md)
- 新版 呼出元 1件 [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) · 呼出先 31件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065cd34",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065ccf4",
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
      "site": "0065cde4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065cda4",
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
      "site": "0065d148",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065d108",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065cd34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065cde4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065cf04",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0065cd34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065cde4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065cf04",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[39]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ccf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md#insn-0065ccf4) · [`0065cd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md#insn-0065cd34) · [`0065cda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md#insn-0065cda4)
- 新版 `0065cd34`（命令位置の公開資料なし） · `0065cd74`（命令位置の公開資料なし） · `0065cde4`（命令位置の公開資料なし）

~~~diff
- 0065ccf4 ["INT_ADD", "register:40f0:8", ["const:65ccf4:8", "const:4:8"]]
- 0065ccf4 ["CALL", null, ["ram:46c984:8"]]
+ 0065cd34 ["INT_ADD", "register:40f0:8", ["const:65cd34:8", "const:4:8"]]
+ 0065cd34 ["CALL", null, ["ram:46c9c4:8"]]
- 0065ccf4 bytes 243ff897
+ 0065cd34 bytes 243ff897
- 0065cd34 ["INT_ADD", "register:40f0:8", ["const:65cd34:8", "const:4:8"]]
- 0065cd34 ["CALL", null, ["callee:00467b60:8"]]
+ 0065cd74 ["INT_ADD", "register:40f0:8", ["const:65cd74:8", "const:4:8"]]
+ 0065cd74 ["CALL", null, ["callee:00467b60:8"]]
- 0065cd34 bytes 7b2bf897
+ 0065cd74 bytes 7b2bf897
- 0065cda4 ["INT_ADD", "register:40f0:8", ["const:65cda4:8", "const:4:8"]]
- 0065cda4 ["CALL", null, ["ram:46c984:8"]]
+ 0065cde4 ["INT_ADD", "register:40f0:8", ["const:65cde4:8", "const:4:8"]]
+ 0065cde4 ["CALL", null, ["ram:46c9c4:8"]]
- 0065cda4 bytes f83ef897
+ 0065cde4 bytes f83ef897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c508c375c3450ad2a51041c71f8200"></a>

### [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) → [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) FUN_0065d630

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) · 呼出先 31件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md)
- 新版 呼出元 1件 [`00651aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00651/00651aa4.md) · 呼出先 31件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065d698",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065d658",
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
      "site": "0065d748",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065d708",
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
      "site": "0065daac",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065da6c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065d698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065d748",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0065d868",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0065d698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065d748",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0065d868",
      "DATA",
      [
        "storage",
        "004347f8",
        null,
        "byte[39]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065d658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md#insn-0065d658) · [`0065d698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md#insn-0065d698) · [`0065d708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md#insn-0065d708)
- 新版 `0065d698`（命令位置の公開資料なし） · `0065d6d8`（命令位置の公開資料なし） · `0065d748`（命令位置の公開資料なし）

~~~diff
- 0065d658 ["INT_ADD", "register:40f0:8", ["const:65d658:8", "const:4:8"]]
- 0065d658 ["CALL", null, ["ram:46c984:8"]]
+ 0065d698 ["INT_ADD", "register:40f0:8", ["const:65d698:8", "const:4:8"]]
+ 0065d698 ["CALL", null, ["ram:46c9c4:8"]]
- 0065d658 bytes cb3cf897
+ 0065d698 bytes cb3cf897
- 0065d698 ["INT_ADD", "register:40f0:8", ["const:65d698:8", "const:4:8"]]
- 0065d698 ["CALL", null, ["callee:00467b60:8"]]
+ 0065d6d8 ["INT_ADD", "register:40f0:8", ["const:65d6d8:8", "const:4:8"]]
+ 0065d6d8 ["CALL", null, ["callee:00467b60:8"]]
- 0065d698 bytes 2229f897
+ 0065d6d8 bytes 2229f897
- 0065d708 ["INT_ADD", "register:40f0:8", ["const:65d708:8", "const:4:8"]]
- 0065d708 ["CALL", null, ["ram:46c984:8"]]
+ 0065d748 ["INT_ADD", "register:40f0:8", ["const:65d748:8", "const:4:8"]]
+ 0065d748 ["CALL", null, ["ram:46c9c4:8"]]
- 0065d708 bytes 9f3cf897
+ 0065d748 bytes 9f3cf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eebd778aa39745860b63a6fd20a84731"></a>

### [`0065df54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df54.md) → [`0065df94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065df94.md) FUN_0065df94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065dfa0",
      "incomplete_value": false,
      "site": "0065dfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065df60",
      "incomplete_value": false,
      "site": "0065df6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0065dfac",
      "DATA",
      [
        "storage",
        "00c73e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065dfac",
      "DATA",
      [
        "storage",
        "00c74248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065df5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df54.md#insn-0065df5c) · [`0065df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df54.md#insn-0065df60)
- 新版 `0065df9c`（命令位置の公開資料なし） · `0065dfa0`（命令位置の公開資料なし）

~~~diff
- 0065df5c ["COPY", "register:4050:8", ["const:c73000:8"]]
+ 0065df9c ["COPY", "register:4050:8", ["const:c74000:8"]]
- 0065df5c bytes aa3000d0
+ 0065df9c bytes aa3000f0
- 0065df60 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0065df60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0065df60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0065df60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0065dfa0 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0065dfa0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0065dfa0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0065dfa0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0065df60 bytes 4a213991
+ 0065dfa0 bytes 4a210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7998721f93c653f7b8af490448381d05"></a>

### [`0065df98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df98.md) → [`0065dfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065dfd8.md) FUN_0065dfd8

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
      "definition_site": "0065dff0",
      "incomplete_value": false,
      "site": "0065dffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065dfb0",
      "incomplete_value": false,
      "site": "0065dfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0065dffc",
      "DATA",
      [
        "storage",
        "00c73e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065dffc",
      "DATA",
      [
        "storage",
        "00c74248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065dfac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df98.md#insn-0065dfac) · [`0065dfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df98.md#insn-0065dfb0) · [`0065dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065df98.md#insn-0065dfe0)
- 新版 `0065dfec`（命令位置の公開資料なし） · `0065dff0`（命令位置の公開資料なし） · `0065e020`（命令位置の公開資料なし）

~~~diff
- 0065dfac ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0065dfec ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065dfac bytes a83000d0
+ 0065dfec bytes a83000f0
- 0065dfb0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0065dfb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065dfb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065dfb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065dff0 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0065dff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065dff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065dff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065dfb0 bytes 08213991
+ 0065dff0 bytes 08210991
- 0065dfe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0065dfe0 ["INT_ADD", "register:40f0:8", ["const:65dfe0:8", "const:4:8"]]
- 0065dfe0 ["CALLIND", null, ["register:0:8"]]
+ 0065e020 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0065e020 ["INT_ADD", "register:40f0:8", ["const:65e020:8", "const:4:8"]]
+ 0065e020 ["CALLIND", null, ["register:0:8"]]
- 0065dfe0 bytes 00013fd6
+ 0065e020 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e23c6e370d856bbde79b294cf717523d"></a>

### [`0065dff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065dff4.md) → [`0065e034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e034.md) FUN_0065e034

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065e05c",
      "incomplete_value": false,
      "site": "0065e060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065e01c",
      "incomplete_value": false,
      "site": "0065e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0065e060",
      "DATA",
      [
        "storage",
        "00c73e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e060",
      "DATA",
      [
        "storage",
        "00c74248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065dff4.md#insn-0065e008) · [`0065e018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065dff4.md#insn-0065e018) · [`0065e01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065dff4.md#insn-0065e01c)
- 新版 `0065e048`（命令位置の公開資料なし） · `0065e058`（命令位置の公開資料なし） · `0065e05c`（命令位置の公開資料なし）

~~~diff
- 0065e008 ["INT_ADD", "register:40f0:8", ["const:65e008:8", "const:4:8"]]
- 0065e008 ["CALL", null, ["callee:00c57e90:8"]]
+ 0065e048 ["INT_ADD", "register:40f0:8", ["const:65e048:8", "const:4:8"]]
+ 0065e048 ["CALL", null, ["callee:00c57e90:8"]]
- 0065e008 bytes a2e61794
+ 0065e048 bytes 92e71794
- 0065e018 ["COPY", "register:4048:8", ["const:c73000:8"]]
+ 0065e058 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0065e018 bytes a93000b0
+ 0065e058 bytes a93000d0
- 0065e01c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0065e01c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065e01c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065e01c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065e05c ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0065e05c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e05c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e05c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065e01c bytes 29213991
+ 0065e05c bytes 29210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fdb049478b97f4e01b1d2c0eae780df"></a>

### [`0065e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e084.md) → [`0065e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e0c4.md) FUN_0065e0c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065e0e0",
      "incomplete_value": false,
      "site": "0065e0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065e0a0",
      "incomplete_value": false,
      "site": "0065e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0065e0e4",
      "DATA",
      [
        "storage",
        "00c73e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e0e4",
      "DATA",
      [
        "storage",
        "00c74248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e084.md#insn-0065e09c) · [`0065e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e084.md#insn-0065e0a0) · [`0065e0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e084.md#insn-0065e0c8)
- 新版 `0065e0dc`（命令位置の公開資料なし） · `0065e0e0`（命令位置の公開資料なし） · `0065e108`（命令位置の公開資料なし）

~~~diff
- 0065e09c ["COPY", "register:4050:8", ["const:c73000:8"]]
+ 0065e0dc ["COPY", "register:4050:8", ["const:c74000:8"]]
- 0065e09c bytes aa3000b0
+ 0065e0dc bytes aa3000d0
- 0065e0a0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0065e0a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0065e0a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0065e0a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0065e0e0 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0065e0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0065e0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0065e0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0065e0a0 bytes 4a213991
+ 0065e0e0 bytes 4a210991
- 0065e0c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0065e0c8 ["INT_ADD", "register:40f0:8", ["const:65e0c8:8", "const:4:8"]]
- 0065e0c8 ["CALLIND", null, ["register:0:8"]]
+ 0065e108 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0065e108 ["INT_ADD", "register:40f0:8", ["const:65e108:8", "const:4:8"]]
+ 0065e108 ["CALLIND", null, ["register:0:8"]]
- 0065e0c8 bytes 20013fd6
+ 0065e108 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2afe9bdb9633cab49179fcd128f87f5"></a>

### [`0065e1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e1bc.md) → [`0065e1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e1fc.md) FUN_0065e1fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065e18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e18c.md) · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00658364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658364.md)
- 新版 呼出元 1件 [`0065e1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e1cc.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006583a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/006583a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "0065e220",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065e1e0",
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
      "site": "0065e22c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065e1ec",
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
      "0065e220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065e22c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0065e220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065e22c",
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

- 旧版 [`0065e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e1bc.md#insn-0065e1e0) · [`0065e1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e1bc.md#insn-0065e1ec) · [`0065e210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e1bc.md#insn-0065e210)
- 新版 `0065e220`（命令位置の公開資料なし） · `0065e22c`（命令位置の公開資料なし） · `0065e250`（命令位置の公開資料なし）

~~~diff
- 0065e1e0 ["INT_ADD", "register:40f0:8", ["const:65e1e0:8", "const:4:8"]]
- 0065e1e0 ["CALL", null, ["ram:47acb4:8"]]
+ 0065e220 ["INT_ADD", "register:40f0:8", ["const:65e220:8", "const:4:8"]]
+ 0065e220 ["CALL", null, ["ram:47acf4:8"]]
- 0065e1e0 bytes b572f897
+ 0065e220 bytes b572f897
- 0065e1ec ["INT_ADD", "register:40f0:8", ["const:65e1ec:8", "const:4:8"]]
- 0065e1ec ["CALL", null, ["ram:47acb4:8"]]
+ 0065e22c ["INT_ADD", "register:40f0:8", ["const:65e22c:8", "const:4:8"]]
+ 0065e22c ["CALL", null, ["ram:47acf4:8"]]
- 0065e1ec bytes b272f897
+ 0065e22c bytes b272f897
- 0065e210 ["INT_ADD", "register:40f0:8", ["const:65e210:8", "const:4:8"]]
- 0065e210 ["CALL", null, ["callee:006583a4:8"]]
+ 0065e250 ["INT_ADD", "register:40f0:8", ["const:65e250:8", "const:4:8"]]
+ 0065e250 ["CALL", null, ["callee:006583a4:8"]]
- 0065e210 bytes 55e8ff97
+ 0065e250 bytes 55e8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497581d36829e87406208e5b3d5d9c23"></a>

### [`0065e244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e244.md) → [`0065e284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e284.md) FUN_0065e284

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
      "definition_site": "0065e298",
      "incomplete_value": false,
      "site": "0065e29c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065e258",
      "incomplete_value": false,
      "site": "0065e25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "0065e29c",
      "DATA",
      [
        "storage",
        "00c73ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e29c",
      "DATA",
      [
        "storage",
        "00c742c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e244.md#insn-0065e250) · [`0065e254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e244.md#insn-0065e254) · [`0065e258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e244.md#insn-0065e258)
- 新版 `0065e290`（命令位置の公開資料なし） · `0065e294`（命令位置の公開資料なし） · `0065e298`（命令位置の公開資料なし）

~~~diff
- 0065e250 ["INT_ADD", "register:40f0:8", ["const:65e250:8", "const:4:8"]]
- 0065e250 ["CALL", null, ["callee:00c57e90:8"]]
+ 0065e290 ["INT_ADD", "register:40f0:8", ["const:65e290:8", "const:4:8"]]
+ 0065e290 ["CALL", null, ["callee:00c57e90:8"]]
- 0065e250 bytes 10e61794
+ 0065e290 bytes 00e71794
- 0065e254 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0065e294 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065e254 bytes a83000b0
+ 0065e294 bytes a83000d0
- 0065e258 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 0065e258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065e258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065e258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065e298 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0065e298 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e298 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e298 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065e258 bytes 08213b91
+ 0065e298 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c721366ef79d08344bcc3188dbd398f4"></a>

### [`0065e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e2b0.md) → [`0065e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e2f0.md) FUN_0065e2f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065e280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e280.md) · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 1件 [`0065e2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e2c0.md) · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "0065e310",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065e2d0",
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
      "site": "0065e31c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065e2dc",
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
      "0065e310",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065e31c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065e340",
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
      "0065e310",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065e31c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065e340",
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

- 旧版 [`0065e2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e2b0.md#insn-0065e2d0) · [`0065e2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e2b0.md#insn-0065e2dc) · [`0065e310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e2b0.md#insn-0065e310)
- 新版 `0065e310`（命令位置の公開資料なし） · `0065e31c`（命令位置の公開資料なし） · `0065e350`（命令位置の公開資料なし）

~~~diff
- 0065e2d0 ["INT_ADD", "register:40f0:8", ["const:65e2d0:8", "const:4:8"]]
- 0065e2d0 ["CALL", null, ["ram:47acb4:8"]]
+ 0065e310 ["INT_ADD", "register:40f0:8", ["const:65e310:8", "const:4:8"]]
+ 0065e310 ["CALL", null, ["ram:47acf4:8"]]
- 0065e2d0 bytes 7972f897
+ 0065e310 bytes 7972f897
- 0065e2dc ["INT_ADD", "register:40f0:8", ["const:65e2dc:8", "const:4:8"]]
- 0065e2dc ["CALL", null, ["ram:47acb4:8"]]
+ 0065e31c ["INT_ADD", "register:40f0:8", ["const:65e31c:8", "const:4:8"]]
+ 0065e31c ["CALL", null, ["ram:47acf4:8"]]
- 0065e2dc bytes 7672f897
+ 0065e31c bytes 7672f897
- 0065e310 ["INT_ADD", "register:40f0:8", ["const:65e310:8", "const:4:8"]]
- 0065e310 ["CALL", null, ["callee:008514f8:8"]]
+ 0065e350 ["INT_ADD", "register:40f0:8", ["const:65e350:8", "const:4:8"]]
+ 0065e350 ["CALL", null, ["callee:008514f8:8"]]
- 0065e310 bytes 6acc0794
+ 0065e350 bytes 6acc0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ec154b1a08fa16e458df072ae4e9dd"></a>

### [`0065e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e330.md) → [`0065e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e370.md) FUN_0065e370

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00658d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658d6c.md) [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) [`0065ad00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065a/0065ad00.md) [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) [`0065e330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e330.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 8件 [`00658dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658dac.md) [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md) [`0065ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065a/0065ad40.md) [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md) [`0065e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065e370.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0065e4c0",
      "incomplete_value": false,
      "site": "0065e4c8",
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
      "definition_site": "0065e480",
      "incomplete_value": false,
      "site": "0065e488",
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
      "definition_site": "0065e4e4",
      "incomplete_value": false,
      "site": "0065e4f0",
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
      "definition_site": "0065e4a4",
      "incomplete_value": false,
      "site": "0065e4b0",
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
      "definition_site": "0065e618",
      "incomplete_value": false,
      "site": "0065e620",
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
      "definition_site": "0065e5d8",
      "incomplete_value": false,
      "site": "0065e5e0",
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
      "0065e4c0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0065e4e4",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0065e618",
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
      "0065e4c0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0065e4e4",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0065e618",
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

- 旧版 [`0065e488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e330.md#insn-0065e488) · [`0065e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e330.md#insn-0065e4b0) · [`0065e5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065e330.md#insn-0065e5e0)
- 新版 `0065e4c8`（命令位置の公開資料なし） · `0065e4f0`（命令位置の公開資料なし） · `0065e620`（命令位置の公開資料なし）

~~~diff
- 0065e488 ["INT_ADD", "register:40f0:8", ["const:65e488:8", "const:4:8"]]
- 0065e488 ["CALL", null, ["callee:00441e94:8"]]
+ 0065e4c8 ["INT_ADD", "register:40f0:8", ["const:65e4c8:8", "const:4:8"]]
+ 0065e4c8 ["CALL", null, ["callee:00441e94:8"]]
- 0065e488 bytes 738ef797
+ 0065e4c8 bytes 738ef797
- 0065e4b0 ["INT_ADD", "register:40f0:8", ["const:65e4b0:8", "const:4:8"]]
- 0065e4b0 ["CALL", null, ["callee:004427f4:8"]]
+ 0065e4f0 ["INT_ADD", "register:40f0:8", ["const:65e4f0:8", "const:4:8"]]
+ 0065e4f0 ["CALL", null, ["callee:004427f4:8"]]
- 0065e4b0 bytes c190f797
+ 0065e4f0 bytes c190f797
- 0065e5e0 ["INT_ADD", "register:40f0:8", ["const:65e5e0:8", "const:4:8"]]
- 0065e5e0 ["CALL", null, ["callee:00441e94:8"]]
+ 0065e620 ["INT_ADD", "register:40f0:8", ["const:65e620:8", "const:4:8"]]
+ 0065e620 ["CALL", null, ["callee:00441e94:8"]]
- 0065e5e0 bytes 1d8ef797
+ 0065e620 bytes 1d8ef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f43169350115f87856e4005469fc0c"></a>

### [`0065ebb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ebb8.md) → [`0065ebf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ebf8.md) FUN_0065ebf8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065eb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eb88.md) · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md)
- 新版 呼出元 1件 [`0065ebc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ebc8.md) · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

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
      "site": "0065ec18",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065ebd8",
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
      "site": "0065ec40",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065ec00",
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
      "0065ec18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065ec40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0065ec18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065ec40",
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

- 旧版 [`0065ebd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ebb8.md#insn-0065ebd8) · [`0065ec00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ebb8.md#insn-0065ec00) · [`0065ec14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ebb8.md#insn-0065ec14)
- 新版 `0065ec18`（命令位置の公開資料なし） · `0065ec40`（命令位置の公開資料なし） · `0065ec54`（命令位置の公開資料なし）

~~~diff
- 0065ebd8 ["INT_ADD", "register:40f0:8", ["const:65ebd8:8", "const:4:8"]]
- 0065ebd8 ["CALL", null, ["ram:47acb4:8"]]
+ 0065ec18 ["INT_ADD", "register:40f0:8", ["const:65ec18:8", "const:4:8"]]
+ 0065ec18 ["CALL", null, ["ram:47acf4:8"]]
- 0065ebd8 bytes 3770f897
+ 0065ec18 bytes 3770f897
- 0065ec00 ["INT_ADD", "register:40f0:8", ["const:65ec00:8", "const:4:8"]]
- 0065ec00 ["CALL", null, ["ram:47acb4:8"]]
+ 0065ec40 ["INT_ADD", "register:40f0:8", ["const:65ec40:8", "const:4:8"]]
+ 0065ec40 ["CALL", null, ["ram:47acf4:8"]]
- 0065ec00 bytes 2d70f897
+ 0065ec40 bytes 2d70f897
- 0065ec14 ["INT_ADD", "register:40f0:8", ["const:65ec14:8", "const:4:8"]]
- 0065ec14 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0065ec54 ["INT_ADD", "register:40f0:8", ["const:65ec54:8", "const:4:8"]]
+ 0065ec54 ["CALL", null, ["callee:0047cdd4:8"]]
- 0065ec14 bytes 6078f897
+ 0065ec54 bytes 6078f897
~~~


<a id="compare-887ac0a2cd40f39f4b0755e587ad711e"></a>

### [`0065ec5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ec5c.md) → [`0065ec9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ec9c.md) FUN_0065ec9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065eca8",
      "incomplete_value": false,
      "site": "0065ecb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065ec68",
      "incomplete_value": false,
      "site": "0065ec74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0065ecb4",
      "DATA",
      [
        "storage",
        "00c73fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065ecb4",
      "DATA",
      [
        "storage",
        "00c743c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ec5c.md#insn-0065ec64) · [`0065ec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ec5c.md#insn-0065ec68)
- 新版 `0065eca4`（命令位置の公開資料なし） · `0065eca8`（命令位置の公開資料なし）

~~~diff
- 0065ec64 ["COPY", "register:4050:8", ["const:c73000:8"]]
+ 0065eca4 ["COPY", "register:4050:8", ["const:c74000:8"]]
- 0065ec64 bytes aa3000b0
+ 0065eca4 bytes aa3000d0
- 0065ec68 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0065ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0065ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0065ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0065eca8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0065eca8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0065eca8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0065eca8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0065ec68 bytes 4a213f91
+ 0065eca8 bytes 4a210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c973cad3a7d190611d4b97654d438be9"></a>

### [`0065eca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eca0.md) → [`0065ece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ece0.md) FUN_0065ece0

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
      "definition_site": "0065ecf8",
      "incomplete_value": false,
      "site": "0065ed04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065ecb8",
      "incomplete_value": false,
      "site": "0065ecc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0065ed04",
      "DATA",
      [
        "storage",
        "00c73fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065ed04",
      "DATA",
      [
        "storage",
        "00c743c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ecb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eca0.md#insn-0065ecb4) · [`0065ecb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eca0.md#insn-0065ecb8) · [`0065ece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eca0.md#insn-0065ece8)
- 新版 `0065ecf4`（命令位置の公開資料なし） · `0065ecf8`（命令位置の公開資料なし） · `0065ed28`（命令位置の公開資料なし）

~~~diff
- 0065ecb4 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0065ecf4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065ecb4 bytes a83000b0
+ 0065ecf4 bytes a83000d0
- 0065ecb8 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0065ecb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065ecb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065ecb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065ecf8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0065ecf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065ecf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065ecf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065ecb8 bytes 08213f91
+ 0065ecf8 bytes 08210f91
- 0065ece8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0065ece8 ["INT_ADD", "register:40f0:8", ["const:65ece8:8", "const:4:8"]]
- 0065ece8 ["CALLIND", null, ["register:0:8"]]
+ 0065ed28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0065ed28 ["INT_ADD", "register:40f0:8", ["const:65ed28:8", "const:4:8"]]
+ 0065ed28 ["CALLIND", null, ["register:0:8"]]
- 0065ece8 bytes 00013fd6
+ 0065ed28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aecf64d478c036e2927a0f715998f75"></a>

### [`0065ecfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ecfc.md) → [`0065ed3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ed3c.md) FUN_0065ed3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065ed64",
      "incomplete_value": false,
      "site": "0065ed68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065ed24",
      "incomplete_value": false,
      "site": "0065ed28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0065ed68",
      "DATA",
      [
        "storage",
        "00c73fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065ed68",
      "DATA",
      [
        "storage",
        "00c743c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ed10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ecfc.md#insn-0065ed10) · [`0065ed20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ecfc.md#insn-0065ed20) · [`0065ed24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ecfc.md#insn-0065ed24)
- 新版 `0065ed50`（命令位置の公開資料なし） · `0065ed60`（命令位置の公開資料なし） · `0065ed64`（命令位置の公開資料なし）

~~~diff
- 0065ed10 ["INT_ADD", "register:40f0:8", ["const:65ed10:8", "const:4:8"]]
- 0065ed10 ["CALL", null, ["callee:00c57e90:8"]]
+ 0065ed50 ["INT_ADD", "register:40f0:8", ["const:65ed50:8", "const:4:8"]]
+ 0065ed50 ["CALL", null, ["callee:00c57e90:8"]]
- 0065ed10 bytes 60e31794
+ 0065ed50 bytes 50e41794
- 0065ed20 ["COPY", "register:4048:8", ["const:c73000:8"]]
+ 0065ed60 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0065ed20 bytes a93000b0
+ 0065ed60 bytes a93000d0
- 0065ed24 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0065ed24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065ed24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065ed24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065ed64 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0065ed64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065ed64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065ed64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065ed24 bytes 29213f91
+ 0065ed64 bytes 29210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f8e3230c1f8eb34c3cf78bdc19dd9f"></a>

### [`0065ed8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ed8c.md) → [`0065edcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065edcc.md) FUN_0065edcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0065ede8",
      "incomplete_value": false,
      "site": "0065edec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065eda8",
      "incomplete_value": false,
      "site": "0065edac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0065edec",
      "DATA",
      [
        "storage",
        "00c73fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065edec",
      "DATA",
      [
        "storage",
        "00c743c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065eda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ed8c.md#insn-0065eda4) · [`0065eda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ed8c.md#insn-0065eda8) · [`0065edd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ed8c.md#insn-0065edd0)
- 新版 `0065ede4`（命令位置の公開資料なし） · `0065ede8`（命令位置の公開資料なし） · `0065ee10`（命令位置の公開資料なし）

~~~diff
- 0065eda4 ["COPY", "register:4050:8", ["const:c73000:8"]]
+ 0065ede4 ["COPY", "register:4050:8", ["const:c74000:8"]]
- 0065eda4 bytes aa3000b0
+ 0065ede4 bytes aa3000d0
- 0065eda8 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0065eda8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0065eda8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0065eda8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0065ede8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0065ede8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0065ede8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0065ede8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0065eda8 bytes 4a213f91
+ 0065ede8 bytes 4a210f91
- 0065edd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0065edd0 ["INT_ADD", "register:40f0:8", ["const:65edd0:8", "const:4:8"]]
- 0065edd0 ["CALLIND", null, ["register:0:8"]]
+ 0065ee10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0065ee10 ["INT_ADD", "register:40f0:8", ["const:65ee10:8", "const:4:8"]]
+ 0065ee10 ["CALLIND", null, ["register:0:8"]]
- 0065edd0 bytes 20013fd6
+ 0065ee10 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35690ba5023dff5ecebb4abacd3547d1"></a>

### [`0065eec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eec4.md) → [`0065ef04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ef04.md) FUN_0065ef04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065ee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ee94.md) · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00658364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658364.md)
- 新版 呼出元 1件 [`0065eed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065eed4.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006583a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/006583a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "0065ef28",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065eee8",
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
      "site": "0065ef34",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065eef4",
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
      "0065ef28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065ef34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0065ef28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065ef34",
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

- 旧版 [`0065eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eec4.md#insn-0065eee8) · [`0065eef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eec4.md#insn-0065eef4) · [`0065ef18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065eec4.md#insn-0065ef18)
- 新版 `0065ef28`（命令位置の公開資料なし） · `0065ef34`（命令位置の公開資料なし） · `0065ef58`（命令位置の公開資料なし）

~~~diff
- 0065eee8 ["INT_ADD", "register:40f0:8", ["const:65eee8:8", "const:4:8"]]
- 0065eee8 ["CALL", null, ["ram:47acb4:8"]]
+ 0065ef28 ["INT_ADD", "register:40f0:8", ["const:65ef28:8", "const:4:8"]]
+ 0065ef28 ["CALL", null, ["ram:47acf4:8"]]
- 0065eee8 bytes 736ff897
+ 0065ef28 bytes 736ff897
- 0065eef4 ["INT_ADD", "register:40f0:8", ["const:65eef4:8", "const:4:8"]]
- 0065eef4 ["CALL", null, ["ram:47acb4:8"]]
+ 0065ef34 ["INT_ADD", "register:40f0:8", ["const:65ef34:8", "const:4:8"]]
+ 0065ef34 ["CALL", null, ["ram:47acf4:8"]]
- 0065eef4 bytes 706ff897
+ 0065ef34 bytes 706ff897
- 0065ef18 ["INT_ADD", "register:40f0:8", ["const:65ef18:8", "const:4:8"]]
- 0065ef18 ["CALL", null, ["callee:006583a4:8"]]
+ 0065ef58 ["INT_ADD", "register:40f0:8", ["const:65ef58:8", "const:4:8"]]
+ 0065ef58 ["CALL", null, ["callee:006583a4:8"]]
- 0065ef18 bytes 13e5ff97
+ 0065ef58 bytes 13e5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1548e9b761fdd89b8f1e916d11c725d3"></a>

### [`0065ef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ef4c.md) → [`0065ef8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065ef8c.md) FUN_0065ef8c

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
      "definition_site": "0065efa0",
      "incomplete_value": false,
      "site": "0065efa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065ef60",
      "incomplete_value": false,
      "site": "0065ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0065efa4",
      "DATA",
      [
        "storage",
        "00c74048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065efa4",
      "DATA",
      [
        "storage",
        "00c74448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ef58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ef4c.md#insn-0065ef58) · [`0065ef60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ef4c.md#insn-0065ef60)
- 新版 `0065ef98`（命令位置の公開資料なし） · `0065efa0`（命令位置の公開資料なし）

~~~diff
- 0065ef58 ["INT_ADD", "register:40f0:8", ["const:65ef58:8", "const:4:8"]]
- 0065ef58 ["CALL", null, ["callee:00c57e90:8"]]
+ 0065ef98 ["INT_ADD", "register:40f0:8", ["const:65ef98:8", "const:4:8"]]
+ 0065ef98 ["CALL", null, ["callee:00c57e90:8"]]
- 0065ef58 bytes cee21794
+ 0065ef98 bytes bee31794
- 0065ef60 ["COPY", "tmp:0:8", ["const:48:8"]]
- 0065ef60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065ef60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065ef60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065efa0 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 0065efa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065efa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065efa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065ef60 bytes 08210191
+ 0065efa0 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49497efda4e1728a8548e398c0de68c6"></a>

### [`0065efb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065efb8.md) → [`0065eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065eff8.md) FUN_0065eff8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065ef88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ef88.md) · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 1件 [`0065efc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065e/0065efc8.md) · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "0065f018",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065efd8",
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
      "site": "0065f024",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065efe4",
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
      "0065f018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0065f048",
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
      "0065f018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0065f048",
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

- 旧版 [`0065efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065efb8.md#insn-0065efd8) · [`0065efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065efb8.md#insn-0065efe4) · [`0065f018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065efb8.md#insn-0065f018)
- 新版 `0065f018`（命令位置の公開資料なし） · `0065f024`（命令位置の公開資料なし） · `0065f058`（命令位置の公開資料なし）

~~~diff
- 0065efd8 ["INT_ADD", "register:40f0:8", ["const:65efd8:8", "const:4:8"]]
- 0065efd8 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f018 ["INT_ADD", "register:40f0:8", ["const:65f018:8", "const:4:8"]]
+ 0065f018 ["CALL", null, ["ram:47acf4:8"]]
- 0065efd8 bytes 376ff897
+ 0065f018 bytes 376ff897
- 0065efe4 ["INT_ADD", "register:40f0:8", ["const:65efe4:8", "const:4:8"]]
- 0065efe4 ["CALL", null, ["ram:47acb4:8"]]
+ 0065f024 ["INT_ADD", "register:40f0:8", ["const:65f024:8", "const:4:8"]]
+ 0065f024 ["CALL", null, ["ram:47acf4:8"]]
- 0065efe4 bytes 346ff897
+ 0065f024 bytes 346ff897
- 0065f018 ["INT_ADD", "register:40f0:8", ["const:65f018:8", "const:4:8"]]
- 0065f018 ["CALL", null, ["callee:008514f8:8"]]
+ 0065f058 ["INT_ADD", "register:40f0:8", ["const:65f058:8", "const:4:8"]]
+ 0065f058 ["CALL", null, ["callee:008514f8:8"]]
- 0065f018 bytes 28c90794
+ 0065f058 bytes 28c90794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

