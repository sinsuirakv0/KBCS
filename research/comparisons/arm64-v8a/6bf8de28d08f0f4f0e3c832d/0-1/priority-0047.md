# v16.0.0 → v16.0.1 · 最優先の変更候補 (47)

[一覧の目次](README.md)

<a id="compare-ed6e8c7151715b2bfe49c949bd7c390c"></a>

### [`0088af24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af24.md) → [`0088af64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af64.md) FUN_0088af64

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
      "definition_site": "0088af68",
      "incomplete_value": false,
      "site": "0088af6c",
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
      "definition_site": "0088af28",
      "incomplete_value": false,
      "site": "0088af2c",
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
      "0088af6c",
      "DATA",
      [
        "storage",
        "00c812b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088af6c",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088af28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af24.md#insn-0088af28)
- 新版 [`0088af68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af64.md#insn-0088af68)

~~~diff
- 0088af28 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0088af28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088af28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088af28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088af68 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0088af68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088af28 bytes 08c10a91
+ 0088af68 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3325005bf7cf427891cf96e5e019504"></a>

### [`0088af34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af34.md) → [`0088af74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md) FUN_0088af74

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
      "definition_site": "0088af84",
      "incomplete_value": false,
      "site": "0088af8c",
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
      "definition_site": "0088af44",
      "incomplete_value": false,
      "site": "0088af4c",
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
      "0088af8c",
      "DATA",
      [
        "storage",
        "00c812b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088af8c",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088af44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af34.md#insn-0088af44) · [`0088af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af34.md#insn-0088af50)
- 新版 [`0088af84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md#insn-0088af84) · [`0088af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md#insn-0088af90)

~~~diff
- 0088af44 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0088af44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088af44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088af44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088af84 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0088af84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088af44 bytes 08c10a91
+ 0088af84 bytes 08c11a91
- 0088af50 ["INT_ADD", "register:40f0:8", ["const:88af50:8", "const:4:8"]]
- 0088af50 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088af90 ["INT_ADD", "register:40f0:8", ["const:88af90:8", "const:4:8"]]
+ 0088af90 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088af50 bytes d4320f94
+ 0088af90 bytes c4330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4812939cedbde997a305475574d8edf3"></a>

### [`0088af70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af70.md) → [`0088afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md) FUN_0088afb0

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
      "definition_site": "0088afe8",
      "incomplete_value": false,
      "site": "0088aff4",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088afa8",
      "incomplete_value": false,
      "site": "0088afb4",
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
            "const:300:8"
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
      "definition_site": "0088b008",
      "incomplete_value": false,
      "site": "0088b00c",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088afc8",
      "incomplete_value": false,
      "site": "0088afcc",
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
            "const:cb8:8"
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
      "definition_site": "0088b028",
      "incomplete_value": false,
      "site": "0088b030",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088afe8",
      "incomplete_value": false,
      "site": "0088aff0",
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
            "const:a90:8"
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
      "0088aff4",
      "DATA",
      [
        "storage",
        "00c81300",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b00c",
      "DATA",
      [
        "storage",
        "00c80cb8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b028",
      "PARAM",
      [
        "storage",
        "002aba90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088aff4",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b00c",
      "DATA",
      [
        "storage",
        "00c810b8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b028",
      "PARAM",
      [
        "storage",
        "002abad0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088aff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af70.md#insn-0088aff0) · [`0088b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af70.md#insn-0088b000) · [`0088af94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af70.md#insn-0088af94)
- 新版 [`0088b030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088b030) · [`0088b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088b040) · [`0088afd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088afd4)

~~~diff
- 0088aff0 ["INT_ADD", "register:40f0:8", ["const:88aff0:8", "const:4:8"]]
- 0088aff0 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b030 ["INT_ADD", "register:40f0:8", ["const:88b030:8", "const:4:8"]]
+ 0088b030 ["CALL", null, ["callee:00c58190:8"]]
- 0088aff0 bytes 68330f94
+ 0088b030 bytes 58340f94
- 0088b000 ["INT_ADD", "register:40f0:8", ["const:88b000:8", "const:4:8"]]
- 0088b000 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b040 ["INT_ADD", "register:40f0:8", ["const:88b040:8", "const:4:8"]]
+ 0088b040 ["CALL", null, ["callee:00c58190:8"]]
- 0088b000 bytes 64330f94
+ 0088b040 bytes 54340f94
- 0088af94 ["INT_ADD", "register:40f0:8", ["const:88af94:8", "const:4:8"]]
- 0088af94 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088afd4 ["INT_ADD", "register:40f0:8", ["const:88afd4:8", "const:4:8"]]
+ 0088afd4 ["CALL", null, ["callee:00c57e90:8"]]
- 0088af94 bytes bf320f94
+ 0088afd4 bytes af330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-784dae80a193204aefa181f0f729d19f"></a>

### [`0088b048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b048.md) → [`0088b088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b088.md) FUN_0088b088

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
      "definition_site": "0088b08c",
      "incomplete_value": false,
      "site": "0088b090",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b04c",
      "incomplete_value": false,
      "site": "0088b050",
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
            "const:300:8"
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
      "0088b090",
      "DATA",
      [
        "storage",
        "00c81300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b090",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b048.md#insn-0088b04c)
- 新版 [`0088b08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b088.md#insn-0088b08c)

~~~diff
- 0088b04c ["COPY", "tmp:0:8", ["const:300:8"]]
- 0088b04c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b04c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b04c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b08c ["COPY", "tmp:0:8", ["const:700:8"]]
+ 0088b08c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b08c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b08c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b04c bytes 08010c91
+ 0088b08c bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0817a5278d4833a056b15c520c171923"></a>

### [`0088b058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b058.md) → [`0088b098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md) FUN_0088b098

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
      "definition_site": "0088b0a8",
      "incomplete_value": false,
      "site": "0088b0b0",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b068",
      "incomplete_value": false,
      "site": "0088b070",
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
            "const:300:8"
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
      "0088b0b0",
      "DATA",
      [
        "storage",
        "00c81300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b0b0",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b058.md#insn-0088b068) · [`0088b074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b058.md#insn-0088b074)
- 新版 [`0088b0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md#insn-0088b0a8) · [`0088b0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md#insn-0088b0b4)

~~~diff
- 0088b068 ["COPY", "tmp:0:8", ["const:300:8"]]
- 0088b068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b0a8 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 0088b0a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b0a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b0a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b068 bytes 08010c91
+ 0088b0a8 bytes 08011c91
- 0088b074 ["INT_ADD", "register:40f0:8", ["const:88b074:8", "const:4:8"]]
- 0088b074 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088b0b4 ["INT_ADD", "register:40f0:8", ["const:88b0b4:8", "const:4:8"]]
+ 0088b0b4 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088b074 bytes 8b320f94
+ 0088b0b4 bytes 7b330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3598f713099f818c92907fadf493639e"></a>

### [`0088b094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b094.md) → [`0088b0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md) FUN_0088b0d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b10c",
      "incomplete_value": false,
      "site": "0088b118",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b0cc",
      "incomplete_value": false,
      "site": "0088b0d8",
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
            "const:350:8"
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
      "definition_site": "0088b12c",
      "incomplete_value": false,
      "site": "0088b130",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b0ec",
      "incomplete_value": false,
      "site": "0088b0f0",
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
            "const:cf8:8"
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
      "definition_site": "0088b148",
      "incomplete_value": false,
      "site": "0088b150",
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
            "const:581:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b108",
      "incomplete_value": false,
      "site": "0088b110",
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
            "const:541:8"
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
      "0088b118",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b130",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b148",
      "PARAM",
      [
        "storage",
        "002b9541",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b118",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b130",
      "DATA",
      [
        "storage",
        "00c810f8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b148",
      "PARAM",
      [
        "storage",
        "002b9581",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b094.md#insn-0088b0e0) · [`0088b110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b094.md#insn-0088b110) · [`0088b118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b094.md#insn-0088b118)
- 新版 [`0088b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b120) · [`0088b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b150) · [`0088b158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b158)

~~~diff
- 0088b0e0 ["INT_ADD", "register:40f0:8", ["const:88b0e0:8", "const:4:8"]]
- 0088b0e0 ["CALL", null, ["callee:00887478:8"]]
+ 0088b120 ["INT_ADD", "register:40f0:8", ["const:88b120:8", "const:4:8"]]
+ 0088b120 ["CALL", null, ["callee:00887478:8"]]
- 0088b0e0 bytes d6f0ff97
+ 0088b120 bytes d6f0ff97
- 0088b110 ["INT_ADD", "register:40f0:8", ["const:88b110:8", "const:4:8"]]
- 0088b110 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b150 ["INT_ADD", "register:40f0:8", ["const:88b150:8", "const:4:8"]]
+ 0088b150 ["CALL", null, ["callee:00c58190:8"]]
- 0088b110 bytes 20330f94
+ 0088b150 bytes 10340f94
- 0088b118 ["COPY", "tmp:0:8", ["const:883:8"]]
- 0088b118 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0088b118 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0088b118 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088b158 ["COPY", "tmp:0:8", ["const:8c3:8"]]
+ 0088b158 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088b158 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088b158 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0088b118 bytes 210c2291
+ 0088b158 bytes 210c2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2896242c0723633384fec17fecfce3e"></a>

### [`0088b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b168.md) → [`0088b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1a8.md) FUN_0088b1a8

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
      "definition_site": "0088b1ac",
      "incomplete_value": false,
      "site": "0088b1b0",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b16c",
      "incomplete_value": false,
      "site": "0088b170",
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
            "const:350:8"
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
      "0088b1b0",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b1b0",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b168.md#insn-0088b16c)
- 新版 [`0088b1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1a8.md#insn-0088b1ac)

~~~diff
- 0088b16c ["COPY", "tmp:0:8", ["const:350:8"]]
- 0088b16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b1ac ["COPY", "tmp:0:8", ["const:750:8"]]
+ 0088b1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b16c bytes 08410d91
+ 0088b1ac bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e4998fa1d791596fb242e90ec9cff1"></a>

### [`0088b178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b178.md) → [`0088b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md) FUN_0088b1b8

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
      "definition_site": "0088b1c8",
      "incomplete_value": false,
      "site": "0088b1d0",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b188",
      "incomplete_value": false,
      "site": "0088b190",
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
            "const:350:8"
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
      "0088b1d0",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b1d0",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b178.md#insn-0088b188) · [`0088b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b178.md#insn-0088b194)
- 新版 [`0088b1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md#insn-0088b1c8) · [`0088b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md#insn-0088b1d4)

~~~diff
- 0088b188 ["COPY", "tmp:0:8", ["const:350:8"]]
- 0088b188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b1c8 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 0088b1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b188 bytes 08410d91
+ 0088b1c8 bytes 08411d91
- 0088b194 ["INT_ADD", "register:40f0:8", ["const:88b194:8", "const:4:8"]]
- 0088b194 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088b1d4 ["INT_ADD", "register:40f0:8", ["const:88b1d4:8", "const:4:8"]]
+ 0088b1d4 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088b194 bytes 43320f94
+ 0088b1d4 bytes 33330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc72a179701e0011db6b5b29970a887"></a>

### [`0088b1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b1b4.md) → [`0088b1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md) FUN_0088b1f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b22c",
      "incomplete_value": false,
      "site": "0088b238",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b1ec",
      "incomplete_value": false,
      "site": "0088b1f8",
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
            "const:3a0:8"
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
      "definition_site": "0088b24c",
      "incomplete_value": false,
      "site": "0088b250",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b20c",
      "incomplete_value": false,
      "site": "0088b210",
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
            "const:cd8:8"
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
      "definition_site": "0088b268",
      "incomplete_value": false,
      "site": "0088b270",
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
            "const:6f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b228",
      "incomplete_value": false,
      "site": "0088b230",
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
            "const:6b7:8"
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
      "0088b238",
      "DATA",
      [
        "storage",
        "00c813a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b250",
      "DATA",
      [
        "storage",
        "00c80cd8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b268",
      "PARAM",
      [
        "storage",
        "002b86b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b238",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b250",
      "DATA",
      [
        "storage",
        "00c810d8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b268",
      "PARAM",
      [
        "storage",
        "002b86f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b1b4.md#insn-0088b200) · [`0088b230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b1b4.md#insn-0088b230) · [`0088b238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b1b4.md#insn-0088b238)
- 新版 [`0088b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b240) · [`0088b270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b270) · [`0088b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b278)

~~~diff
- 0088b200 ["INT_ADD", "register:40f0:8", ["const:88b200:8", "const:4:8"]]
- 0088b200 ["CALL", null, ["callee:00887478:8"]]
+ 0088b240 ["INT_ADD", "register:40f0:8", ["const:88b240:8", "const:4:8"]]
+ 0088b240 ["CALL", null, ["callee:00887478:8"]]
- 0088b200 bytes 8ef0ff97
+ 0088b240 bytes 8ef0ff97
- 0088b230 ["INT_ADD", "register:40f0:8", ["const:88b230:8", "const:4:8"]]
- 0088b230 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b270 ["INT_ADD", "register:40f0:8", ["const:88b270:8", "const:4:8"]]
+ 0088b270 ["CALL", null, ["callee:00c58190:8"]]
- 0088b230 bytes d8320f94
+ 0088b270 bytes c8330f94
- 0088b238 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0088b238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0088b238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0088b238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088b278 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0088b278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088b278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088b278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0088b238 bytes 21c00591
+ 0088b278 bytes 21c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc9b17c8b4d45038587b8346bf0a661"></a>

### [`0088b288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b288.md) → [`0088b2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2c8.md) FUN_0088b2c8

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
      "definition_site": "0088b2cc",
      "incomplete_value": false,
      "site": "0088b2d0",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b28c",
      "incomplete_value": false,
      "site": "0088b290",
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
            "const:3a0:8"
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
      "0088b2d0",
      "DATA",
      [
        "storage",
        "00c813a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b2d0",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b288.md#insn-0088b28c)
- 新版 [`0088b2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2c8.md#insn-0088b2cc)

~~~diff
- 0088b28c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0088b28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b2cc ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0088b2cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b2cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b2cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b28c bytes 08810e91
+ 0088b2cc bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd0931ec905a91e4858a18161fca936e"></a>

### [`0088b298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b298.md) → [`0088b2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md) FUN_0088b2d8

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
      "definition_site": "0088b2e8",
      "incomplete_value": false,
      "site": "0088b2f0",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b2a8",
      "incomplete_value": false,
      "site": "0088b2b0",
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
            "const:3a0:8"
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
      "0088b2f0",
      "DATA",
      [
        "storage",
        "00c813a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b2f0",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b298.md#insn-0088b2a8) · [`0088b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b298.md#insn-0088b2b4)
- 新版 [`0088b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md#insn-0088b2e8) · [`0088b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md#insn-0088b2f4)

~~~diff
- 0088b2a8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0088b2a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b2e8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0088b2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b2a8 bytes 08810e91
+ 0088b2e8 bytes 08811e91
- 0088b2b4 ["INT_ADD", "register:40f0:8", ["const:88b2b4:8", "const:4:8"]]
- 0088b2b4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088b2f4 ["INT_ADD", "register:40f0:8", ["const:88b2f4:8", "const:4:8"]]
+ 0088b2f4 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088b2b4 bytes fb310f94
+ 0088b2f4 bytes eb320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217302a07afbce4a6ddeae3a9599dee1"></a>

### [`0088b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md) → [`0088b314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md) FUN_0088b314

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0088a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088a8a4.md) [`0088ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088ae40.md) [`0088af64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088a/0088af64.md) [`0088b088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b088.md) [`0088b1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b1a8.md) · 呼出先 3件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 7件 [`0088a8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8e4.md) [`0088ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae80.md) [`0088afa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afa4.md) [`0088b0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0c8.md) [`0088b1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1e8.md) · 呼出先 3件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b338",
      "incomplete_value": false,
      "site": "0088b33c",
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
      "definition_site": "0088b2f8",
      "incomplete_value": false,
      "site": "0088b2fc",
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
      "0088b33c",
      "DATA",
      [
        "storage",
        "00c80c38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088b33c",
      "DATA",
      [
        "storage",
        "00c81038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md#insn-0088b2f4) · [`0088b2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md#insn-0088b2f8) · [`0088b30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md#insn-0088b30c)
- 新版 [`0088b334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b334) · [`0088b338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b338) · [`0088b34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b34c)

~~~diff
- 0088b2f4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088b334 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0088b2f4 bytes a81f00b0
+ 0088b334 bytes a81f00d0
- 0088b2f8 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0088b2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b338 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0088b338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b2f8 bytes 08e13091
+ 0088b338 bytes 08e10091
- 0088b30c ["INT_ADD", "register:40f0:8", ["const:88b30c:8", "const:4:8"]]
- 0088b30c ["CALL", null, ["callee:00597ecc:8"]]
+ 0088b34c ["INT_ADD", "register:40f0:8", ["const:88b34c:8", "const:4:8"]]
+ 0088b34c ["CALL", null, ["callee:00597ecc:8"]]
- 0088b30c bytes e032f497
+ 0088b34c bytes e032f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fedcb2524a173588e439857ee9df97"></a>

### [`0088b458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b458.md) → [`0088b498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md) FUN_0088b498

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b4e4",
      "incomplete_value": false,
      "site": "0088b4f0",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b4a4",
      "incomplete_value": false,
      "site": "0088b4b0",
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
            "const:3f0:8"
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
      "definition_site": "0088b500",
      "incomplete_value": false,
      "site": "0088b508",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b4c0",
      "incomplete_value": false,
      "site": "0088b4c8",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088b524",
      "incomplete_value": false,
      "site": "0088b52c",
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
            "const:704:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b4e4",
      "incomplete_value": false,
      "site": "0088b4ec",
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
            "const:6c4:8"
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
      "0088b4f0",
      "DATA",
      [
        "storage",
        "00c813f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b508",
      "DATA",
      [
        "storage",
        "00c80d18",
        null,
        "pointer"
      ]
    ],
    [
      "0088b524",
      "PARAM",
      [
        "storage",
        "002b86c4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b4f0",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b508",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ],
    [
      "0088b524",
      "PARAM",
      [
        "storage",
        "002b8704",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b458.md#insn-0088b488) · [`0088b4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b458.md#insn-0088b4bc) · [`0088b4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b458.md#insn-0088b4ec)
- 新版 [`0088b4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b4c8) · [`0088b4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b4fc) · [`0088b52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b52c)

~~~diff
- 0088b488 ["INT_ADD", "register:40f0:8", ["const:88b488:8", "const:4:8"]]
- 0088b488 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088b4c8 ["INT_ADD", "register:40f0:8", ["const:88b4c8:8", "const:4:8"]]
+ 0088b4c8 ["CALL", null, ["callee:00c57e90:8"]]
- 0088b488 bytes 82310f94
+ 0088b4c8 bytes 72320f94
- 0088b4bc ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088b4fc ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0088b4bc bytes a81f00b0
+ 0088b4fc bytes a81f00d0
- 0088b4ec ["INT_ADD", "register:40f0:8", ["const:88b4ec:8", "const:4:8"]]
- 0088b4ec ["CALL", null, ["callee:00c58190:8"]]
+ 0088b52c ["INT_ADD", "register:40f0:8", ["const:88b52c:8", "const:4:8"]]
+ 0088b52c ["CALL", null, ["callee:00c58190:8"]]
- 0088b4ec bytes 29320f94
+ 0088b52c bytes 19330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f03c81b20815a76b7c6f8d465e3af7"></a>

### [`0088b548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b548.md) → [`0088b588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b588.md) FUN_0088b588

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
      "definition_site": "0088b58c",
      "incomplete_value": false,
      "site": "0088b590",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b54c",
      "incomplete_value": false,
      "site": "0088b550",
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
      "0088b590",
      "DATA",
      [
        "storage",
        "00c813f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b590",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b548.md#insn-0088b54c)
- 新版 [`0088b58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b588.md#insn-0088b58c)

~~~diff
- 0088b54c ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 0088b54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b58c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 0088b58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b54c bytes 08c10f91
+ 0088b58c bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9497649826839bd0dd83bc0ecb7bb6b3"></a>

### [`0088b558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b558.md) → [`0088b598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md) FUN_0088b598

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
      "definition_site": "0088b5a8",
      "incomplete_value": false,
      "site": "0088b5b0",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b568",
      "incomplete_value": false,
      "site": "0088b570",
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
      "0088b5b0",
      "DATA",
      [
        "storage",
        "00c813f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b5b0",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b558.md#insn-0088b568) · [`0088b574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b558.md#insn-0088b574)
- 新版 [`0088b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md#insn-0088b5a8) · [`0088b5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md#insn-0088b5b4)

~~~diff
- 0088b568 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 0088b568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b5a8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 0088b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b568 bytes 08c10f91
+ 0088b5a8 bytes 08c11f91
- 0088b574 ["INT_ADD", "register:40f0:8", ["const:88b574:8", "const:4:8"]]
- 0088b574 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0088b5b4 ["INT_ADD", "register:40f0:8", ["const:88b5b4:8", "const:4:8"]]
+ 0088b5b4 ["CALL", null, ["callee:00c57ea0:8"]]
- 0088b574 bytes 4b310f94
+ 0088b5b4 bytes 3b320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fde602fbbca43c52041df8fd8f210ee"></a>

### [`0088b588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b588.md) → [`0088b5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md) FUN_0088b5c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`0088b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b2d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`0088b314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "0088b5f0",
      "incomplete_value": false,
      "site": "0088b5f0",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b5b0",
      "incomplete_value": false,
      "site": "0088b5b0",
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
            "const:d18:8"
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
      "0088b5f0",
      "DATA",
      [
        "storage",
        "00c80d18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088b5f0",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b588.md#insn-0088b5a0) · [`0088b5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b588.md#insn-0088b5a4) · [`0088b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b588.md#insn-0088b5c0)
- 新版 [`0088b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b5e0) · [`0088b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b5e4) · [`0088b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b600)

~~~diff
- 0088b5a0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0088b5e0 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0088b5a0 bytes a91f00b0
+ 0088b5e0 bytes a91f00d0
- 0088b5a4 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0088b5a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b5a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b5a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088b5e4 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0088b5e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b5e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b5e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b5a4 bytes 29613491
+ 0088b5e4 bytes 29610491
- 0088b5c0 ["INT_ADD", "register:40f0:8", ["const:88b5c0:8", "const:4:8"]]
- 0088b5c0 ["CALL", null, ["callee:00597ecc:8"]]
+ 0088b600 ["INT_ADD", "register:40f0:8", ["const:88b600:8", "const:4:8"]]
+ 0088b600 ["CALL", null, ["callee:00597ecc:8"]]
- 0088b5c0 bytes 3332f497
+ 0088b600 bytes 3332f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e18d75ab446421fd61d4e9c6af14b4"></a>

### [`0088b608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b608.md) → [`0088b648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md) FUN_0088b648

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
      "definition_site": "0088b680",
      "incomplete_value": false,
      "site": "0088b68c",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b640",
      "incomplete_value": false,
      "site": "0088b64c",
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
            "const:350:8"
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
      "definition_site": "0088b6a0",
      "incomplete_value": false,
      "site": "0088b6a4",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b660",
      "incomplete_value": false,
      "site": "0088b664",
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
            "const:cf8:8"
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
      "definition_site": "0088b6c0",
      "incomplete_value": false,
      "site": "0088b6c8",
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
            "const:581:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b680",
      "incomplete_value": false,
      "site": "0088b688",
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
            "const:541:8"
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
      "0088b68c",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b6a4",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b6c0",
      "PARAM",
      [
        "storage",
        "002b9541",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b68c",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b6a4",
      "DATA",
      [
        "storage",
        "00c810f8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b6c0",
      "PARAM",
      [
        "storage",
        "002b9581",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b608.md#insn-0088b688) · [`0088b698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b608.md#insn-0088b698) · [`0088b62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b608.md#insn-0088b62c)
- 新版 [`0088b6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b6c8) · [`0088b6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b6d8) · [`0088b66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b66c)

~~~diff
- 0088b688 ["INT_ADD", "register:40f0:8", ["const:88b688:8", "const:4:8"]]
- 0088b688 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b6c8 ["INT_ADD", "register:40f0:8", ["const:88b6c8:8", "const:4:8"]]
+ 0088b6c8 ["CALL", null, ["callee:00c58190:8"]]
- 0088b688 bytes c2310f94
+ 0088b6c8 bytes b2320f94
- 0088b698 ["INT_ADD", "register:40f0:8", ["const:88b698:8", "const:4:8"]]
- 0088b698 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b6d8 ["INT_ADD", "register:40f0:8", ["const:88b6d8:8", "const:4:8"]]
+ 0088b6d8 ["CALL", null, ["callee:00c58190:8"]]
- 0088b698 bytes be310f94
+ 0088b6d8 bytes ae320f94
- 0088b62c ["INT_ADD", "register:40f0:8", ["const:88b62c:8", "const:4:8"]]
- 0088b62c ["CALL", null, ["callee:00c57e90:8"]]
+ 0088b66c ["INT_ADD", "register:40f0:8", ["const:88b66c:8", "const:4:8"]]
+ 0088b66c ["CALL", null, ["callee:00c57e90:8"]]
- 0088b62c bytes 19310f94
+ 0088b66c bytes 09320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7179c766f0c01520adc898ad440991d"></a>

### [`0088b6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b6e0.md) → [`0088b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md) FUN_0088b720

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
      "definition_site": "0088b758",
      "incomplete_value": false,
      "site": "0088b764",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b718",
      "incomplete_value": false,
      "site": "0088b724",
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
            "const:3a0:8"
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
      "definition_site": "0088b778",
      "incomplete_value": false,
      "site": "0088b77c",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b738",
      "incomplete_value": false,
      "site": "0088b73c",
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
            "const:cd8:8"
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
      "definition_site": "0088b798",
      "incomplete_value": false,
      "site": "0088b7a0",
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
            "const:6f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b758",
      "incomplete_value": false,
      "site": "0088b760",
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
            "const:6b7:8"
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
      "0088b764",
      "DATA",
      [
        "storage",
        "00c813a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b77c",
      "DATA",
      [
        "storage",
        "00c80cd8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b798",
      "PARAM",
      [
        "storage",
        "002b86b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b764",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b77c",
      "DATA",
      [
        "storage",
        "00c810d8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b798",
      "PARAM",
      [
        "storage",
        "002b86f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b6e0.md#insn-0088b760) · [`0088b770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b6e0.md#insn-0088b770) · [`0088b704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b6e0.md#insn-0088b704)
- 新版 [`0088b7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b7a0) · [`0088b7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b7b0) · [`0088b744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b744)

~~~diff
- 0088b760 ["INT_ADD", "register:40f0:8", ["const:88b760:8", "const:4:8"]]
- 0088b760 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b7a0 ["INT_ADD", "register:40f0:8", ["const:88b7a0:8", "const:4:8"]]
+ 0088b7a0 ["CALL", null, ["callee:00c58190:8"]]
- 0088b760 bytes 8c310f94
+ 0088b7a0 bytes 7c320f94
- 0088b770 ["INT_ADD", "register:40f0:8", ["const:88b770:8", "const:4:8"]]
- 0088b770 ["CALL", null, ["callee:00c58190:8"]]
+ 0088b7b0 ["INT_ADD", "register:40f0:8", ["const:88b7b0:8", "const:4:8"]]
+ 0088b7b0 ["CALL", null, ["callee:00c58190:8"]]
- 0088b770 bytes 88310f94
+ 0088b7b0 bytes 78320f94
- 0088b704 ["INT_ADD", "register:40f0:8", ["const:88b704:8", "const:4:8"]]
- 0088b704 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088b744 ["INT_ADD", "register:40f0:8", ["const:88b744:8", "const:4:8"]]
+ 0088b744 ["CALL", null, ["callee:00c57e90:8"]]
- 0088b704 bytes e3300f94
+ 0088b744 bytes d3310f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c96b4784382cbcf1267698a78273918"></a>

### [`0088b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b7b8.md) → [`0088b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md) FUN_0088b7f8

採用 · 移動量 `+0x40` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00887898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887898.md) · 呼出先 3件 [`00887438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00887/00887438.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b844",
      "incomplete_value": false,
      "site": "0088b850",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b804",
      "incomplete_value": false,
      "site": "0088b810",
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
            "const:3f0:8"
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
      "definition_site": "0088b860",
      "incomplete_value": false,
      "site": "0088b868",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b820",
      "incomplete_value": false,
      "site": "0088b828",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088b884",
      "incomplete_value": false,
      "site": "0088b88c",
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
            "const:704:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b844",
      "incomplete_value": false,
      "site": "0088b84c",
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
            "const:6c4:8"
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
      "0088b850",
      "DATA",
      [
        "storage",
        "00c813f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b868",
      "DATA",
      [
        "storage",
        "00c80d18",
        null,
        "pointer"
      ]
    ],
    [
      "0088b884",
      "PARAM",
      [
        "storage",
        "002b86c4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b850",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b868",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ],
    [
      "0088b884",
      "PARAM",
      [
        "storage",
        "002b8704",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b7b8.md#insn-0088b7e8) · [`0088b81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b7b8.md#insn-0088b81c) · [`0088b84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b7b8.md#insn-0088b84c)
- 新版 [`0088b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b828) · [`0088b85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b85c) · [`0088b88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b88c)

~~~diff
- 0088b7e8 ["INT_ADD", "register:40f0:8", ["const:88b7e8:8", "const:4:8"]]
- 0088b7e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088b828 ["INT_ADD", "register:40f0:8", ["const:88b828:8", "const:4:8"]]
+ 0088b828 ["CALL", null, ["callee:00c57e90:8"]]
- 0088b7e8 bytes aa300f94
+ 0088b828 bytes 9a310f94
- 0088b81c ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0088b85c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0088b81c bytes a81f00b0
+ 0088b85c bytes a81f00d0
- 0088b84c ["INT_ADD", "register:40f0:8", ["const:88b84c:8", "const:4:8"]]
- 0088b84c ["CALL", null, ["callee:00c58190:8"]]
+ 0088b88c ["INT_ADD", "register:40f0:8", ["const:88b88c:8", "const:4:8"]]
+ 0088b88c ["CALL", null, ["callee:00c58190:8"]]
- 0088b84c bytes 51310f94
+ 0088b88c bytes 41320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94454db5083705e2ffe31b12c59527b7"></a>

### [`0088b8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8b0.md) → [`0088b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md) FUN_0088b8f0

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
      "definition_site": "0088b914",
      "incomplete_value": false,
      "site": "0088b914",
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
      "definition_site": "0088b8d4",
      "incomplete_value": false,
      "site": "0088b8d4",
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
      "0088b914",
      "DATA",
      [
        "storage",
        "00c81440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b914",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8b0.md#insn-0088b8c4) · [`0088b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8b0.md#insn-0088b8d0)
- 新版 [`0088b904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md#insn-0088b904) · [`0088b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md#insn-0088b910)

~~~diff
- 0088b8c4 ["INT_ADD", "register:40f0:8", ["const:88b8c4:8", "const:4:8"]]
- 0088b8c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088b904 ["INT_ADD", "register:40f0:8", ["const:88b904:8", "const:4:8"]]
+ 0088b904 ["CALL", null, ["callee:00c57e90:8"]]
- 0088b8c4 bytes 73300f94
+ 0088b904 bytes 63310f94
- 0088b8d0 ["COPY", "tmp:0:8", ["const:440:8"]]
- 0088b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b910 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0088b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b8d0 bytes 08011191
+ 0088b910 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad09e6334eff16006a3e49f1927a8cc4"></a>

### [`0088b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8e4.md) → [`0088b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b924.md) FUN_0088b924

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
      "definition_site": "0088b930",
      "incomplete_value": false,
      "site": "0088b930",
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
      "definition_site": "0088b8f0",
      "incomplete_value": false,
      "site": "0088b8f0",
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
      "0088b930",
      "DATA",
      [
        "storage",
        "00c81440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b930",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b8e4.md#insn-0088b8ec)
- 新版 [`0088b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b924.md#insn-0088b92c)

~~~diff
- 0088b8ec ["COPY", "tmp:0:8", ["const:440:8"]]
- 0088b8ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b8ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b8ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088b92c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0088b92c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b92c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b92c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b8ec bytes 29011191
+ 0088b92c bytes 29012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3815026bf78062ee09f861ac86cbb34"></a>

### [`0088b9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b9f4.md) → [`0088ba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba34.md) FUN_0088ba34

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
      "definition_site": "0088ba40",
      "incomplete_value": false,
      "site": "0088ba40",
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
      "definition_site": "0088ba00",
      "incomplete_value": false,
      "site": "0088ba00",
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
      "0088ba40",
      "DATA",
      [
        "storage",
        "00c814c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ba40",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088b9f4.md#insn-0088b9fc)
- 新版 [`0088ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba34.md#insn-0088ba3c)

~~~diff
- 0088b9fc ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0088b9fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b9fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b9fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088ba3c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0088ba3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ba3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ba3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b9fc bytes 29011391
+ 0088ba3c bytes 29012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3881771ce5c13949cbffbad5e0ec7af"></a>

### [`0088baec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088baec.md) → [`0088bb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb2c.md) FUN_0088bb2c

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
      "definition_site": "0088bb38",
      "incomplete_value": false,
      "site": "0088bb38",
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
      "definition_site": "0088baf8",
      "incomplete_value": false,
      "site": "0088baf8",
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
      "0088bb38",
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
      "0088bb38",
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

- 旧版 [`0088baf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088baec.md#insn-0088baf4)
- 新版 [`0088bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb2c.md#insn-0088bb34)

~~~diff
- 0088baf4 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0088baf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088baf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088baf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088bb34 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0088bb34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bb34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bb34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088baf4 bytes 29011591
+ 0088bb34 bytes 29012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f2d5aafa5456f34aa73c19b2c72807f"></a>

### [`0088bd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bd50.md) → [`0088bd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md) _INIT_165

採用 · 移動量 `+0x40` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088bdf0",
      "incomplete_value": true,
      "site": "0088be0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088bdb0",
      "incomplete_value": true,
      "site": "0088bdcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088be30",
      "incomplete_value": true,
      "site": "0088be48",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088bdf0",
      "incomplete_value": true,
      "site": "0088be08",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "0088be8c",
      "incomplete_value": true,
      "site": "0088bed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088be4c",
      "incomplete_value": true,
      "site": "0088be90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3c:8"
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
      "0088bdcc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0088bdf0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0088be10",
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
      "0088bdcc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0088bdf0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0088be10",
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

- 旧版 [`0088bdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bd50.md#insn-0088bdc8) · [`0088bd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bd50.md#insn-0088bd7c) · [`0088bd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bd50.md#insn-0088bd84)
- 新版 [`0088be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md#insn-0088be08) · [`0088bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md#insn-0088bdbc)

~~~diff
- 0088bdc8 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0088bdc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0088bdc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0088bdc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0088be08 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0088be08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0088be08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0088be08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0088bdc8 bytes 4a093691
+ 0088be08 bytes 4a093791
- 0088bd7c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0088bd7c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0088bd7c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0088bd7c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0088bdbc ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0088bdbc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0088bdbc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0088bdbc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0088bd7c bytes 73621191
+ 0088bdbc bytes 73622191
- 0088bd84 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 0088bd84 bytes 69d1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acfa3ca4b3bcbf41b90d6cc22d5b82d"></a>

### [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) → [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) FUN_0088c120

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`00472ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472ab8.md) [`00472b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b6c.md) [`00472b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b7c.md) [`00472d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d64.md) [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00472af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md) [`00472bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bac.md) [`00472bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md) [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.65% / 新版 94.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c268",
      "incomplete_value": false,
      "site": "0088c270",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c228",
      "incomplete_value": false,
      "site": "0088c230",
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
            "const:798:8"
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
      "definition_site": "0088c334",
      "incomplete_value": false,
      "site": "0088c334",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c2f4",
      "incomplete_value": false,
      "site": "0088c2f4",
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
            "const:688:8"
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
      "definition_site": "0088c380",
      "incomplete_value": false,
      "site": "0088c380",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c340",
      "incomplete_value": false,
      "site": "0088c340",
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
            "const:718:8"
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
      "0088c168",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472b6c"
      ]
    ],
    [
      "0088c1f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ],
    [
      "0088c224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ],
  "added": [
    [
      "0088c168",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472bac"
      ]
    ],
    [
      "0088c1f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "0088c224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md#insn-0088c128) · [`0088c1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md#insn-0088c1b4) · [`0088c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md#insn-0088c1e4)
- 新版 [`0088c168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c168) · [`0088c1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c1f4) · [`0088c224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c224)

~~~diff
- 0088c128 ["INT_ADD", "register:40f0:8", ["const:88c128:8", "const:4:8"]]
- 0088c128 ["CALL", null, ["ram:472b6c:8"]]
+ 0088c168 ["INT_ADD", "register:40f0:8", ["const:88c168:8", "const:4:8"]]
+ 0088c168 ["CALL", null, ["ram:472bac:8"]]
- 0088c128 bytes 919aef97
+ 0088c168 bytes 919aef97
- 0088c1b4 ["INT_ADD", "register:40f0:8", ["const:88c1b4:8", "const:4:8"]]
- 0088c1b4 ["CALL", null, ["ram:768398:8"]]
+ 0088c1f4 ["INT_ADD", "register:40f0:8", ["const:88c1f4:8", "const:4:8"]]
+ 0088c1f4 ["CALL", null, ["ram:7683d8:8"]]
- 0088c1b4 bytes 7970fb97
+ 0088c1f4 bytes 7970fb97
- 0088c1e4 ["INT_ADD", "register:40f0:8", ["const:88c1e4:8", "const:4:8"]]
- 0088c1e4 ["CALL", null, ["ram:764344:8"]]
+ 0088c224 ["INT_ADD", "register:40f0:8", ["const:88c224:8", "const:4:8"]]
+ 0088c224 ["CALL", null, ["ram:764384:8"]]
- 0088c1e4 bytes 5860fb97
+ 0088c224 bytes 5860fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a18053bf493675d9e726094226b0586"></a>

### [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) → [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) FUN_0088c4ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`0088f45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f45c.md) [`0088f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f630.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md)
- 新版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`0088f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md) [`0088f674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f674.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c5cc",
      "incomplete_value": true,
      "site": "0088c5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:54d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c58c",
      "incomplete_value": true,
      "site": "0088c58c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
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
      "definition_site": "0088c5d0",
      "incomplete_value": true,
      "site": "0088c5d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088c590",
      "incomplete_value": true,
      "site": "0088c590",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088c4d0",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088c490",
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
      "0088c4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0088c4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0088c4f0",
      "READ",
      [
        "storage",
        "00ca4d50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0088c4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c4f0",
      "READ",
      [
        "storage",
        "00ca5150",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md#insn-0088c490) · [`0088c498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md#insn-0088c498) · [`0088c494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md#insn-0088c494)
- 新版 [`0088c4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c4d0) · [`0088c4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c4d8) · [`0088c4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c4d4)

~~~diff
- 0088c490 ["INT_ADD", "register:40f0:8", ["const:88c490:8", "const:4:8"]]
- 0088c490 ["CALL", null, ["ram:48ccb8:8"]]
+ 0088c4d0 ["INT_ADD", "register:40f0:8", ["const:88c4d0:8", "const:4:8"]]
+ 0088c4d0 ["CALL", null, ["ram:48ccf8:8"]]
- 0088c490 bytes 0a02f097
+ 0088c4d0 bytes 0a02f097
- 0088c498 ["INT_ADD", "register:40f0:8", ["const:88c498:8", "const:4:8"]]
- 0088c498 ["CALL", null, ["ram:48ccb8:8"]]
+ 0088c4d8 ["INT_ADD", "register:40f0:8", ["const:88c4d8:8", "const:4:8"]]
+ 0088c4d8 ["CALL", null, ["ram:48ccf8:8"]]
- 0088c498 bytes 0802f097
+ 0088c4d8 bytes 0802f097
- 0088c494 ["INT_ADD", "register:40f0:8", ["const:88c494:8", "const:4:8"]]
- 0088c494 ["CALL", null, ["callee:0048e7e0:8"]]
+ 0088c4d4 ["INT_ADD", "register:40f0:8", ["const:88c4d4:8", "const:4:8"]]
+ 0088c4d4 ["CALL", null, ["callee:0048e7e0:8"]]
- 0088c494 bytes c308f097
+ 0088c4d4 bytes c308f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490514bf35101461dd3b3aa63d29e386"></a>

### [`0088f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f240.md) → [`0088f280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md) FUN_0088f280

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088f2e8",
      "incomplete_value": false,
      "site": "0088f2ec",
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
      "definition_site": "0088f2a8",
      "incomplete_value": false,
      "site": "0088f2ac",
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
      "0088f2e8",
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
      "0088f2e8",
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

- 旧版 [`0088f2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f240.md#insn-0088f2ac) · [`0088f264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f240.md#insn-0088f264) · [`0088f2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f240.md#insn-0088f2a8)
- 新版 [`0088f2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2ec) · [`0088f2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2a4) · [`0088f2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2e8)

~~~diff
- 0088f2ac ["INT_ADD", "register:40f0:8", ["const:88f2ac:8", "const:4:8"]]
- 0088f2ac ["CALL", null, ["callee:00442930:8"]]
+ 0088f2ec ["INT_ADD", "register:40f0:8", ["const:88f2ec:8", "const:4:8"]]
+ 0088f2ec ["CALL", null, ["callee:00442930:8"]]
- 0088f2ac bytes 91cdee97
+ 0088f2ec bytes 91cdee97
- 0088f264 ["INT_ADD", "register:40f0:8", ["const:88f264:8", "const:4:8"]]
- 0088f264 ["CALL", null, ["callee:0046d5a8:8"]]
+ 0088f2a4 ["INT_ADD", "register:40f0:8", ["const:88f2a4:8", "const:4:8"]]
+ 0088f2a4 ["CALL", null, ["callee:0046d5a8:8"]]
- 0088f264 bytes c178ef97
+ 0088f2a4 bytes c178ef97
- 0088f2a8 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0088f2a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0088f2a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0088f2a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0088f2e8 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 0088f2e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0088f2e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0088f2e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0088f2a8 bytes 00c00391
+ 0088f2e8 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-848f407deeb65ca246986f6e7a452caa"></a>

### [`0088f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md) → [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) FUN_0088f6e0

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`0088fc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fc20.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`0088fc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.08% / 新版 94.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f714",
      "incomplete_value": true,
      "site": "0088f724",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f6d0",
      "incomplete_value": true,
      "site": "0088f6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5ff:8"
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
      "definition_site": "0088f728",
      "incomplete_value": true,
      "site": "0088f728",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088f6e4",
      "incomplete_value": true,
      "site": "0088f6e4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f71c",
      "incomplete_value": true,
      "site": "0088f72c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088f6d8",
      "incomplete_value": true,
      "site": "0088f6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0088f714",
      "READ",
      [
        "storage",
        "002a45ff",
        null,
        "string"
      ]
    ],
    [
      "0088f718",
      "READ",
      [
        "storage",
        "002a460e",
        null,
        "string"
      ]
    ],
    [
      "0088f71c",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088f714",
      "READ",
      [
        "storage",
        "002a46cc",
        null,
        "string"
      ]
    ],
    [
      "0088f718",
      "READ",
      [
        "storage",
        "002a46db",
        null,
        "string"
      ]
    ],
    [
      "0088f71c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md#insn-0088f864) · [`0088f6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md#insn-0088f6c0) · [`0088f6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f69c.md#insn-0088f6c8)
- 新版 [`0088f8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f8a8) · [`0088f704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f704) · [`0088f70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f70c)

~~~diff
- 0088f864 ["INT_ADD", "register:40f0:8", ["const:88f864:8", "const:4:8"]]
- 0088f864 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088f8a8 ["INT_ADD", "register:40f0:8", ["const:88f8a8:8", "const:4:8"]]
+ 0088f8a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0088f864 bytes 93200f94
+ 0088f8a8 bytes 82210f94
- 0088f6c0 ["INT_ADD", "register:40f0:8", ["const:88f6c0:8", "const:4:8"]]
- 0088f6c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088f704 ["INT_ADD", "register:40f0:8", ["const:88f704:8", "const:4:8"]]
+ 0088f704 ["CALL", null, ["callee:00c57e90:8"]]
- 0088f6c0 bytes f4200f94
+ 0088f704 bytes e3210f94
- 0088f6c8 ["COPY", "tmp:0:8", ["const:5ff:8"]]
- 0088f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f70c ["COPY", "tmp:0:8", ["const:6cc:8"]]
+ 0088f70c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f70c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f70c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f6c8 bytes 08fd1791
+ 0088f70c bytes 08311b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-864ccb3223db29d45cdbfcf1d27cb4d7"></a>

### [`0088fae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fae4.md) → [`0088fb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md) FUN_0088fb28

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088fb3c",
      "incomplete_value": false,
      "site": "0088fb40",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088faf8",
      "incomplete_value": false,
      "site": "0088fafc",
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
            "const:808:8"
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
      "0088fb40",
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fb40",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088faf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fae4.md#insn-0088faf8) · [`0088fb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fae4.md#insn-0088fb0c) · [`0088fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fae4.md#insn-0088fb2c)
- 新版 [`0088fb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb3c) · [`0088fb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb50) · [`0088fb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb70)

~~~diff
- 0088faf8 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0088faf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088faf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088faf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fb3c ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 0088fb3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088faf8 bytes 08212091
+ 0088fb3c bytes 08213091
- 0088fb0c ["INT_ADD", "register:40f0:8", ["const:88fb0c:8", "const:4:8"]]
- 0088fb0c ["CALL", null, ["callee:00c53d00:8"]]
+ 0088fb50 ["INT_ADD", "register:40f0:8", ["const:88fb50:8", "const:4:8"]]
+ 0088fb50 ["CALL", null, ["callee:00c53d00:8"]]
- 0088fb0c bytes 750f0f94
+ 0088fb50 bytes 6c100f94
- 0088fb2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fb2c ["INT_ADD", "register:40f0:8", ["const:88fb2c:8", "const:4:8"]]
- 0088fb2c ["CALLIND", null, ["register:0:8"]]
+ 0088fb70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fb70 ["INT_ADD", "register:40f0:8", ["const:88fb70:8", "const:4:8"]]
+ 0088fb70 ["CALLIND", null, ["register:0:8"]]
- 0088fb2c bytes 00013fd6
+ 0088fb70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c061c8082b45aef59f3e1e04f66b47e"></a>

### [`0088fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb40.md) → [`0088fb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md) FUN_0088fb84

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088fb9c",
      "incomplete_value": false,
      "site": "0088fba0",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fb58",
      "incomplete_value": false,
      "site": "0088fb5c",
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
            "const:808:8"
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
      "0088fba0",
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fba0",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb40.md#insn-0088fb58) · [`0088fb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb40.md#insn-0088fb6c) · [`0088fb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb40.md#insn-0088fb80)
- 新版 [`0088fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fb9c) · [`0088fbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fbb0) · [`0088fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fbc4)

~~~diff
- 0088fb58 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0088fb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fb9c ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 0088fb9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fb58 bytes 08212091
+ 0088fb9c bytes 08213091
- 0088fb6c ["INT_ADD", "register:40f0:8", ["const:88fb6c:8", "const:4:8"]]
- 0088fb6c ["CALL", null, ["callee:00c53d00:8"]]
+ 0088fbb0 ["INT_ADD", "register:40f0:8", ["const:88fbb0:8", "const:4:8"]]
+ 0088fbb0 ["CALL", null, ["callee:00c53d00:8"]]
- 0088fb6c bytes 5d0f0f94
+ 0088fbb0 bytes 54100f94
- 0088fb80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fb80 ["INT_ADD", "register:40f0:8", ["const:88fb80:8", "const:4:8"]]
- 0088fb80 ["CALLIND", null, ["register:0:8"]]
+ 0088fbc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fbc4 ["INT_ADD", "register:40f0:8", ["const:88fbc4:8", "const:4:8"]]
+ 0088fbc4 ["CALLIND", null, ["register:0:8"]]
- 0088fb80 bytes 00013fd6
+ 0088fbc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8bbdac4ded929bbbe8c0d3e6ab59ed"></a>

### [`0088fb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb9c.md) → [`0088fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md) FUN_0088fbe0

採用 · 移動量 `+0x44` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088fc04",
      "incomplete_value": false,
      "site": "0088fc04",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fbc0",
      "incomplete_value": false,
      "site": "0088fbc0",
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
            "const:808:8"
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
      "0088fc04",
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fc04",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb9c.md#insn-0088fbb0) · [`0088fbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb9c.md#insn-0088fbbc) · [`0088fbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fb9c.md#insn-0088fbd8)
- 新版 [`0088fbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fbf4) · [`0088fc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fc00) · [`0088fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fc1c)

~~~diff
- 0088fbb0 ["INT_ADD", "register:40f0:8", ["const:88fbb0:8", "const:4:8"]]
- 0088fbb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088fbf4 ["INT_ADD", "register:40f0:8", ["const:88fbf4:8", "const:4:8"]]
+ 0088fbf4 ["CALL", null, ["callee:00c57e90:8"]]
- 0088fbb0 bytes b81f0f94
+ 0088fbf4 bytes a7200f94
- 0088fbbc ["COPY", "tmp:0:8", ["const:808:8"]]
- 0088fbbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fbbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fbbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fc00 ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 0088fc00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fbbc bytes 29212091
+ 0088fc00 bytes 29213091
- 0088fbd8 ["INT_ADD", "register:40f0:8", ["const:88fbd8:8", "const:4:8"]]
- 0088fbd8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0088fc1c ["INT_ADD", "register:40f0:8", ["const:88fc1c:8", "const:4:8"]]
+ 0088fc1c ["CALL", null, ["callee:00c53cd0:8"]]
- 0088fbd8 bytes 360f0f94
+ 0088fc1c bytes 2d100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7270f58b8d27e00a429d73e950658976"></a>

### [`0088fbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fbec.md) → [`0088fc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md) FUN_0088fc30

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088fc3c",
      "incomplete_value": false,
      "site": "0088fc3c",
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
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fbf8",
      "incomplete_value": false,
      "site": "0088fbf8",
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
            "const:808:8"
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
      "0088fc3c",
      "DATA",
      [
        "storage",
        "00c81808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fc3c",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fbec.md#insn-0088fbf4) · [`0088fc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fbec.md#insn-0088fc14)
- 新版 [`0088fc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md#insn-0088fc38) · [`0088fc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md#insn-0088fc58)

~~~diff
- 0088fbf4 ["COPY", "tmp:0:8", ["const:808:8"]]
- 0088fbf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fbf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fbf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fc38 ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 0088fc38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fbf4 bytes 29212091
+ 0088fc38 bytes 29213091
- 0088fc14 ["INT_ADD", "register:40f0:8", ["const:88fc14:8", "const:4:8"]]
- 0088fc14 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0088fc58 ["INT_ADD", "register:40f0:8", ["const:88fc58:8", "const:4:8"]]
+ 0088fc58 ["CALL", null, ["callee:00c53cd0:8"]]
- 0088fc14 bytes 270f0f94
+ 0088fc58 bytes 1e100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-099a52d08384aff2904cf7a4ebd2730f"></a>

### [`0088fcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md) → [`0088fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md) FUN_0088fd04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "0088fd0c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088fcc8",
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
      "0088fd0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0088fd0c",
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

- 旧版 [`0088fcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md#insn-0088fcc8) · [`0088fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md#insn-0088fccc) · [`0088fcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fcc0.md#insn-0088fcd4)
- 新版 [`0088fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd0c) · [`0088fd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd10) · [`0088fd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd18)

~~~diff
- 0088fcc8 ["INT_ADD", "register:40f0:8", ["const:88fcc8:8", "const:4:8"]]
- 0088fcc8 ["CALL", null, ["ram:48ccb8:8"]]
+ 0088fd0c ["INT_ADD", "register:40f0:8", ["const:88fd0c:8", "const:4:8"]]
+ 0088fd0c ["CALL", null, ["ram:48ccf8:8"]]
- 0088fcc8 bytes fcf3ef97
+ 0088fd0c bytes fbf3ef97
- 0088fccc ["INT_ADD", "register:40f0:8", ["const:88fccc:8", "const:4:8"]]
- 0088fccc ["CALL", null, ["callee:0048dc4c:8"]]
+ 0088fd10 ["INT_ADD", "register:40f0:8", ["const:88fd10:8", "const:4:8"]]
+ 0088fd10 ["CALL", null, ["callee:0048dc4c:8"]]
- 0088fccc bytes d0f7ef97
+ 0088fd10 bytes cff7ef97
- 0088fcd4 ["INT_ADD", "register:40f0:8", ["const:88fcd4:8", "const:4:8"]]
- 0088fcd4 ["CALL", null, ["callee:008514f8:8"]]
+ 0088fd18 ["INT_ADD", "register:40f0:8", ["const:88fd18:8", "const:4:8"]]
+ 0088fd18 ["CALL", null, ["callee:008514f8:8"]]
- 0088fcd4 bytes f905ff97
+ 0088fd18 bytes f805ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b372d8783ec904b7838510af6d9fab06"></a>

### [`0088fd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd1c.md) → [`0088fd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md) FUN_0088fd60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088fd74",
      "incomplete_value": false,
      "site": "0088fd78",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fd30",
      "incomplete_value": false,
      "site": "0088fd34",
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
            "const:898:8"
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
      "0088fd78",
      "DATA",
      [
        "storage",
        "00c81898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fd78",
      "DATA",
      [
        "storage",
        "00c81c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd1c.md#insn-0088fd28) · [`0088fd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd1c.md#insn-0088fd30)
- 新版 [`0088fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md#insn-0088fd6c) · [`0088fd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md#insn-0088fd74)

~~~diff
- 0088fd28 ["INT_ADD", "register:40f0:8", ["const:88fd28:8", "const:4:8"]]
- 0088fd28 ["CALL", null, ["callee:00c57e90:8"]]
+ 0088fd6c ["INT_ADD", "register:40f0:8", ["const:88fd6c:8", "const:4:8"]]
+ 0088fd6c ["CALL", null, ["callee:00c57e90:8"]]
- 0088fd28 bytes 5a1f0f94
+ 0088fd6c bytes 49200f94
- 0088fd30 ["COPY", "tmp:0:8", ["const:898:8"]]
- 0088fd30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fd74 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0088fd74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fd74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fd74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fd30 bytes 08612291
+ 0088fd74 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b931c92c8515fb5903691c23e413393"></a>

### [`0088fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) → [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) FUN_0088fd9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`00890170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md) [`008901c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`008901b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md) [`00890204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 83.87% / 新版 83.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fdd4",
      "incomplete_value": true,
      "site": "0088fdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fd90",
      "incomplete_value": true,
      "site": "0088fd90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88e:8"
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
      "definition_site": "0088fdcc",
      "incomplete_value": true,
      "site": "0088fdd8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088fd88",
      "incomplete_value": true,
      "site": "0088fd94",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fe68",
      "incomplete_value": false,
      "site": "0088fe68",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fe24",
      "incomplete_value": false,
      "site": "0088fe24",
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
            "const:908:8"
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
      "0088fdc0",
      "READ",
      [
        "storage",
        "002b788e",
        null,
        "string"
      ]
    ],
    [
      "0088fdcc",
      "READ",
      [
        "storage",
        "002b7895",
        null,
        "string"
      ]
    ],
    [
      "0088fe68",
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fdc0",
      "READ",
      [
        "storage",
        "002b78ce",
        null,
        "string"
      ]
    ],
    [
      "0088fdcc",
      "READ",
      [
        "storage",
        "002b78d5",
        null,
        "string"
      ]
    ],
    [
      "0088fe68",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md#insn-0088fe94) · [`0088fd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md#insn-0088fd74) · [`0088fda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md#insn-0088fda4)
- 新版 [`0088fed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fed8) · [`0088fdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fdb8) · [`0088fde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fde8)

~~~diff
- 0088fe94 ["INT_ADD", "register:40f0:8", ["const:88fe94:8", "const:4:8"]]
- 0088fe94 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0088fed8 ["INT_ADD", "register:40f0:8", ["const:88fed8:8", "const:4:8"]]
+ 0088fed8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0088fe94 bytes 071f0f94
+ 0088fed8 bytes f61f0f94
- 0088fd74 ["COPY", "tmp:0:8", ["const:88e:8"]]
- 0088fd74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fd74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fd74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fdb8 ["COPY", "tmp:0:8", ["const:8ce:8"]]
+ 0088fdb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fdb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fdb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fd74 bytes 29392291
+ 0088fdb8 bytes 29392391
- 0088fda4 ["INT_ADD", "register:40f0:8", ["const:88fda4:8", "const:4:8"]]
- 0088fda4 ["CALL", null, ["callee:0048ce54:8"]]
+ 0088fde8 ["INT_ADD", "register:40f0:8", ["const:88fde8:8", "const:4:8"]]
+ 0088fde8 ["CALL", null, ["callee:0048ce54:8"]]
- 0088fda4 bytes 1cf4ef97
+ 0088fde8 bytes 1bf4ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7097c4ff64c2b0d698d9d7656324cc5a"></a>

### [`00890034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890034.md) → [`00890078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md) FUN_00890078

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0089008c",
      "incomplete_value": false,
      "site": "00890090",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890048",
      "incomplete_value": false,
      "site": "0089004c",
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
            "const:908:8"
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
      "00890090",
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890090",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890034.md#insn-00890048) · [`0089005c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890034.md#insn-0089005c) · [`0089007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890034.md#insn-0089007c)
- 新版 [`0089008c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-0089008c) · [`008900a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-008900a0) · [`008900c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-008900c0)

~~~diff
- 00890048 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00890048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00890048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00890048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089008c ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 0089008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00890048 bytes 08212491
+ 0089008c bytes 08213491
- 0089005c ["INT_ADD", "register:40f0:8", ["const:89005c:8", "const:4:8"]]
- 0089005c ["CALL", null, ["callee:00c53d00:8"]]
+ 008900a0 ["INT_ADD", "register:40f0:8", ["const:8900a0:8", "const:4:8"]]
+ 008900a0 ["CALL", null, ["callee:00c53d00:8"]]
- 0089005c bytes 210e0f94
+ 008900a0 bytes 180f0f94
- 0089007c ["COPY", "register:0:8", ["register:4040:8"]]
- 0089007c ["INT_ADD", "register:40f0:8", ["const:89007c:8", "const:4:8"]]
- 0089007c ["CALLIND", null, ["register:0:8"]]
+ 008900c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008900c0 ["INT_ADD", "register:40f0:8", ["const:8900c0:8", "const:4:8"]]
+ 008900c0 ["CALLIND", null, ["register:0:8"]]
- 0089007c bytes 00013fd6
+ 008900c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3938e5d6b6c6dd892c64743f41b667f3"></a>

### [`00890090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890090.md) → [`008900d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md) FUN_008900d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008900ec",
      "incomplete_value": false,
      "site": "008900f0",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008900a8",
      "incomplete_value": false,
      "site": "008900ac",
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
            "const:908:8"
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
      "008900f0",
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008900f0",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008900a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890090.md#insn-008900a8) · [`008900bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890090.md#insn-008900bc) · [`008900d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890090.md#insn-008900d0)
- 新版 [`008900ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-008900ec) · [`00890100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-00890100) · [`00890114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-00890114)

~~~diff
- 008900a8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 008900a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008900a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008900a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008900ec ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 008900ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008900ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008900ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008900a8 bytes 08212491
+ 008900ec bytes 08213491
- 008900bc ["INT_ADD", "register:40f0:8", ["const:8900bc:8", "const:4:8"]]
- 008900bc ["CALL", null, ["callee:00c53d00:8"]]
+ 00890100 ["INT_ADD", "register:40f0:8", ["const:890100:8", "const:4:8"]]
+ 00890100 ["CALL", null, ["callee:00c53d00:8"]]
- 008900bc bytes 090e0f94
+ 00890100 bytes 000f0f94
- 008900d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008900d0 ["INT_ADD", "register:40f0:8", ["const:8900d0:8", "const:4:8"]]
- 008900d0 ["CALLIND", null, ["register:0:8"]]
+ 00890114 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890114 ["INT_ADD", "register:40f0:8", ["const:890114:8", "const:4:8"]]
+ 00890114 ["CALLIND", null, ["register:0:8"]]
- 008900d0 bytes 00013fd6
+ 00890114 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e19841207224ef7a312121d27fd62840"></a>

### [`0089013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089013c.md) → [`00890180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md) FUN_00890180

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0089018c",
      "incomplete_value": false,
      "site": "0089018c",
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
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890148",
      "incomplete_value": false,
      "site": "00890148",
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
            "const:908:8"
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
      "0089018c",
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089018c",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089013c.md#insn-00890144) · [`00890150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089013c.md#insn-00890150) · [`00890164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089013c.md#insn-00890164)
- 新版 [`00890188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md#insn-00890188) · [`00890194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md#insn-00890194) · [`008901a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md#insn-008901a8)

~~~diff
- 00890144 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00890144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00890144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00890144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00890188 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00890188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00890188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00890188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00890144 bytes 29212491
+ 00890188 bytes 29213491
- 00890150 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00890150 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00890194 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00890194 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00890150 bytes e80000b4
+ 00890194 bytes e80000b4
- 00890164 ["INT_ADD", "register:40f0:8", ["const:890164:8", "const:4:8"]]
- 00890164 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008901a8 ["INT_ADD", "register:40f0:8", ["const:8901a8:8", "const:4:8"]]
+ 008901a8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00890164 bytes d30d0f94
+ 008901a8 bytes ca0e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96a0cb10b8a0ebce1d328996046057a"></a>

### [`0089023c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089023c.md) → [`00890280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md) _INIT_166

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 54.76% / 新版 56.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089026c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008902b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0089026c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890278",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00890294",
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
      "008902b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008902bc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008902d8",
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

- 旧版 [`0089026c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089023c.md#insn-0089026c) · [`00890294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/0089023c.md#insn-00890294)
- 新版 [`008902b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md#insn-008902b0)

~~~diff
- 0089026c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0089026c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0089026c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0089026c bytes a9831ff8
- 00890294 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00890294 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00890294 bytes e013813c
+ 008902b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008902b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 008902b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008902b0 bytes a9831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e739c513a0d05d8c8a49a813a7dbb2"></a>

### [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) → [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) FUN_00890610

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00890b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) [`00891d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md) · 呼出先 3件 [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 2件 [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) [`00891dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891dc8.md) · 呼出先 3件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 57.14% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008905d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008905d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00890614"
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
      "unmatched:008905d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089061c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00890678"
      ]
    ]
  ],
  "added": [
    [
      "00890614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00890660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00890678"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008905d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md#insn-008905d0) · [`00890614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md#insn-00890614)
- 新版 [`00890658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md#insn-00890658) · [`00890614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md#insn-00890614)

~~~diff
- 008905d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008905d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008905d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008905d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008905d0 bytes fd7b04a9
- 00890614 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00890614 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00890658 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00890658 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00890614 bytes c00000b4
+ 00890658 bytes c00000b4
+ 00890614 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00890614 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00890614 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 00890614 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00890614 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc7268f7e9050cca68219577537a92d"></a>

### [`00890710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) → [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) FUN_00890754

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00890b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) [`00890d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md) [`00892580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) [`00890d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md) [`008925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.93% / 新版 75.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008907bc",
      "incomplete_value": true,
      "site": "008907bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:1ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890778",
      "incomplete_value": true,
      "site": "00890778",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:1bf:8"
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
      "definition_site": "00890818",
      "incomplete_value": true,
      "site": "00890818",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
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
    "old": {
      "definition_site": "008907d4",
      "incomplete_value": true,
      "site": "008907d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:1e3:8"
              ]
            ]
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
      "unmatched:00890758",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008907a8",
      "READ",
      [
        "storage",
        "002f31bf",
        null,
        "string"
      ]
    ],
    [
      "008907c4",
      "READ",
      [
        "storage",
        "002f31cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0089079c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008907a8",
      "READ",
      [
        "storage",
        "002f31ff",
        null,
        "string"
      ]
    ],
    [
      "008907c4",
      "READ",
      [
        "storage",
        "002f320b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md#insn-00890758) · [`0089079c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md#insn-0089079c)
- 新版 [`008907e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md#insn-008907e0) · [`0089079c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md#insn-0089079c)

~~~diff
- 00890758 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00890758 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00890758 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00890758 bytes a8031ff8
- 0089079c ["COPY", "tmp:0:8", ["const:1d7:8"]]
- 0089079c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0089079c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0089079c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008907e0 ["COPY", "tmp:0:8", ["const:217:8"]]
+ 008907e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008907e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008907e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0089079c bytes 295d0791
+ 008907e0 bytes 295d0891
+ 0089079c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0089079c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
+ 0089079c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0089079c bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d09ca88ac9c3edc2916188492093aa"></a>

### [`00890b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md) → [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) FUN_00890bd0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00890710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 61.11% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00890bf8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00890be0",
      "incomplete_value": true,
      "site": "00890be4",
      "value": [
        "live",
        "register:8:8"
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
      "unmatched:00890bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00890bf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md#insn-00890bb4) · [`00890be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890b8c.md#insn-00890be4)
- 新版 [`00890c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md#insn-00890c28) · [`00890bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md#insn-00890bf8)

~~~diff
- 00890bb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00890bb4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00890bb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00890bb4 bytes a8831ff8
- 00890be4 ["INT_ADD", "register:40f0:8", ["const:890be4:8", "const:4:8"]]
- 00890be4 ["CALL", null, ["callee:0043bb20:8"]]
+ 00890c28 ["INT_ADD", "register:40f0:8", ["const:890c28:8", "const:4:8"]]
+ 00890c28 ["CALL", null, ["callee:0043bb20:8"]]
- 00890be4 bytes bfabee97
+ 00890c28 bytes beabee97
+ 00890bf8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00890bf8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00890bf8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00890bf8 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a165bac34323d3d19803aa7d6e7558a"></a>

### [`00890d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md) → [`00890d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md) FUN_00890d8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00890710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 67.69% / 新版 65.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00890e28",
      "incomplete_value": true,
      "site": "00890e2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00890e24",
      "incomplete_value": true,
      "site": "00890e28",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:118:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00890de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md#insn-00890de8) · [`00890e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md#insn-00890e28) · [`00890d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890d48.md#insn-00890d5c)
- 新版 [`00890e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890e2c) · [`00890e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890e6c) · [`00890da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md#insn-00890da0)

~~~diff
- 00890de8 ["INT_ADD", "register:40f0:8", ["const:890de8:8", "const:4:8"]]
- 00890de8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00890e2c ["INT_ADD", "register:40f0:8", ["const:890e2c:8", "const:4:8"]]
+ 00890e2c ["CALL", null, ["callee:00c57eb0:8"]]
- 00890de8 bytes 321b0f94
+ 00890e2c bytes 211c0f94
- 00890e28 ["INT_ADD", "register:40f0:8", ["const:890e28:8", "const:4:8"]]
- 00890e28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00890e6c ["INT_ADD", "register:40f0:8", ["const:890e6c:8", "const:4:8"]]
+ 00890e6c ["CALL", null, ["callee:00c57eb0:8"]]
- 00890e28 bytes 221b0f94
+ 00890e6c bytes 111c0f94
- 00890d5c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00890d5c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00890d5c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00890d5c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00890da0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00890da0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00890da0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00890da0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00890d5c bytes 48040037
+ 00890da0 bytes 48040037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa2f470216c1e5226fb1c0935708d43"></a>

### [`00890f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md) → [`00890fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890fe0.md) FUN_00890fe0

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008486d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008486d4.md) [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`008548ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/008548ac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00848714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848714.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`008548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008548ec.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 74.67% / 新版 74.67%

CFGの説明率　旧版 12.24% / 新版 11.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00890fe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00890ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00890ffc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00890fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089101c"
      ]
    ],
    [
      "unmatched:00890ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00891008"
      ]
    ],
    [
      "unmatched:00890ffc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008910c0"
      ]
    ]
  ],
  "added": [
    [
      "0089102c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089101c"
      ]
    ],
    [
      "0089103c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089104c"
      ]
    ],
    [
      "00891040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00891060"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md#insn-00890fe8) · [`00890ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md#insn-00890ff8) · [`00890ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890f9c.md#insn-00890ffc)

~~~diff
- 00890fe8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00890fe8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00890fe8 bytes 95ffffb4
- 00890ff8 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00890ff8 bytes 80000054
- 00890ffc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00890ffc ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00890ffc bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba1329d07684147c4927a370d792b67"></a>

### [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) → [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) FUN_00891304

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · 呼出先 23件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) · 呼出先 23件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.19% / 新版 91.19%

CFGの説明率　旧版 67.39% / 新版 65.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 3件, `store_value` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891598"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00891648",
      "incomplete_value": false,
      "site": "00891648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891604",
      "incomplete_value": false,
      "site": "00891604",
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
            "const:c28:8"
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
      "unmatched:00891538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089183c"
      ]
    ],
    [
      "unmatched:00891558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089183c"
      ]
    ],
    [
      "unmatched:00891580",
      "WRITE",
      [
        "storage",
        "Stack[-0x188]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0089157c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089183c"
      ]
    ],
    [
      "0089159c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089183c"
      ]
    ],
    [
      "008915c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x188]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008914b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md#insn-008914b4) · [`00891514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md#insn-00891514) · [`00891538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md#insn-00891538)
- 新版 [`008914f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md#insn-008914f8) · [`00891558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md#insn-00891558)

~~~diff
- 008914b4 ["INT_ADD", "register:40f0:8", ["const:8914b4:8", "const:4:8"]]
- 008914b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008914f8 ["INT_ADD", "register:40f0:8", ["const:8914f8:8", "const:4:8"]]
+ 008914f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 008914b4 bytes 7f190f94
+ 008914f8 bytes 6e1a0f94
- 00891514 ["INT_ADD", "register:40f0:8", ["const:891514:8", "const:4:8"]]
- 00891514 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00891558 ["INT_ADD", "register:40f0:8", ["const:891558:8", "const:4:8"]]
+ 00891558 ["CALL", null, ["callee:00c57eb0:8"]]
- 00891514 bytes 67190f94
+ 00891558 bytes 561a0f94
- 00891538 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00891538 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00891538 ["CBRANCH", null, ["local:b90:8", "tmp:1:1"]]
- 00891538 bytes 09160054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4f3327d464fd81eb18405bc7fa31986"></a>

### [`008919c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008919c8.md) → [`00891a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891a0c.md) FUN_00891a0c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b38cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38cec.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b39114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39114.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 89.29% / 新版 86.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00891acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00891b10"
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
      "00891b04",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[47]"
      ]
    ],
    [
      "00891b08",
      "READ",
      [
        "storage",
        "002f3278",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00891acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00891b1c"
      ]
    ]
  ],
  "added": [
    [
      "00891b04",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[55]"
      ]
    ],
    [
      "00891b08",
      "READ",
      [
        "storage",
        "002f32b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00891b10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00891b1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008919c8.md#insn-00891acc) · [`008919e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008919c8.md#insn-008919e4)
- 新版 [`00891b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891a0c.md#insn-00891b10) · [`00891a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891a0c.md#insn-00891a28)

~~~diff
- 00891acc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00891acc ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00891acc bytes 6a000054
+ 00891b10 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00891b10 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00891b10 bytes 6a000054
- 008919e4 ["INT_ADD", "register:40f0:8", ["const:8919e4:8", "const:4:8"]]
- 008919e4 ["CALL", null, ["callee:00b39114:8"]]
+ 00891a28 ["INT_ADD", "register:40f0:8", ["const:891a28:8", "const:4:8"]]
+ 00891a28 ["CALL", null, ["callee:00b39114:8"]]
- 008919e4 bytes c29c0a94
+ 00891a28 bytes bb9d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6b612a58a0b075868a7614a5e93782"></a>

### [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) → [`00891b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md) FUN_00891b6c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`008923f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md) [`00893108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) [`00893258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) · 呼出先 9件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00892c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c4c.md) [`00892c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c50.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md)
- 新版 呼出元 4件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) [`0089243c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089243c.md) [`0089314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md) [`0089329c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089329c.md) · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00892c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c90.md) [`00892c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c94.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.14% / 新版 74.14%

CFGの説明率　旧版 58.06% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891b88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00891b4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00891c1c"
      ]
    ],
    [
      "unmatched:00891b74",
      "READ",
      [
        "storage",
        "002a5a0e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00891b78",
      "READ",
      [
        "storage",
        "002a5a1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00891b90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00891c1c"
      ]
    ],
    [
      "00891bb8",
      "READ",
      [
        "storage",
        "002a5aea",
        null,
        "string"
      ]
    ],
    [
      "00891bbc",
      "READ",
      [
        "storage",
        "002a5afa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md#insn-00891b4c) · [`00891b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md#insn-00891b80) · [`00891b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md#insn-00891b84)

~~~diff
- 00891b4c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00891b4c bytes 60040054
- 00891b80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00891b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00891b80 bytes e00b00f9
- 00891b84 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00891b84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00891b84 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a3ee41f8655a1da2e96d8fcc6feb63e"></a>

### [`00891d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md) → [`00891dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891dc8.md) FUN_00891dc8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008905cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008905cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00890610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890610.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 53.57% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00891df8"
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
      "unmatched:00891db4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00891dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00891e68",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00891df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00891e14",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00891eac",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md#insn-00891db4) · [`00891dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891d84.md#insn-00891dd0)
- 新版 [`00891df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891dc8.md#insn-00891df8)

~~~diff
- 00891db4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00891db4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00891db4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00891db4 bytes a8831ff8
- 00891dd0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00891dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00891dd0 bytes e003803d
+ 00891df8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00891df8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00891df8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00891df8 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff575e54c548318f1bbef485a7af3cf5"></a>

### [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) → [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) FUN_00891f60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00892e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 16件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde0.md) [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) [`0058f3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f3f4.md)
- 新版 呼出元 3件 [`00892eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892eac.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 16件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce20.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 72.07% / 新版 74.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892290",
      "incomplete_value": false,
      "site": "00892298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089224c",
      "incomplete_value": false,
      "site": "00892254",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008922a4",
      "incomplete_value": false,
      "site": "008922a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892260",
      "incomplete_value": false,
      "site": "00892260",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008920f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008920f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089221c"
      ]
    ],
    [
      "0089215c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008921d8"
      ]
    ],
    [
      "008921fc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008921d8"
      ]
    ]
  ],
  "added": [
    [
      "00892134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892374"
      ]
    ],
    [
      "0089215c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0089221c"
      ]
    ],
    [
      "008921fc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0089221c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008920f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md#insn-008920f0) · [`00892134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md#insn-00892134)
- 新版 [`00892178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md#insn-00892178) · [`00892134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md#insn-00892134)

~~~diff
- 008920f0 ["CBRANCH", null, ["local:b72:8", "register:102:1"]]
- 008920f0 bytes 02120054
- 00892134 ["COPY", "register:0:8", ["register:4040:8"]]
- 00892134 ["INT_ADD", "register:40f0:8", ["const:892134:8", "const:4:8"]]
- 00892134 ["CALLIND", null, ["register:0:8"]]
+ 00892178 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00892178 ["INT_ADD", "register:40f0:8", ["const:892178:8", "const:4:8"]]
+ 00892178 ["CALLIND", null, ["register:0:8"]]
- 00892134 bytes 00013fd6
+ 00892178 bytes 00013fd6
+ 00892134 ["CBRANCH", null, ["local:b70:8", "register:102:1"]]
+ 00892134 bytes 02120054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6f6660d2b010449b0eddfaf6f5c20e1"></a>

### [`008923f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md) → [`0089243c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089243c.md) FUN_0089243c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 7件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008bb4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4cc.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 7件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00891b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008bb510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb510.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 63.41% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008923fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00892440"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00892444"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008923fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00892444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008924a8"
      ]
    ],
    [
      "unmatched:008924bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089255c"
      ]
    ]
  ],
  "added": [
    [
      "00892440",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00892488",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008924a8"
      ]
    ],
    [
      "00892500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089255c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008923fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md#insn-008923fc) · [`00892444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008923f8.md#insn-00892444)
- 新版 [`00892440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089243c.md#insn-00892440)

~~~diff
- 008923fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008923fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008923fc bytes e80b00fd
+ 00892440 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00892440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
+ 00892440 bytes e80b00fd
- 00892444 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00892444 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed3216f14da8de66536c457aa8e5ccb2"></a>

### [`00892580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md) → [`008925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md) FUN_008925c4

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00890710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890710.md) [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "008925d0",
      "incomplete_value": false,
      "site": "008925d4",
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
      "definition_site": "0089258c",
      "incomplete_value": false,
      "site": "00892590",
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
      "008925d0",
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
      "008925d0",
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

- 旧版 [`00892590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md#insn-00892590) · [`0089258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892580.md#insn-0089258c)
- 新版 [`008925d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md#insn-008925d4) · [`008925d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md#insn-008925d0)

~~~diff
- 00892590 ["INT_ADD", "register:40f0:8", ["const:892590:8", "const:4:8"]]
- 00892590 ["CALL", null, ["callee:0043b778:8"]]
+ 008925d4 ["INT_ADD", "register:40f0:8", ["const:8925d4:8", "const:4:8"]]
+ 008925d4 ["CALL", null, ["callee:0043b778:8"]]
- 00892590 bytes 6aa4ee97
+ 008925d4 bytes 69a4ee97
- 0089258c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0089258c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0089258c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0089258c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008925d0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008925d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008925d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008925d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0089258c bytes 00303c91
+ 008925d0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c73384b56393af373e7adc0d54946e"></a>

### [`00892598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892598.md) → [`008925dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md) FUN_008925dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008925f0",
      "incomplete_value": false,
      "site": "008925f4",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008925ac",
      "incomplete_value": false,
      "site": "008925b0",
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
            "const:998:8"
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
      "008925f4",
      "DATA",
      [
        "storage",
        "00c81998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008925f4",
      "DATA",
      [
        "storage",
        "00c81d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008925a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892598.md#insn-008925a4) · [`008925ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892598.md#insn-008925ac)
- 新版 [`008925e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md#insn-008925e8) · [`008925f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md#insn-008925f0)

~~~diff
- 008925a4 ["INT_ADD", "register:40f0:8", ["const:8925a4:8", "const:4:8"]]
- 008925a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008925e8 ["INT_ADD", "register:40f0:8", ["const:8925e8:8", "const:4:8"]]
+ 008925e8 ["CALL", null, ["callee:00c57e90:8"]]
- 008925a4 bytes 3b150f94
+ 008925e8 bytes 2a160f94
- 008925ac ["COPY", "tmp:0:8", ["const:998:8"]]
- 008925ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008925ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008925ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008925f0 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 008925f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008925f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008925f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008925ac bytes 08612691
+ 008925f0 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f90be182e9f60dad8f8dd20f49dffa"></a>

### [`008925d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md) → [`00892618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md) FUN_00892618

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00892718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892718.md) [`0089271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/0089271c.md) [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0089275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089275c.md) [`00892760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892760.md) [`00b3a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a5b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892644",
      "incomplete_value": false,
      "site": "0089264c",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892600",
      "incomplete_value": false,
      "site": "00892608",
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
            "const:a18:8"
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
      "0089264c",
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ],
    [
      "00892680",
      "READ",
      [
        "storage",
        "00c81a38",
        null,
        "pointer"
      ]
    ],
    [
      "00892680",
      "READ",
      [
        "storage",
        "00c81a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089264c",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ],
    [
      "00892680",
      "READ",
      [
        "storage",
        "00c81e38",
        null,
        "pointer"
      ]
    ],
    [
      "00892680",
      "READ",
      [
        "storage",
        "00c81e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008925f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md#insn-008925f8) · [`00892600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md#insn-00892600) · [`00892614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md#insn-00892614)
- 新版 [`0089263c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-0089263c) · [`00892644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-00892644) · [`00892658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-00892658)

~~~diff
- 008925f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008925f8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 0089263c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 0089263c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008925f8 bytes 6b020054
+ 0089263c bytes 6b020054
- 00892600 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 00892600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892644 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00892644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892600 bytes 08612891
+ 00892644 bytes 08613891
- 00892614 ["INT_ADD", "register:40f0:8", ["const:892614:8", "const:4:8"]]
- 00892614 ["CALL", null, ["callee:00b3a5b8:8"]]
+ 00892658 ["INT_ADD", "register:40f0:8", ["const:892658:8", "const:4:8"]]
+ 00892658 ["CALL", null, ["callee:00b3a5b8:8"]]
- 00892614 bytes df9e0a94
+ 00892658 bytes d89f0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4841aa7c80916f0c4fbfe26f9d806fd"></a>

### [`00892708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892708.md) → [`0089274c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089274c.md) FUN_0089274c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892750",
      "incomplete_value": false,
      "site": "00892754",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089270c",
      "incomplete_value": false,
      "site": "00892710",
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
      "00892754",
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892754",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089270c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892708.md#insn-0089270c)
- 新版 [`00892750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089274c.md#insn-00892750)

~~~diff
- 0089270c ["COPY", "tmp:0:8", ["const:a18:8"]]
- 0089270c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089270c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089270c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892750 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00892750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089270c bytes 08612891
+ 00892750 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e96101ea16b919b80f287e0972cd51fd"></a>

### [`00892720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892720.md) → [`00892764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md) FUN_00892764

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.93% / 新版 86.93%

CFGの説明率　旧版 37.93% / 新版 37.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892724"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892724"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892798"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00892724",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00892758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "unmatched:00892790",
      "READ",
      [
        "storage",
        "002a338f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00892768",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0089279c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "008927d4",
      "READ",
      [
        "storage",
        "002a345c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892720.md#insn-00892724) · [`00892758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892720.md#insn-00892758) · [`0089275c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892720.md#insn-0089275c)
- 新版 [`008927a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md#insn-008927a0)

~~~diff
- 00892724 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00892724 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00892724 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00892724 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00892724 bytes fd7b0da9
- 00892758 ["INT_ADD", "register:40f0:8", ["const:892758:8", "const:4:8"]]
- 00892758 ["CALL", null, ["ram:71c420:8"]]
- 00892758 bytes 3227fa97
- 0089275c ["INT_ADD", "register:40f0:8", ["const:89275c:8", "const:4:8"]]
- 0089275c ["CALL", null, ["callee:008514f8:8"]]
+ 008927a0 ["INT_ADD", "register:40f0:8", ["const:8927a0:8", "const:4:8"]]
+ 008927a0 ["CALL", null, ["callee:008514f8:8"]]
- 0089275c bytes 57fbfe97
+ 008927a0 bytes 56fbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8104869c486fd8642d3c64a5d8526d72"></a>

### [`00892ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892ac8.md) → [`00892b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md) FUN_00892b0c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892b20",
      "incomplete_value": false,
      "site": "00892b24",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892adc",
      "incomplete_value": false,
      "site": "00892ae0",
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
            "const:a88:8"
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
      "00892b24",
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892b24",
      "DATA",
      [
        "storage",
        "00c81e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892ac8.md#insn-00892ad4) · [`00892adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892ac8.md#insn-00892adc)
- 新版 [`00892b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md#insn-00892b18) · [`00892b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md#insn-00892b20)

~~~diff
- 00892ad4 ["INT_ADD", "register:40f0:8", ["const:892ad4:8", "const:4:8"]]
- 00892ad4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00892b18 ["INT_ADD", "register:40f0:8", ["const:892b18:8", "const:4:8"]]
+ 00892b18 ["CALL", null, ["callee:00c57e90:8"]]
- 00892ad4 bytes ef130f94
+ 00892b18 bytes de140f94
- 00892adc ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00892adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892b20 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00892b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892adc bytes 08212a91
+ 00892b20 bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b87917bd68759b3361a237d9df38733a"></a>

### [`00892aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892aec.md) → [`00892b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b30.md) FUN_00892b30

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892b34",
      "incomplete_value": false,
      "site": "00892b38",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892af0",
      "incomplete_value": false,
      "site": "00892af4",
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
            "const:a88:8"
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
      "00892b38",
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892b38",
      "DATA",
      [
        "storage",
        "00c81e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892aec.md#insn-00892af0)
- 新版 [`00892b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b30.md#insn-00892b34)

~~~diff
- 00892af0 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00892af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892b34 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 00892b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892af0 bytes 08212a91
+ 00892b34 bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f40bcb1b382d4337cdc8630a8bde5b8"></a>

### [`00892b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b04.md) → [`00892b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b48.md) FUN_00892b48

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00892b6c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892b28",
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
      "00892b6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00892b6c",
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

- 旧版 [`00892b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b04.md#insn-00892b28) · [`00892b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b04.md#insn-00892b34)
- 新版 [`00892b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b48.md#insn-00892b6c) · [`00892b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b48.md#insn-00892b78)

~~~diff
- 00892b28 ["INT_ADD", "register:40f0:8", ["const:892b28:8", "const:4:8"]]
- 00892b28 ["CALL", null, ["ram:47acb4:8"]]
+ 00892b6c ["INT_ADD", "register:40f0:8", ["const:892b6c:8", "const:4:8"]]
+ 00892b6c ["CALL", null, ["ram:47acf4:8"]]
- 00892b28 bytes 63a0ef97
+ 00892b6c bytes 62a0ef97
- 00892b34 ["INT_ADD", "register:40f0:8", ["const:892b34:8", "const:4:8"]]
- 00892b34 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00892b78 ["INT_ADD", "register:40f0:8", ["const:892b78:8", "const:4:8"]]
+ 00892b78 ["CALL", null, ["callee:0047cdd4:8"]]
- 00892b34 bytes 98a8ef97
+ 00892b78 bytes 97a8ef97
~~~


<a id="compare-19dad69397f1bf44582b8fe5fac6885a"></a>

### [`00892b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b78.md) → [`00892bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892bbc.md) FUN_00892bbc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892bd0",
      "incomplete_value": false,
      "site": "00892bd4",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892b8c",
      "incomplete_value": false,
      "site": "00892b90",
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
            "const:b28:8"
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
      "00892bd4",
      "DATA",
      [
        "storage",
        "00c81b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892bd4",
      "DATA",
      [
        "storage",
        "00c81f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b78.md#insn-00892b84) · [`00892b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892b78.md#insn-00892b8c)
- 新版 [`00892bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892bbc.md#insn-00892bc8) · [`00892bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892bbc.md#insn-00892bd0)

~~~diff
- 00892b84 ["INT_ADD", "register:40f0:8", ["const:892b84:8", "const:4:8"]]
- 00892b84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00892bc8 ["INT_ADD", "register:40f0:8", ["const:892bc8:8", "const:4:8"]]
+ 00892bc8 ["CALL", null, ["callee:00c57e90:8"]]
- 00892b84 bytes c3130f94
+ 00892bc8 bytes b2140f94
- 00892b8c ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00892b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892bd0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00892bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892b8c bytes 08a12c91
+ 00892bd0 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a09a0eeda9ccf9a5bdfc8818d11858c"></a>

### [`00892c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c54.md) → [`00892c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c98.md) FUN_00892c98

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00892cbc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892c78",
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
      "00892cbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00892cbc",
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

- 旧版 [`00892c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c54.md#insn-00892c78) · [`00892c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c54.md#insn-00892c84)
- 新版 [`00892cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c98.md#insn-00892cbc) · [`00892cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c98.md#insn-00892cc8)

~~~diff
- 00892c78 ["INT_ADD", "register:40f0:8", ["const:892c78:8", "const:4:8"]]
- 00892c78 ["CALL", null, ["ram:47acb4:8"]]
+ 00892cbc ["INT_ADD", "register:40f0:8", ["const:892cbc:8", "const:4:8"]]
+ 00892cbc ["CALL", null, ["ram:47acf4:8"]]
- 00892c78 bytes 0fa0ef97
+ 00892cbc bytes 0ea0ef97
- 00892c84 ["INT_ADD", "register:40f0:8", ["const:892c84:8", "const:4:8"]]
- 00892c84 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00892cc8 ["INT_ADD", "register:40f0:8", ["const:892cc8:8", "const:4:8"]]
+ 00892cc8 ["CALL", null, ["callee:0047cdd4:8"]]
- 00892c84 bytes 44a8ef97
+ 00892cc8 bytes 43a8ef97
~~~


<a id="compare-9464c52e7be44b65bb2e255c691b7cf7"></a>

### [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) → [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md) FUN_00892d08

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`008912c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008912c0.md) [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`00892e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) [`00893108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) [`00893258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 7件 [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) [`00892eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892eac.md) [`0089314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md) [`0089329c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089329c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00892d14",
      "incomplete_value": false,
      "site": "00892d18",
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
      "definition_site": "00892cd0",
      "incomplete_value": false,
      "site": "00892cd4",
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
      "00892d14",
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
      "00892d14",
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

- 旧版 [`00892cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md#insn-00892cd4) · [`00892cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md#insn-00892cd0)
- 新版 [`00892d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md#insn-00892d18) · [`00892d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md#insn-00892d14)

~~~diff
- 00892cd4 ["INT_ADD", "register:40f0:8", ["const:892cd4:8", "const:4:8"]]
- 00892cd4 ["CALL", null, ["callee:00442930:8"]]
+ 00892d18 ["INT_ADD", "register:40f0:8", ["const:892d18:8", "const:4:8"]]
+ 00892d18 ["CALL", null, ["callee:00442930:8"]]
- 00892cd4 bytes 07bfee97
+ 00892d18 bytes 06bfee97
- 00892cd0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00892cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00892cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00892cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00892d14 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00892d14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00892d14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00892d14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00892cd0 bytes 00303c91
+ 00892d14 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca4f037292eb7dd85631be3f64403e35"></a>

### [`00892cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cd8.md) → [`00892d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d1c.md) FUN_00892d1c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892d24",
      "incomplete_value": false,
      "site": "00892d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892ce0",
      "incomplete_value": false,
      "site": "00892ce4",
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
            "const:c28:8"
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
      "00892d28",
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892d28",
      "DATA",
      [
        "storage",
        "00c82028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cd8.md#insn-00892cdc) · [`00892ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cd8.md#insn-00892ce0)
- 新版 [`00892d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d1c.md#insn-00892d20) · [`00892d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d1c.md#insn-00892d24)

~~~diff
- 00892cdc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892d20 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00892cdc bytes 691f00f0
+ 00892d20 bytes 891f0090
- 00892ce0 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00892ce0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892ce0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892ce0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00892d24 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00892d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00892d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00892d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892ce0 bytes 29a13091
+ 00892d24 bytes 29a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec8e381219fb67602f4d1a4406561bb0"></a>

### [`00892cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cf8.md) → [`00892d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d3c.md) FUN_00892d3c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892d44",
      "incomplete_value": false,
      "site": "00892d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892d00",
      "incomplete_value": false,
      "site": "00892d04",
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
            "const:c28:8"
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
      "00892d48",
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892d48",
      "DATA",
      [
        "storage",
        "00c82028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cf8.md#insn-00892cfc) · [`00892d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cf8.md#insn-00892d00) · [`00892d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cf8.md#insn-00892d24)
- 新版 [`00892d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d3c.md#insn-00892d40) · [`00892d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d3c.md#insn-00892d44) · [`00892d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d3c.md#insn-00892d68)

~~~diff
- 00892cfc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892d40 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00892cfc bytes 691f00f0
+ 00892d40 bytes 891f0090
- 00892d00 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00892d00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892d00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892d00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00892d44 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00892d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00892d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00892d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892d00 bytes 29a13091
+ 00892d44 bytes 29a10091
- 00892d24 ["INT_ADD", "register:40f0:8", ["const:892d24:8", "const:4:8"]]
- 00892d24 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00892d68 ["INT_ADD", "register:40f0:8", ["const:892d68:8", "const:4:8"]]
+ 00892d68 ["CALL", null, ["callee:00c57eb0:8"]]
- 00892d24 bytes 63130f94
+ 00892d68 bytes 52140f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e11f85d304930bee3dd03fb402a5457b"></a>

### [`00892d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892d38.md) → [`00892d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d7c.md) FUN_00892d7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00892dac",
      "incomplete_value": false,
      "site": "00892dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892d68",
      "incomplete_value": false,
      "site": "00892d68",
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
            "const:c28:8"
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
      "00892dac",
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892dac",
      "DATA",
      [
        "storage",
        "00c82028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892d38.md#insn-00892d4c) · [`00892d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892d38.md#insn-00892d58) · [`00892d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892d38.md#insn-00892d5c)
- 新版 [`00892d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d7c.md#insn-00892d90) · [`00892d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d7c.md#insn-00892d9c) · [`00892da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d7c.md#insn-00892da0)

~~~diff
- 00892d4c ["INT_ADD", "register:40f0:8", ["const:892d4c:8", "const:4:8"]]
- 00892d4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00892d90 ["INT_ADD", "register:40f0:8", ["const:892d90:8", "const:4:8"]]
+ 00892d90 ["CALL", null, ["callee:00c57e90:8"]]
- 00892d4c bytes 51130f94
+ 00892d90 bytes 40140f94
- 00892d58 ["COPY", "register:4058:8", ["const:c81000:8"]]
+ 00892d9c ["COPY", "register:4058:8", ["const:c82000:8"]]
- 00892d58 bytes 6b1f00f0
+ 00892d9c bytes 8b1f0090
- 00892d5c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00892d5c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00892d5c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00892d5c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00892da0 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00892da0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00892da0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00892da0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00892d5c bytes 6ba13091
+ 00892da0 bytes 6ba10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0028ae050d627cf7812c357471b90cb5"></a>

### [`00892dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892dbc.md) → [`00892e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892e00.md) FUN_00892e00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "00892e20",
      "incomplete_value": false,
      "site": "00892e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892ddc",
      "incomplete_value": false,
      "site": "00892ddc",
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
            "const:c28:8"
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
      "00892e20",
      "DATA",
      [
        "storage",
        "00c81c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892e20",
      "DATA",
      [
        "storage",
        "00c82028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892dbc.md#insn-00892dcc) · [`00892dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892dbc.md#insn-00892dd0) · [`00892dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892dbc.md#insn-00892dd8)
- 新版 [`00892e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892e00.md#insn-00892e10) · [`00892e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892e00.md#insn-00892e14)

~~~diff
- 00892dcc ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00892e10 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00892dcc bytes 691f00f0
+ 00892e10 bytes 891f0090
- 00892dd0 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00892dd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892dd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892dd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00892e14 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00892e14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00892e14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00892e14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892dd0 bytes 29a13091
+ 00892e14 bytes 29a10091
- 00892dd8 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00892dd8 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e46c417a65abb8f7696ee3f7dcc899"></a>

### [`00892e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md) → [`00892eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892eac.md) FUN_00892eac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.24% / 新版 92.24%

CFGの説明率　旧版 63.27% / 新版 65.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892e70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00892e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00892e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893028",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008930c4"
      ]
    ]
  ],
  "added": [
    [
      "00892eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00892eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0089306c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008930c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md#insn-00892e6c) · [`00892e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md#insn-00892e70) · [`00892eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892e68.md#insn-00892eb0)
- 新版 [`00892ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892eac.md#insn-00892ef4)

~~~diff
- 00892e6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00892e6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00892e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00892e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00892e6c bytes fd7b04a9
- 00892e70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00892e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00892e70 bytes fb2b00f9
- 00892eb0 ["CBRANCH", null, ["local:b28:8", "register:101:1"]]
+ 00892ef4 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00892eb0 bytes e0090054
+ 00892ef4 bytes e0090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1feda27f23d17f5282c7a39c45daf7"></a>

### [`008930b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930b0.md) → [`008930f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008930f4.md) FUN_008930f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893114",
      "incomplete_value": false,
      "site": "00893118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008930d0",
      "incomplete_value": false,
      "site": "008930d4",
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
            "const:ca8:8"
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
      "00893118",
      "DATA",
      [
        "storage",
        "00c81ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893118",
      "DATA",
      [
        "storage",
        "00c820a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008930c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930b0.md#insn-008930c4) · [`008930cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930b0.md#insn-008930cc) · [`008930d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930b0.md#insn-008930d0)
- 新版 [`00893108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008930f4.md#insn-00893108) · [`00893110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008930f4.md#insn-00893110) · [`00893114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008930f4.md#insn-00893114)

~~~diff
- 008930c4 ["INT_ADD", "register:40f0:8", ["const:8930c4:8", "const:4:8"]]
- 008930c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00893108 ["INT_ADD", "register:40f0:8", ["const:893108:8", "const:4:8"]]
+ 00893108 ["CALL", null, ["callee:00c57e90:8"]]
- 008930c4 bytes 73120f94
+ 00893108 bytes 62130f94
- 008930cc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893110 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008930cc bytes 681f00d0
+ 00893110 bytes 681f00f0
- 008930d0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 008930d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008930d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008930d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893114 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00893114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008930d0 bytes 08a13291
+ 00893114 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d533cea0b84431de2420be5fbdce2e91"></a>

### [`008930e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930e8.md) → [`0089312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089312c.md) FUN_0089312c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893130",
      "incomplete_value": false,
      "site": "00893134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008930ec",
      "incomplete_value": false,
      "site": "008930f0",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008930f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0089313c"
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
      "00893134",
      "DATA",
      [
        "storage",
        "00c81ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893134",
      "DATA",
      [
        "storage",
        "00c820a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008930f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930e8.md#insn-008930f8) · [`008930e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008930e8.md#insn-008930e8)
- 新版 [`0089313c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089312c.md#insn-0089313c) · [`0089312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089312c.md#insn-0089312c)

~~~diff
- 008930f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 008930f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008930f8 bytes 2080803c
+ 0089313c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
+ 0089313c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 0089313c bytes 2080803c
- 008930e8 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089312c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008930e8 bytes 681f00d0
+ 0089312c bytes 681f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c41a8be556051ba3a21a188e4f32aff"></a>

### [`00893108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) → [`0089314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md) FUN_0089314c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00891b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md) [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 57.14% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008931b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008931fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00893168",
      "incomplete_value": false,
      "site": "0089316c",
      "value": [
        "leaf",
        "const:2:8"
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00893128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md#insn-00893128) · [`0089316c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md#insn-0089316c) · [`008931b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md#insn-008931b8)
- 新版 [`0089316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md#insn-0089316c) · [`008931b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md#insn-008931b0)

~~~diff
- 00893128 ["INT_ADD", "register:40f0:8", ["const:893128:8", "const:4:8"]]
- 00893128 ["CALL", null, ["callee:00b39614:8"]]
+ 0089316c ["INT_ADD", "register:40f0:8", ["const:89316c:8", "const:4:8"]]
+ 0089316c ["CALL", null, ["callee:00b39614:8"]]
- 00893128 bytes 31980a94
+ 0089316c bytes 2a990a94
- 0089316c ["INT_ADD", "register:40f0:8", ["const:89316c:8", "const:4:8"]]
- 0089316c ["CALL", null, ["callee:00891b6c:8"]]
+ 008931b0 ["INT_ADD", "register:40f0:8", ["const:8931b0:8", "const:4:8"]]
+ 008931b0 ["CALL", null, ["callee:00891b6c:8"]]
- 0089316c bytes 6ffaff97
+ 008931b0 bytes 6ffaff97
- 008931b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 008931b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 008931b8 bytes 001100fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1cc3336fc0881fb9801cb8cf20bb7b7"></a>

### [`00893238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893238.md) → [`0089327c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089327c.md) FUN_0089327c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893280",
      "incomplete_value": false,
      "site": "00893284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089323c",
      "incomplete_value": false,
      "site": "00893240",
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
            "const:d28:8"
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
      "00893284",
      "DATA",
      [
        "storage",
        "00c81d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893284",
      "DATA",
      [
        "storage",
        "00c82128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893238.md#insn-00893238) · [`0089323c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893238.md#insn-0089323c)
- 新版 [`0089327c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089327c.md#insn-0089327c) · [`00893280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089327c.md#insn-00893280)

~~~diff
- 00893238 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089327c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00893238 bytes 681f00d0
+ 0089327c bytes 681f00f0
- 0089323c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0089323c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089323c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089323c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893280 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 00893280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089323c bytes 08a13491
+ 00893280 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01c49357739798d6b7fdfcca034e754f"></a>

### [`00893258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md) → [`0089329c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089329c.md) FUN_0089329c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00891b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891b28.md) [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00891b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md) [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 40.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893258"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893258"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089325c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00893258",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089325c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008932e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089335c"
      ]
    ]
  ],
  "added": [
    [
      "0089329c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008932a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00893324",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089335c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md#insn-00893258) · [`0089325c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md#insn-0089325c) · [`0089329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893258.md#insn-0089329c)
- 新版 [`008932e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089329c.md#insn-008932e0)

~~~diff
- 00893258 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00893258 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00893258 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00893258 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00893258 bytes fd7bbea9
- 0089325c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0089325c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0089325c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0089325c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089325c bytes f44f01a9
- 0089329c ["INT_ADD", "register:40f0:8", ["const:89329c:8", "const:4:8"]]
- 0089329c ["CALL", null, ["callee:008bb510:8"]]
+ 008932e0 ["INT_ADD", "register:40f0:8", ["const:8932e0:8", "const:4:8"]]
+ 008932e0 ["CALL", null, ["callee:008bb510:8"]]
- 0089329c bytes 8ca00094
+ 008932e0 bytes 8ca00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0750929ed828adfb78d7feb1a9d3b63"></a>

### [`00893384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893384.md) → [`008933c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008933c8.md) FUN_008933c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008933cc",
      "incomplete_value": false,
      "site": "008933d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893388",
      "incomplete_value": false,
      "site": "0089338c",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008933d8"
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
      "008933d0",
      "DATA",
      [
        "storage",
        "00c81da8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008933d0",
      "DATA",
      [
        "storage",
        "00c821a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893384.md#insn-00893394) · [`00893384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893384.md#insn-00893384)
- 新版 [`008933d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008933c8.md#insn-008933d8) · [`008933c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008933c8.md#insn-008933c8)

~~~diff
- 00893394 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00893394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00893394 bytes 2080803c
+ 008933d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
+ 008933d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 008933d8 bytes 2080803c
- 00893384 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008933c8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00893384 bytes 681f00d0
+ 008933c8 bytes 681f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1e5ae88999ef8cf07787306e20874f"></a>

### [`00893448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893448.md) → [`0089348c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089348c.md) FUN_0089348c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008934a0",
      "incomplete_value": false,
      "site": "008934a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089345c",
      "incomplete_value": false,
      "site": "00893460",
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
            "const:e28:8"
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
      "008934a4",
      "DATA",
      [
        "storage",
        "00c81e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008934a4",
      "DATA",
      [
        "storage",
        "00c82228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893448.md#insn-00893454) · [`00893458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893448.md#insn-00893458) · [`0089345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893448.md#insn-0089345c)
- 新版 [`00893498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089348c.md#insn-00893498) · [`0089349c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089348c.md#insn-0089349c) · [`008934a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089348c.md#insn-008934a0)

~~~diff
- 00893454 ["INT_ADD", "register:40f0:8", ["const:893454:8", "const:4:8"]]
- 00893454 ["CALL", null, ["callee:00c57e90:8"]]
+ 00893498 ["INT_ADD", "register:40f0:8", ["const:893498:8", "const:4:8"]]
+ 00893498 ["CALL", null, ["callee:00c57e90:8"]]
- 00893454 bytes 8f110f94
+ 00893498 bytes 7e120f94
- 00893458 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0089349c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00893458 bytes 681f00d0
+ 0089349c bytes 681f00f0
- 0089345c ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0089345c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089345c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089345c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008934a0 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 008934a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008934a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008934a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089345c bytes 08a13891
+ 008934a0 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-493652028f0c604916aab85c47fa882f"></a>

### [`0089346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089346c.md) → [`008934b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934b0.md) FUN_008934b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008934b4",
      "incomplete_value": false,
      "site": "008934b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893470",
      "incomplete_value": false,
      "site": "00893474",
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
            "const:e28:8"
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
      "008934b8",
      "DATA",
      [
        "storage",
        "00c81e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008934b8",
      "DATA",
      [
        "storage",
        "00c82228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089346c.md#insn-0089346c) · [`00893470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089346c.md#insn-00893470)
- 新版 [`008934b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934b0.md#insn-008934b0) · [`008934b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934b0.md#insn-008934b4)

~~~diff
- 0089346c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008934b0 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0089346c bytes 681f00d0
+ 008934b0 bytes 681f00f0
- 00893470 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00893470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00893470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00893470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008934b4 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 008934b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008934b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008934b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00893470 bytes 08a13891
+ 008934b4 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51fb12934b212b1bdc0f6058cb3f60c0"></a>

### [`008934b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934b4.md) → [`008934f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934f8.md) FUN_008934f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893518",
      "incomplete_value": false,
      "site": "0089351c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008934d4",
      "incomplete_value": false,
      "site": "008934d8",
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
            "const:ea8:8"
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
      "0089351c",
      "DATA",
      [
        "storage",
        "00c81ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089351c",
      "DATA",
      [
        "storage",
        "00c822a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008934c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934b4.md#insn-008934c8) · [`008934d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934b4.md#insn-008934d0) · [`008934d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934b4.md#insn-008934d4)
- 新版 [`0089350c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934f8.md#insn-0089350c) · [`00893514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934f8.md#insn-00893514) · [`00893518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008934f8.md#insn-00893518)

~~~diff
- 008934c8 ["INT_ADD", "register:40f0:8", ["const:8934c8:8", "const:4:8"]]
- 008934c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0089350c ["INT_ADD", "register:40f0:8", ["const:89350c:8", "const:4:8"]]
+ 0089350c ["CALL", null, ["callee:00c57e90:8"]]
- 008934c8 bytes 72110f94
+ 0089350c bytes 61120f94
- 008934d0 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893514 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008934d0 bytes 681f00d0
+ 00893514 bytes 681f00f0
- 008934d4 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 008934d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008934d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008934d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893518 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00893518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008934d4 bytes 08a13a91
+ 00893518 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeabe7ff855241d248f5d3d96939f3c9"></a>

### [`008934ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934ec.md) → [`00893530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893530.md) FUN_00893530

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893534",
      "incomplete_value": false,
      "site": "00893538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008934f0",
      "incomplete_value": false,
      "site": "008934f4",
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
            "const:ea8:8"
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
      "00893538",
      "DATA",
      [
        "storage",
        "00c81ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893538",
      "DATA",
      [
        "storage",
        "00c822a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008934ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934ec.md#insn-008934ec) · [`008934f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/008934ec.md#insn-008934f0)
- 新版 [`00893530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893530.md#insn-00893530) · [`00893534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893530.md#insn-00893534)

~~~diff
- 008934ec ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893530 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008934ec bytes 681f00d0
+ 00893530 bytes 681f00f0
- 008934f0 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 008934f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008934f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008934f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893534 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 00893534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008934f0 bytes 08a13a91
+ 00893534 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2cdb02256f2a908365da032a35153b6"></a>

### [`0089350c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md) → [`00893550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893550.md) FUN_00893550

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde0.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`00892cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892cc4.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce20.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`00892d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892d08.md)

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
      "site": "00893580",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0089353c",
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
      "site": "0089358c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00893548",
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
      "00893580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0089358c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00893580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0089358c",
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

- 旧版 [`0089353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md#insn-0089353c) · [`00893548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md#insn-00893548) · [`00893540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089350c.md#insn-00893540)
- 新版 [`00893580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893550.md#insn-00893580) · [`0089358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893550.md#insn-0089358c) · [`00893584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893550.md#insn-00893584)

~~~diff
- 0089353c ["INT_ADD", "register:40f0:8", ["const:89353c:8", "const:4:8"]]
- 0089353c ["CALL", null, ["ram:47acb4:8"]]
+ 00893580 ["INT_ADD", "register:40f0:8", ["const:893580:8", "const:4:8"]]
+ 00893580 ["CALL", null, ["ram:47acf4:8"]]
- 0089353c bytes de9def97
+ 00893580 bytes dd9def97
- 00893548 ["INT_ADD", "register:40f0:8", ["const:893548:8", "const:4:8"]]
- 00893548 ["CALL", null, ["ram:47acb4:8"]]
+ 0089358c ["INT_ADD", "register:40f0:8", ["const:89358c:8", "const:4:8"]]
+ 0089358c ["CALL", null, ["ram:47acf4:8"]]
- 00893548 bytes db9def97
+ 0089358c bytes da9def97
- 00893540 ["INT_ADD", "register:40f0:8", ["const:893540:8", "const:4:8"]]
- 00893540 ["CALL", null, ["callee:0047ce20:8"]]
+ 00893584 ["INT_ADD", "register:40f0:8", ["const:893584:8", "const:4:8"]]
+ 00893584 ["CALL", null, ["callee:0047ce20:8"]]
- 00893540 bytes 28a6ef97
+ 00893584 bytes 27a6ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c0a985ce4ef5105f3491db1d9594ce3"></a>

### [`00893588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893588.md) → [`008935cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008935cc.md) _INIT_167

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 63.04% / 新版 63.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008935b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008935e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008935b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008935c4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008935e0",
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
      "008935fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00893608",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00893624",
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

- 旧版 [`008935b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893588.md#insn-008935b8) · [`008935e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893588.md#insn-008935e0)
- 新版 [`008935fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008935cc.md#insn-008935fc)

~~~diff
- 008935b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008935b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008935b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008935b8 bytes a9831ff8
- 008935e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008935e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008935e0 bytes e013813c
+ 008935fc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008935fc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 008935fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008935fc bytes a9831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42888d689f88334b737369e6798c8528"></a>

### [`00893918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893918.md) → [`0089395c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089395c.md) FUN_0089395c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde0.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`0083f244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f244.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce20.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0083f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f284.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

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
      "site": "008939b0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0089396c",
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
      "site": "008939bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00893978",
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
      "008939b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008939bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008939b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008939bc",
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

- 旧版 [`0089396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893918.md#insn-0089396c) · [`00893978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893918.md#insn-00893978) · [`00893920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893918.md#insn-00893920)
- 新版 [`008939b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089395c.md#insn-008939b0) · [`008939bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089395c.md#insn-008939bc) · [`00893964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089395c.md#insn-00893964)

~~~diff
- 0089396c ["INT_ADD", "register:40f0:8", ["const:89396c:8", "const:4:8"]]
- 0089396c ["CALL", null, ["ram:47acb4:8"]]
+ 008939b0 ["INT_ADD", "register:40f0:8", ["const:8939b0:8", "const:4:8"]]
+ 008939b0 ["CALL", null, ["ram:47acf4:8"]]
- 0089396c bytes d29cef97
+ 008939b0 bytes d19cef97
- 00893978 ["INT_ADD", "register:40f0:8", ["const:893978:8", "const:4:8"]]
- 00893978 ["CALL", null, ["ram:47acb4:8"]]
+ 008939bc ["INT_ADD", "register:40f0:8", ["const:8939bc:8", "const:4:8"]]
+ 008939bc ["CALL", null, ["ram:47acf4:8"]]
- 00893978 bytes cf9cef97
+ 008939bc bytes ce9cef97
- 00893920 ["INT_ADD", "register:40f0:8", ["const:893920:8", "const:4:8"]]
- 00893920 ["CALL", null, ["callee:008514f8:8"]]
+ 00893964 ["INT_ADD", "register:40f0:8", ["const:893964:8", "const:4:8"]]
+ 00893964 ["CALL", null, ["callee:008514f8:8"]]
- 00893920 bytes e6f6fe97
+ 00893964 bytes e5f6fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-581e5f35708363136ccc9782988b937d"></a>

### [`0089398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md) → [`008939d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008939d0.md) FUN_008939d0

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md) [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.65% / 新版 82.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00893ac0",
      "incomplete_value": true,
      "site": "00893ad0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893a7c",
      "incomplete_value": true,
      "site": "00893a8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a27:8"
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
      "definition_site": "00893ac4",
      "incomplete_value": true,
      "site": "00893ad8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00893a80",
      "incomplete_value": true,
      "site": "00893a94",
      "value": [
        "LOAD",
        "16",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00893ad4",
      "incomplete_value": true,
      "site": "00893ae4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00893a90",
      "incomplete_value": true,
      "site": "00893aa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b10:8"
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
      "00893a10",
      "DATA",
      [
        "storage",
        "002f3db2",
        "switchD_008939d4::switchdataD_002f3db2",
        "byte"
      ]
    ],
    [
      "00893a1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00893a40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00893a10",
      "DATA",
      [
        "storage",
        "002f3df2",
        "switchD_00893a18::switchdataD_002f3df2",
        "byte"
      ]
    ],
    [
      "00893a1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00893a40",
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

- 旧版 [`008939d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md#insn-008939d8) · [`008939fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md#insn-008939fc) · [`00893a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089398c.md#insn-00893a10)
- 新版 [`00893a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008939d0.md#insn-00893a1c) · [`00893a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008939d0.md#insn-00893a40) · [`00893a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/008939d0.md#insn-00893a54)

~~~diff
- 008939d8 ["INT_ADD", "register:40f0:8", ["const:8939d8:8", "const:4:8"]]
- 008939d8 ["CALL", null, ["ram:48ccb8:8"]]
+ 00893a1c ["INT_ADD", "register:40f0:8", ["const:893a1c:8", "const:4:8"]]
+ 00893a1c ["CALL", null, ["ram:48ccf8:8"]]
- 008939d8 bytes b8e4ef97
+ 00893a1c bytes b7e4ef97
- 008939fc ["INT_ADD", "register:40f0:8", ["const:8939fc:8", "const:4:8"]]
- 008939fc ["CALL", null, ["ram:48ccb8:8"]]
+ 00893a40 ["INT_ADD", "register:40f0:8", ["const:893a40:8", "const:4:8"]]
+ 00893a40 ["CALL", null, ["ram:48ccf8:8"]]
- 008939fc bytes afe4ef97
+ 00893a40 bytes aee4ef97
- 00893a10 ["INT_ADD", "register:40f0:8", ["const:893a10:8", "const:4:8"]]
- 00893a10 ["CALL", null, ["ram:48ccb8:8"]]
+ 00893a54 ["INT_ADD", "register:40f0:8", ["const:893a54:8", "const:4:8"]]
+ 00893a54 ["CALL", null, ["ram:48ccf8:8"]]
- 00893a10 bytes aae4ef97
+ 00893a54 bytes a9e4ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a274313157e9f4bda4b86402deaaa951"></a>

### [`00893b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md) → [`00893b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893b84.md) FUN_00893b84

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) · 呼出先 14件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 14件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.39% / 新版 82.39%

CFGの説明率　旧版 69.05% / 新版 72.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00893cd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00893cb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00893bbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00893bc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00893bd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00893bbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00893bc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00893bd8",
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

- 旧版 [`00893b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md#insn-00893b50) · [`00893b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md#insn-00893b78) · [`00893b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md#insn-00893b84)
- 新版 [`00893b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893b84.md#insn-00893b94) · [`00893bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893b84.md#insn-00893bbc) · [`00893bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893b84.md#insn-00893bc8)

~~~diff
- 00893b50 ["INT_ADD", "register:40f0:8", ["const:893b50:8", "const:4:8"]]
- 00893b50 ["CALL", null, ["callee:008514f8:8"]]
+ 00893b94 ["INT_ADD", "register:40f0:8", ["const:893b94:8", "const:4:8"]]
+ 00893b94 ["CALL", null, ["callee:008514f8:8"]]
- 00893b50 bytes 5af6fe97
+ 00893b94 bytes 59f6fe97
- 00893b78 ["INT_ADD", "register:40f0:8", ["const:893b78:8", "const:4:8"]]
- 00893b78 ["CALL", null, ["ram:48ccb8:8"]]
+ 00893bbc ["INT_ADD", "register:40f0:8", ["const:893bbc:8", "const:4:8"]]
+ 00893bbc ["CALL", null, ["ram:48ccf8:8"]]
- 00893b78 bytes 50e4ef97
+ 00893bbc bytes 4fe4ef97
- 00893b84 ["INT_ADD", "register:40f0:8", ["const:893b84:8", "const:4:8"]]
- 00893b84 ["CALL", null, ["ram:47acb4:8"]]
+ 00893bc8 ["INT_ADD", "register:40f0:8", ["const:893bc8:8", "const:4:8"]]
+ 00893bc8 ["CALL", null, ["ram:47acf4:8"]]
- 00893b84 bytes 4c9cef97
+ 00893bc8 bytes 4b9cef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e628b09de9943ab5dd2246463a8c6a2"></a>

### [`00893d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md) → [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) FUN_00893dbc

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 53件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f394.md) [`0043f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md)
- 新版 呼出元 0件  · 呼出先 53件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f3d4.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.95% / 新版 55.95%

CFGの説明率　旧版 26.82% / 新版 27.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `call_target` 6件, `store_value` 6件, `unresolved_branch_alignment` 64件, `unresolved_call_alignment` 167件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00893edc",
      "incomplete_value": true,
      "site": "00893edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893e98",
      "incomplete_value": true,
      "site": "00893e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c22:8"
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
      "definition_site": "00893f24",
      "incomplete_value": true,
      "site": "00893f30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:550:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893ee0",
      "incomplete_value": true,
      "site": "00893eec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
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
      "definition_site": "00893f20",
      "incomplete_value": true,
      "site": "00893f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:743:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00893edc",
      "incomplete_value": true,
      "site": "00893ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:703:8"
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
      "00893e9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00893fd8"
      ]
    ],
    [
      "00893ecc",
      "READ",
      [
        "storage",
        "002bcc22",
        null,
        "string"
      ]
    ],
    [
      "00893f04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00893e9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089401c"
      ]
    ],
    [
      "00893ecc",
      "READ",
      [
        "storage",
        "002bcc62",
        null,
        "string"
      ]
    ],
    [
      "00893f04",
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

- 旧版 [`00893ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md#insn-00893ec0) · [`00893f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md#insn-00893f1c) · [`00893f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893d78.md#insn-00893f34)
- 新版 [`00893f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md#insn-00893f04) · [`00893f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md#insn-00893f60) · [`00893f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md#insn-00893f78)

~~~diff
- 00893ec0 ["INT_ADD", "register:40f0:8", ["const:893ec0:8", "const:4:8"]]
- 00893ec0 ["CALL", null, ["ram:48ccb8:8"]]
+ 00893f04 ["INT_ADD", "register:40f0:8", ["const:893f04:8", "const:4:8"]]
+ 00893f04 ["CALL", null, ["ram:48ccf8:8"]]
- 00893ec0 bytes 7ee3ef97
+ 00893f04 bytes 7de3ef97
- 00893f1c ["INT_ADD", "register:40f0:8", ["const:893f1c:8", "const:4:8"]]
- 00893f1c ["CALL", null, ["callee:00492ce8:8"]]
+ 00893f60 ["INT_ADD", "register:40f0:8", ["const:893f60:8", "const:4:8"]]
+ 00893f60 ["CALL", null, ["callee:00492ce8:8"]]
- 00893f1c bytes 63fbef97
+ 00893f60 bytes 62fbef97
- 00893f34 ["BRANCH", null, ["local:b96:8"]]
+ 00893f78 ["BRANCH", null, ["local:b94:8"]]
- 00893f34 bytes 69010014
+ 00893f78 bytes 69010014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e59398ad5442248c773dc410579ab0"></a>

### [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) → [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) FUN_008959d0

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 99件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md)
- 新版 呼出元 0件  · 呼出先 99件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.87% / 新版 56.87%

CFGの説明率　旧版 32.59% / 新版 32.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 7件, `store_value` 5件, `unresolved_branch_alignment` 73件, `unresolved_call_alignment` 128件, `unresolved_store_alignment` 51件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00895a30",
      "incomplete_value": true,
      "site": "00895a30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008959ec",
      "incomplete_value": true,
      "site": "008959ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ec:8"
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
      "definition_site": "00895a34",
      "incomplete_value": true,
      "site": "00895a34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008959f0",
      "incomplete_value": true,
      "site": "008959f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00895a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00895a20",
      "READ",
      [
        "storage",
        "002a05ec",
        null,
        "string"
      ]
    ],
    [
      "00895a24",
      "READ",
      [
        "storage",
        "002a05f1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00895a38",
      "READ",
      [
        "storage",
        "002b7154",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00895a20",
      "READ",
      [
        "storage",
        "002a06b9",
        null,
        "string"
      ]
    ],
    [
      "00895a24",
      "READ",
      [
        "storage",
        "002a06be",
        null,
        "string"
      ]
    ],
    [
      "00895a7c",
      "READ",
      [
        "storage",
        "002b7194",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00895a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md#insn-00895a00) · [`00895a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md#insn-00895a30) · [`00895a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md#insn-00895a34)
- 新版 [`00895a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md#insn-00895a44)

~~~diff
- 00895a00 ["INT_ADD", "register:40f0:8", ["const:895a00:8", "const:4:8"]]
- 00895a00 ["CALL", null, ["callee:0048e0b8:8"]]
+ 00895a44 ["INT_ADD", "register:40f0:8", ["const:895a44:8", "const:4:8"]]
+ 00895a44 ["CALL", null, ["callee:0048e0b8:8"]]
- 00895a00 bytes 9ee1ef97
+ 00895a44 bytes 9de1ef97
- 00895a30 ["COPY", "tmp:0:8", ["const:154:8"]]
- 00895a30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00895a30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00895a30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00895a30 bytes 29510591
- 00895a34 ["COPY", "register:4040:8", ["const:20:8"]]
- 00895a34 bytes 08048052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00ffcdef83676913ff63687c05b70cb3"></a>

### [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) → [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) FUN_0089b28c

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`0044b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b214.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`0044b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b254.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.02% / 新版 89.02%

CFGの説明率　旧版 39.81% / 新版 38.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089b560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089b678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089b688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0089b3f4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ],
    [
      "0089b408",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "qword"
      ]
    ],
    [
      "unmatched:0089b3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089bc88"
      ]
    ]
  ],
  "added": [
    [
      "0089b3f4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ],
    [
      "0089b408",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "dword"
      ]
    ],
    [
      "0089b418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089bc88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md#insn-0089b394) · [`0089b3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md#insn-0089b3d4) · [`0089b3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md#insn-0089b3d8)
- 新版 [`0089b3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md#insn-0089b3d8)

~~~diff
- 0089b394 ["INT_ADD", "register:40f0:8", ["const:89b394:8", "const:4:8"]]
- 0089b394 ["CALL", null, ["callee:0069ec1c:8"]]
+ 0089b3d8 ["INT_ADD", "register:40f0:8", ["const:89b3d8:8", "const:4:8"]]
+ 0089b3d8 ["CALL", null, ["callee:0069ec1c:8"]]
- 0089b394 bytes 120ef897
+ 0089b3d8 bytes 110ef897
- 0089b3d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0089b3d4 ["CBRANCH", null, ["local:b137:8", "tmp:0:1"]]
- 0089b3d4 bytes 81430054
- 0089b3d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:c0:8"]]
- 0089b3d8 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 0089b3d8 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 0089b3d8 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 0089b3d8 bytes f44f4ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4087603184f514e8b8b820f4146a050"></a>

### [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) → [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) FUN_0089d4c8

採用 · 移動量 `+0x44` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 52件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00472b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b6c.md) [`00472b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472b7c.md) [`00472d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472d1c.md)
- 新版 呼出元 0件  · 呼出先 52件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00472bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bac.md) [`00472bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md) [`00472d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472d5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.09% / 新版 77.09%

CFGの説明率　旧版 59.32% / 新版 58.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 10件, `store_value` 6件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 30件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0089d5cc",
      "incomplete_value": true,
      "site": "0089d5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cdd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089d588",
      "incomplete_value": true,
      "site": "0089d588",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9d:8"
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
      "definition_site": "0089d700",
      "incomplete_value": true,
      "site": "0089d718",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089d6bc",
      "incomplete_value": true,
      "site": "0089d6d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d00:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089d77c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0089d5b8",
      "READ",
      [
        "storage",
        "002adc9d",
        null,
        "string"
      ]
    ],
    [
      "0089d6f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0089d700",
      "READ",
      [
        "storage",
        "002bcd00",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0089d5b8",
      "READ",
      [
        "storage",
        "002adcdd",
        null,
        "string"
      ]
    ],
    [
      "0089d6f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0089d700",
      "READ",
      [
        "storage",
        "002bcd40",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089d5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md#insn-0089d5cc) · [`0089d77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md#insn-0089d77c)
- 新版 [`0089d610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md#insn-0089d610) · [`0089d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md#insn-0089d7c0)

~~~diff
- 0089d5cc ["INT_ADD", "register:40f0:8", ["const:89d5cc:8", "const:4:8"]]
- 0089d5cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0089d610 ["INT_ADD", "register:40f0:8", ["const:89d610:8", "const:4:8"]]
+ 0089d610 ["CALL", null, ["callee:00c57eb0:8"]]
- 0089d5cc bytes 39e90e94
+ 0089d610 bytes 28ea0e94
- 0089d77c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0089d77c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:31:8"]]
- 0089d77c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0089d77c bytes e91303f8
+ 0089d7c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0089d7c0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:31:8"]]
+ 0089d7c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0089d7c0 bytes e91303f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2aa2c5751a875fcea04680ed7bb61d1"></a>

### [`008a3d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3d24.md) → [`008a3d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3d68.md) FUN_008a3d68

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 31.58% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008a3dfc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3dec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a3db8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3e08"
      ]
    ]
  ],
  "added": [
    [
      "008a3dfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3e08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a3d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3d24.md#insn-008a3d74) · [`008a3db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3d24.md#insn-008a3db8) · [`008a3dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3d24.md#insn-008a3dec)
- 新版 [`008a3db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3d68.md#insn-008a3db8)

~~~diff
- 008a3d74 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008a3d74 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 008a3db8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008a3db8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 008a3d74 bytes 2a030054
+ 008a3db8 bytes 2a030054
- 008a3db8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008a3db8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 008a3db8 bytes 680000b4
- 008a3dec ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a3dec ["RETURN", null, ["register:0:8"]]
- 008a3dec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef183ecee9b5ccd238934e05f0fd712e"></a>

### [`008a3e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3e1c.md) → [`008a3e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3e60.md) FUN_008a3e60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008b0b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0b54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008b0b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0b98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 36.84% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008a3f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a3f2c",
      "incomplete_value": true,
      "site": "008a3f38",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 8
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a3f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3fd0"
      ]
    ]
  ],
  "added": [
    [
      "008a3f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3fd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3e1c.md#insn-008a3ef4) · [`008a3f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3e1c.md#insn-008a3f04) · [`008a3f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3e1c.md#insn-008a3f24)
- 新版 [`008a3f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3e60.md#insn-008a3f38) · [`008a3f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3e60.md#insn-008a3f48)

~~~diff
- 008a3ef4 ["INT_ADD", "register:40f0:8", ["const:8a3ef4:8", "const:4:8"]]
- 008a3ef4 ["CALL", null, ["callee:008b0b98:8"]]
+ 008a3f38 ["INT_ADD", "register:40f0:8", ["const:8a3f38:8", "const:4:8"]]
+ 008a3f38 ["CALL", null, ["callee:008b0b98:8"]]
- 008a3ef4 bytes 18330094
+ 008a3f38 bytes 18330094
- 008a3f04 ["INT_ADD", "register:40f0:8", ["const:8a3f04:8", "const:4:8"]]
- 008a3f04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008a3f48 ["INT_ADD", "register:40f0:8", ["const:8a3f48:8", "const:4:8"]]
+ 008a3f48 ["CALL", null, ["callee:00c57eb0:8"]]
- 008a3f04 bytes ebce0e94
+ 008a3f48 bytes dacf0e94
- 008a3f24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008a3f24 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 008a3f24 bytes 41030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f28c1d2c56b0a59a2c524e1e9542c83"></a>

### [`008a3f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3f90.md) → [`008a3fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3fd4.md) FUN_008a3fd4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008b524c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b5/008b524c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008b5290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b5/008b5290.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 21.74% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a3f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a3f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a3f9c",
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
      "008a3fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008a3fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008a3fe0",
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

- 旧版 [`008a3f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3f90.md#insn-008a3f94) · [`008a3f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3f90.md#insn-008a3f98) · [`008a3f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3f90.md#insn-008a3f9c)

~~~diff
- 008a3f94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008a3f94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008a3f94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008a3f94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a3f94 bytes fd7b04a9
- 008a3f98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 008a3f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008a3f98 bytes f72b00f9
- 008a3f9c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008a3f9c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008a3f9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008a3f9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a3f9c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caf0f7fe0ffb9cd3924a1e3f97f8be3c"></a>

### [`008a40c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md) → [`008a4108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4108.md) FUN_008a4108

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/0089777c.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008977c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/008977c0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.39% / 新版 85.39%

CFGの説明率　旧版 25.00% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a40e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008a4144"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a416c",
      "incomplete_value": true,
      "site": "008a4174",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
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
      "unmatched:008a40e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4244"
      ]
    ],
    [
      "008a412c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a415c"
      ]
    ],
    [
      "unmatched:008a4160",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008a412c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4244"
      ]
    ],
    [
      "008a4144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a415c"
      ]
    ],
    [
      "008a41a4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a40e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md#insn-008a40e8) · [`008a411c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md#insn-008a411c) · [`008a4130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a40c4.md#insn-008a4130)
- 新版 [`008a4160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4108.md#insn-008a4160) · [`008a4174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4108.md#insn-008a4174)

~~~diff
- 008a40e8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 008a40e8 bytes c0080054
- 008a411c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 008a4160 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 008a411c bytes 40030054
+ 008a4160 bytes 40030054
- 008a4130 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a4130 ["INT_ADD", "register:40f0:8", ["const:8a4130:8", "const:4:8"]]
- 008a4130 ["CALLIND", null, ["register:0:8"]]
+ 008a4174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008a4174 ["INT_ADD", "register:40f0:8", ["const:8a4174:8", "const:4:8"]]
+ 008a4174 ["CALLIND", null, ["register:0:8"]]
- 008a4130 bytes 00013fd6
+ 008a4174 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822e2e4f51d18d964bdc034992e3aea3"></a>

### [`008a4230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4230.md) → [`008a4274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4274.md) FUN_008a4274

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a4288",
      "incomplete_value": false,
      "site": "008a428c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4244",
      "incomplete_value": false,
      "site": "008a4248",
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
      "008a428c",
      "DATA",
      [
        "storage",
        "00c81fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a428c",
      "DATA",
      [
        "storage",
        "00c823a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a423c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4230.md#insn-008a423c) · [`008a4240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4230.md#insn-008a4240) · [`008a4244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4230.md#insn-008a4244)
- 新版 [`008a4280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4274.md#insn-008a4280) · [`008a4284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4274.md#insn-008a4284) · [`008a4288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4274.md#insn-008a4288)

~~~diff
- 008a423c ["INT_ADD", "register:40f0:8", ["const:8a423c:8", "const:4:8"]]
- 008a423c ["CALL", null, ["callee:00c57e90:8"]]
+ 008a4280 ["INT_ADD", "register:40f0:8", ["const:8a4280:8", "const:4:8"]]
+ 008a4280 ["CALL", null, ["callee:00c57e90:8"]]
- 008a423c bytes 15ce0e94
+ 008a4280 bytes 04cf0e94
- 008a4240 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008a4284 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008a4240 bytes e81e00b0
+ 008a4284 bytes e81e00d0
- 008a4244 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 008a4244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a4244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a4244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a4288 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008a4288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a4244 bytes 08813e91
+ 008a4288 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a19d8cf21eb24357a657188c624594c"></a>

### [`008a4254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4254.md) → [`008a4298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4298.md) FUN_008a4298

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a429c",
      "incomplete_value": false,
      "site": "008a42a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4258",
      "incomplete_value": false,
      "site": "008a425c",
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
      "008a42a0",
      "DATA",
      [
        "storage",
        "00c81fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a42a0",
      "DATA",
      [
        "storage",
        "00c823a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4254.md#insn-008a4254) · [`008a4258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4254.md#insn-008a4258)
- 新版 [`008a4298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4298.md#insn-008a4298) · [`008a429c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4298.md#insn-008a429c)

~~~diff
- 008a4254 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008a4298 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008a4254 bytes e81e00b0
+ 008a4298 bytes e81e00d0
- 008a4258 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 008a4258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a4258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a4258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a429c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008a429c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a429c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a429c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a4258 bytes 08813e91
+ 008a429c bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a585412161e1c5f9b676da12db439dee"></a>

### [`008a426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a426c.md) → [`008a42b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a42b0.md) FUN_008a42b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`008a43a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a0.md) [`008a43a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a4.md) [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008a43e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43e4.md) [`008a43e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43e8.md) [`00b3a3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a3f0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 50.00% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a42c8",
      "incomplete_value": false,
      "site": "008a42d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4284",
      "incomplete_value": false,
      "site": "008a4294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a42dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008a4320"
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
      "008a42d8",
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ],
    [
      "008a430c",
      "READ",
      [
        "storage",
        "00c82030",
        null,
        "pointer"
      ]
    ],
    [
      "008a430c",
      "READ",
      [
        "storage",
        "00c82038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a42d8",
      "DATA",
      [
        "storage",
        "00c82410",
        null,
        "undefined *"
      ]
    ],
    [
      "008a430c",
      "READ",
      [
        "storage",
        "00c82430",
        null,
        "pointer"
      ]
    ],
    [
      "008a430c",
      "READ",
      [
        "storage",
        "00c82438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a42d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a426c.md#insn-008a42d8) · [`008a42dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a426c.md#insn-008a42dc)
- 新版 [`008a4320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a42b0.md#insn-008a4320)

~~~diff
- 008a42d8 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4040:8"]]
- 008a42d8 ["INT_SBORROW", "register:106:1", ["register:4040:8", "register:4048:8"]]
- 008a42d8 ["INT_SUB", "tmp:0:8", ["register:4040:8", "register:4048:8"]]
- 008a42d8 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 008a42d8 bytes 1f0109eb
- 008a42dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008a42dc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 008a42dc bytes 01030054
+ 008a4320 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008a4320 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 008a4320 bytes 01030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd66648435ff08dcdaf38f0d5c90bf9e"></a>

### [`008a436c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a436c.md) → [`008a43b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43b0.md) FUN_008a43b0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4384"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a43c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a43b8",
      "incomplete_value": false,
      "site": "008a43bc",
      "value": [
        "leaf",
        "const:10:8"
      ]
    },
    "old": null,
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
      "unmatched:008a4384",
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a43c8",
      "DATA",
      [
        "storage",
        "00c82410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a436c.md#insn-008a4378) · [`008a4384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a436c.md#insn-008a4384)
- 新版 [`008a43bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43b0.md#insn-008a43bc) · [`008a43c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43b0.md#insn-008a43c8)

~~~diff
- 008a4378 ["INT_ADD", "register:40f0:8", ["const:8a4378:8", "const:4:8"]]
- 008a4378 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a43bc ["INT_ADD", "register:40f0:8", ["const:8a43bc:8", "const:4:8"]]
+ 008a43bc ["CALL", null, ["callee:00c57e90:8"]]
- 008a4378 bytes c6cd0e94
+ 008a43bc bytes b5ce0e94
- 008a4384 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a4384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a4384 bytes 080000f9
+ 008a43c8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a43c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a43c8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d12423bb31f972e7d220415461bf440d"></a>

### [`008a43a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md) → [`008a43ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43ec.md) FUN_008a43ec

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`008a44e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44e8.md) [`008a44ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44ec.md) [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008a452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a452c.md) [`008a4530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4530.md) [`00b3a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a5b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a441c",
      "incomplete_value": true,
      "site": "008a4424",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a43e0",
      "value": [
        "live",
        "register:4098:8"
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
      "008a4420",
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ],
    [
      "008a4454",
      "READ",
      [
        "storage",
        "00c820a0",
        null,
        "pointer"
      ]
    ],
    [
      "008a4454",
      "READ",
      [
        "storage",
        "00c820a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a4420",
      "DATA",
      [
        "storage",
        "00c82480",
        null,
        "undefined *"
      ]
    ],
    [
      "008a4454",
      "READ",
      [
        "storage",
        "00c824a0",
        null,
        "pointer"
      ]
    ],
    [
      "008a4454",
      "READ",
      [
        "storage",
        "00c824a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a43d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md#insn-008a43d4) · [`008a43d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md#insn-008a43d8) · [`008a43e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md#insn-008a43e8)
- 新版 [`008a442c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43ec.md#insn-008a442c)

~~~diff
- 008a43d4 ["COPY", "tmp:0:8", ["const:80:8"]]
- 008a43d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a43d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a43d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a43d4 bytes 08010291
- 008a43d8 ["COPY", "register:4098:8", ["register:8:8"]]
- 008a43d8 bytes f3030091
- 008a43e8 ["INT_ADD", "register:40f0:8", ["const:8a43e8:8", "const:4:8"]]
- 008a43e8 ["CALL", null, ["callee:00b3a5b8:8"]]
+ 008a442c ["INT_ADD", "register:40f0:8", ["const:8a442c:8", "const:4:8"]]
+ 008a442c ["CALL", null, ["callee:00b3a5b8:8"]]
- 008a43e8 bytes 6a570a94
+ 008a442c bytes 63580a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab2dbf9a3ff7c463907d81c9e3d3f0f2"></a>

### [`008a44b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44b4.md) → [`008a44f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a44f8.md) FUN_008a44f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a450c",
      "incomplete_value": false,
      "site": "008a4510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a44c8",
      "incomplete_value": false,
      "site": "008a44cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "008a4510",
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a4510",
      "DATA",
      [
        "storage",
        "00c82480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a44c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44b4.md#insn-008a44c0) · [`008a44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44b4.md#insn-008a44c8)
- 新版 [`008a4504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a44f8.md#insn-008a4504) · [`008a450c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a44f8.md#insn-008a450c)

~~~diff
- 008a44c0 ["INT_ADD", "register:40f0:8", ["const:8a44c0:8", "const:4:8"]]
- 008a44c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a4504 ["INT_ADD", "register:40f0:8", ["const:8a4504:8", "const:4:8"]]
+ 008a4504 ["CALL", null, ["callee:00c57e90:8"]]
- 008a44c0 bytes 74cd0e94
+ 008a4504 bytes 63ce0e94
- 008a44c8 ["COPY", "tmp:0:8", ["const:80:8"]]
- 008a44c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a44c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a44c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a450c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 008a450c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a450c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a450c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a44c8 bytes 08010291
+ 008a450c bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4a48d202ea97dc6131bd3fca852202"></a>

### [`008a44d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44d8.md) → [`008a451c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a451c.md) FUN_008a451c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a4520",
      "incomplete_value": false,
      "site": "008a4524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a44dc",
      "incomplete_value": false,
      "site": "008a44e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
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
      "008a4524",
      "DATA",
      [
        "storage",
        "00c82080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a4524",
      "DATA",
      [
        "storage",
        "00c82480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44d8.md#insn-008a44dc)
- 新版 [`008a4520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a451c.md#insn-008a4520)

~~~diff
- 008a44dc ["COPY", "tmp:0:8", ["const:80:8"]]
- 008a44dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a44dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a44dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a4520 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 008a4520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a44dc bytes 08010291
+ 008a4520 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ef8b39759e4a397a5fa0e4f00760985"></a>

### [`008a44f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44f0.md) → [`008a4534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4534.md) FUN_008a4534

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.50% / 新版 91.50%

CFGの説明率　旧版 53.70% / 新版 56.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a4528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "unmatched:008a4560",
      "READ",
      [
        "storage",
        "002a338f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008a4568",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008a456c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "008a45a4",
      "READ",
      [
        "storage",
        "002a345c",
        null,
        "string"
      ]
    ],
    [
      "008a45ac",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44f0.md#insn-008a4528) · [`008a452c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44f0.md#insn-008a452c) · [`008a4568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a44f0.md#insn-008a4568)
- 新版 [`008a4570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4534.md#insn-008a4570)

~~~diff
- 008a4528 ["INT_ADD", "register:40f0:8", ["const:8a4528:8", "const:4:8"]]
- 008a4528 ["CALL", null, ["ram:71c420:8"]]
- 008a4528 bytes bedff997
- 008a452c ["INT_ADD", "register:40f0:8", ["const:8a452c:8", "const:4:8"]]
- 008a452c ["CALL", null, ["callee:008514f8:8"]]
+ 008a4570 ["INT_ADD", "register:40f0:8", ["const:8a4570:8", "const:4:8"]]
+ 008a4570 ["CALL", null, ["callee:008514f8:8"]]
- 008a452c bytes e3b3fe97
+ 008a4570 bytes e2b3fe97
- 008a4568 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008a4568 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:30:8"]]
- 008a4568 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008a4568 bytes e8c30039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-761722f4ecbef3b971a42733ada3668f"></a>

### [`008a4898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4898.md) → [`008a48dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a48dc.md) FUN_008a48dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a48f0",
      "incomplete_value": false,
      "site": "008a48f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a48ac",
      "incomplete_value": false,
      "site": "008a48b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "008a48f4",
      "DATA",
      [
        "storage",
        "00c820f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a48f4",
      "DATA",
      [
        "storage",
        "00c824f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a48a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4898.md#insn-008a48a4) · [`008a48ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4898.md#insn-008a48ac)
- 新版 [`008a48e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a48dc.md#insn-008a48e8) · [`008a48f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a48dc.md#insn-008a48f0)

~~~diff
- 008a48a4 ["INT_ADD", "register:40f0:8", ["const:8a48a4:8", "const:4:8"]]
- 008a48a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a48e8 ["INT_ADD", "register:40f0:8", ["const:8a48e8:8", "const:4:8"]]
+ 008a48e8 ["CALL", null, ["callee:00c57e90:8"]]
- 008a48a4 bytes 7bcc0e94
+ 008a48e8 bytes 6acd0e94
- 008a48ac ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008a48ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a48ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a48ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a48f0 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008a48f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a48f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a48f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a48ac bytes 08c10391
+ 008a48f0 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-003fe644eaa1a3a5c8c30ca62d25962c"></a>

### [`008a48bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48bc.md) → [`008a4900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4900.md) FUN_008a4900

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008a4904",
      "incomplete_value": false,
      "site": "008a4908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a48c0",
      "incomplete_value": false,
      "site": "008a48c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "008a4908",
      "DATA",
      [
        "storage",
        "00c820f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a4908",
      "DATA",
      [
        "storage",
        "00c824f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a48c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48bc.md#insn-008a48c0)
- 新版 [`008a4904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4900.md#insn-008a4904)

~~~diff
- 008a48c0 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008a48c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a48c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a48c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a4904 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008a4904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a4904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a48c0 bytes 08c10391
+ 008a4904 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c58e0a383297bccbb729ab79f62f4ab"></a>

### [`008a48d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48d4.md) → [`008a4918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4918.md) FUN_008a4918

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008a493c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a48f8",
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
      "008a493c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008a493c",
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

- 旧版 [`008a48f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48d4.md#insn-008a48f8) · [`008a4904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a48d4.md#insn-008a4904)
- 新版 [`008a493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4918.md#insn-008a493c) · [`008a4948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4918.md#insn-008a4948)

~~~diff
- 008a48f8 ["INT_ADD", "register:40f0:8", ["const:8a48f8:8", "const:4:8"]]
- 008a48f8 ["CALL", null, ["ram:47acb4:8"]]
+ 008a493c ["INT_ADD", "register:40f0:8", ["const:8a493c:8", "const:4:8"]]
+ 008a493c ["CALL", null, ["ram:47acf4:8"]]
- 008a48f8 bytes ef58ef97
+ 008a493c bytes ee58ef97
- 008a4904 ["INT_ADD", "register:40f0:8", ["const:8a4904:8", "const:4:8"]]
- 008a4904 ["CALL", null, ["callee:0047cdd4:8"]]
+ 008a4948 ["INT_ADD", "register:40f0:8", ["const:8a4948:8", "const:4:8"]]
+ 008a4948 ["CALL", null, ["callee:0047cdd4:8"]]
- 008a4904 bytes 2461ef97
+ 008a4948 bytes 2361ef97
~~~


