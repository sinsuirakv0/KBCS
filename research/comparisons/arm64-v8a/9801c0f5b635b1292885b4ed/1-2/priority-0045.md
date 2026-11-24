# v16.0.0 → v16.0.1 · 最優先の変更候補 (45)

[一覧の目次](README.md)

<a id="compare-6dd288492dc697b75b4912c67f869015"></a>

### [`008744a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744a4.md) → [`008744e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md) FUN_008744e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874508",
      "incomplete_value": false,
      "site": "0087450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008744c8",
      "incomplete_value": false,
      "site": "008744cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0087450c",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087450c",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008744b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744a4.md#insn-008744b8) · [`008744c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744a4.md#insn-008744c8) · [`008744e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744a4.md#insn-008744e8)
- 新版 [`008744f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-008744f8) · [`00874508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-00874508) · [`00874528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-00874528)

~~~diff
- 008744b8 ["INT_ADD", "register:40f0:8", ["const:8744b8:8", "const:4:8"]]
- 008744b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 008744f8 ["INT_ADD", "register:40f0:8", ["const:8744f8:8", "const:4:8"]]
+ 008744f8 ["CALL", null, ["callee:00c57e90:8"]]
- 008744b8 bytes 768d0f94
+ 008744f8 bytes 668e0f94
- 008744c8 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 008744c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008744c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008744c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874508 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00874508 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874508 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874508 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008744c8 bytes 29012391
+ 00874508 bytes 29013391
- 008744e8 ["INT_ADD", "register:40f0:8", ["const:8744e8:8", "const:4:8"]]
- 008744e8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00874528 ["INT_ADD", "register:40f0:8", ["const:874528:8", "const:4:8"]]
+ 00874528 ["CALL", null, ["callee:00c53cd0:8"]]
- 008744e8 bytes f27c0f94
+ 00874528 bytes ea7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29d3fb9f239f91eb9f2f34bf1f8caf7"></a>

### [`008744fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744fc.md) → [`0087453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md) FUN_0087453c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00874544",
      "incomplete_value": false,
      "site": "00874548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874504",
      "incomplete_value": false,
      "site": "00874508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00874548",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874548",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744fc.md#insn-00874504) · [`0087452c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008744fc.md#insn-0087452c)
- 新版 [`00874544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md#insn-00874544) · [`0087456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md#insn-0087456c)

~~~diff
- 00874504 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00874504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874544 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00874544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874504 bytes 29012391
+ 00874544 bytes 29013391
- 0087452c ["INT_ADD", "register:40f0:8", ["const:87452c:8", "const:4:8"]]
- 0087452c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0087456c ["INT_ADD", "register:40f0:8", ["const:87456c:8", "const:4:8"]]
+ 0087456c ["CALL", null, ["callee:00c53cd0:8"]]
- 0087452c bytes e17c0f94
+ 0087456c bytes d97d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74af2797df37d4601b82ac9375f35d0"></a>

### [`008746a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md) → [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) FUN_008746e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008745d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008745d8.md) · 呼出先 7件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) [`008749f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749f4.md) [`00874a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874a44.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00874618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md) · 呼出先 7件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) [`00874a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md) [`00874a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874784",
      "incomplete_value": false,
      "site": "00874784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874744",
      "incomplete_value": false,
      "site": "00874744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "008747a0",
      "incomplete_value": false,
      "site": "008747a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874760",
      "incomplete_value": false,
      "site": "00874760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00874784",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ],
    [
      "008747a0",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ],
    [
      "008747e8",
      "READ",
      [
        "storage",
        "00c7f950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00874784",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "008747a0",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "008747e8",
      "READ",
      [
        "storage",
        "00c7fd50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md#insn-0087472c) · [`00874734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md#insn-00874734) · [`0087474c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008746a8.md#insn-0087474c)
- 新版 [`0087476c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-0087476c) · [`00874774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-00874774) · [`0087478c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-0087478c)

~~~diff
- 0087472c ["INT_ADD", "register:40f0:8", ["const:87472c:8", "const:4:8"]]
- 0087472c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0087476c ["INT_ADD", "register:40f0:8", ["const:87476c:8", "const:4:8"]]
+ 0087476c ["CALL", null, ["callee:00c53cd0:8"]]
- 0087472c bytes 617c0f94
+ 0087476c bytes 597d0f94
- 00874734 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00874734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874774 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00874774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874734 bytes 08c12491
+ 00874774 bytes 08c13491
- 0087474c ["INT_ADD", "register:40f0:8", ["const:87474c:8", "const:4:8"]]
- 0087474c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0087478c ["INT_ADD", "register:40f0:8", ["const:87478c:8", "const:4:8"]]
+ 0087478c ["CALL", null, ["callee:00c53cd0:8"]]
- 0087474c bytes 597c0f94
+ 0087478c bytes 517d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f99c4464aec73ff0b75257c1a3e6a89"></a>

### [`008748a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008748a8.md) → [`008748e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md) FUN_008748e8

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
      "definition_site": "008748fc",
      "incomplete_value": false,
      "site": "00874900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008748bc",
      "incomplete_value": false,
      "site": "008748c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "00874900",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874900",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008748bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008748a8.md#insn-008748bc) · [`008748d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008748a8.md#insn-008748d0) · [`008748f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008748a8.md#insn-008748f0)
- 新版 [`008748fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-008748fc) · [`00874910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-00874910) · [`00874930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-00874930)

~~~diff
- 008748bc ["COPY", "tmp:0:8", ["const:930:8"]]
- 008748bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008748bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008748bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008748fc ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 008748fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008748fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008748fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008748bc bytes 08c12491
+ 008748fc bytes 08c13491
- 008748d0 ["INT_ADD", "register:40f0:8", ["const:8748d0:8", "const:4:8"]]
- 008748d0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874910 ["INT_ADD", "register:40f0:8", ["const:874910:8", "const:4:8"]]
+ 00874910 ["CALL", null, ["callee:00c53d00:8"]]
- 008748d0 bytes 047c0f94
+ 00874910 bytes fc7c0f94
- 008748f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008748f0 ["INT_ADD", "register:40f0:8", ["const:8748f0:8", "const:4:8"]]
- 008748f0 ["CALLIND", null, ["register:0:8"]]
+ 00874930 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874930 ["INT_ADD", "register:40f0:8", ["const:874930:8", "const:4:8"]]
+ 00874930 ["CALLIND", null, ["register:0:8"]]
- 008748f0 bytes 00013fd6
+ 00874930 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-981ad75a412b8966930ae9ed3c37a7be"></a>

### [`00874904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874904.md) → [`00874944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md) FUN_00874944

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
      "definition_site": "0087495c",
      "incomplete_value": false,
      "site": "00874960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087491c",
      "incomplete_value": false,
      "site": "00874920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00874960",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874960",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874904.md#insn-0087491c) · [`00874930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874904.md#insn-00874930) · [`00874944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874904.md#insn-00874944)
- 新版 [`0087495c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-0087495c) · [`00874970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-00874970) · [`00874984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-00874984)

~~~diff
- 0087491c ["COPY", "tmp:0:8", ["const:930:8"]]
- 0087491c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087491c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087491c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087495c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0087495c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087495c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087495c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087491c bytes 08c12491
+ 0087495c bytes 08c13491
- 00874930 ["INT_ADD", "register:40f0:8", ["const:874930:8", "const:4:8"]]
- 00874930 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874970 ["INT_ADD", "register:40f0:8", ["const:874970:8", "const:4:8"]]
+ 00874970 ["CALL", null, ["callee:00c53d00:8"]]
- 00874930 bytes ec7b0f94
+ 00874970 bytes e47c0f94
- 00874944 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874944 ["INT_ADD", "register:40f0:8", ["const:874944:8", "const:4:8"]]
- 00874944 ["CALLIND", null, ["register:0:8"]]
+ 00874984 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874984 ["INT_ADD", "register:40f0:8", ["const:874984:8", "const:4:8"]]
+ 00874984 ["CALLIND", null, ["register:0:8"]]
- 00874944 bytes 00013fd6
+ 00874984 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9a6c9ccd78e3ce0e5deec7b8ed1dd9"></a>

### [`00874960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874960.md) → [`008749a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md) FUN_008749a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008749c4",
      "incomplete_value": false,
      "site": "008749c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874984",
      "incomplete_value": false,
      "site": "00874988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "008749c8",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008749c8",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874960.md#insn-00874974) · [`00874984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874960.md#insn-00874984) · [`008749a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874960.md#insn-008749a4)
- 新版 [`008749b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749b4) · [`008749c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749c4) · [`008749e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749e4)

~~~diff
- 00874974 ["INT_ADD", "register:40f0:8", ["const:874974:8", "const:4:8"]]
- 00874974 ["CALL", null, ["callee:00c57e90:8"]]
+ 008749b4 ["INT_ADD", "register:40f0:8", ["const:8749b4:8", "const:4:8"]]
+ 008749b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00874974 bytes 478c0f94
+ 008749b4 bytes 378d0f94
- 00874984 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00874984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008749c4 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 008749c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008749c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008749c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874984 bytes 29c12491
+ 008749c4 bytes 29c13491
- 008749a4 ["INT_ADD", "register:40f0:8", ["const:8749a4:8", "const:4:8"]]
- 008749a4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008749e4 ["INT_ADD", "register:40f0:8", ["const:8749e4:8", "const:4:8"]]
+ 008749e4 ["CALL", null, ["callee:00c53cd0:8"]]
- 008749a4 bytes c37b0f94
+ 008749e4 bytes bb7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e23fb66bf12e15886caab6a652941355"></a>

### [`008749b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749b8.md) → [`008749f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md) FUN_008749f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00874a00",
      "incomplete_value": false,
      "site": "00874a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008749c0",
      "incomplete_value": false,
      "site": "008749c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "00874a04",
      "DATA",
      [
        "storage",
        "00c7f930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874a04",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008749c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749b8.md#insn-008749c0) · [`008749e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/008749b8.md#insn-008749e8)
- 新版 [`00874a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md#insn-00874a00) · [`00874a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md#insn-00874a28)

~~~diff
- 008749c0 ["COPY", "tmp:0:8", ["const:930:8"]]
- 008749c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008749c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008749c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874a00 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00874a00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008749c0 bytes 29c12491
+ 00874a00 bytes 29c13491
- 008749e8 ["INT_ADD", "register:40f0:8", ["const:8749e8:8", "const:4:8"]]
- 008749e8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00874a28 ["INT_ADD", "register:40f0:8", ["const:874a28:8", "const:4:8"]]
+ 00874a28 ["CALL", null, ["callee:00c53cd0:8"]]
- 008749e8 bytes b27b0f94
+ 00874a28 bytes aa7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c04968cda86d5225e75c2edf73ea7c5"></a>

### [`00874b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b1c.md) → [`00874b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md) FUN_00874b5c

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
      "definition_site": "00874b70",
      "incomplete_value": false,
      "site": "00874b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874b30",
      "incomplete_value": false,
      "site": "00874b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00874b74",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874b74",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b1c.md#insn-00874b30) · [`00874b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b1c.md#insn-00874b44) · [`00874b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b1c.md#insn-00874b64)
- 新版 [`00874b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874b70) · [`00874b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874b84) · [`00874ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874ba4)

~~~diff
- 00874b30 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00874b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874b70 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00874b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874b30 bytes 08012791
+ 00874b70 bytes 08013791
- 00874b44 ["INT_ADD", "register:40f0:8", ["const:874b44:8", "const:4:8"]]
- 00874b44 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874b84 ["INT_ADD", "register:40f0:8", ["const:874b84:8", "const:4:8"]]
+ 00874b84 ["CALL", null, ["callee:00c53d00:8"]]
- 00874b44 bytes 677b0f94
+ 00874b84 bytes 5f7c0f94
- 00874b64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874b64 ["INT_ADD", "register:40f0:8", ["const:874b64:8", "const:4:8"]]
- 00874b64 ["CALLIND", null, ["register:0:8"]]
+ 00874ba4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874ba4 ["INT_ADD", "register:40f0:8", ["const:874ba4:8", "const:4:8"]]
+ 00874ba4 ["CALLIND", null, ["register:0:8"]]
- 00874b64 bytes 00013fd6
+ 00874ba4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97104581427000f8423d56bd83bafc13"></a>

### [`00874b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b78.md) → [`00874bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md) FUN_00874bb8

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
      "definition_site": "00874bd0",
      "incomplete_value": false,
      "site": "00874bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874b90",
      "incomplete_value": false,
      "site": "00874b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00874bd4",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874bd4",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b78.md#insn-00874b90) · [`00874ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b78.md#insn-00874ba4) · [`00874bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874b78.md#insn-00874bb8)
- 新版 [`00874bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874bd0) · [`00874be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874be4) · [`00874bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874bf8)

~~~diff
- 00874b90 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00874b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874bd0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00874bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874b90 bytes 08012791
+ 00874bd0 bytes 08013791
- 00874ba4 ["INT_ADD", "register:40f0:8", ["const:874ba4:8", "const:4:8"]]
- 00874ba4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00874be4 ["INT_ADD", "register:40f0:8", ["const:874be4:8", "const:4:8"]]
+ 00874be4 ["CALL", null, ["callee:00c53d00:8"]]
- 00874ba4 bytes 4f7b0f94
+ 00874be4 bytes 477c0f94
- 00874bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874bb8 ["INT_ADD", "register:40f0:8", ["const:874bb8:8", "const:4:8"]]
- 00874bb8 ["CALLIND", null, ["register:0:8"]]
+ 00874bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874bf8 ["INT_ADD", "register:40f0:8", ["const:874bf8:8", "const:4:8"]]
+ 00874bf8 ["CALLIND", null, ["register:0:8"]]
- 00874bb8 bytes 00013fd6
+ 00874bf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3592bf2e3503a088a9d608e0a8141ca2"></a>

### [`00874bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874bd4.md) → [`00874c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md) FUN_00874c14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874c38",
      "incomplete_value": false,
      "site": "00874c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874bf8",
      "incomplete_value": false,
      "site": "00874bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00874c3c",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874c3c",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874bd4.md#insn-00874be8) · [`00874bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874bd4.md#insn-00874bf8) · [`00874c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874bd4.md#insn-00874c18)
- 新版 [`00874c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c28) · [`00874c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c38) · [`00874c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c58)

~~~diff
- 00874be8 ["INT_ADD", "register:40f0:8", ["const:874be8:8", "const:4:8"]]
- 00874be8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00874c28 ["INT_ADD", "register:40f0:8", ["const:874c28:8", "const:4:8"]]
+ 00874c28 ["CALL", null, ["callee:00c57e90:8"]]
- 00874be8 bytes aa8b0f94
+ 00874c28 bytes 9a8c0f94
- 00874bf8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00874bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874c38 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00874c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874bf8 bytes 29012791
+ 00874c38 bytes 29013791
- 00874c18 ["INT_ADD", "register:40f0:8", ["const:874c18:8", "const:4:8"]]
- 00874c18 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00874c58 ["INT_ADD", "register:40f0:8", ["const:874c58:8", "const:4:8"]]
+ 00874c58 ["CALL", null, ["callee:00c53cd0:8"]]
- 00874c18 bytes 267b0f94
+ 00874c58 bytes 1e7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ef7bc29c39acb9480dc87a15e4b4bc"></a>

### [`00874c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c2c.md) → [`00874c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md) FUN_00874c6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00874c74",
      "incomplete_value": false,
      "site": "00874c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c34",
      "incomplete_value": false,
      "site": "00874c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00874c78",
      "DATA",
      [
        "storage",
        "00c7f9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874c78",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c2c.md#insn-00874c34) · [`00874c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874c2c.md#insn-00874c5c)
- 新版 [`00874c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md#insn-00874c74) · [`00874c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md#insn-00874c9c)

~~~diff
- 00874c34 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00874c34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874c34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874c34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874c74 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00874c74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874c34 bytes 29012791
+ 00874c74 bytes 29013791
- 00874c5c ["INT_ADD", "register:40f0:8", ["const:874c5c:8", "const:4:8"]]
- 00874c5c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00874c9c ["INT_ADD", "register:40f0:8", ["const:874c9c:8", "const:4:8"]]
+ 00874c9c ["CALL", null, ["callee:00c53cd0:8"]]
- 00874c5c bytes 157b0f94
+ 00874c9c bytes 0d7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5393305d2edba60c0ab1a3023de2a4"></a>

### [`00874d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md) → [`00874d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md) FUN_00874d7c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00874d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d08.md) · 呼出先 6件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00874d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d48.md) · 呼出先 6件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 72.28% / 新版 72.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874dd0",
      "incomplete_value": true,
      "site": "00874dd8",
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874d90",
      "incomplete_value": true,
      "site": "00874d98",
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
                "const:160:8"
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
      "definition_site": "00874dcc",
      "incomplete_value": true,
      "site": "00874ddc",
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
                "const:8ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874d8c",
      "incomplete_value": true,
      "site": "00874d9c",
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
                "const:7df:8"
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
      "definition_site": "00874dcc",
      "incomplete_value": true,
      "site": "00874ddc",
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
      "definition_site": "00874d8c",
      "incomplete_value": true,
      "site": "00874d9c",
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
      "00874dcc",
      "READ",
      [
        "storage",
        "002a47df",
        null,
        "string"
      ]
    ],
    [
      "00874dcc",
      "READ",
      [
        "storage",
        "002a47ef",
        null,
        "string"
      ]
    ],
    [
      "00874dd0",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00874dcc",
      "READ",
      [
        "storage",
        "002a48ac",
        null,
        "string"
      ]
    ],
    [
      "00874dcc",
      "READ",
      [
        "storage",
        "002a48bc",
        null,
        "string"
      ]
    ],
    [
      "00874dd0",
      "READ",
      [
        "storage",
        "002c31a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md#insn-00874dd8) · [`00874dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md#insn-00874dfc) · [`00874e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874d3c.md#insn-00874e2c)
- 新版 [`00874e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874e18) · [`00874e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874e3c) · [`00874e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874e6c)

~~~diff
- 00874dd8 ["COPY", "tmp:0:8", ["const:587:8"]]
- 00874dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874e18 ["COPY", "tmp:0:8", ["const:654:8"]]
+ 00874e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874dd8 bytes 081d1691
+ 00874e18 bytes 08511991
- 00874dfc ["INT_ADD", "register:40f0:8", ["const:874dfc:8", "const:4:8"]]
- 00874dfc ["CALL", null, ["callee:00597ecc:8"]]
+ 00874e3c ["INT_ADD", "register:40f0:8", ["const:874e3c:8", "const:4:8"]]
+ 00874e3c ["CALL", null, ["callee:00597ecc:8"]]
- 00874dfc bytes 248cf497
+ 00874e3c bytes 248cf497
- 00874e2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:530:8"]]
- 00874e2c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00874e2c ["COPY", "register:5010:8", ["const:0:8"]]
- 00874e2c ["COPY", "register:5018:8", ["const:0:8"]]
+ 00874e6c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:570:8"]]
+ 00874e6c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00874e6c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00874e6c ["COPY", "register:5018:8", ["const:0:8"]]
- 00874e2c bytes 204dc13d
+ 00874e6c bytes 205dc13d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240b097a00888c80b95bd8ca36e56e34"></a>

### [`00874f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f54.md) → [`00874f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md) FUN_00874f94

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
      "definition_site": "00874fa8",
      "incomplete_value": false,
      "site": "00874fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874f68",
      "incomplete_value": false,
      "site": "00874f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00874fac",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874fac",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f54.md#insn-00874f68) · [`00874f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f54.md#insn-00874f7c) · [`00874f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874f54.md#insn-00874f9c)
- 新版 [`00874fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fa8) · [`00874fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fbc) · [`00874fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fdc)

~~~diff
- 00874f68 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00874f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874fa8 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00874fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874f68 bytes 08012991
+ 00874fa8 bytes 08013991
- 00874f7c ["INT_ADD", "register:40f0:8", ["const:874f7c:8", "const:4:8"]]
- 00874f7c ["CALL", null, ["callee:00c53d00:8"]]
+ 00874fbc ["INT_ADD", "register:40f0:8", ["const:874fbc:8", "const:4:8"]]
+ 00874fbc ["CALL", null, ["callee:00c53d00:8"]]
- 00874f7c bytes 597a0f94
+ 00874fbc bytes 517b0f94
- 00874f9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00874f9c ["INT_ADD", "register:40f0:8", ["const:874f9c:8", "const:4:8"]]
- 00874f9c ["CALLIND", null, ["register:0:8"]]
+ 00874fdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874fdc ["INT_ADD", "register:40f0:8", ["const:874fdc:8", "const:4:8"]]
+ 00874fdc ["CALLIND", null, ["register:0:8"]]
- 00874f9c bytes 00013fd6
+ 00874fdc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-905c48a5940a814ece269a075a37de27"></a>

### [`00874fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874fb0.md) → [`00874ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md) FUN_00874ff0

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
      "definition_site": "00875008",
      "incomplete_value": false,
      "site": "0087500c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874fc8",
      "incomplete_value": false,
      "site": "00874fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "0087500c",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087500c",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874fb0.md#insn-00874fc8) · [`00874fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874fb0.md#insn-00874fdc) · [`00874ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00874/00874fb0.md#insn-00874ff0)
- 新版 [`00875008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-00875008) · [`0087501c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-0087501c) · [`00875030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-00875030)

~~~diff
- 00874fc8 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00874fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875008 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00875008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874fc8 bytes 08012991
+ 00875008 bytes 08013991
- 00874fdc ["INT_ADD", "register:40f0:8", ["const:874fdc:8", "const:4:8"]]
- 00874fdc ["CALL", null, ["callee:00c53d00:8"]]
+ 0087501c ["INT_ADD", "register:40f0:8", ["const:87501c:8", "const:4:8"]]
+ 0087501c ["CALL", null, ["callee:00c53d00:8"]]
- 00874fdc bytes 417a0f94
+ 0087501c bytes 397b0f94
- 00874ff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874ff0 ["INT_ADD", "register:40f0:8", ["const:874ff0:8", "const:4:8"]]
- 00874ff0 ["CALLIND", null, ["register:0:8"]]
+ 00875030 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875030 ["INT_ADD", "register:40f0:8", ["const:875030:8", "const:4:8"]]
+ 00875030 ["CALLIND", null, ["register:0:8"]]
- 00874ff0 bytes 00013fd6
+ 00875030 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-379190b4d168d216a69073d037cc7373"></a>

### [`0087500c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087500c.md) → [`0087504c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md) FUN_0087504c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875070",
      "incomplete_value": false,
      "site": "00875074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875030",
      "incomplete_value": false,
      "site": "00875034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00875074",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875074",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087500c.md#insn-00875020) · [`00875030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087500c.md#insn-00875030) · [`00875050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/0087500c.md#insn-00875050)
- 新版 [`00875060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875060) · [`00875070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875070) · [`00875090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875090)

~~~diff
- 00875020 ["INT_ADD", "register:40f0:8", ["const:875020:8", "const:4:8"]]
- 00875020 ["CALL", null, ["callee:00c57e90:8"]]
+ 00875060 ["INT_ADD", "register:40f0:8", ["const:875060:8", "const:4:8"]]
+ 00875060 ["CALL", null, ["callee:00c57e90:8"]]
- 00875020 bytes 9c8a0f94
+ 00875060 bytes 8c8b0f94
- 00875030 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00875030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875070 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00875070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875030 bytes 29012991
+ 00875070 bytes 29013991
- 00875050 ["INT_ADD", "register:40f0:8", ["const:875050:8", "const:4:8"]]
- 00875050 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875090 ["INT_ADD", "register:40f0:8", ["const:875090:8", "const:4:8"]]
+ 00875090 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875050 bytes 187a0f94
+ 00875090 bytes 107b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d90de292bdc0f8c1e8c52fc7a58ef75"></a>

### [`00875064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875064.md) → [`008750a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md) FUN_008750a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "008750ac",
      "incomplete_value": false,
      "site": "008750b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087506c",
      "incomplete_value": false,
      "site": "00875070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "008750b0",
      "DATA",
      [
        "storage",
        "00c7fa40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008750b0",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875064.md#insn-0087506c) · [`00875094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875064.md#insn-00875094)
- 新版 [`008750ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md#insn-008750ac) · [`008750d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md#insn-008750d4)

~~~diff
- 0087506c ["COPY", "tmp:0:8", ["const:a40:8"]]
- 0087506c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087506c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087506c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008750ac ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 008750ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008750ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008750ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087506c bytes 29012991
+ 008750ac bytes 29013991
- 00875094 ["INT_ADD", "register:40f0:8", ["const:875094:8", "const:4:8"]]
- 00875094 ["CALL", null, ["callee:00c53cd0:8"]]
+ 008750d4 ["INT_ADD", "register:40f0:8", ["const:8750d4:8", "const:4:8"]]
+ 008750d4 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875094 bytes 077a0f94
+ 008750d4 bytes ff7a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05c9640e6270234d29dd6e043fede900"></a>

### [`00875174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md) → [`008751b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md) FUN_008751b4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00875140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875140.md) · 呼出先 6件 [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00875180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875180.md) · 呼出先 6件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 69.35% / 新版 69.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00875208",
      "incomplete_value": true,
      "site": "00875210",
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
                "const:f70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008751c8",
      "incomplete_value": true,
      "site": "008751d0",
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
                "const:f30:8"
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
      "definition_site": "00875204",
      "incomplete_value": true,
      "site": "00875214",
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
                "const:63a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008751c4",
      "incomplete_value": true,
      "site": "008751d4",
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
                "const:56d:8"
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
      "definition_site": "00875204",
      "incomplete_value": true,
      "site": "00875214",
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
      "definition_site": "008751c4",
      "incomplete_value": true,
      "site": "008751d4",
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
      "00875204",
      "READ",
      [
        "storage",
        "002a356d",
        null,
        "string"
      ]
    ],
    [
      "00875204",
      "READ",
      [
        "storage",
        "002a357d",
        null,
        "string"
      ]
    ],
    [
      "00875208",
      "READ",
      [
        "storage",
        "002c2f30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00875204",
      "READ",
      [
        "storage",
        "002a363a",
        null,
        "string"
      ]
    ],
    [
      "00875204",
      "READ",
      [
        "storage",
        "002a364a",
        null,
        "string"
      ]
    ],
    [
      "00875208",
      "READ",
      [
        "storage",
        "002c2f70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md#insn-00875210) · [`00875214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md#insn-00875214) · [`008752dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875174.md#insn-008752dc)
- 新版 [`00875250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md#insn-00875250) · [`0087531c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md#insn-0087531c)

~~~diff
- 00875210 ["COPY", "tmp:0:8", ["const:fad:8"]]
- 00875210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875250 ["COPY", "tmp:0:8", ["const:fed:8"]]
+ 00875250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875210 bytes 08b53e91
+ 00875250 bytes 08b53f91
- 00875214 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00875214 bytes 69d2ffb0
- 008752dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:820:8"]]
- 008752dc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 008752dc ["COPY", "register:5010:8", ["const:0:8"]]
- 008752dc ["COPY", "register:5018:8", ["const:0:8"]]
+ 0087531c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:860:8"]]
+ 0087531c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0087531c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0087531c ["COPY", "register:5018:8", ["const:0:8"]]
- 008752dc bytes 0009c23d
+ 0087531c bytes 0019c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5ee42d4b291176ad4acaa1410c0829"></a>

### [`00875980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875980.md) → [`008759c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md) FUN_008759c0

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
      "definition_site": "008759e4",
      "incomplete_value": false,
      "site": "008759e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008759a4",
      "incomplete_value": false,
      "site": "008759a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "008759e4",
      "DATA",
      [
        "storage",
        "00c7fac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008759e4",
      "DATA",
      [
        "storage",
        "00c7fec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875980.md#insn-00875994) · [`008759a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875980.md#insn-008759a0)
- 新版 [`008759d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md#insn-008759d4) · [`008759e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md#insn-008759e0)

~~~diff
- 00875994 ["INT_ADD", "register:40f0:8", ["const:875994:8", "const:4:8"]]
- 00875994 ["CALL", null, ["callee:00c57e90:8"]]
+ 008759d4 ["INT_ADD", "register:40f0:8", ["const:8759d4:8", "const:4:8"]]
+ 008759d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00875994 bytes 3f880f94
+ 008759d4 bytes 2f890f94
- 008759a0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008759a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008759a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008759a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008759e0 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 008759e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008759e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008759e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008759a0 bytes 08012b91
+ 008759e0 bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1b4033c26ba0661900ea650f9c9af0"></a>

### [`008759b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008759b4.md) → [`008759f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759f4.md) FUN_008759f4

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
      "definition_site": "00875a00",
      "incomplete_value": false,
      "site": "00875a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008759c0",
      "incomplete_value": false,
      "site": "008759c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "00875a00",
      "DATA",
      [
        "storage",
        "00c7fac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a00",
      "DATA",
      [
        "storage",
        "00c7fec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008759bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/008759b4.md#insn-008759bc)
- 新版 [`008759fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759f4.md#insn-008759fc)

~~~diff
- 008759bc ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008759bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008759bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008759bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008759fc ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 008759fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008759fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008759fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008759bc bytes 29012b91
+ 008759fc bytes 29013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d9b01c4f16dfa2de2d118e1a6be63c3"></a>

### [`00875a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a18.md) → [`00875a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md) FUN_00875a58

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
      "definition_site": "00875a6c",
      "incomplete_value": false,
      "site": "00875a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875a2c",
      "incomplete_value": false,
      "site": "00875a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "00875a70",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a70",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a18.md#insn-00875a2c) · [`00875a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a18.md#insn-00875a40) · [`00875a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a18.md#insn-00875a60)
- 新版 [`00875a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875a6c) · [`00875a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875a80) · [`00875aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875aa0)

~~~diff
- 00875a2c ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00875a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875a6c ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00875a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875a2c bytes 08012d91
+ 00875a6c bytes 08013d91
- 00875a40 ["INT_ADD", "register:40f0:8", ["const:875a40:8", "const:4:8"]]
- 00875a40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875a80 ["INT_ADD", "register:40f0:8", ["const:875a80:8", "const:4:8"]]
+ 00875a80 ["CALL", null, ["callee:00c53d00:8"]]
- 00875a40 bytes a8770f94
+ 00875a80 bytes a0780f94
- 00875a60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875a60 ["INT_ADD", "register:40f0:8", ["const:875a60:8", "const:4:8"]]
- 00875a60 ["CALLIND", null, ["register:0:8"]]
+ 00875aa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875aa0 ["INT_ADD", "register:40f0:8", ["const:875aa0:8", "const:4:8"]]
+ 00875aa0 ["CALLIND", null, ["register:0:8"]]
- 00875a60 bytes 00013fd6
+ 00875aa0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50d2a8415b036b6982c185bfc094d07c"></a>

### [`00875a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a74.md) → [`00875ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md) FUN_00875ab4

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
      "definition_site": "00875acc",
      "incomplete_value": false,
      "site": "00875ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875a8c",
      "incomplete_value": false,
      "site": "00875a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "00875ad0",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875ad0",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a74.md#insn-00875a8c) · [`00875aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a74.md#insn-00875aa0) · [`00875ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875a74.md#insn-00875ab4)
- 新版 [`00875acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875acc) · [`00875ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875ae0) · [`00875af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875af4)

~~~diff
- 00875a8c ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00875a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875acc ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00875acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875a8c bytes 08012d91
+ 00875acc bytes 08013d91
- 00875aa0 ["INT_ADD", "register:40f0:8", ["const:875aa0:8", "const:4:8"]]
- 00875aa0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875ae0 ["INT_ADD", "register:40f0:8", ["const:875ae0:8", "const:4:8"]]
+ 00875ae0 ["CALL", null, ["callee:00c53d00:8"]]
- 00875aa0 bytes 90770f94
+ 00875ae0 bytes 88780f94
- 00875ab4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875ab4 ["INT_ADD", "register:40f0:8", ["const:875ab4:8", "const:4:8"]]
- 00875ab4 ["CALLIND", null, ["register:0:8"]]
+ 00875af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875af4 ["INT_ADD", "register:40f0:8", ["const:875af4:8", "const:4:8"]]
+ 00875af4 ["CALLIND", null, ["register:0:8"]]
- 00875ab4 bytes 00013fd6
+ 00875af4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b42b605c467e80ea9ef8e095d59d6f"></a>

### [`00875ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ad0.md) → [`00875b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md) FUN_00875b10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875b34",
      "incomplete_value": false,
      "site": "00875b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875af4",
      "incomplete_value": false,
      "site": "00875af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "00875b38",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b38",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ad0.md#insn-00875ae4) · [`00875af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ad0.md#insn-00875af4) · [`00875b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ad0.md#insn-00875b14)
- 新版 [`00875b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b24) · [`00875b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b34) · [`00875b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b54)

~~~diff
- 00875ae4 ["INT_ADD", "register:40f0:8", ["const:875ae4:8", "const:4:8"]]
- 00875ae4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00875b24 ["INT_ADD", "register:40f0:8", ["const:875b24:8", "const:4:8"]]
+ 00875b24 ["CALL", null, ["callee:00c57e90:8"]]
- 00875ae4 bytes eb870f94
+ 00875b24 bytes db880f94
- 00875af4 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00875af4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875af4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875af4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875b34 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00875b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875af4 bytes 29012d91
+ 00875b34 bytes 29013d91
- 00875b14 ["INT_ADD", "register:40f0:8", ["const:875b14:8", "const:4:8"]]
- 00875b14 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875b54 ["INT_ADD", "register:40f0:8", ["const:875b54:8", "const:4:8"]]
+ 00875b54 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875b14 bytes 67770f94
+ 00875b54 bytes 5f780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21154c708b6b7aeb2cb842c6195ed705"></a>

### [`00875b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b28.md) → [`00875b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md) FUN_00875b68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00875b70",
      "incomplete_value": false,
      "site": "00875b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875b30",
      "incomplete_value": false,
      "site": "00875b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "00875b74",
      "DATA",
      [
        "storage",
        "00c7fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b74",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b28.md#insn-00875b30) · [`00875b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875b28.md#insn-00875b58)
- 新版 [`00875b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md#insn-00875b70) · [`00875b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md#insn-00875b98)

~~~diff
- 00875b30 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00875b30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875b30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875b30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875b70 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00875b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875b30 bytes 29012d91
+ 00875b70 bytes 29013d91
- 00875b58 ["INT_ADD", "register:40f0:8", ["const:875b58:8", "const:4:8"]]
- 00875b58 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875b98 ["INT_ADD", "register:40f0:8", ["const:875b98:8", "const:4:8"]]
+ 00875b98 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875b58 bytes 56770f94
+ 00875b98 bytes 4e780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646b7657af52485fb26cd4d6df7b4683"></a>

### [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) → [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) FUN_00875c78

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c04.md) · 呼出先 6件 [`00875f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f78.md) [`00875fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00875c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c44.md) · 呼出先 6件 [`00875fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md) [`00876008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875d08",
      "incomplete_value": false,
      "site": "00875d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875cc8",
      "incomplete_value": false,
      "site": "00875cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "definition_site": "00875d24",
      "incomplete_value": false,
      "site": "00875d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875ce4",
      "incomplete_value": false,
      "site": "00875ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00875cb8",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "byte[15]"
      ]
    ],
    [
      "00875d08",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00875d24",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875cb8",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "qword"
      ]
    ],
    [
      "00875d08",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00875d24",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md#insn-00875c90) · [`00875cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md#insn-00875cb0) · [`00875cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md#insn-00875cb8)
- 新版 [`00875cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cd0) · [`00875cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cf0) · [`00875cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cf8)

~~~diff
- 00875c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875c90 ["INT_ADD", "register:40f0:8", ["const:875c90:8", "const:4:8"]]
- 00875c90 ["CALLIND", null, ["register:0:8"]]
+ 00875cd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875cd0 ["INT_ADD", "register:40f0:8", ["const:875cd0:8", "const:4:8"]]
+ 00875cd0 ["CALLIND", null, ["register:0:8"]]
- 00875c90 bytes 00013fd6
+ 00875cd0 bytes 00013fd6
- 00875cb0 ["INT_ADD", "register:40f0:8", ["const:875cb0:8", "const:4:8"]]
- 00875cb0 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875cf0 ["INT_ADD", "register:40f0:8", ["const:875cf0:8", "const:4:8"]]
+ 00875cf0 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875cb0 bytes 00770f94
+ 00875cf0 bytes f8770f94
- 00875cb8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00875cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875cf8 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00875cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875cb8 bytes 08c12e91
+ 00875cf8 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-825ac56f217d68223061af73092a1bd3"></a>

### [`00875e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e2c.md) → [`00875e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md) FUN_00875e6c

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
      "definition_site": "00875e80",
      "incomplete_value": false,
      "site": "00875e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875e40",
      "incomplete_value": false,
      "site": "00875e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00875e84",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875e84",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e2c.md#insn-00875e40) · [`00875e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e2c.md#insn-00875e54) · [`00875e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e2c.md#insn-00875e74)
- 新版 [`00875e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875e80) · [`00875e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875e94) · [`00875eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875eb4)

~~~diff
- 00875e40 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00875e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875e80 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00875e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875e40 bytes 08c12e91
+ 00875e80 bytes 08c13e91
- 00875e54 ["INT_ADD", "register:40f0:8", ["const:875e54:8", "const:4:8"]]
- 00875e54 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875e94 ["INT_ADD", "register:40f0:8", ["const:875e94:8", "const:4:8"]]
+ 00875e94 ["CALL", null, ["callee:00c53d00:8"]]
- 00875e54 bytes a3760f94
+ 00875e94 bytes 9b770f94
- 00875e74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875e74 ["INT_ADD", "register:40f0:8", ["const:875e74:8", "const:4:8"]]
- 00875e74 ["CALLIND", null, ["register:0:8"]]
+ 00875eb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875eb4 ["INT_ADD", "register:40f0:8", ["const:875eb4:8", "const:4:8"]]
+ 00875eb4 ["CALLIND", null, ["register:0:8"]]
- 00875e74 bytes 00013fd6
+ 00875eb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62b1c199e219bd976cf6267d2cd56467"></a>

### [`00875e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e88.md) → [`00875ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md) FUN_00875ec8

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
      "definition_site": "00875ee0",
      "incomplete_value": false,
      "site": "00875ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875ea0",
      "incomplete_value": false,
      "site": "00875ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00875ee4",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875ee4",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e88.md#insn-00875ea0) · [`00875eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e88.md#insn-00875eb4) · [`00875ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e88.md#insn-00875ec8)
- 新版 [`00875ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875ee0) · [`00875ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875ef4) · [`00875f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875f08)

~~~diff
- 00875ea0 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00875ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875ee0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00875ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875ea0 bytes 08c12e91
+ 00875ee0 bytes 08c13e91
- 00875eb4 ["INT_ADD", "register:40f0:8", ["const:875eb4:8", "const:4:8"]]
- 00875eb4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00875ef4 ["INT_ADD", "register:40f0:8", ["const:875ef4:8", "const:4:8"]]
+ 00875ef4 ["CALL", null, ["callee:00c53d00:8"]]
- 00875eb4 bytes 8b760f94
+ 00875ef4 bytes 83770f94
- 00875ec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875ec8 ["INT_ADD", "register:40f0:8", ["const:875ec8:8", "const:4:8"]]
- 00875ec8 ["CALLIND", null, ["register:0:8"]]
+ 00875f08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875f08 ["INT_ADD", "register:40f0:8", ["const:875f08:8", "const:4:8"]]
+ 00875f08 ["CALLIND", null, ["register:0:8"]]
- 00875ec8 bytes 00013fd6
+ 00875f08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06464e1a018d448af055ade4eb922bfd"></a>

### [`00875ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md) → [`00875f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md) FUN_00875f24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875f48",
      "incomplete_value": false,
      "site": "00875f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875f08",
      "incomplete_value": false,
      "site": "00875f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00875f4c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875f4c",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875ef8) · [`00875f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875f08) · [`00875f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875f28)
- 新版 [`00875f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f38) · [`00875f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f48) · [`00875f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f68)

~~~diff
- 00875ef8 ["INT_ADD", "register:40f0:8", ["const:875ef8:8", "const:4:8"]]
- 00875ef8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00875f38 ["INT_ADD", "register:40f0:8", ["const:875f38:8", "const:4:8"]]
+ 00875f38 ["CALL", null, ["callee:00c57e90:8"]]
- 00875ef8 bytes e6860f94
+ 00875f38 bytes d6870f94
- 00875f08 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00875f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875f48 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00875f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875f08 bytes 29c12e91
+ 00875f48 bytes 29c13e91
- 00875f28 ["INT_ADD", "register:40f0:8", ["const:875f28:8", "const:4:8"]]
- 00875f28 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875f68 ["INT_ADD", "register:40f0:8", ["const:875f68:8", "const:4:8"]]
+ 00875f68 ["CALL", null, ["callee:00c53cd0:8"]]
- 00875f28 bytes 62760f94
+ 00875f68 bytes 5a770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1344d38efc16c7ed01c95348dc591003"></a>

### [`00875f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f3c.md) → [`00875f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md) FUN_00875f7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "00875f84",
      "incomplete_value": false,
      "site": "00875f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875f44",
      "incomplete_value": false,
      "site": "00875f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
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
      "00875f88",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875f88",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f3c.md#insn-00875f44) · [`00875f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875f3c.md#insn-00875f6c)
- 新版 [`00875f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md#insn-00875f84) · [`00875fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md#insn-00875fac)

~~~diff
- 00875f44 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00875f44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875f44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875f44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875f84 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00875f84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875f44 bytes 29c12e91
+ 00875f84 bytes 29c13e91
- 00875f6c ["INT_ADD", "register:40f0:8", ["const:875f6c:8", "const:4:8"]]
- 00875f6c ["CALL", null, ["callee:00c53cd0:8"]]
+ 00875fac ["INT_ADD", "register:40f0:8", ["const:875fac:8", "const:4:8"]]
+ 00875fac ["CALL", null, ["callee:00c53cd0:8"]]
- 00875f6c bytes 51760f94
+ 00875fac bytes 49770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cc540beea0e3da8354be9a3b7803957"></a>

### [`008760a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760a0.md) → [`008760e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760e0.md) FUN_008760e0

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
      "definition_site": "008760e4",
      "incomplete_value": false,
      "site": "008760e8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008760a4",
      "incomplete_value": false,
      "site": "008760a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "008760e8",
      "DATA",
      [
        "storage",
        "00c7fc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008760e8",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008760a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760a0.md#insn-008760a0) · [`008760a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760a0.md#insn-008760a4)
- 新版 [`008760e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760e0.md#insn-008760e0) · [`008760e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760e0.md#insn-008760e4)

~~~diff
- 008760a0 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008760e0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008760a0 bytes 482000b0
+ 008760e0 bytes 482000d0
- 008760a4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 008760a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008760a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008760a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008760e4 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 008760e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008760e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008760e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008760a4 bytes 08013191
+ 008760e4 bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f491fc277e6f76874a67d1f56cb626d"></a>

### [`008760b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760b0.md) → [`008760f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md) FUN_008760f0

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
      "definition_site": "00876100",
      "incomplete_value": false,
      "site": "00876108",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008760c0",
      "incomplete_value": false,
      "site": "008760c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "00876108",
      "DATA",
      [
        "storage",
        "00c7fc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00876108",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008760bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760b0.md#insn-008760bc) · [`008760c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760b0.md#insn-008760c0) · [`008760cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760b0.md#insn-008760cc)
- 新版 [`008760fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md#insn-008760fc) · [`00876100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md#insn-00876100) · [`0087610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md#insn-0087610c)

~~~diff
- 008760bc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008760fc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008760bc bytes 482000b0
+ 008760fc bytes 482000d0
- 008760c0 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 008760c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008760c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008760c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876100 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00876100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008760c0 bytes 08013191
+ 00876100 bytes 08010191
- 008760cc ["INT_ADD", "register:40f0:8", ["const:8760cc:8", "const:4:8"]]
- 008760cc ["CALL", null, ["callee:00c57ea0:8"]]
+ 0087610c ["INT_ADD", "register:40f0:8", ["const:87610c:8", "const:4:8"]]
+ 0087610c ["CALL", null, ["callee:00c57ea0:8"]]
- 008760cc bytes 75860f94
+ 0087610c bytes 65870f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df61f14f97e2afdb93763cf03bd1612c"></a>

### [`008760f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md) → [`00876130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md) FUN_00876130

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876174",
      "incomplete_value": false,
      "site": "00876174",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876134",
      "incomplete_value": false,
      "site": "00876134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "definition_site": "008761dc",
      "incomplete_value": true,
      "site": "008761dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087619c",
      "incomplete_value": true,
      "site": "0087619c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:95a:8"
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
      "definition_site": "008761f4",
      "incomplete_value": true,
      "site": "008761f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008761b4",
      "incomplete_value": true,
      "site": "008761b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fec:8"
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
      "00876174",
      "DATA",
      [
        "storage",
        "00c7fc90",
        null,
        "undefined *"
      ]
    ],
    [
      "00876194",
      "PARAM",
      [
        "storage",
        "002ef71a",
        null,
        "string"
      ]
    ],
    [
      "008761a8",
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
      "00876174",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ],
    [
      "00876194",
      "PARAM",
      [
        "storage",
        "002ef75a",
        null,
        "string"
      ]
    ],
    [
      "008761a8",
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

- 旧版 [`0087615c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md#insn-0087615c) · [`008761d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md#insn-008761d8) · [`008761f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md#insn-008761f8)
- 新版 [`0087619c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-0087619c) · [`00876218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-00876218) · [`00876238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-00876238)

~~~diff
- 0087615c ["INT_ADD", "register:40f0:8", ["const:87615c:8", "const:4:8"]]
- 0087615c ["CALL", null, ["callee:00c58190:8"]]
+ 0087619c ["INT_ADD", "register:40f0:8", ["const:87619c:8", "const:4:8"]]
+ 0087619c ["CALL", null, ["callee:00c58190:8"]]
- 0087615c bytes 0d870f94
+ 0087619c bytes fd870f94
- 008761d8 ["INT_ADD", "register:40f0:8", ["const:8761d8:8", "const:4:8"]]
- 008761d8 ["CALL", null, ["callee:0047e60c:8"]]
+ 00876218 ["INT_ADD", "register:40f0:8", ["const:876218:8", "const:4:8"]]
+ 00876218 ["CALL", null, ["callee:0047e60c:8"]]
- 008761d8 bytes fd20f097
+ 00876218 bytes fd20f097
- 008761f8 ["INT_ADD", "register:40f0:8", ["const:8761f8:8", "const:4:8"]]
- 008761f8 ["CALL", null, ["callee:00c53d00:8"]]
+ 00876238 ["INT_ADD", "register:40f0:8", ["const:876238:8", "const:4:8"]]
+ 00876238 ["CALL", null, ["callee:00c53d00:8"]]
- 008761f8 bytes ba750f94
+ 00876238 bytes b2760f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df46ab60a44fcbe9b4b2a1e828fb196b"></a>

### [`008764ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md) → [`0087652c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md) FUN_0087652c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876544",
      "incomplete_value": false,
      "site": "00876548",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876504",
      "incomplete_value": false,
      "site": "00876508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00876548",
      "DATA",
      [
        "storage",
        "00c7fc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876548",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876500) · [`00876504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876504) · [`00876514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876514)
- 新版 [`00876540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-00876540) · [`00876544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-00876544) · [`00876554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-00876554)

~~~diff
- 00876500 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00876540 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00876500 bytes 492000b0
+ 00876540 bytes 492000d0
- 00876504 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00876504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876544 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00876544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876504 bytes 29413291
+ 00876544 bytes 29410291
- 00876514 ["INT_ADD", "register:40f0:8", ["const:876514:8", "const:4:8"]]
- 00876514 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00876554 ["INT_ADD", "register:40f0:8", ["const:876554:8", "const:4:8"]]
+ 00876554 ["CALL", null, ["callee:00c57eb0:8"]]
- 00876514 bytes 67850f94
+ 00876554 bytes 57860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147351479c095ee808404e7cdff32873"></a>

### [`00876598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md) → [`008765d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md) FUN_008765d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "008765f0",
      "incomplete_value": false,
      "site": "008765f4",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008765b0",
      "incomplete_value": false,
      "site": "008765b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "008765f4",
      "DATA",
      [
        "storage",
        "00c7fc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008765f4",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008765ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765ac) · [`008765b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765b0) · [`008765c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765c0)
- 新版 [`008765ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-008765ec) · [`008765f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-008765f0) · [`00876600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-00876600)

~~~diff
- 008765ac ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 008765ec ["COPY", "register:4048:8", ["const:c80000:8"]]
- 008765ac bytes 492000b0
+ 008765ec bytes 492000d0
- 008765b0 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 008765b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008765b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008765b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008765f0 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 008765f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008765f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008765f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008765b0 bytes 29413291
+ 008765f0 bytes 29410291
- 008765c0 ["INT_ADD", "register:40f0:8", ["const:8765c0:8", "const:4:8"]]
- 008765c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00876600 ["INT_ADD", "register:40f0:8", ["const:876600:8", "const:4:8"]]
+ 00876600 ["CALL", null, ["callee:00c57eb0:8"]]
- 008765c0 bytes 3c850f94
+ 00876600 bytes 2c860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-302ba5630d1f25eeb21a5c21bb3d290d"></a>

### [`00876664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md) → [`008766a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md) FUN_008766a4

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
      "definition_site": "008766c8",
      "incomplete_value": false,
      "site": "008766c8",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876688",
      "incomplete_value": false,
      "site": "00876688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
      "008766c8",
      "DATA",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008766c8",
      "DATA",
      [
        "storage",
        "00c800f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876678) · [`00876680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876680) · [`00876684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876684)
- 新版 [`008766b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md#insn-008766b8) · [`008766c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md#insn-008766c0) · [`008766c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md#insn-008766c4)

~~~diff
- 00876678 ["INT_ADD", "register:40f0:8", ["const:876678:8", "const:4:8"]]
- 00876678 ["CALL", null, ["callee:00c57e90:8"]]
+ 008766b8 ["INT_ADD", "register:40f0:8", ["const:8766b8:8", "const:4:8"]]
+ 008766b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00876678 bytes 06850f94
+ 008766b8 bytes f6850f94
- 00876680 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008766c0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00876680 bytes 482000b0
+ 008766c0 bytes 482000d0
- 00876684 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 00876684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00876684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00876684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008766c4 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 008766c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008766c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008766c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00876684 bytes 08c13391
+ 008766c4 bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d25a4b95f23d562dcc2a36184246d1a"></a>

### [`00876698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md) → [`008766d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766d8.md) FUN_008766d8

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
      "definition_site": "008766e4",
      "incomplete_value": false,
      "site": "008766e4",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008766a4",
      "incomplete_value": false,
      "site": "008766a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
      "008766e4",
      "DATA",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008766e4",
      "DATA",
      [
        "storage",
        "00c800f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md#insn-0087669c) · [`008766a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md#insn-008766a0)
- 新版 [`008766dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766d8.md#insn-008766dc) · [`008766e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766d8.md#insn-008766e0)

~~~diff
- 0087669c ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 008766dc ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0087669c bytes 492000b0
+ 008766dc bytes 492000d0
- 008766a0 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 008766a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008766a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008766a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008766e0 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 008766e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008766e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008766e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008766a0 bytes 29c13391
+ 008766e0 bytes 29c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513bd725e78e02b48c4fbb5fe8cefc10"></a>

### [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) → [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) FUN_008766f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) [`00873048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873048.md) [`00873058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md) [`008760e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760e0.md) [`008760f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004953d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md) [`00873088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873088.md) [`00873098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md) [`00876120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876120.md) [`00876130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008767a0",
      "incomplete_value": false,
      "site": "008767ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876760",
      "incomplete_value": false,
      "site": "0087676c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876818",
      "incomplete_value": false,
      "site": "00876824",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008767d8",
      "incomplete_value": false,
      "site": "008767e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "008767ac",
      "DATA",
      [
        "storage",
        "00c7f810",
        null,
        "pointer"
      ]
    ],
    [
      "008767f8",
      "READ",
      [
        "storage",
        "00c7f820",
        null,
        "undefined *"
      ]
    ],
    [
      "00876824",
      "DATA",
      [
        "storage",
        "00c7fc40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008767ac",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ],
    [
      "008767f8",
      "READ",
      [
        "storage",
        "00c7fc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00876824",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008766f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md#insn-008766f4) · [`00876714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md#insn-00876714) · [`0087671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md#insn-0087671c)
- 新版 [`00876734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-00876734) · [`00876754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-00876754) · [`0087675c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-0087675c)

~~~diff
- 008766f4 ["INT_ADD", "register:40f0:8", ["const:8766f4:8", "const:4:8"]]
- 008766f4 ["CALL", null, ["callee:008b9178:8"]]
+ 00876734 ["INT_ADD", "register:40f0:8", ["const:876734:8", "const:4:8"]]
+ 00876734 ["CALL", null, ["callee:008b9178:8"]]
- 008766f4 bytes 900a0194
+ 00876734 bytes 910a0194
- 00876714 ["INT_ADD", "register:40f0:8", ["const:876714:8", "const:4:8"]]
- 00876714 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00876754 ["INT_ADD", "register:40f0:8", ["const:876754:8", "const:4:8"]]
+ 00876754 ["CALL", null, ["callee:00c53cd0:8"]]
- 00876714 bytes 67740f94
+ 00876754 bytes 5f750f94
- 0087671c ["INT_ADD", "register:40f0:8", ["const:87671c:8", "const:4:8"]]
- 0087671c ["CALL", null, ["callee:004953d4:8"]]
+ 0087675c ["INT_ADD", "register:40f0:8", ["const:87675c:8", "const:4:8"]]
+ 0087675c ["CALL", null, ["callee:004953d4:8"]]
- 0087671c bytes 1e7bf097
+ 0087675c bytes 1e7bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ce57bbadfa1274bdd9392bebea0dea"></a>

### [`00876980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md) → [`008769c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md) FUN_008769c0

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
      "definition_site": "008769e4",
      "incomplete_value": false,
      "site": "008769e4",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008769a4",
      "incomplete_value": false,
      "site": "008769a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "008769e4",
      "DATA",
      [
        "storage",
        "00c7fd70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008769e4",
      "DATA",
      [
        "storage",
        "00c80170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-00876994) · [`0087699c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-0087699c) · [`008769a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-008769a0)
- 新版 [`008769d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md#insn-008769d4) · [`008769dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md#insn-008769dc) · [`008769e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md#insn-008769e0)

~~~diff
- 00876994 ["INT_ADD", "register:40f0:8", ["const:876994:8", "const:4:8"]]
- 00876994 ["CALL", null, ["callee:00c57e90:8"]]
+ 008769d4 ["INT_ADD", "register:40f0:8", ["const:8769d4:8", "const:4:8"]]
+ 008769d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00876994 bytes 3f840f94
+ 008769d4 bytes 2f850f94
- 0087699c ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008769dc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087699c bytes 482000b0
+ 008769dc bytes 482000d0
- 008769a0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 008769a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008769a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008769a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008769e0 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 008769e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008769e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008769e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008769a0 bytes 08c13591
+ 008769e0 bytes 08c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59925d6a19d1bcd5f080e6ec2bfe9f3b"></a>

### [`008769b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md) → [`008769f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769f4.md) FUN_008769f4

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
      "definition_site": "00876a00",
      "incomplete_value": false,
      "site": "00876a00",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008769c0",
      "incomplete_value": false,
      "site": "008769c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "00876a00",
      "DATA",
      [
        "storage",
        "00c7fd70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876a00",
      "DATA",
      [
        "storage",
        "00c80170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008769b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md#insn-008769b8) · [`008769bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md#insn-008769bc)
- 新版 [`008769f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769f4.md#insn-008769f8) · [`008769fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769f4.md#insn-008769fc)

~~~diff
- 008769b8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 008769f8 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 008769b8 bytes 492000b0
+ 008769f8 bytes 492000d0
- 008769bc ["COPY", "tmp:0:8", ["const:d70:8"]]
- 008769bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008769bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008769bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008769fc ["COPY", "tmp:0:8", ["const:170:8"]]
+ 008769fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008769fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008769fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008769bc bytes 29c13591
+ 008769fc bytes 29c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b871a37e5e9d201edde5ef0f716986"></a>

### [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) → [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) FUN_00876a10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md) [`0044f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md) [`0044f43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "site": "00876a58",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876a18",
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
      "site": "00876acc",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876a8c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00876a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00876acc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00876a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00876acc",
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

- 旧版 [`00876a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876a18) · [`00876a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876a8c) · [`00876acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876acc)
- 新版 [`00876a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876a58) · [`00876acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876acc) · [`00876b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876b0c)

~~~diff
- 00876a18 ["INT_ADD", "register:40f0:8", ["const:876a18:8", "const:4:8"]]
- 00876a18 ["CALL", null, ["ram:47acb4:8"]]
+ 00876a58 ["INT_ADD", "register:40f0:8", ["const:876a58:8", "const:4:8"]]
+ 00876a58 ["CALL", null, ["ram:47acf4:8"]]
- 00876a18 bytes a710f097
+ 00876a58 bytes a710f097
- 00876a8c ["INT_ADD", "register:40f0:8", ["const:876a8c:8", "const:4:8"]]
- 00876a8c ["CALL", null, ["ram:48ccb8:8"]]
+ 00876acc ["INT_ADD", "register:40f0:8", ["const:876acc:8", "const:4:8"]]
+ 00876acc ["CALL", null, ["ram:48ccf8:8"]]
- 00876a8c bytes 8b58f097
+ 00876acc bytes 8b58f097
- 00876acc ["INT_ADD", "register:40f0:8", ["const:876acc:8", "const:4:8"]]
- 00876acc ["CALL", null, ["callee:00c57eb0:8"]]
+ 00876b0c ["INT_ADD", "register:40f0:8", ["const:876b0c:8", "const:4:8"]]
+ 00876b0c ["CALL", null, ["callee:00c57eb0:8"]]
- 00876acc bytes f9830f94
+ 00876b0c bytes e9840f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d24c07a7fc4d17a0cf1a2572851331"></a>

### [`00876b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md) → [`00876b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md) _INIT_157

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
      "definition_site": "00876bb0",
      "incomplete_value": true,
      "site": "00876bcc",
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
      "definition_site": "00876b70",
      "incomplete_value": true,
      "site": "00876b8c",
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
      "definition_site": "00876bd4",
      "incomplete_value": true,
      "site": "00876bf0",
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
      "definition_site": "00876b94",
      "incomplete_value": true,
      "site": "00876bb0",
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
      "definition_site": "00876bf4",
      "incomplete_value": true,
      "site": "00876c10",
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
      "definition_site": "00876bb4",
      "incomplete_value": true,
      "site": "00876bd0",
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
      "00876bb0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00876bd4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00876bf4",
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
      "00876bb0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00876bd4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00876bf4",
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

- 旧版 [`00876bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876bac) · [`00876bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876bcc) · [`00876c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876c94)
- 新版 [`00876bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876bec) · [`00876c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876c0c) · [`00876cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876cd4)

~~~diff
- 00876bac ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00876bac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00876bac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00876bac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00876bec ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00876bec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00876bec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00876bec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00876bac bytes 4a093691
+ 00876bec bytes 4a093791
- 00876bcc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00876bcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00876bcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00876bcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00876c0c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00876c0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00876c0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00876c0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00876bcc bytes 4a553a91
+ 00876c0c bytes 4a893d91
- 00876c94 ["INT_ADD", "register:40f0:8", ["const:876c94:8", "const:4:8"]]
- 00876c94 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00876cd4 ["INT_ADD", "register:40f0:8", ["const:876cd4:8", "const:4:8"]]
+ 00876cd4 ["CALL", null, ["callee:0043b7f8:8"]]
- 00876c94 bytes c912ef97
+ 00876cd4 bytes c912ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d9a496c4fca3e889809dc1ad17fa319"></a>

### [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) → [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) FUN_00876f04

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) · 呼出先 26件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)
- 新版 呼出元 1件 [`00872a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md) · 呼出先 26件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.20% / 新版 91.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件, `store_destination` 2件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00876f80",
      "incomplete_value": true,
      "site": "00876f90",
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
                "const:889:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876f40",
      "incomplete_value": true,
      "site": "00876f50",
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
                "const:849:8"
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
      "definition_site": "00876f84",
      "incomplete_value": true,
      "site": "00876f94",
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
      "definition_site": "00876f44",
      "incomplete_value": true,
      "site": "00876f54",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00876f88",
      "incomplete_value": true,
      "site": "00876f98",
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
      "definition_site": "00876f48",
      "incomplete_value": true,
      "site": "00876f58",
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
      "00876f64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00876f80",
      "READ",
      [
        "storage",
        "002b7849",
        null,
        "string"
      ]
    ],
    [
      "00876f84",
      "READ",
      [
        "storage",
        "002b7858",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00876f64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00876f80",
      "READ",
      [
        "storage",
        "002b7889",
        null,
        "string"
      ]
    ],
    [
      "00876f84",
      "READ",
      [
        "storage",
        "002b7898",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md#insn-00876f10) · [`00876f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md#insn-00876f24) · [`00876f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md#insn-00876f48)
- 新版 [`00876f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-00876f50) · [`00876f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-00876f64) · [`00876f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-00876f88)

~~~diff
- 00876f10 ["INT_ADD", "register:40f0:8", ["const:876f10:8", "const:4:8"]]
- 00876f10 ["CALL", null, ["callee:008514f8:8"]]
+ 00876f50 ["INT_ADD", "register:40f0:8", ["const:876f50:8", "const:4:8"]]
+ 00876f50 ["CALL", null, ["callee:008514f8:8"]]
- 00876f10 bytes 6a69ff97
+ 00876f50 bytes 6a69ff97
- 00876f24 ["INT_ADD", "register:40f0:8", ["const:876f24:8", "const:4:8"]]
- 00876f24 ["CALL", null, ["ram:48ccb8:8"]]
+ 00876f64 ["INT_ADD", "register:40f0:8", ["const:876f64:8", "const:4:8"]]
+ 00876f64 ["CALL", null, ["ram:48ccf8:8"]]
- 00876f24 bytes 6557f097
+ 00876f64 bytes 6557f097
- 00876f48 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9c0:8"]]
- 00876f48 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 00876f48 ["COPY", "register:5050:8", ["const:0:8"]]
- 00876f48 ["COPY", "register:5058:8", ["const:0:8"]]
+ 00876f88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a00:8"]]
+ 00876f88 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 00876f88 ["COPY", "register:5050:8", ["const:0:8"]]
+ 00876f88 ["COPY", "register:5058:8", ["const:0:8"]]
- 00876f48 bytes 2271c23d
+ 00876f88 bytes 2281c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5bb02be4174dfd8ca0501bd6868ff23"></a>

### [`00877a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md) → [`00877a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md) FUN_00877a70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`00877d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`00877d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

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
      "definition_site": "00877b28",
      "incomplete_value": false,
      "site": "00877b34",
      "value": [
        "leaf",
        "const:877d50:8"
      ]
    },
    "old": {
      "definition_site": "00877ae8",
      "incomplete_value": false,
      "site": "00877af4",
      "value": [
        "leaf",
        "const:877d10:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00877bcc",
      "incomplete_value": false,
      "site": "00877bd0",
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
            "const:f27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00877b8c",
      "incomplete_value": false,
      "site": "00877b90",
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
            "const:e5a:8"
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
      "00877b28",
      "PARAM",
      [
        "storage",
        "00877d10",
        null,
        null
      ]
    ],
    [
      "00877bcc",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00877b28",
      "PARAM",
      [
        "storage",
        "00877d50",
        null,
        null
      ]
    ],
    [
      "00877bcc",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md#insn-00877ab4) · [`00877af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md#insn-00877af4) · [`00877b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md#insn-00877b50)
- 新版 [`00877af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877af4) · [`00877b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877b34) · [`00877b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877b90)

~~~diff
- 00877ab4 ["INT_ADD", "register:40f0:8", ["const:877ab4:8", "const:4:8"]]
- 00877ab4 ["CALL", null, ["callee:00c58170:8"]]
+ 00877af4 ["INT_ADD", "register:40f0:8", ["const:877af4:8", "const:4:8"]]
+ 00877af4 ["CALL", null, ["callee:00c58170:8"]]
- 00877ab4 bytes af800f94
+ 00877af4 bytes 9f810f94
- 00877af4 ["INT_ADD", "register:40f0:8", ["const:877af4:8", "const:4:8"]]
- 00877af4 ["CALL", null, ["callee:00c58110:8"]]
+ 00877b34 ["INT_ADD", "register:40f0:8", ["const:877b34:8", "const:4:8"]]
+ 00877b34 ["CALL", null, ["callee:00c58110:8"]]
- 00877af4 bytes 87800f94
+ 00877b34 bytes 77810f94
- 00877b50 ["INT_ADD", "register:40f0:8", ["const:877b50:8", "const:4:8"]]
- 00877b50 ["CALL", null, ["callee:008514f8:8"]]
+ 00877b90 ["INT_ADD", "register:40f0:8", ["const:877b90:8", "const:4:8"]]
+ 00877b90 ["CALL", null, ["callee:008514f8:8"]]
- 00877b50 bytes 5a66ff97
+ 00877b90 bytes 5a66ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41fc15f033847ef9911251b896d38d86"></a>

### [`00877e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e58.md) → [`00877e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md) _INIT_158

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
      "definition_site": "00877ed4",
      "incomplete_value": true,
      "site": "00877ef0",
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
      "definition_site": "00877e94",
      "incomplete_value": true,
      "site": "00877eb0",
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
      "definition_site": "00877ef8",
      "incomplete_value": true,
      "site": "00877f14",
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
      "definition_site": "00877eb8",
      "incomplete_value": true,
      "site": "00877ed4",
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
      "definition_site": "00877f18",
      "incomplete_value": true,
      "site": "00877f34",
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
      "definition_site": "00877ed8",
      "incomplete_value": true,
      "site": "00877ef4",
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
      "00877ed4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00877ef8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00877f18",
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
      "00877ed4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00877ef8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00877f18",
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

- 旧版 [`00877ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e58.md#insn-00877ed0) · [`00877ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e58.md#insn-00877ef0) · [`0087808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e58.md#insn-0087808c)
- 新版 [`00877f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-00877f10) · [`00877f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-00877f30) · [`008780cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-008780cc)

~~~diff
- 00877ed0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00877ed0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00877ed0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00877ed0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00877f10 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00877f10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00877f10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00877f10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00877ed0 bytes 4a093691
+ 00877f10 bytes 4a093791
- 00877ef0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00877ef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00877ef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00877ef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00877f30 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00877f30 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00877f30 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00877f30 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00877ef0 bytes 4a553a91
+ 00877f30 bytes 4a893d91
- 0087808c ["INT_ADD", "register:40f0:8", ["const:87808c:8", "const:4:8"]]
- 0087808c ["CALL", null, ["callee:00c57e30:8"]]
+ 008780cc ["INT_ADD", "register:40f0:8", ["const:8780cc:8", "const:4:8"]]
+ 008780cc ["CALL", null, ["callee:00c57e30:8"]]
- 0087808c bytes 697e0f94
+ 008780cc bytes 597f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e95bf209429fd2f0b2e13afdb1c95c9"></a>

### [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) → [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) FUN_008783f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 19件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006eec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006eec6c.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 6件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)
- 新版 呼出元 19件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006eecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006eecac.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`0070d3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070d3b8.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 6件 [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008784b0",
      "incomplete_value": false,
      "site": "008784b0",
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
            "const:27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878470",
      "incomplete_value": false,
      "site": "00878470",
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
            "const:fe7:8"
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
      "definition_site": "00878520",
      "incomplete_value": false,
      "site": "00878520",
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
            "const:223:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008784e0",
      "incomplete_value": false,
      "site": "008784e0",
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
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878590",
      "incomplete_value": false,
      "site": "00878590",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878550",
      "incomplete_value": false,
      "site": "00878550",
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
            "const:16a:8"
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
      "008784b0",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "008784f8",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "unmatched:008784c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a830"
      ]
    ]
  ],
  "added": [
    [
      "008784b0",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "008784f8",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878508",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a830"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md#insn-00878488) · [`008784c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md#insn-008784c8) · [`008784d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md#insn-008784d0)
- 新版 [`008784c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md#insn-008784c8) · [`00878510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md#insn-00878510)

~~~diff
- 00878488 ["INT_ADD", "register:40f0:8", ["const:878488:8", "const:4:8"]]
- 00878488 ["CALL", null, ["callee:00c5a830:8"]]
+ 008784c8 ["INT_ADD", "register:40f0:8", ["const:8784c8:8", "const:4:8"]]
+ 008784c8 ["CALL", null, ["callee:00c5a830:8"]]
- 00878488 bytes ea870f94
+ 008784c8 bytes da880f94
- 008784c8 ["INT_ADD", "register:40f0:8", ["const:8784c8:8", "const:4:8"]]
- 008784c8 ["CALL", null, ["callee:00c5a830:8"]]
- 008784c8 bytes da870f94
- 008784d0 ["INT_ADD", "register:40f0:8", ["const:8784d0:8", "const:4:8"]]
- 008784d0 ["CALL", null, ["ram:71be98:8"]]
+ 00878510 ["INT_ADD", "register:40f0:8", ["const:878510:8", "const:4:8"]]
+ 00878510 ["CALL", null, ["ram:71bed8:8"]]
- 008784d0 bytes 728efa97
+ 00878510 bytes 728efa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3683e707fa8112a58b6fc412adae54ee"></a>

### [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) → [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) FUN_00878758

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) [`00878bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md) [`00878e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878e98.md) [`00878eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878eb0.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md)
- 新版 呼出元 5件 [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) [`00878bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md) [`00878ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878ed8.md) [`00878ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878ef0.md) [`0087929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/0087929c.md) · 呼出先 11件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`00b3c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c8dc.md)

変更の種類 call, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008787f0",
      "incomplete_value": false,
      "site": "008787f0",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008787b0",
      "incomplete_value": false,
      "site": "008787b0",
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
            "const:fc0:8"
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
      "definition_site": "00878858",
      "incomplete_value": false,
      "site": "00878858",
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
            "const:723:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878818",
      "incomplete_value": false,
      "site": "00878818",
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
            "const:6e3:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00878878"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008787f0",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878814",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878844",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "008787f0",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "00878814",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "00878844",
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

- 旧版 [`008787c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md#insn-008787c4) · [`008787d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md#insn-008787d8) · [`008787f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md#insn-008787f0)
- 新版 [`00878804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-00878804) · [`00878818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-00878818) · [`00878830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-00878830)

~~~diff
- 008787c4 ["INT_ADD", "register:40f0:8", ["const:8787c4:8", "const:4:8"]]
- 008787c4 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 00878804 ["INT_ADD", "register:40f0:8", ["const:878804:8", "const:4:8"]]
+ 00878804 ["CALL", null, ["callee:00c5a8f0:8"]]
- 008787c4 bytes 4b870f94
+ 00878804 bytes 3b880f94
- 008787d8 ["INT_ADD", "register:40f0:8", ["const:8787d8:8", "const:4:8"]]
- 008787d8 ["CALL", null, ["callee:00c5a840:8"]]
+ 00878818 ["INT_ADD", "register:40f0:8", ["const:878818:8", "const:4:8"]]
+ 00878818 ["CALL", null, ["callee:00c5a840:8"]]
- 008787d8 bytes 1a870f94
+ 00878818 bytes 0a880f94
- 008787f0 ["INT_ADD", "register:40f0:8", ["const:8787f0:8", "const:4:8"]]
- 008787f0 ["CALL", null, ["callee:00c5a830:8"]]
+ 00878830 ["INT_ADD", "register:40f0:8", ["const:878830:8", "const:4:8"]]
+ 00878830 ["CALL", null, ["callee:00c5a830:8"]]
- 008787f0 bytes 10870f94
+ 00878830 bytes 00880f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2881a99ec2da85727b545942c177a6ef"></a>

### [`00878bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md) → [`00878bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md) FUN_00878bec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`00696de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696de4.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 6件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)
- 新版 呼出元 5件 [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 6件 [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878c9c",
      "incomplete_value": false,
      "site": "00878c9c",
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
            "const:27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878c5c",
      "incomplete_value": false,
      "site": "00878c5c",
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
            "const:fe7:8"
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
      "definition_site": "00878d10",
      "incomplete_value": false,
      "site": "00878d10",
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
            "const:223:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878cd0",
      "incomplete_value": false,
      "site": "00878cd0",
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
            "const:156:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878d80",
      "incomplete_value": false,
      "site": "00878d80",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878d40",
      "incomplete_value": false,
      "site": "00878d40",
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
            "const:16a:8"
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
      "00878c9c",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "00878ce4",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "00878cfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "00878c9c",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878ce4",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878cfc",
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

- 旧版 [`00878c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878c90) · [`00878cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878cbc) · [`00878cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878cfc)
- 新版 [`00878cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878cd0) · [`00878cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878cfc) · [`00878d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878d3c)

~~~diff
- 00878c90 ["INT_ADD", "register:40f0:8", ["const:878c90:8", "const:4:8"]]
- 00878c90 ["CALL", null, ["callee:00c5a830:8"]]
+ 00878cd0 ["INT_ADD", "register:40f0:8", ["const:878cd0:8", "const:4:8"]]
+ 00878cd0 ["CALL", null, ["callee:00c5a830:8"]]
- 00878c90 bytes e8850f94
+ 00878cd0 bytes d8860f94
- 00878cbc ["INT_ADD", "register:40f0:8", ["const:878cbc:8", "const:4:8"]]
- 00878cbc ["CALL", null, ["ram:71be98:8"]]
+ 00878cfc ["INT_ADD", "register:40f0:8", ["const:878cfc:8", "const:4:8"]]
+ 00878cfc ["CALL", null, ["ram:71bed8:8"]]
- 00878cbc bytes 778cfa97
+ 00878cfc bytes 778cfa97
- 00878cfc ["INT_ADD", "register:40f0:8", ["const:878cfc:8", "const:4:8"]]
- 00878cfc ["CALL", null, ["callee:00c5a840:8"]]
+ 00878d3c ["INT_ADD", "register:40f0:8", ["const:878d3c:8", "const:4:8"]]
+ 00878d3c ["CALL", null, ["callee:00c5a840:8"]]
- 00878cfc bytes d1850f94
+ 00878d3c bytes c1860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ff30aefc12bd77aac8c5b3231f54b7"></a>

### [`00878ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md) → [`00878f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md) FUN_00878f08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md)
- 新版 呼出元 1件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 11件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`00b3c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c8dc.md)

変更の種類 call, call_argument_candidate, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878f90",
      "incomplete_value": false,
      "site": "00878f90",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878f50",
      "incomplete_value": false,
      "site": "00878f50",
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
            "const:fc0:8"
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
      "definition_site": "00878ff8",
      "incomplete_value": false,
      "site": "00878ff8",
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
            "const:723:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878fb8",
      "incomplete_value": false,
      "site": "00878fb8",
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
            "const:6e3:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879018"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878f90",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878fb4",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878fe4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "00878f90",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "00878fb4",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "00878fe4",
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

- 旧版 [`00878f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md#insn-00878f64) · [`00878f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md#insn-00878f78) · [`00878f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md#insn-00878f90)
- 新版 [`00878fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00878fa4) · [`00878fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00878fb8) · [`00878fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00878fd0)

~~~diff
- 00878f64 ["INT_ADD", "register:40f0:8", ["const:878f64:8", "const:4:8"]]
- 00878f64 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 00878fa4 ["INT_ADD", "register:40f0:8", ["const:878fa4:8", "const:4:8"]]
+ 00878fa4 ["CALL", null, ["callee:00c5a8f0:8"]]
- 00878f64 bytes 63850f94
+ 00878fa4 bytes 53860f94
- 00878f78 ["INT_ADD", "register:40f0:8", ["const:878f78:8", "const:4:8"]]
- 00878f78 ["CALL", null, ["callee:00c5a840:8"]]
+ 00878fb8 ["INT_ADD", "register:40f0:8", ["const:878fb8:8", "const:4:8"]]
+ 00878fb8 ["CALL", null, ["callee:00c5a840:8"]]
- 00878f78 bytes 32850f94
+ 00878fb8 bytes 22860f94
- 00878f90 ["INT_ADD", "register:40f0:8", ["const:878f90:8", "const:4:8"]]
- 00878f90 ["CALL", null, ["callee:00c5a830:8"]]
+ 00878fd0 ["INT_ADD", "register:40f0:8", ["const:878fd0:8", "const:4:8"]]
+ 00878fd0 ["CALL", null, ["callee:00c5a830:8"]]
- 00878f90 bytes 28850f94
+ 00878fd0 bytes 18860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03a934313bcb4bf5307203763f9d1adf"></a>

### [`00879274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879274.md) → [`008792b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md) _INIT_159

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879314",
      "incomplete_value": true,
      "site": "00879330",
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
      "definition_site": "008792d4",
      "incomplete_value": true,
      "site": "008792f0",
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
      "definition_site": "00879334",
      "incomplete_value": true,
      "site": "00879350",
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
      "definition_site": "008792f4",
      "incomplete_value": true,
      "site": "00879310",
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
      "definition_site": "00879354",
      "incomplete_value": true,
      "site": "0087936c",
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
      "definition_site": "00879314",
      "incomplete_value": true,
      "site": "0087932c",
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
      "008792f0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00879314",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00879334",
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
      "008792f0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00879314",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00879334",
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

- 旧版 [`008792ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879274.md#insn-008792ec) · [`0087930c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879274.md#insn-0087930c) · [`008794a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879274.md#insn-008794a8)
- 新版 [`0087932c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-0087932c) · [`0087934c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-0087934c) · [`008794e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-008794e8)

~~~diff
- 008792ec ["COPY", "tmp:0:8", ["const:d82:8"]]
- 008792ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008792ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008792ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087932c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0087932c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087932c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087932c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008792ec bytes 4a093691
+ 0087932c bytes 4a093791
- 0087930c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0087930c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087930c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087930c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087934c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0087934c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087934c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087934c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087930c bytes 4a553a91
+ 0087934c bytes 4a893d91
- 008794a8 ["INT_ADD", "register:40f0:8", ["const:8794a8:8", "const:4:8"]]
- 008794a8 ["CALL", null, ["callee:00c57e30:8"]]
+ 008794e8 ["INT_ADD", "register:40f0:8", ["const:8794e8:8", "const:4:8"]]
+ 008794e8 ["CALL", null, ["callee:00c57e30:8"]]
- 008794a8 bytes 62790f94
+ 008794e8 bytes 527a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4027bf31f64bf6e7ce39f0f816ce6e68"></a>

### [`00879604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md) → [`00879644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md) FUN_00879644

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087bc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0087bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008796d0",
      "incomplete_value": false,
      "site": "008796d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879690",
      "incomplete_value": false,
      "site": "00879698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "00879680",
      "PARAM",
      [
        "storage",
        "011231f8",
        null,
        "undefined2"
      ]
    ],
    [
      "008796d0",
      "PARAM",
      [
        "storage",
        "011231e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879680",
      "PARAM",
      [
        "storage",
        "011235f8",
        null,
        "undefined2"
      ]
    ],
    [
      "008796d0",
      "PARAM",
      [
        "storage",
        "011235e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md#insn-00879698) · [`00879640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md#insn-00879640) · [`0087964c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md#insn-0087964c)
- 新版 [`008796d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-008796d8) · [`00879680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-00879680) · [`0087968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-0087968c)

~~~diff
- 00879698 ["INT_ADD", "register:40f0:8", ["const:879698:8", "const:4:8"]]
- 00879698 ["CALL", null, ["callee:00493998:8"]]
+ 008796d8 ["INT_ADD", "register:40f0:8", ["const:8796d8:8", "const:4:8"]]
+ 008796d8 ["CALL", null, ["callee:00493998:8"]]
- 00879698 bytes b068f097
+ 008796d8 bytes b068f097
- 00879640 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00879640 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00879640 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00879640 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00879680 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00879680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00879680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00879680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00879640 bytes 21e00791
+ 00879680 bytes 21e01791
- 0087964c ["INT_ADD", "register:40f0:8", ["const:87964c:8", "const:4:8"]]
- 0087964c ["CALL", null, ["callee:005626f4:8"]]
+ 0087968c ["INT_ADD", "register:40f0:8", ["const:87968c:8", "const:4:8"]]
+ 0087968c ["CALL", null, ["callee:005626f4:8"]]
- 0087964c bytes 1aa4f397
+ 0087968c bytes 1aa4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe8b078cee02433e4bab5affe8bee12"></a>

### [`00879774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879774.md) → [`008797b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md) _INIT_160

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.24% / 新版 75.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008797f0",
      "incomplete_value": true,
      "site": "0087980c",
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
      "definition_site": "008797b0",
      "incomplete_value": true,
      "site": "008797cc",
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
      "definition_site": "00879814",
      "incomplete_value": true,
      "site": "00879830",
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
      "definition_site": "008797d4",
      "incomplete_value": true,
      "site": "008797f0",
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
      "definition_site": "00879834",
      "incomplete_value": true,
      "site": "00879850",
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
      "definition_site": "008797f4",
      "incomplete_value": true,
      "site": "00879810",
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
      "008797f0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00879814",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00879834",
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
      "008797f0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00879814",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00879834",
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

- 旧版 [`008797ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879774.md#insn-008797ec) · [`0087980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879774.md#insn-0087980c) · [`008798d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879774.md#insn-008798d4)
- 新版 [`0087982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-0087982c) · [`0087984c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-0087984c) · [`00879914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-00879914)

~~~diff
- 008797ec ["COPY", "tmp:0:8", ["const:d82:8"]]
- 008797ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008797ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008797ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087982c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0087982c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087982c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087982c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008797ec bytes 4a093691
+ 0087982c bytes 4a093791
- 0087980c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0087980c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087980c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087980c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087984c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0087984c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087984c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087984c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087980c bytes 4a553a91
+ 0087984c bytes 4a893d91
- 008798d4 ["INT_ADD", "register:40f0:8", ["const:8798d4:8", "const:4:8"]]
- 008798d4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00879914 ["INT_ADD", "register:40f0:8", ["const:879914:8", "const:4:8"]]
+ 00879914 ["CALL", null, ["callee:0043b7f8:8"]]
- 008798d4 bytes b907ef97
+ 00879914 bytes b907ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf1d4ae3590b8f0c6bfa2364b64457d"></a>

### [`00879d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md) → [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) FUN_00879d88

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1890.md) · 呼出先 10件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0087a2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a2c8.md) [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`0087bb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bb84.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`0087bbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.44% / 新版 95.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879e10",
      "incomplete_value": true,
      "site": "00879e1c",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879dd0",
      "incomplete_value": true,
      "site": "00879ddc",
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
                "const:20:8"
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
      "definition_site": "00879e0c",
      "incomplete_value": true,
      "site": "00879e20",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:c6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879dcc",
      "incomplete_value": true,
      "site": "00879de0",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:b8f:8"
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
      "definition_site": "00879e0c",
      "incomplete_value": true,
      "site": "00879e20",
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
      "definition_site": "00879dcc",
      "incomplete_value": true,
      "site": "00879de0",
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
      "00879e0c",
      "READ",
      [
        "storage",
        "002a6b8f",
        null,
        null
      ]
    ],
    [
      "00879e0c",
      "READ",
      [
        "storage",
        "002a6b9f",
        null,
        null
      ]
    ],
    [
      "00879e10",
      "READ",
      [
        "storage",
        "002a6baf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879e0c",
      "READ",
      [
        "storage",
        "002a6c6b",
        null,
        null
      ]
    ],
    [
      "00879e0c",
      "READ",
      [
        "storage",
        "002a6c7b",
        null,
        null
      ]
    ],
    [
      "00879e10",
      "READ",
      [
        "storage",
        "002a6c8b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md#insn-00879dbc) · [`00879dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md#insn-00879dac) · [`00879dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879d48.md#insn-00879dc4)
- 新版 [`00879dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879dfc) · [`00879dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879dec) · [`00879e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879e04)

~~~diff
- 00879dbc ["INT_ADD", "register:40f0:8", ["const:879dbc:8", "const:4:8"]]
- 00879dbc ["CALL", null, ["callee:00c57e90:8"]]
+ 00879dfc ["INT_ADD", "register:40f0:8", ["const:879dfc:8", "const:4:8"]]
+ 00879dfc ["CALL", null, ["callee:00c57e90:8"]]
- 00879dbc bytes 35770f94
+ 00879dfc bytes 25780f94
- 00879dac ["COPY", "register:0:8", ["register:4040:8"]]
- 00879dac ["INT_ADD", "register:40f0:8", ["const:879dac:8", "const:4:8"]]
- 00879dac ["CALLIND", null, ["register:0:8"]]
+ 00879dec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00879dec ["INT_ADD", "register:40f0:8", ["const:879dec:8", "const:4:8"]]
+ 00879dec ["CALLIND", null, ["register:0:8"]]
- 00879dac bytes 00013fd6
+ 00879dec bytes 00013fd6
- 00879dc4 ["COPY", "tmp:0:8", ["const:b8f:8"]]
- 00879dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879e04 ["COPY", "tmp:0:8", ["const:c6b:8"]]
+ 00879e04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879e04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879e04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879dc4 bytes 293d2e91
+ 00879e04 bytes 29ad3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-838d1d0aeee3b4d68cb34598fce2b8bc"></a>

### [`0087a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md) → [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) FUN_0087aa10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a708.md) [`00b34a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34a7c.md) · 呼出先 7件 [`0087b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md) [`0087bf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bf60.md) [`0087c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c138.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`00b34ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34ea4.md) · 呼出先 7件 [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) [`0087bfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa0.md) [`0087c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c178.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087aad8",
      "incomplete_value": false,
      "site": "0087aad8",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aa98",
      "incomplete_value": false,
      "site": "0087aa98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "definition_site": "0087aa78",
      "incomplete_value": false,
      "site": "0087aa90",
      "value": [
        "leaf",
        "const:87bfa0:8"
      ]
    },
    "old": {
      "definition_site": "0087aa38",
      "incomplete_value": false,
      "site": "0087aa50",
      "value": [
        "leaf",
        "const:87bf60:8"
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
      "0087aa78",
      "PARAM",
      [
        "storage",
        "0087bf60",
        null,
        null
      ]
    ],
    [
      "0087aad8",
      "DATA",
      [
        "storage",
        "00c7ff88",
        null,
        "undefined *"
      ]
    ],
    [
      "0087ab58",
      "READ",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aa78",
      "PARAM",
      [
        "storage",
        "0087bfa0",
        null,
        null
      ]
    ],
    [
      "0087aad8",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ],
    [
      "0087ab58",
      "READ",
      [
        "storage",
        "00c803b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md#insn-0087aa10) · [`0087aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md#insn-0087aa50) · [`0087aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a9d0.md#insn-0087aa58)
- 新版 [`0087aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087aa50) · [`0087aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087aa90) · [`0087aa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087aa98)

~~~diff
- 0087aa10 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aa10 ["INT_ADD", "register:40f0:8", ["const:87aa10:8", "const:4:8"]]
- 0087aa10 ["CALLIND", null, ["register:0:8"]]
+ 0087aa50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087aa50 ["INT_ADD", "register:40f0:8", ["const:87aa50:8", "const:4:8"]]
+ 0087aa50 ["CALLIND", null, ["register:0:8"]]
- 0087aa10 bytes 20013fd6
+ 0087aa50 bytes 20013fd6
- 0087aa50 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aa50 ["INT_ADD", "register:40f0:8", ["const:87aa50:8", "const:4:8"]]
- 0087aa50 ["CALLIND", null, ["register:0:8"]]
+ 0087aa90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087aa90 ["INT_ADD", "register:40f0:8", ["const:87aa90:8", "const:4:8"]]
+ 0087aa90 ["CALLIND", null, ["register:0:8"]]
- 0087aa50 bytes 20013fd6
+ 0087aa90 bytes 20013fd6
- 0087aa58 ["INT_ADD", "register:40f0:8", ["const:87aa58:8", "const:4:8"]]
- 0087aa58 ["CALL", null, ["callee:00c5aa10:8"]]
+ 0087aa98 ["INT_ADD", "register:40f0:8", ["const:87aa98:8", "const:4:8"]]
+ 0087aa98 ["CALL", null, ["callee:00c5aa10:8"]]
- 0087aa58 bytes ee7e0f94
+ 0087aa98 bytes de7f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b1ca2d926d2da17b497f595070a90ce"></a>

### [`0087b0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md) → [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) FUN_0087b0f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087ac18.md) · 呼出先 7件 [`0087b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b408.md) [`0087c5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c5c8.md) [`0087c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c7a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) · 呼出先 7件 [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) [`0087c608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c608.md) [`0087c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c7e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087b1b8",
      "incomplete_value": false,
      "site": "0087b1b8",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b178",
      "incomplete_value": false,
      "site": "0087b178",
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
            "const:98:8"
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
      "definition_site": "0087b158",
      "incomplete_value": false,
      "site": "0087b170",
      "value": [
        "leaf",
        "const:87c608:8"
      ]
    },
    "old": {
      "definition_site": "0087b118",
      "incomplete_value": false,
      "site": "0087b130",
      "value": [
        "leaf",
        "const:87c5c8:8"
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
      "0087b158",
      "PARAM",
      [
        "storage",
        "0087c5c8",
        null,
        null
      ]
    ],
    [
      "0087b1b8",
      "DATA",
      [
        "storage",
        "00c80098",
        null,
        "undefined *"
      ]
    ],
    [
      "0087b238",
      "READ",
      [
        "storage",
        "00c800c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b158",
      "PARAM",
      [
        "storage",
        "0087c608",
        null,
        null
      ]
    ],
    [
      "0087b1b8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ],
    [
      "0087b238",
      "READ",
      [
        "storage",
        "00c804c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md#insn-0087b0f0) · [`0087b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md#insn-0087b130) · [`0087b138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b0b0.md#insn-0087b138)
- 新版 [`0087b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b130) · [`0087b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b170) · [`0087b178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b178)

~~~diff
- 0087b0f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b0f0 ["INT_ADD", "register:40f0:8", ["const:87b0f0:8", "const:4:8"]]
- 0087b0f0 ["CALLIND", null, ["register:0:8"]]
+ 0087b130 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b130 ["INT_ADD", "register:40f0:8", ["const:87b130:8", "const:4:8"]]
+ 0087b130 ["CALLIND", null, ["register:0:8"]]
- 0087b0f0 bytes 20013fd6
+ 0087b130 bytes 20013fd6
- 0087b130 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b130 ["INT_ADD", "register:40f0:8", ["const:87b130:8", "const:4:8"]]
- 0087b130 ["CALLIND", null, ["register:0:8"]]
+ 0087b170 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b170 ["INT_ADD", "register:40f0:8", ["const:87b170:8", "const:4:8"]]
+ 0087b170 ["CALLIND", null, ["register:0:8"]]
- 0087b130 bytes 20013fd6
+ 0087b170 bytes 20013fd6
- 0087b138 ["INT_ADD", "register:40f0:8", ["const:87b138:8", "const:4:8"]]
- 0087b138 ["CALL", null, ["callee:00c5aa10:8"]]
+ 0087b178 ["INT_ADD", "register:40f0:8", ["const:87b178:8", "const:4:8"]]
+ 0087b178 ["CALL", null, ["callee:00c5aa10:8"]]
- 0087b138 bytes 367d0f94
+ 0087b178 bytes 267e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d173623aa9eeba64cd5fc56023d8d32e"></a>

### [`0087b564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b564.md) → [`0087b5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5a4.md) FUN_0087b5a4

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
      "definition_site": "0087b5b0",
      "incomplete_value": false,
      "site": "0087b5bc",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b570",
      "incomplete_value": false,
      "site": "0087b57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0087b5bc",
      "DATA",
      [
        "storage",
        "00c7fe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b5bc",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b564.md#insn-0087b56c) · [`0087b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b564.md#insn-0087b570)
- 新版 [`0087b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5a4.md#insn-0087b5ac) · [`0087b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5a4.md#insn-0087b5b0)

~~~diff
- 0087b56c ["COPY", "register:4050:8", ["const:c7f000:8"]]
+ 0087b5ac ["COPY", "register:4050:8", ["const:c80000:8"]]
- 0087b56c bytes 2a200090
+ 0087b5ac bytes 2a2000b0
- 0087b570 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0087b570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087b570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087b570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087b5b0 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0087b5b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087b5b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087b5b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087b570 bytes 4aa13991
+ 0087b5b0 bytes 4aa10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec994283a742dcb4519a3a4458b384f"></a>

### [`0087b5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b5a8.md) → [`0087b5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md) FUN_0087b5e8

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
      "definition_site": "0087b600",
      "incomplete_value": false,
      "site": "0087b60c",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b5c0",
      "incomplete_value": false,
      "site": "0087b5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0087b60c",
      "DATA",
      [
        "storage",
        "00c7fe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b60c",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b5a8.md#insn-0087b5bc) · [`0087b5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b5a8.md#insn-0087b5c0) · [`0087b5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b5a8.md#insn-0087b5f0)
- 新版 [`0087b5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md#insn-0087b5fc) · [`0087b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md#insn-0087b600) · [`0087b630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md#insn-0087b630)

~~~diff
- 0087b5bc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087b5fc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087b5bc bytes 28200090
+ 0087b5fc bytes 282000b0
- 0087b5c0 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0087b5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b600 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0087b600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b5c0 bytes 08a13991
+ 0087b600 bytes 08a10991
- 0087b5f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b5f0 ["INT_ADD", "register:40f0:8", ["const:87b5f0:8", "const:4:8"]]
- 0087b5f0 ["CALLIND", null, ["register:0:8"]]
+ 0087b630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b630 ["INT_ADD", "register:40f0:8", ["const:87b630:8", "const:4:8"]]
+ 0087b630 ["CALLIND", null, ["register:0:8"]]
- 0087b5f0 bytes 00013fd6
+ 0087b630 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a3700ff9fc59f383fcb4d33ffb45ed"></a>

### [`0087b604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b604.md) → [`0087b644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md) FUN_0087b644

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0087b670",
      "incomplete_value": false,
      "site": "0087b670",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b630",
      "incomplete_value": false,
      "site": "0087b630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "0087b670",
      "DATA",
      [
        "storage",
        "00c7fe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b670",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b604.md#insn-0087b618) · [`0087b624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b604.md#insn-0087b624) · [`0087b628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b604.md#insn-0087b628)
- 新版 [`0087b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b658) · [`0087b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b664) · [`0087b668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b668)

~~~diff
- 0087b618 ["INT_ADD", "register:40f0:8", ["const:87b618:8", "const:4:8"]]
- 0087b618 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087b658 ["INT_ADD", "register:40f0:8", ["const:87b658:8", "const:4:8"]]
+ 0087b658 ["CALL", null, ["callee:00c57e90:8"]]
- 0087b618 bytes 1e710f94
+ 0087b658 bytes 0e720f94
- 0087b624 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087b664 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087b624 bytes 28200090
+ 0087b664 bytes 282000b0
- 0087b628 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0087b628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b668 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0087b668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b628 bytes 08a13991
+ 0087b668 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8bcaf7665d01f66893357681f7f3d62"></a>

### [`0087b68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b68c.md) → [`0087b6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md) FUN_0087b6cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b6e8",
      "incomplete_value": false,
      "site": "0087b6e8",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b6a8",
      "incomplete_value": false,
      "site": "0087b6a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "0087b6e8",
      "DATA",
      [
        "storage",
        "00c7fe68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b6e8",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b68c.md#insn-0087b6a0) · [`0087b6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b68c.md#insn-0087b6a4) · [`0087b6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b68c.md#insn-0087b6c8)
- 新版 [`0087b6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md#insn-0087b6e0) · [`0087b6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md#insn-0087b6e4) · [`0087b708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md#insn-0087b708)

~~~diff
- 0087b6a0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 0087b6e0 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0087b6a0 bytes 29200090
+ 0087b6e0 bytes 292000b0
- 0087b6a4 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0087b6a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087b6a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087b6a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087b6e4 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0087b6e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087b6e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087b6e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087b6a4 bytes 29a13991
+ 0087b6e4 bytes 29a10991
- 0087b6c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b6c8 ["INT_ADD", "register:40f0:8", ["const:87b6c8:8", "const:4:8"]]
- 0087b6c8 ["CALLIND", null, ["register:0:8"]]
+ 0087b708 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b708 ["INT_ADD", "register:40f0:8", ["const:87b708:8", "const:4:8"]]
+ 0087b708 ["CALLIND", null, ["register:0:8"]]
- 0087b6c8 bytes 20013fd6
+ 0087b708 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618a6ed15c7ee8781478b4d5da3f4dbd"></a>

### [`0087b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b7d0.md) → [`0087b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md) FUN_0087b810

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b828",
      "incomplete_value": false,
      "site": "0087b838",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b7e8",
      "incomplete_value": false,
      "site": "0087b7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "0087b838",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b838",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b7d0.md#insn-0087b7e4) · [`0087b7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b7d0.md#insn-0087b7e8) · [`0087b81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b7d0.md#insn-0087b81c)
- 新版 [`0087b824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md#insn-0087b824) · [`0087b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md#insn-0087b828) · [`0087b85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md#insn-0087b85c)

~~~diff
- 0087b7e4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087b824 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087b7e4 bytes 28200090
+ 0087b824 bytes 282000b0
- 0087b7e8 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 0087b7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b828 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0087b828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b7e8 bytes 08e13b91
+ 0087b828 bytes 08e10b91
- 0087b81c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b81c ["INT_ADD", "register:40f0:8", ["const:87b81c:8", "const:4:8"]]
- 0087b81c ["CALLIND", null, ["register:0:8"]]
+ 0087b85c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b85c ["INT_ADD", "register:40f0:8", ["const:87b85c:8", "const:4:8"]]
+ 0087b85c ["CALLIND", null, ["register:0:8"]]
- 0087b81c bytes 00013fd6
+ 0087b85c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07833ef055b5733e73b43c20439a8e1e"></a>

### [`0087b860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b860.md) → [`0087b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md) FUN_0087b8a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b8b8",
      "incomplete_value": false,
      "site": "0087b8c8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b878",
      "incomplete_value": false,
      "site": "0087b888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "0087b8c8",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b8c8",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b860.md#insn-0087b874) · [`0087b878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b860.md#insn-0087b878) · [`0087b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b860.md#insn-0087b8ac)
- 新版 [`0087b8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b8b4) · [`0087b8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b8b8) · [`0087b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b8ec)

~~~diff
- 0087b874 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087b8b4 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087b874 bytes 28200090
+ 0087b8b4 bytes 282000b0
- 0087b878 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 0087b878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b8b8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0087b8b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b8b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b8b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b878 bytes 08e13b91
+ 0087b8b8 bytes 08e10b91
- 0087b8ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b8ac ["INT_ADD", "register:40f0:8", ["const:87b8ac:8", "const:4:8"]]
- 0087b8ac ["CALLIND", null, ["register:0:8"]]
+ 0087b8ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b8ec ["INT_ADD", "register:40f0:8", ["const:87b8ec:8", "const:4:8"]]
+ 0087b8ec ["CALLIND", null, ["register:0:8"]]
- 0087b8ac bytes 00013fd6
+ 0087b8ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75fb44ecd470f19204a5181e75a041ed"></a>

### [`0087b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md) → [`0087b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md) FUN_0087b92c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b95c",
      "incomplete_value": false,
      "site": "0087b95c",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b91c",
      "incomplete_value": false,
      "site": "0087b91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "0087b95c",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b95c",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md#insn-0087b904) · [`0087b910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md#insn-0087b910) · [`0087b914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md#insn-0087b914)
- 新版 [`0087b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b944) · [`0087b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b950) · [`0087b954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b954)

~~~diff
- 0087b904 ["INT_ADD", "register:40f0:8", ["const:87b904:8", "const:4:8"]]
- 0087b904 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087b944 ["INT_ADD", "register:40f0:8", ["const:87b944:8", "const:4:8"]]
+ 0087b944 ["CALL", null, ["callee:00c57e90:8"]]
- 0087b904 bytes 63700f94
+ 0087b944 bytes 53710f94
- 0087b910 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087b950 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087b910 bytes 28200090
+ 0087b950 bytes 282000b0
- 0087b914 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 0087b914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b954 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0087b954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b914 bytes 08e13b91
+ 0087b954 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a6dc04344f038d84c484c513878d515"></a>

### [`0087b9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b9fc.md) → [`0087ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md) FUN_0087ba3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ba64",
      "incomplete_value": true,
      "site": "0087ba64",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ba24",
      "incomplete_value": true,
      "site": "0087ba24",
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
            "const:ef8:8"
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
      "0087ba64",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ba64",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ba18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b9fc.md#insn-0087ba18) · [`0087ba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b9fc.md#insn-0087ba1c) · [`0087ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b9fc.md#insn-0087ba40)
- 新版 [`0087ba58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087ba58) · [`0087ba5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087ba5c) · [`0087ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087ba80)

~~~diff
- 0087ba18 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087ba58 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087ba18 bytes 28200090
+ 0087ba58 bytes 282000b0
- 0087ba1c ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 0087ba1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087ba1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087ba1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087ba5c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 0087ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087ba1c bytes 08e13b91
+ 0087ba5c bytes 08e10b91
- 0087ba40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087ba40 ["INT_ADD", "register:40f0:8", ["const:87ba40:8", "const:4:8"]]
- 0087ba40 ["CALLIND", null, ["register:0:8"]]
+ 0087ba80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087ba80 ["INT_ADD", "register:40f0:8", ["const:87ba80:8", "const:4:8"]]
+ 0087ba80 ["CALLIND", null, ["register:0:8"]]
- 0087ba40 bytes 00013fd6
+ 0087ba80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd30b156f1b374363cfa23357fc01ce6"></a>

### [`0087bc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md) → [`0087bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md) FUN_0087bc44

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00879604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md) [`0087a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087a/0087a708.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00879644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md) [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087bcbc",
      "incomplete_value": true,
      "site": "0087bcd0",
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
      "definition_site": "0087bc7c",
      "incomplete_value": true,
      "site": "0087bc90",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087bcd4",
      "incomplete_value": true,
      "site": "0087bce4",
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
                "const:781:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bc94",
      "incomplete_value": true,
      "site": "0087bca4",
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
                "const:741:8"
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
      "definition_site": "0087bcd4",
      "incomplete_value": true,
      "site": "0087bce4",
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
      "definition_site": "0087bc94",
      "incomplete_value": true,
      "site": "0087bca4",
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
      "0087bcbc",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ],
    [
      "0087bcd4",
      "READ",
      [
        "storage",
        "002c1741",
        null,
        null
      ]
    ],
    [
      "0087bcd4",
      "READ",
      [
        "storage",
        "002c1751",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087bcbc",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ],
    [
      "0087bcd4",
      "READ",
      [
        "storage",
        "002c1781",
        null,
        null
      ]
    ],
    [
      "0087bcd4",
      "READ",
      [
        "storage",
        "002c1791",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087bd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md#insn-0087bd7c) · [`0087bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md#insn-0087bc34) · [`0087bc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md#insn-0087bc4c)
- 新版 [`0087bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bdbc) · [`0087bc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bc74) · [`0087bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md#insn-0087bc8c)

~~~diff
- 0087bd7c ["INT_ADD", "register:40f0:8", ["const:87bd7c:8", "const:4:8"]]
- 0087bd7c ["CALL", null, ["ram:87a708:8"]]
+ 0087bdbc ["INT_ADD", "register:40f0:8", ["const:87bdbc:8", "const:4:8"]]
+ 0087bdbc ["CALL", null, ["ram:87a748:8"]]
- 0087bd7c bytes 63faff97
+ 0087bdbc bytes 63faff97
- 0087bc34 ["INT_ADD", "register:40f0:8", ["const:87bc34:8", "const:4:8"]]
- 0087bc34 ["CALL", null, ["callee:00c5aa00:8"]]
+ 0087bc74 ["INT_ADD", "register:40f0:8", ["const:87bc74:8", "const:4:8"]]
+ 0087bc74 ["CALL", null, ["callee:00c5aa00:8"]]
- 0087bc34 bytes 737a0f94
+ 0087bc74 bytes 637b0f94
- 0087bc4c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bc4c ["INT_ADD", "register:40f0:8", ["const:87bc4c:8", "const:4:8"]]
- 0087bc4c ["CALLIND", null, ["register:0:8"]]
+ 0087bc8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bc8c ["INT_ADD", "register:40f0:8", ["const:87bc8c:8", "const:4:8"]]
+ 0087bc8c ["CALLIND", null, ["register:0:8"]]
- 0087bc4c bytes 00013fd6
+ 0087bc8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4269b9520c4f81ab162d6e7b3f4315e1"></a>

### [`0087bf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bf64.md) → [`0087bfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa4.md) FUN_0087bfa4

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
      "definition_site": "0087bfb0",
      "incomplete_value": false,
      "site": "0087bfbc",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bf70",
      "incomplete_value": false,
      "site": "0087bf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0087bfbc",
      "DATA",
      [
        "storage",
        "00c7ff88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087bfbc",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087bf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bf64.md#insn-0087bf6c) · [`0087bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bf64.md#insn-0087bf70)
- 新版 [`0087bfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa4.md#insn-0087bfac) · [`0087bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa4.md#insn-0087bfb0)

~~~diff
- 0087bf6c ["COPY", "register:4050:8", ["const:c7f000:8"]]
+ 0087bfac ["COPY", "register:4050:8", ["const:c80000:8"]]
- 0087bf6c bytes 2a200090
+ 0087bfac bytes 2a2000b0
- 0087bf70 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0087bf70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087bf70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087bf70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087bfb0 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0087bfb0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087bfb0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087bfb0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087bf70 bytes 4a213e91
+ 0087bfb0 bytes 4a210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed76d1ecebd22ea958bba145a76a260"></a>

### [`0087bfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bfa8.md) → [`0087bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md) FUN_0087bfe8

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
      "definition_site": "0087c000",
      "incomplete_value": false,
      "site": "0087c00c",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bfc0",
      "incomplete_value": false,
      "site": "0087bfcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0087c00c",
      "DATA",
      [
        "storage",
        "00c7ff88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c00c",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087bfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bfa8.md#insn-0087bfbc) · [`0087bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bfa8.md#insn-0087bfc0) · [`0087bff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bfa8.md#insn-0087bff0)
- 新版 [`0087bffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md#insn-0087bffc) · [`0087c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md#insn-0087c000) · [`0087c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfe8.md#insn-0087c030)

~~~diff
- 0087bfbc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087bffc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087bfbc bytes 28200090
+ 0087bffc bytes 282000b0
- 0087bfc0 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0087bfc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087bfc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087bfc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c000 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0087c000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087bfc0 bytes 08213e91
+ 0087c000 bytes 08210e91
- 0087bff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087bff0 ["INT_ADD", "register:40f0:8", ["const:87bff0:8", "const:4:8"]]
- 0087bff0 ["CALLIND", null, ["register:0:8"]]
+ 0087c030 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c030 ["INT_ADD", "register:40f0:8", ["const:87c030:8", "const:4:8"]]
+ 0087c030 ["CALLIND", null, ["register:0:8"]]
- 0087bff0 bytes 00013fd6
+ 0087c030 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a9d7b1e9191ea524425f80e899b463"></a>

### [`0087c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c004.md) → [`0087c044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md) FUN_0087c044

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0087c070",
      "incomplete_value": false,
      "site": "0087c070",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c030",
      "incomplete_value": false,
      "site": "0087c030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0087c070",
      "DATA",
      [
        "storage",
        "00c7ff88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c070",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c004.md#insn-0087c018) · [`0087c024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c004.md#insn-0087c024) · [`0087c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c004.md#insn-0087c028)
- 新版 [`0087c058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c058) · [`0087c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c064) · [`0087c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c044.md#insn-0087c068)

~~~diff
- 0087c018 ["INT_ADD", "register:40f0:8", ["const:87c018:8", "const:4:8"]]
- 0087c018 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087c058 ["INT_ADD", "register:40f0:8", ["const:87c058:8", "const:4:8"]]
+ 0087c058 ["CALL", null, ["callee:00c57e90:8"]]
- 0087c018 bytes 9e6e0f94
+ 0087c058 bytes 8e6f0f94
- 0087c024 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087c064 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0087c024 bytes 082000f0
+ 0087c064 bytes 28200090
- 0087c028 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0087c028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c068 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0087c068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c028 bytes 08213e91
+ 0087c068 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cad6268682c7454db90a1df8512d15e"></a>

### [`0087c08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c08c.md) → [`0087c0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md) FUN_0087c0cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c0e8",
      "incomplete_value": false,
      "site": "0087c0e8",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c0a8",
      "incomplete_value": false,
      "site": "0087c0a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0087c0e8",
      "DATA",
      [
        "storage",
        "00c7ff88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c0e8",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c08c.md#insn-0087c0a0) · [`0087c0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c08c.md#insn-0087c0a4) · [`0087c0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c08c.md#insn-0087c0c8)
- 新版 [`0087c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md#insn-0087c0e0) · [`0087c0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md#insn-0087c0e4) · [`0087c108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c0cc.md#insn-0087c108)

~~~diff
- 0087c0a0 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 0087c0e0 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0087c0a0 bytes 092000f0
+ 0087c0e0 bytes 29200090
- 0087c0a4 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0087c0a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c0a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c0a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c0e4 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0087c0e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c0e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c0e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c0a4 bytes 29213e91
+ 0087c0e4 bytes 29210e91
- 0087c0c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c0c8 ["INT_ADD", "register:40f0:8", ["const:87c0c8:8", "const:4:8"]]
- 0087c0c8 ["CALLIND", null, ["register:0:8"]]
+ 0087c108 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c108 ["INT_ADD", "register:40f0:8", ["const:87c108:8", "const:4:8"]]
+ 0087c108 ["CALLIND", null, ["register:0:8"]]
- 0087c0c8 bytes 20013fd6
+ 0087c108 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1f114202582e0769c0e67ccd3b1b2c6"></a>

### [`0087c1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c1d0.md) → [`0087c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c210.md) FUN_0087c210

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
      "definition_site": "0087c21c",
      "incomplete_value": false,
      "site": "0087c228",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c1dc",
      "incomplete_value": false,
      "site": "0087c1e8",
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
            "const:8:8"
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
      "0087c228",
      "DATA",
      [
        "storage",
        "00c80008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c228",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c1d0.md#insn-0087c1dc)
- 新版 [`0087c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c210.md#insn-0087c21c)

~~~diff
- 0087c1dc ["COPY", "tmp:0:8", ["const:8:8"]]
- 0087c1dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c1dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c1dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087c21c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0087c21c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c21c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c21c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c1dc bytes 4a210091
+ 0087c21c bytes 4a211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-365ecdc79c889a9fec6384dc11fe9673"></a>

### [`0087c214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c214.md) → [`0087c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md) FUN_0087c254

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
      "definition_site": "0087c26c",
      "incomplete_value": false,
      "site": "0087c278",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c22c",
      "incomplete_value": false,
      "site": "0087c238",
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
            "const:8:8"
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
      "0087c278",
      "DATA",
      [
        "storage",
        "00c80008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c278",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c214.md#insn-0087c22c) · [`0087c25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c214.md#insn-0087c25c)
- 新版 [`0087c26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md#insn-0087c26c) · [`0087c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c254.md#insn-0087c29c)

~~~diff
- 0087c22c ["COPY", "tmp:0:8", ["const:8:8"]]
- 0087c22c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c22c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c22c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c26c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0087c26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c22c bytes 08210091
+ 0087c26c bytes 08211091
- 0087c25c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c25c ["INT_ADD", "register:40f0:8", ["const:87c25c:8", "const:4:8"]]
- 0087c25c ["CALLIND", null, ["register:0:8"]]
+ 0087c29c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c29c ["INT_ADD", "register:40f0:8", ["const:87c29c:8", "const:4:8"]]
+ 0087c29c ["CALLIND", null, ["register:0:8"]]
- 0087c25c bytes 00013fd6
+ 0087c29c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a99239518cb7c62cbddbbeb6d57488c"></a>

### [`0087c270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c270.md) → [`0087c2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md) FUN_0087c2b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0087c2dc",
      "incomplete_value": false,
      "site": "0087c2dc",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c29c",
      "incomplete_value": false,
      "site": "0087c29c",
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
            "const:8:8"
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
      "0087c2dc",
      "DATA",
      [
        "storage",
        "00c80008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c2dc",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c270.md#insn-0087c284) · [`0087c294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c270.md#insn-0087c294) · [`0087c2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c270.md#insn-0087c2b8)
- 新版 [`0087c2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2c4) · [`0087c2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2d4) · [`0087c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c2b0.md#insn-0087c2f8)

~~~diff
- 0087c284 ["INT_ADD", "register:40f0:8", ["const:87c284:8", "const:4:8"]]
- 0087c284 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087c2c4 ["INT_ADD", "register:40f0:8", ["const:87c2c4:8", "const:4:8"]]
+ 0087c2c4 ["CALL", null, ["callee:00c57e90:8"]]
- 0087c284 bytes 036e0f94
+ 0087c2c4 bytes f36e0f94
- 0087c294 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0087c294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c2d4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0087c2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c294 bytes 08210091
+ 0087c2d4 bytes 08211091
- 0087c2b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c2b8 ["INT_ADD", "register:40f0:8", ["const:87c2b8:8", "const:4:8"]]
- 0087c2b8 ["CALLIND", null, ["register:0:8"]]
+ 0087c2f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c2f8 ["INT_ADD", "register:40f0:8", ["const:87c2f8:8", "const:4:8"]]
+ 0087c2f8 ["CALLIND", null, ["register:0:8"]]
- 0087c2b8 bytes 00013fd6
+ 0087c2f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69656c464ac0b39e450a7fe70ef4633e"></a>

### [`0087c2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c2f8.md) → [`0087c338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md) FUN_0087c338

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c354",
      "incomplete_value": false,
      "site": "0087c354",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c314",
      "incomplete_value": false,
      "site": "0087c314",
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
            "const:8:8"
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
      "0087c354",
      "DATA",
      [
        "storage",
        "00c80008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c354",
      "DATA",
      [
        "storage",
        "00c80408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c2f8.md#insn-0087c310) · [`0087c334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c2f8.md#insn-0087c334)
- 新版 [`0087c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md#insn-0087c350) · [`0087c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c338.md#insn-0087c374)

~~~diff
- 0087c310 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0087c310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c350 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 0087c350 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c350 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c350 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c310 bytes 29210091
+ 0087c350 bytes 29211091
- 0087c334 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c334 ["INT_ADD", "register:40f0:8", ["const:87c334:8", "const:4:8"]]
- 0087c334 ["CALLIND", null, ["register:0:8"]]
+ 0087c374 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c374 ["INT_ADD", "register:40f0:8", ["const:87c374:8", "const:4:8"]]
+ 0087c374 ["CALLIND", null, ["register:0:8"]]
- 0087c334 bytes 20013fd6
+ 0087c374 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3fa86cb34829207f69b308ba1390794"></a>

### [`0087c5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c5cc.md) → [`0087c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c60c.md) FUN_0087c60c

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
      "definition_site": "0087c618",
      "incomplete_value": false,
      "site": "0087c624",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c5d8",
      "incomplete_value": false,
      "site": "0087c5e4",
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
      "0087c624",
      "DATA",
      [
        "storage",
        "00c80098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c624",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c5cc.md#insn-0087c5d8)
- 新版 [`0087c618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c60c.md#insn-0087c618)

~~~diff
- 0087c5d8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0087c5d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c5d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c5d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087c618 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0087c618 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c618 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087c618 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c5d8 bytes 4a610291
+ 0087c618 bytes 4a611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588ee52d48471a1f7fed90fb63967c66"></a>

### [`0087c610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c610.md) → [`0087c650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md) FUN_0087c650

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
      "definition_site": "0087c668",
      "incomplete_value": false,
      "site": "0087c674",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c628",
      "incomplete_value": false,
      "site": "0087c634",
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
      "0087c674",
      "DATA",
      [
        "storage",
        "00c80098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c674",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c610.md#insn-0087c628) · [`0087c658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c610.md#insn-0087c658)
- 新版 [`0087c668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md#insn-0087c668) · [`0087c698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c650.md#insn-0087c698)

~~~diff
- 0087c628 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0087c628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c668 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0087c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c628 bytes 08610291
+ 0087c668 bytes 08611291
- 0087c658 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c658 ["INT_ADD", "register:40f0:8", ["const:87c658:8", "const:4:8"]]
- 0087c658 ["CALLIND", null, ["register:0:8"]]
+ 0087c698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c698 ["INT_ADD", "register:40f0:8", ["const:87c698:8", "const:4:8"]]
+ 0087c698 ["CALLIND", null, ["register:0:8"]]
- 0087c658 bytes 00013fd6
+ 0087c698 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e8a99d75a3df3865cb652809ebc532"></a>

### [`0087c66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c66c.md) → [`0087c6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md) FUN_0087c6ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0087c6d8",
      "incomplete_value": false,
      "site": "0087c6d8",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c698",
      "incomplete_value": false,
      "site": "0087c698",
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
            "const:98:8"
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
      "0087c6d8",
      "DATA",
      [
        "storage",
        "00c80098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c6d8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c66c.md#insn-0087c680) · [`0087c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c66c.md#insn-0087c690) · [`0087c6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c66c.md#insn-0087c6b4)
- 新版 [`0087c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6c0) · [`0087c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6d0) · [`0087c6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c6ac.md#insn-0087c6f4)

~~~diff
- 0087c680 ["INT_ADD", "register:40f0:8", ["const:87c680:8", "const:4:8"]]
- 0087c680 ["CALL", null, ["callee:00c57e90:8"]]
+ 0087c6c0 ["INT_ADD", "register:40f0:8", ["const:87c6c0:8", "const:4:8"]]
+ 0087c6c0 ["CALL", null, ["callee:00c57e90:8"]]
- 0087c680 bytes 046d0f94
+ 0087c6c0 bytes f46d0f94
- 0087c690 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0087c690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c6d0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0087c6d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c6d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c6d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c690 bytes 08610291
+ 0087c6d0 bytes 08611291
- 0087c6b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c6b4 ["INT_ADD", "register:40f0:8", ["const:87c6b4:8", "const:4:8"]]
- 0087c6b4 ["CALLIND", null, ["register:0:8"]]
+ 0087c6f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c6f4 ["INT_ADD", "register:40f0:8", ["const:87c6f4:8", "const:4:8"]]
+ 0087c6f4 ["CALLIND", null, ["register:0:8"]]
- 0087c6b4 bytes 00013fd6
+ 0087c6f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ba5fb8a5d83b8dbb1f21e262362723"></a>

### [`0087c6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c6f4.md) → [`0087c734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md) FUN_0087c734

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c750",
      "incomplete_value": false,
      "site": "0087c750",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c710",
      "incomplete_value": false,
      "site": "0087c710",
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
      "0087c750",
      "DATA",
      [
        "storage",
        "00c80098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c750",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c6f4.md#insn-0087c70c) · [`0087c730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c6f4.md#insn-0087c730)
- 新版 [`0087c74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md#insn-0087c74c) · [`0087c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c734.md#insn-0087c770)

~~~diff
- 0087c70c ["COPY", "tmp:0:8", ["const:98:8"]]
- 0087c70c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c70c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c70c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c74c ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0087c74c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c74c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c74c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c70c bytes 29610291
+ 0087c74c bytes 29611291
- 0087c730 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c730 ["INT_ADD", "register:40f0:8", ["const:87c730:8", "const:4:8"]]
- 0087c730 ["CALLIND", null, ["register:0:8"]]
+ 0087c770 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c770 ["INT_ADD", "register:40f0:8", ["const:87c770:8", "const:4:8"]]
+ 0087c770 ["CALLIND", null, ["register:0:8"]]
- 0087c730 bytes 20013fd6
+ 0087c770 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af54d0be263f033ee3fc22028e4c741"></a>

### [`0087c838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c838.md) → [`0087c878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md) FUN_0087c878

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c890",
      "incomplete_value": false,
      "site": "0087c8a0",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c850",
      "incomplete_value": false,
      "site": "0087c860",
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
            "const:118:8"
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
      "0087c8a0",
      "DATA",
      [
        "storage",
        "00c80118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c8a0",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c838.md#insn-0087c850) · [`0087c884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c838.md#insn-0087c884)
- 新版 [`0087c890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md#insn-0087c890) · [`0087c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c878.md#insn-0087c8c4)

~~~diff
- 0087c850 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0087c850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c890 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0087c890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c850 bytes 08610491
+ 0087c890 bytes 08611491
- 0087c884 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c884 ["INT_ADD", "register:40f0:8", ["const:87c884:8", "const:4:8"]]
- 0087c884 ["CALLIND", null, ["register:0:8"]]
+ 0087c8c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c8c4 ["INT_ADD", "register:40f0:8", ["const:87c8c4:8", "const:4:8"]]
+ 0087c8c4 ["CALLIND", null, ["register:0:8"]]
- 0087c884 bytes 00013fd6
+ 0087c8c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed37678706244308554cf60c9aef0b73"></a>

### [`0087c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c8c8.md) → [`0087c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md) FUN_0087c908

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c920",
      "incomplete_value": false,
      "site": "0087c930",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c8e0",
      "incomplete_value": false,
      "site": "0087c8f0",
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
            "const:118:8"
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
      "0087c930",
      "DATA",
      [
        "storage",
        "00c80118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c930",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c8c8.md#insn-0087c8e0) · [`0087c914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c8c8.md#insn-0087c914) · [`0087c940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c8c8.md#insn-0087c940)
- 新版 [`0087c920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c920) · [`0087c954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c954) · [`0087c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c908.md#insn-0087c980)

~~~diff
- 0087c8e0 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0087c8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c920 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0087c920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c8e0 bytes 08610491
+ 0087c920 bytes 08611491
- 0087c914 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c914 ["INT_ADD", "register:40f0:8", ["const:87c914:8", "const:4:8"]]
- 0087c914 ["CALLIND", null, ["register:0:8"]]
+ 0087c954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c954 ["INT_ADD", "register:40f0:8", ["const:87c954:8", "const:4:8"]]
+ 0087c954 ["CALLIND", null, ["register:0:8"]]
- 0087c914 bytes 00013fd6
+ 0087c954 bytes 00013fd6
- 0087c940 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c940 ["INT_ADD", "register:40f0:8", ["const:87c940:8", "const:4:8"]]
- 0087c940 ["CALLIND", null, ["register:0:8"]]
+ 0087c980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c980 ["INT_ADD", "register:40f0:8", ["const:87c980:8", "const:4:8"]]
+ 0087c980 ["CALLIND", null, ["register:0:8"]]
- 0087c940 bytes 00013fd6
+ 0087c980 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7ecec5052e0f6d03dbed7917cac65d"></a>

### [`0087c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c954.md) → [`0087c994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md) FUN_0087c994

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0087c9c4",
      "incomplete_value": false,
      "site": "0087c9c4",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c984",
      "incomplete_value": false,
      "site": "0087c984",
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
            "const:118:8"
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
      "0087c9c4",
      "DATA",
      [
        "storage",
        "00c80118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c9c4",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c954.md#insn-0087c96c) · [`0087c97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c954.md#insn-0087c97c) · [`0087c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087c954.md#insn-0087c9a0)
- 新版 [`0087c9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087c9ac) · [`0087c9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087c9bc) · [`0087c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c994.md#insn-0087c9e0)

~~~diff
- 0087c96c ["INT_ADD", "register:40f0:8", ["const:87c96c:8", "const:4:8"]]
- 0087c96c ["CALL", null, ["callee:00c57e90:8"]]
+ 0087c9ac ["INT_ADD", "register:40f0:8", ["const:87c9ac:8", "const:4:8"]]
+ 0087c9ac ["CALL", null, ["callee:00c57e90:8"]]
- 0087c96c bytes 496c0f94
+ 0087c9ac bytes 396d0f94
- 0087c97c ["COPY", "tmp:0:8", ["const:118:8"]]
- 0087c97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c9bc ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0087c9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c97c bytes 08610491
+ 0087c9bc bytes 08611491
- 0087c9a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c9a0 ["INT_ADD", "register:40f0:8", ["const:87c9a0:8", "const:4:8"]]
- 0087c9a0 ["CALLIND", null, ["register:0:8"]]
+ 0087c9e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c9e0 ["INT_ADD", "register:40f0:8", ["const:87c9e0:8", "const:4:8"]]
+ 0087c9e0 ["CALLIND", null, ["register:0:8"]]
- 0087c9a0 bytes 00013fd6
+ 0087c9e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ff1509dfbabd925f012ca3468b961f"></a>

### [`0087ca5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ca5c.md) → [`0087ca9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md) FUN_0087ca9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "0087cac4",
      "incomplete_value": false,
      "site": "0087cac4",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ca84",
      "incomplete_value": false,
      "site": "0087ca84",
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
            "const:118:8"
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
      "0087cac4",
      "DATA",
      [
        "storage",
        "00c80118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087cac4",
      "DATA",
      [
        "storage",
        "00c80518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ca7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ca5c.md#insn-0087ca7c) · [`0087ca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ca5c.md#insn-0087ca80) · [`0087caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ca5c.md#insn-0087caa0)
- 新版 [`0087cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md#insn-0087cabc) · [`0087cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ca9c.md#insn-0087cae0)

~~~diff
- 0087ca7c ["COPY", "tmp:0:8", ["const:118:8"]]
- 0087ca7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087ca7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087ca7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087cabc ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0087cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087ca7c bytes 08610491
+ 0087cabc bytes 08611491
- 0087ca80 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0087ca80 bytes f40301aa
- 0087caa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087caa0 ["INT_ADD", "register:40f0:8", ["const:87caa0:8", "const:4:8"]]
- 0087caa0 ["CALLIND", null, ["register:0:8"]]
+ 0087cae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087cae0 ["INT_ADD", "register:40f0:8", ["const:87cae0:8", "const:4:8"]]
+ 0087cae0 ["CALLIND", null, ["register:0:8"]]
- 0087caa0 bytes 00013fd6
+ 0087cae0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16cdfcad065dc34bf2a5d44f6e2cd9f3"></a>

### [`0087ce30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ce30.md) → [`0087ce70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md) _INIT_161

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 78.74% / 新版 78.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 7件, `store_value` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ceac",
      "incomplete_value": true,
      "site": "0087cec8",
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
      "definition_site": "0087ce6c",
      "incomplete_value": true,
      "site": "0087ce88",
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
      "definition_site": "0087cf10",
      "incomplete_value": true,
      "site": "0087cf28",
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
      "definition_site": "0087ced0",
      "incomplete_value": true,
      "site": "0087cee8",
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
      "definition_site": "0087cf4c",
      "incomplete_value": true,
      "site": "0087cf68",
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
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087cf0c",
      "incomplete_value": true,
      "site": "0087cf28",
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
                "const:e90:8"
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
      "0087ceac",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0087ced0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0087cef0",
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
      "0087ceac",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087ced0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087cef0",
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

- 旧版 [`0087cea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ce30.md#insn-0087cea8) · [`0087cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ce30.md#insn-0087cec8) · [`0087d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ce30.md#insn-0087d050)
- 新版 [`0087cee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087cee8) · [`0087cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087cf08) · [`0087d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087ce70.md#insn-0087d090)

~~~diff
- 0087cea8 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0087cea8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087cea8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087cea8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087cee8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0087cee8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cee8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cee8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087cea8 bytes 4a093691
+ 0087cee8 bytes 4a093791
- 0087cec8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0087cec8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087cec8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087cec8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087cf08 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0087cf08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cf08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cf08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087cec8 bytes 4a553a91
+ 0087cf08 bytes 4a893d91
- 0087d050 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0087d050 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0087d050 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0087d050 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0087d090 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0087d090 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0087d090 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0087d090 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0087d050 bytes 73422e91
+ 0087d090 bytes 73423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31a0aaae38feee21e69898461cfd54ec"></a>

### [`0087d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4cc.md) → [`0087d50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md) FUN_0087d50c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00861348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00861/00861348.md) · 呼出先 6件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a550.md)
- 新版 呼出元 1件 [`00861388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/00861388.md) · 呼出先 6件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a950.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d548",
      "incomplete_value": false,
      "site": "0087d550",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087d508",
      "incomplete_value": false,
      "site": "0087d510",
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
            "const:1a8:8"
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
      "0087d550",
      "DATA",
      [
        "storage",
        "00c801a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d550",
      "DATA",
      [
        "storage",
        "00c805a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087d4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4cc.md#insn-0087d4d8) · [`0087d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4cc.md#insn-0087d4e0) · [`0087d4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d4cc.md#insn-0087d4e4)
- 新版 [`0087d518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d518) · [`0087d520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d520) · [`0087d524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d50c.md#insn-0087d524)

~~~diff
- 0087d4d8 ["INT_ADD", "register:40f0:8", ["const:87d4d8:8", "const:4:8"]]
- 0087d4d8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0087d518 ["INT_ADD", "register:40f0:8", ["const:87d518:8", "const:4:8"]]
+ 0087d518 ["CALL", null, ["callee:00588e6c:8"]]
- 0087d4d8 bytes 552ef497
+ 0087d518 bytes 552ef497
- 0087d4e0 ["INT_ADD", "register:40f0:8", ["const:87d4e0:8", "const:4:8"]]
- 0087d4e0 ["CALL", null, ["callee:0058915c:8"]]
+ 0087d520 ["INT_ADD", "register:40f0:8", ["const:87d520:8", "const:4:8"]]
+ 0087d520 ["CALL", null, ["callee:0058915c:8"]]
- 0087d4e0 bytes 0f2ff497
+ 0087d520 bytes 0f2ff497
- 0087d4e4 ["INT_ADD", "register:40f0:8", ["const:87d4e4:8", "const:4:8"]]
- 0087d4e4 ["CALL", null, ["callee:00589850:8"]]
+ 0087d524 ["INT_ADD", "register:40f0:8", ["const:87d524:8", "const:4:8"]]
+ 0087d524 ["CALL", null, ["callee:00589850:8"]]
- 0087d4e4 bytes cb30f497
+ 0087d524 bytes cb30f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-357b4231039075971f8dec82ae129c98"></a>

### [`0087d520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d520.md) → [`0087d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md) _INIT_162

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
      "definition_site": "0087d59c",
      "incomplete_value": true,
      "site": "0087d5b8",
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
      "definition_site": "0087d55c",
      "incomplete_value": true,
      "site": "0087d578",
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
      "definition_site": "0087d5c0",
      "incomplete_value": true,
      "site": "0087d5dc",
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
      "definition_site": "0087d580",
      "incomplete_value": true,
      "site": "0087d59c",
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
      "definition_site": "0087d5e0",
      "incomplete_value": true,
      "site": "0087d5fc",
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
      "definition_site": "0087d5a0",
      "incomplete_value": true,
      "site": "0087d5bc",
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
      "0087d59c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0087d5c0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0087d5e0",
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
      "0087d59c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087d5c0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087d5e0",
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

- 旧版 [`0087d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d520.md#insn-0087d598) · [`0087d5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d520.md#insn-0087d5b8) · [`0087d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d520.md#insn-0087d680)
- 新版 [`0087d5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d5d8) · [`0087d5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d5f8) · [`0087d6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d560.md#insn-0087d6c0)

~~~diff
- 0087d598 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0087d598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087d598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087d598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087d5d8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0087d5d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d5d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d5d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087d598 bytes 4a093691
+ 0087d5d8 bytes 4a093791
- 0087d5b8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0087d5b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087d5b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087d5b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087d5f8 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0087d5f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d5f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d5f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087d5b8 bytes 4a553a91
+ 0087d5f8 bytes 4a893d91
- 0087d680 ["INT_ADD", "register:40f0:8", ["const:87d680:8", "const:4:8"]]
- 0087d680 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0087d6c0 ["INT_ADD", "register:40f0:8", ["const:87d6c0:8", "const:4:8"]]
+ 0087d6c0 ["CALL", null, ["callee:0043b7f8:8"]]
- 0087d680 bytes 4ef8ee97
+ 0087d6c0 bytes 4ef8ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00f4c23441409a15d47c0aa77ed7586b"></a>

### [`0087dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md) → [`0087dc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md) FUN_0087dc24

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dcd0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0087dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dd10.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087dc3c",
      "incomplete_value": true,
      "site": "0087dc40",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dbfc",
      "incomplete_value": true,
      "site": "0087dc00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:438:8"
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
      "definition_site": "0087dc54",
      "incomplete_value": true,
      "site": "0087dc58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:820:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087dc14",
      "incomplete_value": true,
      "site": "0087dc18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
      "definition_site": "0087dc84",
      "incomplete_value": true,
      "site": "0087dc88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
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
      "definition_site": "0087dc44",
      "incomplete_value": true,
      "site": "0087dc48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1123000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087dc30",
      "READ",
      [
        "storage",
        "01123428",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dc3c",
      "READ",
      [
        "storage",
        "01123438",
        null,
        "undefined8"
      ]
    ],
    [
      "0087dc48",
      "READ",
      [
        "storage",
        "01123410",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087dc30",
      "READ",
      [
        "storage",
        "01123828",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dc3c",
      "READ",
      [
        "storage",
        "01123838",
        null,
        "undefined8"
      ]
    ],
    [
      "0087dc48",
      "READ",
      [
        "storage",
        "01123810",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md#insn-0087dc00) · [`0087dc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md#insn-0087dc08) · [`0087dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md#insn-0087dc18)
- 新版 [`0087dc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc40) · [`0087dc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc48) · [`0087dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087dc24.md#insn-0087dc58)

~~~diff
- 0087dc00 ["INT_ADD", "register:40f0:8", ["const:87dc00:8", "const:4:8"]]
- 0087dc00 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087dc40 ["INT_ADD", "register:40f0:8", ["const:87dc40:8", "const:4:8"]]
+ 0087dc40 ["CALL", null, ["callee:00c57eb0:8"]]
- 0087dc00 bytes ac670f94
+ 0087dc40 bytes 9c680f94
- 0087dc08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:410:8"]]
- 0087dc08 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0087dc08 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 0087dc48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:810:8"]]
+ 0087dc48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0087dc48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0087dc08 bytes 08415039
+ 0087dc48 bytes 08416039
- 0087dc18 ["INT_ADD", "register:40f0:8", ["const:87dc18:8", "const:4:8"]]
- 0087dc18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0087dc58 ["INT_ADD", "register:40f0:8", ["const:87dc58:8", "const:4:8"]]
+ 0087dc58 ["CALL", null, ["callee:00c57eb0:8"]]
- 0087dc18 bytes a6670f94
+ 0087dc58 bytes 96680f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0caa000d665dac1bfadc98e0ef7d9f3"></a>

### [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) → [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) FUN_0087e710

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087e6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6cc.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) [`0087eff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md)
- 新版 呼出元 1件 [`0087e70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e70c.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0087ed4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087ed4c.md) [`0087f038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f038.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087e908",
      "incomplete_value": false,
      "site": "0087e90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087e8c8",
      "incomplete_value": false,
      "site": "0087e8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087e798",
      "READ",
      [
        "storage",
        "01123368",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e798",
      "READ",
      [
        "storage",
        "01123380",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7a0",
      "READ",
      [
        "storage",
        "01123368",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0087e798",
      "READ",
      [
        "storage",
        "01123768",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e798",
      "READ",
      [
        "storage",
        "01123780",
        null,
        "undefined1"
      ]
    ],
    [
      "0087e7a0",
      "READ",
      [
        "storage",
        "01123768",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087e8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md#insn-0087e8cc) · [`0087e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md#insn-0087e90c) · [`0087e708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md#insn-0087e708)
- 新版 [`0087e90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e90c) · [`0087e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e94c) · [`0087e748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md#insn-0087e748)

~~~diff
- 0087e8cc ["INT_ADD", "register:40f0:8", ["const:87e8cc:8", "const:4:8"]]
- 0087e8cc ["CALL", null, ["callee:0087ed4c:8"]]
+ 0087e90c ["INT_ADD", "register:40f0:8", ["const:87e90c:8", "const:4:8"]]
+ 0087e90c ["CALL", null, ["callee:0087ed4c:8"]]
- 0087e8cc bytes 10010094
+ 0087e90c bytes 10010094
- 0087e90c ["INT_ADD", "register:40f0:8", ["const:87e90c:8", "const:4:8"]]
- 0087e90c ["CALL", null, ["callee:00c53d00:8"]]
+ 0087e94c ["INT_ADD", "register:40f0:8", ["const:87e94c:8", "const:4:8"]]
+ 0087e94c ["CALL", null, ["callee:00c53d00:8"]]
- 0087e90c bytes f5530f94
+ 0087e94c bytes ed540f94
- 0087e708 ["INT_ADD", "register:40f0:8", ["const:87e708:8", "const:4:8"]]
- 0087e708 ["CALL", null, ["callee:00b36338:8"]]
+ 0087e748 ["INT_ADD", "register:40f0:8", ["const:87e748:8", "const:4:8"]]
+ 0087e748 ["CALL", null, ["callee:00b36338:8"]]
- 0087e708 bytes 02de0a94
+ 0087e748 bytes fcde0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1b199b24e08e01e2802475c61790957"></a>

### [`0087efb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087efb8.md) → [`0087eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eff8.md) FUN_0087eff8

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
      "definition_site": "0087effc",
      "incomplete_value": false,
      "site": "0087f000",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087efbc",
      "incomplete_value": false,
      "site": "0087efc0",
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
            "const:200:8"
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
      "0087f000",
      "DATA",
      [
        "storage",
        "00c80200",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087f000",
      "DATA",
      [
        "storage",
        "00c80600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087efbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087efb8.md#insn-0087efbc)
- 新版 [`0087effc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eff8.md#insn-0087effc)

~~~diff
- 0087efbc ["COPY", "tmp:0:8", ["const:200:8"]]
- 0087efbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087efbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087efbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087effc ["COPY", "tmp:0:8", ["const:600:8"]]
+ 0087effc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087effc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087effc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087efbc bytes 08010891
+ 0087effc bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235440232a1a7d7a1ba6edd43eaff3ca"></a>

### [`0087efc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087efc8.md) → [`0087f008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md) FUN_0087f008

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
      "definition_site": "0087f018",
      "incomplete_value": false,
      "site": "0087f020",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087efd8",
      "incomplete_value": false,
      "site": "0087efe0",
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
            "const:200:8"
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
      "0087f020",
      "DATA",
      [
        "storage",
        "00c80200",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087f020",
      "DATA",
      [
        "storage",
        "00c80600",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087efc8.md#insn-0087efd8) · [`0087efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087efc8.md#insn-0087efe4)
- 新版 [`0087f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md#insn-0087f018) · [`0087f024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f008.md#insn-0087f024)

~~~diff
- 0087efd8 ["COPY", "tmp:0:8", ["const:200:8"]]
- 0087efd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087efd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087efd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087f018 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 0087f018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087f018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087efd8 bytes 08010891
+ 0087f018 bytes 08011891
- 0087efe4 ["INT_ADD", "register:40f0:8", ["const:87efe4:8", "const:4:8"]]
- 0087efe4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0087f024 ["INT_ADD", "register:40f0:8", ["const:87f024:8", "const:4:8"]]
+ 0087f024 ["CALL", null, ["callee:00c57ea0:8"]]
- 0087efe4 bytes af620f94
+ 0087f024 bytes 9f630f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f041e40e9c7cb1ae3762cc7e7227fe"></a>

### [`0087f0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md) → [`0087f10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md) FUN_0087f10c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.29% / 新版 94.29%

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
      "site": "0087f134",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f0f4",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0087f13c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f0fc",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0087f134",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0087f13c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0087f14c",
      "READ",
      [
        "storage",
        "002b786c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087f134",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f13c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f14c",
      "READ",
      [
        "storage",
        "002b78ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md#insn-0087f0f4) · [`0087f0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md#insn-0087f0fc) · [`0087f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md#insn-0087f13c)
- 新版 [`0087f134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f134) · [`0087f13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f13c) · [`0087f17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md#insn-0087f17c)

~~~diff
- 0087f0f4 ["INT_ADD", "register:40f0:8", ["const:87f0f4:8", "const:4:8"]]
- 0087f0f4 ["CALL", null, ["ram:48ccb8:8"]]
+ 0087f134 ["INT_ADD", "register:40f0:8", ["const:87f134:8", "const:4:8"]]
+ 0087f134 ["CALL", null, ["ram:48ccf8:8"]]
- 0087f0f4 bytes f136f097
+ 0087f134 bytes f136f097
- 0087f0fc ["INT_ADD", "register:40f0:8", ["const:87f0fc:8", "const:4:8"]]
- 0087f0fc ["CALL", null, ["ram:48ccb8:8"]]
+ 0087f13c ["INT_ADD", "register:40f0:8", ["const:87f13c:8", "const:4:8"]]
+ 0087f13c ["CALL", null, ["ram:48ccf8:8"]]
- 0087f0fc bytes ef36f097
+ 0087f13c bytes ef36f097
- 0087f13c ["INT_ADD", "register:40f0:8", ["const:87f13c:8", "const:4:8"]]
- 0087f13c ["CALL", null, ["callee:004928ac:8"]]
+ 0087f17c ["INT_ADD", "register:40f0:8", ["const:87f17c:8", "const:4:8"]]
+ 0087f17c ["CALL", null, ["callee:004928ac:8"]]
- 0087f13c bytes cc4df097
+ 0087f17c bytes cc4df097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2409f659c312befd8cf70ecd0f6435"></a>

### [`0087f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f228.md) → [`0087f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md) FUN_0087f268

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087f2ac",
      "incomplete_value": true,
      "site": "0087f2c0",
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
                "const:554:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f26c",
      "incomplete_value": true,
      "site": "0087f280",
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
                "const:487:8"
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
      "site": "0087f294",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f254",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0087f29c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087f25c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0087f290",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0087f294",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0087f29c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0087f290",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0087f294",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0087f29c",
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

- 旧版 [`0087f254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f228.md#insn-0087f254) · [`0087f25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f228.md#insn-0087f25c) · [`0087f29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f228.md#insn-0087f29c)
- 新版 [`0087f294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f294) · [`0087f29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f29c) · [`0087f2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f268.md#insn-0087f2dc)

~~~diff
- 0087f254 ["INT_ADD", "register:40f0:8", ["const:87f254:8", "const:4:8"]]
- 0087f254 ["CALL", null, ["ram:48ccb8:8"]]
+ 0087f294 ["INT_ADD", "register:40f0:8", ["const:87f294:8", "const:4:8"]]
+ 0087f294 ["CALL", null, ["ram:48ccf8:8"]]
- 0087f254 bytes 9936f097
+ 0087f294 bytes 9936f097
- 0087f25c ["INT_ADD", "register:40f0:8", ["const:87f25c:8", "const:4:8"]]
- 0087f25c ["CALL", null, ["ram:48ccb8:8"]]
+ 0087f29c ["INT_ADD", "register:40f0:8", ["const:87f29c:8", "const:4:8"]]
+ 0087f29c ["CALL", null, ["ram:48ccf8:8"]]
- 0087f25c bytes 9736f097
+ 0087f29c bytes 9736f097
- 0087f29c ["INT_ADD", "register:40f0:8", ["const:87f29c:8", "const:4:8"]]
- 0087f29c ["CALL", null, ["callee:004928ac:8"]]
+ 0087f2dc ["INT_ADD", "register:40f0:8", ["const:87f2dc:8", "const:4:8"]]
+ 0087f2dc ["CALL", null, ["callee:004928ac:8"]]
- 0087f29c bytes 744df097
+ 0087f2dc bytes 744df097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd470e3d069335ac46a69ca7e185a1ce"></a>

### [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) → [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) FUN_0087f368

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 55件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md)
- 新版 呼出元 0件  · 呼出先 55件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 24件, `store_value` 12件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087f430",
      "incomplete_value": false,
      "site": "0087f430",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f3f0",
      "incomplete_value": false,
      "site": "0087f3f0",
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
            "const:598:8"
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
      "definition_site": "0087f488",
      "incomplete_value": true,
      "site": "0087f488",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:8ab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f448",
      "incomplete_value": true,
      "site": "0087f448",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:86b:8"
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
      "definition_site": "0087f6b4",
      "incomplete_value": true,
      "site": "0087f6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087f674",
      "incomplete_value": true,
      "site": "0087f674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4cb:8"
              ]
            ]
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
      "0087f430",
      "DATA",
      [
        "storage",
        "00c80598",
        null,
        "undefined *"
      ]
    ],
    [
      "0087f478",
      "READ",
      [
        "storage",
        "002ba86b",
        null,
        "string"
      ]
    ],
    [
      "0087f494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14bf0"
      ]
    ]
  ],
  "added": [
    [
      "0087f430",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ],
    [
      "0087f478",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "0087f494",
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

- 旧版 [`0087f430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md#insn-0087f430) · [`0087f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md#insn-0087f454) · [`0087f47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md#insn-0087f47c)
- 新版 [`0087f470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f470) · [`0087f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f494) · [`0087f4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md#insn-0087f4bc)

~~~diff
- 0087f430 ["COPY", "tmp:0:8", ["const:86b:8"]]
- 0087f430 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087f430 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087f430 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087f470 ["COPY", "tmp:0:8", ["const:8ab:8"]]
+ 0087f470 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087f470 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087f470 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087f430 bytes 29ad2191
+ 0087f470 bytes 29ad2291
- 0087f454 ["INT_ADD", "register:40f0:8", ["const:87f454:8", "const:4:8"]]
- 0087f454 ["CALL", null, ["ram:a14bf0:8"]]
+ 0087f494 ["INT_ADD", "register:40f0:8", ["const:87f494:8", "const:4:8"]]
+ 0087f494 ["CALL", null, ["ram:a14d8c:8"]]
- 0087f454 bytes e7550694
+ 0087f494 bytes 3e560694
- 0087f47c ["INT_ADD", "register:40f0:8", ["const:87f47c:8", "const:4:8"]]
- 0087f47c ["CALL", null, ["callee:00484dfc:8"]]
+ 0087f4bc ["INT_ADD", "register:40f0:8", ["const:87f4bc:8", "const:4:8"]]
+ 0087f4bc ["CALL", null, ["callee:00484dfc:8"]]
- 0087f47c bytes 5016f097
+ 0087f4bc bytes 5016f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a18338383fbe7da7768d20c74771abc1"></a>

### [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) → [`0088018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md) FUN_0088018c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 9件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md)
- 新版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 9件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088024c",
      "incomplete_value": false,
      "site": "0088024c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088020c",
      "incomplete_value": false,
      "site": "0088020c",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008801c8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880188",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "008801d8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880198",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "008801c0",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "byte[11]"
      ]
    ],
    [
      "008801c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "008801d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "008801c0",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "dword"
      ]
    ],
    [
      "008801c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008801d8",
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

- 旧版 [`00880188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-00880188) · [`00880198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-00880198) · [`0088018c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-0088018c)
- 新版 [`008801c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801c8) · [`008801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801d8) · [`008801cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md#insn-008801cc)

~~~diff
- 00880188 ["INT_ADD", "register:40f0:8", ["const:880188:8", "const:4:8"]]
- 00880188 ["CALL", null, ["ram:48ccb8:8"]]
+ 008801c8 ["INT_ADD", "register:40f0:8", ["const:8801c8:8", "const:4:8"]]
+ 008801c8 ["CALL", null, ["ram:48ccf8:8"]]
- 00880188 bytes cc32f097
+ 008801c8 bytes cc32f097
- 00880198 ["INT_ADD", "register:40f0:8", ["const:880198:8", "const:4:8"]]
- 00880198 ["CALL", null, ["ram:48ccb8:8"]]
+ 008801d8 ["INT_ADD", "register:40f0:8", ["const:8801d8:8", "const:4:8"]]
+ 008801d8 ["CALL", null, ["ram:48ccf8:8"]]
- 00880198 bytes c832f097
+ 008801d8 bytes c832f097
- 0088018c ["INT_ADD", "register:40f0:8", ["const:88018c:8", "const:4:8"]]
- 0088018c ["CALL", null, ["callee:00492c00:8"]]
+ 008801cc ["INT_ADD", "register:40f0:8", ["const:8801cc:8", "const:4:8"]]
+ 008801cc ["CALL", null, ["callee:00492c00:8"]]
- 0088018c bytes 8d4af097
+ 008801cc bytes 8d4af097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d466bea186ba684537b32723335782"></a>

### [`00880380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md) → [`008803c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md) FUN_008803c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008803dc",
      "incomplete_value": true,
      "site": "008803e0",
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
      "definition_site": "0088039c",
      "incomplete_value": true,
      "site": "008803a0",
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
      "008803d4",
      "READ",
      [
        "storage",
        "00c9a898",
        null,
        "pointer"
      ]
    ],
    [
      "008803e0",
      "DATA",
      [
        "storage",
        "00c65198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008803d4",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ],
    [
      "008803e0",
      "DATA",
      [
        "storage",
        "00c65598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008803e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-008803e0) · [`00880394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-00880394) · [`008803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-008803b0)
- 新版 [`00880420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-00880420) · [`008803d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-008803d4) · [`008803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008803c0.md#insn-008803f0)

~~~diff
- 008803e0 ["INT_ADD", "register:40f0:8", ["const:8803e0:8", "const:4:8"]]
- 008803e0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00880420 ["INT_ADD", "register:40f0:8", ["const:880420:8", "const:4:8"]]
+ 00880420 ["CALL", null, ["callee:00c57e80:8"]]
- 008803e0 bytes a85d0f94
+ 00880420 bytes 985e0f94
- 00880394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00880394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008803d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 008803d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00880394 bytes 084d44f9
+ 008803d4 bytes 084d46f9
- 008803b0 ["INT_ADD", "register:40f0:8", ["const:8803b0:8", "const:4:8"]]
- 008803b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 008803f0 ["INT_ADD", "register:40f0:8", ["const:8803f0:8", "const:4:8"]]
+ 008803f0 ["CALL", null, ["callee:00c53d00:8"]]
- 008803b0 bytes 4c4d0f94
+ 008803f0 bytes 444e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36cb945fc77bb564b7561ddfa45bbd48"></a>

### [`008803fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md) → [`0088043c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md) FUN_0088043c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf58.md) [`0047cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf98.md) [`0047cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cfb8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008804a0",
      "incomplete_value": true,
      "site": "008804b0",
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
                "const:7a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00880460",
      "incomplete_value": true,
      "site": "00880470",
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
                "const:765:8"
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
      "definition_site": "008804b4",
      "incomplete_value": true,
      "site": "008804b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00880474",
      "incomplete_value": true,
      "site": "00880474",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088054c",
      "incomplete_value": true,
      "site": "0088055c",
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088050c",
      "incomplete_value": true,
      "site": "0088051c",
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
                "const:3f0:8"
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
      "0088046c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00880470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00880488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0088046c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00880470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00880488",
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

- 旧版 [`00880430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md#insn-00880430) · [`00880434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md#insn-00880434) · [`00880448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md#insn-00880448)
- 新版 [`00880470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880470) · [`00880474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880474) · [`00880488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088043c.md#insn-00880488)

~~~diff
- 00880430 ["INT_ADD", "register:40f0:8", ["const:880430:8", "const:4:8"]]
- 00880430 ["CALL", null, ["ram:48ccb8:8"]]
+ 00880470 ["INT_ADD", "register:40f0:8", ["const:880470:8", "const:4:8"]]
+ 00880470 ["CALL", null, ["ram:48ccf8:8"]]
- 00880430 bytes 2232f097
+ 00880470 bytes 2232f097
- 00880434 ["INT_ADD", "register:40f0:8", ["const:880434:8", "const:4:8"]]
- 00880434 ["CALL", null, ["callee:0048e7e0:8"]]
+ 00880474 ["INT_ADD", "register:40f0:8", ["const:880474:8", "const:4:8"]]
+ 00880474 ["CALL", null, ["callee:0048e7e0:8"]]
- 00880434 bytes db38f097
+ 00880474 bytes db38f097
- 00880448 ["INT_ADD", "register:40f0:8", ["const:880448:8", "const:4:8"]]
- 00880448 ["CALL", null, ["ram:48ccb8:8"]]
+ 00880488 ["INT_ADD", "register:40f0:8", ["const:880488:8", "const:4:8"]]
+ 00880488 ["CALL", null, ["ram:48ccf8:8"]]
- 00880448 bytes 1c32f097
+ 00880488 bytes 1c32f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae8eee11a158e30879129be0751dfb60"></a>

### [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) → [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) FUN_008806a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) [`008843dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008843dc.md) [`00884788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884788.md) [`00885328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885328.md) [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) · 呼出先 15件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md)
- 新版 呼出元 13件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) [`0088441c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/0088441c.md) [`008847c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/008847c8.md) [`00885368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885368.md) [`00885724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00885/00885724.md) · 呼出先 15件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00880808",
      "incomplete_value": false,
      "site": "00880810",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008807c8",
      "incomplete_value": false,
      "site": "008807d0",
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
            "const:698:8"
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
      "definition_site": "0088096c",
      "incomplete_value": false,
      "site": "00880974",
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
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088092c",
      "incomplete_value": false,
      "site": "00880934",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008806e4",
      "value": [
        "leaf",
        "ram:768bdc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008806a4",
      "value": [
        "leaf",
        "ram:768b9c:8"
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
      "008806e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768b9c"
      ]
    ],
    [
      "00880714",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:008806d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "008806e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768bdc"
      ]
    ],
    [
      "00880714",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00880718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008806a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md#insn-008806a4) · [`008806d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md#insn-008806d4) · [`008806d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md#insn-008806d8)
- 新版 [`008806e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md#insn-008806e4) · [`00880714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md#insn-00880714)

~~~diff
- 008806a4 ["INT_ADD", "register:40f0:8", ["const:8806a4:8", "const:4:8"]]
- 008806a4 ["CALL", null, ["ram:768b9c:8"]]
+ 008806e4 ["INT_ADD", "register:40f0:8", ["const:8806e4:8", "const:4:8"]]
+ 008806e4 ["CALL", null, ["ram:768bdc:8"]]
- 008806a4 bytes 3ea1fb97
+ 008806e4 bytes 3ea1fb97
- 008806d4 ["INT_ADD", "register:40f0:8", ["const:8806d4:8", "const:4:8"]]
- 008806d4 ["CALL", null, ["ram:764344:8"]]
+ 00880714 ["INT_ADD", "register:40f0:8", ["const:880714:8", "const:4:8"]]
+ 00880714 ["CALL", null, ["ram:764384:8"]]
- 008806d4 bytes 1c8ffb97
+ 00880714 bytes 1c8ffb97
- 008806d8 ["INT_ADD", "register:40f0:8", ["const:8806d8:8", "const:4:8"]]
- 008806d8 ["CALL", null, ["callee:008514f8:8"]]
- 008806d8 bytes 7843ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-450d6c71c0c7fb4daee415629808a67f"></a>

### [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) → [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) FUN_00880cf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 16件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) · 呼出先 14件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768388.md)
- 新版 呼出元 16件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) [`00883ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883ad4.md) · 呼出先 14件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007683c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007683c8.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00880e38",
      "incomplete_value": false,
      "site": "00880e38",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00880df8",
      "incomplete_value": false,
      "site": "00880df8",
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
            "const:928:8"
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
      "site": "00880d28",
      "value": [
        "leaf",
        "ram:7683c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880ce8",
      "value": [
        "leaf",
        "ram:768388:8"
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
      "site": "00880d38",
      "value": [
        "leaf",
        "ram:7685a4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00880cf8",
      "value": [
        "leaf",
        "ram:768564:8"
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
      "00880d28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768388"
      ]
    ],
    [
      "00880d38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768564"
      ]
    ],
    [
      "00880d5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ],
  "added": [
    [
      "00880d28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683c8"
      ]
    ],
    [
      "00880d38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007685a4"
      ]
    ],
    [
      "00880d5c",
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

- 旧版 [`00880ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md#insn-00880ce8) · [`00880cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md#insn-00880cf8) · [`00880d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md#insn-00880d1c)
- 新版 [`00880d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880d28) · [`00880d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880d38) · [`00880d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md#insn-00880d5c)

~~~diff
- 00880ce8 ["INT_ADD", "register:40f0:8", ["const:880ce8:8", "const:4:8"]]
- 00880ce8 ["CALL", null, ["ram:768388:8"]]
+ 00880d28 ["INT_ADD", "register:40f0:8", ["const:880d28:8", "const:4:8"]]
+ 00880d28 ["CALL", null, ["ram:7683c8:8"]]
- 00880ce8 bytes a89dfb97
+ 00880d28 bytes a89dfb97
- 00880cf8 ["INT_ADD", "register:40f0:8", ["const:880cf8:8", "const:4:8"]]
- 00880cf8 ["CALL", null, ["ram:768564:8"]]
+ 00880d38 ["INT_ADD", "register:40f0:8", ["const:880d38:8", "const:4:8"]]
+ 00880d38 ["CALL", null, ["ram:7685a4:8"]]
- 00880cf8 bytes 1b9efb97
+ 00880d38 bytes 1b9efb97
- 00880d1c ["INT_ADD", "register:40f0:8", ["const:880d1c:8", "const:4:8"]]
- 00880d1c ["CALL", null, ["ram:764344:8"]]
+ 00880d5c ["INT_ADD", "register:40f0:8", ["const:880d5c:8", "const:4:8"]]
+ 00880d5c ["CALL", null, ["ram:764384:8"]]
- 00880d1c bytes 8a8dfb97
+ 00880d5c bytes 8a8dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8c76d4f273c4788cd6b7adadc62f9a7"></a>

### [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) → [`00881098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md) FUN_00881098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0056081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`00886160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`008861a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008861a0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00881168",
      "incomplete_value": false,
      "site": "00881168",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881128",
      "incomplete_value": false,
      "site": "00881128",
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
            "const:a28:8"
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
      "00881168",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ],
    [
      "008811e8",
      "READ",
      [
        "storage",
        "00c80a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00881168",
      "DATA",
      [
        "storage",
        "00c80e28",
        null,
        "undefined *"
      ]
    ],
    [
      "008811e8",
      "READ",
      [
        "storage",
        "00c80e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md#insn-00881168) · [`0088108c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md#insn-0088108c) · [`008810c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md#insn-008810c0)
- 新版 [`008811a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-008811a8) · [`008810cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-008810cc) · [`00881100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881098.md#insn-00881100)

~~~diff
- 00881168 ["COPY", "register:0:8", ["register:4040:8"]]
- 00881168 ["INT_ADD", "register:40f0:8", ["const:881168:8", "const:4:8"]]
- 00881168 ["CALLIND", null, ["register:0:8"]]
+ 008811a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008811a8 ["INT_ADD", "register:40f0:8", ["const:8811a8:8", "const:4:8"]]
+ 008811a8 ["CALLIND", null, ["register:0:8"]]
- 00881168 bytes 00013fd6
+ 008811a8 bytes 00013fd6
- 0088108c ["INT_ADD", "register:40f0:8", ["const:88108c:8", "const:4:8"]]
- 0088108c ["CALL", null, ["callee:0056085c:8"]]
+ 008810cc ["INT_ADD", "register:40f0:8", ["const:8810cc:8", "const:4:8"]]
+ 008810cc ["CALL", null, ["callee:0056085c:8"]]
- 0088108c bytes e47df397
+ 008810cc bytes e47df397
- 008810c0 ["INT_ADD", "register:40f0:8", ["const:8810c0:8", "const:4:8"]]
- 008810c0 ["CALL", null, ["callee:0043bb20:8"]]
+ 00881100 ["INT_ADD", "register:40f0:8", ["const:881100:8", "const:4:8"]]
+ 00881100 ["CALL", null, ["callee:0043bb20:8"]]
- 008810c0 bytes 88eaee97
+ 00881100 bytes 88eaee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b8ace49e98bb78d6c6708fa1207aec"></a>

### [`00881370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md) → [`008813b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md) FUN_008813b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.95% / 新版 84.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008814a0",
      "incomplete_value": true,
      "site": "008814b0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881460",
      "incomplete_value": true,
      "site": "00881470",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:220:8"
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
      "definition_site": "008814a4",
      "incomplete_value": true,
      "site": "008814b4",
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
      "definition_site": "00881464",
      "incomplete_value": true,
      "site": "00881474",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008814a8",
      "incomplete_value": true,
      "site": "008814b8",
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
      "definition_site": "00881468",
      "incomplete_value": true,
      "site": "00881478",
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
      "008813ec",
      "READ",
      [
        "storage",
        "002ba86b",
        null,
        "string"
      ]
    ],
    [
      "008813f0",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "008813ec",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "008813f0",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881428",
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

- 旧版 [`008813e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md#insn-008813e8) · [`00881434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md#insn-00881434) · [`00881444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md#insn-00881444)
- 新版 [`00881428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881428) · [`00881474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881474) · [`00881484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/008813b0.md#insn-00881484)

~~~diff
- 008813e8 ["INT_ADD", "register:40f0:8", ["const:8813e8:8", "const:4:8"]]
- 008813e8 ["CALL", null, ["ram:48ccb8:8"]]
+ 00881428 ["INT_ADD", "register:40f0:8", ["const:881428:8", "const:4:8"]]
+ 00881428 ["CALL", null, ["ram:48ccf8:8"]]
- 008813e8 bytes 342ef097
+ 00881428 bytes 342ef097
- 00881434 ["INT_ADD", "register:40f0:8", ["const:881434:8", "const:4:8"]]
- 00881434 ["CALL", null, ["callee:008514f8:8"]]
+ 00881474 ["INT_ADD", "register:40f0:8", ["const:881474:8", "const:4:8"]]
+ 00881474 ["CALL", null, ["callee:008514f8:8"]]
- 00881434 bytes 2140ff97
+ 00881474 bytes 2140ff97
- 00881444 ["INT_ADD", "register:40f0:8", ["const:881444:8", "const:4:8"]]
- 00881444 ["CALL", null, ["ram:48ccb8:8"]]
+ 00881484 ["INT_ADD", "register:40f0:8", ["const:881484:8", "const:4:8"]]
+ 00881484 ["CALL", null, ["ram:48ccf8:8"]]
- 00881444 bytes 1d2ef097
+ 00881484 bytes 1d2ef097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00557fe7f2152cf1b6fa2d79c5fb3eb7"></a>

### [`00881544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md) → [`00881584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md) FUN_00881584

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00484210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484210.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.80% / 新版 82.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008815d0",
      "incomplete_value": true,
      "site": "008815d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:8ab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881590",
      "incomplete_value": true,
      "site": "00881590",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:86b:8"
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
      "definition_site": "00881674",
      "incomplete_value": true,
      "site": "00881684",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881634",
      "incomplete_value": true,
      "site": "00881644",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:220:8"
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
      "definition_site": "00881678",
      "incomplete_value": true,
      "site": "00881688",
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
      "definition_site": "00881638",
      "incomplete_value": true,
      "site": "00881648",
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
      "008815c0",
      "READ",
      [
        "storage",
        "002ba86b",
        null,
        "string"
      ]
    ],
    [
      "008815c4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "008815fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "008815c0",
      "READ",
      [
        "storage",
        "002ba8ab",
        null,
        "string"
      ]
    ],
    [
      "008815c4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "008815fc",
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

- 旧版 [`008815bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md#insn-008815bc) · [`00881608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md#insn-00881608) · [`00881618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md#insn-00881618)
- 新版 [`008815fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-008815fc) · [`00881648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-00881648) · [`00881658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881584.md#insn-00881658)

~~~diff
- 008815bc ["INT_ADD", "register:40f0:8", ["const:8815bc:8", "const:4:8"]]
- 008815bc ["CALL", null, ["ram:48ccb8:8"]]
+ 008815fc ["INT_ADD", "register:40f0:8", ["const:8815fc:8", "const:4:8"]]
+ 008815fc ["CALL", null, ["ram:48ccf8:8"]]
- 008815bc bytes bf2df097
+ 008815fc bytes bf2df097
- 00881608 ["INT_ADD", "register:40f0:8", ["const:881608:8", "const:4:8"]]
- 00881608 ["CALL", null, ["callee:008514f8:8"]]
+ 00881648 ["INT_ADD", "register:40f0:8", ["const:881648:8", "const:4:8"]]
+ 00881648 ["CALL", null, ["callee:008514f8:8"]]
- 00881608 bytes ac3fff97
+ 00881648 bytes ac3fff97
- 00881618 ["INT_ADD", "register:40f0:8", ["const:881618:8", "const:4:8"]]
- 00881618 ["CALL", null, ["ram:48ccb8:8"]]
+ 00881658 ["INT_ADD", "register:40f0:8", ["const:881658:8", "const:4:8"]]
+ 00881658 ["CALL", null, ["ram:48ccf8:8"]]
- 00881618 bytes a82df097
+ 00881658 bytes a82df097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361c4a1ceaa50c920fd8ed4ba3fcf4c0"></a>

### [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) → [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) FUN_00881758

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088196c",
      "incomplete_value": false,
      "site": "0088196c",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088192c",
      "incomplete_value": false,
      "site": "0088192c",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00881a3c",
      "incomplete_value": false,
      "site": "00881a40",
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
      "definition_site": "008819fc",
      "incomplete_value": false,
      "site": "00881a00",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881798",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881758",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00881794",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "008817b4",
      "READ",
      [
        "storage",
        "002a1500",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00881794",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008817b4",
      "READ",
      [
        "storage",
        "002a15cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md#insn-00881758) · [`008817dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md#insn-008817dc) · [`008818bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md#insn-008818bc)
- 新版 [`00881798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-00881798) · [`0088181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-0088181c) · [`008818fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md#insn-008818fc)

~~~diff
- 00881758 ["INT_ADD", "register:40f0:8", ["const:881758:8", "const:4:8"]]
- 00881758 ["CALL", null, ["ram:48ccb8:8"]]
+ 00881798 ["INT_ADD", "register:40f0:8", ["const:881798:8", "const:4:8"]]
+ 00881798 ["CALL", null, ["ram:48ccf8:8"]]
- 00881758 bytes 582df097
+ 00881798 bytes 582df097
- 008817dc ["INT_ADD", "register:40f0:8", ["const:8817dc:8", "const:4:8"]]
- 008817dc ["CALL", null, ["ram:48ccb8:8"]]
+ 0088181c ["INT_ADD", "register:40f0:8", ["const:88181c:8", "const:4:8"]]
+ 0088181c ["CALL", null, ["ram:48ccf8:8"]]
- 008817dc bytes 372df097
+ 0088181c bytes 372df097
- 008818bc ["INT_ADD", "register:40f0:8", ["const:8818bc:8", "const:4:8"]]
- 008818bc ["CALL", null, ["ram:48ccb8:8"]]
+ 008818fc ["INT_ADD", "register:40f0:8", ["const:8818fc:8", "const:4:8"]]
+ 008818fc ["CALL", null, ["ram:48ccf8:8"]]
- 008818bc bytes ff2cf097
+ 008818fc bytes ff2cf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cddff782c52c15ec442d86579582e33c"></a>

### [`00881c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md) → [`00881c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md) FUN_00881c7c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00881cb8",
      "incomplete_value": true,
      "site": "00881ccc",
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
                "const:554:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00881c78",
      "incomplete_value": true,
      "site": "00881c8c",
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
                "const:487:8"
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
      "site": "00881ca8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881c68",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "00881d0c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881ccc",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00881ca4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881ca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00881cb8",
      "READ",
      [
        "storage",
        "002a2487",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00881ca4",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "00881ca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00881cb8",
      "READ",
      [
        "storage",
        "002a2554",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00881c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881c68) · [`00881ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881ca8) · [`00881ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881ccc)
- 新版 [`00881ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881ca8) · [`00881ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881ce8) · [`00881d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881c7c.md#insn-00881d0c)

~~~diff
- 00881c68 ["INT_ADD", "register:40f0:8", ["const:881c68:8", "const:4:8"]]
- 00881c68 ["CALL", null, ["ram:48ccb8:8"]]
+ 00881ca8 ["INT_ADD", "register:40f0:8", ["const:881ca8:8", "const:4:8"]]
+ 00881ca8 ["CALL", null, ["ram:48ccf8:8"]]
- 00881c68 bytes 142cf097
+ 00881ca8 bytes 142cf097
- 00881ca8 ["INT_ADD", "register:40f0:8", ["const:881ca8:8", "const:4:8"]]
- 00881ca8 ["CALL", null, ["callee:004928ac:8"]]
+ 00881ce8 ["INT_ADD", "register:40f0:8", ["const:881ce8:8", "const:4:8"]]
+ 00881ce8 ["CALL", null, ["callee:004928ac:8"]]
- 00881ca8 bytes f142f097
+ 00881ce8 bytes f142f097
- 00881ccc ["INT_ADD", "register:40f0:8", ["const:881ccc:8", "const:4:8"]]
- 00881ccc ["CALL", null, ["ram:48ccb8:8"]]
+ 00881d0c ["INT_ADD", "register:40f0:8", ["const:881d0c:8", "const:4:8"]]
+ 00881d0c ["CALL", null, ["ram:48ccf8:8"]]
- 00881ccc bytes fb2bf097
+ 00881d0c bytes fb2bf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29655893e04228de92abfec26c4f9c8e"></a>

### [`00882130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md) → [`00882170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md) FUN_00882170

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086d63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d63c.md) · 呼出先 5件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0086d67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d67c.md) · 呼出先 5件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

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
      "site": "008821e8",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008821a8",
      "value": [
        "leaf",
        "ram:764ea0:8"
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
      "008821e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "008821e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008821a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md#insn-008821a8) · [`00882150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md#insn-00882150) · [`00882164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md#insn-00882164)
- 新版 [`008821e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-008821e8) · [`00882190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-00882190) · [`008821a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882170.md#insn-008821a4)

~~~diff
- 008821a8 ["INT_ADD", "register:40f0:8", ["const:8821a8:8", "const:4:8"]]
- 008821a8 ["CALL", null, ["ram:764ea0:8"]]
+ 008821e8 ["INT_ADD", "register:40f0:8", ["const:8821e8:8", "const:4:8"]]
+ 008821e8 ["CALL", null, ["ram:764ee0:8"]]
- 008821a8 bytes 3e8bfb97
+ 008821e8 bytes 3e8bfb97
- 00882150 ["INT_ADD", "register:40f0:8", ["const:882150:8", "const:4:8"]]
- 00882150 ["CALL", null, ["callee:008514f8:8"]]
+ 00882190 ["INT_ADD", "register:40f0:8", ["const:882190:8", "const:4:8"]]
+ 00882190 ["CALL", null, ["callee:008514f8:8"]]
- 00882150 bytes da3cff97
+ 00882190 bytes da3cff97
- 00882164 ["INT_ADD", "register:40f0:8", ["const:882164:8", "const:4:8"]]
- 00882164 ["CALL", null, ["callee:008514f8:8"]]
+ 008821a4 ["INT_ADD", "register:40f0:8", ["const:8821a4:8", "const:4:8"]]
+ 008821a4 ["CALL", null, ["callee:008514f8:8"]]
- 00882164 bytes d53cff97
+ 008821a4 bytes d53cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935d282cc7b6aa1bba5c740d14df49fe"></a>

### [`00882400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882400.md) → [`00882440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882440.md) FUN_00882440

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
      "definition_site": "0088244c",
      "incomplete_value": false,
      "site": "00882458",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088240c",
      "incomplete_value": false,
      "site": "00882418",
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
      "00882458",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882458",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882400.md#insn-0088240c)
- 新版 [`0088244c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/00882440.md#insn-0088244c)

~~~diff
- 0088240c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0088240c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0088240c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0088240c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0088244c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 0088244c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0088244c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0088244c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0088240c bytes 4a610c91
+ 0088244c bytes 4a611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

