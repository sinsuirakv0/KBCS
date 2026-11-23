# v16.0.0 → v16.0.1 · 最優先の変更候補 (26)

[一覧の目次](README.md)

<a id="compare-6cfb8fc5e8c4167a18c296830bc5378b"></a>

### [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) → [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) FUN_005fb93c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005fb400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb400.md) · 呼出先 52件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)
- 新版 呼出元 1件 [`005fb440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb440.md) · 呼出先 52件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fbc8c",
      "incomplete_value": false,
      "site": "005fbc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:27d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fbc4c",
      "incomplete_value": false,
      "site": "005fbc54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:23d:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fbd64",
      "incomplete_value": false,
      "site": "005fbd70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:27d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fbd24",
      "incomplete_value": false,
      "site": "005fbd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:23d:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005fbe44",
      "incomplete_value": true,
      "site": "005fbe4c",
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
            "const:38d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005fbe04",
      "incomplete_value": true,
      "site": "005fbe0c",
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
            "const:34d:8"
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
      "005fbb78",
      "READ",
      [
        "storage",
        "002c40a0",
        null,
        "undefined8"
      ]
    ],
    [
      "005fbbcc",
      "READ",
      [
        "storage",
        "002c40a0",
        null,
        "undefined8"
      ]
    ],
    [
      "005fbc8c",
      "PARAM",
      [
        "storage",
        "002b623d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005fbb78",
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ],
    [
      "005fbbcc",
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ],
    [
      "005fbc8c",
      "PARAM",
      [
        "storage",
        "002b627d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005fbc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md#insn-005fbc14) · [`005fbc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md#insn-005fbc54) · [`005fbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md#insn-005fbd30)
- 新版 `005fbc54`（命令位置の公開資料なし） · `005fbc94`（命令位置の公開資料なし） · `005fbd70`（命令位置の公開資料なし）

~~~diff
- 005fbc14 ["INT_ADD", "register:40f0:8", ["const:5fbc14:8", "const:4:8"]]
- 005fbc14 ["CALL", null, ["callee:00af520c:8"]]
+ 005fbc54 ["INT_ADD", "register:40f0:8", ["const:5fbc54:8", "const:4:8"]]
+ 005fbc54 ["CALL", null, ["callee:00af520c:8"]]
- 005fbc14 bytes 74e41394
+ 005fbc54 bytes 6ee51394
- 005fbc54 ["INT_ADD", "register:40f0:8", ["const:5fbc54:8", "const:4:8"]]
- 005fbc54 ["CALL", null, ["callee:00c580b0:8"]]
+ 005fbc94 ["INT_ADD", "register:40f0:8", ["const:5fbc94:8", "const:4:8"]]
+ 005fbc94 ["CALL", null, ["callee:00c580b0:8"]]
- 005fbc54 bytes 17701994
+ 005fbc94 bytes 07711994
- 005fbd30 ["INT_ADD", "register:40f0:8", ["const:5fbd30:8", "const:4:8"]]
- 005fbd30 ["CALL", null, ["callee:00c580b0:8"]]
+ 005fbd70 ["INT_ADD", "register:40f0:8", ["const:5fbd70:8", "const:4:8"]]
+ 005fbd70 ["CALL", null, ["callee:00c580b0:8"]]
- 005fbd30 bytes e06f1994
+ 005fbd70 bytes d0701994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e054ad83d718fb9f1b919ddbec074acc"></a>

### [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) → [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) FUN_005fc3a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 30件 [`004675a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675a8.md) [`004675c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675c4.md) [`00467610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md) [`00467740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467740.md) [`004677a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004677a0.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 30件 [`004675e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004675e8.md) [`00467604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467604.md) [`00467650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md) [`00467780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467780.md) [`004677e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004677e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fc4a0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fc460",
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
      "site": "005fc4cc",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fc48c",
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
      "site": "005fc544",
      "value": [
        "leaf",
        "ram:4675e8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fc504",
      "value": [
        "leaf",
        "ram:4675a8:8"
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
      "005fc404",
      "READ",
      [
        "storage",
        "00c9b070",
        null,
        "pointer"
      ]
    ],
    [
      "005fc42c",
      "READ",
      [
        "storage",
        "00ca3fe8",
        null,
        "undefined4"
      ]
    ],
    [
      "005fc4a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "005fc404",
      "READ",
      [
        "storage",
        "00c9b470",
        null,
        "pointer"
      ]
    ],
    [
      "005fc42c",
      "READ",
      [
        "storage",
        "00ca43e8",
        null,
        "undefined4"
      ]
    ],
    [
      "005fc4a0",
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

- 旧版 [`005fc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md#insn-005fc460) · [`005fc48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md#insn-005fc48c) · [`005fc504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md#insn-005fc504)
- 新版 `005fc4a0`（命令位置の公開資料なし） · `005fc4cc`（命令位置の公開資料なし） · `005fc544`（命令位置の公開資料なし）

~~~diff
- 005fc460 ["INT_ADD", "register:40f0:8", ["const:5fc460:8", "const:4:8"]]
- 005fc460 ["CALL", null, ["ram:46c984:8"]]
+ 005fc4a0 ["INT_ADD", "register:40f0:8", ["const:5fc4a0:8", "const:4:8"]]
+ 005fc4a0 ["CALL", null, ["ram:46c9c4:8"]]
- 005fc460 bytes 49c1f997
+ 005fc4a0 bytes 49c1f997
- 005fc48c ["INT_ADD", "register:40f0:8", ["const:5fc48c:8", "const:4:8"]]
- 005fc48c ["CALL", null, ["ram:46c984:8"]]
+ 005fc4cc ["INT_ADD", "register:40f0:8", ["const:5fc4cc:8", "const:4:8"]]
+ 005fc4cc ["CALL", null, ["ram:46c9c4:8"]]
- 005fc48c bytes 3ec1f997
+ 005fc4cc bytes 3ec1f997
- 005fc504 ["INT_ADD", "register:40f0:8", ["const:5fc504:8", "const:4:8"]]
- 005fc504 ["CALL", null, ["ram:4675a8:8"]]
+ 005fc544 ["INT_ADD", "register:40f0:8", ["const:5fc544:8", "const:4:8"]]
+ 005fc544 ["CALL", null, ["ram:4675e8:8"]]
- 005fc504 bytes 29acf997
+ 005fc544 bytes 29acf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b3b3e3680f600f47d439a5e5d9e7590"></a>

### [`005fdc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md) → [`005fdc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fd/005fdc58.md) FUN_005fdc58

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) · 呼出先 28件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md)
- 新版 呼出元 2件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00718774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) · 呼出先 28件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fdc94",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fdc54",
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
      "site": "005fdcf8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fdcb8",
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
      "site": "005fdd18",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005fdcd8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "005fdc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005fdcf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "005fdd18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "005fdc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005fdcf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "005fdd18",
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

- 旧版 [`005fdc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md#insn-005fdc54) · [`005fdc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md#insn-005fdc94) · [`005fdcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md#insn-005fdcb8)
- 新版 `005fdc94`（命令位置の公開資料なし） · `005fdcd4`（命令位置の公開資料なし） · `005fdcf8`（命令位置の公開資料なし）

~~~diff
- 005fdc54 ["INT_ADD", "register:40f0:8", ["const:5fdc54:8", "const:4:8"]]
- 005fdc54 ["CALL", null, ["ram:47acb4:8"]]
+ 005fdc94 ["INT_ADD", "register:40f0:8", ["const:5fdc94:8", "const:4:8"]]
+ 005fdc94 ["CALL", null, ["ram:47acf4:8"]]
- 005fdc54 bytes 18f4f997
+ 005fdc94 bytes 18f4f997
- 005fdc94 ["INT_ADD", "register:40f0:8", ["const:5fdc94:8", "const:4:8"]]
- 005fdc94 ["CALL", null, ["callee:00af2d08:8"]]
+ 005fdcd4 ["INT_ADD", "register:40f0:8", ["const:5fdcd4:8", "const:4:8"]]
+ 005fdcd4 ["CALL", null, ["callee:00af2d08:8"]]
- 005fdc94 bytes 13d31394
+ 005fdcd4 bytes 0dd41394
- 005fdcb8 ["INT_ADD", "register:40f0:8", ["const:5fdcb8:8", "const:4:8"]]
- 005fdcb8 ["CALL", null, ["ram:47acb4:8"]]
+ 005fdcf8 ["INT_ADD", "register:40f0:8", ["const:5fdcf8:8", "const:4:8"]]
+ 005fdcf8 ["CALL", null, ["ram:47acf4:8"]]
- 005fdcb8 bytes fff3f997
+ 005fdcf8 bytes fff3f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc7ddb73daccfb8c494525b33801291"></a>

### [`005fe1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1f4.md) → [`005fe234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe234.md) FUN_005fe234

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005f7900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`005f7940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7940.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005fe240",
      "incomplete_value": false,
      "site": "005fe244",
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
      "definition_site": "005fe200",
      "incomplete_value": false,
      "site": "005fe204",
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
      "005fe240",
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
      "005fe240",
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

- 旧版 [`005fe204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1f4.md#insn-005fe204) · [`005fe200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1f4.md#insn-005fe200)
- 新版 `005fe244`（命令位置の公開資料なし） · `005fe240`（命令位置の公開資料なし）

~~~diff
- 005fe204 ["INT_ADD", "register:40f0:8", ["const:5fe204:8", "const:4:8"]]
- 005fe204 ["CALL", null, ["callee:0043b778:8"]]
+ 005fe244 ["INT_ADD", "register:40f0:8", ["const:5fe244:8", "const:4:8"]]
+ 005fe244 ["CALL", null, ["callee:0043b778:8"]]
- 005fe204 bytes 4df5f897
+ 005fe244 bytes 4df5f897
- 005fe200 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005fe200 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005fe200 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005fe200 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005fe240 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005fe240 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe240 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe240 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005fe200 bytes 00303c91
+ 005fe240 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12c666ec782f285310b981d7762f8a9"></a>

### [`005fe208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md) → [`005fe248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe248.md) FUN_005fe248

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005f87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) [`005f8c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8c54.md) [`005f8e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8e40.md) [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 8件 [`005f8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8820.md) [`005f8c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8c94.md) [`005f8e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8e80.md) [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "005fe254",
      "incomplete_value": false,
      "site": "005fe258",
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
      "definition_site": "005fe214",
      "incomplete_value": false,
      "site": "005fe218",
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
      "005fe254",
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
      "005fe254",
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

- 旧版 [`005fe218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md#insn-005fe218) · [`005fe214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md#insn-005fe214)
- 新版 `005fe258`（命令位置の公開資料なし） · `005fe254`（命令位置の公開資料なし）

~~~diff
- 005fe218 ["INT_ADD", "register:40f0:8", ["const:5fe218:8", "const:4:8"]]
- 005fe218 ["CALL", null, ["callee:00442930:8"]]
+ 005fe258 ["INT_ADD", "register:40f0:8", ["const:5fe258:8", "const:4:8"]]
+ 005fe258 ["CALL", null, ["callee:00442930:8"]]
- 005fe218 bytes b611f997
+ 005fe258 bytes b611f997
- 005fe214 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005fe214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005fe214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005fe214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005fe254 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005fe254 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe254 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe254 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005fe214 bytes 00303c91
+ 005fe254 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b22ba592446573bcc0296298244db2f"></a>

### [`005fe21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe21c.md) → [`005fe25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe25c.md) FUN_005fe25c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f8e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8e40.md) [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`007140e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/007140e4.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 5件 [`005f8e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8e80.md) [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`00714124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714124.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "005fe268",
      "incomplete_value": false,
      "site": "005fe26c",
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
      "definition_site": "005fe228",
      "incomplete_value": false,
      "site": "005fe22c",
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
      "005fe268",
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
      "005fe268",
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

- 旧版 [`005fe22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe21c.md#insn-005fe22c) · [`005fe228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe21c.md#insn-005fe228)
- 新版 `005fe26c`（命令位置の公開資料なし） · `005fe268`（命令位置の公開資料なし）

~~~diff
- 005fe22c ["INT_ADD", "register:40f0:8", ["const:5fe22c:8", "const:4:8"]]
- 005fe22c ["CALL", null, ["callee:0043b778:8"]]
+ 005fe26c ["INT_ADD", "register:40f0:8", ["const:5fe26c:8", "const:4:8"]]
+ 005fe26c ["CALL", null, ["callee:0043b778:8"]]
- 005fe22c bytes 43f5f897
+ 005fe26c bytes 43f5f897
- 005fe228 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005fe228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005fe228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005fe228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005fe268 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005fe268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005fe228 bytes 00303c91
+ 005fe268 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c899fd476aea1ef260cdecdc51f4a4"></a>

### [`005fe230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe230.md) → [`005fe270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe270.md) FUN_005fe270

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005f950c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f950c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`005f954c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f9/005f954c.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "005fe27c",
      "incomplete_value": false,
      "site": "005fe280",
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
      "definition_site": "005fe23c",
      "incomplete_value": false,
      "site": "005fe240",
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
      "005fe27c",
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
      "005fe27c",
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

- 旧版 [`005fe240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe230.md#insn-005fe240) · [`005fe23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe230.md#insn-005fe23c)
- 新版 `005fe280`（命令位置の公開資料なし） · `005fe27c`（命令位置の公開資料なし）

~~~diff
- 005fe240 ["INT_ADD", "register:40f0:8", ["const:5fe240:8", "const:4:8"]]
- 005fe240 ["CALL", null, ["callee:00442930:8"]]
+ 005fe280 ["INT_ADD", "register:40f0:8", ["const:5fe280:8", "const:4:8"]]
+ 005fe280 ["CALL", null, ["callee:00442930:8"]]
- 005fe240 bytes ac11f997
+ 005fe280 bytes ac11f997
- 005fe23c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005fe23c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005fe23c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005fe23c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005fe27c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005fe27c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe27c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe27c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005fe23c bytes 00303c91
+ 005fe27c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f521652c631483abdd30f1b3957a85d"></a>

### [`005fe244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md) → [`005fe284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe284.md) FUN_005fe284

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f9670.md) [`005fa4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa4b8.md) [`007153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007153c0.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`005f96b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f9/005f96b0.md) [`005fa4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fa/005fa4f8.md) [`00715400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715400.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "005fe290",
      "incomplete_value": true,
      "site": "005fe294",
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
      "definition_site": "005fe250",
      "incomplete_value": true,
      "site": "005fe254",
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
      "005fe290",
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
      "005fe290",
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

- 旧版 [`005fe254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md#insn-005fe254) · [`005fe250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md#insn-005fe250)
- 新版 `005fe294`（命令位置の公開資料なし） · `005fe290`（命令位置の公開資料なし）

~~~diff
- 005fe254 ["INT_ADD", "register:40f0:8", ["const:5fe254:8", "const:4:8"]]
- 005fe254 ["CALL", null, ["callee:00442930:8"]]
+ 005fe294 ["INT_ADD", "register:40f0:8", ["const:5fe294:8", "const:4:8"]]
+ 005fe294 ["CALL", null, ["callee:00442930:8"]]
- 005fe254 bytes a711f997
+ 005fe294 bytes a711f997
- 005fe250 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 005fe250 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005fe250 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005fe250 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005fe290 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 005fe290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005fe290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005fe250 bytes 00303c91
+ 005fe290 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-078db642d4ad91551bf31cddcb884a8c"></a>

### [`005fe29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe29c.md) → [`005fe2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe2dc.md) _INIT_76

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.18% / 新版 84.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005fe318",
      "incomplete_value": true,
      "site": "005fe334",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005fe2d8",
      "incomplete_value": true,
      "site": "005fe2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005fe33c",
      "incomplete_value": true,
      "site": "005fe358",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005fe2fc",
      "incomplete_value": true,
      "site": "005fe318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005fe35c",
      "incomplete_value": true,
      "site": "005fe378",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005fe31c",
      "incomplete_value": true,
      "site": "005fe338",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005fe318",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "005fe33c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "005fe35c",
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
      "005fe318",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005fe33c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005fe35c",
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

- 旧版 [`005fe314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe29c.md#insn-005fe314) · [`005fe334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe29c.md#insn-005fe334) · [`005fe424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe29c.md#insn-005fe424)
- 新版 `005fe354`（命令位置の公開資料なし） · `005fe374`（命令位置の公開資料なし） · `005fe464`（命令位置の公開資料なし）

~~~diff
- 005fe314 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 005fe314 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005fe314 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005fe314 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005fe354 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 005fe354 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005fe354 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005fe354 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005fe314 bytes 4a093691
+ 005fe354 bytes 4a093791
- 005fe334 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 005fe334 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005fe334 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005fe334 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005fe374 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 005fe374 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005fe374 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005fe374 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005fe334 bytes 4a553a91
+ 005fe374 bytes 4a893d91
- 005fe424 ["INT_ADD", "register:40f0:8", ["const:5fe424:8", "const:4:8"]]
- 005fe424 ["CALL", null, ["callee:0043b7f8:8"]]
+ 005fe464 ["INT_ADD", "register:40f0:8", ["const:5fe464:8", "const:4:8"]]
+ 005fe464 ["CALL", null, ["callee:0043b7f8:8"]]
- 005fe424 bytes e5f4f897
+ 005fe464 bytes e5f4f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c675d1cf8d1fa1ccab839eedbb6650"></a>

### [`00605164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605164.md) → [`006051a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/006051a4.md) FUN_006051a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 4件 [`00616118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616118.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 4件 [`00616158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616158.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006051d8",
      "incomplete_value": true,
      "site": "006051dc",
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
      "definition_site": "00605198",
      "incomplete_value": true,
      "site": "0060519c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060521c",
      "incomplete_value": true,
      "site": "00605220",
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
      "definition_site": "006051dc",
      "incomplete_value": true,
      "site": "006051e0",
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
      "006051d0",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ],
    [
      "006051dc",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00605214",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006051d0",
      "READ",
      [
        "storage",
        "00c9b370",
        null,
        "pointer"
      ]
    ],
    [
      "006051dc",
      "DATA",
      [
        "storage",
        "00c8b7b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00605214",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00605188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605164.md#insn-00605188) · [`00605190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605164.md#insn-00605190) · [`006051ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605164.md#insn-006051ac)
- 新版 `006051c8`（命令位置の公開資料なし） · `006051d0`（命令位置の公開資料なし） · `006051ec`（命令位置の公開資料なし）

~~~diff
- 00605188 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 006051c8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00605188 bytes a83400b0
+ 006051c8 bytes a83400d0
- 00605190 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 00605190 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006051d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 006051d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00605190 bytes 08b947f9
+ 006051d0 bytes 08b941f9
- 006051ac ["INT_ADD", "register:40f0:8", ["const:6051ac:8", "const:4:8"]]
- 006051ac ["CALL", null, ["callee:00c53d00:8"]]
+ 006051ec ["INT_ADD", "register:40f0:8", ["const:6051ec:8", "const:4:8"]]
+ 006051ec ["CALL", null, ["callee:00c53d00:8"]]
- 006051ac bytes cd391994
+ 006051ec bytes c53a1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae82cfb4a4a2cee379660eb3dfc4ba98"></a>

### [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) → [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) FUN_00605254

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 61件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046cc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cc34.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 61件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046cc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc74.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 11件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006061b0",
      "incomplete_value": true,
      "site": "006061c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:198:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00606170",
      "incomplete_value": true,
      "site": "00606180",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 208,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006052b8",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00605278",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "site": "0060535c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0060531c",
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
      "006052b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "0060535c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006055ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006052b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "0060535c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006055ec",
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

- 旧版 [`00605278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md#insn-00605278) · [`0060531c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md#insn-0060531c) · [`006055ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md#insn-006055ac)
- 新版 `006052b8`（命令位置の公開資料なし） · `0060535c`（命令位置の公開資料なし） · `006055ec`（命令位置の公開資料なし）

~~~diff
- 00605278 ["INT_ADD", "register:40f0:8", ["const:605278:8", "const:4:8"]]
- 00605278 ["CALL", null, ["ram:802b4c:8"]]
+ 006052b8 ["INT_ADD", "register:40f0:8", ["const:6052b8:8", "const:4:8"]]
+ 006052b8 ["CALL", null, ["ram:802b8c:8"]]
- 00605278 bytes 35f60794
+ 006052b8 bytes 35f60794
- 0060531c ["INT_ADD", "register:40f0:8", ["const:60531c:8", "const:4:8"]]
- 0060531c ["CALL", null, ["ram:47acb4:8"]]
+ 0060535c ["INT_ADD", "register:40f0:8", ["const:60535c:8", "const:4:8"]]
+ 0060535c ["CALL", null, ["ram:47acf4:8"]]
- 0060531c bytes 66d6f997
+ 0060535c bytes 66d6f997
- 006055ac ["INT_ADD", "register:40f0:8", ["const:6055ac:8", "const:4:8"]]
- 006055ac ["CALL", null, ["ram:47acb4:8"]]
+ 006055ec ["INT_ADD", "register:40f0:8", ["const:6055ec:8", "const:4:8"]]
+ 006055ec ["CALL", null, ["ram:47acf4:8"]]
- 006055ac bytes c2d5f997
+ 006055ec bytes c2d5f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b98e61d86853faa60a5f8bcb6ce6ac1"></a>

### [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) → [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) FUN_006064d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 22件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cb1c.md) [`0046cc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cc34.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00616118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616118.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 22件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb5c.md) [`0046cc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc74.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00616158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616158.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.42% / 新版 96.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006068d4",
      "incomplete_value": false,
      "site": "006068d4",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00606894",
      "incomplete_value": false,
      "site": "00606894",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00606514",
      "incomplete_value": true,
      "site": "00606514",
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
      "definition_site": "006064d4",
      "incomplete_value": true,
      "site": "006064d4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060651c",
      "incomplete_value": false,
      "site": "0060652c",
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
      "definition_site": "006064dc",
      "incomplete_value": false,
      "site": "006064ec",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00606510",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0060651c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00606524",
      "PARAM",
      [
        "storage",
        "00c71578",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00606510",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0060651c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00606524",
      "PARAM",
      [
        "storage",
        "00c71978",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006064e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md#insn-006064e4) · [`006064ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md#insn-006064ec) · [`00606524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md#insn-00606524)
- 新版 `00606524`（命令位置の公開資料なし） · `0060652c`（命令位置の公開資料なし） · `00606564`（命令位置の公開資料なし）

~~~diff
- 006064e4 ["COPY", "tmp:0:8", ["const:578:8"]]
- 006064e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006064e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006064e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00606524 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00606524 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00606524 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00606524 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006064e4 bytes 42e01591
+ 00606524 bytes 42e02591
- 006064ec ["INT_ADD", "register:40f0:8", ["const:6064ec:8", "const:4:8"]]
- 006064ec ["CALL", null, ["callee:00c58610:8"]]
+ 0060652c ["INT_ADD", "register:40f0:8", ["const:60652c:8", "const:4:8"]]
+ 0060652c ["CALL", null, ["callee:00c58610:8"]]
- 006064ec bytes 49471994
+ 0060652c bytes 39481994
- 00606524 ["INT_ADD", "register:40f0:8", ["const:606524:8", "const:4:8"]]
- 00606524 ["CALL", null, ["ram:46c984:8"]]
+ 00606564 ["INT_ADD", "register:40f0:8", ["const:606564:8", "const:4:8"]]
+ 00606564 ["CALL", null, ["ram:46c9c4:8"]]
- 00606524 bytes 1899f997
+ 00606564 bytes 1899f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34d7ab24cb8a9356249cb78c4bad0caa"></a>

### [`0060d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md) → [`0060d624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060d/0060d624.md) FUN_0060d624

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`00615708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615708.md) [`0071d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d0f4.md)
- 新版 呼出元 2件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`00615748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615748.md) [`0071d134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d134.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060d65c",
      "incomplete_value": true,
      "site": "0060d674",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e19:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d61c",
      "incomplete_value": true,
      "site": "0060d634",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dd9:8"
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
      "definition_site": "0060d678",
      "incomplete_value": true,
      "site": "0060d678",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0060d638",
      "incomplete_value": true,
      "site": "0060d638",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060d740",
      "incomplete_value": true,
      "site": "0060d74c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d700",
      "incomplete_value": true,
      "site": "0060d70c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d8c:8"
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
      "0060d65c",
      "READ",
      [
        "storage",
        "002b0dd9",
        null,
        "string"
      ]
    ],
    [
      "0060d660",
      "READ",
      [
        "storage",
        "002b0de7",
        null,
        "string"
      ]
    ],
    [
      "0060d724",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d0f4"
      ]
    ]
  ],
  "added": [
    [
      "0060d65c",
      "READ",
      [
        "storage",
        "002b0e19",
        null,
        "string"
      ]
    ],
    [
      "0060d660",
      "READ",
      [
        "storage",
        "002b0e27",
        null,
        "string"
      ]
    ],
    [
      "0060d724",
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

- 旧版 [`0060d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md#insn-0060d6e4) · [`0060d740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md#insn-0060d740) · [`0060d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060d/0060d5e4.md#insn-0060d610)
- 新版 `0060d724`（命令位置の公開資料なし） · `0060d780`（命令位置の公開資料なし） · `0060d650`（命令位置の公開資料なし）

~~~diff
- 0060d6e4 ["INT_ADD", "register:40f0:8", ["const:60d6e4:8", "const:4:8"]]
- 0060d6e4 ["CALL", null, ["ram:71d0f4:8"]]
+ 0060d724 ["INT_ADD", "register:40f0:8", ["const:60d724:8", "const:4:8"]]
+ 0060d724 ["CALL", null, ["ram:71d134:8"]]
- 0060d6e4 bytes 843e0494
+ 0060d724 bytes 843e0494
- 0060d740 ["INT_ADD", "register:40f0:8", ["const:60d740:8", "const:4:8"]]
- 0060d740 ["CALL", null, ["ram:71ecc0:8"]]
+ 0060d780 ["INT_ADD", "register:40f0:8", ["const:60d780:8", "const:4:8"]]
+ 0060d780 ["CALL", null, ["ram:71ed00:8"]]
- 0060d740 bytes 60450494
+ 0060d780 bytes 60450494
- 0060d610 ["COPY", "tmp:0:8", ["const:dd9:8"]]
- 0060d610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0060d610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0060d610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0060d650 ["COPY", "tmp:0:8", ["const:e19:8"]]
+ 0060d650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0060d650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0060d650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0060d610 bytes 29653791
+ 0060d650 bytes 29653891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc562e102a8e41fb8d4af6e17c7842d3"></a>

### [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) → [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) FUN_0060e0c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`0061706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md) [`00934468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md) · 呼出先 37件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 4件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006170ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md) [`00934604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934604.md) · 呼出先 37件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060e4a0",
      "incomplete_value": true,
      "site": "0060e4b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060e460",
      "incomplete_value": true,
      "site": "0060e474",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:37b:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0060e4a4",
      "incomplete_value": true,
      "site": "0060e4b8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0060e464",
      "incomplete_value": true,
      "site": "0060e478",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060e4a8",
      "incomplete_value": true,
      "site": "0060e4bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0060e468",
      "incomplete_value": true,
      "site": "0060e47c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0060e170",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ],
    [
      "0060e194",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ],
    [
      "0060e1b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "0060e170",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ],
    [
      "0060e194",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ],
    [
      "0060e1b8",
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

- 旧版 [`0060e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md#insn-0060e160) · [`0060e178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md#insn-0060e178) · [`0060e1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md#insn-0060e1a0)
- 新版 `0060e1a0`（命令位置の公開資料なし） · `0060e1b8`（命令位置の公開資料なし） · `0060e1e0`（命令位置の公開資料なし）

~~~diff
- 0060e160 ["INT_ADD", "register:40f0:8", ["const:60e160:8", "const:4:8"]]
- 0060e160 ["CALL", null, ["callee:008056ec:8"]]
+ 0060e1a0 ["INT_ADD", "register:40f0:8", ["const:60e1a0:8", "const:4:8"]]
+ 0060e1a0 ["CALL", null, ["callee:008056ec:8"]]
- 0060e160 bytes 53dd0794
+ 0060e1a0 bytes 53dd0794
- 0060e178 ["INT_ADD", "register:40f0:8", ["const:60e178:8", "const:4:8"]]
- 0060e178 ["CALL", null, ["ram:a65bf4:8"]]
+ 0060e1b8 ["INT_ADD", "register:40f0:8", ["const:60e1b8:8", "const:4:8"]]
+ 0060e1b8 ["CALL", null, ["ram:a65dec:8"]]
- 0060e178 bytes 9f5e1194
+ 0060e1b8 bytes 0d5f1194
- 0060e1a0 ["INT_ADD", "register:40f0:8", ["const:60e1a0:8", "const:4:8"]]
- 0060e1a0 ["CALL", null, ["ram:804034:8"]]
+ 0060e1e0 ["INT_ADD", "register:40f0:8", ["const:60e1e0:8", "const:4:8"]]
+ 0060e1e0 ["CALL", null, ["ram:804074:8"]]
- 0060e1a0 bytes a5d70794
+ 0060e1e0 bytes a5d70794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc70464b3cc0c54c911f6d498e17af8"></a>

### [`0060eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md) → [`0060eb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060eb50.md) FUN_0060eb50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 38件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 38件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.31% / 新版 96.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0060ec4c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0060ec0c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "0060eca0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0060ec60",
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
      "site": "0060ed6c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0060ed2c",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "0060ebfc",
      "DATA",
      [
        "storage",
        "0038f2aa",
        null,
        "byte[27]"
      ]
    ],
    [
      "0060ec00",
      "DATA",
      [
        "storage",
        "0038f342",
        null,
        "byte[43]"
      ]
    ],
    [
      "0060ec04",
      "DATA",
      [
        "storage",
        "0038f343",
        null,
        "byte[43]"
      ]
    ]
  ],
  "added": [
    [
      "0060ebfc",
      "DATA",
      [
        "storage",
        "0038f2aa",
        null,
        "qword"
      ]
    ],
    [
      "0060ec00",
      "DATA",
      [
        "storage",
        "0038f342",
        null,
        "dword"
      ]
    ],
    [
      "0060ec04",
      "DATA",
      [
        "storage",
        "0038f343",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md#insn-0060ec0c) · [`0060ec60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md#insn-0060ec60) · [`0060ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060eb10.md#insn-0060ed2c)
- 新版 `0060ec4c`（命令位置の公開資料なし） · `0060eca0`（命令位置の公開資料なし） · `0060ed6c`（命令位置の公開資料なし）

~~~diff
- 0060ec0c ["INT_ADD", "register:40f0:8", ["const:60ec0c:8", "const:4:8"]]
- 0060ec0c ["CALL", null, ["ram:46c984:8"]]
+ 0060ec4c ["INT_ADD", "register:40f0:8", ["const:60ec4c:8", "const:4:8"]]
+ 0060ec4c ["CALL", null, ["ram:46c9c4:8"]]
- 0060ec0c bytes 5e77f997
+ 0060ec4c bytes 5e77f997
- 0060ec60 ["INT_ADD", "register:40f0:8", ["const:60ec60:8", "const:4:8"]]
- 0060ec60 ["CALL", null, ["ram:46c984:8"]]
+ 0060eca0 ["INT_ADD", "register:40f0:8", ["const:60eca0:8", "const:4:8"]]
+ 0060eca0 ["CALL", null, ["ram:46c9c4:8"]]
- 0060ec60 bytes 4977f997
+ 0060eca0 bytes 4977f997
- 0060ed2c ["INT_ADD", "register:40f0:8", ["const:60ed2c:8", "const:4:8"]]
- 0060ed2c ["CALL", null, ["ram:46c984:8"]]
+ 0060ed6c ["INT_ADD", "register:40f0:8", ["const:60ed6c:8", "const:4:8"]]
+ 0060ed6c ["CALL", null, ["ram:46c9c4:8"]]
- 0060ed2c bytes 1677f997
+ 0060ed6c bytes 1677f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f564d431436356c377c5716d611f301"></a>

### [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) → [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) FUN_006103bc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 68件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 68件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `call_target` 14件, `store_value` 7件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006104a8",
      "incomplete_value": true,
      "site": "006104bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610468",
      "incomplete_value": true,
      "site": "0061047c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d5f:8"
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
      "definition_site": "006104ac",
      "incomplete_value": true,
      "site": "006104c0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0061046c",
      "incomplete_value": true,
      "site": "00610480",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006104b0",
      "incomplete_value": true,
      "site": "006104c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610470",
      "incomplete_value": true,
      "site": "00610484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a50:8"
              ]
            ]
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
      "006104a8",
      "READ",
      [
        "storage",
        "002a8d5f",
        null,
        "string"
      ]
    ],
    [
      "006104ac",
      "READ",
      [
        "storage",
        "002a8d69",
        null,
        "string"
      ]
    ],
    [
      "006104b0",
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
      "006104a8",
      "READ",
      [
        "storage",
        "002a8e2c",
        null,
        "string"
      ]
    ],
    [
      "006104ac",
      "READ",
      [
        "storage",
        "002a8e36",
        null,
        "string"
      ]
    ],
    [
      "006104b0",
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

- 旧版 [`0061052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md#insn-0061052c) · [`00610660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md#insn-00610660)
- 新版 `006104a4`（命令位置の公開資料なし） · `0061056c`（命令位置の公開資料なし） · `006106a0`（命令位置の公開資料なし）

~~~diff
+ 006104a4 ["COPY", "register:4048:8", ["const:2c2000:8"]]
+ 006104a4 bytes 89e5ffd0
- 0061052c ["INT_ADD", "register:40f0:8", ["const:61052c:8", "const:4:8"]]
- 0061052c ["CALL", null, ["ram:a65bf4:8"]]
+ 0061056c ["INT_ADD", "register:40f0:8", ["const:61056c:8", "const:4:8"]]
+ 0061056c ["CALL", null, ["ram:a65dec:8"]]
- 0061052c bytes b2551194
+ 0061056c bytes 20561194
- 00610660 ["INT_ADD", "register:40f0:8", ["const:610660:8", "const:4:8"]]
- 00610660 ["CALL", null, ["ram:47acb4:8"]]
+ 006106a0 ["INT_ADD", "register:40f0:8", ["const:6106a0:8", "const:4:8"]]
+ 006106a0 ["CALL", null, ["ram:47acf4:8"]]
- 00610660 bytes 95a9f997
+ 006106a0 bytes 95a9f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78fd40f91bbbaa34030649c2a1098585"></a>

### [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) → [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) FUN_00611e60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00626484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626484.md) · 呼出先 15件 [`005e60c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e60c4.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006264c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/006264c4.md) · 呼出先 15件 [`005e6104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e6/005e6104.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.87% / 新版 90.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00611f10",
      "incomplete_value": false,
      "site": "00611f18",
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
      "definition_site": "00611ed0",
      "incomplete_value": false,
      "site": "00611ed8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00611f38",
      "incomplete_value": false,
      "site": "00611f44",
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
      "definition_site": "00611ef8",
      "incomplete_value": false,
      "site": "00611f04",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00611f70",
      "incomplete_value": false,
      "site": "00611f74",
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
      "definition_site": "00611f30",
      "incomplete_value": false,
      "site": "00611f34",
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
      "00611e9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e60c4"
      ]
    ],
    [
      "00611ecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "00611f18",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00611e9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e6104"
      ]
    ],
    [
      "00611ecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "00611f18",
      "DATA",
      [
        "storage",
        "002aeaf4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00611e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md#insn-00611e5c) · [`00611e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md#insn-00611e8c) · [`00611f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md#insn-00611f98)
- 新版 `00611e9c`（命令位置の公開資料なし） · `00611ecc`（命令位置の公開資料なし） · `00611fd8`（命令位置の公開資料なし）

~~~diff
- 00611e5c ["INT_ADD", "register:40f0:8", ["const:611e5c:8", "const:4:8"]]
- 00611e5c ["CALL", null, ["ram:5e60c4:8"]]
+ 00611e9c ["INT_ADD", "register:40f0:8", ["const:611e9c:8", "const:4:8"]]
+ 00611e9c ["CALL", null, ["ram:5e6104:8"]]
- 00611e5c bytes 9a50ff97
+ 00611e9c bytes 9a50ff97
- 00611e8c ["INT_ADD", "register:40f0:8", ["const:611e8c:8", "const:4:8"]]
- 00611e8c ["CALL", null, ["ram:71c420:8"]]
+ 00611ecc ["INT_ADD", "register:40f0:8", ["const:611ecc:8", "const:4:8"]]
+ 00611ecc ["CALL", null, ["ram:71c460:8"]]
- 00611e8c bytes 65290494
+ 00611ecc bytes 65290494
- 00611f98 ["INT_ADD", "register:40f0:8", ["const:611f98:8", "const:4:8"]]
- 00611f98 ["CALL", null, ["callee:00c5a830:8"]]
+ 00611fd8 ["INT_ADD", "register:40f0:8", ["const:611fd8:8", "const:4:8"]]
+ 00611fd8 ["CALL", null, ["callee:00c5a830:8"]]
- 00611f98 bytes 26211994
+ 00611fd8 bytes 16221994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff9a7ae90d104d3bc96da015ea8af7a1"></a>

### [`0061300c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md) → [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) FUN_0061304c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 43件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 43件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.03% / 新版 91.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 7件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00613134",
      "incomplete_value": true,
      "site": "00613140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006130f4",
      "incomplete_value": true,
      "site": "00613100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
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
      "definition_site": "00613180",
      "incomplete_value": true,
      "site": "0061319c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00613140",
      "incomplete_value": true,
      "site": "0061315c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006133dc",
      "incomplete_value": false,
      "site": "006133dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061339c",
      "incomplete_value": false,
      "site": "0061339c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00613134",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ],
    [
      "0061316c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00613180",
      "READ",
      [
        "storage",
        "002c3d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00613134",
      "READ",
      [
        "storage",
        "002c3f40",
        null,
        "undefined8"
      ]
    ],
    [
      "0061316c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00613180",
      "READ",
      [
        "storage",
        "002c3d40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061312c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md#insn-0061312c) · [`00613140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md#insn-00613140) · [`006131e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/0061300c.md#insn-006131e0)
- 新版 `0061316c`（命令位置の公開資料なし） · `00613180`（命令位置の公開資料なし） · `00613220`（命令位置の公開資料なし）

~~~diff
- 0061312c ["INT_ADD", "register:40f0:8", ["const:61312c:8", "const:4:8"]]
- 0061312c ["CALL", null, ["ram:46c984:8"]]
+ 0061316c ["INT_ADD", "register:40f0:8", ["const:61316c:8", "const:4:8"]]
+ 0061316c ["CALL", null, ["ram:46c9c4:8"]]
- 0061312c bytes 1666f997
+ 0061316c bytes 1666f997
- 00613140 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
- 00613140 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00613140 ["COPY", "register:5008:8", ["const:0:8"]]
- 00613140 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00613180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 00613180 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00613180 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00613180 ["COPY", "register:5010:8", ["const:0:8"]]
- 00613140 bytes 008146fd
+ 00613180 bytes 00a146fd
- 006131e0 ["INT_ADD", "register:40f0:8", ["const:6131e0:8", "const:4:8"]]
- 006131e0 ["CALL", null, ["ram:48ccb8:8"]]
+ 00613220 ["INT_ADD", "register:40f0:8", ["const:613220:8", "const:4:8"]]
+ 00613220 ["CALL", null, ["ram:48ccf8:8"]]
- 006131e0 bytes b6e6f997
+ 00613220 bytes b6e6f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e4871ca878256a103b8780f283273a"></a>

### [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) → [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) FUN_00613c64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 25件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 25件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00613ce4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00613ca4",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00613d70",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00613d30",
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
      "site": "00613da0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00613d60",
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
      "00613ce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00613cf4",
      "READ",
      [
        "storage",
        "00c9b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "00613d0c",
      "READ",
      [
        "storage",
        "00ca3c6c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00613ce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00613cf4",
      "READ",
      [
        "storage",
        "00c9b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "00613d0c",
      "READ",
      [
        "storage",
        "00ca406c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00613ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md#insn-00613ca4) · [`00613d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md#insn-00613d30) · [`00613d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md#insn-00613d60)
- 新版 `00613ce4`（命令位置の公開資料なし） · `00613d70`（命令位置の公開資料なし） · `00613da0`（命令位置の公開資料なし）

~~~diff
- 00613ca4 ["INT_ADD", "register:40f0:8", ["const:613ca4:8", "const:4:8"]]
- 00613ca4 ["CALL", null, ["ram:46c984:8"]]
+ 00613ce4 ["INT_ADD", "register:40f0:8", ["const:613ce4:8", "const:4:8"]]
+ 00613ce4 ["CALL", null, ["ram:46c9c4:8"]]
- 00613ca4 bytes 3863f997
+ 00613ce4 bytes 3863f997
- 00613d30 ["INT_ADD", "register:40f0:8", ["const:613d30:8", "const:4:8"]]
- 00613d30 ["CALL", null, ["ram:46c984:8"]]
+ 00613d70 ["INT_ADD", "register:40f0:8", ["const:613d70:8", "const:4:8"]]
+ 00613d70 ["CALL", null, ["ram:46c9c4:8"]]
- 00613d30 bytes 1563f997
+ 00613d70 bytes 1563f997
- 00613d60 ["INT_ADD", "register:40f0:8", ["const:613d60:8", "const:4:8"]]
- 00613d60 ["CALL", null, ["ram:46c984:8"]]
+ 00613da0 ["INT_ADD", "register:40f0:8", ["const:613da0:8", "const:4:8"]]
+ 00613da0 ["CALL", null, ["ram:46c9c4:8"]]
- 00613d60 bytes 0963f997
+ 00613da0 bytes 0963f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4648eee372557f7fa783f1c59d40d89"></a>

### [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) → [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) FUN_0061452c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 55件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046cc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cc34.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 55件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046cc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 7件, `store_value` 6件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00614674",
      "incomplete_value": true,
      "site": "00614680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614634",
      "incomplete_value": true,
      "site": "00614640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
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
      "definition_site": "006146f0",
      "incomplete_value": true,
      "site": "006146f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006146b0",
      "incomplete_value": true,
      "site": "006146b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "00614748",
      "incomplete_value": true,
      "site": "00614750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614708",
      "incomplete_value": true,
      "site": "00614710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "00614628",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "qword"
      ]
    ],
    [
      "00614674",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ],
    [
      "006146f0",
      "READ",
      [
        "storage",
        "002c3f10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00614628",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "uleb128"
      ]
    ],
    [
      "00614674",
      "READ",
      [
        "storage",
        "002c3f40",
        null,
        "undefined8"
      ]
    ],
    [
      "006146f0",
      "READ",
      [
        "storage",
        "002c3f50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00614714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md#insn-00614714) · [`0061472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md#insn-0061472c) · [`00614784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md#insn-00614784)
- 新版 `00614754`（命令位置の公開資料なし） · `0061476c`（命令位置の公開資料なし） · `006147c4`（命令位置の公開資料なし）

~~~diff
- 00614714 ["INT_ADD", "register:40f0:8", ["const:614714:8", "const:4:8"]]
- 00614714 ["CALL", null, ["ram:47acb4:8"]]
+ 00614754 ["INT_ADD", "register:40f0:8", ["const:614754:8", "const:4:8"]]
+ 00614754 ["CALL", null, ["ram:47acf4:8"]]
- 00614714 bytes 6899f997
+ 00614754 bytes 6899f997
- 0061472c ["INT_ADD", "register:40f0:8", ["const:61472c:8", "const:4:8"]]
- 0061472c ["CALL", null, ["ram:46c984:8"]]
+ 0061476c ["INT_ADD", "register:40f0:8", ["const:61476c:8", "const:4:8"]]
+ 0061476c ["CALL", null, ["ram:46c9c4:8"]]
- 0061472c bytes 9660f997
+ 0061476c bytes 9660f997
- 00614784 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:768:8"]]
- 00614784 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006147c4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b68:8"]]
+ 006147c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00614784 bytes 00b443f9
+ 006147c4 bytes 00b445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7c92455ff9c21c8b7f8db5d2d93241"></a>

### [`006153cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006153cc.md) → [`0061540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/0061540c.md) FUN_0061540c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 13件 [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 13件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.07% / 新版 98.07%

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
      "site": "00615478",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00615438",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00615500",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006154c0",
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
      "site": "0061553c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006154fc",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00615478",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00615488",
      "READ",
      [
        "storage",
        "00c9b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "006154a0",
      "READ",
      [
        "storage",
        "00ca3c6c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00615478",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00615488",
      "READ",
      [
        "storage",
        "00c9b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "006154a0",
      "READ",
      [
        "storage",
        "00ca406c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00615438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006153cc.md#insn-00615438) · [`006154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006153cc.md#insn-006154c0) · [`006154fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006153cc.md#insn-006154fc)
- 新版 `00615478`（命令位置の公開資料なし） · `00615500`（命令位置の公開資料なし） · `0061553c`（命令位置の公開資料なし）

~~~diff
- 00615438 ["INT_ADD", "register:40f0:8", ["const:615438:8", "const:4:8"]]
- 00615438 ["CALL", null, ["ram:46c984:8"]]
+ 00615478 ["INT_ADD", "register:40f0:8", ["const:615478:8", "const:4:8"]]
+ 00615478 ["CALL", null, ["ram:46c9c4:8"]]
- 00615438 bytes 535df997
+ 00615478 bytes 535df997
- 006154c0 ["INT_ADD", "register:40f0:8", ["const:6154c0:8", "const:4:8"]]
- 006154c0 ["CALL", null, ["ram:46c984:8"]]
+ 00615500 ["INT_ADD", "register:40f0:8", ["const:615500:8", "const:4:8"]]
+ 00615500 ["CALL", null, ["ram:46c9c4:8"]]
- 006154c0 bytes 315df997
+ 00615500 bytes 315df997
- 006154fc ["INT_ADD", "register:40f0:8", ["const:6154fc:8", "const:4:8"]]
- 006154fc ["CALL", null, ["ram:46c984:8"]]
+ 0061553c ["INT_ADD", "register:40f0:8", ["const:61553c:8", "const:4:8"]]
+ 0061553c ["CALL", null, ["ram:46c9c4:8"]]
- 006154fc bytes 225df997
+ 0061553c bytes 225df997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b00e41bfb95c404c5aea90542af80453"></a>

### [`006158d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md) → [`00615910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md) FUN_00615910

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00604fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604fac.md) [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md)
- 新版 呼出元 4件 [`00604fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604fec.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

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
      "site": "00615a70",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00615a30",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "006159b4",
      "DATA",
      [
        "storage",
        "003c76a8",
        "fde_003c76a8",
        "dword"
      ]
    ],
    [
      "006159d4",
      "DATA",
      [
        "storage",
        "003c76a8",
        "fde_003c76a8",
        "dword"
      ]
    ],
    [
      "00615a10",
      "DATA",
      [
        "storage",
        "003c76a8",
        "fde_003c76a8",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006159b4",
      "DATA",
      [
        "storage",
        "003c76a8",
        null,
        "byte[15]"
      ]
    ],
    [
      "006159d4",
      "DATA",
      [
        "storage",
        "003c76a8",
        null,
        "byte[15]"
      ]
    ],
    [
      "00615a10",
      "DATA",
      [
        "storage",
        "003c76a8",
        null,
        "byte[15]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00615a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md#insn-00615a30) · [`00615a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md#insn-00615a70) · [`006158fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md#insn-006158fc)
- 新版 `00615a70`（命令位置の公開資料なし） · `00615ab0`（命令位置の公開資料なし） · `0061593c`（命令位置の公開資料なし）

~~~diff
- 00615a30 ["INT_ADD", "register:40f0:8", ["const:615a30:8", "const:4:8"]]
- 00615a30 ["CALL", null, ["ram:a65bf4:8"]]
+ 00615a70 ["INT_ADD", "register:40f0:8", ["const:615a70:8", "const:4:8"]]
+ 00615a70 ["CALL", null, ["ram:a65dec:8"]]
- 00615a30 bytes 71401194
+ 00615a70 bytes df401194
- 00615a70 ["INT_ADD", "register:40f0:8", ["const:615a70:8", "const:4:8"]]
- 00615a70 ["CALL", null, ["callee:00800378:8"]]
+ 00615ab0 ["INT_ADD", "register:40f0:8", ["const:615ab0:8", "const:4:8"]]
+ 00615ab0 ["CALL", null, ["callee:00800378:8"]]
- 00615a70 bytes 32aa0794
+ 00615ab0 bytes 32aa0794
- 006158fc ["INT_ADD", "register:40f0:8", ["const:6158fc:8", "const:4:8"]]
- 006158fc ["CALL", null, ["callee:00800378:8"]]
+ 0061593c ["INT_ADD", "register:40f0:8", ["const:61593c:8", "const:4:8"]]
+ 0061593c ["CALL", null, ["callee:00800378:8"]]
- 006158fc bytes 8faa0794
+ 0061593c bytes 8faa0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d83190cc226b6a537a59d6d3e9215d9e"></a>

### [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) → [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) FUN_00615ecc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00615c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615c90.md) [`00615ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615ea0.md) [`006412bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/006412bc.md) [`0079061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/0079061c.md) [`007938c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 7件 [`00615cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615cd0.md) [`00615ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ee0.md) [`006412fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006412fc.md) [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) [`00793908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793908.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00615ed8",
      "incomplete_value": false,
      "site": "00615edc",
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
      "definition_site": "00615e98",
      "incomplete_value": false,
      "site": "00615e9c",
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
      "00615ed8",
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
      "00615ed8",
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

- 旧版 [`00615e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md#insn-00615e9c) · [`00615e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md#insn-00615e98)
- 新版 `00615edc`（命令位置の公開資料なし） · `00615ed8`（命令位置の公開資料なし）

~~~diff
- 00615e9c ["INT_ADD", "register:40f0:8", ["const:615e9c:8", "const:4:8"]]
- 00615e9c ["CALL", null, ["callee:0043b778:8"]]
+ 00615edc ["INT_ADD", "register:40f0:8", ["const:615edc:8", "const:4:8"]]
+ 00615edc ["CALL", null, ["callee:0043b778:8"]]
- 00615e9c bytes 2796f897
+ 00615edc bytes 2796f897
- 00615e98 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00615e98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00615e98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00615e98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00615ed8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00615ed8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00615ed8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00615ed8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00615e98 bytes 00303c91
+ 00615ed8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8c601df42fb980c87b6a19e601e6cbb"></a>

### [`006161ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006161ac.md) → [`006161ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006161ec.md) FUN_006161ec

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
      "definition_site": "0061620c",
      "incomplete_value": false,
      "site": "00616210",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006161cc",
      "incomplete_value": false,
      "site": "006161d0",
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
            "const:5b8:8"
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
      "00616210",
      "DATA",
      [
        "storage",
        "00c715b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616210",
      "DATA",
      [
        "storage",
        "00c719b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006161c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006161ac.md#insn-006161c0) · [`006161cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006161ac.md#insn-006161cc)
- 新版 `00616200`（命令位置の公開資料なし） · `0061620c`（命令位置の公開資料なし）

~~~diff
- 006161c0 ["INT_ADD", "register:40f0:8", ["const:6161c0:8", "const:4:8"]]
- 006161c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00616200 ["INT_ADD", "register:40f0:8", ["const:616200:8", "const:4:8"]]
+ 00616200 ["CALL", null, ["callee:00c57e90:8"]]
- 006161c0 bytes 34061994
+ 00616200 bytes 24071994
- 006161cc ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 006161cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006161cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006161cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061620c ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 0061620c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061620c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061620c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006161cc bytes 08e11691
+ 0061620c bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03f3132a3f220e4672713cfb08ebcfb1"></a>

### [`00616204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616204.md) → [`00616244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616244.md) FUN_00616244

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00616308",
      "incomplete_value": true,
      "site": "00616308",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e76:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006162c8",
      "incomplete_value": true,
      "site": "006162c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e36:8"
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
      "definition_site": "00616450",
      "incomplete_value": false,
      "site": "00616450",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616410",
      "incomplete_value": false,
      "site": "00616410",
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
            "const:628:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616288",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616248",
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
      "00616288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006162a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006162f0",
      "READ",
      [
        "storage",
        "002b1e36",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00616288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006162a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006162f0",
      "READ",
      [
        "storage",
        "002b1e76",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616204.md#insn-00616248) · [`00616264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616204.md#insn-00616264) · [`00616308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616204.md#insn-00616308)
- 新版 `00616288`（命令位置の公開資料なし） · `006162a4`（命令位置の公開資料なし） · `00616348`（命令位置の公開資料なし）

~~~diff
- 00616248 ["INT_ADD", "register:40f0:8", ["const:616248:8", "const:4:8"]]
- 00616248 ["CALL", null, ["ram:47acb4:8"]]
+ 00616288 ["INT_ADD", "register:40f0:8", ["const:616288:8", "const:4:8"]]
+ 00616288 ["CALL", null, ["ram:47acf4:8"]]
- 00616248 bytes 9b92f997
+ 00616288 bytes 9b92f997
- 00616264 ["INT_ADD", "register:40f0:8", ["const:616264:8", "const:4:8"]]
- 00616264 ["CALL", null, ["ram:47acb4:8"]]
+ 006162a4 ["INT_ADD", "register:40f0:8", ["const:6162a4:8", "const:4:8"]]
+ 006162a4 ["CALL", null, ["ram:47acf4:8"]]
- 00616264 bytes 9492f997
+ 006162a4 bytes 9492f997
- 00616308 ["INT_ADD", "register:40f0:8", ["const:616308:8", "const:4:8"]]
- 00616308 ["CALL", null, ["callee:008b6f18:8"]]
+ 00616348 ["INT_ADD", "register:40f0:8", ["const:616348:8", "const:4:8"]]
+ 00616348 ["CALL", null, ["callee:008b6f18:8"]]
- 00616308 bytes f3820a94
+ 00616348 bytes f4820a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-565e289a37baf94248c3ee5cf1ae870f"></a>

### [`00616674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616674.md) → [`006166b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166b4.md) FUN_006166b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006166d8",
      "incomplete_value": true,
      "site": "006166dc",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616698",
      "incomplete_value": true,
      "site": "0061669c",
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
            "const:628:8"
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
      "006166dc",
      "DATA",
      [
        "storage",
        "00c71628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006166dc",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616674.md#insn-00616688) · [`00616698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616674.md#insn-00616698)
- 新版 `006166c8`（命令位置の公開資料なし） · `006166d8`（命令位置の公開資料なし）

~~~diff
- 00616688 ["INT_ADD", "register:40f0:8", ["const:616688:8", "const:4:8"]]
- 00616688 ["CALL", null, ["callee:00c57e90:8"]]
+ 006166c8 ["INT_ADD", "register:40f0:8", ["const:6166c8:8", "const:4:8"]]
+ 006166c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00616688 bytes 02051994
+ 006166c8 bytes f2051994
- 00616698 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00616698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006166d8 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 006166d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006166d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006166d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616698 bytes 08a11891
+ 006166d8 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e2d1431997e8ec48809c86bf154927"></a>

### [`006166b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166b4.md) → [`006166f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166f4.md) FUN_006166f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006166f8",
      "incomplete_value": false,
      "site": "006166fc",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006166b8",
      "incomplete_value": false,
      "site": "006166bc",
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
            "const:628:8"
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
      "006166fc",
      "DATA",
      [
        "storage",
        "00c71628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006166fc",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006166b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166b4.md#insn-006166b8)
- 新版 `006166f8`（命令位置の公開資料なし）

~~~diff
- 006166b8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 006166b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006166b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006166b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006166f8 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 006166f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006166f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006166f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006166b8 bytes 08a11891
+ 006166f8 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d942917dc4b7a8f3dfa58db6c16598"></a>

### [`006166dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md) → [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) FUN_0061671c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) [`00616908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616908.md) [`0061690c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/0061690c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`00616948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616948.md) [`0061694c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061694c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006167e8",
      "incomplete_value": false,
      "site": "006167e8",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006167a8",
      "incomplete_value": false,
      "site": "006167a8",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616760",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616720",
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
      "site": "006167c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616788",
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
      "00616760",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006167c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006167e8",
      "DATA",
      [
        "storage",
        "00c71698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616760",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006167c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006167e8",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md#insn-00616720) · [`00616788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md#insn-00616788) · [`0061672c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166dc.md#insn-0061672c)
- 新版 `00616760`（命令位置の公開資料なし） · `006167c8`（命令位置の公開資料なし） · `0061676c`（命令位置の公開資料なし）

~~~diff
- 00616720 ["INT_ADD", "register:40f0:8", ["const:616720:8", "const:4:8"]]
- 00616720 ["CALL", null, ["ram:47acb4:8"]]
+ 00616760 ["INT_ADD", "register:40f0:8", ["const:616760:8", "const:4:8"]]
+ 00616760 ["CALL", null, ["ram:47acf4:8"]]
- 00616720 bytes 6591f997
+ 00616760 bytes 6591f997
- 00616788 ["INT_ADD", "register:40f0:8", ["const:616788:8", "const:4:8"]]
- 00616788 ["CALL", null, ["ram:47acb4:8"]]
+ 006167c8 ["INT_ADD", "register:40f0:8", ["const:6167c8:8", "const:4:8"]]
+ 006167c8 ["CALL", null, ["ram:47acf4:8"]]
- 00616788 bytes 4b91f997
+ 006167c8 bytes 4b91f997
- 0061672c ["INT_ADD", "register:40f0:8", ["const:61672c:8", "const:4:8"]]
- 0061672c ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061676c ["INT_ADD", "register:40f0:8", ["const:61676c:8", "const:4:8"]]
+ 0061676c ["CALL", null, ["callee:0047cdd4:8"]]
- 0061672c bytes 9a99f997
+ 0061676c bytes 9a99f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194ba0f8e4f37eafd10b4388a9be74a3"></a>

### [`006168a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md) → [`006168e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006168e8.md) FUN_006168e8

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
      "definition_site": "0061690c",
      "incomplete_value": false,
      "site": "00616910",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006168cc",
      "incomplete_value": false,
      "site": "006168d0",
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
            "const:698:8"
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
      "00616910",
      "DATA",
      [
        "storage",
        "00c71698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616910",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006168bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md#insn-006168bc) · [`006168cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md#insn-006168cc)
- 新版 `006168fc`（命令位置の公開資料なし） · `0061690c`（命令位置の公開資料なし）

~~~diff
- 006168bc ["INT_ADD", "register:40f0:8", ["const:6168bc:8", "const:4:8"]]
- 006168bc ["CALL", null, ["callee:00c57e90:8"]]
+ 006168fc ["INT_ADD", "register:40f0:8", ["const:6168fc:8", "const:4:8"]]
+ 006168fc ["CALL", null, ["callee:00c57e90:8"]]
- 006168bc bytes 75041994
+ 006168fc bytes 65051994
- 006168cc ["COPY", "tmp:0:8", ["const:698:8"]]
- 006168cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006168cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006168cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061690c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0061690c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061690c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061690c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006168cc bytes 08611a91
+ 0061690c bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2176935317122ab10f12ad7d4ebc27ba"></a>

### [`006168e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168e8.md) → [`00616928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616928.md) FUN_00616928

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0061692c",
      "incomplete_value": false,
      "site": "00616930",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006168ec",
      "incomplete_value": false,
      "site": "006168f0",
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
      "00616930",
      "DATA",
      [
        "storage",
        "00c71698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616930",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006168ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168e8.md#insn-006168ec)
- 新版 `0061692c`（命令位置の公開資料なし）

~~~diff
- 006168ec ["COPY", "tmp:0:8", ["const:698:8"]]
- 006168ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006168ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006168ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061692c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0061692c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061692c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061692c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006168ec bytes 08611a91
+ 0061692c bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe1d561de618418847e83f13d773af6a"></a>

### [`00616910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md) → [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) FUN_00616950

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616aa8",
      "incomplete_value": false,
      "site": "00616aa8",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616a68",
      "incomplete_value": false,
      "site": "00616a68",
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
            "const:708:8"
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
      "definition_site": "00616b34",
      "incomplete_value": true,
      "site": "00616b48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00616af4",
      "incomplete_value": true,
      "site": "00616b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616b68",
      "incomplete_value": false,
      "site": "00616b68",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616b28",
      "incomplete_value": false,
      "site": "00616b28",
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
            "const:788:8"
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
      "0061698c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006169b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "006169bc",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0061698c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006169b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "006169bc",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[55]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md#insn-0061694c) · [`00616978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md#insn-00616978) · [`00616998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616910.md#insn-00616998)
- 新版 `0061698c`（命令位置の公開資料なし） · `006169b8`（命令位置の公開資料なし） · `006169d8`（命令位置の公開資料なし）

~~~diff
- 0061694c ["INT_ADD", "register:40f0:8", ["const:61694c:8", "const:4:8"]]
- 0061694c ["CALL", null, ["ram:47acb4:8"]]
+ 0061698c ["INT_ADD", "register:40f0:8", ["const:61698c:8", "const:4:8"]]
+ 0061698c ["CALL", null, ["ram:47acf4:8"]]
- 0061694c bytes da90f997
+ 0061698c bytes da90f997
- 00616978 ["INT_ADD", "register:40f0:8", ["const:616978:8", "const:4:8"]]
- 00616978 ["CALL", null, ["ram:71c420:8"]]
+ 006169b8 ["INT_ADD", "register:40f0:8", ["const:6169b8:8", "const:4:8"]]
+ 006169b8 ["CALL", null, ["ram:71c460:8"]]
- 00616978 bytes aa160494
+ 006169b8 bytes aa160494
- 00616998 ["INT_ADD", "register:40f0:8", ["const:616998:8", "const:4:8"]]
- 00616998 ["CALL", null, ["ram:47acb4:8"]]
+ 006169d8 ["INT_ADD", "register:40f0:8", ["const:6169d8:8", "const:4:8"]]
+ 006169d8 ["CALL", null, ["ram:47acf4:8"]]
- 00616998 bytes c790f997
+ 006169d8 bytes c790f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f13ad8fbf05ae539ec1df314b3a28fe"></a>

### [`00616e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616e0c.md) → [`00616e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e4c.md) FUN_00616e4c

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
      "definition_site": "00616e6c",
      "incomplete_value": false,
      "site": "00616e70",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616e2c",
      "incomplete_value": false,
      "site": "00616e30",
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
            "const:708:8"
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
      "00616e70",
      "DATA",
      [
        "storage",
        "00c71708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616e70",
      "DATA",
      [
        "storage",
        "00c71b08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616e0c.md#insn-00616e20) · [`00616e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616e0c.md#insn-00616e2c)
- 新版 `00616e60`（命令位置の公開資料なし） · `00616e6c`（命令位置の公開資料なし）

~~~diff
- 00616e20 ["INT_ADD", "register:40f0:8", ["const:616e20:8", "const:4:8"]]
- 00616e20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00616e60 ["INT_ADD", "register:40f0:8", ["const:616e60:8", "const:4:8"]]
+ 00616e60 ["CALL", null, ["callee:00c57e90:8"]]
- 00616e20 bytes 1c031994
+ 00616e60 bytes 0c041994
- 00616e2c ["COPY", "tmp:0:8", ["const:708:8"]]
- 00616e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616e6c ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00616e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616e2c bytes 08211c91
+ 00616e6c bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-840f70fb89ff791e1827d686cae5b728"></a>

### [`00616e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616e44.md) → [`00616e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e84.md) FUN_00616e84

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
      "definition_site": "00616e88",
      "incomplete_value": false,
      "site": "00616e8c",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616e48",
      "incomplete_value": false,
      "site": "00616e4c",
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
            "const:708:8"
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
      "00616e8c",
      "DATA",
      [
        "storage",
        "00c71708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616e8c",
      "DATA",
      [
        "storage",
        "00c71b08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616e44.md#insn-00616e48)
- 新版 `00616e88`（命令位置の公開資料なし）

~~~diff
- 00616e48 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00616e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616e88 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00616e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616e48 bytes 08211c91
+ 00616e88 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75f66c097352fd562bc4d787f10e4e43"></a>

### [`00616ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616ec4.md) → [`00616f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f04.md) FUN_00616f04

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
      "definition_site": "00616f24",
      "incomplete_value": false,
      "site": "00616f28",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616ee4",
      "incomplete_value": false,
      "site": "00616ee8",
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
            "const:788:8"
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
      "00616f28",
      "DATA",
      [
        "storage",
        "00c71788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616f28",
      "DATA",
      [
        "storage",
        "00c71b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616ec4.md#insn-00616ed8) · [`00616ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616ec4.md#insn-00616ee4)
- 新版 `00616f18`（命令位置の公開資料なし） · `00616f24`（命令位置の公開資料なし）

~~~diff
- 00616ed8 ["INT_ADD", "register:40f0:8", ["const:616ed8:8", "const:4:8"]]
- 00616ed8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00616f18 ["INT_ADD", "register:40f0:8", ["const:616f18:8", "const:4:8"]]
+ 00616f18 ["CALL", null, ["callee:00c57e90:8"]]
- 00616ed8 bytes ee021994
+ 00616f18 bytes de031994
- 00616ee4 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00616ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616f24 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00616f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616ee4 bytes 08211e91
+ 00616f24 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d300178a855866b18a7e75a09d921f05"></a>

### [`00616efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616efc.md) → [`00616f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f3c.md) FUN_00616f3c

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
      "definition_site": "00616f40",
      "incomplete_value": false,
      "site": "00616f44",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616f00",
      "incomplete_value": false,
      "site": "00616f04",
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
            "const:788:8"
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
      "00616f44",
      "DATA",
      [
        "storage",
        "00c71788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616f44",
      "DATA",
      [
        "storage",
        "00c71b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616efc.md#insn-00616f00)
- 新版 `00616f40`（命令位置の公開資料なし）

~~~diff
- 00616f00 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00616f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616f40 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00616f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616f00 bytes 08211e91
+ 00616f40 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ade951ffbf08431f8f9fd43af17a812"></a>

### [`00616f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md) → [`00616f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f5c.md) FUN_00616f5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "00616f8c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616f4c",
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
      "00616f8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00616f8c",
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

- 旧版 [`00616f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md#insn-00616f4c) · [`00616f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md#insn-00616f58) · [`00616f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616f1c.md#insn-00616f60)
- 新版 `00616f8c`（命令位置の公開資料なし） · `00616f98`（命令位置の公開資料なし） · `00616fa0`（命令位置の公開資料なし）

~~~diff
- 00616f4c ["INT_ADD", "register:40f0:8", ["const:616f4c:8", "const:4:8"]]
- 00616f4c ["CALL", null, ["ram:47acb4:8"]]
+ 00616f8c ["INT_ADD", "register:40f0:8", ["const:616f8c:8", "const:4:8"]]
+ 00616f8c ["CALL", null, ["ram:47acf4:8"]]
- 00616f4c bytes 5a8ff997
+ 00616f8c bytes 5a8ff997
- 00616f58 ["INT_ADD", "register:40f0:8", ["const:616f58:8", "const:4:8"]]
- 00616f58 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00616f98 ["INT_ADD", "register:40f0:8", ["const:616f98:8", "const:4:8"]]
+ 00616f98 ["CALL", null, ["callee:0047cdd4:8"]]
- 00616f58 bytes 8f97f997
+ 00616f98 bytes 8f97f997
- 00616f60 ["INT_ADD", "register:40f0:8", ["const:616f60:8", "const:4:8"]]
- 00616f60 ["CALL", null, ["callee:008b9178:8"]]
+ 00616fa0 ["INT_ADD", "register:40f0:8", ["const:616fa0:8", "const:4:8"]]
+ 00616fa0 ["CALL", null, ["callee:008b9178:8"]]
- 00616f60 bytes 75880a94
+ 00616fa0 bytes 76880a94
~~~


<a id="compare-702f98e26338014b2be9d28b93479349"></a>

### [`00616fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616fb0.md) → [`00616ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616ff0.md) FUN_00616ff0

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
      "definition_site": "00617004",
      "incomplete_value": false,
      "site": "00617008",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616fc4",
      "incomplete_value": false,
      "site": "00616fc8",
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
            "const:838:8"
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
      "00617008",
      "DATA",
      [
        "storage",
        "00c71838",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617008",
      "DATA",
      [
        "storage",
        "00c71c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616fb0.md#insn-00616fbc) · [`00616fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616fb0.md#insn-00616fc4)
- 新版 `00616ffc`（命令位置の公開資料なし） · `00617004`（命令位置の公開資料なし）

~~~diff
- 00616fbc ["INT_ADD", "register:40f0:8", ["const:616fbc:8", "const:4:8"]]
- 00616fbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00616ffc ["INT_ADD", "register:40f0:8", ["const:616ffc:8", "const:4:8"]]
+ 00616ffc ["CALL", null, ["callee:00c57e90:8"]]
- 00616fbc bytes b5021994
+ 00616ffc bytes a5031994
- 00616fc4 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00616fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00617004 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00617004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00617004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00617004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616fc4 bytes 08e12091
+ 00617004 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87e590e9b7de73be0adaadeb2862418"></a>

### [`0061701c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061701c.md) → [`0061705c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/0061705c.md) FUN_0061705c

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
      "definition_site": "00617080",
      "incomplete_value": false,
      "site": "00617080",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00617040",
      "incomplete_value": false,
      "site": "00617040",
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
      "00617080",
      "DATA",
      [
        "storage",
        "00c718c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617080",
      "DATA",
      [
        "storage",
        "00c71cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061701c.md#insn-00617030) · [`0061703c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061701c.md#insn-0061703c)
- 新版 `00617070`（命令位置の公開資料なし） · `0061707c`（命令位置の公開資料なし）

~~~diff
- 00617030 ["INT_ADD", "register:40f0:8", ["const:617030:8", "const:4:8"]]
- 00617030 ["CALL", null, ["callee:00c57e90:8"]]
+ 00617070 ["INT_ADD", "register:40f0:8", ["const:617070:8", "const:4:8"]]
+ 00617070 ["CALL", null, ["callee:00c57e90:8"]]
- 00617030 bytes 98021994
+ 00617070 bytes 88031994
- 0061703c ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0061703c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061703c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061703c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061707c ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 0061707c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061707c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061707c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061703c bytes 08212391
+ 0061707c bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce285da73873686a0ea4b404d56346b7"></a>

### [`00617050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617050.md) → [`00617090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617090.md) FUN_00617090

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
      "definition_site": "0061709c",
      "incomplete_value": false,
      "site": "0061709c",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061705c",
      "incomplete_value": false,
      "site": "0061705c",
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
            "const:8c8:8"
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
      "0061709c",
      "DATA",
      [
        "storage",
        "00c718c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061709c",
      "DATA",
      [
        "storage",
        "00c71cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617050.md#insn-00617058)
- 新版 `00617098`（命令位置の公開資料なし）

~~~diff
- 00617058 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00617058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00617058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00617058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00617098 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00617098 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00617098 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00617098 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00617058 bytes 29212391
+ 00617098 bytes 29213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d155530534ac740692c270515dd60c1a"></a>

### [`0061706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md) → [`006170ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md) FUN_006170ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`00820074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00820/00820074.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`008200b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/008200b4.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "006170d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617090",
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
      "site": "006170ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006170ac",
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
      "site": "0061711c",
      "value": [
        "leaf",
        "ram:8200b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006170dc",
      "value": [
        "leaf",
        "ram:820074:8"
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
      "006170d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006170ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0061711c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00820074"
      ]
    ]
  ],
  "added": [
    [
      "006170d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006170ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061711c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008200b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md#insn-00617090) · [`006170ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md#insn-006170ac) · [`006170dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061706c.md#insn-006170dc)
- 新版 `006170d0`（命令位置の公開資料なし） · `006170ec`（命令位置の公開資料なし） · `0061711c`（命令位置の公開資料なし）

~~~diff
- 00617090 ["INT_ADD", "register:40f0:8", ["const:617090:8", "const:4:8"]]
- 00617090 ["CALL", null, ["ram:47acb4:8"]]
+ 006170d0 ["INT_ADD", "register:40f0:8", ["const:6170d0:8", "const:4:8"]]
+ 006170d0 ["CALL", null, ["ram:47acf4:8"]]
- 00617090 bytes 098ff997
+ 006170d0 bytes 098ff997
- 006170ac ["INT_ADD", "register:40f0:8", ["const:6170ac:8", "const:4:8"]]
- 006170ac ["CALL", null, ["ram:47acb4:8"]]
+ 006170ec ["INT_ADD", "register:40f0:8", ["const:6170ec:8", "const:4:8"]]
+ 006170ec ["CALL", null, ["ram:47acf4:8"]]
- 006170ac bytes 028ff997
+ 006170ec bytes 028ff997
- 006170dc ["INT_ADD", "register:40f0:8", ["const:6170dc:8", "const:4:8"]]
- 006170dc ["CALL", null, ["ram:820074:8"]]
+ 0061711c ["INT_ADD", "register:40f0:8", ["const:61711c:8", "const:4:8"]]
+ 0061711c ["CALL", null, ["ram:8200b4:8"]]
- 006170dc bytes e6230894
+ 0061711c bytes e6230894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6c776e67dbdf32e317c331461583f8"></a>

### [`00617330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md) → [`00617370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md) FUN_00617370

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0061716c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061716c.md) [`00617330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md) [`0061bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md)
- 新版 呼出元 3件 [`006171ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006171ac.md) [`00617370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md) [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006174e0",
      "incomplete_value": true,
      "site": "006174ec",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006174a0",
      "incomplete_value": true,
      "site": "006174ac",
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
      "definition_site": "00617598",
      "incomplete_value": false,
      "site": "006175a0",
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
      "definition_site": "00617558",
      "incomplete_value": false,
      "site": "00617560",
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
      "definition_site": "00617664",
      "incomplete_value": false,
      "site": "00617674",
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
      "definition_site": "00617624",
      "incomplete_value": false,
      "site": "00617634",
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
      "006174e0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00617598",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "006175b0",
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
      "006174e0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00617598",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006175b0",
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

- 旧版 [`006174ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md#insn-006174ac) · [`00617560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md#insn-00617560) · [`00617634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md#insn-00617634)
- 新版 `006174ec`（命令位置の公開資料なし） · `006175a0`（命令位置の公開資料なし） · `00617674`（命令位置の公開資料なし）

~~~diff
- 006174ac ["INT_ADD", "register:40f0:8", ["const:6174ac:8", "const:4:8"]]
- 006174ac ["CALL", null, ["callee:00441e94:8"]]
+ 006174ec ["INT_ADD", "register:40f0:8", ["const:6174ec:8", "const:4:8"]]
+ 006174ec ["CALL", null, ["callee:00441e94:8"]]
- 006174ac bytes 6aaaf897
+ 006174ec bytes 6aaaf897
- 00617560 ["INT_ADD", "register:40f0:8", ["const:617560:8", "const:4:8"]]
- 00617560 ["CALL", null, ["callee:00441e94:8"]]
+ 006175a0 ["INT_ADD", "register:40f0:8", ["const:6175a0:8", "const:4:8"]]
+ 006175a0 ["CALL", null, ["callee:00441e94:8"]]
- 00617560 bytes 3daaf897
+ 006175a0 bytes 3daaf897
- 00617634 ["INT_ADD", "register:40f0:8", ["const:617634:8", "const:4:8"]]
- 00617634 ["CALL", null, ["callee:004427f4:8"]]
+ 00617674 ["INT_ADD", "register:40f0:8", ["const:617674:8", "const:4:8"]]
+ 00617674 ["CALL", null, ["callee:004427f4:8"]]
- 00617634 bytes 60acf897
+ 00617674 bytes 60acf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd9c3150cf0340c73c101829a5026bc9"></a>

### [`00617f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f04.md) → [`00617f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f44.md) FUN_00617f44

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
      "definition_site": "00617f68",
      "incomplete_value": false,
      "site": "00617f68",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00617f28",
      "incomplete_value": false,
      "site": "00617f28",
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
            "const:948:8"
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
      "00617f68",
      "DATA",
      [
        "storage",
        "00c71948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617f68",
      "DATA",
      [
        "storage",
        "00c71d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f04.md#insn-00617f18) · [`00617f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f04.md#insn-00617f24)
- 新版 `00617f58`（命令位置の公開資料なし） · `00617f64`（命令位置の公開資料なし）

~~~diff
- 00617f18 ["INT_ADD", "register:40f0:8", ["const:617f18:8", "const:4:8"]]
- 00617f18 ["CALL", null, ["callee:00c57e90:8"]]
+ 00617f58 ["INT_ADD", "register:40f0:8", ["const:617f58:8", "const:4:8"]]
+ 00617f58 ["CALL", null, ["callee:00c57e90:8"]]
- 00617f18 bytes defe1894
+ 00617f58 bytes ceff1894
- 00617f24 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00617f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00617f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00617f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00617f64 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00617f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00617f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00617f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00617f24 bytes 08212591
+ 00617f64 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba465a77d5214248dc680d47a9625a85"></a>

### [`00617f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f54.md) → [`00617f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f94.md) FUN_00617f94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) [`00618188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618188.md) [`0061818c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/0061818c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`006181c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181c8.md) [`006181cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181cc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00618084",
      "incomplete_value": false,
      "site": "00618084",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618044",
      "incomplete_value": false,
      "site": "00618044",
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
            "const:9b8:8"
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
      "site": "00617fd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617f90",
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
      "site": "00617fec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617fac",
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
      "00617fd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00617fec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00618084",
      "DATA",
      [
        "storage",
        "00c719b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617fd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00617fec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00618084",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f54.md#insn-00617f90) · [`00617fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f54.md#insn-00617fac) · [`00618004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617f54.md#insn-00618004)
- 新版 `00617fd0`（命令位置の公開資料なし） · `00617fec`（命令位置の公開資料なし） · `00618044`（命令位置の公開資料なし）

~~~diff
- 00617f90 ["INT_ADD", "register:40f0:8", ["const:617f90:8", "const:4:8"]]
- 00617f90 ["CALL", null, ["ram:47acb4:8"]]
+ 00617fd0 ["INT_ADD", "register:40f0:8", ["const:617fd0:8", "const:4:8"]]
+ 00617fd0 ["CALL", null, ["ram:47acf4:8"]]
- 00617f90 bytes 498bf997
+ 00617fd0 bytes 498bf997
- 00617fac ["INT_ADD", "register:40f0:8", ["const:617fac:8", "const:4:8"]]
- 00617fac ["CALL", null, ["ram:47acb4:8"]]
+ 00617fec ["INT_ADD", "register:40f0:8", ["const:617fec:8", "const:4:8"]]
+ 00617fec ["CALL", null, ["ram:47acf4:8"]]
- 00617fac bytes 428bf997
+ 00617fec bytes 428bf997
- 00618004 ["INT_ADD", "register:40f0:8", ["const:618004:8", "const:4:8"]]
- 00618004 ["CALL", null, ["callee:008b79c8:8"]]
+ 00618044 ["INT_ADD", "register:40f0:8", ["const:618044:8", "const:4:8"]]
+ 00618044 ["CALL", null, ["callee:008b79c8:8"]]
- 00618004 bytes 607e0a94
+ 00618044 bytes 617e0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15be2ab8972c23b2bf181f100af3cfdc"></a>

### [`00618128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618128.md) → [`00618168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618168.md) FUN_00618168

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
      "definition_site": "0061818c",
      "incomplete_value": false,
      "site": "00618190",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061814c",
      "incomplete_value": false,
      "site": "00618150",
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
            "const:9b8:8"
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
      "00618190",
      "DATA",
      [
        "storage",
        "00c719b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00618190",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061813c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618128.md#insn-0061813c) · [`0061814c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618128.md#insn-0061814c)
- 新版 `0061817c`（命令位置の公開資料なし） · `0061818c`（命令位置の公開資料なし）

~~~diff
- 0061813c ["INT_ADD", "register:40f0:8", ["const:61813c:8", "const:4:8"]]
- 0061813c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061817c ["INT_ADD", "register:40f0:8", ["const:61817c:8", "const:4:8"]]
+ 0061817c ["CALL", null, ["callee:00c57e90:8"]]
- 0061813c bytes 55fe1894
+ 0061817c bytes 45ff1894
- 0061814c ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 0061814c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061814c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061814c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061818c ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0061818c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061818c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061818c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061814c bytes 08e12691
+ 0061818c bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57c9ff13d8b718a67e41ebb588daa39"></a>

### [`00618168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618168.md) → [`006181a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181a8.md) FUN_006181a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006181ac",
      "incomplete_value": false,
      "site": "006181b0",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061816c",
      "incomplete_value": false,
      "site": "00618170",
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
            "const:9b8:8"
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
      "006181b0",
      "DATA",
      [
        "storage",
        "00c719b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006181b0",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061816c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618168.md#insn-0061816c)
- 新版 `006181ac`（命令位置の公開資料なし）

~~~diff
- 0061816c ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 0061816c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061816c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061816c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006181ac ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 006181ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006181ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006181ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061816c bytes 08e12691
+ 006181ac bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e935e134b9b464025c3236a0fd4c2493"></a>

### [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) → [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) FUN_00618200

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00618190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/00618190.md) · 呼出先 31件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)
- 新版 呼出元 1件 [`006181d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181d0.md) · 呼出先 31件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.93% / 新版 93.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `call_target` 4件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006182c4",
      "incomplete_value": false,
      "site": "006182c4",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618284",
      "incomplete_value": false,
      "site": "00618284",
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
            "const:a28:8"
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
      "definition_site": "00618494",
      "incomplete_value": true,
      "site": "00618494",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:edf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618454",
      "incomplete_value": true,
      "site": "00618454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006184c8",
      "incomplete_value": true,
      "site": "006184c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618488",
      "incomplete_value": true,
      "site": "00618488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:834:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00618230",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00618240",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ],
    [
      "00618240",
      "READ",
      [
        "storage",
        "00ca487c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00618230",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00618240",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ],
    [
      "00618240",
      "READ",
      [
        "storage",
        "00ca4c7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00618364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md#insn-00618364) · [`00618374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md#insn-00618374) · [`00618620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md#insn-00618620)
- 新版 `006183a4`（命令位置の公開資料なし） · `006183b4`（命令位置の公開資料なし） · `00618660`（命令位置の公開資料なし）

~~~diff
- 00618364 ["INT_ADD", "register:40f0:8", ["const:618364:8", "const:4:8"]]
- 00618364 ["CALL", null, ["ram:802b4c:8"]]
+ 006183a4 ["INT_ADD", "register:40f0:8", ["const:6183a4:8", "const:4:8"]]
+ 006183a4 ["CALL", null, ["ram:802b8c:8"]]
- 00618364 bytes faa90794
+ 006183a4 bytes faa90794
- 00618374 ["INT_ADD", "register:40f0:8", ["const:618374:8", "const:4:8"]]
- 00618374 ["CALL", null, ["ram:8039f8:8"]]
+ 006183b4 ["INT_ADD", "register:40f0:8", ["const:6183b4:8", "const:4:8"]]
+ 006183b4 ["CALL", null, ["ram:803a38:8"]]
- 00618374 bytes a1ad0794
+ 006183b4 bytes a1ad0794
- 00618620 ["COPY", "register:0:8", ["register:4040:8"]]
- 00618620 ["INT_ADD", "register:40f0:8", ["const:618620:8", "const:4:8"]]
- 00618620 ["CALLIND", null, ["register:0:8"]]
+ 00618660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00618660 ["INT_ADD", "register:40f0:8", ["const:618660:8", "const:4:8"]]
+ 00618660 ["CALLIND", null, ["register:0:8"]]
- 00618620 bytes 00013fd6
+ 00618660 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb58f2db58277bf6f8ab05cd85465596"></a>

### [`0061a034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md) → [`0061a074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a074.md) FUN_0061a074

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
      "definition_site": "0061a094",
      "incomplete_value": false,
      "site": "0061a098",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061a054",
      "incomplete_value": false,
      "site": "0061a058",
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
            "const:a28:8"
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
      "0061a098",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061a098",
      "DATA",
      [
        "storage",
        "00c71e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061a048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md#insn-0061a048) · [`0061a054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md#insn-0061a054)
- 新版 `0061a088`（命令位置の公開資料なし） · `0061a094`（命令位置の公開資料なし）

~~~diff
- 0061a048 ["INT_ADD", "register:40f0:8", ["const:61a048:8", "const:4:8"]]
- 0061a048 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061a088 ["INT_ADD", "register:40f0:8", ["const:61a088:8", "const:4:8"]]
+ 0061a088 ["CALL", null, ["callee:00c57e90:8"]]
- 0061a048 bytes 92f61894
+ 0061a088 bytes 82f71894
- 0061a054 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0061a054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061a054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061a054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061a094 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0061a094 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a094 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a094 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061a054 bytes 08a12891
+ 0061a094 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4cf6b4af60c523dcc76a70765238e1"></a>

### [`0061a06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a06c.md) → [`0061a0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a0ac.md) FUN_0061a0ac

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
      "definition_site": "0061a0b0",
      "incomplete_value": false,
      "site": "0061a0b4",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061a070",
      "incomplete_value": false,
      "site": "0061a074",
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
            "const:a28:8"
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
      "0061a0b4",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061a0b4",
      "DATA",
      [
        "storage",
        "00c71e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a06c.md#insn-0061a070)
- 新版 `0061a0b0`（命令位置の公開資料なし）

~~~diff
- 0061a070 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0061a070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061a070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061a070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061a0b0 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0061a0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061a070 bytes 08a12891
+ 0061a0b0 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f172319ed2ed672dd9b5e287e02164f"></a>

### [`0061a2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md) → [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) FUN_0061a314

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0061a108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a108.md) [`0061a2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md) [`0097c30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097c/0097c30c.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`0061a148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a148.md) [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) [`0097c4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097c/0097c4a8.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061a540",
      "incomplete_value": false,
      "site": "0061a548",
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
      "definition_site": "0061a500",
      "incomplete_value": false,
      "site": "0061a508",
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
      "definition_site": "0061a558",
      "incomplete_value": false,
      "site": "0061a568",
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
      "definition_site": "0061a518",
      "incomplete_value": false,
      "site": "0061a528",
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
      "definition_site": "0061a60c",
      "incomplete_value": false,
      "site": "0061a61c",
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
      "definition_site": "0061a5cc",
      "incomplete_value": false,
      "site": "0061a5dc",
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
      "0061a488",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0061a540",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0061a558",
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
      "0061a488",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061a540",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061a558",
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

- 旧版 [`0061a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md#insn-0061a508) · [`0061a528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md#insn-0061a528) · [`0061a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md#insn-0061a5dc)
- 新版 `0061a548`（命令位置の公開資料なし） · `0061a568`（命令位置の公開資料なし） · `0061a61c`（命令位置の公開資料なし）

~~~diff
- 0061a508 ["INT_ADD", "register:40f0:8", ["const:61a508:8", "const:4:8"]]
- 0061a508 ["CALL", null, ["callee:00441e94:8"]]
+ 0061a548 ["INT_ADD", "register:40f0:8", ["const:61a548:8", "const:4:8"]]
+ 0061a548 ["CALL", null, ["callee:00441e94:8"]]
- 0061a508 bytes 539ef897
+ 0061a548 bytes 539ef897
- 0061a528 ["INT_ADD", "register:40f0:8", ["const:61a528:8", "const:4:8"]]
- 0061a528 ["CALL", null, ["callee:004427f4:8"]]
+ 0061a568 ["INT_ADD", "register:40f0:8", ["const:61a568:8", "const:4:8"]]
+ 0061a568 ["CALL", null, ["callee:004427f4:8"]]
- 0061a528 bytes a3a0f897
+ 0061a568 bytes a3a0f897
- 0061a5dc ["INT_ADD", "register:40f0:8", ["const:61a5dc:8", "const:4:8"]]
- 0061a5dc ["CALL", null, ["callee:004427f4:8"]]
+ 0061a61c ["INT_ADD", "register:40f0:8", ["const:61a61c:8", "const:4:8"]]
+ 0061a61c ["CALL", null, ["callee:004427f4:8"]]
- 0061a5dc bytes 76a0f897
+ 0061a61c bytes 76a0f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcedde3cefbd2b79e5bf1829303fbf7a"></a>

### [`0061aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) → [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) FUN_0061aef8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0061a2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a2d4.md) [`0061aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) [`0072c340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c340.md) [`007f0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md)
- 新版 呼出元 4件 [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) [`0072c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061b054",
      "incomplete_value": false,
      "site": "0061b05c",
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
      "definition_site": "0061b014",
      "incomplete_value": false,
      "site": "0061b01c",
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
      "definition_site": "0061b078",
      "incomplete_value": false,
      "site": "0061b084",
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
      "definition_site": "0061b038",
      "incomplete_value": false,
      "site": "0061b044",
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
      "definition_site": "0061b1c4",
      "incomplete_value": false,
      "site": "0061b1d0",
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
      "definition_site": "0061b184",
      "incomplete_value": false,
      "site": "0061b190",
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
      "0061b054",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0061b078",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0061b1ac",
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
      "0061b054",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061b078",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0061b1ac",
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

- 旧版 [`0061b01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md#insn-0061b01c) · [`0061b044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md#insn-0061b044) · [`0061b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md#insn-0061b190)
- 新版 `0061b05c`（命令位置の公開資料なし） · `0061b084`（命令位置の公開資料なし） · `0061b1d0`（命令位置の公開資料なし）

~~~diff
- 0061b01c ["INT_ADD", "register:40f0:8", ["const:61b01c:8", "const:4:8"]]
- 0061b01c ["CALL", null, ["callee:00441e94:8"]]
+ 0061b05c ["INT_ADD", "register:40f0:8", ["const:61b05c:8", "const:4:8"]]
+ 0061b05c ["CALL", null, ["callee:00441e94:8"]]
- 0061b01c bytes 8e9bf897
+ 0061b05c bytes 8e9bf897
- 0061b044 ["INT_ADD", "register:40f0:8", ["const:61b044:8", "const:4:8"]]
- 0061b044 ["CALL", null, ["callee:004427f4:8"]]
+ 0061b084 ["INT_ADD", "register:40f0:8", ["const:61b084:8", "const:4:8"]]
+ 0061b084 ["CALL", null, ["callee:004427f4:8"]]
- 0061b044 bytes dc9df897
+ 0061b084 bytes dc9df897
- 0061b190 ["INT_ADD", "register:40f0:8", ["const:61b190:8", "const:4:8"]]
- 0061b190 ["CALL", null, ["callee:004427f4:8"]]
+ 0061b1d0 ["INT_ADD", "register:40f0:8", ["const:61b1d0:8", "const:4:8"]]
+ 0061b1d0 ["CALL", null, ["callee:004427f4:8"]]
- 0061b190 bytes 899df897
+ 0061b1d0 bytes 899df897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e0b70e166d277af3ef14a0fae58827"></a>

### [`0061bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md) → [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) FUN_0061bbd0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0061b95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061b95c.md) [`0061bb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md) [`00b31730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b31/00b31730.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`0061b99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061b99c.md) [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) [`00b31b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31b58.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061bd44",
      "incomplete_value": false,
      "site": "0061bd4c",
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
      "definition_site": "0061bd04",
      "incomplete_value": false,
      "site": "0061bd0c",
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
      "definition_site": "0061bdf8",
      "incomplete_value": false,
      "site": "0061be00",
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
      "definition_site": "0061bdb8",
      "incomplete_value": false,
      "site": "0061bdc0",
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
      "definition_site": "0061be10",
      "incomplete_value": false,
      "site": "0061be20",
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
      "definition_site": "0061bdd0",
      "incomplete_value": false,
      "site": "0061bde0",
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
      "0061bd44",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0061bdf8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0061be10",
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
      "0061bd44",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061bdf8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061be10",
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

- 旧版 [`0061bd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md#insn-0061bd0c) · [`0061bdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md#insn-0061bdc0) · [`0061bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061b/0061bb90.md#insn-0061bde0)
- 新版 `0061bd4c`（命令位置の公開資料なし） · `0061be00`（命令位置の公開資料なし） · `0061be20`（命令位置の公開資料なし）

~~~diff
- 0061bd0c ["INT_ADD", "register:40f0:8", ["const:61bd0c:8", "const:4:8"]]
- 0061bd0c ["CALL", null, ["callee:00441e94:8"]]
+ 0061bd4c ["INT_ADD", "register:40f0:8", ["const:61bd4c:8", "const:4:8"]]
+ 0061bd4c ["CALL", null, ["callee:00441e94:8"]]
- 0061bd0c bytes 5298f897
+ 0061bd4c bytes 5298f897
- 0061bdc0 ["INT_ADD", "register:40f0:8", ["const:61bdc0:8", "const:4:8"]]
- 0061bdc0 ["CALL", null, ["callee:00441e94:8"]]
+ 0061be00 ["INT_ADD", "register:40f0:8", ["const:61be00:8", "const:4:8"]]
+ 0061be00 ["CALL", null, ["callee:00441e94:8"]]
- 0061bdc0 bytes 2598f897
+ 0061be00 bytes 2598f897
- 0061bde0 ["INT_ADD", "register:40f0:8", ["const:61bde0:8", "const:4:8"]]
- 0061bde0 ["CALL", null, ["callee:004427f4:8"]]
+ 0061be20 ["INT_ADD", "register:40f0:8", ["const:61be20:8", "const:4:8"]]
+ 0061be20 ["CALL", null, ["callee:004427f4:8"]]
- 0061bde0 bytes 759af897
+ 0061be20 bytes 759af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6a75bfa1c494d87052361618e75e94"></a>

### [`0061c99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c99c.md) → [`0061c9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061c9dc.md) FUN_0061c9dc

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
      "definition_site": "0061c9f0",
      "incomplete_value": false,
      "site": "0061c9f4",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061c9b0",
      "incomplete_value": false,
      "site": "0061c9b4",
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
            "const:ac8:8"
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
      "0061c9f4",
      "DATA",
      [
        "storage",
        "00c71ac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061c9f4",
      "DATA",
      [
        "storage",
        "00c71ec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061c9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c99c.md#insn-0061c9a8) · [`0061c9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c99c.md#insn-0061c9b0)
- 新版 `0061c9e8`（命令位置の公開資料なし） · `0061c9f0`（命令位置の公開資料なし）

~~~diff
- 0061c9a8 ["INT_ADD", "register:40f0:8", ["const:61c9a8:8", "const:4:8"]]
- 0061c9a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061c9e8 ["INT_ADD", "register:40f0:8", ["const:61c9e8:8", "const:4:8"]]
+ 0061c9e8 ["CALL", null, ["callee:00c57e90:8"]]
- 0061c9a8 bytes 3aec1894
+ 0061c9e8 bytes 2aed1894
- 0061c9b0 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 0061c9b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061c9b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061c9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061c9f0 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 0061c9f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061c9f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061c9f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061c9b0 bytes 08212b91
+ 0061c9f0 bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6fb3a388aa137b88b1c0d867ac79f9"></a>

### [`0061c9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md) → [`0061ca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca18.md) FUN_0061ca18

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
      "site": "0061ca3c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061c9fc",
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
      "0061ca3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061ca3c",
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

- 旧版 [`0061c9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md#insn-0061c9fc) · [`0061ca08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061c9d8.md#insn-0061ca08)
- 新版 `0061ca3c`（命令位置の公開資料なし） · `0061ca48`（命令位置の公開資料なし）

~~~diff
- 0061c9fc ["INT_ADD", "register:40f0:8", ["const:61c9fc:8", "const:4:8"]]
- 0061c9fc ["CALL", null, ["ram:47acb4:8"]]
+ 0061ca3c ["INT_ADD", "register:40f0:8", ["const:61ca3c:8", "const:4:8"]]
+ 0061ca3c ["CALL", null, ["ram:47acf4:8"]]
- 0061c9fc bytes ae78f997
+ 0061ca3c bytes ae78f997
- 0061ca08 ["INT_ADD", "register:40f0:8", ["const:61ca08:8", "const:4:8"]]
- 0061ca08 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061ca48 ["INT_ADD", "register:40f0:8", ["const:61ca48:8", "const:4:8"]]
+ 0061ca48 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061ca08 bytes e380f997
+ 0061ca48 bytes e380f997
~~~


<a id="compare-89580b980726252025789a71133122cb"></a>

### [`0061cae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cae0.md) → [`0061cb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb20.md) FUN_0061cb20

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
      "definition_site": "0061cb34",
      "incomplete_value": true,
      "site": "0061cb38",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061caf4",
      "incomplete_value": true,
      "site": "0061caf8",
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
            "const:bd8:8"
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
      "0061cb38",
      "DATA",
      [
        "storage",
        "00c71bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cb38",
      "DATA",
      [
        "storage",
        "00c71fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061caec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cae0.md#insn-0061caec) · [`0061caf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cae0.md#insn-0061caf4)
- 新版 `0061cb2c`（命令位置の公開資料なし） · `0061cb34`（命令位置の公開資料なし）

~~~diff
- 0061caec ["INT_ADD", "register:40f0:8", ["const:61caec:8", "const:4:8"]]
- 0061caec ["CALL", null, ["callee:00c57e90:8"]]
+ 0061cb2c ["INT_ADD", "register:40f0:8", ["const:61cb2c:8", "const:4:8"]]
+ 0061cb2c ["CALL", null, ["callee:00c57e90:8"]]
- 0061caec bytes e9eb1894
+ 0061cb2c bytes d9ec1894
- 0061caf4 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 0061caf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061caf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061caf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cb34 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0061cb34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061caf4 bytes 08612f91
+ 0061cb34 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3d794a5b4cc08da02a5fa0671dac70d"></a>

### [`0061cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cb1c.md) → [`0061cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb5c.md) FUN_0061cb5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061cb84",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061cb44",
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
      "0061cb84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061cb84",
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

- 旧版 [`0061cb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cb1c.md#insn-0061cb44) · [`0061cb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cb1c.md#insn-0061cb50) · [`0061cb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cb1c.md#insn-0061cb68)
- 新版 `0061cb84`（命令位置の公開資料なし） · `0061cb90`（命令位置の公開資料なし） · `0061cba8`（命令位置の公開資料なし）

~~~diff
- 0061cb44 ["INT_ADD", "register:40f0:8", ["const:61cb44:8", "const:4:8"]]
- 0061cb44 ["CALL", null, ["ram:47acb4:8"]]
+ 0061cb84 ["INT_ADD", "register:40f0:8", ["const:61cb84:8", "const:4:8"]]
+ 0061cb84 ["CALL", null, ["ram:47acf4:8"]]
- 0061cb44 bytes 5c78f997
+ 0061cb84 bytes 5c78f997
- 0061cb50 ["INT_ADD", "register:40f0:8", ["const:61cb50:8", "const:4:8"]]
- 0061cb50 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061cb90 ["INT_ADD", "register:40f0:8", ["const:61cb90:8", "const:4:8"]]
+ 0061cb90 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061cb50 bytes 9180f997
+ 0061cb90 bytes 9180f997
- 0061cb68 ["INT_ADD", "register:40f0:8", ["const:61cb68:8", "const:4:8"]]
- 0061cb68 ["CALL", null, ["callee:008514f8:8"]]
+ 0061cba8 ["INT_ADD", "register:40f0:8", ["const:61cba8:8", "const:4:8"]]
+ 0061cba8 ["CALL", null, ["callee:008514f8:8"]]
- 0061cb68 bytes 54d20894
+ 0061cba8 bytes 54d20894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-956ac425f85db40403312e42fb03fe38"></a>

### [`0061cc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cc78.md) → [`0061ccb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccb8.md) FUN_0061ccb8

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
      "definition_site": "0061cccc",
      "incomplete_value": false,
      "site": "0061ccd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cc8c",
      "incomplete_value": false,
      "site": "0061cc90",
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
            "const:c58:8"
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
      "0061ccd0",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ccd0",
      "DATA",
      [
        "storage",
        "00c72058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cc78.md#insn-0061cc84) · [`0061cc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cc78.md#insn-0061cc88) · [`0061cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cc78.md#insn-0061cc8c)
- 新版 `0061ccc4`（命令位置の公開資料なし） · `0061ccc8`（命令位置の公開資料なし） · `0061cccc`（命令位置の公開資料なし）

~~~diff
- 0061cc84 ["INT_ADD", "register:40f0:8", ["const:61cc84:8", "const:4:8"]]
- 0061cc84 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061ccc4 ["INT_ADD", "register:40f0:8", ["const:61ccc4:8", "const:4:8"]]
+ 0061ccc4 ["CALL", null, ["callee:00c57e90:8"]]
- 0061cc84 bytes 83eb1894
+ 0061ccc4 bytes 73ec1894
- 0061cc88 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061ccc8 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061cc88 bytes a83200b0
+ 0061ccc8 bytes a83200d0
- 0061cc8c ["COPY", "tmp:0:8", ["const:c58:8"]]
- 0061cc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061cc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061cc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cccc ["COPY", "tmp:0:8", ["const:58:8"]]
+ 0061cccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061cc8c bytes 08613191
+ 0061cccc bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36bbef1b217dd868d56a699905b5e1d"></a>

### [`0061ccb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ccb4.md) → [`0061ccf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccf4.md) FUN_0061ccf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061cd1c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061ccdc",
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
      "0061cd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061cd1c",
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

- 旧版 [`0061ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ccb4.md#insn-0061ccdc) · [`0061cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ccb4.md#insn-0061cce8) · [`0061cd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ccb4.md#insn-0061cd00)
- 新版 `0061cd1c`（命令位置の公開資料なし） · `0061cd28`（命令位置の公開資料なし） · `0061cd40`（命令位置の公開資料なし）

~~~diff
- 0061ccdc ["INT_ADD", "register:40f0:8", ["const:61ccdc:8", "const:4:8"]]
- 0061ccdc ["CALL", null, ["ram:47acb4:8"]]
+ 0061cd1c ["INT_ADD", "register:40f0:8", ["const:61cd1c:8", "const:4:8"]]
+ 0061cd1c ["CALL", null, ["ram:47acf4:8"]]
- 0061ccdc bytes f677f997
+ 0061cd1c bytes f677f997
- 0061cce8 ["INT_ADD", "register:40f0:8", ["const:61cce8:8", "const:4:8"]]
- 0061cce8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061cd28 ["INT_ADD", "register:40f0:8", ["const:61cd28:8", "const:4:8"]]
+ 0061cd28 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061cce8 bytes 2b80f997
+ 0061cd28 bytes 2b80f997
- 0061cd00 ["INT_ADD", "register:40f0:8", ["const:61cd00:8", "const:4:8"]]
- 0061cd00 ["CALL", null, ["callee:008514f8:8"]]
+ 0061cd40 ["INT_ADD", "register:40f0:8", ["const:61cd40:8", "const:4:8"]]
+ 0061cd40 ["CALL", null, ["callee:008514f8:8"]]
- 0061cd00 bytes eed10894
+ 0061cd40 bytes eed10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63e4cf48be5edf44cc5927507b5f9568"></a>

### [`0061ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce10.md) → [`0061ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce50.md) FUN_0061ce50

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
      "definition_site": "0061ce64",
      "incomplete_value": false,
      "site": "0061ce68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ce24",
      "incomplete_value": false,
      "site": "0061ce28",
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
            "const:cd8:8"
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
      "0061ce68",
      "DATA",
      [
        "storage",
        "00c71cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ce68",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ce1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce10.md#insn-0061ce1c) · [`0061ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce10.md#insn-0061ce20) · [`0061ce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce10.md#insn-0061ce24)
- 新版 `0061ce5c`（命令位置の公開資料なし） · `0061ce60`（命令位置の公開資料なし） · `0061ce64`（命令位置の公開資料なし）

~~~diff
- 0061ce1c ["INT_ADD", "register:40f0:8", ["const:61ce1c:8", "const:4:8"]]
- 0061ce1c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061ce5c ["INT_ADD", "register:40f0:8", ["const:61ce5c:8", "const:4:8"]]
+ 0061ce5c ["CALL", null, ["callee:00c57e90:8"]]
- 0061ce1c bytes 1deb1894
+ 0061ce5c bytes 0dec1894
- 0061ce20 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061ce60 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061ce20 bytes a83200b0
+ 0061ce60 bytes a83200d0
- 0061ce24 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0061ce24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ce64 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0061ce64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ce64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ce64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ce24 bytes 08613391
+ 0061ce64 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2351a1bf621230d668c545d0fd69d559"></a>

### [`0061ce4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce4c.md) → [`0061ce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce8c.md) FUN_0061ce8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061ceb4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061ce74",
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
      "0061ceb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061ceb4",
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

- 旧版 [`0061ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce4c.md#insn-0061ce74) · [`0061ce80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce4c.md#insn-0061ce80) · [`0061ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061ce4c.md#insn-0061ce98)
- 新版 `0061ceb4`（命令位置の公開資料なし） · `0061cec0`（命令位置の公開資料なし） · `0061ced8`（命令位置の公開資料なし）

~~~diff
- 0061ce74 ["INT_ADD", "register:40f0:8", ["const:61ce74:8", "const:4:8"]]
- 0061ce74 ["CALL", null, ["ram:47acb4:8"]]
+ 0061ceb4 ["INT_ADD", "register:40f0:8", ["const:61ceb4:8", "const:4:8"]]
+ 0061ceb4 ["CALL", null, ["ram:47acf4:8"]]
- 0061ce74 bytes 9077f997
+ 0061ceb4 bytes 9077f997
- 0061ce80 ["INT_ADD", "register:40f0:8", ["const:61ce80:8", "const:4:8"]]
- 0061ce80 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061cec0 ["INT_ADD", "register:40f0:8", ["const:61cec0:8", "const:4:8"]]
+ 0061cec0 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061ce80 bytes c57ff997
+ 0061cec0 bytes c57ff997
- 0061ce98 ["INT_ADD", "register:40f0:8", ["const:61ce98:8", "const:4:8"]]
- 0061ce98 ["CALL", null, ["callee:008514f8:8"]]
+ 0061ced8 ["INT_ADD", "register:40f0:8", ["const:61ced8:8", "const:4:8"]]
+ 0061ced8 ["CALL", null, ["callee:008514f8:8"]]
- 0061ce98 bytes 88d10894
+ 0061ced8 bytes 88d10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f6d1079d69e51b2a7821dc61bacda7"></a>

### [`0061cfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cfe4.md) → [`0061d024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d024.md) FUN_0061d024

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d04c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d00c",
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
      "0061d04c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d04c",
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

- 旧版 [`0061d00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cfe4.md#insn-0061d00c) · [`0061d018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cfe4.md#insn-0061d018) · [`0061d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061c/0061cfe4.md#insn-0061d030)
- 新版 `0061d04c`（命令位置の公開資料なし） · `0061d058`（命令位置の公開資料なし） · `0061d070`（命令位置の公開資料なし）

~~~diff
- 0061d00c ["INT_ADD", "register:40f0:8", ["const:61d00c:8", "const:4:8"]]
- 0061d00c ["CALL", null, ["ram:47acb4:8"]]
+ 0061d04c ["INT_ADD", "register:40f0:8", ["const:61d04c:8", "const:4:8"]]
+ 0061d04c ["CALL", null, ["ram:47acf4:8"]]
- 0061d00c bytes 2a77f997
+ 0061d04c bytes 2a77f997
- 0061d018 ["INT_ADD", "register:40f0:8", ["const:61d018:8", "const:4:8"]]
- 0061d018 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061d058 ["INT_ADD", "register:40f0:8", ["const:61d058:8", "const:4:8"]]
+ 0061d058 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061d018 bytes 5f7ff997
+ 0061d058 bytes 5f7ff997
- 0061d030 ["INT_ADD", "register:40f0:8", ["const:61d030:8", "const:4:8"]]
- 0061d030 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d070 ["INT_ADD", "register:40f0:8", ["const:61d070:8", "const:4:8"]]
+ 0061d070 ["CALL", null, ["callee:008514f8:8"]]
- 0061d030 bytes 22d10894
+ 0061d070 bytes 22d10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118f06f608d210dc9789b670ed28c887"></a>

### [`0061d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d140.md) → [`0061d180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d180.md) FUN_0061d180

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
      "definition_site": "0061d194",
      "incomplete_value": false,
      "site": "0061d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d154",
      "incomplete_value": false,
      "site": "0061d158",
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
            "const:dd8:8"
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
      "0061d198",
      "DATA",
      [
        "storage",
        "00c71dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d198",
      "DATA",
      [
        "storage",
        "00c721d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d140.md#insn-0061d14c) · [`0061d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d140.md#insn-0061d150) · [`0061d154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d140.md#insn-0061d154)
- 新版 `0061d18c`（命令位置の公開資料なし） · `0061d190`（命令位置の公開資料なし） · `0061d194`（命令位置の公開資料なし）

~~~diff
- 0061d14c ["INT_ADD", "register:40f0:8", ["const:61d14c:8", "const:4:8"]]
- 0061d14c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061d18c ["INT_ADD", "register:40f0:8", ["const:61d18c:8", "const:4:8"]]
+ 0061d18c ["CALL", null, ["callee:00c57e90:8"]]
- 0061d14c bytes 51ea1894
+ 0061d18c bytes 41eb1894
- 0061d150 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061d190 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061d150 bytes a8320090
+ 0061d190 bytes a83200b0
- 0061d154 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 0061d154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d194 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0061d194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d154 bytes 08613791
+ 0061d194 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aeb892d600f56cbab297ffbd0e71c2b"></a>

### [`0061d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d17c.md) → [`0061d1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1bc.md) FUN_0061d1bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d1e4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d1a4",
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
      "0061d1e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d1e4",
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

- 旧版 [`0061d1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d17c.md#insn-0061d1a4) · [`0061d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d17c.md#insn-0061d1b0) · [`0061d1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d17c.md#insn-0061d1c8)
- 新版 `0061d1e4`（命令位置の公開資料なし） · `0061d1f0`（命令位置の公開資料なし） · `0061d208`（命令位置の公開資料なし）

~~~diff
- 0061d1a4 ["INT_ADD", "register:40f0:8", ["const:61d1a4:8", "const:4:8"]]
- 0061d1a4 ["CALL", null, ["ram:47acb4:8"]]
+ 0061d1e4 ["INT_ADD", "register:40f0:8", ["const:61d1e4:8", "const:4:8"]]
+ 0061d1e4 ["CALL", null, ["ram:47acf4:8"]]
- 0061d1a4 bytes c476f997
+ 0061d1e4 bytes c476f997
- 0061d1b0 ["INT_ADD", "register:40f0:8", ["const:61d1b0:8", "const:4:8"]]
- 0061d1b0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061d1f0 ["INT_ADD", "register:40f0:8", ["const:61d1f0:8", "const:4:8"]]
+ 0061d1f0 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061d1b0 bytes f97ef997
+ 0061d1f0 bytes f97ef997
- 0061d1c8 ["INT_ADD", "register:40f0:8", ["const:61d1c8:8", "const:4:8"]]
- 0061d1c8 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d208 ["INT_ADD", "register:40f0:8", ["const:61d208:8", "const:4:8"]]
+ 0061d208 ["CALL", null, ["callee:008514f8:8"]]
- 0061d1c8 bytes bcd00894
+ 0061d208 bytes bcd00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ee69a7b2ac774c071afb8dd6c3f9c09"></a>

### [`0061d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d2d8.md) → [`0061d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d318.md) FUN_0061d318

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
      "definition_site": "0061d32c",
      "incomplete_value": false,
      "site": "0061d330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d2ec",
      "incomplete_value": false,
      "site": "0061d2f0",
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
            "const:e58:8"
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
      "0061d330",
      "DATA",
      [
        "storage",
        "00c71e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d330",
      "DATA",
      [
        "storage",
        "00c72258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d2d8.md#insn-0061d2e4) · [`0061d2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d2d8.md#insn-0061d2e8) · [`0061d2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d2d8.md#insn-0061d2ec)
- 新版 `0061d324`（命令位置の公開資料なし） · `0061d328`（命令位置の公開資料なし） · `0061d32c`（命令位置の公開資料なし）

~~~diff
- 0061d2e4 ["INT_ADD", "register:40f0:8", ["const:61d2e4:8", "const:4:8"]]
- 0061d2e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061d324 ["INT_ADD", "register:40f0:8", ["const:61d324:8", "const:4:8"]]
+ 0061d324 ["CALL", null, ["callee:00c57e90:8"]]
- 0061d2e4 bytes ebe91894
+ 0061d324 bytes dbea1894
- 0061d2e8 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061d328 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061d2e8 bytes a8320090
+ 0061d328 bytes a83200b0
- 0061d2ec ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0061d2ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d2ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d2ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d32c ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0061d32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d2ec bytes 08613991
+ 0061d32c bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-967e4caadabfe6b24d5e06d6d38b01d2"></a>

### [`0061d314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d314.md) → [`0061d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d354.md) FUN_0061d354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "site": "0061d4ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d4ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0061d4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d4ec",
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

- 旧版 [`0061d4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d314.md#insn-0061d4ac) · [`0061d338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d314.md#insn-0061d338) · [`0061d374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d314.md#insn-0061d374)
- 新版 `0061d4ec`（命令位置の公開資料なし） · `0061d378`（命令位置の公開資料なし） · `0061d3b4`（命令位置の公開資料なし）

~~~diff
- 0061d4ac ["INT_ADD", "register:40f0:8", ["const:61d4ac:8", "const:4:8"]]
- 0061d4ac ["CALL", null, ["ram:47acb4:8"]]
+ 0061d4ec ["INT_ADD", "register:40f0:8", ["const:61d4ec:8", "const:4:8"]]
+ 0061d4ec ["CALL", null, ["ram:47acf4:8"]]
- 0061d4ac bytes 0276f997
+ 0061d4ec bytes 0276f997
- 0061d338 ["INT_ADD", "register:40f0:8", ["const:61d338:8", "const:4:8"]]
- 0061d338 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d378 ["INT_ADD", "register:40f0:8", ["const:61d378:8", "const:4:8"]]
+ 0061d378 ["CALL", null, ["callee:008514f8:8"]]
- 0061d338 bytes 60d00894
+ 0061d378 bytes 60d00894
- 0061d374 ["INT_ADD", "register:40f0:8", ["const:61d374:8", "const:4:8"]]
- 0061d374 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d3b4 ["INT_ADD", "register:40f0:8", ["const:61d3b4:8", "const:4:8"]]
+ 0061d3b4 ["CALL", null, ["callee:008514f8:8"]]
- 0061d374 bytes 51d00894
+ 0061d3b4 bytes 51d00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b8ac699f6810f5cc611390b6c4fd55"></a>

### [`0061d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d570.md) → [`0061d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5b0.md) FUN_0061d5b0

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
      "definition_site": "0061d5c4",
      "incomplete_value": false,
      "site": "0061d5c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d584",
      "incomplete_value": false,
      "site": "0061d588",
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
            "const:ed8:8"
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
      "0061d5c8",
      "DATA",
      [
        "storage",
        "00c71ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d5c8",
      "DATA",
      [
        "storage",
        "00c722d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d570.md#insn-0061d57c) · [`0061d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d570.md#insn-0061d580) · [`0061d584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d570.md#insn-0061d584)
- 新版 `0061d5bc`（命令位置の公開資料なし） · `0061d5c0`（命令位置の公開資料なし） · `0061d5c4`（命令位置の公開資料なし）

~~~diff
- 0061d57c ["INT_ADD", "register:40f0:8", ["const:61d57c:8", "const:4:8"]]
- 0061d57c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061d5bc ["INT_ADD", "register:40f0:8", ["const:61d5bc:8", "const:4:8"]]
+ 0061d5bc ["CALL", null, ["callee:00c57e90:8"]]
- 0061d57c bytes 45e91894
+ 0061d5bc bytes 35ea1894
- 0061d580 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061d5c0 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061d580 bytes a8320090
+ 0061d5c0 bytes a83200b0
- 0061d584 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0061d584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d5c4 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0061d5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d584 bytes 08613b91
+ 0061d5c4 bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802fcd478a4ee2bb4947ba6942adc136"></a>

### [`0061d5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d5ac.md) → [`0061d5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5ec.md) FUN_0061d5ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d614",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d5d4",
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
      "0061d614",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d614",
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

- 旧版 [`0061d5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d5ac.md#insn-0061d5d4) · [`0061d5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d5ac.md#insn-0061d5e0) · [`0061d5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d5ac.md#insn-0061d5f8)
- 新版 `0061d614`（命令位置の公開資料なし） · `0061d620`（命令位置の公開資料なし） · `0061d638`（命令位置の公開資料なし）

~~~diff
- 0061d5d4 ["INT_ADD", "register:40f0:8", ["const:61d5d4:8", "const:4:8"]]
- 0061d5d4 ["CALL", null, ["ram:47acb4:8"]]
+ 0061d614 ["INT_ADD", "register:40f0:8", ["const:61d614:8", "const:4:8"]]
+ 0061d614 ["CALL", null, ["ram:47acf4:8"]]
- 0061d5d4 bytes b875f997
+ 0061d614 bytes b875f997
- 0061d5e0 ["INT_ADD", "register:40f0:8", ["const:61d5e0:8", "const:4:8"]]
- 0061d5e0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061d620 ["INT_ADD", "register:40f0:8", ["const:61d620:8", "const:4:8"]]
+ 0061d620 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061d5e0 bytes ed7df997
+ 0061d620 bytes ed7df997
- 0061d5f8 ["INT_ADD", "register:40f0:8", ["const:61d5f8:8", "const:4:8"]]
- 0061d5f8 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d638 ["INT_ADD", "register:40f0:8", ["const:61d638:8", "const:4:8"]]
+ 0061d638 ["CALL", null, ["callee:008514f8:8"]]
- 0061d5f8 bytes b0cf0894
+ 0061d638 bytes b0cf0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8dcfe4c4923c740553fc0eba1bce1e9"></a>

### [`0061d744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d744.md) → [`0061d784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d784.md) FUN_0061d784

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d7ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d76c",
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
      "0061d7ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d7ac",
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

- 旧版 [`0061d76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d744.md#insn-0061d76c) · [`0061d778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d744.md#insn-0061d778) · [`0061d790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d744.md#insn-0061d790)
- 新版 `0061d7ac`（命令位置の公開資料なし） · `0061d7b8`（命令位置の公開資料なし） · `0061d7d0`（命令位置の公開資料なし）

~~~diff
- 0061d76c ["INT_ADD", "register:40f0:8", ["const:61d76c:8", "const:4:8"]]
- 0061d76c ["CALL", null, ["ram:47acb4:8"]]
+ 0061d7ac ["INT_ADD", "register:40f0:8", ["const:61d7ac:8", "const:4:8"]]
+ 0061d7ac ["CALL", null, ["ram:47acf4:8"]]
- 0061d76c bytes 5275f997
+ 0061d7ac bytes 5275f997
- 0061d778 ["INT_ADD", "register:40f0:8", ["const:61d778:8", "const:4:8"]]
- 0061d778 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061d7b8 ["INT_ADD", "register:40f0:8", ["const:61d7b8:8", "const:4:8"]]
+ 0061d7b8 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061d778 bytes 877df997
+ 0061d7b8 bytes 877df997
- 0061d790 ["INT_ADD", "register:40f0:8", ["const:61d790:8", "const:4:8"]]
- 0061d790 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d7d0 ["INT_ADD", "register:40f0:8", ["const:61d7d0:8", "const:4:8"]]
+ 0061d7d0 ["CALL", null, ["callee:008514f8:8"]]
- 0061d790 bytes 4acf0894
+ 0061d7d0 bytes 4acf0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4161e3db2f9139ebcb0b4c0a365f4e62"></a>

### [`0061d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8dc.md) → [`0061d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d91c.md) FUN_0061d91c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d944",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d904",
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
      "0061d944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061d944",
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

- 旧版 [`0061d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8dc.md#insn-0061d904) · [`0061d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8dc.md#insn-0061d910) · [`0061d928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061d8dc.md#insn-0061d928)
- 新版 `0061d944`（命令位置の公開資料なし） · `0061d950`（命令位置の公開資料なし） · `0061d968`（命令位置の公開資料なし）

~~~diff
- 0061d904 ["INT_ADD", "register:40f0:8", ["const:61d904:8", "const:4:8"]]
- 0061d904 ["CALL", null, ["ram:47acb4:8"]]
+ 0061d944 ["INT_ADD", "register:40f0:8", ["const:61d944:8", "const:4:8"]]
+ 0061d944 ["CALL", null, ["ram:47acf4:8"]]
- 0061d904 bytes ec74f997
+ 0061d944 bytes ec74f997
- 0061d910 ["INT_ADD", "register:40f0:8", ["const:61d910:8", "const:4:8"]]
- 0061d910 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061d950 ["INT_ADD", "register:40f0:8", ["const:61d950:8", "const:4:8"]]
+ 0061d950 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061d910 bytes 217df997
+ 0061d950 bytes 217df997
- 0061d928 ["INT_ADD", "register:40f0:8", ["const:61d928:8", "const:4:8"]]
- 0061d928 ["CALL", null, ["callee:008514f8:8"]]
+ 0061d968 ["INT_ADD", "register:40f0:8", ["const:61d968:8", "const:4:8"]]
+ 0061d968 ["CALL", null, ["callee:008514f8:8"]]
- 0061d928 bytes e4ce0894
+ 0061d968 bytes e4ce0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-785cbcb46aed6cea9f539c8c7b8719dd"></a>

### [`0061da38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da38.md) → [`0061da78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061da78.md) FUN_0061da78

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
      "definition_site": "0061da8c",
      "incomplete_value": false,
      "site": "0061da90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061da4c",
      "incomplete_value": false,
      "site": "0061da50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "0061da90",
      "DATA",
      [
        "storage",
        "00c72058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061da90",
      "DATA",
      [
        "storage",
        "00c72458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061da44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da38.md#insn-0061da44) · [`0061da4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da38.md#insn-0061da4c)
- 新版 `0061da84`（命令位置の公開資料なし） · `0061da8c`（命令位置の公開資料なし）

~~~diff
- 0061da44 ["INT_ADD", "register:40f0:8", ["const:61da44:8", "const:4:8"]]
- 0061da44 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061da84 ["INT_ADD", "register:40f0:8", ["const:61da84:8", "const:4:8"]]
+ 0061da84 ["CALL", null, ["callee:00c57e90:8"]]
- 0061da44 bytes 13e81894
+ 0061da84 bytes 03e91894
- 0061da4c ["COPY", "tmp:0:8", ["const:58:8"]]
- 0061da4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061da4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061da4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061da8c ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0061da8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061da8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061da8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061da4c bytes 08610191
+ 0061da8c bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c598dbd5ef0c423c3c1ac00ec13e61bc"></a>

### [`0061da74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da74.md) → [`0061dab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dab4.md) FUN_0061dab4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061dadc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061da9c",
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
      "0061dadc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061dadc",
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

- 旧版 [`0061da9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da74.md#insn-0061da9c) · [`0061daa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da74.md#insn-0061daa8) · [`0061dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061da74.md#insn-0061dac0)
- 新版 `0061dadc`（命令位置の公開資料なし） · `0061dae8`（命令位置の公開資料なし） · `0061db00`（命令位置の公開資料なし）

~~~diff
- 0061da9c ["INT_ADD", "register:40f0:8", ["const:61da9c:8", "const:4:8"]]
- 0061da9c ["CALL", null, ["ram:47acb4:8"]]
+ 0061dadc ["INT_ADD", "register:40f0:8", ["const:61dadc:8", "const:4:8"]]
+ 0061dadc ["CALL", null, ["ram:47acf4:8"]]
- 0061da9c bytes 8674f997
+ 0061dadc bytes 8674f997
- 0061daa8 ["INT_ADD", "register:40f0:8", ["const:61daa8:8", "const:4:8"]]
- 0061daa8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061dae8 ["INT_ADD", "register:40f0:8", ["const:61dae8:8", "const:4:8"]]
+ 0061dae8 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061daa8 bytes bb7cf997
+ 0061dae8 bytes bb7cf997
- 0061dac0 ["INT_ADD", "register:40f0:8", ["const:61dac0:8", "const:4:8"]]
- 0061dac0 ["CALL", null, ["callee:008514f8:8"]]
+ 0061db00 ["INT_ADD", "register:40f0:8", ["const:61db00:8", "const:4:8"]]
+ 0061db00 ["CALL", null, ["callee:008514f8:8"]]
- 0061dac0 bytes 7ece0894
+ 0061db00 bytes 7ece0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfbe75697dba376a2279ec74d8ec29ac"></a>

### [`0061dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc0c.md) → [`0061dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc4c.md) FUN_0061dc4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

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
      "site": "0061dc74",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061dc34",
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
      "0061dc74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061dc74",
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

- 旧版 [`0061dc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc0c.md#insn-0061dc34) · [`0061dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc0c.md#insn-0061dc40) · [`0061dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dc0c.md#insn-0061dc60)
- 新版 `0061dc74`（命令位置の公開資料なし） · `0061dc80`（命令位置の公開資料なし） · `0061dca0`（命令位置の公開資料なし）

~~~diff
- 0061dc34 ["INT_ADD", "register:40f0:8", ["const:61dc34:8", "const:4:8"]]
- 0061dc34 ["CALL", null, ["ram:47acb4:8"]]
+ 0061dc74 ["INT_ADD", "register:40f0:8", ["const:61dc74:8", "const:4:8"]]
+ 0061dc74 ["CALL", null, ["ram:47acf4:8"]]
- 0061dc34 bytes 2074f997
+ 0061dc74 bytes 2074f997
- 0061dc40 ["INT_ADD", "register:40f0:8", ["const:61dc40:8", "const:4:8"]]
- 0061dc40 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061dc80 ["INT_ADD", "register:40f0:8", ["const:61dc80:8", "const:4:8"]]
+ 0061dc80 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061dc40 bytes 557cf997
+ 0061dc80 bytes 557cf997
- 0061dc60 ["INT_ADD", "register:40f0:8", ["const:61dc60:8", "const:4:8"]]
- 0061dc60 ["CALL", null, ["callee:008514f8:8"]]
+ 0061dca0 ["INT_ADD", "register:40f0:8", ["const:61dca0:8", "const:4:8"]]
+ 0061dca0 ["CALL", null, ["callee:008514f8:8"]]
- 0061dc60 bytes 16ce0894
+ 0061dca0 bytes 16ce0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac587405cad41778e86a4118410c0b9"></a>

### [`0061dd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd70.md) → [`0061ddb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddb0.md) FUN_0061ddb0

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
      "definition_site": "0061ddc4",
      "incomplete_value": true,
      "site": "0061ddc8",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061dd84",
      "incomplete_value": true,
      "site": "0061dd88",
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
            "const:158:8"
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
      "0061ddc8",
      "DATA",
      [
        "storage",
        "00c72158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ddc8",
      "DATA",
      [
        "storage",
        "00c72558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061dd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd70.md#insn-0061dd7c) · [`0061dd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061dd70.md#insn-0061dd84)
- 新版 `0061ddbc`（命令位置の公開資料なし） · `0061ddc4`（命令位置の公開資料なし）

~~~diff
- 0061dd7c ["INT_ADD", "register:40f0:8", ["const:61dd7c:8", "const:4:8"]]
- 0061dd7c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061ddbc ["INT_ADD", "register:40f0:8", ["const:61ddbc:8", "const:4:8"]]
+ 0061ddbc ["CALL", null, ["callee:00c57e90:8"]]
- 0061dd7c bytes 45e71894
+ 0061ddbc bytes 35e81894
- 0061dd84 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0061dd84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061dd84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061dd84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ddc4 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 0061ddc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ddc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ddc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061dd84 bytes 08610591
+ 0061ddc4 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1dd0ff1d03995c4400024865203ac61"></a>

### [`0061ddac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061ddac.md) → [`0061ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddec.md) FUN_0061ddec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061de14",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061ddd4",
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
      "0061de14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061de14",
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

- 旧版 [`0061ddd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061ddac.md#insn-0061ddd4) · [`0061dde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061ddac.md#insn-0061dde0) · [`0061ddf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061ddac.md#insn-0061ddf8)
- 新版 `0061de14`（命令位置の公開資料なし） · `0061de20`（命令位置の公開資料なし） · `0061de38`（命令位置の公開資料なし）

~~~diff
- 0061ddd4 ["INT_ADD", "register:40f0:8", ["const:61ddd4:8", "const:4:8"]]
- 0061ddd4 ["CALL", null, ["ram:47acb4:8"]]
+ 0061de14 ["INT_ADD", "register:40f0:8", ["const:61de14:8", "const:4:8"]]
+ 0061de14 ["CALL", null, ["ram:47acf4:8"]]
- 0061ddd4 bytes b873f997
+ 0061de14 bytes b873f997
- 0061dde0 ["INT_ADD", "register:40f0:8", ["const:61dde0:8", "const:4:8"]]
- 0061dde0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061de20 ["INT_ADD", "register:40f0:8", ["const:61de20:8", "const:4:8"]]
+ 0061de20 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061dde0 bytes ed7bf997
+ 0061de20 bytes ed7bf997
- 0061ddf8 ["INT_ADD", "register:40f0:8", ["const:61ddf8:8", "const:4:8"]]
- 0061ddf8 ["CALL", null, ["callee:008514f8:8"]]
+ 0061de38 ["INT_ADD", "register:40f0:8", ["const:61de38:8", "const:4:8"]]
+ 0061de38 ["CALL", null, ["callee:008514f8:8"]]
- 0061ddf8 bytes b0cd0894
+ 0061de38 bytes b0cd0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bebc4e846fcffee98a1218e96e8d253"></a>

### [`0061df08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df08.md) → [`0061df48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df48.md) FUN_0061df48

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
      "definition_site": "0061df5c",
      "incomplete_value": false,
      "site": "0061df60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061df1c",
      "incomplete_value": false,
      "site": "0061df20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "0061df60",
      "DATA",
      [
        "storage",
        "00c721d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061df60",
      "DATA",
      [
        "storage",
        "00c725d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061df14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df08.md#insn-0061df14) · [`0061df1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df08.md#insn-0061df1c)
- 新版 `0061df54`（命令位置の公開資料なし） · `0061df5c`（命令位置の公開資料なし）

~~~diff
- 0061df14 ["INT_ADD", "register:40f0:8", ["const:61df14:8", "const:4:8"]]
- 0061df14 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061df54 ["INT_ADD", "register:40f0:8", ["const:61df54:8", "const:4:8"]]
+ 0061df54 ["CALL", null, ["callee:00c57e90:8"]]
- 0061df14 bytes dfe61894
+ 0061df54 bytes cfe71894
- 0061df1c ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0061df1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061df1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061df1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061df5c ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0061df5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061df5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061df5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061df1c bytes 08610791
+ 0061df5c bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8bbd6173f77c1fafb15030975858381"></a>

### [`0061df44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df44.md) → [`0061df84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df84.md) FUN_0061df84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061dfac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061df6c",
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
      "0061dfac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061dfac",
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

- 旧版 [`0061df6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df44.md#insn-0061df6c) · [`0061df78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df44.md#insn-0061df78) · [`0061df90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061d/0061df44.md#insn-0061df90)
- 新版 `0061dfac`（命令位置の公開資料なし） · `0061dfb8`（命令位置の公開資料なし） · `0061dfd0`（命令位置の公開資料なし）

~~~diff
- 0061df6c ["INT_ADD", "register:40f0:8", ["const:61df6c:8", "const:4:8"]]
- 0061df6c ["CALL", null, ["ram:47acb4:8"]]
+ 0061dfac ["INT_ADD", "register:40f0:8", ["const:61dfac:8", "const:4:8"]]
+ 0061dfac ["CALL", null, ["ram:47acf4:8"]]
- 0061df6c bytes 5273f997
+ 0061dfac bytes 5273f997
- 0061df78 ["INT_ADD", "register:40f0:8", ["const:61df78:8", "const:4:8"]]
- 0061df78 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061dfb8 ["INT_ADD", "register:40f0:8", ["const:61dfb8:8", "const:4:8"]]
+ 0061dfb8 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061df78 bytes 877bf997
+ 0061dfb8 bytes 877bf997
- 0061df90 ["INT_ADD", "register:40f0:8", ["const:61df90:8", "const:4:8"]]
- 0061df90 ["CALL", null, ["callee:008514f8:8"]]
+ 0061dfd0 ["INT_ADD", "register:40f0:8", ["const:61dfd0:8", "const:4:8"]]
+ 0061dfd0 ["CALL", null, ["callee:008514f8:8"]]
- 0061df90 bytes 4acd0894
+ 0061dfd0 bytes 4acd0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1560c202c434378d0c77b6536c723ed"></a>

### [`0061e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0a0.md) → [`0061e0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e0e0.md) FUN_0061e0e0

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
      "definition_site": "0061e0f4",
      "incomplete_value": false,
      "site": "0061e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e0b4",
      "incomplete_value": false,
      "site": "0061e0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "0061e0f8",
      "DATA",
      [
        "storage",
        "00c72258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e0f8",
      "DATA",
      [
        "storage",
        "00c72658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0a0.md#insn-0061e0ac) · [`0061e0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0a0.md#insn-0061e0b4)
- 新版 `0061e0ec`（命令位置の公開資料なし） · `0061e0f4`（命令位置の公開資料なし）

~~~diff
- 0061e0ac ["INT_ADD", "register:40f0:8", ["const:61e0ac:8", "const:4:8"]]
- 0061e0ac ["CALL", null, ["callee:00c57e90:8"]]
+ 0061e0ec ["INT_ADD", "register:40f0:8", ["const:61e0ec:8", "const:4:8"]]
+ 0061e0ec ["CALL", null, ["callee:00c57e90:8"]]
- 0061e0ac bytes 79e61894
+ 0061e0ec bytes 69e71894
- 0061e0b4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0061e0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e0f4 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0061e0f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e0f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e0f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e0b4 bytes 08610991
+ 0061e0f4 bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-950be0c5c5acab8849d1d001c8929192"></a>

### [`0061e0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0dc.md) → [`0061e11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e11c.md) FUN_0061e11c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061e144",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e104",
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
      "0061e144",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061e144",
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

- 旧版 [`0061e104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0dc.md#insn-0061e104) · [`0061e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0dc.md#insn-0061e110) · [`0061e128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e0dc.md#insn-0061e128)
- 新版 `0061e144`（命令位置の公開資料なし） · `0061e150`（命令位置の公開資料なし） · `0061e168`（命令位置の公開資料なし）

~~~diff
- 0061e104 ["INT_ADD", "register:40f0:8", ["const:61e104:8", "const:4:8"]]
- 0061e104 ["CALL", null, ["ram:47acb4:8"]]
+ 0061e144 ["INT_ADD", "register:40f0:8", ["const:61e144:8", "const:4:8"]]
+ 0061e144 ["CALL", null, ["ram:47acf4:8"]]
- 0061e104 bytes ec72f997
+ 0061e144 bytes ec72f997
- 0061e110 ["INT_ADD", "register:40f0:8", ["const:61e110:8", "const:4:8"]]
- 0061e110 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061e150 ["INT_ADD", "register:40f0:8", ["const:61e150:8", "const:4:8"]]
+ 0061e150 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061e110 bytes 217bf997
+ 0061e150 bytes 217bf997
- 0061e128 ["INT_ADD", "register:40f0:8", ["const:61e128:8", "const:4:8"]]
- 0061e128 ["CALL", null, ["callee:008514f8:8"]]
+ 0061e168 ["INT_ADD", "register:40f0:8", ["const:61e168:8", "const:4:8"]]
+ 0061e168 ["CALL", null, ["callee:008514f8:8"]]
- 0061e128 bytes e4cc0894
+ 0061e168 bytes e4cc0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a29b0258a285ed4a8982455f9537f6f1"></a>

### [`0061e238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e238.md) → [`0061e278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e278.md) FUN_0061e278

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
      "definition_site": "0061e28c",
      "incomplete_value": false,
      "site": "0061e290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e24c",
      "incomplete_value": false,
      "site": "0061e250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "0061e290",
      "DATA",
      [
        "storage",
        "00c722d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e290",
      "DATA",
      [
        "storage",
        "00c726d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e238.md#insn-0061e244) · [`0061e24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e238.md#insn-0061e24c)
- 新版 `0061e284`（命令位置の公開資料なし） · `0061e28c`（命令位置の公開資料なし）

~~~diff
- 0061e244 ["INT_ADD", "register:40f0:8", ["const:61e244:8", "const:4:8"]]
- 0061e244 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061e284 ["INT_ADD", "register:40f0:8", ["const:61e284:8", "const:4:8"]]
+ 0061e284 ["CALL", null, ["callee:00c57e90:8"]]
- 0061e244 bytes 13e61894
+ 0061e284 bytes 03e71894
- 0061e24c ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0061e24c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e24c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e24c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e28c ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 0061e28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e24c bytes 08610b91
+ 0061e28c bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f9d857f6e200ef2d6b643b2bad89c73"></a>

### [`0061e274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e274.md) → [`0061e2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e2b4.md) FUN_0061e2b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

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
      "site": "0061e2dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e29c",
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
      "0061e2dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061e2dc",
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

- 旧版 [`0061e29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e274.md#insn-0061e29c) · [`0061e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e274.md#insn-0061e2a8) · [`0061e2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e274.md#insn-0061e2c8)
- 新版 `0061e2dc`（命令位置の公開資料なし） · `0061e2e8`（命令位置の公開資料なし） · `0061e308`（命令位置の公開資料なし）

~~~diff
- 0061e29c ["INT_ADD", "register:40f0:8", ["const:61e29c:8", "const:4:8"]]
- 0061e29c ["CALL", null, ["ram:47acb4:8"]]
+ 0061e2dc ["INT_ADD", "register:40f0:8", ["const:61e2dc:8", "const:4:8"]]
+ 0061e2dc ["CALL", null, ["ram:47acf4:8"]]
- 0061e29c bytes 8672f997
+ 0061e2dc bytes 8672f997
- 0061e2a8 ["INT_ADD", "register:40f0:8", ["const:61e2a8:8", "const:4:8"]]
- 0061e2a8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061e2e8 ["INT_ADD", "register:40f0:8", ["const:61e2e8:8", "const:4:8"]]
+ 0061e2e8 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061e2a8 bytes bb7af997
+ 0061e2e8 bytes bb7af997
- 0061e2c8 ["INT_ADD", "register:40f0:8", ["const:61e2c8:8", "const:4:8"]]
- 0061e2c8 ["CALL", null, ["callee:008514f8:8"]]
+ 0061e308 ["INT_ADD", "register:40f0:8", ["const:61e308:8", "const:4:8"]]
+ 0061e308 ["CALL", null, ["callee:008514f8:8"]]
- 0061e2c8 bytes 7ccc0894
+ 0061e308 bytes 7ccc0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147cd36ee53d5d7fc84b3480069f73b5"></a>

### [`0061e3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3ec.md) → [`0061e42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e42c.md) FUN_0061e42c

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
      "definition_site": "0061e440",
      "incomplete_value": true,
      "site": "0061e444",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e400",
      "incomplete_value": true,
      "site": "0061e404",
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
            "const:358:8"
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
      "0061e444",
      "DATA",
      [
        "storage",
        "00c72358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e444",
      "DATA",
      [
        "storage",
        "00c72758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3ec.md#insn-0061e3f8) · [`0061e400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e3ec.md#insn-0061e400)
- 新版 `0061e438`（命令位置の公開資料なし） · `0061e440`（命令位置の公開資料なし）

~~~diff
- 0061e3f8 ["INT_ADD", "register:40f0:8", ["const:61e3f8:8", "const:4:8"]]
- 0061e3f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061e438 ["INT_ADD", "register:40f0:8", ["const:61e438:8", "const:4:8"]]
+ 0061e438 ["CALL", null, ["callee:00c57e90:8"]]
- 0061e3f8 bytes a6e51894
+ 0061e438 bytes 96e61894
- 0061e400 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0061e400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e440 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 0061e440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e400 bytes 08610d91
+ 0061e440 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b3fa7dbda04974c5115c2279c9324f7"></a>

### [`0061e508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e508.md) → [`0061e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e548.md) FUN_0061e548

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
      "definition_site": "0061e56c",
      "incomplete_value": false,
      "site": "0061e56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e52c",
      "incomplete_value": false,
      "site": "0061e52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "0061e56c",
      "DATA",
      [
        "storage",
        "00c723d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e56c",
      "DATA",
      [
        "storage",
        "00c727d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e508.md#insn-0061e51c) · [`0061e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e508.md#insn-0061e528)
- 新版 `0061e55c`（命令位置の公開資料なし） · `0061e568`（命令位置の公開資料なし）

~~~diff
- 0061e51c ["INT_ADD", "register:40f0:8", ["const:61e51c:8", "const:4:8"]]
- 0061e51c ["CALL", null, ["callee:00c57e90:8"]]
+ 0061e55c ["INT_ADD", "register:40f0:8", ["const:61e55c:8", "const:4:8"]]
+ 0061e55c ["CALL", null, ["callee:00c57e90:8"]]
- 0061e51c bytes 5de51894
+ 0061e55c bytes 4de61894
- 0061e528 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0061e528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e568 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0061e568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e528 bytes 08610f91
+ 0061e568 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1c22dbf7419ef8007604734a76e062"></a>

### [`0061e558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md) → [`0061e598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md) FUN_0061e598

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00747390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747390.md) [`00747398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/00747398.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007473d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473d0.md) [`007473d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473d8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

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
      "site": "0061e5b4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e574",
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
      "site": "0061e5d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e594",
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
      "0061e5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0061e5d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0061e5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061e5d4",
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

- 旧版 [`0061e574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md#insn-0061e574) · [`0061e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md#insn-0061e594) · [`0061e5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e558.md#insn-0061e5a0)
- 新版 `0061e5b4`（命令位置の公開資料なし） · `0061e5d4`（命令位置の公開資料なし） · `0061e5e0`（命令位置の公開資料なし）

~~~diff
- 0061e574 ["INT_ADD", "register:40f0:8", ["const:61e574:8", "const:4:8"]]
- 0061e574 ["CALL", null, ["ram:47acb4:8"]]
+ 0061e5b4 ["INT_ADD", "register:40f0:8", ["const:61e5b4:8", "const:4:8"]]
+ 0061e5b4 ["CALL", null, ["ram:47acf4:8"]]
- 0061e574 bytes d071f997
+ 0061e5b4 bytes d071f997
- 0061e594 ["INT_ADD", "register:40f0:8", ["const:61e594:8", "const:4:8"]]
- 0061e594 ["CALL", null, ["ram:47acb4:8"]]
+ 0061e5d4 ["INT_ADD", "register:40f0:8", ["const:61e5d4:8", "const:4:8"]]
+ 0061e5d4 ["CALL", null, ["ram:47acf4:8"]]
- 0061e594 bytes c871f997
+ 0061e5d4 bytes c871f997
- 0061e5a0 ["INT_ADD", "register:40f0:8", ["const:61e5a0:8", "const:4:8"]]
- 0061e5a0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061e5e0 ["INT_ADD", "register:40f0:8", ["const:61e5e0:8", "const:4:8"]]
+ 0061e5e0 ["CALL", null, ["callee:0047cdd4:8"]]
- 0061e5a0 bytes fd79f997
+ 0061e5e0 bytes fd79f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7456227f65f8d551d96ef743c1f7d5c6"></a>

### [`0061e62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e62c.md) → [`0061e66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e66c.md) FUN_0061e66c

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
      "definition_site": "0061e680",
      "incomplete_value": false,
      "site": "0061e684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e640",
      "incomplete_value": false,
      "site": "0061e644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0061e684",
      "DATA",
      [
        "storage",
        "00c72458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e684",
      "DATA",
      [
        "storage",
        "00c72858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e62c.md#insn-0061e638) · [`0061e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e62c.md#insn-0061e640)
- 新版 `0061e678`（命令位置の公開資料なし） · `0061e680`（命令位置の公開資料なし）

~~~diff
- 0061e638 ["INT_ADD", "register:40f0:8", ["const:61e638:8", "const:4:8"]]
- 0061e638 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061e678 ["INT_ADD", "register:40f0:8", ["const:61e678:8", "const:4:8"]]
+ 0061e678 ["CALL", null, ["callee:00c57e90:8"]]
- 0061e638 bytes 16e51894
+ 0061e678 bytes 06e61894
- 0061e640 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0061e640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e680 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0061e680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e640 bytes 08611191
+ 0061e680 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85959021ceddf82575bb7cc01e6ec947"></a>

### [`0061e668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md) → [`0061e6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md) FUN_0061e6a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.68% / 新版 87.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_destination` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e78c",
      "incomplete_value": false,
      "site": "0061e794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e74c",
      "incomplete_value": false,
      "site": "0061e754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "definition_site": "0061e9a0",
      "incomplete_value": false,
      "site": "0061e9a0",
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
      "definition_site": "0061e960",
      "incomplete_value": false,
      "site": "0061e960",
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
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0061e9a4",
      "incomplete_value": false,
      "site": "0061e9a4",
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
      "definition_site": "0061e964",
      "incomplete_value": false,
      "site": "0061e964",
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
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0061e6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0061e6e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0061e728",
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
      "0061e6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0061e6e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061e728",
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

- 旧版 [`0061e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md#insn-0061e68c) · [`0061e6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md#insn-0061e6a0) · [`0061e6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061e668.md#insn-0061e6ac)
- 新版 `0061e6cc`（命令位置の公開資料なし） · `0061e6e0`（命令位置の公開資料なし） · `0061e6ec`（命令位置の公開資料なし）

~~~diff
- 0061e68c ["INT_ADD", "register:40f0:8", ["const:61e68c:8", "const:4:8"]]
- 0061e68c ["CALL", null, ["ram:48ccb8:8"]]
+ 0061e6cc ["INT_ADD", "register:40f0:8", ["const:61e6cc:8", "const:4:8"]]
+ 0061e6cc ["CALL", null, ["ram:48ccf8:8"]]
- 0061e68c bytes 8bb9f997
+ 0061e6cc bytes 8bb9f997
- 0061e6a0 ["INT_ADD", "register:40f0:8", ["const:61e6a0:8", "const:4:8"]]
- 0061e6a0 ["CALL", null, ["ram:47acb4:8"]]
+ 0061e6e0 ["INT_ADD", "register:40f0:8", ["const:61e6e0:8", "const:4:8"]]
+ 0061e6e0 ["CALL", null, ["ram:47acf4:8"]]
- 0061e6a0 bytes 8571f997
+ 0061e6e0 bytes 8571f997
- 0061e6ac ["INT_ADD", "register:40f0:8", ["const:61e6ac:8", "const:4:8"]]
- 0061e6ac ["CALL", null, ["callee:0047cdd4:8"]]
+ 0061e6ec ["INT_ADD", "register:40f0:8", ["const:61e6ec:8", "const:4:8"]]
+ 0061e6ec ["CALL", null, ["callee:0047cdd4:8"]]
- 0061e6ac bytes ba79f997
+ 0061e6ec bytes ba79f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39613fa3090e70eb08009b766ee9d524"></a>

### [`0061eaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eaa8.md) → [`0061eae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eae8.md) FUN_0061eae8

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
      "definition_site": "0061eafc",
      "incomplete_value": false,
      "site": "0061eb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061eabc",
      "incomplete_value": false,
      "site": "0061eac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0061eb00",
      "DATA",
      [
        "storage",
        "00c724c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061eb00",
      "DATA",
      [
        "storage",
        "00c728c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061eab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eaa8.md#insn-0061eab4) · [`0061eabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eaa8.md#insn-0061eabc)
- 新版 `0061eaf4`（命令位置の公開資料なし） · `0061eafc`（命令位置の公開資料なし）

~~~diff
- 0061eab4 ["INT_ADD", "register:40f0:8", ["const:61eab4:8", "const:4:8"]]
- 0061eab4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061eaf4 ["INT_ADD", "register:40f0:8", ["const:61eaf4:8", "const:4:8"]]
+ 0061eaf4 ["CALL", null, ["callee:00c57e90:8"]]
- 0061eab4 bytes f7e31894
+ 0061eaf4 bytes e7e41894
- 0061eabc ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0061eabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061eabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061eabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061eafc ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 0061eafc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eafc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eafc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061eabc bytes 08211391
+ 0061eafc bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af48d8e7f37f8b04f13f14df3329068e"></a>

### [`0061eacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eacc.md) → [`0061eb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eb0c.md) FUN_0061eb0c

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
      "definition_site": "0061eb10",
      "incomplete_value": false,
      "site": "0061eb14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ead0",
      "incomplete_value": false,
      "site": "0061ead4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "0061eb14",
      "DATA",
      [
        "storage",
        "00c724c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061eb14",
      "DATA",
      [
        "storage",
        "00c728c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ead0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eacc.md#insn-0061ead0)
- 新版 `0061eb10`（命令位置の公開資料なし）

~~~diff
- 0061ead0 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0061ead0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ead0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ead0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061eb10 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 0061eb10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ead0 bytes 08211391
+ 0061eb10 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6798cb45ee0d1eafc0fffae31d3268f1"></a>

### [`0061eb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb68.md) → [`0061eba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eba8.md) FUN_0061eba8

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
      "definition_site": "0061ebbc",
      "incomplete_value": false,
      "site": "0061ebc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061eb7c",
      "incomplete_value": false,
      "site": "0061eb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0061ebc0",
      "DATA",
      [
        "storage",
        "00c72558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ebc0",
      "DATA",
      [
        "storage",
        "00c72958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061eb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb68.md#insn-0061eb74) · [`0061eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061eb68.md#insn-0061eb7c)
- 新版 `0061ebb4`（命令位置の公開資料なし） · `0061ebbc`（命令位置の公開資料なし）

~~~diff
- 0061eb74 ["INT_ADD", "register:40f0:8", ["const:61eb74:8", "const:4:8"]]
- 0061eb74 ["CALL", null, ["callee:00c57e90:8"]]
+ 0061ebb4 ["INT_ADD", "register:40f0:8", ["const:61ebb4:8", "const:4:8"]]
+ 0061ebb4 ["CALL", null, ["callee:00c57e90:8"]]
- 0061eb74 bytes c7e31894
+ 0061ebb4 bytes b7e41894
- 0061eb7c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0061eb7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061eb7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061eb7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ebbc ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0061ebbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ebbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ebbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061eb7c bytes 08611591
+ 0061ebbc bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a1a4e3c3657dae7f0cf1a7cd0d6e2c"></a>

### [`0061edb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md) → [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) FUN_0061edf4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061ebd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061ebd0.md) [`0061edb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0061ec10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061ec10.md) [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061ef6c",
      "incomplete_value": false,
      "site": "0061ef78",
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
      "definition_site": "0061ef2c",
      "incomplete_value": false,
      "site": "0061ef38",
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
      "definition_site": "0061f024",
      "incomplete_value": false,
      "site": "0061f02c",
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
      "definition_site": "0061efe4",
      "incomplete_value": false,
      "site": "0061efec",
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
      "definition_site": "0061f0ec",
      "incomplete_value": false,
      "site": "0061f0f8",
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
      "definition_site": "0061f0ac",
      "incomplete_value": false,
      "site": "0061f0b8",
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
      "0061ef6c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0061f024",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0061f03c",
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
      "0061ef6c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061f024",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061f03c",
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

- 旧版 [`0061ef38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md#insn-0061ef38) · [`0061efec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md#insn-0061efec) · [`0061f0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md#insn-0061f0b8)
- 新版 `0061ef78`（命令位置の公開資料なし） · `0061f02c`（命令位置の公開資料なし） · `0061f0f8`（命令位置の公開資料なし）

~~~diff
- 0061ef38 ["INT_ADD", "register:40f0:8", ["const:61ef38:8", "const:4:8"]]
- 0061ef38 ["CALL", null, ["callee:00441e94:8"]]
+ 0061ef78 ["INT_ADD", "register:40f0:8", ["const:61ef78:8", "const:4:8"]]
+ 0061ef78 ["CALL", null, ["callee:00441e94:8"]]
- 0061ef38 bytes c78bf897
+ 0061ef78 bytes c78bf897
- 0061efec ["INT_ADD", "register:40f0:8", ["const:61efec:8", "const:4:8"]]
- 0061efec ["CALL", null, ["callee:00441e94:8"]]
+ 0061f02c ["INT_ADD", "register:40f0:8", ["const:61f02c:8", "const:4:8"]]
+ 0061f02c ["CALL", null, ["callee:00441e94:8"]]
- 0061efec bytes 9a8bf897
+ 0061f02c bytes 9a8bf897
- 0061f0b8 ["INT_ADD", "register:40f0:8", ["const:61f0b8:8", "const:4:8"]]
- 0061f0b8 ["CALL", null, ["callee:004427f4:8"]]
+ 0061f0f8 ["INT_ADD", "register:40f0:8", ["const:61f0f8:8", "const:4:8"]]
+ 0061f0f8 ["CALL", null, ["callee:004427f4:8"]]
- 0061f0b8 bytes bf8df897
+ 0061f0f8 bytes bf8df897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fb01ef4e1df5cc6c60a718e7d6d8ad4"></a>

### [`0061f994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md) → [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) FUN_0061f9d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061edb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061e/0061edb4.md) [`0061f994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061fb4c",
      "incomplete_value": false,
      "site": "0061fb54",
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
      "definition_site": "0061fb0c",
      "incomplete_value": false,
      "site": "0061fb14",
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
      "definition_site": "0061fc00",
      "incomplete_value": true,
      "site": "0061fc08",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061fbc0",
      "incomplete_value": true,
      "site": "0061fbc8",
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
      "definition_site": "0061fccc",
      "incomplete_value": false,
      "site": "0061fcdc",
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
      "definition_site": "0061fc8c",
      "incomplete_value": false,
      "site": "0061fc9c",
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
      "0061fb4c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0061fc00",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0061fc18",
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
      "0061fb4c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061fc00",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061fc18",
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

- 旧版 [`0061fb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md#insn-0061fb14) · [`0061fbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md#insn-0061fbc8) · [`0061fc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md#insn-0061fc9c)
- 新版 `0061fb54`（命令位置の公開資料なし） · `0061fc08`（命令位置の公開資料なし） · `0061fcdc`（命令位置の公開資料なし）

~~~diff
- 0061fb14 ["INT_ADD", "register:40f0:8", ["const:61fb14:8", "const:4:8"]]
- 0061fb14 ["CALL", null, ["callee:00441e94:8"]]
+ 0061fb54 ["INT_ADD", "register:40f0:8", ["const:61fb54:8", "const:4:8"]]
+ 0061fb54 ["CALL", null, ["callee:00441e94:8"]]
- 0061fb14 bytes d088f897
+ 0061fb54 bytes d088f897
- 0061fbc8 ["INT_ADD", "register:40f0:8", ["const:61fbc8:8", "const:4:8"]]
- 0061fbc8 ["CALL", null, ["callee:00441e94:8"]]
+ 0061fc08 ["INT_ADD", "register:40f0:8", ["const:61fc08:8", "const:4:8"]]
+ 0061fc08 ["CALL", null, ["callee:00441e94:8"]]
- 0061fbc8 bytes a388f897
+ 0061fc08 bytes a388f897
- 0061fc9c ["INT_ADD", "register:40f0:8", ["const:61fc9c:8", "const:4:8"]]
- 0061fc9c ["CALL", null, ["callee:004427f4:8"]]
+ 0061fcdc ["INT_ADD", "register:40f0:8", ["const:61fcdc:8", "const:4:8"]]
+ 0061fcdc ["CALL", null, ["callee:004427f4:8"]]
- 0061fc9c bytes c68af897
+ 0061fcdc bytes c68af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d0f0b9d9bf66a37c3536325ec33166"></a>

### [`006203f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md) → [`00620430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md) FUN_00620430

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061f994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061f/0061f994.md) [`006203f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) [`00620430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006205a0",
      "incomplete_value": false,
      "site": "006205a8",
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
      "definition_site": "00620560",
      "incomplete_value": false,
      "site": "00620568",
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
      "definition_site": "00620654",
      "incomplete_value": false,
      "site": "0062065c",
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
      "definition_site": "00620614",
      "incomplete_value": false,
      "site": "0062061c",
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
      "definition_site": "0062066c",
      "incomplete_value": false,
      "site": "0062067c",
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
      "definition_site": "0062062c",
      "incomplete_value": false,
      "site": "0062063c",
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
      "006205a0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00620654",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0062066c",
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
      "006205a0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00620654",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0062066c",
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

- 旧版 [`00620568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md#insn-00620568) · [`0062061c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md#insn-0062061c) · [`0062063c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md#insn-0062063c)
- 新版 `006205a8`（命令位置の公開資料なし） · `0062065c`（命令位置の公開資料なし） · `0062067c`（命令位置の公開資料なし）

~~~diff
- 00620568 ["INT_ADD", "register:40f0:8", ["const:620568:8", "const:4:8"]]
- 00620568 ["CALL", null, ["callee:00441e94:8"]]
+ 006205a8 ["INT_ADD", "register:40f0:8", ["const:6205a8:8", "const:4:8"]]
+ 006205a8 ["CALL", null, ["callee:00441e94:8"]]
- 00620568 bytes 3b86f897
+ 006205a8 bytes 3b86f897
- 0062061c ["INT_ADD", "register:40f0:8", ["const:62061c:8", "const:4:8"]]
- 0062061c ["CALL", null, ["callee:00441e94:8"]]
+ 0062065c ["INT_ADD", "register:40f0:8", ["const:62065c:8", "const:4:8"]]
+ 0062065c ["CALL", null, ["callee:00441e94:8"]]
- 0062061c bytes 0e86f897
+ 0062065c bytes 0e86f897
- 0062063c ["INT_ADD", "register:40f0:8", ["const:62063c:8", "const:4:8"]]
- 0062063c ["CALL", null, ["callee:004427f4:8"]]
+ 0062067c ["INT_ADD", "register:40f0:8", ["const:62067c:8", "const:4:8"]]
+ 0062067c ["CALL", null, ["callee:004427f4:8"]]
- 0062063c bytes 5e88f897
+ 0062067c bytes 5e88f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe2d11ac981afb02781b150999a6fe58"></a>

### [`00620ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md) → [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) FUN_00620f24

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00620cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620cf0.md) [`00620ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00620d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620d30.md) [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062115c",
      "incomplete_value": true,
      "site": "00621164",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062111c",
      "incomplete_value": true,
      "site": "00621124",
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
      "definition_site": "00621174",
      "incomplete_value": false,
      "site": "00621180",
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
      "definition_site": "00621134",
      "incomplete_value": false,
      "site": "00621140",
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
      "definition_site": "006214c0",
      "incomplete_value": false,
      "site": "006214d0",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00621480",
      "incomplete_value": false,
      "site": "00621490",
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
            "const:cf5:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006210a4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0062115c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00621174",
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
      "006210a4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0062115c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00621174",
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

- 旧版 [`00621124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md#insn-00621124) · [`00621140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md#insn-00621140) · [`00621450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md#insn-00621450)
- 新版 `00621164`（命令位置の公開資料なし） · `00621180`（命令位置の公開資料なし） · `00621490`（命令位置の公開資料なし）

~~~diff
- 00621124 ["INT_ADD", "register:40f0:8", ["const:621124:8", "const:4:8"]]
- 00621124 ["CALL", null, ["callee:00441e94:8"]]
+ 00621164 ["INT_ADD", "register:40f0:8", ["const:621164:8", "const:4:8"]]
+ 00621164 ["CALL", null, ["callee:00441e94:8"]]
- 00621124 bytes 4c83f897
+ 00621164 bytes 4c83f897
- 00621140 ["INT_ADD", "register:40f0:8", ["const:621140:8", "const:4:8"]]
- 00621140 ["CALL", null, ["callee:004427f4:8"]]
+ 00621180 ["INT_ADD", "register:40f0:8", ["const:621180:8", "const:4:8"]]
+ 00621180 ["CALL", null, ["callee:004427f4:8"]]
- 00621140 bytes 9d85f897
+ 00621180 bytes 9d85f897
- 00621450 ["INT_ADD", "register:40f0:8", ["const:621450:8", "const:4:8"]]
- 00621450 ["CALL", null, ["callee:00c57e90:8"]]
+ 00621490 ["INT_ADD", "register:40f0:8", ["const:621490:8", "const:4:8"]]
+ 00621490 ["CALL", null, ["callee:00c57e90:8"]]
- 00621450 bytes 90d91894
+ 00621490 bytes 80da1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2778fada84b74e73fad731b549f06da5"></a>

### [`00621ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md) → [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) FUN_00621b10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00620ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/00620ee4.md) [`00621ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00621d40",
      "incomplete_value": false,
      "site": "00621d48",
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
      "definition_site": "00621d00",
      "incomplete_value": false,
      "site": "00621d08",
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
      "definition_site": "00621d5c",
      "incomplete_value": false,
      "site": "00621d68",
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
      "definition_site": "00621d1c",
      "incomplete_value": false,
      "site": "00621d28",
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
      "definition_site": "00621e10",
      "incomplete_value": false,
      "site": "00621e1c",
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
      "definition_site": "00621dd0",
      "incomplete_value": false,
      "site": "00621ddc",
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
      "00621c88",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00621d40",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00621d5c",
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
      "00621c88",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00621d40",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00621d5c",
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

- 旧版 [`00621d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md#insn-00621d08) · [`00621d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md#insn-00621d28) · [`00621ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md#insn-00621ddc)
- 新版 `00621d48`（命令位置の公開資料なし） · `00621d68`（命令位置の公開資料なし） · `00621e1c`（命令位置の公開資料なし）

~~~diff
- 00621d08 ["INT_ADD", "register:40f0:8", ["const:621d08:8", "const:4:8"]]
- 00621d08 ["CALL", null, ["callee:00441e94:8"]]
+ 00621d48 ["INT_ADD", "register:40f0:8", ["const:621d48:8", "const:4:8"]]
+ 00621d48 ["CALL", null, ["callee:00441e94:8"]]
- 00621d08 bytes 5380f897
+ 00621d48 bytes 5380f897
- 00621d28 ["INT_ADD", "register:40f0:8", ["const:621d28:8", "const:4:8"]]
- 00621d28 ["CALL", null, ["callee:004427f4:8"]]
+ 00621d68 ["INT_ADD", "register:40f0:8", ["const:621d68:8", "const:4:8"]]
+ 00621d68 ["CALL", null, ["callee:004427f4:8"]]
- 00621d28 bytes a382f897
+ 00621d68 bytes a382f897
- 00621ddc ["INT_ADD", "register:40f0:8", ["const:621ddc:8", "const:4:8"]]
- 00621ddc ["CALL", null, ["callee:004427f4:8"]]
+ 00621e1c ["INT_ADD", "register:40f0:8", ["const:621e1c:8", "const:4:8"]]
+ 00621e1c ["CALL", null, ["callee:004427f4:8"]]
- 00621ddc bytes 7682f897
+ 00621e1c bytes 7682f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d18212751d3cf2b2b185b54268f1d34"></a>

### [`00622520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md) → [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) FUN_00622560

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00621ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00621/00621ad0.md) [`00622520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006226d0",
      "incomplete_value": false,
      "site": "006226d8",
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
      "definition_site": "00622690",
      "incomplete_value": false,
      "site": "00622698",
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
      "definition_site": "00622784",
      "incomplete_value": true,
      "site": "0062278c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00622744",
      "incomplete_value": true,
      "site": "0062274c",
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
      "definition_site": "00622850",
      "incomplete_value": false,
      "site": "00622860",
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
      "definition_site": "00622810",
      "incomplete_value": false,
      "site": "00622820",
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
      "006226d0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00622784",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0062279c",
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
      "006226d0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00622784",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0062279c",
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

- 旧版 [`00622698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md#insn-00622698) · [`0062274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md#insn-0062274c) · [`00622820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md#insn-00622820)
- 新版 `006226d8`（命令位置の公開資料なし） · `0062278c`（命令位置の公開資料なし） · `00622860`（命令位置の公開資料なし）

~~~diff
- 00622698 ["INT_ADD", "register:40f0:8", ["const:622698:8", "const:4:8"]]
- 00622698 ["CALL", null, ["callee:00441e94:8"]]
+ 006226d8 ["INT_ADD", "register:40f0:8", ["const:6226d8:8", "const:4:8"]]
+ 006226d8 ["CALL", null, ["callee:00441e94:8"]]
- 00622698 bytes ef7df897
+ 006226d8 bytes ef7df897
- 0062274c ["INT_ADD", "register:40f0:8", ["const:62274c:8", "const:4:8"]]
- 0062274c ["CALL", null, ["callee:00441e94:8"]]
+ 0062278c ["INT_ADD", "register:40f0:8", ["const:62278c:8", "const:4:8"]]
+ 0062278c ["CALL", null, ["callee:00441e94:8"]]
- 0062274c bytes c27df897
+ 0062278c bytes c27df897
- 00622820 ["INT_ADD", "register:40f0:8", ["const:622820:8", "const:4:8"]]
- 00622820 ["CALL", null, ["callee:004427f4:8"]]
+ 00622860 ["INT_ADD", "register:40f0:8", ["const:622860:8", "const:4:8"]]
+ 00622860 ["CALL", null, ["callee:004427f4:8"]]
- 00622820 bytes e57ff897
+ 00622860 bytes e57ff897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c780f733581269a6b8ec3f92db2772b6"></a>

### [`00622e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md) → [`00622e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md) FUN_00622e60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00622520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622520.md) [`00622e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md) [`00630244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630244.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 4件 [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) [`00622e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md) [`00630284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630284.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00622fbc",
      "incomplete_value": false,
      "site": "00622fc4",
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
      "definition_site": "00622f7c",
      "incomplete_value": false,
      "site": "00622f84",
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
      "definition_site": "00622fe0",
      "incomplete_value": false,
      "site": "00622fec",
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
      "definition_site": "00622fa0",
      "incomplete_value": false,
      "site": "00622fac",
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
      "definition_site": "00623114",
      "incomplete_value": false,
      "site": "0062311c",
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
      "definition_site": "006230d4",
      "incomplete_value": false,
      "site": "006230dc",
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
      "00622fbc",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00622fe0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00623114",
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
      "00622fbc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00622fe0",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00623114",
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

- 旧版 [`00622f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md#insn-00622f84) · [`00622fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md#insn-00622fac) · [`006230dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md#insn-006230dc)
- 新版 `00622fc4`（命令位置の公開資料なし） · `00622fec`（命令位置の公開資料なし） · `0062311c`（命令位置の公開資料なし）

~~~diff
- 00622f84 ["INT_ADD", "register:40f0:8", ["const:622f84:8", "const:4:8"]]
- 00622f84 ["CALL", null, ["callee:00441e94:8"]]
+ 00622fc4 ["INT_ADD", "register:40f0:8", ["const:622fc4:8", "const:4:8"]]
+ 00622fc4 ["CALL", null, ["callee:00441e94:8"]]
- 00622f84 bytes b47bf897
+ 00622fc4 bytes b47bf897
- 00622fac ["INT_ADD", "register:40f0:8", ["const:622fac:8", "const:4:8"]]
- 00622fac ["CALL", null, ["callee:004427f4:8"]]
+ 00622fec ["INT_ADD", "register:40f0:8", ["const:622fec:8", "const:4:8"]]
+ 00622fec ["CALL", null, ["callee:004427f4:8"]]
- 00622fac bytes 027ef897
+ 00622fec bytes 027ef897
- 006230dc ["INT_ADD", "register:40f0:8", ["const:6230dc:8", "const:4:8"]]
- 006230dc ["CALL", null, ["callee:00441e94:8"]]
+ 0062311c ["INT_ADD", "register:40f0:8", ["const:62311c:8", "const:4:8"]]
+ 0062311c ["CALL", null, ["callee:00441e94:8"]]
- 006230dc bytes 5e7bf897
+ 0062311c bytes 5e7bf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b772f031c092d42f9c78d00f43d0bfaf"></a>

### [`00623638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md) → [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) FUN_00623678

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00611b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611b9c.md) [`00623638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md) [`006256d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00625/006256d8.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`00611bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611bdc.md) [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006238a8",
      "incomplete_value": false,
      "site": "006238b0",
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
      "definition_site": "00623868",
      "incomplete_value": false,
      "site": "00623870",
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
      "definition_site": "006238c4",
      "incomplete_value": false,
      "site": "006238d0",
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
      "definition_site": "00623884",
      "incomplete_value": false,
      "site": "00623890",
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
      "definition_site": "00623b84",
      "incomplete_value": false,
      "site": "00623b94",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00623b44",
      "incomplete_value": false,
      "site": "00623b54",
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
            "const:cf5:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006237e8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "006238a8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "006238c4",
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
      "006237e8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006238a8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006238c4",
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

- 旧版 [`00623870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md#insn-00623870) · [`00623890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md#insn-00623890) · [`00623b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md#insn-00623b14)
- 新版 `006238b0`（命令位置の公開資料なし） · `006238d0`（命令位置の公開資料なし） · `00623b54`（命令位置の公開資料なし）

~~~diff
- 00623870 ["INT_ADD", "register:40f0:8", ["const:623870:8", "const:4:8"]]
- 00623870 ["CALL", null, ["callee:00441e94:8"]]
+ 006238b0 ["INT_ADD", "register:40f0:8", ["const:6238b0:8", "const:4:8"]]
+ 006238b0 ["CALL", null, ["callee:00441e94:8"]]
- 00623870 bytes 7979f897
+ 006238b0 bytes 7979f897
- 00623890 ["INT_ADD", "register:40f0:8", ["const:623890:8", "const:4:8"]]
- 00623890 ["CALL", null, ["callee:004427f4:8"]]
+ 006238d0 ["INT_ADD", "register:40f0:8", ["const:6238d0:8", "const:4:8"]]
+ 006238d0 ["CALL", null, ["callee:004427f4:8"]]
- 00623890 bytes c97bf897
+ 006238d0 bytes c97bf897
- 00623b14 ["INT_ADD", "register:40f0:8", ["const:623b14:8", "const:4:8"]]
- 00623b14 ["CALL", null, ["callee:00c57e90:8"]]
+ 00623b54 ["INT_ADD", "register:40f0:8", ["const:623b54:8", "const:4:8"]]
+ 00623b54 ["CALL", null, ["callee:00c57e90:8"]]
- 00623b14 bytes dfcf1894
+ 00623b54 bytes cfd01894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6a0c90227cd2b06793540f411e037ae"></a>

### [`00623f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md) → [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) FUN_00623f68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00623638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623638.md) [`00623f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`009dcf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcf68.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 4件 [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009dd104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624214",
      "incomplete_value": false,
      "site": "0062421c",
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
      "definition_site": "006241d4",
      "incomplete_value": false,
      "site": "006241dc",
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
      "definition_site": "006242bc",
      "incomplete_value": false,
      "site": "006242c8",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062427c",
      "incomplete_value": false,
      "site": "00624288",
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
            "const:30f:8"
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
      "definition_site": "006244d8",
      "incomplete_value": false,
      "site": "006244e8",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624498",
      "incomplete_value": false,
      "site": "006244a8",
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
            "const:cf5:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006240bc",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "006240e0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00624214",
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
      "006240bc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006240e0",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00624214",
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

- 旧版 [`006241dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md#insn-006241dc) · [`00624288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md#insn-00624288) · [`006244a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00623/00623f28.md#insn-006244a8)
- 新版 `0062421c`（命令位置の公開資料なし） · `006242c8`（命令位置の公開資料なし） · `006244e8`（命令位置の公開資料なし）

~~~diff
- 006241dc ["INT_ADD", "register:40f0:8", ["const:6241dc:8", "const:4:8"]]
- 006241dc ["CALL", null, ["callee:00441e94:8"]]
+ 0062421c ["INT_ADD", "register:40f0:8", ["const:62421c:8", "const:4:8"]]
+ 0062421c ["CALL", null, ["callee:00441e94:8"]]
- 006241dc bytes 1e77f897
+ 0062421c bytes 1e77f897
- 00624288 ["INT_ADD", "register:40f0:8", ["const:624288:8", "const:4:8"]]
- 00624288 ["CALL", null, ["callee:00441cec:8"]]
+ 006242c8 ["INT_ADD", "register:40f0:8", ["const:6242c8:8", "const:4:8"]]
+ 006242c8 ["CALL", null, ["callee:00441cec:8"]]
- 00624288 bytes 8976f897
+ 006242c8 bytes 8976f897
- 006244a8 ["INT_ADD", "register:40f0:8", ["const:6244a8:8", "const:4:8"]]
- 006244a8 ["CALL", null, ["callee:00c58080:8"]]
+ 006244e8 ["INT_ADD", "register:40f0:8", ["const:6244e8:8", "const:4:8"]]
+ 006244e8 ["CALL", null, ["callee:00c58080:8"]]
- 006244a8 bytes f6cd1894
+ 006244e8 bytes e6ce1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64c7a1b62cd82c77de631d576832b30"></a>

### [`0062472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/0062472c.md) → [`0062476c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/0062476c.md) FUN_0062476c

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
      "definition_site": "00624780",
      "incomplete_value": false,
      "site": "00624784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624740",
      "incomplete_value": false,
      "site": "00624744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00624784",
      "DATA",
      [
        "storage",
        "00c725d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00624784",
      "DATA",
      [
        "storage",
        "00c729d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00624738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/0062472c.md#insn-00624738) · [`00624740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/0062472c.md#insn-00624740)
- 新版 `00624778`（命令位置の公開資料なし） · `00624780`（命令位置の公開資料なし）

~~~diff
- 00624738 ["INT_ADD", "register:40f0:8", ["const:624738:8", "const:4:8"]]
- 00624738 ["CALL", null, ["callee:00c57e90:8"]]
+ 00624778 ["INT_ADD", "register:40f0:8", ["const:624778:8", "const:4:8"]]
+ 00624778 ["CALL", null, ["callee:00c57e90:8"]]
- 00624738 bytes d6cc1894
+ 00624778 bytes c6cd1894
- 00624740 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00624740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00624740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00624740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00624780 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00624780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00624780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00624780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00624740 bytes 08611791
+ 00624780 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8335d3cc6b842b457736f61058836a5"></a>

### [`00624750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624750.md) → [`00624790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624790.md) FUN_00624790

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
      "definition_site": "00624794",
      "incomplete_value": false,
      "site": "00624798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624754",
      "incomplete_value": false,
      "site": "00624758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00624798",
      "DATA",
      [
        "storage",
        "00c725d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00624798",
      "DATA",
      [
        "storage",
        "00c729d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00624754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624750.md#insn-00624754)
- 新版 `00624794`（命令位置の公開資料なし）

~~~diff
- 00624754 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00624754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00624754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00624754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00624794 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00624794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00624794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00624794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00624754 bytes 08611791
+ 00624794 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9afa21bb0e3dcdc5e838c79ecf7325"></a>

### [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) → [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) FUN_006247a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0072bc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bc78.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0072bcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bcb8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624a64",
      "incomplete_value": false,
      "site": "00624a68",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624a24",
      "incomplete_value": false,
      "site": "00624a28",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624a78",
      "incomplete_value": true,
      "site": "00624aa0",
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
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624a38",
      "incomplete_value": true,
      "site": "00624a60",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624a90",
      "incomplete_value": false,
      "site": "00624aa0",
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
      "definition_site": "00624a50",
      "incomplete_value": false,
      "site": "00624a60",
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
    "ordinal": 25,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0062491c",
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00624994",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006249b0",
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
      "0062491c",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00624994",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006249b0",
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

- 旧版 [`00624a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md#insn-00624a28) · [`00624a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md#insn-00624a60) · [`00624a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md#insn-00624a68)
- 新版 `00624a68`（命令位置の公開資料なし） · `00624aa0`（命令位置の公開資料なし） · `00624aa8`（命令位置の公開資料なし）

~~~diff
- 00624a28 ["INT_ADD", "register:40f0:8", ["const:624a28:8", "const:4:8"]]
- 00624a28 ["CALL", null, ["callee:00c57e50:8"]]
+ 00624a68 ["INT_ADD", "register:40f0:8", ["const:624a68:8", "const:4:8"]]
+ 00624a68 ["CALL", null, ["callee:00c57e50:8"]]
- 00624a28 bytes 0acc1894
+ 00624a68 bytes facc1894
- 00624a60 ["INT_ADD", "register:40f0:8", ["const:624a60:8", "const:4:8"]]
- 00624a60 ["CALL", null, ["callee:00c57e30:8"]]
+ 00624aa0 ["INT_ADD", "register:40f0:8", ["const:624aa0:8", "const:4:8"]]
+ 00624aa0 ["CALL", null, ["callee:00c57e30:8"]]
- 00624a60 bytes f4cb1894
+ 00624aa0 bytes e4cc1894
- 00624a68 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00624a68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00624a68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00624a68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00624aa8 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00624aa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00624aa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00624aa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00624a68 bytes 00e02c91
+ 00624aa8 bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495a674c4e29ce4e4f3108958553bb63"></a>

### [`00624c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md) → [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) FUN_00624cbc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00624b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624b2c.md) [`00624c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`00624b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624b6c.md) [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624ee8",
      "incomplete_value": false,
      "site": "00624ef0",
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
      "definition_site": "00624ea8",
      "incomplete_value": false,
      "site": "00624eb0",
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
      "definition_site": "00625218",
      "incomplete_value": false,
      "site": "00625224",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006251d8",
      "incomplete_value": false,
      "site": "006251e4",
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
            "const:cf5:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062538c",
      "incomplete_value": false,
      "site": "00625398",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062534c",
      "incomplete_value": false,
      "site": "00625358",
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
            "const:30f:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00624e34",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00624ee8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00624f00",
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
      "00624e34",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00624ee8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00624f00",
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

- 旧版 [`00624eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md#insn-00624eb0) · [`006251e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md#insn-006251e4) · [`00625358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624c7c.md#insn-00625358)
- 新版 `00624ef0`（命令位置の公開資料なし） · `00625224`（命令位置の公開資料なし） · `00625398`（命令位置の公開資料なし）

~~~diff
- 00624eb0 ["INT_ADD", "register:40f0:8", ["const:624eb0:8", "const:4:8"]]
- 00624eb0 ["CALL", null, ["callee:00441e94:8"]]
+ 00624ef0 ["INT_ADD", "register:40f0:8", ["const:624ef0:8", "const:4:8"]]
+ 00624ef0 ["CALL", null, ["callee:00441e94:8"]]
- 00624eb0 bytes e973f897
+ 00624ef0 bytes e973f897
- 006251e4 ["INT_ADD", "register:40f0:8", ["const:6251e4:8", "const:4:8"]]
- 006251e4 ["CALL", null, ["callee:00c58080:8"]]
+ 00625224 ["INT_ADD", "register:40f0:8", ["const:625224:8", "const:4:8"]]
+ 00625224 ["CALL", null, ["callee:00c58080:8"]]
- 006251e4 bytes a7ca1894
+ 00625224 bytes 97cb1894
- 00625358 ["INT_ADD", "register:40f0:8", ["const:625358:8", "const:4:8"]]
- 00625358 ["CALL", null, ["callee:00441cec:8"]]
+ 00625398 ["INT_ADD", "register:40f0:8", ["const:625398:8", "const:4:8"]]
+ 00625398 ["CALL", null, ["callee:00441cec:8"]]
- 00625358 bytes 5572f897
+ 00625398 bytes 5572f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

