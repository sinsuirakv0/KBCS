# v16.0.0 → v16.0.1 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-6e676c94e6a1017dd77089d6711445ca"></a>

### [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) → [`00577318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md) FUN_00577318

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c4.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md)
- 新版 呼出元 1件 [`00550a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a04.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577454",
      "incomplete_value": false,
      "site": "0057745c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577414",
      "incomplete_value": false,
      "site": "0057741c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "0057746c",
      "incomplete_value": false,
      "site": "0057746c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057742c",
      "incomplete_value": false,
      "site": "0057742c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577518",
      "incomplete_value": true,
      "site": "00577518",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005774d8",
      "incomplete_value": true,
      "site": "005774d8",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00577380",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "0057745c",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "0057746c",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577380",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "0057745c",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "0057746c",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md#insn-00577424) · [`005774d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md#insn-005774d8) · [`00577320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md#insn-00577320)
- 新版 [`00577464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577464) · [`00577518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577518) · [`00577360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577318.md#insn-00577360)

~~~diff
- 00577424 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00577424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00577464 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00577464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00577464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00577464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577424 bytes 08811d91
+ 00577464 bytes 08812d91
- 005774d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 005774d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 00577518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005774d8 bytes 093907f9
+ 00577518 bytes 093901f9
- 00577320 ["INT_ADD", "register:40f0:8", ["const:577320:8", "const:4:8"]]
- 00577320 ["CALL", null, ["callee:00588e6c:8"]]
+ 00577360 ["INT_ADD", "register:40f0:8", ["const:577360:8", "const:4:8"]]
+ 00577360 ["CALL", null, ["callee:00588e6c:8"]]
- 00577320 bytes c3460094
+ 00577360 bytes c3460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dda6f2c78705a33984abaa34c3c623f"></a>

### [`00577638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577638.md) → [`00577678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md) FUN_00577678

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005777ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005777ac.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`005777ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005777ec.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577698",
      "incomplete_value": false,
      "site": "00577698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577658",
      "incomplete_value": false,
      "site": "00577658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "00577698",
      "DATA",
      [
        "storage",
        "00c6b7e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00577698",
      "DATA",
      [
        "storage",
        "00c6bbe8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577638.md#insn-00577698) · [`00577650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577638.md#insn-00577650) · [`00577654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577638.md#insn-00577654)
- 新版 [`005776d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md#insn-005776d8) · [`00577690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577678.md#insn-00577690)

~~~diff
- 00577698 ["INT_ADD", "register:40f0:8", ["const:577698:8", "const:4:8"]]
- 00577698 ["CALL", null, ["callee:0043bb20:8"]]
+ 005776d8 ["INT_ADD", "register:40f0:8", ["const:5776d8:8", "const:4:8"]]
+ 005776d8 ["CALL", null, ["callee:0043bb20:8"]]
- 00577698 bytes 1211fb97
+ 005776d8 bytes 1211fb97
- 00577650 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 00577650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00577650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00577650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00577690 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00577690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00577690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00577690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00577650 bytes 08a11f91
+ 00577690 bytes 08a12f91
- 00577654 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00577654 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ea779729470ad7782aad469be61d35"></a>

### [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) → [`005778e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md) FUN_005778e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) [`0057710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md) [`0057714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/0057714c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577a20",
      "incomplete_value": false,
      "site": "00577a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005779e0",
      "incomplete_value": false,
      "site": "005779e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577ae4",
      "incomplete_value": true,
      "site": "00577ae4",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577aa4",
      "incomplete_value": true,
      "site": "00577aa4",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00577ae0",
      "incomplete_value": true,
      "site": "00577ae0",
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
      "definition_site": "00577aa0",
      "incomplete_value": true,
      "site": "00577aa0",
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
      "0057794c",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "00577a28",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577a38",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057794c",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "00577a28",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577a38",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md#insn-00577aa4) · [`005778ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md#insn-005778ec) · [`005778f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md#insn-005778f4)
- 新版 [`00577ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-00577ae4) · [`0057792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-0057792c) · [`00577934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/005778e0.md#insn-00577934)

~~~diff
- 00577aa4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00577aa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 00577ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577aa4 bytes 093907f9
+ 00577ae4 bytes 093901f9
- 005778ec ["INT_ADD", "register:40f0:8", ["const:5778ec:8", "const:4:8"]]
- 005778ec ["CALL", null, ["callee:00588e6c:8"]]
+ 0057792c ["INT_ADD", "register:40f0:8", ["const:57792c:8", "const:4:8"]]
+ 0057792c ["CALL", null, ["callee:00588e6c:8"]]
- 005778ec bytes 50450094
+ 0057792c bytes 50450094
- 005778f4 ["INT_ADD", "register:40f0:8", ["const:5778f4:8", "const:4:8"]]
- 005778f4 ["CALL", null, ["callee:0058915c:8"]]
+ 00577934 ["INT_ADD", "register:40f0:8", ["const:577934:8", "const:4:8"]]
+ 00577934 ["CALL", null, ["callee:0058915c:8"]]
- 005778f4 bytes 0a460094
+ 00577934 bytes 0a460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fea325dd65e6fa2cd99ec225f544d95a"></a>

### [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) → [`00577c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md) FUN_00577c80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/0057699c.md) [`00576f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/00576f08.md) [`00577080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577080.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577dd8",
      "incomplete_value": false,
      "site": "00577dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577d98",
      "incomplete_value": false,
      "site": "00577d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577e84",
      "incomplete_value": true,
      "site": "00577e84",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577e44",
      "incomplete_value": true,
      "site": "00577e44",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00577e80",
      "incomplete_value": true,
      "site": "00577e80",
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
      "definition_site": "00577e40",
      "incomplete_value": true,
      "site": "00577e40",
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
      "00577cec",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "00577dc8",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577dd8",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577cec",
      "READ",
      [
        "storage",
        "002ba437",
        null,
        "string"
      ]
    ],
    [
      "00577dc8",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577dd8",
      "DATA",
      [
        "storage",
        "00c6bb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md#insn-00577d58) · [`00577e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md#insn-00577e44) · [`00577c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md#insn-00577c8c)
- 新版 [`00577d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577d98) · [`00577e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577e84) · [`00577ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00577/00577c80.md#insn-00577ccc)

~~~diff
- 00577d58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577d58 ["INT_ADD", "register:40f0:8", ["const:577d58:8", "const:4:8"]]
- 00577d58 ["CALLIND", null, ["register:0:8"]]
+ 00577d98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00577d98 ["INT_ADD", "register:40f0:8", ["const:577d98:8", "const:4:8"]]
+ 00577d98 ["CALLIND", null, ["register:0:8"]]
- 00577d58 bytes 00013fd6
+ 00577d98 bytes 00013fd6
- 00577e44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00577e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577e84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 00577e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577e44 bytes 093907f9
+ 00577e84 bytes 093901f9
- 00577c8c ["INT_ADD", "register:40f0:8", ["const:577c8c:8", "const:4:8"]]
- 00577c8c ["CALL", null, ["callee:00588e6c:8"]]
+ 00577ccc ["INT_ADD", "register:40f0:8", ["const:577ccc:8", "const:4:8"]]
+ 00577ccc ["CALL", null, ["callee:00588e6c:8"]]
- 00577c8c bytes 68440094
+ 00577ccc bytes 68440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad3568825ffad5e23baf7324bed02bf"></a>

### [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) → [`00578020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md) FUN_00578020

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00578184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005781c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/005781c4.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057c220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c220.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057804c",
      "incomplete_value": false,
      "site": "00578050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057800c",
      "incomplete_value": false,
      "site": "00578010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00578050",
      "DATA",
      [
        "storage",
        "00c6b808",
        null,
        "undefined *"
      ]
    ],
    [
      "00578074",
      "READ",
      [
        "storage",
        "002a31ee",
        null,
        "string"
      ]
    ],
    [
      "00578114",
      "PARAM",
      [
        "storage",
        "00ca5e70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578050",
      "DATA",
      [
        "storage",
        "00c6bc08",
        null,
        "undefined *"
      ]
    ],
    [
      "00578074",
      "READ",
      [
        "storage",
        "002a32bb",
        null,
        "string"
      ]
    ],
    [
      "00578114",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057800c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md#insn-0057800c) · [`00578014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md#insn-00578014) · [`0057801c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md#insn-0057801c)
- 新版 [`0057804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-0057804c) · [`00578054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-00578054) · [`0057805c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578020.md#insn-0057805c)

~~~diff
- 0057800c ["COPY", "tmp:0:8", ["const:808:8"]]
- 0057800c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057800c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057800c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057804c ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 0057804c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057804c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057804c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057800c bytes 08212091
+ 0057804c bytes 08213091
- 00578014 ["INT_ADD", "register:40f0:8", ["const:578014:8", "const:4:8"]]
- 00578014 ["CALL", null, ["callee:00588e6c:8"]]
+ 00578054 ["INT_ADD", "register:40f0:8", ["const:578054:8", "const:4:8"]]
+ 00578054 ["CALL", null, ["callee:00588e6c:8"]]
- 00578014 bytes 86430094
+ 00578054 bytes 86430094
- 0057801c ["INT_ADD", "register:40f0:8", ["const:57801c:8", "const:4:8"]]
- 0057801c ["CALL", null, ["callee:0058915c:8"]]
+ 0057805c ["INT_ADD", "register:40f0:8", ["const:57805c:8", "const:4:8"]]
+ 0057805c ["CALL", null, ["callee:0058915c:8"]]
- 0057801c bytes 40440094
+ 0057805c bytes 40440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8c65ddf61e95a6e47b0b776248561d"></a>

### [`0057831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/0057831c.md) → [`0057835c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md) FUN_0057835c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005783c8",
      "incomplete_value": true,
      "site": "005783c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:8b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578388",
      "incomplete_value": true,
      "site": "00578388",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:876:8"
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
      "definition_site": "005783e0",
      "incomplete_value": true,
      "site": "005783f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005783a0",
      "incomplete_value": true,
      "site": "005783b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:198:8"
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
      "definition_site": "005783f4",
      "incomplete_value": true,
      "site": "005783f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005783b4",
      "incomplete_value": true,
      "site": "005783b4",
      "value": [
        "LOAD",
        "8",
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
      "005783b4",
      "READ",
      [
        "storage",
        "002ad876",
        null,
        "string"
      ]
    ],
    [
      "005783e0",
      "READ",
      [
        "storage",
        "002b6198",
        null,
        "string"
      ]
    ],
    [
      "005783e4",
      "READ",
      [
        "storage",
        "002b61a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005783b4",
      "READ",
      [
        "storage",
        "002ad8b6",
        null,
        "string"
      ]
    ],
    [
      "005783e0",
      "READ",
      [
        "storage",
        "002b61d8",
        null,
        "string"
      ]
    ],
    [
      "005783e4",
      "READ",
      [
        "storage",
        "002b61e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005783f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/0057831c.md#insn-005783f4) · [`00578414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/0057831c.md#insn-00578414) · [`0057846c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/0057831c.md#insn-0057846c)
- 新版 [`00578434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-00578434) · [`00578454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-00578454) · [`005784ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/0057835c.md#insn-005784ac)

~~~diff
- 005783f4 ["INT_ADD", "register:40f0:8", ["const:5783f4:8", "const:4:8"]]
- 005783f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00578434 ["INT_ADD", "register:40f0:8", ["const:578434:8", "const:4:8"]]
+ 00578434 ["CALL", null, ["callee:00c57eb0:8"]]
- 005783f4 bytes af7d1b94
+ 00578434 bytes 9f7e1b94
- 00578414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 00578414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
+ 00578454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
+ 00578454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 00578414 bytes 16690eb9
+ 00578454 bytes 166902b9
- 0057846c ["INT_ADD", "register:40f0:8", ["const:57846c:8", "const:4:8"]]
- 0057846c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005784ac ["INT_ADD", "register:40f0:8", ["const:5784ac:8", "const:4:8"]]
+ 005784ac ["CALL", null, ["callee:00c57eb0:8"]]
- 0057846c bytes 917d1b94
+ 005784ac bytes 817e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f67434864079c1fc5f3bdab861cb349"></a>

### [`00578750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578750.md) → [`00578790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md) FUN_00578790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005787ec",
      "incomplete_value": true,
      "site": "005787ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005787ac",
      "incomplete_value": true,
      "site": "005787ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:876:8"
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
      "definition_site": "00578800",
      "incomplete_value": true,
      "site": "00578808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005787c0",
      "incomplete_value": true,
      "site": "005787c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e7:8"
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
      "definition_site": "0057880c",
      "incomplete_value": true,
      "site": "0057880c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005787cc",
      "incomplete_value": true,
      "site": "005787cc",
      "value": [
        "LOAD",
        "8",
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
      "005787dc",
      "READ",
      [
        "storage",
        "002ad876",
        null,
        "string"
      ]
    ],
    [
      "00578800",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ],
    [
      "00578804",
      "READ",
      [
        "storage",
        "002a66f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005787dc",
      "READ",
      [
        "storage",
        "002ad8b6",
        null,
        "string"
      ]
    ],
    [
      "00578800",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ],
    [
      "00578804",
      "READ",
      [
        "storage",
        "002a67d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578750.md#insn-00578808) · [`00578778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578750.md#insn-00578778) · [`00578780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578750.md#insn-00578780)
- 新版 [`00578848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-00578848) · [`005787b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-005787b8) · [`005787c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-005787c0)

~~~diff
- 00578808 ["INT_ADD", "register:40f0:8", ["const:578808:8", "const:4:8"]]
- 00578808 ["CALL", null, ["callee:00589144:8"]]
+ 00578848 ["INT_ADD", "register:40f0:8", ["const:578848:8", "const:4:8"]]
+ 00578848 ["CALL", null, ["callee:00589144:8"]]
- 00578808 bytes 3f420094
+ 00578848 bytes 3f420094
- 00578778 ["INT_ADD", "register:40f0:8", ["const:578778:8", "const:4:8"]]
- 00578778 ["CALL", null, ["callee:00588e6c:8"]]
+ 005787b8 ["INT_ADD", "register:40f0:8", ["const:5787b8:8", "const:4:8"]]
+ 005787b8 ["CALL", null, ["callee:00588e6c:8"]]
- 00578778 bytes ad410094
+ 005787b8 bytes ad410094
- 00578780 ["INT_ADD", "register:40f0:8", ["const:578780:8", "const:4:8"]]
- 00578780 ["CALL", null, ["callee:0058915c:8"]]
+ 005787c0 ["INT_ADD", "register:40f0:8", ["const:5787c0:8", "const:4:8"]]
+ 005787c0 ["CALL", null, ["callee:0058915c:8"]]
- 00578780 bytes 67420094
+ 005787c0 bytes 67420094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c8d370b43ff671f35449f15246cb299"></a>

### [`005788d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md) → [`00578910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md) FUN_00578910

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578968",
      "incomplete_value": true,
      "site": "00578968",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578928",
      "incomplete_value": true,
      "site": "00578928",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:594:8"
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
      "definition_site": "00578970",
      "incomplete_value": true,
      "site": "00578970",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578930",
      "incomplete_value": true,
      "site": "00578930",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057896c",
      "incomplete_value": true,
      "site": "00578980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057892c",
      "incomplete_value": true,
      "site": "00578940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b0:8"
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
      "00578950",
      "READ",
      [
        "storage",
        "002ab594",
        null,
        "string"
      ]
    ],
    [
      "00578958",
      "READ",
      [
        "storage",
        "002ab599",
        null,
        "string"
      ]
    ],
    [
      "0057896c",
      "READ",
      [
        "storage",
        "002b61b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578950",
      "READ",
      [
        "storage",
        "002ab5d4",
        null,
        "string"
      ]
    ],
    [
      "00578958",
      "READ",
      [
        "storage",
        "002ab5d9",
        null,
        "string"
      ]
    ],
    [
      "0057896c",
      "READ",
      [
        "storage",
        "002b61f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md#insn-00578900) · [`00578984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md#insn-00578984) · [`005788f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md#insn-005788f8)
- 新版 [`00578940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-00578940) · [`005789c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-005789c4) · [`00578938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-00578938)

~~~diff
- 00578900 ["INT_ADD", "register:40f0:8", ["const:578900:8", "const:4:8"]]
- 00578900 ["CALL", null, ["callee:0058915c:8"]]
+ 00578940 ["INT_ADD", "register:40f0:8", ["const:578940:8", "const:4:8"]]
+ 00578940 ["CALL", null, ["callee:0058915c:8"]]
- 00578900 bytes 07420094
+ 00578940 bytes 07420094
- 00578984 ["INT_ADD", "register:40f0:8", ["const:578984:8", "const:4:8"]]
- 00578984 ["CALL", null, ["callee:00589144:8"]]
+ 005789c4 ["INT_ADD", "register:40f0:8", ["const:5789c4:8", "const:4:8"]]
+ 005789c4 ["CALL", null, ["callee:00589144:8"]]
- 00578984 bytes e0410094
+ 005789c4 bytes e0410094
- 005788f8 ["INT_ADD", "register:40f0:8", ["const:5788f8:8", "const:4:8"]]
- 005788f8 ["CALL", null, ["callee:00588e6c:8"]]
+ 00578938 ["INT_ADD", "register:40f0:8", ["const:578938:8", "const:4:8"]]
+ 00578938 ["CALL", null, ["callee:00588e6c:8"]]
- 005788f8 bytes 4d410094
+ 00578938 bytes 4d410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a066e30874e10d2d4416680773754f73"></a>

### [`00578a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578a6c.md) → [`00578aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md) FUN_00578aac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578af8",
      "incomplete_value": true,
      "site": "00578af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578ab8",
      "incomplete_value": true,
      "site": "00578ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb5:8"
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
      "definition_site": "00578afc",
      "incomplete_value": true,
      "site": "00578afc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578abc",
      "incomplete_value": true,
      "site": "00578abc",
      "value": [
        "LOAD",
        "8",
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
      "00578ae8",
      "READ",
      [
        "storage",
        "002a8cb5",
        null,
        "string"
      ]
    ],
    [
      "00578af0",
      "READ",
      [
        "storage",
        "002a8cba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578ae8",
      "READ",
      [
        "storage",
        "002a8d82",
        null,
        "string"
      ]
    ],
    [
      "00578af0",
      "READ",
      [
        "storage",
        "002a8d87",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578a6c.md#insn-00578af8) · [`00578a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578a6c.md#insn-00578a90) · [`00578a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578a6c.md#insn-00578a98)
- 新版 [`00578b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578b38) · [`00578ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578ad0) · [`00578ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578ad8)

~~~diff
- 00578af8 ["INT_ADD", "register:40f0:8", ["const:578af8:8", "const:4:8"]]
- 00578af8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00578b38 ["INT_ADD", "register:40f0:8", ["const:578b38:8", "const:4:8"]]
+ 00578b38 ["CALL", null, ["callee:00c57eb0:8"]]
- 00578af8 bytes ee7b1b94
+ 00578b38 bytes de7c1b94
- 00578a90 ["INT_ADD", "register:40f0:8", ["const:578a90:8", "const:4:8"]]
- 00578a90 ["CALL", null, ["callee:00588e6c:8"]]
+ 00578ad0 ["INT_ADD", "register:40f0:8", ["const:578ad0:8", "const:4:8"]]
+ 00578ad0 ["CALL", null, ["callee:00588e6c:8"]]
- 00578a90 bytes e7400094
+ 00578ad0 bytes e7400094
- 00578a98 ["INT_ADD", "register:40f0:8", ["const:578a98:8", "const:4:8"]]
- 00578a98 ["CALL", null, ["callee:0058915c:8"]]
+ 00578ad8 ["INT_ADD", "register:40f0:8", ["const:578ad8:8", "const:4:8"]]
+ 00578ad8 ["CALL", null, ["callee:0058915c:8"]]
- 00578a98 bytes a1410094
+ 00578ad8 bytes a1410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dee80aa445ca584dd6c3e668d76aff07"></a>

### [`00578b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578b9c.md) → [`00578bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md) FUN_00578bdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578c28",
      "incomplete_value": true,
      "site": "00578c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578be8",
      "incomplete_value": true,
      "site": "00578be8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
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
      "definition_site": "00578c2c",
      "incomplete_value": true,
      "site": "00578c2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578bec",
      "incomplete_value": true,
      "site": "00578bec",
      "value": [
        "LOAD",
        "8",
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
      "00578c18",
      "READ",
      [
        "storage",
        "002b0d20",
        null,
        "string"
      ]
    ],
    [
      "00578c20",
      "READ",
      [
        "storage",
        "002b0d25",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578c18",
      "READ",
      [
        "storage",
        "002b0d60",
        null,
        "string"
      ]
    ],
    [
      "00578c20",
      "READ",
      [
        "storage",
        "002b0d65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578b9c.md#insn-00578c28) · [`00578bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578b9c.md#insn-00578bc0) · [`00578bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578b9c.md#insn-00578bc8)
- 新版 [`00578c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c68) · [`00578c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c00) · [`00578c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c08)

~~~diff
- 00578c28 ["INT_ADD", "register:40f0:8", ["const:578c28:8", "const:4:8"]]
- 00578c28 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00578c68 ["INT_ADD", "register:40f0:8", ["const:578c68:8", "const:4:8"]]
+ 00578c68 ["CALL", null, ["callee:00c57eb0:8"]]
- 00578c28 bytes a27b1b94
+ 00578c68 bytes 927c1b94
- 00578bc0 ["INT_ADD", "register:40f0:8", ["const:578bc0:8", "const:4:8"]]
- 00578bc0 ["CALL", null, ["callee:00588e6c:8"]]
+ 00578c00 ["INT_ADD", "register:40f0:8", ["const:578c00:8", "const:4:8"]]
+ 00578c00 ["CALL", null, ["callee:00588e6c:8"]]
- 00578bc0 bytes 9b400094
+ 00578c00 bytes 9b400094
- 00578bc8 ["INT_ADD", "register:40f0:8", ["const:578bc8:8", "const:4:8"]]
- 00578bc8 ["CALL", null, ["callee:0058915c:8"]]
+ 00578c08 ["INT_ADD", "register:40f0:8", ["const:578c08:8", "const:4:8"]]
+ 00578c08 ["CALL", null, ["callee:0058915c:8"]]
- 00578bc8 bytes 55410094
+ 00578c08 bytes 55410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8df04e2fc454996b27e46136ff76590b"></a>

### [`00578d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578d0c.md) → [`00578d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md) FUN_00578d4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578d98",
      "incomplete_value": true,
      "site": "00578d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cde:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578d58",
      "incomplete_value": true,
      "site": "00578d58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9e:8"
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
      "definition_site": "00578d9c",
      "incomplete_value": true,
      "site": "00578d9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578d5c",
      "incomplete_value": true,
      "site": "00578d5c",
      "value": [
        "LOAD",
        "8",
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
      "00578d88",
      "READ",
      [
        "storage",
        "002b3c9e",
        null,
        "string"
      ]
    ],
    [
      "00578d90",
      "READ",
      [
        "storage",
        "002b3ca3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578d88",
      "READ",
      [
        "storage",
        "002b3cde",
        null,
        "string"
      ]
    ],
    [
      "00578d90",
      "READ",
      [
        "storage",
        "002b3ce3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578d0c.md#insn-00578d98) · [`00578d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578d0c.md#insn-00578d30) · [`00578d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578d0c.md#insn-00578d38)
- 新版 [`00578dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578dd8) · [`00578d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578d70) · [`00578d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578d78)

~~~diff
- 00578d98 ["INT_ADD", "register:40f0:8", ["const:578d98:8", "const:4:8"]]
- 00578d98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00578dd8 ["INT_ADD", "register:40f0:8", ["const:578dd8:8", "const:4:8"]]
+ 00578dd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00578d98 bytes 467b1b94
+ 00578dd8 bytes 367c1b94
- 00578d30 ["INT_ADD", "register:40f0:8", ["const:578d30:8", "const:4:8"]]
- 00578d30 ["CALL", null, ["callee:00588e6c:8"]]
+ 00578d70 ["INT_ADD", "register:40f0:8", ["const:578d70:8", "const:4:8"]]
+ 00578d70 ["CALL", null, ["callee:00588e6c:8"]]
- 00578d30 bytes 3f400094
+ 00578d70 bytes 3f400094
- 00578d38 ["INT_ADD", "register:40f0:8", ["const:578d38:8", "const:4:8"]]
- 00578d38 ["CALL", null, ["callee:0058915c:8"]]
+ 00578d78 ["INT_ADD", "register:40f0:8", ["const:578d78:8", "const:4:8"]]
+ 00578d78 ["CALL", null, ["callee:0058915c:8"]]
- 00578d38 bytes f9400094
+ 00578d78 bytes f9400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df5b39b370422fa9f1e8e2756b9b691"></a>

### [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) → [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) FUN_00578ebc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057901c",
      "incomplete_value": true,
      "site": "0057901c",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578fdc",
      "incomplete_value": true,
      "site": "00578fdc",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579290",
      "incomplete_value": true,
      "site": "00579290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579250",
      "incomplete_value": true,
      "site": "00579250",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:882:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579294",
      "incomplete_value": true,
      "site": "00579294",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579254",
      "incomplete_value": true,
      "site": "00579254",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00578f98",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00578ffc",
      "DATA",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "0057900c",
      "WRITE",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578f98",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "00578ffc",
      "DATA",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057900c",
      "WRITE",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md#insn-00578fdc) · [`00578ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md#insn-00578ed8)
- 新版 [`0057901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md#insn-0057901c) · [`0057927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md#insn-0057927c) · [`00578f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md#insn-00578f18)

~~~diff
- 00578fdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
- 00578fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057901c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
+ 0057901c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00578fdc bytes 091d07f9
+ 0057901c bytes 091d01f9
+ 0057927c ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 0057927c bytes f60300aa
- 00578ed8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00578ed8 ["INT_ADD", "register:40f0:8", ["const:578ed8:8", "const:4:8"]]
- 00578ed8 ["CALLIND", null, ["register:0:8"]]
+ 00578f18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00578f18 ["INT_ADD", "register:40f0:8", ["const:578f18:8", "const:4:8"]]
+ 00578f18 ["CALLIND", null, ["register:0:8"]]
- 00578ed8 bytes 20013fd6
+ 00578f18 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9f4d1ec68e411817c6ecd462f17d5c"></a>

### [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) → [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) FUN_00579524

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md)
- 新版 呼出元 1件 [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00579660",
      "incomplete_value": false,
      "site": "00579668",
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
            "const:1eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579620",
      "incomplete_value": false,
      "site": "00579628",
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
            "const:11e:8"
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
      "definition_site": "005796c4",
      "incomplete_value": false,
      "site": "005796cc",
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
            "const:d6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579684",
      "incomplete_value": false,
      "site": "0057968c",
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
            "const:d2e:8"
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
      "definition_site": "00579728",
      "incomplete_value": false,
      "site": "00579730",
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
            "const:5e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005796e8",
      "incomplete_value": false,
      "site": "005796f0",
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
            "const:5a2:8"
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
      "00579660",
      "PARAM",
      [
        "storage",
        "002a011e",
        null,
        "string"
      ]
    ],
    [
      "005796c4",
      "PARAM",
      [
        "storage",
        "002b0d2e",
        null,
        "string"
      ]
    ],
    [
      "00579728",
      "PARAM",
      [
        "storage",
        "002ab5a2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00579660",
      "PARAM",
      [
        "storage",
        "002a01eb",
        null,
        "string"
      ]
    ],
    [
      "005796c4",
      "PARAM",
      [
        "storage",
        "002b0d6e",
        null,
        "string"
      ]
    ],
    [
      "00579728",
      "PARAM",
      [
        "storage",
        "002ab5e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md#insn-00579628) · [`0057968c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md#insn-0057968c) · [`005796f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md#insn-005796f0)
- 新版 [`00579668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-00579668) · [`005796cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-005796cc) · [`00579730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-00579730)

~~~diff
- 00579628 ["INT_ADD", "register:40f0:8", ["const:579628:8", "const:4:8"]]
- 00579628 ["CALL", null, ["callee:00c57f70:8"]]
+ 00579668 ["INT_ADD", "register:40f0:8", ["const:579668:8", "const:4:8"]]
+ 00579668 ["CALL", null, ["callee:00c57f70:8"]]
- 00579628 bytes 52791b94
+ 00579668 bytes 427a1b94
- 0057968c ["INT_ADD", "register:40f0:8", ["const:57968c:8", "const:4:8"]]
- 0057968c ["CALL", null, ["callee:00c57f70:8"]]
+ 005796cc ["INT_ADD", "register:40f0:8", ["const:5796cc:8", "const:4:8"]]
+ 005796cc ["CALL", null, ["callee:00c57f70:8"]]
- 0057968c bytes 39791b94
+ 005796cc bytes 297a1b94
- 005796f0 ["INT_ADD", "register:40f0:8", ["const:5796f0:8", "const:4:8"]]
- 005796f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00579730 ["INT_ADD", "register:40f0:8", ["const:579730:8", "const:4:8"]]
+ 00579730 ["CALL", null, ["callee:00c57f70:8"]]
- 005796f0 bytes 20791b94
+ 00579730 bytes 107a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803e6b5c2415ccd65f7dabd3f1a95d6a"></a>

### [`00579a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/00579a8c.md) → [`00579acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md) FUN_00579acc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00579c28",
      "incomplete_value": true,
      "site": "00579c28",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579be8",
      "incomplete_value": true,
      "site": "00579be8",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579dc8",
      "incomplete_value": true,
      "site": "00579dc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579d88",
      "incomplete_value": true,
      "site": "00579d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:882:8"
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
      "definition_site": "00579dd0",
      "incomplete_value": true,
      "site": "00579dd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579d90",
      "incomplete_value": true,
      "site": "00579d90",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00579ba4",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c08",
      "DATA",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c18",
      "WRITE",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00579ba4",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c08",
      "DATA",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c18",
      "WRITE",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/00579a8c.md#insn-00579be8) · [`00579d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/00579a8c.md#insn-00579d60) · [`00579de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/00579a8c.md#insn-00579de4)
- 新版 [`00579c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579c28) · [`00579da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579da0) · [`00579e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579e24)

~~~diff
- 00579be8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
- 00579be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00579c28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
+ 00579c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00579be8 bytes 091d07f9
+ 00579c28 bytes 091d01f9
- 00579d60 ["INT_ADD", "register:40f0:8", ["const:579d60:8", "const:4:8"]]
- 00579d60 ["CALL", null, ["callee:0058915c:8"]]
+ 00579da0 ["INT_ADD", "register:40f0:8", ["const:579da0:8", "const:4:8"]]
+ 00579da0 ["CALL", null, ["callee:0058915c:8"]]
- 00579d60 bytes ef3c0094
+ 00579da0 bytes ef3c0094
- 00579de4 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00579de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00579de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00579de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00579e24 ["COPY", "tmp:0:8", ["const:1d5:8"]]
+ 00579e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00579e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00579e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00579de4 bytes 29210491
+ 00579e24 bytes 29550791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a209c144baf38b5583f989285f497099"></a>

### [`0057a0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a0fc.md) → [`0057a13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md) FUN_0057a13c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a1a0",
      "incomplete_value": true,
      "site": "0057a1a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a160",
      "incomplete_value": true,
      "site": "0057a160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cac:8"
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
      "definition_site": "0057a1a4",
      "incomplete_value": true,
      "site": "0057a1a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a164",
      "incomplete_value": true,
      "site": "0057a164",
      "value": [
        "LOAD",
        "8",
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
      "0057a190",
      "READ",
      [
        "storage",
        "002b3cac",
        null,
        "string"
      ]
    ],
    [
      "0057a198",
      "READ",
      [
        "storage",
        "002b3cb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a190",
      "READ",
      [
        "storage",
        "002b3cec",
        null,
        "string"
      ]
    ],
    [
      "0057a198",
      "READ",
      [
        "storage",
        "002b3cf1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a0fc.md#insn-0057a138) · [`0057a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a0fc.md#insn-0057a140) · [`0057a14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a0fc.md#insn-0057a14c)
- 新版 [`0057a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a178) · [`0057a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a180) · [`0057a18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a18c)

~~~diff
- 0057a138 ["INT_ADD", "register:40f0:8", ["const:57a138:8", "const:4:8"]]
- 0057a138 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057a178 ["INT_ADD", "register:40f0:8", ["const:57a178:8", "const:4:8"]]
+ 0057a178 ["CALL", null, ["callee:00588e6c:8"]]
- 0057a138 bytes 3d3b0094
+ 0057a178 bytes 3d3b0094
- 0057a140 ["INT_ADD", "register:40f0:8", ["const:57a140:8", "const:4:8"]]
- 0057a140 ["CALL", null, ["callee:0058915c:8"]]
+ 0057a180 ["INT_ADD", "register:40f0:8", ["const:57a180:8", "const:4:8"]]
+ 0057a180 ["CALL", null, ["callee:0058915c:8"]]
- 0057a140 bytes f73b0094
+ 0057a180 bytes f73b0094
- 0057a14c ["COPY", "tmp:0:8", ["const:cac:8"]]
- 0057a14c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a14c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a14c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a18c ["COPY", "tmp:0:8", ["const:cec:8"]]
+ 0057a18c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a18c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a18c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a14c bytes 29b13291
+ 0057a18c bytes 29b13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6115408d9afdc4ede3e2ebb73d5aac60"></a>

### [`0057a34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a34c.md) → [`0057a38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md) FUN_0057a38c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a3e0",
      "incomplete_value": true,
      "site": "0057a3e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:441:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a3a0",
      "incomplete_value": true,
      "site": "0057a3a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:401:8"
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
      "definition_site": "0057a3e4",
      "incomplete_value": true,
      "site": "0057a3e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a3a4",
      "incomplete_value": true,
      "site": "0057a3a4",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057a3d0",
      "READ",
      [
        "storage",
        "002ba401",
        null,
        "string"
      ]
    ],
    [
      "0057a3d8",
      "READ",
      [
        "storage",
        "002ba407",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a3d0",
      "READ",
      [
        "storage",
        "002ba441",
        null,
        "string"
      ]
    ],
    [
      "0057a3d8",
      "READ",
      [
        "storage",
        "002ba447",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a34c.md#insn-0057a3e4) · [`0057a378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a34c.md#insn-0057a378) · [`0057a380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a34c.md#insn-0057a380)
- 新版 [`0057a424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a424) · [`0057a3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a3b8) · [`0057a3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a3c0)

~~~diff
- 0057a3e4 ["INT_ADD", "register:40f0:8", ["const:57a3e4:8", "const:4:8"]]
- 0057a3e4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057a424 ["INT_ADD", "register:40f0:8", ["const:57a424:8", "const:4:8"]]
+ 0057a424 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057a3e4 bytes b3751b94
+ 0057a424 bytes a3761b94
- 0057a378 ["INT_ADD", "register:40f0:8", ["const:57a378:8", "const:4:8"]]
- 0057a378 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057a3b8 ["INT_ADD", "register:40f0:8", ["const:57a3b8:8", "const:4:8"]]
+ 0057a3b8 ["CALL", null, ["callee:00588e6c:8"]]
- 0057a378 bytes ad3a0094
+ 0057a3b8 bytes ad3a0094
- 0057a380 ["INT_ADD", "register:40f0:8", ["const:57a380:8", "const:4:8"]]
- 0057a380 ["CALL", null, ["callee:0058915c:8"]]
+ 0057a3c0 ["INT_ADD", "register:40f0:8", ["const:57a3c0:8", "const:4:8"]]
+ 0057a3c0 ["CALL", null, ["callee:0058915c:8"]]
- 0057a380 bytes 673b0094
+ 0057a3c0 bytes 673b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b1eea8d5c778bc57ecb7ad7b04ae8ae"></a>

### [`0057a484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a484.md) → [`0057a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md) FUN_0057a4c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a518",
      "incomplete_value": true,
      "site": "0057a518",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a4d8",
      "incomplete_value": true,
      "site": "0057a4d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:41b:8"
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
      "definition_site": "0057a51c",
      "incomplete_value": true,
      "site": "0057a51c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a4dc",
      "incomplete_value": true,
      "site": "0057a4dc",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057a508",
      "READ",
      [
        "storage",
        "002b741b",
        null,
        "string"
      ]
    ],
    [
      "0057a510",
      "READ",
      [
        "storage",
        "002b7421",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a508",
      "READ",
      [
        "storage",
        "002b745b",
        null,
        "string"
      ]
    ],
    [
      "0057a510",
      "READ",
      [
        "storage",
        "002b7461",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a484.md#insn-0057a51c) · [`0057a4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a484.md#insn-0057a4b0) · [`0057a4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a484.md#insn-0057a4b8)
- 新版 [`0057a55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a55c) · [`0057a4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a4f0) · [`0057a4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a4f8)

~~~diff
- 0057a51c ["INT_ADD", "register:40f0:8", ["const:57a51c:8", "const:4:8"]]
- 0057a51c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057a55c ["INT_ADD", "register:40f0:8", ["const:57a55c:8", "const:4:8"]]
+ 0057a55c ["CALL", null, ["callee:00c57eb0:8"]]
- 0057a51c bytes 65751b94
+ 0057a55c bytes 55761b94
- 0057a4b0 ["INT_ADD", "register:40f0:8", ["const:57a4b0:8", "const:4:8"]]
- 0057a4b0 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057a4f0 ["INT_ADD", "register:40f0:8", ["const:57a4f0:8", "const:4:8"]]
+ 0057a4f0 ["CALL", null, ["callee:00588e6c:8"]]
- 0057a4b0 bytes 5f3a0094
+ 0057a4f0 bytes 5f3a0094
- 0057a4b8 ["INT_ADD", "register:40f0:8", ["const:57a4b8:8", "const:4:8"]]
- 0057a4b8 ["CALL", null, ["callee:0058915c:8"]]
+ 0057a4f8 ["INT_ADD", "register:40f0:8", ["const:57a4f8:8", "const:4:8"]]
+ 0057a4f8 ["CALL", null, ["callee:0058915c:8"]]
- 0057a4b8 bytes 193b0094
+ 0057a4f8 bytes 193b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6714e8d0f4d34dde2929bc8fc06111a"></a>

### [`0057a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md) → [`0057a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md) FUN_0057a5fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057a634",
      "incomplete_value": false,
      "site": "0057a648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a5f4",
      "incomplete_value": false,
      "site": "0057a608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "0057a63c",
      "incomplete_value": false,
      "site": "0057a648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a5fc",
      "incomplete_value": false,
      "site": "0057a608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "0057a634",
      "PARAM",
      [
        "storage",
        "00c6b988",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a63c",
      "PARAM",
      [
        "storage",
        "00c6b9a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0057a634",
      "PARAM",
      [
        "storage",
        "00c6bd88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a63c",
      "PARAM",
      [
        "storage",
        "00c6bda0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md#insn-0057a608) · [`0057a5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md#insn-0057a5f4) · [`0057a5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md#insn-0057a5fc)
- 新版 [`0057a648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a648) · [`0057a634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a634) · [`0057a63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a63c)

~~~diff
- 0057a608 ["INT_ADD", "register:40f0:8", ["const:57a608:8", "const:4:8"]]
- 0057a608 ["CALL", null, ["callee:00c58610:8"]]
+ 0057a648 ["INT_ADD", "register:40f0:8", ["const:57a648:8", "const:4:8"]]
+ 0057a648 ["CALL", null, ["callee:00c58610:8"]]
- 0057a608 bytes 02771b94
+ 0057a648 bytes f2771b94
- 0057a5f4 ["COPY", "tmp:0:8", ["const:988:8"]]
- 0057a5f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057a5f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057a5f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057a634 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0057a634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057a5f4 bytes 21202691
+ 0057a634 bytes 21203691
- 0057a5fc ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 0057a5fc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0057a5fc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0057a5fc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0057a63c ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 0057a63c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0057a63c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0057a63c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0057a5fc bytes 42802691
+ 0057a63c bytes 42803691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d99971eb7f88b9357e1426b002abda6"></a>

### [`0057a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md) → [`0057a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md) FUN_0057a73c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509cc.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`00550a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a0c.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a7b8",
      "incomplete_value": true,
      "site": "0057a7b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:524:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a778",
      "incomplete_value": true,
      "site": "0057a778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e4:8"
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
      "definition_site": "0057a7dc",
      "incomplete_value": true,
      "site": "0057a7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
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
      "definition_site": "0057a79c",
      "incomplete_value": true,
      "site": "0057a79c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a89c",
      "incomplete_value": false,
      "site": "0057a8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a85c",
      "incomplete_value": false,
      "site": "0057a864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "0057a7ac",
      "READ",
      [
        "storage",
        "002bb4e4",
        null,
        "string"
      ]
    ],
    [
      "0057a7d8",
      "READ",
      [
        "storage",
        "002b1db8",
        null,
        "string"
      ]
    ],
    [
      "0057a8a4",
      "DATA",
      [
        "storage",
        "00c6bb20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a7ac",
      "READ",
      [
        "storage",
        "002bb524",
        null,
        "string"
      ]
    ],
    [
      "0057a7d8",
      "READ",
      [
        "storage",
        "002b1df8",
        null,
        "string"
      ]
    ],
    [
      "0057a8a4",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md#insn-0057a748) · [`0057a750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md#insn-0057a750) · [`0057a768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md#insn-0057a768)
- 新版 [`0057a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a788) · [`0057a790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a790) · [`0057a7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a7a8)

~~~diff
- 0057a748 ["INT_ADD", "register:40f0:8", ["const:57a748:8", "const:4:8"]]
- 0057a748 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057a788 ["INT_ADD", "register:40f0:8", ["const:57a788:8", "const:4:8"]]
+ 0057a788 ["CALL", null, ["callee:00588e6c:8"]]
- 0057a748 bytes b9390094
+ 0057a788 bytes b9390094
- 0057a750 ["INT_ADD", "register:40f0:8", ["const:57a750:8", "const:4:8"]]
- 0057a750 ["CALL", null, ["callee:0058915c:8"]]
+ 0057a790 ["INT_ADD", "register:40f0:8", ["const:57a790:8", "const:4:8"]]
+ 0057a790 ["CALL", null, ["callee:0058915c:8"]]
- 0057a750 bytes 733a0094
+ 0057a790 bytes 733a0094
- 0057a768 ["COPY", "tmp:0:8", ["const:4e4:8"]]
- 0057a768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a7a8 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 0057a7a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a7a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a7a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a768 bytes 08911391
+ 0057a7a8 bytes 08911491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e1e0c6ce1de49d0ca84a14e25405cc8"></a>

### [`0057a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a928.md) → [`0057a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md) FUN_0057a968

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a984",
      "incomplete_value": false,
      "site": "0057a98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a944",
      "incomplete_value": false,
      "site": "0057a94c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "0057a9a0",
      "incomplete_value": false,
      "site": "0057a9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a960",
      "incomplete_value": false,
      "site": "0057a960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "0057a98c",
      "DATA",
      [
        "storage",
        "00c6bb70",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a9a0",
      "DATA",
      [
        "storage",
        "00c6b8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a98c",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a9a0",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a928.md#insn-0057a93c) · [`0057a944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a928.md#insn-0057a944) · [`0057a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a928.md#insn-0057a950)
- 新版 [`0057a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md#insn-0057a97c) · [`0057a984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md#insn-0057a984)

~~~diff
- 0057a93c ["INT_ADD", "register:40f0:8", ["const:57a93c:8", "const:4:8"]]
- 0057a93c ["CALL", null, ["callee:00c57e90:8"]]
+ 0057a97c ["INT_ADD", "register:40f0:8", ["const:57a97c:8", "const:4:8"]]
+ 0057a97c ["CALL", null, ["callee:00c57e90:8"]]
- 0057a93c bytes 55741b94
+ 0057a97c bytes 45751b94
- 0057a944 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0057a944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a984 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057a984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a944 bytes 08c12d91
+ 0057a984 bytes 08c13d91
- 0057a950 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0057a950 bytes 883700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-966989c01ca883fb9cc99278036ed6d5"></a>

### [`0057a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md) → [`0057a9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md) FUN_0057a9b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aa28",
      "incomplete_value": true,
      "site": "0057aa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9e8",
      "incomplete_value": true,
      "site": "0057a9e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "0057aa30",
      "incomplete_value": true,
      "site": "0057aa30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a9f0",
      "incomplete_value": true,
      "site": "0057a9f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aa2c",
      "incomplete_value": true,
      "site": "0057aa40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9ec",
      "incomplete_value": true,
      "site": "0057aa00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e7:8"
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
      "0057aa10",
      "READ",
      [
        "storage",
        "002bff20",
        null,
        "string"
      ]
    ],
    [
      "0057aa18",
      "READ",
      [
        "storage",
        "002bff26",
        null,
        "string"
      ]
    ],
    [
      "0057aa2c",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057aa10",
      "READ",
      [
        "storage",
        "002bff60",
        null,
        "string"
      ]
    ],
    [
      "0057aa18",
      "READ",
      [
        "storage",
        "002bff66",
        null,
        "string"
      ]
    ],
    [
      "0057aa2c",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md#insn-0057a9a8) · [`0057a9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md#insn-0057a9c0) · [`0057aa40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md#insn-0057aa40)
- 新版 [`0057a9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057a9e8) · [`0057aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057aa00) · [`0057aa80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057aa80)

~~~diff
- 0057a9a8 ["INT_ADD", "register:40f0:8", ["const:57a9a8:8", "const:4:8"]]
- 0057a9a8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057a9e8 ["INT_ADD", "register:40f0:8", ["const:57a9e8:8", "const:4:8"]]
+ 0057a9e8 ["CALL", null, ["callee:00588e6c:8"]]
- 0057a9a8 bytes 21390094
+ 0057a9e8 bytes 21390094
- 0057a9c0 ["INT_ADD", "register:40f0:8", ["const:57a9c0:8", "const:4:8"]]
- 0057a9c0 ["CALL", null, ["callee:0058915c:8"]]
+ 0057aa00 ["INT_ADD", "register:40f0:8", ["const:57aa00:8", "const:4:8"]]
+ 0057aa00 ["CALL", null, ["callee:0058915c:8"]]
- 0057a9c0 bytes d7390094
+ 0057aa00 bytes d7390094
- 0057aa40 ["INT_ADD", "register:40f0:8", ["const:57aa40:8", "const:4:8"]]
- 0057aa40 ["CALL", null, ["callee:0058915c:8"]]
+ 0057aa80 ["INT_ADD", "register:40f0:8", ["const:57aa80:8", "const:4:8"]]
+ 0057aa80 ["CALL", null, ["callee:0058915c:8"]]
- 0057aa40 bytes b7390094
+ 0057aa80 bytes b7390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e04bc2d51eca2a97e772074161a562d3"></a>

### [`0057ac24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ac24.md) → [`0057ac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md) FUN_0057ac64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057acc4",
      "incomplete_value": true,
      "site": "0057acc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:976:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ac84",
      "incomplete_value": true,
      "site": "0057ac84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:89a:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0057ad40",
      "incomplete_value": true,
      "site": "0057ad40",
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
      "definition_site": "0057ad00",
      "incomplete_value": true,
      "site": "0057ad00",
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
      "0057acb4",
      "READ",
      [
        "storage",
        "002a789a",
        null,
        "string"
      ]
    ],
    [
      "0057ad3c",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ad98",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057acb4",
      "READ",
      [
        "storage",
        "002a7976",
        null,
        "string"
      ]
    ],
    [
      "0057ad3c",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ad98",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ac24.md#insn-0057acc0) · [`0057ac54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ac24.md#insn-0057ac54) · [`0057ac5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ac24.md#insn-0057ac5c)
- 新版 [`0057ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ad00) · [`0057ac94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ac94) · [`0057ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ac9c)

~~~diff
- 0057acc0 ["INT_ADD", "register:40f0:8", ["const:57acc0:8", "const:4:8"]]
- 0057acc0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057ad00 ["INT_ADD", "register:40f0:8", ["const:57ad00:8", "const:4:8"]]
+ 0057ad00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057acc0 bytes 7c731b94
+ 0057ad00 bytes 6c741b94
- 0057ac54 ["INT_ADD", "register:40f0:8", ["const:57ac54:8", "const:4:8"]]
- 0057ac54 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057ac94 ["INT_ADD", "register:40f0:8", ["const:57ac94:8", "const:4:8"]]
+ 0057ac94 ["CALL", null, ["callee:00588e6c:8"]]
- 0057ac54 bytes 76380094
+ 0057ac94 bytes 76380094
- 0057ac5c ["INT_ADD", "register:40f0:8", ["const:57ac5c:8", "const:4:8"]]
- 0057ac5c ["CALL", null, ["callee:0058915c:8"]]
+ 0057ac9c ["INT_ADD", "register:40f0:8", ["const:57ac9c:8", "const:4:8"]]
+ 0057ac9c ["CALL", null, ["callee:0058915c:8"]]
- 0057ac5c bytes 30390094
+ 0057ac9c bytes 30390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79baa0e334a53a47ea3caed214ebe363"></a>

### [`0057ae1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae1c.md) → [`0057ae5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md) FUN_0057ae5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aeb8",
      "incomplete_value": true,
      "site": "0057aeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:46a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ae78",
      "incomplete_value": true,
      "site": "0057ae78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:42a:8"
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
      "0057aea0",
      "READ",
      [
        "storage",
        "002b742a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057aea0",
      "READ",
      [
        "storage",
        "002b746a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae1c.md#insn-0057aeb8) · [`0057ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae1c.md#insn-0057ae40) · [`0057ae48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae1c.md#insn-0057ae48)
- 新版 [`0057aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057aef8) · [`0057ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057ae80) · [`0057ae88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057ae88)

~~~diff
- 0057aeb8 ["INT_ADD", "register:40f0:8", ["const:57aeb8:8", "const:4:8"]]
- 0057aeb8 ["CALL", null, ["callee:0058915c:8"]]
+ 0057aef8 ["INT_ADD", "register:40f0:8", ["const:57aef8:8", "const:4:8"]]
+ 0057aef8 ["CALL", null, ["callee:0058915c:8"]]
- 0057aeb8 bytes 99380094
+ 0057aef8 bytes 99380094
- 0057ae40 ["INT_ADD", "register:40f0:8", ["const:57ae40:8", "const:4:8"]]
- 0057ae40 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057ae80 ["INT_ADD", "register:40f0:8", ["const:57ae80:8", "const:4:8"]]
+ 0057ae80 ["CALL", null, ["callee:00588e6c:8"]]
- 0057ae40 bytes fb370094
+ 0057ae80 bytes fb370094
- 0057ae48 ["INT_ADD", "register:40f0:8", ["const:57ae48:8", "const:4:8"]]
- 0057ae48 ["CALL", null, ["callee:0058915c:8"]]
+ 0057ae88 ["INT_ADD", "register:40f0:8", ["const:57ae88:8", "const:4:8"]]
+ 0057ae88 ["CALL", null, ["callee:0058915c:8"]]
- 0057ae48 bytes b5380094
+ 0057ae88 bytes b5380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87b6dc06842fa94c710f9819812b14f3"></a>

### [`0057af3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057af3c.md) → [`0057af7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md) FUN_0057af7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057afe8",
      "incomplete_value": true,
      "site": "0057aff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:121:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057afa8",
      "incomplete_value": true,
      "site": "0057afb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54:8"
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
      "definition_site": "0057aff4",
      "incomplete_value": true,
      "site": "0057aff4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057afb4",
      "incomplete_value": true,
      "site": "0057afb4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b0b4",
      "incomplete_value": false,
      "site": "0057b0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b074",
      "incomplete_value": false,
      "site": "0057b07c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0057afe8",
      "READ",
      [
        "storage",
        "002a2054",
        null,
        "string"
      ]
    ],
    [
      "0057afec",
      "READ",
      [
        "storage",
        "002a2061",
        null,
        "string"
      ]
    ],
    [
      "0057b0bc",
      "DATA",
      [
        "storage",
        "00c6bbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057afe8",
      "READ",
      [
        "storage",
        "002a2121",
        null,
        "string"
      ]
    ],
    [
      "0057afec",
      "READ",
      [
        "storage",
        "002a212e",
        null,
        "string"
      ]
    ],
    [
      "0057b0bc",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057af70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057af3c.md#insn-0057af70) · [`0057af68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057af3c.md#insn-0057af68) · [`0057afa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057af3c.md#insn-0057afa4)
- 新版 [`0057afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afb0) · [`0057afa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afa8) · [`0057afe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afe4)

~~~diff
- 0057af70 ["INT_ADD", "register:40f0:8", ["const:57af70:8", "const:4:8"]]
- 0057af70 ["CALL", null, ["callee:0058915c:8"]]
+ 0057afb0 ["INT_ADD", "register:40f0:8", ["const:57afb0:8", "const:4:8"]]
+ 0057afb0 ["CALL", null, ["callee:0058915c:8"]]
- 0057af70 bytes 6b380094
+ 0057afb0 bytes 6b380094
- 0057af68 ["INT_ADD", "register:40f0:8", ["const:57af68:8", "const:4:8"]]
- 0057af68 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057afa8 ["INT_ADD", "register:40f0:8", ["const:57afa8:8", "const:4:8"]]
+ 0057afa8 ["CALL", null, ["callee:00588e6c:8"]]
- 0057af68 bytes b1370094
+ 0057afa8 bytes b1370094
- 0057afa4 ["COPY", "tmp:0:8", ["const:54:8"]]
- 0057afa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057afa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057afa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057afe4 ["COPY", "tmp:0:8", ["const:121:8"]]
+ 0057afe4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057afe4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057afe4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057afa4 bytes 29510191
+ 0057afe4 bytes 29850491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea0efa2ec367be0439ab760fd2ac42f7"></a>

### [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) → [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) FUN_0057b164

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.90% / 新版 91.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b38c",
      "incomplete_value": true,
      "site": "0057b38c",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b34c",
      "incomplete_value": true,
      "site": "0057b34c",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b448",
      "incomplete_value": false,
      "site": "0057b450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b408",
      "incomplete_value": false,
      "site": "0057b410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b460",
      "incomplete_value": false,
      "site": "0057b460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b420",
      "incomplete_value": false,
      "site": "0057b420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:920:8"
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
      "0057b1e4",
      "READ",
      [
        "storage",
        "002a9cc4",
        null,
        "string"
      ]
    ],
    [
      "0057b1e4",
      "READ",
      [
        "storage",
        "002a9cd4",
        null,
        "string"
      ]
    ],
    [
      "0057b1e8",
      "READ",
      [
        "storage",
        "002c2e80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b1e4",
      "READ",
      [
        "storage",
        "002a9d91",
        null,
        "string"
      ]
    ],
    [
      "0057b1e4",
      "READ",
      [
        "storage",
        "002a9da1",
        null,
        "string"
      ]
    ],
    [
      "0057b1e8",
      "READ",
      [
        "storage",
        "002c2ec0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md#insn-0057b34c) · [`0057b160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md#insn-0057b160) · [`0057b168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md#insn-0057b168)
- 新版 [`0057b38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b38c) · [`0057b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b1a0) · [`0057b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b1a8)

~~~diff
- 0057b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 0057b34c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057b38c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
+ 0057b38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057b34c bytes 094507f9
+ 0057b38c bytes 094501f9
- 0057b160 ["INT_ADD", "register:40f0:8", ["const:57b160:8", "const:4:8"]]
- 0057b160 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057b1a0 ["INT_ADD", "register:40f0:8", ["const:57b1a0:8", "const:4:8"]]
+ 0057b1a0 ["CALL", null, ["callee:00588e6c:8"]]
- 0057b160 bytes 33370094
+ 0057b1a0 bytes 33370094
- 0057b168 ["INT_ADD", "register:40f0:8", ["const:57b168:8", "const:4:8"]]
- 0057b168 ["CALL", null, ["callee:0058915c:8"]]
+ 0057b1a8 ["INT_ADD", "register:40f0:8", ["const:57b1a8:8", "const:4:8"]]
+ 0057b1a8 ["CALL", null, ["callee:0058915c:8"]]
- 0057b168 bytes ed370094
+ 0057b1a8 bytes ed370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-960785c90e5a9bfae5c3a3a3f447df46"></a>

### [`0057b4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b4d8.md) → [`0057b518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md) Java_jp_co_ponos_battlecats_MyActivity_onAlertClick

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.56% / 新版 92.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b688",
      "incomplete_value": true,
      "site": "0057b688",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b648",
      "incomplete_value": true,
      "site": "0057b648",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b544",
      "incomplete_value": true,
      "site": "0057b544",
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
      "definition_site": "0057b504",
      "incomplete_value": true,
      "site": "0057b504",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b684",
      "incomplete_value": true,
      "site": "0057b684",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "0057b644",
      "incomplete_value": true,
      "site": "0057b644",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057b540",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b588",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5bc",
      "READ",
      [
        "storage",
        "00ca5ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b540",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b588",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5bc",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b4d8.md#insn-0057b648) · [`0057b4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b4d8.md#insn-0057b4f8) · [`0057b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b4d8.md#insn-0057b4fc)
- 新版 [`0057b688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b688) · [`0057b538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b538) · [`0057b53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b53c)

~~~diff
- 0057b648 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
- 0057b648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0057b688 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2a0:8"]]
+ 0057b688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057b648 bytes 285107f9
+ 0057b688 bytes 285101f9
- 0057b4f8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0057b538 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0057b4f8 bytes 483900d0
+ 0057b538 bytes 483900f0
- 0057b4fc ["COPY", "tmp:0:8", ["const:e90:8"]]
- 0057b4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b53c ["COPY", "tmp:0:8", ["const:290:8"]]
+ 0057b53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b4fc bytes 08413a91
+ 0057b53c bytes 08410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2fb38c1a9a2692115e2d15f07436522"></a>

### [`0057b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b6bc.md) → [`0057b6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md) Java_jp_co_ponos_battlecats_MyActivity_onButtonClick

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b708",
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
      "definition_site": "0057b6c8",
      "incomplete_value": true,
      "site": "0057b6c8",
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
      "0057b704",
      "READ",
      [
        "storage",
        "00ca5e78",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b75c",
      "READ",
      [
        "storage",
        "00ca5ea0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b704",
      "READ",
      [
        "storage",
        "00ca6278",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b75c",
      "READ",
      [
        "storage",
        "00ca62a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b6bc.md#insn-0057b6bc) · [`0057b6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b6bc.md#insn-0057b6c0) · [`0057b6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b6bc.md#insn-0057b6cc)
- 新版 [`0057b6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md#insn-0057b6fc) · [`0057b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md#insn-0057b700) · [`0057b70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md#insn-0057b70c)

~~~diff
- 0057b6bc ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0057b6fc ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0057b6bc bytes 483900d0
+ 0057b6fc bytes 483900f0
- 0057b6c0 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b700 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 0057b700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b6c0 bytes 08e13991
+ 0057b700 bytes 08e10991
- 0057b6cc ["COPY", "register:4048:8", ["const:ca5000:8"]]
+ 0057b70c ["COPY", "register:4048:8", ["const:ca6000:8"]]
- 0057b6cc bytes 493900d0
+ 0057b70c bytes 493900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7409e1e834a1135f8bc6238ef0de8248"></a>

### [`0057b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b738.md) → [`0057b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewFilter

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b7a0",
      "incomplete_value": true,
      "site": "0057b7a0",
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
      "definition_site": "0057b760",
      "incomplete_value": true,
      "site": "0057b760",
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
      "0057b79c",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b7f4",
      "READ",
      [
        "storage",
        "00ca5ec0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b79c",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b7f4",
      "READ",
      [
        "storage",
        "00ca62c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b738.md#insn-0057b754) · [`0057b758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b738.md#insn-0057b758) · [`0057b764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b738.md#insn-0057b764)
- 新版 [`0057b794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b794) · [`0057b798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b798) · [`0057b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b7a4)

~~~diff
- 0057b754 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0057b794 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0057b754 bytes 483900d0
+ 0057b794 bytes 483900f0
- 0057b758 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0057b758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b798 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 0057b798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b758 bytes 08013991
+ 0057b798 bytes 08010991
- 0057b764 ["COPY", "register:4098:8", ["const:ca5000:8"]]
+ 0057b7a4 ["COPY", "register:4098:8", ["const:ca6000:8"]]
- 0057b764 bytes 533900d0
+ 0057b7a4 bytes 533900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3079b32c9d511d250a7234323f5d1115"></a>

### [`0057b870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b870.md) → [`0057b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewResult

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b8e0",
      "incomplete_value": true,
      "site": "0057b8e0",
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
      "definition_site": "0057b8a0",
      "incomplete_value": true,
      "site": "0057b8a0",
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
      "0057b8dc",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b934",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b8dc",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b934",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b870.md#insn-0057b894) · [`0057b898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b870.md#insn-0057b898) · [`0057b8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b870.md#insn-0057b8a4)
- 新版 [`0057b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b8d4) · [`0057b8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b8d8) · [`0057b8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b8e4)

~~~diff
- 0057b894 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0057b8d4 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0057b894 bytes 483900d0
+ 0057b8d4 bytes 483900f0
- 0057b898 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0057b898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d8 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 0057b8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b898 bytes 08013991
+ 0057b8d8 bytes 08010991
- 0057b8a4 ["COPY", "register:40a8:8", ["const:ca5000:8"]]
+ 0057b8e4 ["COPY", "register:40a8:8", ["const:ca6000:8"]]
- 0057b8a4 bytes 553900d0
+ 0057b8e4 bytes 553900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b446490d434dcb63a6ad31475e4677eb"></a>

### [`0057b9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b9a8.md) → [`0057b9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewEvalResult

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057ba18",
      "incomplete_value": true,
      "site": "0057ba18",
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
      "definition_site": "0057b9d8",
      "incomplete_value": true,
      "site": "0057b9d8",
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
      "0057ba14",
      "READ",
      [
        "storage",
        "00ca5e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bab0",
      "READ",
      [
        "storage",
        "00ca5ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057ba14",
      "READ",
      [
        "storage",
        "00ca6258",
        null,
        "undefined8"
      ]
    ],
    [
      "0057bab0",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b9a8.md#insn-0057b9cc) · [`0057b9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b9a8.md#insn-0057b9d0) · [`0057b9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b9a8.md#insn-0057b9dc)
- 新版 [`0057ba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba0c) · [`0057ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba10) · [`0057ba1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba1c)

~~~diff
- 0057b9cc ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0057ba0c ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0057b9cc bytes 483900d0
+ 0057ba0c bytes 483900f0
- 0057b9d0 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0057b9d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b9d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b9d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba10 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0057ba10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b9d0 bytes 08613991
+ 0057ba10 bytes 08610991
- 0057b9dc ["COPY", "register:40a8:8", ["const:ca5000:8"]]
+ 0057ba1c ["COPY", "register:40a8:8", ["const:ca6000:8"]]
- 0057b9dc bytes 553900d0
+ 0057ba1c bytes 553900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f63d3f604cd78b4d11592e14ef23d0f"></a>

### [`0057bb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bb3c.md) → [`0057bb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md) FUN_0057bb7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057bb94",
      "incomplete_value": false,
      "site": "0057bb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057bb54",
      "incomplete_value": false,
      "site": "0057bb58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "0057bb98",
      "DATA",
      [
        "storage",
        "00c6b7e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057bb98",
      "DATA",
      [
        "storage",
        "00c6bbe8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057bb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bb3c.md#insn-0057bb98) · [`0057bb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bb3c.md#insn-0057bb54) · [`0057bb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bb3c.md#insn-0057bb88)
- 新版 [`0057bbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bbd8) · [`0057bb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bb94) · [`0057bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bbc8)

~~~diff
- 0057bb98 ["INT_ADD", "register:40f0:8", ["const:57bb98:8", "const:4:8"]]
- 0057bb98 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057bbd8 ["INT_ADD", "register:40f0:8", ["const:57bbd8:8", "const:4:8"]]
+ 0057bbd8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057bb98 bytes c66f1b94
+ 0057bbd8 bytes b6701b94
- 0057bb54 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 0057bb54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057bb54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057bb54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057bb94 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0057bb94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bb94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bb94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057bb54 bytes 29a11f91
+ 0057bb94 bytes 29a12f91
- 0057bb88 ["INT_ADD", "register:40f0:8", ["const:57bb88:8", "const:4:8"]]
- 0057bb88 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057bbc8 ["INT_ADD", "register:40f0:8", ["const:57bbc8:8", "const:4:8"]]
+ 0057bbc8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057bb88 bytes ca6f1b94
+ 0057bbc8 bytes ba701b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fd2cbda9e0d20f83ad0c0bc22171ac1"></a>

### [`0057bfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bfd0.md) → [`0057c010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c010.md) FUN_0057c010

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
      "definition_site": "0057c014",
      "incomplete_value": false,
      "site": "0057c018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057bfd4",
      "incomplete_value": false,
      "site": "0057bfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "0057c018",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c018",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057bfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bfd0.md#insn-0057bfd4)
- 新版 [`0057c014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c010.md#insn-0057c014)

~~~diff
- 0057bfd4 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 0057bfd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057bfd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057bfd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c014 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 0057c014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057bfd4 bytes 08012a91
+ 0057c014 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f034c298d0c1429ecfb7ef8dc23127bb"></a>

### [`0057bfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bfe0.md) → [`0057c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md) FUN_0057c020

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
      "definition_site": "0057c030",
      "incomplete_value": false,
      "site": "0057c038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057bff0",
      "incomplete_value": false,
      "site": "0057bff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "0057c038",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c038",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057bff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bfe0.md#insn-0057bff0) · [`0057bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bfe0.md#insn-0057bffc)
- 新版 [`0057c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md#insn-0057c030) · [`0057c03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md#insn-0057c03c)

~~~diff
- 0057bff0 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 0057bff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057bff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057bff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c030 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 0057c030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057bff0 bytes 08012a91
+ 0057c030 bytes 08013a91
- 0057bffc ["INT_ADD", "register:40f0:8", ["const:57bffc:8", "const:4:8"]]
- 0057bffc ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057c03c ["INT_ADD", "register:40f0:8", ["const:57c03c:8", "const:4:8"]]
+ 0057c03c ["CALL", null, ["callee:00c57ea0:8"]]
- 0057bffc bytes a96e1b94
+ 0057c03c bytes 996f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be22778ac5e135a70391eb205f6893d5"></a>

### [`0057c020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c020.md) → [`0057c060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c060.md) FUN_0057c060

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
      "definition_site": "0057c064",
      "incomplete_value": false,
      "site": "0057c068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c024",
      "incomplete_value": false,
      "site": "0057c028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "0057c068",
      "DATA",
      [
        "storage",
        "00c6bad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c068",
      "DATA",
      [
        "storage",
        "00c6bed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c020.md#insn-0057c024)
- 新版 [`0057c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c060.md#insn-0057c064)

~~~diff
- 0057c024 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 0057c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c064 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 0057c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c024 bytes 08412b91
+ 0057c064 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3229c4515dc8407035b4193f03c245d"></a>

### [`0057c030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c030.md) → [`0057c070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md) FUN_0057c070

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
      "definition_site": "0057c080",
      "incomplete_value": false,
      "site": "0057c088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c040",
      "incomplete_value": false,
      "site": "0057c048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "0057c088",
      "DATA",
      [
        "storage",
        "00c6bad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c088",
      "DATA",
      [
        "storage",
        "00c6bed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c030.md#insn-0057c040) · [`0057c04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c030.md#insn-0057c04c)
- 新版 [`0057c080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md#insn-0057c080) · [`0057c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md#insn-0057c08c)

~~~diff
- 0057c040 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 0057c040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c080 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 0057c080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c040 bytes 08412b91
+ 0057c080 bytes 08413b91
- 0057c04c ["INT_ADD", "register:40f0:8", ["const:57c04c:8", "const:4:8"]]
- 0057c04c ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057c08c ["INT_ADD", "register:40f0:8", ["const:57c08c:8", "const:4:8"]]
+ 0057c08c ["CALL", null, ["callee:00c57ea0:8"]]
- 0057c04c bytes 956e1b94
+ 0057c08c bytes 856f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4590d27c5156eb210a41d29c729042cf"></a>

### [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) → [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) FUN_0057c20c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0057c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md) [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`0057c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md) [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0057c218",
      "incomplete_value": false,
      "site": "0057c21c",
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
      "definition_site": "0057c1d8",
      "incomplete_value": false,
      "site": "0057c1dc",
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
      "0057c218",
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
      "0057c218",
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

- 旧版 [`0057c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md#insn-0057c1dc) · [`0057c1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md#insn-0057c1d8)
- 新版 [`0057c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md#insn-0057c21c) · [`0057c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md#insn-0057c218)

~~~diff
- 0057c1dc ["INT_ADD", "register:40f0:8", ["const:57c1dc:8", "const:4:8"]]
- 0057c1dc ["CALL", null, ["callee:0043b778:8"]]
+ 0057c21c ["INT_ADD", "register:40f0:8", ["const:57c21c:8", "const:4:8"]]
+ 0057c21c ["CALL", null, ["callee:0043b778:8"]]
- 0057c1dc bytes 57fdfa97
+ 0057c21c bytes 57fdfa97
- 0057c1d8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0057c1d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c1d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c1d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c218 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0057c218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c1d8 bytes 00303c91
+ 0057c218 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09eb3c3a25def4b6801919cb6f527d1"></a>

### [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md) → [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md) FUN_0057c31c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0057a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md) [`0057a2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md) [`0057a304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`0057a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md) [`0057a2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md) [`0057a344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0057c328",
      "incomplete_value": false,
      "site": "0057c32c",
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
      "definition_site": "0057c2e8",
      "incomplete_value": false,
      "site": "0057c2ec",
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
      "0057c328",
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
      "0057c328",
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

- 旧版 [`0057c2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md#insn-0057c2ec) · [`0057c2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md#insn-0057c2e8)
- 新版 [`0057c32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md#insn-0057c32c) · [`0057c328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md#insn-0057c328)

~~~diff
- 0057c2ec ["INT_ADD", "register:40f0:8", ["const:57c2ec:8", "const:4:8"]]
- 0057c2ec ["CALL", null, ["callee:00442930:8"]]
+ 0057c32c ["INT_ADD", "register:40f0:8", ["const:57c32c:8", "const:4:8"]]
+ 0057c32c ["CALL", null, ["callee:00442930:8"]]
- 0057c2ec bytes 8119fb97
+ 0057c32c bytes 8119fb97
- 0057c2e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0057c2e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c2e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c2e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c328 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0057c328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c2e8 bytes 00303c91
+ 0057c328 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f578b16e637613d88b72d51d223dfc90"></a>

### [`0057c44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c44c.md) → [`0057c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c48c.md) FUN_0057c48c

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
      "definition_site": "0057c490",
      "incomplete_value": false,
      "site": "0057c494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c450",
      "incomplete_value": false,
      "site": "0057c454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0057c494",
      "DATA",
      [
        "storage",
        "00c6bb20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c494",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c44c.md#insn-0057c450)
- 新版 [`0057c490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c48c.md#insn-0057c490)

~~~diff
- 0057c450 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0057c450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c490 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0057c490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c450 bytes 08812c91
+ 0057c490 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a8194ca6c5196742df977e9c2879588"></a>

### [`0057c45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c45c.md) → [`0057c49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md) FUN_0057c49c

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
      "definition_site": "0057c4ac",
      "incomplete_value": false,
      "site": "0057c4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c46c",
      "incomplete_value": false,
      "site": "0057c474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0057c4b4",
      "DATA",
      [
        "storage",
        "00c6bb20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4b4",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c45c.md#insn-0057c46c) · [`0057c478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c45c.md#insn-0057c478)
- 新版 [`0057c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md#insn-0057c4ac) · [`0057c4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md#insn-0057c4b8)

~~~diff
- 0057c46c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0057c46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ac ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0057c4ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c46c bytes 08812c91
+ 0057c4ac bytes 08813c91
- 0057c478 ["INT_ADD", "register:40f0:8", ["const:57c478:8", "const:4:8"]]
- 0057c478 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057c4b8 ["INT_ADD", "register:40f0:8", ["const:57c4b8:8", "const:4:8"]]
+ 0057c4b8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0057c478 bytes 8a6d1b94
+ 0057c4b8 bytes 7a6e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70191740f0cee3f464261e7279069889"></a>

### [`0057c49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c49c.md) → [`0057c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4dc.md) FUN_0057c4dc

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
      "definition_site": "0057c4e0",
      "incomplete_value": false,
      "site": "0057c4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4a0",
      "incomplete_value": false,
      "site": "0057c4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0057c4e4",
      "DATA",
      [
        "storage",
        "00c6bb70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4e4",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c49c.md#insn-0057c4a0)
- 新版 [`0057c4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4dc.md#insn-0057c4e0)

~~~diff
- 0057c4a0 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0057c4a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4e0 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057c4e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4a0 bytes 08c12d91
+ 0057c4e0 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9dfa5a3adb588ff870ad451ace3f83"></a>

### [`0057c4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ac.md) → [`0057c4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md) FUN_0057c4ec

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
      "definition_site": "0057c4fc",
      "incomplete_value": false,
      "site": "0057c504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4bc",
      "incomplete_value": false,
      "site": "0057c4c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "0057c504",
      "DATA",
      [
        "storage",
        "00c6bb70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c504",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ac.md#insn-0057c4bc) · [`0057c4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c4ac.md#insn-0057c4c8)
- 新版 [`0057c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md#insn-0057c4fc) · [`0057c508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md#insn-0057c508)

~~~diff
- 0057c4bc ["COPY", "tmp:0:8", ["const:b70:8"]]
- 0057c4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4fc ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 0057c4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4bc bytes 08c12d91
+ 0057c4fc bytes 08c13d91
- 0057c4c8 ["INT_ADD", "register:40f0:8", ["const:57c4c8:8", "const:4:8"]]
- 0057c4c8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057c508 ["INT_ADD", "register:40f0:8", ["const:57c508:8", "const:4:8"]]
+ 0057c508 ["CALL", null, ["callee:00c57ea0:8"]]
- 0057c4c8 bytes 766d1b94
+ 0057c508 bytes 666e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-665f39b86443db7b168e7dff859250f0"></a>

### [`0057c5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c5cc.md) → [`0057c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c60c.md) FUN_0057c60c

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
      "definition_site": "0057c610",
      "incomplete_value": false,
      "site": "0057c614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c5d0",
      "incomplete_value": false,
      "site": "0057c5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0057c614",
      "DATA",
      [
        "storage",
        "00c6bbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c614",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c5cc.md#insn-0057c5d0)
- 新版 [`0057c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c60c.md#insn-0057c610)

~~~diff
- 0057c5d0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0057c5d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c5d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c5d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c610 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0057c610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c5d0 bytes 08012f91
+ 0057c610 bytes 08013f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4f1825e1dad764a88a30a69cd4017b"></a>

### [`0057c5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c5dc.md) → [`0057c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md) FUN_0057c61c

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
      "definition_site": "0057c62c",
      "incomplete_value": false,
      "site": "0057c634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c5ec",
      "incomplete_value": false,
      "site": "0057c5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0057c634",
      "DATA",
      [
        "storage",
        "00c6bbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c634",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c5dc.md#insn-0057c5ec) · [`0057c5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c5dc.md#insn-0057c5f8)
- 新版 [`0057c62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md#insn-0057c62c) · [`0057c638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md#insn-0057c638)

~~~diff
- 0057c5ec ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0057c5ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c5ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c5ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c62c ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0057c62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c5ec bytes 08012f91
+ 0057c62c bytes 08013f91
- 0057c5f8 ["INT_ADD", "register:40f0:8", ["const:57c5f8:8", "const:4:8"]]
- 0057c5f8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057c638 ["INT_ADD", "register:40f0:8", ["const:57c638:8", "const:4:8"]]
+ 0057c638 ["CALL", null, ["callee:00c57ea0:8"]]
- 0057c5f8 bytes 2a6d1b94
+ 0057c638 bytes 1a6e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767df928ca8fada33a2b0fd1e0c28f7a"></a>

### [`0057c77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c77c.md) → [`0057c7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md) _INIT_31

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0057656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057656c.md) [`00576574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576574.md) [`005766b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766b8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`005765ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765ac.md) [`005765b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765b4.md) [`005766f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766f8.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 12件, `store_value` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c7f8",
      "incomplete_value": true,
      "site": "0057c814",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c7b8",
      "incomplete_value": true,
      "site": "0057c7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c81c",
      "incomplete_value": true,
      "site": "0057c838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c7dc",
      "incomplete_value": true,
      "site": "0057c7f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c83c",
      "incomplete_value": true,
      "site": "0057c858",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057c7fc",
      "incomplete_value": true,
      "site": "0057c818",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057c7f8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0057c81c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0057c83c",
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
      "0057c7f8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0057c81c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0057c83c",
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

- 旧版 [`0057c814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c77c.md#insn-0057c814) · [`0057c99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c77c.md#insn-0057c99c) · [`0057c9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c77c.md#insn-0057c9b4)
- 新版 [`0057c854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c854) · [`0057c9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c9dc) · [`0057c9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c9f4)

~~~diff
- 0057c814 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0057c814 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057c814 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057c814 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057c854 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0057c854 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057c854 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057c854 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057c814 bytes 4a553a91
+ 0057c854 bytes 4a893d91
- 0057c99c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 0057c99c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057c99c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057c99c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057c9dc ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0057c9dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c9dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057c9dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057c99c bytes 73422e91
+ 0057c9dc bytes 73423e91
- 0057c9b4 ["INT_ADD", "register:40f0:8", ["const:57c9b4:8", "const:4:8"]]
- 0057c9b4 ["CALL", null, ["callee:00c57e30:8"]]
+ 0057c9f4 ["INT_ADD", "register:40f0:8", ["const:57c9f4:8", "const:4:8"]]
+ 0057c9f4 ["CALL", null, ["callee:00c57e30:8"]]
- 0057c9b4 bytes 1f6c1b94
+ 0057c9f4 bytes 0f6d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b2a9e6d54b406c32c1e92f551a9496f"></a>

### [`0057cbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cbd8.md) → [`0057cc18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md) FUN_0057cc18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cc38",
      "incomplete_value": false,
      "site": "0057cc38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cbf8",
      "incomplete_value": false,
      "site": "0057cbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cc38",
      "incomplete_value": false,
      "site": "0057cc38",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cbf8",
      "incomplete_value": false,
      "site": "0057cbf8",
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
                "const:c6b000:8"
              ],
              [
                "leaf",
                "const:c10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057cc38",
      "DATA",
      [
        "storage",
        "00c6bc10",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc38",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cc38",
      "DATA",
      [
        "storage",
        "00c6c010",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc38",
      "DATA",
      [
        "storage",
        "00c6c0d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cbd8.md#insn-0057cbe8) · [`0057cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cbd8.md#insn-0057cbec) · [`0057cc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cbd8.md#insn-0057cc00)
- 新版 [`0057cc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md#insn-0057cc28) · [`0057cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md#insn-0057cc2c) · [`0057cc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md#insn-0057cc40)

~~~diff
- 0057cbe8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057cc28 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057cbe8 bytes 683700f0
+ 0057cc28 bytes 88370090
- 0057cbec ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0057cbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cc2c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0057cc2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cbec bytes 08413091
+ 0057cc2c bytes 08410091
- 0057cc00 ["INT_ADD", "register:40f0:8", ["const:57cc00:8", "const:4:8"]]
- 0057cc00 ["CALL", null, ["callee:00c5a140:8"]]
+ 0057cc40 ["INT_ADD", "register:40f0:8", ["const:57cc40:8", "const:4:8"]]
+ 0057cc40 ["CALL", null, ["callee:00c5a140:8"]]
- 0057cc00 bytes 50741b94
+ 0057cc40 bytes 40751b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4237506ffcbc4a0d2bf1bac840a68b4"></a>

### [`0057cc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc38.md) → [`0057cc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md) FUN_0057cc78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cc98",
      "incomplete_value": false,
      "site": "0057cc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc58",
      "incomplete_value": false,
      "site": "0057cc58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cc98",
      "incomplete_value": false,
      "site": "0057cc98",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc58",
      "incomplete_value": false,
      "site": "0057cc58",
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
                "const:c6b000:8"
              ],
              [
                "leaf",
                "const:c10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057cc98",
      "DATA",
      [
        "storage",
        "00c6bc10",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc98",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cc98",
      "DATA",
      [
        "storage",
        "00c6c010",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc98",
      "DATA",
      [
        "storage",
        "00c6c0d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc38.md#insn-0057cc48) · [`0057cc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc38.md#insn-0057cc4c) · [`0057cc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc38.md#insn-0057cc60)
- 新版 [`0057cc88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057cc88) · [`0057cc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057cc8c) · [`0057cca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057cca0)

~~~diff
- 0057cc48 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057cc88 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057cc48 bytes 683700f0
+ 0057cc88 bytes 88370090
- 0057cc4c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0057cc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cc8c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0057cc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cc4c bytes 08413091
+ 0057cc8c bytes 08410091
- 0057cc60 ["INT_ADD", "register:40f0:8", ["const:57cc60:8", "const:4:8"]]
- 0057cc60 ["CALL", null, ["callee:00c5a140:8"]]
+ 0057cca0 ["INT_ADD", "register:40f0:8", ["const:57cca0:8", "const:4:8"]]
+ 0057cca0 ["CALL", null, ["callee:00c5a140:8"]]
- 0057cc60 bytes 38741b94
+ 0057cca0 bytes 28751b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1c389235a74c44d3395a1794de13b1"></a>

### [`0057ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md) → [`0057ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md) FUN_0057ceb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cfe8",
      "incomplete_value": false,
      "site": "0057cff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0057d034",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d034",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md#insn-0057cec4) · [`0057cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md#insn-0057cee0) · [`0057cf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md#insn-0057cf18)
- 新版 [`0057cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf04) · [`0057cf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf20) · [`0057cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf58)

~~~diff
- 0057cec4 ["INT_ADD", "register:40f0:8", ["const:57cec4:8", "const:4:8"]]
- 0057cec4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0057cf04 ["INT_ADD", "register:40f0:8", ["const:57cf04:8", "const:4:8"]]
+ 0057cf04 ["CALL", null, ["callee:00c57e90:8"]]
- 0057cec4 bytes f36a1b94
+ 0057cf04 bytes e36b1b94
- 0057cee0 ["INT_ADD", "register:40f0:8", ["const:57cee0:8", "const:4:8"]]
- 0057cee0 ["CALL", null, ["callee:00c58090:8"]]
+ 0057cf20 ["INT_ADD", "register:40f0:8", ["const:57cf20:8", "const:4:8"]]
+ 0057cf20 ["CALL", null, ["callee:00c58090:8"]]
- 0057cee0 bytes 6c6b1b94
+ 0057cf20 bytes 5c6c1b94
- 0057cf18 ["INT_ADD", "register:40f0:8", ["const:57cf18:8", "const:4:8"]]
- 0057cf18 ["CALL", null, ["callee:00c5a180:8"]]
+ 0057cf58 ["INT_ADD", "register:40f0:8", ["const:57cf58:8", "const:4:8"]]
+ 0057cf58 ["CALL", null, ["callee:00c5a180:8"]]
- 0057cf18 bytes 9a731b94
+ 0057cf58 bytes 8a741b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f84d60cf0f7a3f1a15338bfa096acb5c"></a>

### [`0057d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md) → [`0057d494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md) FUN_0057d494

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d60c",
      "incomplete_value": false,
      "site": "0057d618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d5cc",
      "incomplete_value": false,
      "site": "0057d5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0057d618",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d618",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md#insn-0057d4a0) · [`0057d4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md#insn-0057d4bc) · [`0057d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md#insn-0057d4f8)
- 新版 [`0057d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d4e0) · [`0057d4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d4fc) · [`0057d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d538)

~~~diff
- 0057d4a0 ["INT_ADD", "register:40f0:8", ["const:57d4a0:8", "const:4:8"]]
- 0057d4a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0057d4e0 ["INT_ADD", "register:40f0:8", ["const:57d4e0:8", "const:4:8"]]
+ 0057d4e0 ["CALL", null, ["callee:00c57e90:8"]]
- 0057d4a0 bytes 7c691b94
+ 0057d4e0 bytes 6c6a1b94
- 0057d4bc ["INT_ADD", "register:40f0:8", ["const:57d4bc:8", "const:4:8"]]
- 0057d4bc ["CALL", null, ["callee:00c58090:8"]]
+ 0057d4fc ["INT_ADD", "register:40f0:8", ["const:57d4fc:8", "const:4:8"]]
+ 0057d4fc ["CALL", null, ["callee:00c58090:8"]]
- 0057d4bc bytes f5691b94
+ 0057d4fc bytes e56a1b94
- 0057d4f8 ["INT_ADD", "register:40f0:8", ["const:57d4f8:8", "const:4:8"]]
- 0057d4f8 ["CALL", null, ["callee:00c5a080:8"]]
+ 0057d538 ["INT_ADD", "register:40f0:8", ["const:57d538:8", "const:4:8"]]
+ 0057d538 ["CALL", null, ["callee:00c5a080:8"]]
- 0057d4f8 bytes e2711b94
+ 0057d538 bytes d2721b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484e68e03efc9b08776c9638b582cec5"></a>

### [`0057d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d968.md) → [`0057d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md) FUN_0057d9a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md) [`00c59d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d60.md)
- 新版 呼出元 1件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md) [`00c5a160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057da00",
      "incomplete_value": false,
      "site": "0057da0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d9c0",
      "incomplete_value": false,
      "site": "0057d9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057da20",
      "incomplete_value": false,
      "site": "0057da20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d9e0",
      "incomplete_value": false,
      "site": "0057d9e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "0057da24",
      "incomplete_value": false,
      "site": "0057da28",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d9e4",
      "incomplete_value": false,
      "site": "0057d9e8",
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
                "const:c6b000:8"
              ],
              [
                "leaf",
                "const:c10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057d9c8",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d9dc",
      "READ",
      [
        "storage",
        "00ca5eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057da0c",
      "DATA",
      [
        "storage",
        "00c6beb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d9c8",
      "READ",
      [
        "storage",
        "00c9b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d9dc",
      "READ",
      [
        "storage",
        "00ca62b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057da0c",
      "DATA",
      [
        "storage",
        "00c6c2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d968.md#insn-0057d9a8) · [`0057da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d968.md#insn-0057da30) · [`0057d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d968.md#insn-0057d980)
- 新版 [`0057d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057d9e8) · [`0057da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057da70) · [`0057d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057d9c0)

~~~diff
- 0057d9a8 ["INT_ADD", "register:40f0:8", ["const:57d9a8:8", "const:4:8"]]
- 0057d9a8 ["CALL", null, ["callee:00c5a160:8"]]
+ 0057d9e8 ["INT_ADD", "register:40f0:8", ["const:57d9e8:8", "const:4:8"]]
+ 0057d9e8 ["CALL", null, ["callee:00c5a160:8"]]
- 0057d9a8 bytes ee701b94
+ 0057d9e8 bytes de711b94
- 0057da30 ["INT_ADD", "register:40f0:8", ["const:57da30:8", "const:4:8"]]
- 0057da30 ["CALL", null, ["callee:00c5a090:8"]]
+ 0057da70 ["INT_ADD", "register:40f0:8", ["const:57da70:8", "const:4:8"]]
+ 0057da70 ["CALL", null, ["callee:00c5a090:8"]]
- 0057da30 bytes 98701b94
+ 0057da70 bytes 88711b94
- 0057d980 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0057d9c0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0057d980 bytes e83800b0
+ 0057d9c0 bytes e83800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1fb13f9b14e0fad0d5afa57b6fe320"></a>

### [`0057db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db00.md) → [`0057db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db40.md) FUN_0057db40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db50",
      "incomplete_value": false,
      "site": "0057db50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db10",
      "incomplete_value": false,
      "site": "0057db10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db50",
      "incomplete_value": false,
      "site": "0057db50",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db10",
      "incomplete_value": false,
      "site": "0057db10",
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
                "const:c6b000:8"
              ],
              [
                "leaf",
                "const:cf0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057db50",
      "DATA",
      [
        "storage",
        "00c6bcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db50",
      "DATA",
      [
        "storage",
        "00c6bdb8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057db50",
      "DATA",
      [
        "storage",
        "00c6c0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db50",
      "DATA",
      [
        "storage",
        "00c6c1b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db00.md#insn-0057db00) · [`0057db04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db00.md#insn-0057db04)
- 新版 [`0057db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db40.md#insn-0057db40) · [`0057db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db40.md#insn-0057db44)

~~~diff
- 0057db00 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057db40 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057db00 bytes 683700d0
+ 0057db40 bytes 683700f0
- 0057db04 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 0057db04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057db44 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 0057db44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db04 bytes 08c13391
+ 0057db44 bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5574116ad599d82f62570cf02fe346cf"></a>

### [`0057db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db24.md) → [`0057db64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md) FUN_0057db64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db74",
      "incomplete_value": true,
      "site": "0057db74",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db34",
      "incomplete_value": true,
      "site": "0057db34",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db74",
      "incomplete_value": true,
      "site": "0057db74",
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
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db34",
      "incomplete_value": true,
      "site": "0057db34",
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
                "const:cf0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057db74",
      "DATA",
      [
        "storage",
        "00c6bcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db74",
      "DATA",
      [
        "storage",
        "00c6bdb8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057db74",
      "DATA",
      [
        "storage",
        "00c6c0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db74",
      "DATA",
      [
        "storage",
        "00c6c1b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db24.md#insn-0057db24) · [`0057db28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db24.md#insn-0057db28) · [`0057db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db24.md#insn-0057db54)
- 新版 [`0057db64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md#insn-0057db64) · [`0057db68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md#insn-0057db68) · [`0057db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md#insn-0057db94)

~~~diff
- 0057db24 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057db64 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057db24 bytes 683700d0
+ 0057db64 bytes 683700f0
- 0057db28 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 0057db28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057db68 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 0057db68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db28 bytes 08c13391
+ 0057db68 bytes 08c10391
- 0057db54 ["INT_ADD", "register:40f0:8", ["const:57db54:8", "const:4:8"]]
- 0057db54 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057db94 ["INT_ADD", "register:40f0:8", ["const:57db94:8", "const:4:8"]]
+ 0057db94 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057db54 bytes d7671b94
+ 0057db94 bytes c7681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb0a021aa2a5ca70c9717c8d1c5f16a4"></a>

### [`0057db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db68.md) → [`0057dba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dba8.md) FUN_0057dba8

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
      "definition_site": "0057dbac",
      "incomplete_value": false,
      "site": "0057dbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db6c",
      "incomplete_value": false,
      "site": "0057db70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0057dbb0",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057dbb0",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db68.md#insn-0057db68) · [`0057db6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db68.md#insn-0057db6c)
- 新版 [`0057dba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dba8.md#insn-0057dba8) · [`0057dbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dba8.md#insn-0057dbac)

~~~diff
- 0057db68 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057dba8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057db68 bytes 683700d0
+ 0057dba8 bytes 683700f0
- 0057db6c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0057db6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dbac ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0057dbac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db6c bytes 08813991
+ 0057dbac bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-723b0f9cd9f53d2d72aacc01e6e24cc5"></a>

### [`0057dbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dbb8.md) → [`0057dbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dbf8.md) FUN_0057dbf8

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
      "definition_site": "0057dbfc",
      "incomplete_value": false,
      "site": "0057dc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbbc",
      "incomplete_value": false,
      "site": "0057dbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0057dc00",
      "DATA",
      [
        "storage",
        "00c6beb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dc00",
      "DATA",
      [
        "storage",
        "00c6c2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dbb8.md#insn-0057dbb8) · [`0057dbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dbb8.md#insn-0057dbbc)
- 新版 [`0057dbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dbf8.md#insn-0057dbf8) · [`0057dbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dbf8.md#insn-0057dbfc)

~~~diff
- 0057dbb8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057dbf8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057dbb8 bytes 683700d0
+ 0057dbf8 bytes 683700f0
- 0057dbbc ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 0057dbbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dbfc ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 0057dbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dbbc bytes 08c13a91
+ 0057dbfc bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12b02e3a90927cac3e8975f4ab2fb761"></a>

### [`0057dc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc08.md) → [`0057dc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc48.md) FUN_0057dc48

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
      "definition_site": "0057dc4c",
      "incomplete_value": false,
      "site": "0057dc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc0c",
      "incomplete_value": false,
      "site": "0057dc10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "0057dc50",
      "DATA",
      [
        "storage",
        "00c6bf00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dc50",
      "DATA",
      [
        "storage",
        "00c6c300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc08.md#insn-0057dc08) · [`0057dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc08.md#insn-0057dc0c)
- 新版 [`0057dc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc48.md#insn-0057dc48) · [`0057dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc48.md#insn-0057dc4c)

~~~diff
- 0057dc08 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057dc48 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057dc08 bytes 683700d0
+ 0057dc48 bytes 683700f0
- 0057dc0c ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0057dc0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dc4c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0057dc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc0c bytes 08013c91
+ 0057dc4c bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7788ef47c3da645dc2271933e7e23dc2"></a>

### [`0057dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc18.md) → [`0057dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md) FUN_0057dc58

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
      "definition_site": "0057dc68",
      "incomplete_value": false,
      "site": "0057dc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc28",
      "incomplete_value": false,
      "site": "0057dc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "0057dc70",
      "DATA",
      [
        "storage",
        "00c6bf00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dc70",
      "DATA",
      [
        "storage",
        "00c6c300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc18.md#insn-0057dc24) · [`0057dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc18.md#insn-0057dc28) · [`0057dc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dc18.md#insn-0057dc34)
- 新版 [`0057dc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md#insn-0057dc64) · [`0057dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md#insn-0057dc68) · [`0057dc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md#insn-0057dc74)

~~~diff
- 0057dc24 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057dc64 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057dc24 bytes 683700d0
+ 0057dc64 bytes 683700f0
- 0057dc28 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0057dc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dc68 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0057dc68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc28 bytes 08013c91
+ 0057dc68 bytes 08010c91
- 0057dc34 ["INT_ADD", "register:40f0:8", ["const:57dc34:8", "const:4:8"]]
- 0057dc34 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057dc74 ["INT_ADD", "register:40f0:8", ["const:57dc74:8", "const:4:8"]]
+ 0057dc74 ["CALL", null, ["callee:00c57ea0:8"]]
- 0057dc34 bytes 9b671b94
+ 0057dc74 bytes 8b681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a88ff8f3384199f25643c30af79a1ef"></a>

### [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) → [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) FUN_0057e090

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00550bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bc8.md) [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`005862a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`00550c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c08.md) [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`005862e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e0c4",
      "incomplete_value": false,
      "site": "0057e0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e084",
      "incomplete_value": false,
      "site": "0057e08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "0057e0cc",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e0e4",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e0cc",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e0e4",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md#insn-0057e07c) · [`0057e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md#insn-0057e080) · [`0057e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md#insn-0057e084)
- 新版 [`0057e0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0bc) · [`0057e0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0c0) · [`0057e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0c4)

~~~diff
- 0057e07c ["INT_ADD", "register:40f0:8", ["const:57e07c:8", "const:4:8"]]
- 0057e07c ["CALL", null, ["callee:00c57e90:8"]]
+ 0057e0bc ["INT_ADD", "register:40f0:8", ["const:57e0bc:8", "const:4:8"]]
+ 0057e0bc ["CALL", null, ["callee:00c57e90:8"]]
- 0057e07c bytes 85661b94
+ 0057e0bc bytes 75671b94
- 0057e080 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e0c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e080 bytes 683700b0
+ 0057e0c0 bytes 683700d0
- 0057e084 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0057e084 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e084 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e084 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e0c4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0057e0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e084 bytes 08213f91
+ 0057e0c4 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca97a0768c003084d83d0e45f20bddde"></a>

### [`0057e124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e124.md) → [`0057e164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md) FUN_0057e164

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e17c",
      "incomplete_value": true,
      "site": "0057e180",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e13c",
      "incomplete_value": true,
      "site": "0057e140",
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
            "const:f50:8"
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
      "0057e180",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e180",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e124.md#insn-0057e180) · [`0057e138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e124.md#insn-0057e138) · [`0057e13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e124.md#insn-0057e13c)
- 新版 [`0057e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e1c0) · [`0057e178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e178) · [`0057e17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e17c)

~~~diff
- 0057e180 ["INT_ADD", "register:40f0:8", ["const:57e180:8", "const:4:8"]]
- 0057e180 ["CALL", null, ["callee:00c57e80:8"]]
+ 0057e1c0 ["INT_ADD", "register:40f0:8", ["const:57e1c0:8", "const:4:8"]]
+ 0057e1c0 ["CALL", null, ["callee:00c57e80:8"]]
- 0057e180 bytes 40661b94
+ 0057e1c0 bytes 30671b94
- 0057e138 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e178 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e138 bytes 683700b0
+ 0057e178 bytes 683700d0
- 0057e13c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0057e13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e17c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0057e17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e13c bytes 08413d91
+ 0057e17c bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77de8cfc09e663f9126df20108f2eff6"></a>

### [`0057e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e19c.md) → [`0057e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md) FUN_0057e1dc

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
      "definition_site": "0057e1f4",
      "incomplete_value": false,
      "site": "0057e1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e1b4",
      "incomplete_value": false,
      "site": "0057e1b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0057e1f8",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e1f8",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e19c.md#insn-0057e1b0) · [`0057e1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e19c.md#insn-0057e1b4) · [`0057e1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e19c.md#insn-0057e1c8)
- 新版 [`0057e1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e1f0) · [`0057e1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e1f4) · [`0057e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e208)

~~~diff
- 0057e1b0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e1f0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e1b0 bytes 683700b0
+ 0057e1f0 bytes 683700d0
- 0057e1b4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0057e1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e1f4 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0057e1f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e1b4 bytes 08413d91
+ 0057e1f4 bytes 08410d91
- 0057e1c8 ["INT_ADD", "register:40f0:8", ["const:57e1c8:8", "const:4:8"]]
- 0057e1c8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0057e208 ["INT_ADD", "register:40f0:8", ["const:57e208:8", "const:4:8"]]
+ 0057e208 ["CALL", null, ["callee:00c53d00:8"]]
- 0057e1c8 bytes c6551b94
+ 0057e208 bytes be561b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dce8b47ea5bfb9e2a9ceed3a316d30c1"></a>

### [`0057e214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md) → [`0057e254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md) FUN_0057e254

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057ddd0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0057de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057de10.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e280",
      "incomplete_value": false,
      "site": "0057e284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e240",
      "incomplete_value": false,
      "site": "0057e244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
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
      "definition_site": "0057e28c",
      "incomplete_value": false,
      "site": "0057e29c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e24c",
      "incomplete_value": false,
      "site": "0057e25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0057e284",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e29c",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e284",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e29c",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md#insn-0057e29c) · [`0057e23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md#insn-0057e23c) · [`0057e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md#insn-0057e240)
- 新版 [`0057e2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e2dc) · [`0057e27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e27c) · [`0057e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e280)

~~~diff
- 0057e29c ["INT_ADD", "register:40f0:8", ["const:57e29c:8", "const:4:8"]]
- 0057e29c ["CALL", null, ["callee:00c53cd0:8"]]
+ 0057e2dc ["INT_ADD", "register:40f0:8", ["const:57e2dc:8", "const:4:8"]]
+ 0057e2dc ["CALL", null, ["callee:00c53cd0:8"]]
- 0057e29c bytes 85551b94
+ 0057e2dc bytes 7d561b94
- 0057e23c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e27c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e23c bytes 683700b0
+ 0057e27c bytes 683700d0
- 0057e240 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0057e240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e280 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0057e280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e240 bytes 08213f91
+ 0057e280 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331cea5ecd0decfe115d1a33881f996b"></a>

### [`0057e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e33c.md) → [`0057e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e37c.md) FUN_0057e37c

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
      "definition_site": "0057e380",
      "incomplete_value": false,
      "site": "0057e384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e340",
      "incomplete_value": false,
      "site": "0057e344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0057e384",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e384",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e33c.md#insn-0057e33c) · [`0057e340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e33c.md#insn-0057e340)
- 新版 [`0057e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e37c.md#insn-0057e37c) · [`0057e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e37c.md#insn-0057e380)

~~~diff
- 0057e33c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e37c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e33c bytes 683700b0
+ 0057e37c bytes 683700d0
- 0057e340 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0057e340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e380 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0057e380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e340 bytes 08213f91
+ 0057e380 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c93829edad0694ca6f24c33f3e1b71a5"></a>

### [`0057e34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e34c.md) → [`0057e38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md) FUN_0057e38c

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
      "definition_site": "0057e39c",
      "incomplete_value": false,
      "site": "0057e3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e35c",
      "incomplete_value": false,
      "site": "0057e364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
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
      "0057e3a4",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e3a4",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e34c.md#insn-0057e358) · [`0057e35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e34c.md#insn-0057e35c) · [`0057e368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e34c.md#insn-0057e368)
- 新版 [`0057e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md#insn-0057e398) · [`0057e39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md#insn-0057e39c) · [`0057e3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md#insn-0057e3a8)

~~~diff
- 0057e358 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057e398 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e358 bytes 683700b0
+ 0057e398 bytes 683700d0
- 0057e35c ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0057e35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e39c ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0057e39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e35c bytes 08213f91
+ 0057e39c bytes 08210f91
- 0057e368 ["INT_ADD", "register:40f0:8", ["const:57e368:8", "const:4:8"]]
- 0057e368 ["CALL", null, ["callee:00c57ea0:8"]]
+ 0057e3a8 ["INT_ADD", "register:40f0:8", ["const:57e3a8:8", "const:4:8"]]
+ 0057e3a8 ["CALL", null, ["callee:00c57ea0:8"]]
- 0057e368 bytes ce651b94
+ 0057e3a8 bytes be661b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4ddf5d2216bfd81c982a69e4b03889"></a>

### [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) → [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) FUN_0057e4dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00550bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bec.md) [`0057ebb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb0.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md)
- 新版 呼出元 2件 [`00550c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c2c.md) [`0057ebf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf0.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e53c",
      "incomplete_value": true,
      "site": "0057e53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e4fc",
      "incomplete_value": true,
      "site": "0057e4fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6fe:8"
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
      "definition_site": "0057e548",
      "incomplete_value": true,
      "site": "0057e554",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:ac5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e508",
      "incomplete_value": true,
      "site": "0057e514",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:a85:8"
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
      "definition_site": "0057e5f4",
      "incomplete_value": true,
      "site": "0057e5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:206:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e5b4",
      "incomplete_value": true,
      "site": "0057e5b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1c6:8"
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
      "0057e52c",
      "READ",
      [
        "storage",
        "002a66fe",
        null,
        "string"
      ]
    ],
    [
      "0057e548",
      "READ",
      [
        "storage",
        "002bda85",
        null,
        "string"
      ]
    ],
    [
      "0057e5dc",
      "READ",
      [
        "storage",
        "002b61c6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e52c",
      "READ",
      [
        "storage",
        "002a67da",
        null,
        "string"
      ]
    ],
    [
      "0057e548",
      "READ",
      [
        "storage",
        "002bdac5",
        null,
        "string"
      ]
    ],
    [
      "0057e5dc",
      "READ",
      [
        "storage",
        "002b6206",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md#insn-0057e57c) · [`0057e4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md#insn-0057e4c8) · [`0057e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md#insn-0057e4d0)
- 新版 [`0057e5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e5bc) · [`0057e508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e508) · [`0057e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e510)

~~~diff
- 0057e57c ["INT_ADD", "register:40f0:8", ["const:57e57c:8", "const:4:8"]]
- 0057e57c ["CALL", null, ["callee:00497834:8"]]
+ 0057e5bc ["INT_ADD", "register:40f0:8", ["const:57e5bc:8", "const:4:8"]]
+ 0057e5bc ["CALL", null, ["callee:00497834:8"]]
- 0057e57c bytes 9e64fc97
+ 0057e5bc bytes 9e64fc97
- 0057e4c8 ["INT_ADD", "register:40f0:8", ["const:57e4c8:8", "const:4:8"]]
- 0057e4c8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057e508 ["INT_ADD", "register:40f0:8", ["const:57e508:8", "const:4:8"]]
+ 0057e508 ["CALL", null, ["callee:00588e6c:8"]]
- 0057e4c8 bytes 592a0094
+ 0057e508 bytes 592a0094
- 0057e4d0 ["INT_ADD", "register:40f0:8", ["const:57e4d0:8", "const:4:8"]]
- 0057e4d0 ["CALL", null, ["callee:0058915c:8"]]
+ 0057e510 ["INT_ADD", "register:40f0:8", ["const:57e510:8", "const:4:8"]]
+ 0057e510 ["CALL", null, ["callee:0058915c:8"]]
- 0057e4d0 bytes 132b0094
+ 0057e510 bytes 132b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc61f98baebbe9ca751be817204f40e"></a>

### [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) → [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) FUN_0057e834

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md)
- 新版 呼出元 1件 [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e8a0",
      "incomplete_value": true,
      "site": "0057e8ac",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ac5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e860",
      "incomplete_value": true,
      "site": "0057e86c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a85:8"
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
      "definition_site": "0057e94c",
      "incomplete_value": true,
      "site": "0057e94c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:206:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e90c",
      "incomplete_value": true,
      "site": "0057e90c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1c6:8"
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
      "definition_site": "0057e954",
      "incomplete_value": true,
      "site": "0057e954",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057e914",
      "incomplete_value": true,
      "site": "0057e914",
      "value": [
        "LOAD",
        "8",
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
      "0057e884",
      "READ",
      [
        "storage",
        "002a0127",
        null,
        "string"
      ]
    ],
    [
      "0057e8a0",
      "READ",
      [
        "storage",
        "002bda85",
        null,
        "string"
      ]
    ],
    [
      "0057e934",
      "READ",
      [
        "storage",
        "002b61c6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e884",
      "READ",
      [
        "storage",
        "002a01f4",
        null,
        "string"
      ]
    ],
    [
      "0057e8a0",
      "READ",
      [
        "storage",
        "002bdac5",
        null,
        "string"
      ]
    ],
    [
      "0057e934",
      "READ",
      [
        "storage",
        "002b6206",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md#insn-0057e8d4) · [`0057e968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md#insn-0057e968) · [`0057e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md#insn-0057e820)
- 新版 [`0057e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e914) · [`0057e9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e9a8) · [`0057e860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e860)

~~~diff
- 0057e8d4 ["INT_ADD", "register:40f0:8", ["const:57e8d4:8", "const:4:8"]]
- 0057e8d4 ["CALL", null, ["callee:00497834:8"]]
+ 0057e914 ["INT_ADD", "register:40f0:8", ["const:57e914:8", "const:4:8"]]
+ 0057e914 ["CALL", null, ["callee:00497834:8"]]
- 0057e8d4 bytes c863fc97
+ 0057e914 bytes c863fc97
- 0057e968 ["INT_ADD", "register:40f0:8", ["const:57e968:8", "const:4:8"]]
- 0057e968 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057e9a8 ["INT_ADD", "register:40f0:8", ["const:57e9a8:8", "const:4:8"]]
+ 0057e9a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057e968 bytes 52641b94
+ 0057e9a8 bytes 42651b94
- 0057e820 ["INT_ADD", "register:40f0:8", ["const:57e820:8", "const:4:8"]]
- 0057e820 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057e860 ["INT_ADD", "register:40f0:8", ["const:57e860:8", "const:4:8"]]
+ 0057e860 ["CALL", null, ["callee:00588e6c:8"]]
- 0057e820 bytes 83290094
+ 0057e860 bytes 83290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-276a744a75cde638c3aa230e8da40600"></a>

### [`0057ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md) → [`0057ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md) FUN_0057ee68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057eea8",
      "incomplete_value": true,
      "site": "0057eeb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ee68",
      "incomplete_value": true,
      "site": "0057ee78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:133:8"
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
      "definition_site": "0057eebc",
      "incomplete_value": true,
      "site": "0057eebc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057ee7c",
      "incomplete_value": true,
      "site": "0057ee7c",
      "value": [
        "LOAD",
        "8",
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
      "0057eea8",
      "READ",
      [
        "storage",
        "002a0133",
        null,
        "string"
      ]
    ],
    [
      "0057eeb0",
      "READ",
      [
        "storage",
        "002a0140",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057eea8",
      "READ",
      [
        "storage",
        "002a0200",
        null,
        "string"
      ]
    ],
    [
      "0057eeb0",
      "READ",
      [
        "storage",
        "002a020d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md#insn-0057eeb8) · [`0057ee50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md#insn-0057ee50) · [`0057ee58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md#insn-0057ee58)
- 新版 [`0057eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057eef8) · [`0057ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057ee90) · [`0057ee98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057ee98)

~~~diff
- 0057eeb8 ["INT_ADD", "register:40f0:8", ["const:57eeb8:8", "const:4:8"]]
- 0057eeb8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057eef8 ["INT_ADD", "register:40f0:8", ["const:57eef8:8", "const:4:8"]]
+ 0057eef8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057eeb8 bytes fe621b94
+ 0057eef8 bytes ee631b94
- 0057ee50 ["INT_ADD", "register:40f0:8", ["const:57ee50:8", "const:4:8"]]
- 0057ee50 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057ee90 ["INT_ADD", "register:40f0:8", ["const:57ee90:8", "const:4:8"]]
+ 0057ee90 ["CALL", null, ["callee:00588e6c:8"]]
- 0057ee50 bytes f7270094
+ 0057ee90 bytes f7270094
- 0057ee58 ["INT_ADD", "register:40f0:8", ["const:57ee58:8", "const:4:8"]]
- 0057ee58 ["CALL", null, ["callee:0058915c:8"]]
+ 0057ee98 ["INT_ADD", "register:40f0:8", ["const:57ee98:8", "const:4:8"]]
+ 0057ee98 ["CALL", null, ["callee:0058915c:8"]]
- 0057ee58 bytes b1280094
+ 0057ee98 bytes b1280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8884634cf5cabc1fb951ffc23fb191e1"></a>

### [`0057ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md) → [`0057efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md) FUN_0057efdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f028",
      "incomplete_value": true,
      "site": "0057f044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057efe8",
      "incomplete_value": true,
      "site": "0057f004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d8:8"
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
      "0057f028",
      "READ",
      [
        "storage",
        "002a55d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f028",
      "READ",
      [
        "storage",
        "002a56b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md#insn-0057efc4) · [`0057f044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md#insn-0057f044) · [`0057efcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md#insn-0057efcc)
- 新版 [`0057f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f004) · [`0057f084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f084) · [`0057f00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f00c)

~~~diff
- 0057efc4 ["INT_ADD", "register:40f0:8", ["const:57efc4:8", "const:4:8"]]
- 0057efc4 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f004 ["INT_ADD", "register:40f0:8", ["const:57f004:8", "const:4:8"]]
+ 0057f004 ["CALL", null, ["callee:00588e6c:8"]]
- 0057efc4 bytes 9a270094
+ 0057f004 bytes 9a270094
- 0057f044 ["INT_ADD", "register:40f0:8", ["const:57f044:8", "const:4:8"]]
- 0057f044 ["CALL", null, ["callee:0058915c:8"]]
+ 0057f084 ["INT_ADD", "register:40f0:8", ["const:57f084:8", "const:4:8"]]
+ 0057f084 ["CALL", null, ["callee:0058915c:8"]]
- 0057f044 bytes 36280094
+ 0057f084 bytes 36280094
- 0057efcc ["INT_ADD", "register:40f0:8", ["const:57efcc:8", "const:4:8"]]
- 0057efcc ["CALL", null, ["callee:0058915c:8"]]
+ 0057f00c ["INT_ADD", "register:40f0:8", ["const:57f00c:8", "const:4:8"]]
+ 0057f00c ["CALL", null, ["callee:0058915c:8"]]
- 0057efcc bytes 54280094
+ 0057f00c bytes 54280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed474e7fdcb19f15527f057ef60df1f"></a>

### [`0057f11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md) → [`0057f15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md) FUN_0057f15c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f1a8",
      "incomplete_value": true,
      "site": "0057f1c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f168",
      "incomplete_value": true,
      "site": "0057f184",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f9:8"
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
      "0057f1a8",
      "READ",
      [
        "storage",
        "0029f0f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f1a8",
      "READ",
      [
        "storage",
        "0029f1c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md#insn-0057f144) · [`0057f1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md#insn-0057f1c4) · [`0057f14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md#insn-0057f14c)
- 新版 [`0057f184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f184) · [`0057f204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f204) · [`0057f18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f18c)

~~~diff
- 0057f144 ["INT_ADD", "register:40f0:8", ["const:57f144:8", "const:4:8"]]
- 0057f144 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f184 ["INT_ADD", "register:40f0:8", ["const:57f184:8", "const:4:8"]]
+ 0057f184 ["CALL", null, ["callee:00588e6c:8"]]
- 0057f144 bytes 3a270094
+ 0057f184 bytes 3a270094
- 0057f1c4 ["INT_ADD", "register:40f0:8", ["const:57f1c4:8", "const:4:8"]]
- 0057f1c4 ["CALL", null, ["callee:0058915c:8"]]
+ 0057f204 ["INT_ADD", "register:40f0:8", ["const:57f204:8", "const:4:8"]]
+ 0057f204 ["CALL", null, ["callee:0058915c:8"]]
- 0057f1c4 bytes d6270094
+ 0057f204 bytes d6270094
- 0057f14c ["INT_ADD", "register:40f0:8", ["const:57f14c:8", "const:4:8"]]
- 0057f14c ["CALL", null, ["callee:0058915c:8"]]
+ 0057f18c ["INT_ADD", "register:40f0:8", ["const:57f18c:8", "const:4:8"]]
+ 0057f18c ["CALL", null, ["callee:0058915c:8"]]
- 0057f14c bytes f4270094
+ 0057f18c bytes f4270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7a0906a6024fd74c179be60d4ae30a"></a>

### [`0057f294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f294.md) → [`0057f2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md) FUN_0057f2d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f320",
      "incomplete_value": true,
      "site": "0057f330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:91e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f2e0",
      "incomplete_value": true,
      "site": "0057f2f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8de:8"
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
      "definition_site": "0057f338",
      "incomplete_value": true,
      "site": "0057f338",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f2f8",
      "incomplete_value": true,
      "site": "0057f2f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f334",
      "incomplete_value": true,
      "site": "0057f34c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057f2f4",
      "incomplete_value": true,
      "site": "0057f30c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057f320",
      "READ",
      [
        "storage",
        "002ac8de",
        null,
        "string"
      ]
    ],
    [
      "0057f324",
      "READ",
      [
        "storage",
        "002ac8ed",
        null,
        "string"
      ]
    ],
    [
      "0057f334",
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
      "0057f320",
      "READ",
      [
        "storage",
        "002ac91e",
        null,
        "string"
      ]
    ],
    [
      "0057f324",
      "READ",
      [
        "storage",
        "002ac92d",
        null,
        "string"
      ]
    ],
    [
      "0057f334",
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

- 旧版 [`0057f34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f294.md#insn-0057f34c) · [`0057f2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f294.md#insn-0057f2bc) · [`0057f2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f294.md#insn-0057f2c4)
- 新版 [`0057f38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f38c) · [`0057f2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f2fc) · [`0057f304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f304)

~~~diff
- 0057f34c ["INT_ADD", "register:40f0:8", ["const:57f34c:8", "const:4:8"]]
- 0057f34c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057f38c ["INT_ADD", "register:40f0:8", ["const:57f38c:8", "const:4:8"]]
+ 0057f38c ["CALL", null, ["callee:00c57eb0:8"]]
- 0057f34c bytes d9611b94
+ 0057f38c bytes c9621b94
- 0057f2bc ["INT_ADD", "register:40f0:8", ["const:57f2bc:8", "const:4:8"]]
- 0057f2bc ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f2fc ["INT_ADD", "register:40f0:8", ["const:57f2fc:8", "const:4:8"]]
+ 0057f2fc ["CALL", null, ["callee:00588e6c:8"]]
- 0057f2bc bytes dc260094
+ 0057f2fc bytes dc260094
- 0057f2c4 ["INT_ADD", "register:40f0:8", ["const:57f2c4:8", "const:4:8"]]
- 0057f2c4 ["CALL", null, ["callee:0058915c:8"]]
+ 0057f304 ["INT_ADD", "register:40f0:8", ["const:57f304:8", "const:4:8"]]
+ 0057f304 ["CALL", null, ["callee:0058915c:8"]]
- 0057f2c4 bytes 96270094
+ 0057f304 bytes 96270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5819793e5d93569fcad5e3900f9221b6"></a>

### [`0057f424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f424.md) → [`0057f464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md) FUN_0057f464

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f4b4",
      "incomplete_value": true,
      "site": "0057f4cc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f474",
      "incomplete_value": true,
      "site": "0057f48c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e47:8"
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
      "definition_site": "0057f4d0",
      "incomplete_value": true,
      "site": "0057f4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f490",
      "incomplete_value": true,
      "site": "0057f49c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:edd:8"
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
      "definition_site": "0057f4e0",
      "incomplete_value": true,
      "site": "0057f4e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f4a0",
      "incomplete_value": true,
      "site": "0057f4a0",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057f4b4",
      "READ",
      [
        "storage",
        "002bee47",
        null,
        "string"
      ]
    ],
    [
      "0057f4d0",
      "READ",
      [
        "storage",
        "002b4edd",
        null,
        "string"
      ]
    ],
    [
      "0057f4d4",
      "READ",
      [
        "storage",
        "002b4eeb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f4b4",
      "READ",
      [
        "storage",
        "002bee87",
        null,
        "string"
      ]
    ],
    [
      "0057f4d0",
      "READ",
      [
        "storage",
        "002b4f1d",
        null,
        "string"
      ]
    ],
    [
      "0057f4d4",
      "READ",
      [
        "storage",
        "002b4f2b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f424.md#insn-0057f45c) · [`0057f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f424.md#insn-0057f454) · [`0057f468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f424.md#insn-0057f468)
- 新版 [`0057f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f49c) · [`0057f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f494) · [`0057f4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f4a8)

~~~diff
- 0057f45c ["INT_ADD", "register:40f0:8", ["const:57f45c:8", "const:4:8"]]
- 0057f45c ["CALL", null, ["callee:0058915c:8"]]
+ 0057f49c ["INT_ADD", "register:40f0:8", ["const:57f49c:8", "const:4:8"]]
+ 0057f49c ["CALL", null, ["callee:0058915c:8"]]
- 0057f45c bytes 30270094
+ 0057f49c bytes 30270094
- 0057f454 ["INT_ADD", "register:40f0:8", ["const:57f454:8", "const:4:8"]]
- 0057f454 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f494 ["INT_ADD", "register:40f0:8", ["const:57f494:8", "const:4:8"]]
+ 0057f494 ["CALL", null, ["callee:00588e6c:8"]]
- 0057f454 bytes 76260094
+ 0057f494 bytes 76260094
- 0057f468 ["COPY", "tmp:0:8", ["const:e47:8"]]
- 0057f468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f4a8 ["COPY", "tmp:0:8", ["const:e87:8"]]
+ 0057f4a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f468 bytes 291d3991
+ 0057f4a8 bytes 291d3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d2374d3a2a7b03fb98aa00690f0da3"></a>

### [`0057f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md) → [`0057f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md) FUN_0057f62c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f674",
      "incomplete_value": true,
      "site": "0057f684",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:216:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f634",
      "incomplete_value": true,
      "site": "0057f644",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1d6:8"
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
      "definition_site": "0057f6a0",
      "incomplete_value": true,
      "site": "0057f6b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f660",
      "incomplete_value": true,
      "site": "0057f670",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f2f:8"
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
      "definition_site": "0057f6a4",
      "incomplete_value": true,
      "site": "0057f6b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f664",
      "incomplete_value": true,
      "site": "0057f674",
      "value": [
        "LOAD",
        "8",
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
      "0057f674",
      "READ",
      [
        "storage",
        "002b61d6",
        null,
        "string"
      ]
    ],
    [
      "0057f6a0",
      "READ",
      [
        "storage",
        "002bff2f",
        null,
        "string"
      ]
    ],
    [
      "0057f6a4",
      "READ",
      [
        "storage",
        "002bff3f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f674",
      "READ",
      [
        "storage",
        "002b6216",
        null,
        "string"
      ]
    ],
    [
      "0057f6a0",
      "READ",
      [
        "storage",
        "002bff6f",
        null,
        "string"
      ]
    ],
    [
      "0057f6a4",
      "READ",
      [
        "storage",
        "002bff7f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md#insn-0057f6b4) · [`0057f61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md#insn-0057f61c) · [`0057f624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md#insn-0057f624)
- 新版 [`0057f6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f6f4) · [`0057f65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f65c) · [`0057f664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f664)

~~~diff
- 0057f6b4 ["INT_ADD", "register:40f0:8", ["const:57f6b4:8", "const:4:8"]]
- 0057f6b4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057f6f4 ["INT_ADD", "register:40f0:8", ["const:57f6f4:8", "const:4:8"]]
+ 0057f6f4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057f6b4 bytes ff601b94
+ 0057f6f4 bytes ef611b94
- 0057f61c ["INT_ADD", "register:40f0:8", ["const:57f61c:8", "const:4:8"]]
- 0057f61c ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f65c ["INT_ADD", "register:40f0:8", ["const:57f65c:8", "const:4:8"]]
+ 0057f65c ["CALL", null, ["callee:00588e6c:8"]]
- 0057f61c bytes 04260094
+ 0057f65c bytes 04260094
- 0057f624 ["INT_ADD", "register:40f0:8", ["const:57f624:8", "const:4:8"]]
- 0057f624 ["CALL", null, ["callee:0058915c:8"]]
+ 0057f664 ["INT_ADD", "register:40f0:8", ["const:57f664:8", "const:4:8"]]
+ 0057f664 ["CALL", null, ["callee:0058915c:8"]]
- 0057f624 bytes be260094
+ 0057f664 bytes be260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a76c158f45ffb99dec3d84b31b17b0b4"></a>

### [`0057f82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md) → [`0057f86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md) FUN_0057f86c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f8dc",
      "incomplete_value": true,
      "site": "0057f8dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f89c",
      "incomplete_value": true,
      "site": "0057f89c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ced:8"
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
      "definition_site": "0057f8f8",
      "incomplete_value": true,
      "site": "0057f908",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f8b8",
      "incomplete_value": true,
      "site": "0057f8c8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:820:8"
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
      "0057f8c8",
      "READ",
      [
        "storage",
        "002a9ced",
        null,
        "string"
      ]
    ],
    [
      "0057f8d0",
      "READ",
      [
        "storage",
        "002a9cf2",
        null,
        "string"
      ]
    ],
    [
      "0057f8f8",
      "READ",
      [
        "storage",
        "002c2820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057f8c8",
      "READ",
      [
        "storage",
        "002a9dba",
        null,
        "string"
      ]
    ],
    [
      "0057f8d0",
      "READ",
      [
        "storage",
        "002a9dbf",
        null,
        "string"
      ]
    ],
    [
      "0057f8f8",
      "READ",
      [
        "storage",
        "002c2860",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md#insn-0057f870) · [`0057f878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md#insn-0057f878) · [`0057f884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md#insn-0057f884)
- 新版 [`0057f8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8b0) · [`0057f8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8b8) · [`0057f8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8c4)

~~~diff
- 0057f870 ["INT_ADD", "register:40f0:8", ["const:57f870:8", "const:4:8"]]
- 0057f870 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057f8b0 ["INT_ADD", "register:40f0:8", ["const:57f8b0:8", "const:4:8"]]
+ 0057f8b0 ["CALL", null, ["callee:00588e6c:8"]]
- 0057f870 bytes 6f250094
+ 0057f8b0 bytes 6f250094
- 0057f878 ["INT_ADD", "register:40f0:8", ["const:57f878:8", "const:4:8"]]
- 0057f878 ["CALL", null, ["callee:0058915c:8"]]
+ 0057f8b8 ["INT_ADD", "register:40f0:8", ["const:57f8b8:8", "const:4:8"]]
+ 0057f8b8 ["CALL", null, ["callee:0058915c:8"]]
- 0057f878 bytes 29260094
+ 0057f8b8 bytes 29260094
- 0057f884 ["COPY", "tmp:0:8", ["const:ced:8"]]
- 0057f884 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f884 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f884 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f8c4 ["COPY", "tmp:0:8", ["const:dba:8"]]
+ 0057f8c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f8c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f8c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f884 bytes 29b53391
+ 0057f8c4 bytes 29e93691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dcb7dabd0b264e6c1f378ef1a631204"></a>

### [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) → [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) FUN_0057fb0c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00555258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555258.md) [`0057fce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fce0.md) [`0057fd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md) [`0057fe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md) [`0057febc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057febc.md) · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 6件 [`00555298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555298.md) [`0057fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md) [`0057fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md) [`0057fe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md) [`0057fefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md) · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fb70",
      "incomplete_value": true,
      "site": "0057fb70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cde:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fb30",
      "incomplete_value": true,
      "site": "0057fb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9e:8"
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
      "definition_site": "0057fb78",
      "incomplete_value": true,
      "site": "0057fb78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fb38",
      "incomplete_value": true,
      "site": "0057fb38",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fb74",
      "incomplete_value": true,
      "site": "0057fb88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fb34",
      "incomplete_value": true,
      "site": "0057fb48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f5:8"
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
      "0057fb58",
      "READ",
      [
        "storage",
        "002b2c9e",
        null,
        "string"
      ]
    ],
    [
      "0057fb60",
      "READ",
      [
        "storage",
        "002b2ca3",
        null,
        "string"
      ]
    ],
    [
      "0057fb74",
      "READ",
      [
        "storage",
        "002a11f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fb58",
      "READ",
      [
        "storage",
        "002b2cde",
        null,
        "string"
      ]
    ],
    [
      "0057fb60",
      "READ",
      [
        "storage",
        "002b2ce3",
        null,
        "string"
      ]
    ],
    [
      "0057fb74",
      "READ",
      [
        "storage",
        "002a12c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md#insn-0057fb08) · [`0057fc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md#insn-0057fc5c) · [`0057fb00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md#insn-0057fb00)
- 新版 [`0057fb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fb48) · [`0057fc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fc9c) · [`0057fb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fb40)

~~~diff
- 0057fb08 ["INT_ADD", "register:40f0:8", ["const:57fb08:8", "const:4:8"]]
- 0057fb08 ["CALL", null, ["callee:0058915c:8"]]
+ 0057fb48 ["INT_ADD", "register:40f0:8", ["const:57fb48:8", "const:4:8"]]
+ 0057fb48 ["CALL", null, ["callee:0058915c:8"]]
- 0057fb08 bytes 85250094
+ 0057fb48 bytes 85250094
- 0057fc5c ["INT_ADD", "register:40f0:8", ["const:57fc5c:8", "const:4:8"]]
- 0057fc5c ["CALL", null, ["callee:0058a8bc:8"]]
+ 0057fc9c ["INT_ADD", "register:40f0:8", ["const:57fc9c:8", "const:4:8"]]
+ 0057fc9c ["CALL", null, ["callee:0058a8bc:8"]]
- 0057fc5c bytes 082b0094
+ 0057fc9c bytes 082b0094
- 0057fb00 ["INT_ADD", "register:40f0:8", ["const:57fb00:8", "const:4:8"]]
- 0057fb00 ["CALL", null, ["callee:00588e6c:8"]]
+ 0057fb40 ["INT_ADD", "register:40f0:8", ["const:57fb40:8", "const:4:8"]]
+ 0057fb40 ["CALL", null, ["callee:00588e6c:8"]]
- 0057fb00 bytes cb240094
+ 0057fb40 bytes cb240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-314961670a7821648f099e1b3fa712df"></a>

### [`0057fd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md) → [`0057fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md) FUN_0057fda8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00555260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555260.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005552a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a0.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fde4",
      "incomplete_value": true,
      "site": "0057fde4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:936:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fda4",
      "incomplete_value": true,
      "site": "0057fda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f6:8"
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
      "0057fdc8",
      "READ",
      [
        "storage",
        "002ac8f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fdc8",
      "READ",
      [
        "storage",
        "002ac936",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md#insn-0057fd80) · [`0057fdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md#insn-0057fdb0) · [`0057fdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fd68.md#insn-0057fdc0)
- 新版 [`0057fdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fdc0) · [`0057fdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fdf0) · [`0057fe00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fe00)

~~~diff
- 0057fd80 ["COPY", "tmp:0:8", ["const:8f6:8"]]
- 0057fd80 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0057fd80 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0057fd80 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0057fdc0 ["COPY", "tmp:0:8", ["const:936:8"]]
+ 0057fdc0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fdc0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fdc0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0057fd80 bytes 6bd92391
+ 0057fdc0 bytes 6bd92491
- 0057fdb0 ["INT_ADD", "register:40f0:8", ["const:57fdb0:8", "const:4:8"]]
- 0057fdb0 ["CALL", null, ["callee:0057fb0c:8"]]
+ 0057fdf0 ["INT_ADD", "register:40f0:8", ["const:57fdf0:8", "const:4:8"]]
+ 0057fdf0 ["CALL", null, ["callee:0057fb0c:8"]]
- 0057fdb0 bytes 47ffff97
+ 0057fdf0 bytes 47ffff97
- 0057fdc0 ["INT_ADD", "register:40f0:8", ["const:57fdc0:8", "const:4:8"]]
- 0057fdc0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057fe00 ["INT_ADD", "register:40f0:8", ["const:57fe00:8", "const:4:8"]]
+ 0057fe00 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057fdc0 bytes 3c5f1b94
+ 0057fe00 bytes 2c601b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935d3905418b49a46d1cfa1becec09c6"></a>

### [`0057fe14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md) → [`0057fe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md) FUN_0057fe54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00555264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555264.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005552a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a4.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fe88",
      "incomplete_value": true,
      "site": "0057fe88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fe48",
      "incomplete_value": true,
      "site": "0057fe48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:410:8"
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
      "definition_site": "0057fe8c",
      "incomplete_value": true,
      "site": "0057fe8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fe4c",
      "incomplete_value": true,
      "site": "0057fe4c",
      "value": [
        "LOAD",
        "8",
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
      "0057fe74",
      "READ",
      [
        "storage",
        "002ba410",
        null,
        "string"
      ]
    ],
    [
      "0057fe80",
      "READ",
      [
        "storage",
        "002ba416",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fe74",
      "READ",
      [
        "storage",
        "002ba450",
        null,
        "string"
      ]
    ],
    [
      "0057fe80",
      "READ",
      [
        "storage",
        "002ba456",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fe2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md#insn-0057fe2c) · [`0057fe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md#insn-0057fe58) · [`0057fe68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057fe14.md#insn-0057fe68)
- 新版 [`0057fe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fe6c) · [`0057fe98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fe98) · [`0057fea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fea8)

~~~diff
- 0057fe2c ["COPY", "tmp:0:8", ["const:410:8"]]
- 0057fe2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057fe2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057fe2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057fe6c ["COPY", "tmp:0:8", ["const:450:8"]]
+ 0057fe6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fe6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fe6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057fe2c bytes 4a411091
+ 0057fe6c bytes 4a411191
- 0057fe58 ["INT_ADD", "register:40f0:8", ["const:57fe58:8", "const:4:8"]]
- 0057fe58 ["CALL", null, ["callee:0057fb0c:8"]]
+ 0057fe98 ["INT_ADD", "register:40f0:8", ["const:57fe98:8", "const:4:8"]]
+ 0057fe98 ["CALL", null, ["callee:0057fb0c:8"]]
- 0057fe58 bytes 1dffff97
+ 0057fe98 bytes 1dffff97
- 0057fe68 ["INT_ADD", "register:40f0:8", ["const:57fe68:8", "const:4:8"]]
- 0057fe68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057fea8 ["INT_ADD", "register:40f0:8", ["const:57fea8:8", "const:4:8"]]
+ 0057fea8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057fe68 bytes 125f1b94
+ 0057fea8 bytes 02601b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570997b5129a8a0c11d533933d38d52c"></a>

### [`0057ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057ff60.md) → [`0057ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md) FUN_0057ffa0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/0055526c.md) · 呼出先 3件 [`0057facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057facc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005552ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552ac.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ffd4",
      "incomplete_value": true,
      "site": "0057ffd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ff94",
      "incomplete_value": true,
      "site": "0057ff94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae1:8"
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
      "definition_site": "0057ffd8",
      "incomplete_value": true,
      "site": "0057ffd8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057ff98",
      "incomplete_value": true,
      "site": "0057ff98",
      "value": [
        "LOAD",
        "8",
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
      "0057ffc0",
      "READ",
      [
        "storage",
        "002afae1",
        null,
        "string"
      ]
    ],
    [
      "0057ffcc",
      "READ",
      [
        "storage",
        "002afae6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ffc0",
      "READ",
      [
        "storage",
        "002afb21",
        null,
        "string"
      ]
    ],
    [
      "0057ffcc",
      "READ",
      [
        "storage",
        "002afb26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ff78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057ff60.md#insn-0057ff78) · [`0057ffa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057ff60.md#insn-0057ffa4) · [`0057ffb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057ff60.md#insn-0057ffb4)
- 新版 [`0057ffb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057ffb8) · [`0057ffe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057ffe4) · [`0057fff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057fff4)

~~~diff
- 0057ff78 ["COPY", "tmp:0:8", ["const:ae1:8"]]
- 0057ff78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057ff78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057ff78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057ffb8 ["COPY", "tmp:0:8", ["const:b21:8"]]
+ 0057ffb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057ffb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057ffb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057ff78 bytes 4a852b91
+ 0057ffb8 bytes 4a852c91
- 0057ffa4 ["INT_ADD", "register:40f0:8", ["const:57ffa4:8", "const:4:8"]]
- 0057ffa4 ["CALL", null, ["callee:0057fb0c:8"]]
+ 0057ffe4 ["INT_ADD", "register:40f0:8", ["const:57ffe4:8", "const:4:8"]]
+ 0057ffe4 ["CALL", null, ["callee:0057fb0c:8"]]
- 0057ffa4 bytes cafeff97
+ 0057ffe4 bytes cafeff97
- 0057ffb4 ["INT_ADD", "register:40f0:8", ["const:57ffb4:8", "const:4:8"]]
- 0057ffb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0057fff4 ["INT_ADD", "register:40f0:8", ["const:57fff4:8", "const:4:8"]]
+ 0057fff4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0057ffb4 bytes bf5e1b94
+ 0057fff4 bytes af5f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe85b6526a9b191600d7836b59aa4185"></a>

### [`00580008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580008.md) → [`00580048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580048.md) FUN_00580048

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
      "definition_site": "0058004c",
      "incomplete_value": false,
      "site": "00580050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058000c",
      "incomplete_value": false,
      "site": "00580010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "00580050",
      "DATA",
      [
        "storage",
        "00c6c0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580050",
      "DATA",
      [
        "storage",
        "00c6c4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058000c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580008.md#insn-0058000c)
- 新版 [`0058004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580048.md#insn-0058004c)

~~~diff
- 0058000c ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0058000c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058000c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058000c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058004c ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0058004c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058004c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058004c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058000c bytes 08010391
+ 0058004c bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2bec13eca6da68e3f71bb34df880f31"></a>

### [`00580018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580018.md) → [`00580058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md) FUN_00580058

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
      "definition_site": "00580068",
      "incomplete_value": false,
      "site": "00580070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580028",
      "incomplete_value": false,
      "site": "00580030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "00580070",
      "DATA",
      [
        "storage",
        "00c6c0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580070",
      "DATA",
      [
        "storage",
        "00c6c4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580018.md#insn-00580028) · [`00580034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580018.md#insn-00580034)
- 新版 [`00580068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md#insn-00580068) · [`00580074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md#insn-00580074)

~~~diff
- 00580028 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 00580028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580068 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00580068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580028 bytes 08010391
+ 00580068 bytes 08011391
- 00580034 ["INT_ADD", "register:40f0:8", ["const:580034:8", "const:4:8"]]
- 00580034 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00580074 ["INT_ADD", "register:40f0:8", ["const:580074:8", "const:4:8"]]
+ 00580074 ["CALL", null, ["callee:00c57ea0:8"]]
- 00580034 bytes 9b5e1b94
+ 00580074 bytes 8b5f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a02a6db67269b97c4e901b49c3b4463"></a>

### [`00580058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md) → [`00580098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md) FUN_00580098

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c690.md) · 呼出先 17件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`0055c694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c694.md) [`0055c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c69c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)
- 新版 呼出元 1件 [`0055c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6d0.md) · 呼出先 17件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`0055c6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6d4.md) [`0055c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6dc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.14% / 新版 94.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580100",
      "incomplete_value": true,
      "site": "00580100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800c0",
      "incomplete_value": true,
      "site": "005800c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cac:8"
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
      "definition_site": "0058011c",
      "incomplete_value": true,
      "site": "00580124",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800dc",
      "incomplete_value": true,
      "site": "005800e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e0:8"
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
      "definition_site": "00580118",
      "incomplete_value": true,
      "site": "00580128",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005800d8",
      "incomplete_value": true,
      "site": "005800e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:890:8"
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
      "005800ec",
      "READ",
      [
        "storage",
        "002b2cac",
        null,
        "string"
      ]
    ],
    [
      "00580118",
      "READ",
      [
        "storage",
        "002ad890",
        null,
        "string"
      ]
    ],
    [
      "00580118",
      "READ",
      [
        "storage",
        "002ad8a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005800ec",
      "READ",
      [
        "storage",
        "002b2cec",
        null,
        "string"
      ]
    ],
    [
      "00580118",
      "READ",
      [
        "storage",
        "002ad8d0",
        null,
        "string"
      ]
    ],
    [
      "00580118",
      "READ",
      [
        "storage",
        "002ad8e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md#insn-00580124) · [`0058013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md#insn-0058013c) · [`0058008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580058.md#insn-0058008c)
- 新版 [`00580164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-00580164) · [`0058017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-0058017c) · [`005800cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-005800cc)

~~~diff
- 00580124 ["INT_ADD", "register:40f0:8", ["const:580124:8", "const:4:8"]]
- 00580124 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00580164 ["INT_ADD", "register:40f0:8", ["const:580164:8", "const:4:8"]]
+ 00580164 ["CALL", null, ["callee:00c57eb0:8"]]
- 00580124 bytes 635e1b94
+ 00580164 bytes 535f1b94
- 0058013c ["INT_ADD", "register:40f0:8", ["const:58013c:8", "const:4:8"]]
- 0058013c ["CALL", null, ["callee:00589144:8"]]
+ 0058017c ["INT_ADD", "register:40f0:8", ["const:58017c:8", "const:4:8"]]
+ 0058017c ["CALL", null, ["callee:00589144:8"]]
- 0058013c bytes f2230094
+ 0058017c bytes f2230094
- 0058008c ["INT_ADD", "register:40f0:8", ["const:58008c:8", "const:4:8"]]
- 0058008c ["CALL", null, ["callee:00588e6c:8"]]
+ 005800cc ["INT_ADD", "register:40f0:8", ["const:5800cc:8", "const:4:8"]]
+ 005800cc ["CALL", null, ["callee:00588e6c:8"]]
- 0058008c bytes 68230094
+ 005800cc bytes 68230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be842b9af8ba06c3d17d2751c9b22f4"></a>

### [`00580464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md) → [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) FUN_005804a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e0.md) · 呼出先 20件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) [`0057dda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057dda8.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`0055c820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c820.md) · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) [`0057dde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005804f8",
      "incomplete_value": true,
      "site": "005804f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:ad6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005804b8",
      "incomplete_value": true,
      "site": "005804b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:a96:8"
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
      "definition_site": "00580518",
      "incomplete_value": true,
      "site": "00580520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005804d8",
      "incomplete_value": true,
      "site": "005804e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580514",
      "incomplete_value": true,
      "site": "00580524",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:982:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005804d4",
      "incomplete_value": true,
      "site": "005804e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a6:8"
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
      "005804e8",
      "READ",
      [
        "storage",
        "002bda96",
        null,
        "string"
      ]
    ],
    [
      "00580514",
      "READ",
      [
        "storage",
        "002a78a6",
        null,
        "string"
      ]
    ],
    [
      "00580514",
      "READ",
      [
        "storage",
        "002a78b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005804e8",
      "READ",
      [
        "storage",
        "002bdad6",
        null,
        "string"
      ]
    ],
    [
      "00580514",
      "READ",
      [
        "storage",
        "002a7982",
        null,
        "string"
      ]
    ],
    [
      "00580514",
      "READ",
      [
        "storage",
        "002a7992",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005804a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md#insn-005804a0) · [`0058055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md#insn-0058055c) · [`00580490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580464.md#insn-00580490)
- 新版 [`005804e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-005804e0) · [`0058059c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-0058059c) · [`005804d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-005804d0)

~~~diff
- 005804a0 ["COPY", "tmp:0:8", ["const:a96:8"]]
- 005804a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005804a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005804a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005804e0 ["COPY", "tmp:0:8", ["const:ad6:8"]]
+ 005804e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005804e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005804e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005804a0 bytes 29592a91
+ 005804e0 bytes 29592b91
- 0058055c ["INT_ADD", "register:40f0:8", ["const:58055c:8", "const:4:8"]]
- 0058055c ["CALL", null, ["callee:00c58610:8"]]
+ 0058059c ["INT_ADD", "register:40f0:8", ["const:58059c:8", "const:4:8"]]
+ 0058059c ["CALL", null, ["callee:00c58610:8"]]
- 0058055c bytes 2d5f1b94
+ 0058059c bytes 1d601b94
- 00580490 ["INT_ADD", "register:40f0:8", ["const:580490:8", "const:4:8"]]
- 00580490 ["CALL", null, ["callee:00588e6c:8"]]
+ 005804d0 ["INT_ADD", "register:40f0:8", ["const:5804d0:8", "const:4:8"]]
+ 005804d0 ["CALL", null, ["callee:00588e6c:8"]]
- 00580490 bytes 67220094
+ 005804d0 bytes 67220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e255697d6ab142282509e6a6c1794251"></a>

### [`00580848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md) → [`00580888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md) FUN_00580888

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560414.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00560454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560454.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005808fc",
      "incomplete_value": true,
      "site": "0058090c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:216:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005808bc",
      "incomplete_value": true,
      "site": "005808cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:149:8"
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
      "definition_site": "00580900",
      "incomplete_value": true,
      "site": "00580910",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005808c0",
      "incomplete_value": true,
      "site": "005808d0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580904",
      "incomplete_value": true,
      "site": "00580914",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005808c4",
      "incomplete_value": true,
      "site": "005808d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "005808d0",
      "READ",
      [
        "storage",
        "002c128c",
        null,
        "string"
      ]
    ],
    [
      "005808fc",
      "READ",
      [
        "storage",
        "002a0149",
        null,
        "string"
      ]
    ],
    [
      "00580900",
      "READ",
      [
        "storage",
        "002a0159",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005808d0",
      "READ",
      [
        "storage",
        "002c12cc",
        null,
        "string"
      ]
    ],
    [
      "005808fc",
      "READ",
      [
        "storage",
        "002a0216",
        null,
        "string"
      ]
    ],
    [
      "00580900",
      "READ",
      [
        "storage",
        "002a0226",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md#insn-00580910) · [`00580874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md#insn-00580874) · [`0058087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580848.md#insn-0058087c)
- 新版 [`00580950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-00580950) · [`005808b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-005808b4) · [`005808bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-005808bc)

~~~diff
- 00580910 ["INT_ADD", "register:40f0:8", ["const:580910:8", "const:4:8"]]
- 00580910 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00580950 ["INT_ADD", "register:40f0:8", ["const:580950:8", "const:4:8"]]
+ 00580950 ["CALL", null, ["callee:00c57eb0:8"]]
- 00580910 bytes 685c1b94
+ 00580950 bytes 585d1b94
- 00580874 ["INT_ADD", "register:40f0:8", ["const:580874:8", "const:4:8"]]
- 00580874 ["CALL", null, ["callee:00588e6c:8"]]
+ 005808b4 ["INT_ADD", "register:40f0:8", ["const:5808b4:8", "const:4:8"]]
+ 005808b4 ["CALL", null, ["callee:00588e6c:8"]]
- 00580874 bytes 6e210094
+ 005808b4 bytes 6e210094
- 0058087c ["INT_ADD", "register:40f0:8", ["const:58087c:8", "const:4:8"]]
- 0058087c ["CALL", null, ["callee:0058915c:8"]]
+ 005808bc ["INT_ADD", "register:40f0:8", ["const:5808bc:8", "const:4:8"]]
+ 005808bc ["CALL", null, ["callee:0058915c:8"]]
- 0058087c bytes 28220094
+ 005808bc bytes 28220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e0bfd584020f15a0f68039225a917c3"></a>

### [`00580af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md) → [`00580b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md) FUN_00580b30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056041c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056041c.md) · 呼出先 8件 [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0056045c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056045c.md) · 呼出先 8件 [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580b94",
      "incomplete_value": false,
      "site": "00580ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580b54",
      "incomplete_value": false,
      "site": "00580b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "00580ba0",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00580ba0",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md#insn-00580b40) · [`00580b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md#insn-00580b48) · [`00580b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580af0.md#insn-00580b50)
- 新版 [`00580b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b80) · [`00580b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b88) · [`00580b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b90)

~~~diff
- 00580b40 ["INT_ADD", "register:40f0:8", ["const:580b40:8", "const:4:8"]]
- 00580b40 ["CALL", null, ["callee:00c59160:8"]]
+ 00580b80 ["INT_ADD", "register:40f0:8", ["const:580b80:8", "const:4:8"]]
+ 00580b80 ["CALL", null, ["callee:00c59160:8"]]
- 00580b40 bytes 88601b94
+ 00580b80 bytes 78611b94
- 00580b48 ["INT_ADD", "register:40f0:8", ["const:580b48:8", "const:4:8"]]
- 00580b48 ["CALL", null, ["callee:00c57e90:8"]]
+ 00580b88 ["INT_ADD", "register:40f0:8", ["const:580b88:8", "const:4:8"]]
+ 00580b88 ["CALL", null, ["callee:00c57e90:8"]]
- 00580b48 bytes d25b1b94
+ 00580b88 bytes c25c1b94
- 00580b50 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00580b90 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00580b50 bytes 483700f0
+ 00580b90 bytes 68370090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ddd998738f00acb01e39df28f133336"></a>

### [`00580c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md) → [`00580ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md) FUN_00580ca0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec40.md) · 呼出先 9件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00536e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536e48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`0055ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec80.md) · 呼出先 9件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580d60",
      "incomplete_value": true,
      "site": "00580d60",
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
      "definition_site": "00580d20",
      "incomplete_value": true,
      "site": "00580d20",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580db4",
      "incomplete_value": false,
      "site": "00580dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580d74",
      "incomplete_value": false,
      "site": "00580d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "definition_site": "00580dcc",
      "incomplete_value": false,
      "site": "00580dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580d8c",
      "incomplete_value": false,
      "site": "00580d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "00580d48",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00580d60",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580dbc",
      "DATA",
      [
        "storage",
        "00c6c160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580d48",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00580d60",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580dbc",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md#insn-00580ce0) · [`00580d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md#insn-00580d4c) · [`00580dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00580/00580c60.md#insn-00580dac)
- 新版 [`00580d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580d20) · [`00580d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580d8c) · [`00580dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580dec)

~~~diff
- 00580ce0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580ce0 ["INT_ADD", "register:40f0:8", ["const:580ce0:8", "const:4:8"]]
- 00580ce0 ["CALLIND", null, ["register:0:8"]]
+ 00580d20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580d20 ["INT_ADD", "register:40f0:8", ["const:580d20:8", "const:4:8"]]
+ 00580d20 ["CALLIND", null, ["register:0:8"]]
- 00580ce0 bytes 20013fd6
+ 00580d20 bytes 20013fd6
- 00580d4c ["INT_ADD", "register:40f0:8", ["const:580d4c:8", "const:4:8"]]
- 00580d4c ["CALL", null, ["callee:00c58000:8"]]
+ 00580d8c ["INT_ADD", "register:40f0:8", ["const:580d8c:8", "const:4:8"]]
+ 00580d8c ["CALL", null, ["callee:00c58000:8"]]
- 00580d4c bytes ad5b1b94
+ 00580d8c bytes 9d5c1b94
- 00580dac ["COPY", "register:0:8", ["register:4048:8"]]
- 00580dac ["INT_ADD", "register:40f0:8", ["const:580dac:8", "const:4:8"]]
- 00580dac ["CALLIND", null, ["register:0:8"]]
+ 00580dec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580dec ["INT_ADD", "register:40f0:8", ["const:580dec:8", "const:4:8"]]
+ 00580dec ["CALLIND", null, ["register:0:8"]]
- 00580dac bytes 20013fd6
+ 00580dec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fb55f80edb575ad9ecd8bdfe7c11a0"></a>

### [`00581008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581008.md) → [`00581048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md) FUN_00581048

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec44.md) · 呼出先 12件 [`005975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975cc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0055ec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec84.md) · 呼出先 12件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005810e8",
      "incomplete_value": true,
      "site": "005810e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005810a8",
      "incomplete_value": true,
      "site": "005810a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a53:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00581084",
      "incomplete_value": false,
      "site": "00581094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581044",
      "incomplete_value": false,
      "site": "00581054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "definition_site": "0058108c",
      "incomplete_value": false,
      "site": "00581094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058104c",
      "incomplete_value": false,
      "site": "00581054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "00581084",
      "PARAM",
      [
        "storage",
        "00c6c1c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0058108c",
      "PARAM",
      [
        "storage",
        "00c6c268",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005810c8",
      "READ",
      [
        "storage",
        "002aea53",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581084",
      "PARAM",
      [
        "storage",
        "00c6c5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0058108c",
      "PARAM",
      [
        "storage",
        "00c6c668",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005810c8",
      "READ",
      [
        "storage",
        "002aea93",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581008.md#insn-00581054) · [`00581044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581008.md#insn-00581044) · [`0058104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581008.md#insn-0058104c)
- 新版 [`00581094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-00581094) · [`00581084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-00581084) · [`0058108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-0058108c)

~~~diff
- 00581054 ["INT_ADD", "register:40f0:8", ["const:581054:8", "const:4:8"]]
- 00581054 ["CALL", null, ["callee:00c58610:8"]]
+ 00581094 ["INT_ADD", "register:40f0:8", ["const:581094:8", "const:4:8"]]
+ 00581094 ["CALL", null, ["callee:00c58610:8"]]
- 00581054 bytes 6f5c1b94
+ 00581094 bytes 5f5d1b94
- 00581044 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00581044 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00581044 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00581044 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00581084 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 00581084 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00581084 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00581084 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00581044 bytes 21200791
+ 00581084 bytes 21201791
- 0058104c ["COPY", "tmp:0:8", ["const:268:8"]]
- 0058104c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0058104c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0058104c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0058108c ["COPY", "tmp:0:8", ["const:668:8"]]
+ 0058108c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0058108c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0058108c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0058104c bytes 42a00991
+ 0058108c bytes 42a01991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e876e4ae2589b859b161762395a5f18"></a>

### [`0058123c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/0058123c.md) → [`0058127c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md) FUN_0058127c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ec48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ec48.md) · 呼出先 10件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0055ec88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec88.md) · 呼出先 10件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.99% / 新版 90.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581308",
      "incomplete_value": true,
      "site": "00581318",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005812c8",
      "incomplete_value": true,
      "site": "005812d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aef:8"
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
      "definition_site": "0058130c",
      "incomplete_value": true,
      "site": "0058131c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005812cc",
      "incomplete_value": true,
      "site": "005812dc",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581310",
      "incomplete_value": true,
      "site": "00581320",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005812d0",
      "incomplete_value": true,
      "site": "005812e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "005812b8",
      "PARAM",
      [
        "storage",
        "00c6c1c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005812c0",
      "PARAM",
      [
        "storage",
        "00c6c1d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581308",
      "READ",
      [
        "storage",
        "002afaef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005812b8",
      "PARAM",
      [
        "storage",
        "00c6c5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005812c0",
      "PARAM",
      [
        "storage",
        "00c6c5d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581308",
      "READ",
      [
        "storage",
        "002afb2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/0058123c.md#insn-0058128c) · [`00581320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/0058123c.md#insn-00581320) · [`00581278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/0058123c.md#insn-00581278)
- 新版 [`005812cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-005812cc) · [`00581360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-00581360) · [`005812b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-005812b8)

~~~diff
- 0058128c ["INT_ADD", "register:40f0:8", ["const:58128c:8", "const:4:8"]]
- 0058128c ["CALL", null, ["callee:00c58610:8"]]
+ 005812cc ["INT_ADD", "register:40f0:8", ["const:5812cc:8", "const:4:8"]]
+ 005812cc ["CALL", null, ["callee:00c58610:8"]]
- 0058128c bytes e15b1b94
+ 005812cc bytes d15c1b94
- 00581320 ["INT_ADD", "register:40f0:8", ["const:581320:8", "const:4:8"]]
- 00581320 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00581360 ["INT_ADD", "register:40f0:8", ["const:581360:8", "const:4:8"]]
+ 00581360 ["CALL", null, ["callee:00c57eb0:8"]]
- 00581320 bytes e4591b94
+ 00581360 bytes d45a1b94
- 00581278 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00581278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00581278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00581278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005812b8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 005812b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005812b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005812b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00581278 bytes 21200791
+ 005812b8 bytes 21201791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4274206ee9c6a64f6dbf8c75c190facf"></a>

### [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) → [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) FUN_00581494

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`0055ed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.36% / 新版 92.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581518",
      "incomplete_value": true,
      "site": "0058152c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005814d8",
      "incomplete_value": true,
      "site": "005814ec",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581518",
      "incomplete_value": true,
      "site": "0058152c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005814d8",
      "incomplete_value": true,
      "site": "005814ec",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581524",
      "incomplete_value": true,
      "site": "00581530",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005814e4",
      "incomplete_value": true,
      "site": "005814f0",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
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
      "0058150c",
      "READ",
      [
        "storage",
        "002c2e90",
        null,
        null
      ]
    ],
    [
      "00581518",
      "READ",
      [
        "storage",
        "002b7456",
        null,
        "string"
      ]
    ],
    [
      "00581518",
      "READ",
      [
        "storage",
        "002b7466",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058150c",
      "READ",
      [
        "storage",
        "002c2ed0",
        null,
        null
      ]
    ],
    [
      "00581518",
      "READ",
      [
        "storage",
        "002b7496",
        null,
        "string"
      ]
    ],
    [
      "00581518",
      "READ",
      [
        "storage",
        "002b74a6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005814bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md#insn-005814bc) · [`0058153c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md#insn-0058153c) · [`005815dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md#insn-005815dc)
- 新版 [`005814fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-005814fc) · [`0058157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-0058157c) · [`0058161c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-0058161c)

~~~diff
- 005814bc ["INT_ADD", "register:40f0:8", ["const:5814bc:8", "const:4:8"]]
- 005814bc ["CALL", null, ["callee:00c57e90:8"]]
+ 005814fc ["INT_ADD", "register:40f0:8", ["const:5814fc:8", "const:4:8"]]
+ 005814fc ["CALL", null, ["callee:00c57e90:8"]]
- 005814bc bytes 75591b94
+ 005814fc bytes 655a1b94
- 0058153c ["INT_ADD", "register:40f0:8", ["const:58153c:8", "const:4:8"]]
- 0058153c ["CALL", null, ["callee:00589144:8"]]
+ 0058157c ["INT_ADD", "register:40f0:8", ["const:58157c:8", "const:4:8"]]
+ 0058157c ["CALL", null, ["callee:00589144:8"]]
- 0058153c bytes f21e0094
+ 0058157c bytes f21e0094
- 005815dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005815dc ["INT_ADD", "register:40f0:8", ["const:5815dc:8", "const:4:8"]]
- 005815dc ["CALLIND", null, ["register:0:8"]]
+ 0058161c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058161c ["INT_ADD", "register:40f0:8", ["const:58161c:8", "const:4:8"]]
+ 0058161c ["CALLIND", null, ["register:0:8"]]
- 005815dc bytes 00013fd6
+ 0058161c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39f93035cdf40692dc38c521a61249e4"></a>

### [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) → [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) FUN_00581764

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055f054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f054.md) [`0055f058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f058.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 2件 [`0055f094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f094.md) [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005817dc",
      "incomplete_value": true,
      "site": "005817f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058179c",
      "incomplete_value": true,
      "site": "005817b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e90:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581920",
      "incomplete_value": false,
      "site": "0058192c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005818e0",
      "incomplete_value": false,
      "site": "005818ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "005817dc",
      "READ",
      [
        "storage",
        "002c2e90",
        null,
        null
      ]
    ],
    [
      "005817e8",
      "READ",
      [
        "storage",
        "002b7456",
        null,
        "string"
      ]
    ],
    [
      "005817e8",
      "READ",
      [
        "storage",
        "002b7466",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005817dc",
      "READ",
      [
        "storage",
        "002c2ed0",
        null,
        null
      ]
    ],
    [
      "005817e8",
      "READ",
      [
        "storage",
        "002b7496",
        null,
        "string"
      ]
    ],
    [
      "005817e8",
      "READ",
      [
        "storage",
        "002b74a6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005818ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md#insn-005818ac) · [`00581758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md#insn-00581758) · [`00581760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md#insn-00581760)
- 新版 [`005818ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-005818ec) · [`00581798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-00581798) · [`005817a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-005817a0)

~~~diff
- 005818ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005818ac ["INT_ADD", "register:40f0:8", ["const:5818ac:8", "const:4:8"]]
- 005818ac ["CALLIND", null, ["register:0:8"]]
+ 005818ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005818ec ["INT_ADD", "register:40f0:8", ["const:5818ec:8", "const:4:8"]]
+ 005818ec ["CALLIND", null, ["register:0:8"]]
- 005818ac bytes 00013fd6
+ 005818ec bytes 00013fd6
- 00581758 ["INT_ADD", "register:40f0:8", ["const:581758:8", "const:4:8"]]
- 00581758 ["CALL", null, ["callee:00588e6c:8"]]
+ 00581798 ["INT_ADD", "register:40f0:8", ["const:581798:8", "const:4:8"]]
+ 00581798 ["CALL", null, ["callee:00588e6c:8"]]
- 00581758 bytes b51d0094
+ 00581798 bytes b51d0094
- 00581760 ["INT_ADD", "register:40f0:8", ["const:581760:8", "const:4:8"]]
- 00581760 ["CALL", null, ["callee:0058915c:8"]]
+ 005817a0 ["INT_ADD", "register:40f0:8", ["const:5817a0:8", "const:4:8"]]
+ 005817a0 ["CALL", null, ["callee:0058915c:8"]]
- 00581760 bytes 6f1e0094
+ 005817a0 bytes 6f1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25616508325fa43ef29a7a950ddfd899"></a>

### [`005819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md) → [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) FUN_00581a34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0055e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e710.md) [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md) · 呼出先 2件 [`00582778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582778.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) · 呼出先 2件 [`005827b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00581a5c",
      "incomplete_value": false,
      "site": "00581a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581a1c",
      "incomplete_value": false,
      "site": "00581a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00581a68",
      "DATA",
      [
        "storage",
        "00c6c348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581a68",
      "DATA",
      [
        "storage",
        "00c6c748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md#insn-00581a10) · [`00581a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md#insn-00581a1c) · [`00581a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/005819f4.md#insn-00581a34)
- 新版 [`00581a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a50) · [`00581a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a5c) · [`00581a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a74)

~~~diff
- 00581a10 ["INT_ADD", "register:40f0:8", ["const:581a10:8", "const:4:8"]]
- 00581a10 ["CALL", null, ["callee:00c57e90:8"]]
+ 00581a50 ["INT_ADD", "register:40f0:8", ["const:581a50:8", "const:4:8"]]
+ 00581a50 ["CALL", null, ["callee:00c57e90:8"]]
- 00581a10 bytes 20581b94
+ 00581a50 bytes 10591b94
- 00581a1c ["COPY", "tmp:0:8", ["const:348:8"]]
- 00581a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581a5c ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00581a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581a1c bytes 08210d91
+ 00581a5c bytes 08211d91
- 00581a34 ["INT_ADD", "register:40f0:8", ["const:581a34:8", "const:4:8"]]
- 00581a34 ["CALL", null, ["callee:005827b8:8"]]
+ 00581a74 ["INT_ADD", "register:40f0:8", ["const:581a74:8", "const:4:8"]]
+ 00581a74 ["CALL", null, ["callee:005827b8:8"]]
- 00581a34 bytes 51030094
+ 00581a74 bytes 51030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33bf44e9a5906904b4acd03e1dd9ff0"></a>

### [`00581a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md) → [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) FUN_00581aa8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) [`0055eadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055eadc.md) · 呼出先 2件 [`00582ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582ca0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md) [`0055eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md) · 呼出先 2件 [`00582ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581ad8",
      "incomplete_value": false,
      "site": "00581ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581a98",
      "incomplete_value": false,
      "site": "00581aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00581ae4",
      "DATA",
      [
        "storage",
        "00c6c3f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581ae4",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md#insn-00581a8c) · [`00581a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md#insn-00581a98) · [`00581ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581a68.md#insn-00581ab4)
- 新版 [`00581acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581acc) · [`00581ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581ad8) · [`00581af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581af4)

~~~diff
- 00581a8c ["INT_ADD", "register:40f0:8", ["const:581a8c:8", "const:4:8"]]
- 00581a8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00581acc ["INT_ADD", "register:40f0:8", ["const:581acc:8", "const:4:8"]]
+ 00581acc ["CALL", null, ["callee:00c57e90:8"]]
- 00581a8c bytes 01581b94
+ 00581acc bytes f1581b94
- 00581a98 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00581a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581ad8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00581ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581a98 bytes 08c10f91
+ 00581ad8 bytes 08c11f91
- 00581ab4 ["INT_ADD", "register:40f0:8", ["const:581ab4:8", "const:4:8"]]
- 00581ab4 ["CALL", null, ["callee:00582ce0:8"]]
+ 00581af4 ["INT_ADD", "register:40f0:8", ["const:581af4:8", "const:4:8"]]
+ 00581af4 ["CALL", null, ["callee:00582ce0:8"]]
- 00581ab4 bytes 7b040094
+ 00581af4 bytes 7b040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f797e3d95aa85e7e6562f126b504de8c"></a>

### [`00581d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581d90.md) → [`00581dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581dd0.md) FUN_00581dd0

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
      "definition_site": "00581dd4",
      "incomplete_value": false,
      "site": "00581dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581d94",
      "incomplete_value": false,
      "site": "00581d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "00581dd8",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00581dd8",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581d90.md#insn-00581d94)
- 新版 [`00581dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581dd0.md#insn-00581dd4)

~~~diff
- 00581d94 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00581d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581dd4 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00581dd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581dd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581dd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581d94 bytes 08410491
+ 00581dd4 bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6da7577aaf777d78c9cd91e0da1cd3d"></a>

### [`00581de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581de0.md) → [`00581e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e20.md) FUN_00581e20

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
      "definition_site": "00581e24",
      "incomplete_value": false,
      "site": "00581e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581de4",
      "incomplete_value": false,
      "site": "00581de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "00581e28",
      "DATA",
      [
        "storage",
        "00c6c160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581e28",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581de0.md#insn-00581de4)
- 新版 [`00581e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e20.md#insn-00581e24)

~~~diff
- 00581de4 ["COPY", "tmp:0:8", ["const:160:8"]]
- 00581de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e24 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 00581e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581de4 bytes 08810591
+ 00581e24 bytes 08811591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffea2d2e81d7cb360cb202e17b3009b9"></a>

### [`00581df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581df0.md) → [`00581e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md) FUN_00581e30

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
      "definition_site": "00581e40",
      "incomplete_value": false,
      "site": "00581e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e00",
      "incomplete_value": false,
      "site": "00581e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "00581e48",
      "DATA",
      [
        "storage",
        "00c6c160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581e48",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581df0.md#insn-00581e00) · [`00581e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581df0.md#insn-00581e0c)
- 新版 [`00581e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md#insn-00581e40) · [`00581e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md#insn-00581e4c)

~~~diff
- 00581e00 ["COPY", "tmp:0:8", ["const:160:8"]]
- 00581e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e40 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 00581e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e00 bytes 08810591
+ 00581e40 bytes 08811591
- 00581e0c ["INT_ADD", "register:40f0:8", ["const:581e0c:8", "const:4:8"]]
- 00581e0c ["CALL", null, ["callee:00c57ea0:8"]]
+ 00581e4c ["INT_ADD", "register:40f0:8", ["const:581e4c:8", "const:4:8"]]
+ 00581e4c ["CALL", null, ["callee:00c57ea0:8"]]
- 00581e0c bytes 25571b94
+ 00581e4c bytes 15581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f247c18862a5e71a04af8b97ef2d8863"></a>

### [`00581e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581e80.md) → [`00581ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ec0.md) FUN_00581ec0

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
      "definition_site": "00581ec4",
      "incomplete_value": false,
      "site": "00581ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e84",
      "incomplete_value": false,
      "site": "00581e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00581ec8",
      "DATA",
      [
        "storage",
        "00c6c200",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581ec8",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581e80.md#insn-00581e84)
- 新版 [`00581ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ec0.md#insn-00581ec4)

~~~diff
- 00581e84 ["COPY", "tmp:0:8", ["const:200:8"]]
- 00581e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581ec4 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00581ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e84 bytes 08010891
+ 00581ec4 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-928799de9c652e33620b9cdcf5c5ebd6"></a>

### [`00581e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581e90.md) → [`00581ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md) FUN_00581ed0

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
      "definition_site": "00581ee0",
      "incomplete_value": false,
      "site": "00581ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ea0",
      "incomplete_value": false,
      "site": "00581ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00581ee8",
      "DATA",
      [
        "storage",
        "00c6c200",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581ee8",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581e90.md#insn-00581ea0) · [`00581eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581e90.md#insn-00581eac)
- 新版 [`00581ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md#insn-00581ee0) · [`00581eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md#insn-00581eec)

~~~diff
- 00581ea0 ["COPY", "tmp:0:8", ["const:200:8"]]
- 00581ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581ee0 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00581ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581ea0 bytes 08010891
+ 00581ee0 bytes 08011891
- 00581eac ["INT_ADD", "register:40f0:8", ["const:581eac:8", "const:4:8"]]
- 00581eac ["CALL", null, ["callee:00c57ea0:8"]]
+ 00581eec ["INT_ADD", "register:40f0:8", ["const:581eec:8", "const:4:8"]]
+ 00581eec ["CALL", null, ["callee:00c57ea0:8"]]
- 00581eac bytes fd561b94
+ 00581eec bytes ed571b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bcb7bb2e65dc897cda301a7b2c6f3f7"></a>

### [`00581f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f2c.md) → [`00581f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f6c.md) FUN_00581f6c

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
      "definition_site": "00581f70",
      "incomplete_value": false,
      "site": "00581f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f30",
      "incomplete_value": false,
      "site": "00581f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "00581f74",
      "DATA",
      [
        "storage",
        "00c6c290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581f74",
      "DATA",
      [
        "storage",
        "00c6c690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f2c.md#insn-00581f30)
- 新版 [`00581f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f6c.md#insn-00581f70)

~~~diff
- 00581f30 ["COPY", "tmp:0:8", ["const:290:8"]]
- 00581f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581f70 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00581f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f30 bytes 08410a91
+ 00581f70 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a7cbfc02c8be0ea44bb668d207ac23c"></a>

### [`00581f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f3c.md) → [`00581f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md) FUN_00581f7c

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
      "definition_site": "00581f8c",
      "incomplete_value": false,
      "site": "00581f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f4c",
      "incomplete_value": false,
      "site": "00581f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "00581f94",
      "DATA",
      [
        "storage",
        "00c6c290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581f94",
      "DATA",
      [
        "storage",
        "00c6c690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f3c.md#insn-00581f4c) · [`00581f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f3c.md#insn-00581f58)
- 新版 [`00581f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md#insn-00581f8c) · [`00581f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md#insn-00581f98)

~~~diff
- 00581f4c ["COPY", "tmp:0:8", ["const:290:8"]]
- 00581f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581f8c ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00581f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f4c bytes 08410a91
+ 00581f8c bytes 08411a91
- 00581f58 ["INT_ADD", "register:40f0:8", ["const:581f58:8", "const:4:8"]]
- 00581f58 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00581f98 ["INT_ADD", "register:40f0:8", ["const:581f98:8", "const:4:8"]]
+ 00581f98 ["CALL", null, ["callee:00c57ea0:8"]]
- 00581f58 bytes d2561b94
+ 00581f98 bytes c2571b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53bc764e161e6022ef73dab2821a645"></a>

### [`00581f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md) → [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) FUN_00581fbc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`00581724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581724.md) · 呼出先 5件 [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589750.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) · 呼出先 5件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.63% / 新版 81.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581ff8",
      "incomplete_value": false,
      "site": "00581ff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581fb8",
      "incomplete_value": false,
      "site": "00581fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "definition_site": "0058203c",
      "incomplete_value": true,
      "site": "00582044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00581ffc",
      "incomplete_value": true,
      "site": "00582004",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00582038",
      "incomplete_value": true,
      "site": "00582048",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f34:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ff8",
      "incomplete_value": true,
      "site": "00582008",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef4:8"
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
      "00581ff8",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582038",
      "READ",
      [
        "storage",
        "002b4ef4",
        null,
        "string"
      ]
    ],
    [
      "00582038",
      "READ",
      [
        "storage",
        "002b4f04",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00581ff8",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582038",
      "READ",
      [
        "storage",
        "002b4f34",
        null,
        "string"
      ]
    ],
    [
      "00582038",
      "READ",
      [
        "storage",
        "002b4f44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005820d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md#insn-005820d8) · [`00581f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md#insn-00581f98) · [`00581fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581f7c.md#insn-00581fc0)
- 新版 [`00582118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00582118) · [`00581fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00581fd8) · [`00582000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00582000)

~~~diff
- 005820d8 ["INT_ADD", "register:40f0:8", ["const:5820d8:8", "const:4:8"]]
- 005820d8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00582118 ["INT_ADD", "register:40f0:8", ["const:582118:8", "const:4:8"]]
+ 00582118 ["CALL", null, ["callee:00c57eb0:8"]]
- 005820d8 bytes 76561b94
+ 00582118 bytes 66571b94
- 00581f98 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00581f98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00581f98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00581f98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00581fd8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00581fd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00581fd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00581fd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00581f98 bytes 29810b91
+ 00581fd8 bytes 29811b91
- 00581fc0 ["INT_ADD", "register:40f0:8", ["const:581fc0:8", "const:4:8"]]
- 00581fc0 ["CALL", null, ["callee:00589790:8"]]
+ 00582000 ["INT_ADD", "register:40f0:8", ["const:582000:8", "const:4:8"]]
+ 00582000 ["CALL", null, ["callee:00589790:8"]]
- 00581fc0 bytes e41d0094
+ 00582000 bytes e41d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f655482bc902ad749ed34b80c30caa7a"></a>

### [`00582158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582158.md) → [`00582198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582198.md) FUN_00582198

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)

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
      "definition_site": "005821a0",
      "incomplete_value": false,
      "site": "005821a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582160",
      "incomplete_value": false,
      "site": "00582160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "005821a0",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005821a0",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058215c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582158.md#insn-0058215c)
- 新版 [`0058219c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582198.md#insn-0058219c)

~~~diff
- 0058215c ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 0058215c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058215c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058215c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058219c ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0058219c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058219c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058219c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058215c bytes 08810b91
+ 0058219c bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-792ea8b7ee75510b563a4ec98994b7de"></a>

### [`00582168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582168.md) → [`005821a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md) FUN_005821a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "005821c0",
      "incomplete_value": false,
      "site": "005821c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582180",
      "incomplete_value": false,
      "site": "00582180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "005821c0",
      "DATA",
      [
        "storage",
        "00c6c2e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005821c0",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582168.md#insn-00582178) · [`00582184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582168.md#insn-00582184)
- 新版 [`005821b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md#insn-005821b8) · [`005821c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md#insn-005821c4)

~~~diff
- 00582178 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00582178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821b8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005821b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582178 bytes 08810b91
+ 005821b8 bytes 08811b91
- 00582184 ["INT_ADD", "register:40f0:8", ["const:582184:8", "const:4:8"]]
- 00582184 ["CALL", null, ["callee:0058a8bc:8"]]
+ 005821c4 ["INT_ADD", "register:40f0:8", ["const:5821c4:8", "const:4:8"]]
+ 005821c4 ["CALL", null, ["callee:0058a8bc:8"]]
- 00582184 bytes be210094
+ 005821c4 bytes be210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e25f864398dc3fc989ca5e4d03d8a1"></a>

### [`00582198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md) → [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) FUN_005821d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589c88.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005822b4",
      "incomplete_value": false,
      "site": "005822c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582274",
      "incomplete_value": false,
      "site": "00582280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "005822c0",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005822c0",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md#insn-005821c8) · [`005821e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md#insn-005821e0) · [`005821e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582198.md#insn-005821e8)
- 新版 [`00582208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-00582208) · [`00582220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-00582220) · [`00582228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-00582228)

~~~diff
- 005821c8 ["INT_ADD", "register:40f0:8", ["const:5821c8:8", "const:4:8"]]
- 005821c8 ["CALL", null, ["callee:00588e6c:8"]]
+ 00582208 ["INT_ADD", "register:40f0:8", ["const:582208:8", "const:4:8"]]
+ 00582208 ["CALL", null, ["callee:00588e6c:8"]]
- 005821c8 bytes 191b0094
+ 00582208 bytes 191b0094
- 005821e0 ["INT_ADD", "register:40f0:8", ["const:5821e0:8", "const:4:8"]]
- 005821e0 ["CALL", null, ["callee:00589cc8:8"]]
+ 00582220 ["INT_ADD", "register:40f0:8", ["const:582220:8", "const:4:8"]]
+ 00582220 ["CALL", null, ["callee:00589cc8:8"]]
- 005821e0 bytes aa1e0094
+ 00582220 bytes aa1e0094
- 005821e8 ["INT_ADD", "register:40f0:8", ["const:5821e8:8", "const:4:8"]]
- 005821e8 ["CALL", null, ["callee:00589858:8"]]
+ 00582228 ["INT_ADD", "register:40f0:8", ["const:582228:8", "const:4:8"]]
+ 00582228 ["CALL", null, ["callee:00589858:8"]]
- 005821e8 bytes 8c1d0094
+ 00582228 bytes 8c1d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4d48087a51c8ff38a2f5cadddc9550"></a>

### [`00582320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md) → [`00582360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md) FUN_00582360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589d30.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582444",
      "incomplete_value": false,
      "site": "00582450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582404",
      "incomplete_value": false,
      "site": "00582410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "00582450",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00582450",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md#insn-00582354) · [`0058236c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md#insn-0058236c) · [`00582374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/00582320.md#insn-00582374)
- 新版 [`00582394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-00582394) · [`005823ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-005823ac) · [`005823b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-005823b4)

~~~diff
- 00582354 ["INT_ADD", "register:40f0:8", ["const:582354:8", "const:4:8"]]
- 00582354 ["CALL", null, ["callee:00588e6c:8"]]
+ 00582394 ["INT_ADD", "register:40f0:8", ["const:582394:8", "const:4:8"]]
+ 00582394 ["CALL", null, ["callee:00588e6c:8"]]
- 00582354 bytes b61a0094
+ 00582394 bytes b61a0094
- 0058236c ["INT_ADD", "register:40f0:8", ["const:58236c:8", "const:4:8"]]
- 0058236c ["CALL", null, ["callee:00589d70:8"]]
+ 005823ac ["INT_ADD", "register:40f0:8", ["const:5823ac:8", "const:4:8"]]
+ 005823ac ["CALL", null, ["callee:00589d70:8"]]
- 0058236c bytes 711e0094
+ 005823ac bytes 711e0094
- 00582374 ["INT_ADD", "register:40f0:8", ["const:582374:8", "const:4:8"]]
- 00582374 ["CALL", null, ["callee:00589858:8"]]
+ 005823b4 ["INT_ADD", "register:40f0:8", ["const:5823b4:8", "const:4:8"]]
+ 005823b4 ["CALL", null, ["callee:00589858:8"]]
- 00582374 bytes 291d0094
+ 005823b4 bytes 291d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9dead0747952e3c3eef85ffb4ccf06"></a>

### [`005824b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md) → [`005824f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md) FUN_005824f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589818.md) [`00589ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589ba8.md) [`00589d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589d30.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005825c4",
      "incomplete_value": false,
      "site": "005825d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582584",
      "incomplete_value": false,
      "site": "00582590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "005825d0",
      "DATA",
      [
        "storage",
        "00c6c110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005825d0",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005824e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md#insn-005824e8) · [`00582500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md#insn-00582500) · [`00582508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00582/005824b4.md#insn-00582508)
- 新版 [`00582528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582528) · [`00582540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582540) · [`00582548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582548)

~~~diff
- 005824e8 ["INT_ADD", "register:40f0:8", ["const:5824e8:8", "const:4:8"]]
- 005824e8 ["CALL", null, ["callee:00588e6c:8"]]
+ 00582528 ["INT_ADD", "register:40f0:8", ["const:582528:8", "const:4:8"]]
+ 00582528 ["CALL", null, ["callee:00588e6c:8"]]
- 005824e8 bytes 511a0094
+ 00582528 bytes 511a0094
- 00582500 ["INT_ADD", "register:40f0:8", ["const:582500:8", "const:4:8"]]
- 00582500 ["CALL", null, ["callee:00589d70:8"]]
+ 00582540 ["INT_ADD", "register:40f0:8", ["const:582540:8", "const:4:8"]]
+ 00582540 ["CALL", null, ["callee:00589d70:8"]]
- 00582500 bytes 0c1e0094
+ 00582540 bytes 0c1e0094
- 00582508 ["INT_ADD", "register:40f0:8", ["const:582508:8", "const:4:8"]]
- 00582508 ["CALL", null, ["callee:00589858:8"]]
+ 00582548 ["INT_ADD", "register:40f0:8", ["const:582548:8", "const:4:8"]]
+ 00582548 ["CALL", null, ["callee:00589858:8"]]
- 00582508 bytes c41c0094
+ 00582548 bytes c41c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

