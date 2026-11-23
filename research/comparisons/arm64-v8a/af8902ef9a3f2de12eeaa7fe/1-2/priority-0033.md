# v15.7.4 → v16.0.0 · 最優先の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-dd12c3d562133875b47f942193d37179"></a>

### [`0071e020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e020.md) → [`007481cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007481cc.md) FUN_007481cc

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`005859d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md) [`006f308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f308c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`0071d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d0f4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.30% / 新版 95.30%

CFGの説明率　旧版 93.75% / 新版 95.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e048"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0071e034",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071e048",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "007482bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f308c"
      ]
    ]
  ],
  "added": [
    [
      "007481e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007481f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "007482bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d0f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e020.md#insn-0071e034) · [`0071e048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e020.md#insn-0071e048) · [`0071e110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e020.md#insn-0071e110)
- 新版 [`007482bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007481cc.md#insn-007482bc)

~~~diff
- 0071e034 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0071e034 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0071e034 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0071e034 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071e034 bytes f44f06a9
- 0071e048 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0071e048 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0071e048 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0071e048 bytes a8831ff8
- 0071e110 ["INT_ADD", "register:40f0:8", ["const:71e110:8", "const:4:8"]]
- 0071e110 ["CALL", null, ["ram:6f308c:8"]]
+ 007482bc ["INT_ADD", "register:40f0:8", ["const:7482bc:8", "const:4:8"]]
+ 007482bc ["CALL", null, ["ram:71d0f4:8"]]
- 0071e110 bytes df53ff97
+ 007482bc bytes 8e53ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58dc402e42bb4d7a2cf03e03eeb814cb"></a>

### [`0071e2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2a4.md) → [`00748450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748450.md) FUN_00748450

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0074845c",
      "incomplete_value": false,
      "site": "00748468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e2b0",
      "incomplete_value": false,
      "site": "0071e2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "00748468",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748468",
      "DATA",
      [
        "storage",
        "00c77ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2a4.md#insn-0071e2ac) · [`0071e2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2a4.md#insn-0071e2b0)
- 新版 [`00748458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748450.md#insn-00748458) · [`0074845c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748450.md#insn-0074845c)

~~~diff
- 0071e2ac ["COPY", "register:4050:8", ["const:bfa000:8"]]
+ 00748458 ["COPY", "register:4050:8", ["const:c77000:8"]]
- 0071e2ac bytes ea260090
+ 00748458 bytes 6a2900f0
- 0071e2b0 ["COPY", "tmp:0:8", ["const:998:8"]]
- 0071e2b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0074845c ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0074845c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0074845c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0074845c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e2b0 bytes 4a612691
+ 0074845c bytes 4a012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a0a44f99770f5c1105431833a2e0cfa"></a>

### [`0071e2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2e8.md) → [`00748494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748494.md) FUN_00748494

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "007484ac",
      "incomplete_value": false,
      "site": "007484b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e300",
      "incomplete_value": false,
      "site": "0071e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "007484b8",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007484b8",
      "DATA",
      [
        "storage",
        "00c77ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2e8.md#insn-0071e2fc) · [`0071e300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2e8.md#insn-0071e300) · [`0071e330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e2e8.md#insn-0071e330)
- 新版 [`007484a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748494.md#insn-007484a8) · [`007484ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748494.md#insn-007484ac) · [`007484dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748494.md#insn-007484dc)

~~~diff
- 0071e2fc ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007484a8 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071e2fc bytes e8260090
+ 007484a8 bytes 682900f0
- 0071e300 ["COPY", "tmp:0:8", ["const:998:8"]]
- 0071e300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007484ac ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 007484ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007484ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007484ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e300 bytes 08612691
+ 007484ac bytes 08012b91
- 0071e330 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071e330 ["INT_ADD", "register:40f0:8", ["const:71e330:8", "const:4:8"]]
- 0071e330 ["CALLIND", null, ["register:0:8"]]
+ 007484dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007484dc ["INT_ADD", "register:40f0:8", ["const:7484dc:8", "const:4:8"]]
+ 007484dc ["CALLIND", null, ["register:0:8"]]
- 0071e330 bytes 00013fd6
+ 007484dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ae3178526d27543fd92116223c61bcc"></a>

### [`0071e344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e344.md) → [`007484f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007484f0.md) FUN_007484f0

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00748518",
      "incomplete_value": false,
      "site": "0074851c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e36c",
      "incomplete_value": false,
      "site": "0071e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "0074851c",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074851c",
      "DATA",
      [
        "storage",
        "00c77ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e344.md#insn-0071e358) · [`0071e368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e344.md#insn-0071e368) · [`0071e36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e344.md#insn-0071e36c)
- 新版 [`00748504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007484f0.md#insn-00748504) · [`00748514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007484f0.md#insn-00748514) · [`00748518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007484f0.md#insn-00748518)

~~~diff
- 0071e358 ["INT_ADD", "register:40f0:8", ["const:71e358:8", "const:4:8"]]
- 0071e358 ["CALL", null, ["callee:00c57a90:8"]]
+ 00748504 ["INT_ADD", "register:40f0:8", ["const:748504:8", "const:4:8"]]
+ 00748504 ["CALL", null, ["callee:00c57a90:8"]]
- 0071e358 bytes 3af31294
+ 00748504 bytes 633d1494
- 0071e368 ["COPY", "register:4048:8", ["const:bfa000:8"]]
+ 00748514 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 0071e368 bytes e9260090
+ 00748514 bytes 692900f0
- 0071e36c ["COPY", "tmp:0:8", ["const:998:8"]]
- 0071e36c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0071e36c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0071e36c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748518 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 00748518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0071e36c bytes 29612691
+ 00748518 bytes 29012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9614165a5ad41b8f3599cb600e0dcdd"></a>

### [`0071e3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e3d4.md) → [`00748580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748580.md) FUN_00748580

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0074859c",
      "incomplete_value": false,
      "site": "007485a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e3f0",
      "incomplete_value": false,
      "site": "0071e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "007485a0",
      "DATA",
      [
        "storage",
        "00bfa998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007485a0",
      "DATA",
      [
        "storage",
        "00c77ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e3d4.md#insn-0071e3ec) · [`0071e3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e3d4.md#insn-0071e3f0) · [`0071e418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e3d4.md#insn-0071e418)
- 新版 [`00748598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748580.md#insn-00748598) · [`0074859c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748580.md#insn-0074859c) · [`007485c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748580.md#insn-007485c4)

~~~diff
- 0071e3ec ["COPY", "register:4050:8", ["const:bfa000:8"]]
+ 00748598 ["COPY", "register:4050:8", ["const:c77000:8"]]
- 0071e3ec bytes ea260090
+ 00748598 bytes 6a2900f0
- 0071e3f0 ["COPY", "tmp:0:8", ["const:998:8"]]
- 0071e3f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0074859c ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0074859c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0074859c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0074859c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e3f0 bytes 4a612691
+ 0074859c bytes 4a012b91
- 0071e418 ["COPY", "register:0:8", ["register:4048:8"]]
- 0071e418 ["INT_ADD", "register:40f0:8", ["const:71e418:8", "const:4:8"]]
- 0071e418 ["CALLIND", null, ["register:0:8"]]
+ 007485c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007485c4 ["INT_ADD", "register:40f0:8", ["const:7485c4:8", "const:4:8"]]
+ 007485c4 ["CALLIND", null, ["register:0:8"]]
- 0071e418 bytes 20013fd6
+ 007485c4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-215e2aab7df2ba365c06eeafbf24e0bd"></a>

### [`0071e5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5a8.md) → [`00748754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748754.md) FUN_00748754

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00748758",
      "incomplete_value": false,
      "site": "0074875c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e5ac",
      "incomplete_value": false,
      "site": "0071e5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "0074875c",
      "DATA",
      [
        "storage",
        "00bfaa18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074875c",
      "DATA",
      [
        "storage",
        "00c77b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5a8.md#insn-0071e5a8) · [`0071e5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5a8.md#insn-0071e5ac)
- 新版 [`00748754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748754.md#insn-00748754) · [`00748758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748754.md#insn-00748758)

~~~diff
- 0071e5a8 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00748754 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071e5a8 bytes e8260090
+ 00748754 bytes 682900f0
- 0071e5ac ["COPY", "tmp:0:8", ["const:a18:8"]]
- 0071e5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748758 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00748758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e5ac bytes 08612891
+ 00748758 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58d80d8651e0a5c3716b83583f00484"></a>

### [`0071e5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5f0.md) → [`0074879c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074879c.md) FUN_0074879c

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "007487b0",
      "incomplete_value": false,
      "site": "007487b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e604",
      "incomplete_value": false,
      "site": "0071e608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "007487b4",
      "DATA",
      [
        "storage",
        "00bfaa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007487b4",
      "DATA",
      [
        "storage",
        "00c77bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5f0.md#insn-0071e5fc) · [`0071e600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5f0.md#insn-0071e600) · [`0071e604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e5f0.md#insn-0071e604)
- 新版 [`007487a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074879c.md#insn-007487a8) · [`007487ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074879c.md#insn-007487ac) · [`007487b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074879c.md#insn-007487b0)

~~~diff
- 0071e5fc ["INT_ADD", "register:40f0:8", ["const:71e5fc:8", "const:4:8"]]
- 0071e5fc ["CALL", null, ["callee:00c57a90:8"]]
+ 007487a8 ["INT_ADD", "register:40f0:8", ["const:7487a8:8", "const:4:8"]]
+ 007487a8 ["CALL", null, ["callee:00c57a90:8"]]
- 0071e5fc bytes 91f21294
+ 007487a8 bytes ba3c1494
- 0071e600 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007487ac ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071e600 bytes e8260090
+ 007487ac bytes 682900f0
- 0071e604 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0071e604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007487b0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 007487b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007487b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007487b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e604 bytes 08612a91
+ 007487b0 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-828d4eda4d3c391f41ef2b4c82bd22a2"></a>

### [`0071e614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e614.md) → [`007487c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007487c0.md) FUN_007487c0

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007487c4",
      "incomplete_value": false,
      "site": "007487c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e618",
      "incomplete_value": false,
      "site": "0071e61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "007487c8",
      "DATA",
      [
        "storage",
        "00bfaa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007487c8",
      "DATA",
      [
        "storage",
        "00c77bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e614.md#insn-0071e614) · [`0071e618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e614.md#insn-0071e618)
- 新版 [`007487c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007487c0.md#insn-007487c0) · [`007487c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/007487c0.md#insn-007487c4)

~~~diff
- 0071e614 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007487c0 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071e614 bytes e8260090
+ 007487c0 bytes 682900f0
- 0071e618 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0071e618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007487c4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 007487c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007487c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007487c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e618 bytes 08612a91
+ 007487c4 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1c44385a1db636a5a6bd3c26eeda613"></a>

### [`0071e6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6b0.md) → [`0074885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/0074885c.md) FUN_0074885c

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`005859d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md) [`006f308c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f308c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`0071d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d0f4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 69.05% / 新版 78.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e6b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0071e6b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071e6b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071e6bc",
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
      "00748860",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00748864",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00748868",
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

- 旧版 [`0071e6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6b0.md#insn-0071e6b4) · [`0071e6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6b0.md#insn-0071e6b8) · [`0071e6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e6b0.md#insn-0071e6bc)

~~~diff
- 0071e6b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0071e6b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0071e6b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0071e6b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071e6b4 bytes fd7b02a9
- 0071e6b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 0071e6b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 0071e6b8 bytes fb1b00f9
- 0071e6bc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0071e6bc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0071e6bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0071e6bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071e6bc bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3465a04cb321b06ac7b4562f2c41b96"></a>

### [`0071e8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e8dc.md) → [`00748a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748a88.md) FUN_00748a88

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071e8f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00748aa0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00748a90",
      "incomplete_value": false,
      "site": "00748a94",
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
      "unmatched:0071e8f4",
      "DATA",
      [
        "storage",
        "00bfab98",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0071e8f8",
      "DATA",
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
      "00748aa0",
      "DATA",
      [
        "storage",
        "00c77cc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00748aa4",
      "DATA",
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

- 旧版 [`0071e8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e8dc.md#insn-0071e8e8) · [`0071e8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e8dc.md#insn-0071e8f4) · [`0071e8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e8dc.md#insn-0071e8fc)
- 新版 [`00748a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748a88.md#insn-00748a94)

~~~diff
- 0071e8e8 ["INT_ADD", "register:40f0:8", ["const:71e8e8:8", "const:4:8"]]
- 0071e8e8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00748a94 ["INT_ADD", "register:40f0:8", ["const:748a94:8", "const:4:8"]]
+ 00748a94 ["CALL", null, ["callee:00c57a90:8"]]
- 0071e8e8 bytes d6f11294
+ 00748a94 bytes ff3b1494
- 0071e8f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0071e8f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0071e8f4 bytes 080000f9
- 0071e8fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 0071e8fc ["RETURN", null, ["register:0:8"]]
- 0071e8fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a62058ba975b4496100a6c8308514a3"></a>

### [`0071e900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e900.md) → [`00748aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748aac.md) FUN_00748aac

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00748ab0",
      "incomplete_value": false,
      "site": "00748ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071e904",
      "incomplete_value": false,
      "site": "0071e908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "00748ab4",
      "DATA",
      [
        "storage",
        "00bfab98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00748ab4",
      "DATA",
      [
        "storage",
        "00c77cc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e900.md#insn-0071e900) · [`0071e904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e900.md#insn-0071e904)
- 新版 [`00748aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748aac.md#insn-00748aac) · [`00748ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748aac.md#insn-00748ab0)

~~~diff
- 0071e900 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00748aac ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071e900 bytes e8260090
+ 00748aac bytes 682900f0
- 0071e904 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0071e904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071e904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071e904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748ab0 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00748ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071e904 bytes 08612e91
+ 00748ab0 bytes 08013391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb552bbd07c9aa203caf8a7fc673951"></a>

### [`0071e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md) → [`00748af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md) FUN_00748af0

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 7件 [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) [`0071eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071eb38.md) [`0071ed70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed70.md) [`00720468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720468.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 7件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) [`00748ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md) [`00748f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f1c.md) [`0074a614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a614.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 56.52% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0071e964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md#insn-0071e964) · [`0071e96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md#insn-0071e96c) · [`0071e97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071e944.md#insn-0071e97c)
- 新版 [`00748b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b10) · [`00748b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b18) · [`00748b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748af0.md#insn-00748b28)

~~~diff
- 0071e964 ["INT_ADD", "register:40f0:8", ["const:71e964:8", "const:4:8"]]
- 0071e964 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00748b10 ["INT_ADD", "register:40f0:8", ["const:748b10:8", "const:4:8"]]
+ 00748b10 ["CALL", null, ["callee:00c57ab0:8"]]
- 0071e964 bytes bff11294
+ 00748b10 bytes e83b1494
- 0071e96c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0071e96c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00748b18 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00748b18 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0071e96c bytes 540200b4
+ 00748b18 bytes 540200b4
- 0071e97c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 00748b28 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0071e97c bytes 80010054
+ 00748b28 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94d03fd26bd87cdc2b06192338ca1664"></a>

### [`0071ea9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ea9c.md) → [`00748c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md) FUN_00748c48

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009749a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/009749a4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009aa488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa488.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 72.22% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0071eb00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00748cac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0071eb00"
      ],
      [
        "FALL_THROUGH",
        "00748cac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00748cac",
      "incomplete_value": true,
      "site": "00748cb0",
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
      "definition_site": "0071eb00",
      "incomplete_value": true,
      "site": "0071eb04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "unmatched:0071eb00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00748cb8"
      ]
    ]
  ],
  "added": [
    [
      "00748cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00748cb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ea9c.md#insn-0071eb00) · [`0071eae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ea9c.md#insn-0071eae8)
- 新版 [`00748cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md#insn-00748cac) · [`00748c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748c48.md#insn-00748c94)

~~~diff
- 0071eb00 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0071eb00 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0071eb00 bytes 600000b4
+ 00748cac ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00748cac ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00748cac bytes 600000b4
- 0071eae8 ["INT_ADD", "register:40f0:8", ["const:71eae8:8", "const:4:8"]]
- 0071eae8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00748c94 ["INT_ADD", "register:40f0:8", ["const:748c94:8", "const:4:8"]]
+ 00748c94 ["CALL", null, ["callee:00c57ab0:8"]]
- 0071eae8 bytes 5ef11294
+ 00748c94 bytes 873b1494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc45711816c2c8798505a1395a0340d9"></a>

### [`0071ed5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed5c.md) → [`00748f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md) FUN_00748f08

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071d070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071d/0071d070.md) [`0071eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071eb38.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0074721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00747/0074721c.md) [`00748ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748ce4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00748f18",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0071ed6c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00748f14",
      "incomplete_value": false,
      "site": "00748f18",
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
    "old": {
      "definition_site": "0071ed68",
      "incomplete_value": false,
      "site": "0071ed6c",
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
            "const:39d:8"
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
      "00748f14",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00748f18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00748f14",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00748f18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071ed6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed5c.md#insn-0071ed6c) · [`0071ed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed5c.md#insn-0071ed64) · [`0071ed68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071ed5c.md#insn-0071ed68)
- 新版 [`00748f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md#insn-00748f18) · [`00748f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md#insn-00748f10) · [`00748f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f08.md#insn-00748f14)

~~~diff
- 0071ed6c ["INT_ADD", "register:40f0:8", ["const:71ed6c:8", "const:4:8"]]
- 0071ed6c ["CALL", null, ["ram:418c38:8"]]
+ 00748f18 ["INT_ADD", "register:40f0:8", ["const:748f18:8", "const:4:8"]]
+ 00748f18 ["CALL", null, ["ram:43b738:8"]]
- 0071ed6c bytes b3e7f397
+ 00748f18 bytes 08caf397
- 0071ed64 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00748f10 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0071ed64 bytes 40dcffb0
+ 00748f10 bytes 60dbfff0
- 0071ed68 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0071ed68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00748f14 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00748f14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00748f14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00748f14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0071ed68 bytes 00740e91
+ 00748f14 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b16e9a79e9ca7021cdd86890ceb92ea9"></a>

### [`0071edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md) → [`00748f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f78.md) FUN_00748f78

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0071edcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md) [`0096ff84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096f/0096ff84.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`00748f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00748/00748f78.md) [`007aca8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) [`009a5a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a5/009a5a68.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.89% / 新版 82.89%

CFGの説明率　旧版 32.04% / 新版 43.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071ede0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071ede0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071ede4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0071ede0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071ede4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071edfc",
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
      "00748f8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00748f90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00748fa8",
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

- 旧版 [`0071ede0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md#insn-0071ede0) · [`0071ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md#insn-0071ede4) · [`0071edfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071e/0071edcc.md#insn-0071edfc)

~~~diff
- 0071ede0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0071ede0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0071ede0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 0071ede0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071ede0 bytes f6570ca9
- 0071ede4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0071ede4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0071ede4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 0071ede4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071ede4 bytes f44f0da9
- 0071edfc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0071edfc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0071edfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0071edfc bytes a9831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f633fd2eb3c1843867f14691648a95"></a>

### [`0071f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5b8.md) → [`00749764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749764.md) FUN_00749764

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00749770",
      "incomplete_value": false,
      "site": "0074977c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f5c4",
      "incomplete_value": false,
      "site": "0071f5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "0074977c",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074977c",
      "DATA",
      [
        "storage",
        "00c77d40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5b8.md#insn-0071f5c0) · [`0071f5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5b8.md#insn-0071f5c4)
- 新版 [`0074976c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749764.md#insn-0074976c) · [`00749770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749764.md#insn-00749770)

~~~diff
- 0071f5c0 ["COPY", "register:4050:8", ["const:bfa000:8"]]
+ 0074976c ["COPY", "register:4050:8", ["const:c77000:8"]]
- 0071f5c0 bytes ca2600f0
+ 0074976c bytes 6a2900d0
- 0071f5c4 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0071f5c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00749770 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00749770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00749770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00749770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071f5c4 bytes 4a613091
+ 00749770 bytes 4a013591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf72b3afd13990ac664e91b8a8471b5"></a>

### [`0071f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5fc.md) → [`007497a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/007497a8.md) FUN_007497a8

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "007497c0",
      "incomplete_value": false,
      "site": "007497cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f614",
      "incomplete_value": false,
      "site": "0071f620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "007497cc",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007497cc",
      "DATA",
      [
        "storage",
        "00c77d40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5fc.md#insn-0071f610) · [`0071f614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5fc.md#insn-0071f614) · [`0071f644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f5fc.md#insn-0071f644)
- 新版 [`007497bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/007497a8.md#insn-007497bc) · [`007497c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/007497a8.md#insn-007497c0) · [`007497f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/007497a8.md#insn-007497f0)

~~~diff
- 0071f610 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007497bc ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071f610 bytes c82600f0
+ 007497bc bytes 682900d0
- 0071f614 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 0071f614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0071f614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0071f614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007497c0 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 007497c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007497c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007497c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0071f614 bytes 08613091
+ 007497c0 bytes 08013591
- 0071f644 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071f644 ["INT_ADD", "register:40f0:8", ["const:71f644:8", "const:4:8"]]
- 0071f644 ["CALLIND", null, ["register:0:8"]]
+ 007497f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007497f0 ["INT_ADD", "register:40f0:8", ["const:7497f0:8", "const:4:8"]]
+ 007497f0 ["CALLIND", null, ["register:0:8"]]
- 0071f644 bytes 00013fd6
+ 007497f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25003d38975fdf90b398dbac6b3ed91e"></a>

### [`0071f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f6e8.md) → [`00749894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749894.md) FUN_00749894

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007498b4",
      "incomplete_value": false,
      "site": "007498b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f708",
      "incomplete_value": false,
      "site": "0071f708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0071f748"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "007498f4"
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
      "007498b4",
      "DATA",
      [
        "storage",
        "00bfac18",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0071f748",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "007498b4",
      "DATA",
      [
        "storage",
        "00c77d40",
        null,
        "undefined *"
      ]
    ],
    [
      "007498f4",
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

- 旧版 [`0071f748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f6e8.md#insn-0071f748) · [`0071f700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f6e8.md#insn-0071f700)
- 新版 [`007498f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749894.md#insn-007498f4) · [`007498ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749894.md#insn-007498ac)

~~~diff
- 0071f748 ["COPY", "register:0:8", ["register:4040:8"]]
- 0071f748 ["INT_ADD", "register:40f0:8", ["const:71f748:8", "const:4:8"]]
- 0071f748 ["CALLIND", null, ["register:0:8"]]
- 0071f748 bytes 00013fd6
+ 007498f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007498f4 ["INT_ADD", "register:40f0:8", ["const:7498f4:8", "const:4:8"]]
+ 007498f4 ["CALLIND", null, ["register:0:8"]]
+ 007498f4 bytes 00013fd6
- 0071f700 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007498ac ["COPY", "register:4040:8", ["const:c77000:8"]]
- 0071f700 bytes c82600f0
+ 007498ac bytes 682900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-648754ec94e4e77f548bc8245a543db3"></a>

### [`0071f7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f7e8.md) → [`00749994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00749/00749994.md) FUN_00749994

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0058558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058558c.md) [`005857bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005857bc.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.61% / 新版 65.61%

CFGの説明率　旧版 54.84% / 新版 51.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 53件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071f7f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071f7f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0071f7fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0071f7f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071f7fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0071f810",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007499a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "007499a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007499bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071f7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f7e8.md#insn-0071f7f8) · [`0071f7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f7e8.md#insn-0071f7fc) · [`0071f810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071f/0071f7e8.md#insn-0071f810)

~~~diff
- 0071f7f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0071f7f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0071f7f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0071f7f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071f7f8 bytes f65704a9
- 0071f7fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0071f7fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0071f7fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0071f7fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0071f7fc bytes f44f05a9
- 0071f810 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0071f810 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0071f810 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0071f810 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-037519f1bc356ac087a048cd946a4cdc"></a>

### [`007201bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007201bc.md) → [`0074a368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a368.md) FUN_0074a368

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0074a374",
      "incomplete_value": false,
      "site": "0074a380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007201c8",
      "incomplete_value": false,
      "site": "007201d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "0074a380",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074a380",
      "DATA",
      [
        "storage",
        "00c77dc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007201c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007201bc.md#insn-007201c4) · [`007201c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007201bc.md#insn-007201c8)
- 新版 [`0074a370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a368.md#insn-0074a370) · [`0074a374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a368.md#insn-0074a374)

~~~diff
- 007201c4 ["COPY", "register:4050:8", ["const:bfa000:8"]]
+ 0074a370 ["COPY", "register:4050:8", ["const:c77000:8"]]
- 007201c4 bytes ca2600d0
+ 0074a370 bytes 6a2900b0
- 007201c8 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 007201c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007201c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007201c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0074a374 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 0074a374 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0074a374 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0074a374 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007201c8 bytes 4a613291
+ 0074a374 bytes 4a013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c2976590bd8b2322240e149981aa44a"></a>

### [`0072025c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072025c.md) → [`0074a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a408.md) FUN_0074a408

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0074a434"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0072028c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00720288",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0072028c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0074a454"
      ]
    ],
    [
      "unmatched:00720298",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0074a45c"
      ]
    ]
  ],
  "added": [
    [
      "0074a434",
      "DATA",
      [
        "storage",
        "00c77dc0",
        null,
        "undefined *"
      ]
    ],
    [
      "0074a438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0074a454"
      ]
    ],
    [
      "0074a444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0074a45c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00720270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072025c.md#insn-00720270) · [`00720288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072025c.md#insn-00720288) · [`0072028c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/0072025c.md#insn-0072028c)
- 新版 [`0074a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a408.md#insn-0074a41c)

~~~diff
- 00720270 ["INT_ADD", "register:40f0:8", ["const:720270:8", "const:4:8"]]
- 00720270 ["CALL", null, ["callee:00c57a90:8"]]
+ 0074a41c ["INT_ADD", "register:40f0:8", ["const:74a41c:8", "const:4:8"]]
+ 0074a41c ["CALL", null, ["callee:00c57a90:8"]]
- 00720270 bytes 74eb1294
+ 0074a41c bytes 9d351494
- 00720288 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00720288 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00720288 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00720288 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00720288 bytes 280401f8
- 0072028c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0072028c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0072028c bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7cf037917311f327de1ce39d8be0120"></a>

### [`007202e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007202e4.md) → [`0074a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a490.md) FUN_0074a490

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 33.33% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007202e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007202e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007202e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007202e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:007202e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00720300",
      "DATA",
      [
        "storage",
        "00bfac98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0074a490",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0074a494",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0074a4ac",
      "DATA",
      [
        "storage",
        "00c77dc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007202e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007202e4.md#insn-007202e4) · [`007202e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007202e4.md#insn-007202e8) · [`00720300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/007202e4.md#insn-00720300)

~~~diff
- 007202e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007202e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007202e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 007202e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 007202e4 bytes fd7bbea9
- 007202e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 007202e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 007202e8 bytes f30b00f9
- 00720300 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00720300 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00720300 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00720300 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00720300 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a11d804d26ab31e2f8ba2adadb64ba4"></a>

### [`00720714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720714.md) → [`0074a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a8c0.md) _INIT_130

採用 · 移動量 `+0x2a1ac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072076c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00720744",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00720750",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0072076c",
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
      "0074a8f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0074a8fc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0074a918",
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

- 旧版 [`00720744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720714.md#insn-00720744) · [`0072076c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720714.md#insn-0072076c) · [`00720790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720714.md#insn-00720790)

~~~diff
- 00720744 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00720744 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00720744 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00720744 bytes a9831ff8
- 0072076c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 0072076c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072076c bytes e013813c
- 00720790 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00720790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00720790 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a21da564b8eea5ca93ef148362e7bc"></a>

### [`00720bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720bac.md) → [`0074ad58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074ad58.md) FUN_0074ad58

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.23% / 新版 92.23%

CFGの説明率　旧版 72.13% / 新版 62.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00720bb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00720bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00720bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00720bb4",
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
      "0074ad58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0074ad5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0074ad60",
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

- 旧版 [`00720bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720bac.md#insn-00720bac) · [`00720bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720bac.md#insn-00720bb0) · [`00720bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00720/00720bac.md#insn-00720bb4)

~~~diff
- 00720bac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00720bac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00720bac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00720bac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00720bac bytes fd7bbda9
- 00720bb0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00720bb0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00720bb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00720bb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00720bb0 bytes f65701a9
- 00720bb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00720bb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00720bb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00720bb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00720bb4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2388fb40eff6a9afce5edad5b9da28"></a>

### [`007216cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/007216cc.md) → [`0074b878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074b878.md) FUN_0074b878

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md)
- 新版 呼出元 1件 [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 10.00% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0072173c",
      "incomplete_value": true,
      "site": "00721744",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0072176c",
      "incomplete_value": true,
      "site": "00721778",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 4,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [],
  "added": [
    [
      "0074b9b8",
      "DATA",
      [
        "storage",
        "00432894",
        null,
        "byte[31]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00721744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/007216cc.md#insn-00721744) · [`00721778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/007216cc.md#insn-00721778) · [`00721704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/007216cc.md#insn-00721704)
- 新版 [`0074b8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074b878.md#insn-0074b8f0) · [`0074b924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074b878.md#insn-0074b924) · [`0074b8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074b878.md#insn-0074b8b0)

~~~diff
- 00721744 ["INT_ADD", "register:40f0:8", ["const:721744:8", "const:4:8"]]
- 00721744 ["CALL", null, ["callee:00489f0c:8"]]
+ 0074b8f0 ["INT_ADD", "register:40f0:8", ["const:74b8f0:8", "const:4:8"]]
+ 0074b8f0 ["CALL", null, ["callee:00489f0c:8"]]
- 00721744 bytes 4c16f597
+ 0074b8f0 bytes 87f9f497
- 00721778 ["INT_ADD", "register:40f0:8", ["const:721778:8", "const:4:8"]]
- 00721778 ["CALL", null, ["callee:00489f0c:8"]]
+ 0074b924 ["INT_ADD", "register:40f0:8", ["const:74b924:8", "const:4:8"]]
+ 0074b924 ["CALL", null, ["callee:00489f0c:8"]]
- 00721778 bytes 3f16f597
+ 0074b924 bytes 7af9f497
- 00721704 ["INT_ADD", "register:40f0:8", ["const:721704:8", "const:4:8"]]
- 00721704 ["CALL", null, ["callee:008514b8:8"]]
+ 0074b8b0 ["INT_ADD", "register:40f0:8", ["const:74b8b0:8", "const:4:8"]]
+ 0074b8b0 ["CALL", null, ["callee:008514b8:8"]]
- 00721704 bytes 9ff70394
+ 0074b8b0 bytes 02170494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1242ad5ffa32fbe3b7594e167b745f"></a>

### [`00721960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721960.md) → [`0074bb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074bb0c.md) FUN_0074bb0c

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0062bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bf80.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00651a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651a64.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 26.15% / 新版 20.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00721960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00721960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00721964"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00721960",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00721964",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00721968",
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
      "0074bb0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0074bb10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0074bb14",
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

- 旧版 [`00721960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721960.md#insn-00721960) · [`00721964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721960.md#insn-00721964) · [`00721968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721960.md#insn-00721968)

~~~diff
- 00721960 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00721960 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00721960 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00721960 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00721960 bytes fd7bbda9
- 00721964 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00721964 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00721964 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00721964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00721964 bytes f65701a9
- 00721968 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00721968 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00721968 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00721968 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00721968 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b44e574d03c71adfefd788ed0ca4e76d"></a>

### [`00721cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721cc4.md) → [`0074be70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074be70.md) FUN_0074be70

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`006fed08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fed08.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00728e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 8.33% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00721d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0074bf28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00721d28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0074bebc",
      "DATA",
      [
        "storage",
        "00340384",
        "fde_00340384",
        "dword"
      ]
    ],
    [
      "0074becc",
      "DATA",
      [
        "storage",
        "00340374",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:00721d28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fed08"
      ]
    ]
  ],
  "added": [
    [
      "0074bebc",
      "DATA",
      [
        "storage",
        "0034445c",
        "fde_0034445c",
        "dword"
      ]
    ],
    [
      "0074becc",
      "DATA",
      [
        "storage",
        "0034444c",
        null,
        "dword"
      ]
    ],
    [
      "0074bed4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728e08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00721d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721cc4.md#insn-00721d28) · [`00721d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721cc4.md#insn-00721d7c) · [`00721ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721cc4.md#insn-00721ebc)
- 新版 [`0074c068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074b/0074be70.md#insn-0074c068)

~~~diff
- 00721d28 ["INT_ADD", "register:40f0:8", ["const:721d28:8", "const:4:8"]]
- 00721d28 ["CALL", null, ["ram:6fed08:8"]]
- 00721d28 bytes f873ff97
- 00721d7c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00721d7c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00721d7c bytes 43020054
- 00721ebc ["INT_ADD", "register:40f0:8", ["const:721ebc:8", "const:4:8"]]
- 00721ebc ["CALL", null, ["callee:00468f48:8"]]
+ 0074c068 ["INT_ADD", "register:40f0:8", ["const:74c068:8", "const:4:8"]]
+ 0074c068 ["CALL", null, ["callee:00468f48:8"]]
- 00721ebc bytes 7d90f497
+ 0074c068 bytes b873f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5853610aa5f948102422a01006de773c"></a>

### [`00721f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721f5c.md) → [`0074c108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c108.md) FUN_0074c108

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 3件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 3件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 80.41% / 新版 80.41%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00721f84"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0074c2a4",
      "incomplete_value": true,
      "site": "0074c2c0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0074c2f0",
      "incomplete_value": true,
      "site": "0074c30c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00722144",
      "incomplete_value": true,
      "site": "00722160",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00721f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467820"
      ]
    ],
    [
      "unmatched:00721f88",
      "DATA",
      [
        "storage",
        "0032d678",
        "fde_0032d678",
        "dword"
      ]
    ],
    [
      "unmatched:00721f8c",
      "DATA",
      [
        "storage",
        "0032d684",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "0074c130",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467820"
      ]
    ],
    [
      "0074c134",
      "DATA",
      [
        "storage",
        "003316a0",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0074c138",
      "DATA",
      [
        "storage",
        "003316ac",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00721f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721f5c.md#insn-00721f84) · [`00722114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721f5c.md#insn-00722114) · [`00722160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00721/00721f5c.md#insn-00722160)
- 新版 [`0074c2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c108.md#insn-0074c2c0) · [`0074c30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c108.md#insn-0074c30c)

~~~diff
- 00721f84 ["INT_ADD", "register:40f0:8", ["const:721f84:8", "const:4:8"]]
- 00721f84 ["CALL", null, ["callee:00467820:8"]]
- 00721f84 bytes 818af497
- 00722114 ["INT_ADD", "register:40f0:8", ["const:722114:8", "const:4:8"]]
- 00722114 ["CALL", null, ["callee:00469bc4:8"]]
+ 0074c2c0 ["INT_ADD", "register:40f0:8", ["const:74c2c0:8", "const:4:8"]]
+ 0074c2c0 ["CALL", null, ["callee:00469bc4:8"]]
- 00722114 bytes 0693f497
+ 0074c2c0 bytes 4176f497
- 00722160 ["INT_ADD", "register:40f0:8", ["const:722160:8", "const:4:8"]]
- 00722160 ["CALL", null, ["callee:00469bc4:8"]]
+ 0074c30c ["INT_ADD", "register:40f0:8", ["const:74c30c:8", "const:4:8"]]
+ 0074c30c ["CALL", null, ["callee:00469bc4:8"]]
- 00722160 bytes f392f497
+ 0074c30c bytes 2e76f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afff39a6a042d69eeb26543793961590"></a>

### [`00722264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00722/00722264.md) → [`0074c410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c410.md) FUN_0074c410

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`00a34cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a34/00a34cc8.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00a92b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a92/00a92b50.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.99% / 新版 82.99%

CFGの説明率　旧版 56.00% / 新版 65.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00722264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00722264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00722268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00722264",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00722268",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072226c",
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
      "0074c410",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0074c414",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0074c418",
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

- 旧版 [`00722264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00722/00722264.md#insn-00722264) · [`00722268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00722/00722264.md#insn-00722268) · [`0072226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00722/00722264.md#insn-0072226c)

~~~diff
- 00722264 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00722264 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00722264 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00722264 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00722264 bytes fd7bbca9
- 00722268 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00722268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00722268 bytes f70b00f9
- 0072226c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0072226c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0072226c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0072226c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0072226c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92dfa9989074b179cf53dabebd408726"></a>

### [`00723a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723a20.md) → [`0074dbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074d/0074dbcc.md) FUN_0074dbcc

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) · 呼出先 9件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md)
- 新版 呼出元 1件 [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) · 呼出先 9件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.45% / 新版 80.45%

CFGの説明率　旧版 41.03% / 新版 41.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00723a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00723a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00723a60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00723a38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00723a50",
      "READ",
      [
        "storage",
        "0029f95a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00723a60",
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
      "0074dbe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0074dbfc",
      "READ",
      [
        "storage",
        "002afd78",
        null,
        "string"
      ]
    ],
    [
      "0074dc0c",
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

- 旧版 [`00723a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723a20.md#insn-00723a38) · [`00723a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723a20.md#insn-00723a60) · [`00723a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723a20.md#insn-00723a64)

~~~diff
- 00723a38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00723a38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00723a38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00723a38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00723a38 bytes f44f07a9
- 00723a60 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00723a60 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00723a60 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00723a60 bytes a8831ff8
- 00723a64 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00723a64 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00723a64 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00723a64 bytes ea030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ac2450c4ac3d3fdf8dd04a00da54ef"></a>

### [`00723dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723dc4.md) → [`0074df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074d/0074df70.md) FUN_0074df70

採用 · 移動量 `+0x2a1ac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e68f8.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.67% / 新版 94.67%

CFGの説明率　旧版 46.67% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0074dfc8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00723e1c",
      "value": [
        "leaf",
        "ram:449aec:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0074e070",
      "incomplete_value": true,
      "site": "0074e080",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0074e074",
      "incomplete_value": true,
      "site": "0074e080",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "0074dfc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ]
  ],
  "added": [
    [
      "0074dfc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00723e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723dc4.md#insn-00723e1c) · [`00723ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723dc4.md#insn-00723ed4) · [`00723f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00723/00723dc4.md#insn-00723f5c)
- 新版 [`0074dfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074d/0074df70.md#insn-0074dfc8) · [`0074e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074d/0074df70.md#insn-0074e080) · [`0074e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074d/0074df70.md#insn-0074e108)

~~~diff
- 00723e1c ["INT_ADD", "register:40f0:8", ["const:723e1c:8", "const:4:8"]]
- 00723e1c ["CALL", null, ["ram:449aec:8"]]
+ 0074dfc8 ["INT_ADD", "register:40f0:8", ["const:74dfc8:8", "const:4:8"]]
+ 0074dfc8 ["CALL", null, ["ram:46c984:8"]]
- 00723e1c bytes 3497f497
+ 0074dfc8 bytes 6f7af497
- 00723ed4 ["INT_ADD", "register:40f0:8", ["const:723ed4:8", "const:4:8"]]
- 00723ed4 ["CALL", null, ["callee:00468f48:8"]]
+ 0074e080 ["INT_ADD", "register:40f0:8", ["const:74e080:8", "const:4:8"]]
+ 0074e080 ["CALL", null, ["callee:00468f48:8"]]
- 00723ed4 bytes 7788f497
+ 0074e080 bytes b26bf497
- 00723f5c ["INT_ADD", "register:40f0:8", ["const:723f5c:8", "const:4:8"]]
- 00723f5c ["CALL", null, ["callee:00468f48:8"]]
+ 0074e108 ["INT_ADD", "register:40f0:8", ["const:74e108:8", "const:4:8"]]
+ 0074e108 ["CALL", null, ["callee:00468f48:8"]]
- 00723f5c bytes 5588f497
+ 0074e108 bytes 906bf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea999ce593bb6ef6daf6e81424a54f7"></a>

### [`00724198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724198.md) → [`0074e344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074e/0074e344.md) FUN_0074e344

採用 · 移動量 `+0x2a1ac` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008fdba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fd/008fdba8.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fe0.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`00932474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932474.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 86.15% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007241fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00724200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00724204"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007241f8",
      "READ",
      [
        "storage",
        "00299164",
        null,
        "string"
      ]
    ],
    [
      "unmatched:007241fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00724200",
      "WRITE",
      [
        "storage",
        "Stack[-0xe3]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0074e3a4",
      "READ",
      [
        "storage",
        "002a8f3d",
        null,
        "string"
      ]
    ],
    [
      "0074e3a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "0074e3ac",
      "WRITE",
      [
        "storage",
        "Stack[-0xe3]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007241fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724198.md#insn-007241fc) · [`00724200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724198.md#insn-00724200) · [`00724204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00724/00724198.md#insn-00724204)

~~~diff
- 007241fc ["COPY", "tmp:0:8", ["const:0:8"]]
- 007241fc ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 007241fc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 007241fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:8"]]
- 007241fc bytes bf031bf8
- 00724200 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00724200 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00724200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:5d:8"]]
- 00724200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00724200 bytes ff770139
- 00724204 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00724204 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:51:8"]]
- 00724204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00724204 bytes e81305f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f60e1cd0ed4b1d52e555540a2beb2e"></a>

### [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) → [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) FUN_00752240

採用 · 移動量 `+0x2a1b0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 17件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`0071b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b838.md) [`0071bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071bdc8.md) [`0071c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c4c8.md) [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) · 呼出先 0件 
- 新版 呼出元 17件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md) [`00745f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/00745f74.md) [`00746674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746674.md) [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-1f89217a7566352f1c0cb9deff850586"></a>

### [`007280a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007280a8.md) → [`00752258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752258.md) FUN_00752258

採用 · 移動量 `+0x2a1b0` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`00589fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/00589fe4.md) [`005b5878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b5878.md)
- 新版 呼出元 1件 [`009bf53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`005ae5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5a8.md) [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.08% / 新版 86.08%

CFGの説明率　旧版 68.18% / 新版 73.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007522cc",
      "incomplete_value": true,
      "site": "007522dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ae5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072811c",
      "incomplete_value": true,
      "site": "0072812c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:94c:8"
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
      "definition_site": "007522e0",
      "incomplete_value": true,
      "site": "007522e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00728130",
      "incomplete_value": true,
      "site": "00728130",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007522f8",
      "value": [
        "leaf",
        "ram:71ecc0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00728148",
      "value": [
        "leaf",
        "ram:6f4c58:8"
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
      "007522a0",
      "DATA",
      [
        "storage",
        "00392484",
        null,
        "byte[39]"
      ]
    ],
    [
      "007522cc",
      "READ",
      [
        "storage",
        "0029c94c",
        null,
        "string"
      ]
    ],
    [
      "007522d0",
      "READ",
      [
        "storage",
        "0029c959",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007522a0",
      "DATA",
      [
        "storage",
        "003965a4",
        "fde_003965a4",
        "dword"
      ]
    ],
    [
      "007522cc",
      "READ",
      [
        "storage",
        "002acae5",
        null,
        "string"
      ]
    ],
    [
      "007522d0",
      "READ",
      [
        "storage",
        "002acaf2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00728148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007280a8.md#insn-00728148) · [`0072825c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007280a8.md#insn-0072825c) · [`00728274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007280a8.md#insn-00728274)
- 新版 [`007522f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752258.md#insn-007522f8)

~~~diff
- 00728148 ["INT_ADD", "register:40f0:8", ["const:728148:8", "const:4:8"]]
- 00728148 ["CALL", null, ["ram:6f4c58:8"]]
+ 007522f8 ["INT_ADD", "register:40f0:8", ["const:7522f8:8", "const:4:8"]]
+ 007522f8 ["CALL", null, ["ram:71ecc0:8"]]
- 00728148 bytes c432ff97
+ 007522f8 bytes 7232ff97
- 0072825c ["INT_ADD", "register:40f0:8", ["const:72825c:8", "const:4:8"]]
- 0072825c ["CALL", null, ["callee:0043dd98:8"]]
- 0072825c bytes 0fccf397
- 00728274 ["INT_ADD", "register:40f0:8", ["const:728274:8", "const:4:8"]]
- 00728274 ["CALL", null, ["ram:6f4c58:8"]]
- 00728274 bytes 7932ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eb145787f92c6eb1df2ce9696a1843f"></a>

### [`00729130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729130.md) → [`007532e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532e8.md) FUN_007532e8

採用 · 移動量 `+0x2a1b8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "007532fc",
      "incomplete_value": false,
      "site": "00753300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00729144",
      "incomplete_value": false,
      "site": "00729148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "00753300",
      "DATA",
      [
        "storage",
        "00bfad18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00753300",
      "DATA",
      [
        "storage",
        "00c77e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072913c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729130.md#insn-0072913c) · [`00729140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729130.md#insn-00729140) · [`00729144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729130.md#insn-00729144)
- 新版 [`007532f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532e8.md#insn-007532f4) · [`007532f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532e8.md#insn-007532f8) · [`007532fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007532e8.md#insn-007532fc)

~~~diff
- 0072913c ["INT_ADD", "register:40f0:8", ["const:72913c:8", "const:4:8"]]
- 0072913c ["CALL", null, ["callee:00c57a90:8"]]
+ 007532f4 ["INT_ADD", "register:40f0:8", ["const:7532f4:8", "const:4:8"]]
+ 007532f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0072913c bytes c1c71294
+ 007532f4 bytes e7111494
- 00729140 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 007532f8 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 00729140 bytes 882600b0
+ 007532f8 bytes 28290090
- 00729144 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00729144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00729144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00729144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007532fc ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 007532fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007532fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007532fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00729144 bytes 08613491
+ 007532fc bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9cd1ed9929370915e518fffad474662"></a>

### [`00729154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729154.md) → [`0075330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/0075330c.md) FUN_0075330c

採用 · 移動量 `+0x2a1b8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00753310",
      "incomplete_value": false,
      "site": "00753314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00729158",
      "incomplete_value": false,
      "site": "0072915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "00753314",
      "DATA",
      [
        "storage",
        "00bfad18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00753314",
      "DATA",
      [
        "storage",
        "00c77e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00729154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729154.md#insn-00729154) · [`00729158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/00729154.md#insn-00729158)
- 新版 [`0075330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/0075330c.md#insn-0075330c) · [`00753310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/0075330c.md#insn-00753310)

~~~diff
- 00729154 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 0075330c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 00729154 bytes 882600b0
+ 0075330c bytes 28290090
- 00729158 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00729158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00729158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00729158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00753310 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00753310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00753310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00753310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00729158 bytes 08613491
+ 00753310 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dab1b9b7ae0bc18535c3a71ada8ad8b1"></a>

### [`0072916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072916c.md) → [`00753324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753324.md) FUN_00753324

採用 · 移動量 `+0x2a1b8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad88.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc20.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 84.21% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007533ac",
      "incomplete_value": true,
      "site": "007533c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007291f4",
      "incomplete_value": true,
      "site": "00729208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d6:8"
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
      "definition_site": "007533c4",
      "incomplete_value": true,
      "site": "007533c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0072920c",
      "incomplete_value": true,
      "site": "0072920c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00729194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00729194",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00753390"
      ]
    ],
    [
      "0075335c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "0075339c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "0075334c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00753390"
      ]
    ],
    [
      "0075335c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0075339c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00729194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072916c.md#insn-00729194) · [`007291a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072916c.md#insn-007291a4) · [`007291e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072916c.md#insn-007291e4)
- 新版 [`0075335c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753324.md#insn-0075335c) · [`0075339c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753324.md#insn-0075339c)

~~~diff
- 00729194 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00729194 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00729194 bytes 21020054
- 007291a4 ["INT_ADD", "register:40f0:8", ["const:7291a4:8", "const:4:8"]]
- 007291a4 ["CALL", null, ["ram:457e1c:8"]]
+ 0075335c ["INT_ADD", "register:40f0:8", ["const:75335c:8", "const:4:8"]]
+ 0075335c ["CALL", null, ["ram:47acb4:8"]]
- 007291a4 bytes 1ebbf497
+ 0075335c bytes 569ef497
- 007291e4 ["INT_ADD", "register:40f0:8", ["const:7291e4:8", "const:4:8"]]
- 007291e4 ["CALL", null, ["ram:469e20:8"]]
+ 0075339c ["INT_ADD", "register:40f0:8", ["const:75339c:8", "const:4:8"]]
+ 0075339c ["CALL", null, ["ram:48ccb8:8"]]
- 007291e4 bytes 0f03f597
+ 0075339c bytes 47e6f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d981d66942b60cb298a77d78d62b7b62"></a>

### [`007292d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md) → [`00753490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md) FUN_00753490

採用 · 移動量 `+0x2a1b8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`007259f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00725/007259f0.md) [`00726b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00726/00726b58.md) [`00750e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) [`007bd244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd244.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 7件 [`0074fba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074f/0074fba0.md) [`00750d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00750/00750d08.md) [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007ef3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef3b0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007534a0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007292e8",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075349c",
      "incomplete_value": false,
      "site": "007534a0",
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
    "old": {
      "definition_site": "007292e4",
      "incomplete_value": false,
      "site": "007292e8",
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
            "const:39d:8"
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
      "0075349c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "007534a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0075349c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "007534a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007292e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md#insn-007292e8) · [`007292e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md#insn-007292e0) · [`007292e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292d8.md#insn-007292e4)
- 新版 [`007534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md#insn-007534a0) · [`00753498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md#insn-00753498) · [`0075349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753490.md#insn-0075349c)

~~~diff
- 007292e8 ["INT_ADD", "register:40f0:8", ["const:7292e8:8", "const:4:8"]]
- 007292e8 ["CALL", null, ["ram:418c38:8"]]
+ 007534a0 ["INT_ADD", "register:40f0:8", ["const:7534a0:8", "const:4:8"]]
+ 007534a0 ["CALL", null, ["ram:43b738:8"]]
- 007292e8 bytes 54bef397
+ 007534a0 bytes a6a0f397
- 007292e0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00753498 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 007292e0 bytes e0dbffd0
+ 00753498 bytes 20dbff90
- 007292e4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 007292e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007292e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007292e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0075349c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0075349c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0075349c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0075349c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007292e4 bytes 00740e91
+ 0075349c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af1094bca0867f76ad407f555b9b598"></a>

### [`007292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292ec.md) → [`007534a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/007534a4.md) _INIT_131

採用 · 移動量 `+0x2a1b8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.14% / 新版 75.14%

CFGの説明率　旧版 54.29% / 新版 61.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072931c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00729344"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00729350"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0072931c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00729328",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00729344",
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
      "007534d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "007534e0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007534fc",
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

- 旧版 [`0072931c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292ec.md#insn-0072931c) · [`00729344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292ec.md#insn-00729344) · [`00729350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/007292ec.md#insn-00729350)

~~~diff
- 0072931c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0072931c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0072931c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0072931c bytes a9831ff8
- 00729344 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00729344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00729344 bytes e013813c
- 00729350 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00729350 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 00729350 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00729350 bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146a0c5de022410015a6a98a63e723fd"></a>

### [`0072a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md) → [`007548d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00754/007548d0.md) FUN_007548d0

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0072967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072967c.md) · 呼出先 16件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`00753834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753834.md) · 呼出先 16件 [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.05% / 新版 47.05%

CFGの説明率　旧版 11.85% / 新版 12.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `unresolved_branch_alignment` 41件, `unresolved_call_alignment` 49件, `unresolved_store_alignment` 122件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072a730"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072a744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072a750"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0072a730",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072a734",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0067e15c"
      ]
    ],
    [
      "unmatched:0072a744",
      "DATA",
      [
        "storage",
        "00bfadc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00754904",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00754908",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0067e15c"
      ]
    ],
    [
      "00754918",
      "DATA",
      [
        "storage",
        "00c77ef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072a730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md#insn-0072a730) · [`0072a744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md#insn-0072a744) · [`0072a750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md#insn-0072a750)

~~~diff
- 0072a730 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0072a730 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0072a730 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0072a730 bytes a8831ff8
- 0072a744 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0072a744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0072a744 bytes 680200f9
- 0072a750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
- 0072a750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072a750 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0072a750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0072a750 bytes 600217ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f61a779d3ddb30eebcdc9be04870fffc"></a>

### [`0072b854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b854.md) → [`00755a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755a28.md) FUN_00755a28

採用 · 移動量 `+0x2a1d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0072b94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b94c.md) · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00755b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755b20.md) · 呼出先 3件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.68% / 新版 59.68%

CFGの説明率　旧版 3.85% / 新版 5.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072b870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072b90c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00755a44"
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
      "unmatched:0072b870",
      "DATA",
      [
        "storage",
        "00bfadc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0072b874",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00755a74"
      ]
    ],
    [
      "unmatched:0072b880",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ],
  "added": [
    [
      "00755a44",
      "DATA",
      [
        "storage",
        "00c77ef0",
        null,
        "pointer"
      ]
    ],
    [
      "00755a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00755a74"
      ]
    ],
    [
      "00755a54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072b870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b854.md#insn-0072b870) · [`0072b874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b854.md#insn-0072b874) · [`0072b880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b854.md#insn-0072b880)

~~~diff
- 0072b870 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0072b870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0072b870 bytes 080000f9
- 0072b874 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0072b874 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0072b874 bytes 740100b4
- 0072b880 ["INT_ADD", "register:40f0:8", ["const:72b880:8", "const:4:8"]]
- 0072b880 ["CALL", null, ["callee:00c538e0:8"]]
- 0072b880 bytes 84ad1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfebdc5a3457f15cab4d72a32e4e96ad"></a>

### [`0072b970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b970.md) → [`00755b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755b44.md) _INIT_132

採用 · 移動量 `+0x2a1d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.19% / 新版 71.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072b9a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072b9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072b9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0072b9a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072b9ac",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0072b9b4",
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
      "00755b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00755b80",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00755b88",
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

- 旧版 [`0072b9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b970.md#insn-0072b9a0) · [`0072b9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b970.md#insn-0072b9b4) · [`0072b9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072b970.md#insn-0072b9b8)

~~~diff
- 0072b9a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0072b9a0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0072b9a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0072b9a0 bytes a9831ff8
- 0072b9b4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0072b9b4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0072b9b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0072b9b4 bytes ea130278
- 0072b9b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0072b9b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0072b9b8 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f389991912797d283e2e5edf1f2f72c"></a>

### [`0072bd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072bd00.md) → [`00755ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00755/00755ed4.md) _INIT_133

採用 · 移動量 `+0x2a1d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.45% / 新版 60.45%

CFGの説明率　旧版 77.42% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 35件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072bd30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072bd58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072bd7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0072bd30",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072bd3c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0072bd58",
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
      "00755f04",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00755f10",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00755f2c",
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

- 旧版 [`0072bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072bd00.md#insn-0072bd30) · [`0072bd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072bd00.md#insn-0072bd58) · [`0072bd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072b/0072bd00.md#insn-0072bd7c)

~~~diff
- 0072bd30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0072bd30 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0072bd30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0072bd30 bytes a9831ff8
- 0072bd58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 0072bd58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072bd58 bytes e013813c
- 0072bd7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 0072bd7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072bd7c bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f6e47f9f99ce82ab56c3c0ba5ed6cf"></a>

### [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) → [`00756264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00756/00756264.md) FUN_00756264

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0080735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080735c.md) [`008a4544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4544.md) [`008cb758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb758.md) [`008cd6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cd/008cd6e0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 10件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00838cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc8.md) [`008d83dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d83dc.md) [`008ff628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff628.md) [`009015b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/009015b0.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 30.92% / 新版 30.92%

CFGの説明率　旧版 6.83% / 新版 6.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 35件, `store_value` 3件, `unresolved_branch_alignment` 137件, `unresolved_call_alignment` 141件, `unresolved_store_alignment` 320件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072c0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072c0c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072c0d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0072c0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x118]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072c0c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:0072c0c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00758190"
      ]
    ]
  ],
  "added": [
    [
      "00756290",
      "WRITE",
      [
        "storage",
        "Stack[-0x118]",
        null,
        null
      ]
    ],
    [
      "00756298",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0075629c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00758190"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072c0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md#insn-0072c0bc) · [`0072c0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md#insn-0072c0c4) · [`0072c0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md#insn-0072c0d8)

~~~diff
- 0072c0bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0072c0bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0072c0bc bytes e80700f9
- 0072c0c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0072c0c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0072c0c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0072c0c4 bytes a8831ef8
- 0072c0d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0072c0d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0072c0d8 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e272bcdba139545eac954ccffc599d75"></a>

### [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) → [`00758190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758190.md) FUN_00758190

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`0072c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072c/0072c090.md) [`007802c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) [`008acbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md) [`008c6e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6e18.md) · 呼出先 10件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 7件 [`00756264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00756/00756264.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`008bc884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc884.md) [`008e0a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md) [`008facec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008facec.md) · 呼出先 10件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.54% / 新版 67.54%

CFGの説明率　旧版 80.00% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072dff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072dffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00758204",
      "incomplete_value": true,
      "site": "00758204",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072e030",
      "incomplete_value": true,
      "site": "0072e030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:d9c:8"
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
      "unmatched:0072dff0",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0072e000",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "007581f4",
      "READ",
      [
        "storage",
        "00291d9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007581c4",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "007581d4",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "007581f4",
      "READ",
      [
        "storage",
        "002a13b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072dff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md#insn-0072dff0) · [`0072dffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md#insn-0072dffc) · [`0072e068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md#insn-0072e068)
- 新版 [`0075823c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758190.md#insn-0075823c)

~~~diff
- 0072dff0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0072dff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0072dff0 bytes 680200f9
- 0072dffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
- 0072dffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072dffc bytes 60ba803d
- 0072e068 ["INT_ADD", "register:40f0:8", ["const:72e068:8", "const:4:8"]]
- 0072e068 ["CALL", null, ["callee:0047e5cc:8"]]
+ 0075823c ["INT_ADD", "register:40f0:8", ["const:75823c:8", "const:4:8"]]
+ 0075823c ["CALL", null, ["callee:0047e5cc:8"]]
- 0072e068 bytes b3b5f497
+ 0075823c bytes e498f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-791be5fc98c590542b640bf272ec12d0"></a>

### [`0072e2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md) → [`007584b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md) FUN_007584b8

採用 · 移動量 `+0x2a1d4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0075171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 60.47% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0072e308"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0072e3f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "007584dc"
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
      "unmatched:0072e308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007584f8"
      ]
    ],
    [
      "unmatched:0072e3f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007585e8"
      ]
    ],
    [
      "unmatched:0072e378",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "007584dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007584f8"
      ]
    ],
    [
      "007585cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007585e8"
      ]
    ],
    [
      "0075854c",
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

- 旧版 [`0072e308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md#insn-0072e308) · [`0072e378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md#insn-0072e378) · [`0072e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md#insn-0072e3f4)
- 新版 [`007585c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md#insn-007585c8)

~~~diff
- 0072e308 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0072e308 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0072e308 bytes e00000b5
- 0072e378 ["COPY", "register:0:8", ["register:4040:8"]]
- 0072e378 ["INT_ADD", "register:40f0:8", ["const:72e378:8", "const:4:8"]]
- 0072e378 ["CALLIND", null, ["register:0:8"]]
- 0072e378 bytes 00013fd6
- 0072e3f4 ["INT_ADD", "register:40f0:8", ["const:72e3f4:8", "const:4:8"]]
- 0072e3f4 ["CALL", null, ["callee:00c538e0:8"]]
+ 007585c8 ["INT_ADD", "register:40f0:8", ["const:7585c8:8", "const:4:8"]]
+ 007585c8 ["CALL", null, ["callee:00c538e0:8"]]
- 0072e3f4 bytes a7a21294
+ 007585c8 bytes c6ec1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-850c6e08c9410002e617d018b9eba98c"></a>

### [`0072e62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md) → [`00758800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758800.md) FUN_00758800

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`00654084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) [`00988788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00988/00988788.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md)
- 新版 呼出元 7件 [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md) [`0092472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) [`009be268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md) · 呼出先 21件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.34% / 新版 72.34%

CFGの説明率　旧版 28.49% / 新版 29.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072e758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072e75c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0072e75c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00758840",
      "DATA",
      [
        "storage",
        "00303030",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00758848",
      "DATA",
      [
        "storage",
        "00303030",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:0072e678",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072e494"
      ]
    ]
  ],
  "added": [
    [
      "00758840",
      "DATA",
      [
        "storage",
        "00303030",
        null,
        "string"
      ]
    ],
    [
      "00758848",
      "DATA",
      [
        "storage",
        "00303030",
        null,
        "string"
      ]
    ],
    [
      "0075884c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00758668"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0072e758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md#insn-0072e758) · [`0072e75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md#insn-0072e75c) · [`0072e760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md#insn-0072e760)

~~~diff
- 0072e758 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:28:8"]]
- 0072e758 ["STORE", null, ["const:1b1:8", "register:4040:8", "register:5000:16"]]
- 0072e758 bytes 008d823c
- 0072e75c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
- 0072e75c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072e75c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0072e75c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0072e75c bytes 000107ad
- 0072e760 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 0072e760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0072e760 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0072e760 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0072e760 bytes 000108ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b593d185b9d882515652ebcde21093eb"></a>

### [`007316bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007316bc.md) → [`0075b890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b890.md) FUN_0075b890

採用 · 移動量 `+0x2a1d4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 20.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007316bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007316bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007316c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007316bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:007316c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007316f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0075b8d8"
      ]
    ]
  ],
  "added": [
    [
      "0075b890",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0075b894",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0075b8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0075b8d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007316bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007316bc.md#insn-007316bc) · [`007316c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007316bc.md#insn-007316c0) · [`007316f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007316bc.md#insn-007316f0)

~~~diff
- 007316bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007316bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007316bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 007316bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 007316bc bytes fd7bbea9
- 007316c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 007316c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 007316c0 bytes f30b00f9
- 007316f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 007316f0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 007316f0 bytes a00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-735988878d264c759ddca9a266708f95"></a>

### [`00733374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md) → [`0075d548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md) FUN_0075d548

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 12件 [`0063e7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e7a8.md) [`0063e844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e844.md) [`0063e8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e8b4.md) [`0063eaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063eaf8.md) [`0063ed20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063ed20.md)
- 新版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 12件 [`00664a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664a80.md) [`00664b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b1c.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00664ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664ff8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 59.83% / 新版 59.83%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `call_target` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0075d58c",
      "incomplete_value": true,
      "site": "0075d590",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:378:8"
              ]
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
      "definition_site": "007333b8",
      "incomplete_value": true,
      "site": "007333bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:372:8"
              ]
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00733408"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007334f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0075d5a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e7a8"
      ]
    ],
    [
      "unmatched:007333e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e7a8"
      ]
    ],
    [
      "unmatched:00733400",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e844"
      ]
    ]
  ],
  "added": [
    [
      "0075d5a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664a80"
      ]
    ],
    [
      "0075d5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664a80"
      ]
    ],
    [
      "0075d5d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664b1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007333bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md#insn-007333bc) · [`007333d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md#insn-007333d0) · [`007333e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733374.md#insn-007333e0)
- 新版 [`0075d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md#insn-0075d590) · [`0075d5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md#insn-0075d5a4)

~~~diff
- 007333bc ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
+ 0075d590 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 007333bc bytes 40090054
+ 0075d590 bytes 40090054
- 007333d0 ["INT_ADD", "register:40f0:8", ["const:7333d0:8", "const:4:8"]]
- 007333d0 ["CALL", null, ["ram:63e7a8:8"]]
+ 0075d5a4 ["INT_ADD", "register:40f0:8", ["const:75d5a4:8", "const:4:8"]]
+ 0075d5a4 ["CALL", null, ["ram:664a80:8"]]
- 007333d0 bytes f62cfc97
+ 0075d5a4 bytes 371dfc97
- 007333e0 ["INT_ADD", "register:40f0:8", ["const:7333e0:8", "const:4:8"]]
- 007333e0 ["CALL", null, ["ram:63e7a8:8"]]
- 007333e0 bytes f22cfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-486262f3d8199713f33388985e034e4b"></a>

### [`00734374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md) → [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) FUN_0075e548

採用 · 移動量 `+0x2a1d4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 14件 [`0042bbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bbc8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md)
- 新版 呼出元 2件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 14件 [`0044ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ea60.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.83% / 新版 74.83%

CFGの説明率　旧版 25.00% / 新版 26.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007343c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007343c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007343cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007343bc",
      "READ",
      [
        "storage",
        "002a38e1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:007343bc",
      "READ",
      [
        "storage",
        "002a38f1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:007343c0",
      "READ",
      [
        "storage",
        "002b13d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0075e590",
      "READ",
      [
        "storage",
        "002b3fbb",
        null,
        "string"
      ]
    ],
    [
      "0075e590",
      "READ",
      [
        "storage",
        "002b3fcb",
        null,
        "string"
      ]
    ],
    [
      "0075e594",
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007343c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md#insn-007343c4) · [`007343c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md#insn-007343c8) · [`007343cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md#insn-007343cc)

~~~diff
- 007343c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 007343c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
- 007343c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 007343c4 bytes a0031df8
- 007343c8 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 007343c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 007343c8 bytes a2039c3c
- 007343cc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:80:8"]]
- 007343cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 007343cc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 007343cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 007343cc bytes 000404ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9daa41faea7cbc66d6de086af41a8a"></a>

### [`0073addc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md) → [`007650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md) FUN_007650e8

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) · 呼出先 21件 [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md)
- 新版 呼出元 2件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) · 呼出先 21件 [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.14% / 新版 81.14%

CFGの説明率　旧版 43.42% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ae34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ae38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073aef4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073ae20",
      "READ",
      [
        "storage",
        "0029f98d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0073ae34",
      "WRITE",
      [
        "storage",
        "Stack[-0x250]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073ae38",
      "WRITE",
      [
        "storage",
        "Stack[-0x17f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0076512c",
      "READ",
      [
        "storage",
        "002afdab",
        null,
        "string"
      ]
    ],
    [
      "00765140",
      "WRITE",
      [
        "storage",
        "Stack[-0x250]",
        null,
        null
      ]
    ],
    [
      "00765144",
      "WRITE",
      [
        "storage",
        "Stack[-0x17f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073ae34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md#insn-0073ae34) · [`0073ae38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md#insn-0073ae38) · [`0073ae54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md#insn-0073ae54)

~~~diff
- 0073ae34 ["COPY", "tmp:0:8", ["register:8:8"]]
- 0073ae34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0073ae34 bytes e003803d
- 0073ae38 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:1:8"]]
- 0073ae38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0073ae38 bytes 8013803c
- 0073ae54 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 0073ae54 bytes 40150054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbeb189ecd56abbd419b01f2e8711def"></a>

### [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md) → [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md) FUN_007656e8

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) · 呼出先 22件 [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md) [`0053d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d580.md)
- 新版 呼出元 1件 [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) · 呼出先 22件 [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.10% / 新版 86.10%

CFGの説明率　旧版 79.44% / 新版 75.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073b3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073b3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073b3e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073b3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073b3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073b3e4",
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
      "007656e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "007656ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "007656f0",
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

- 旧版 [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md#insn-0073b3dc) · [`0073b3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md#insn-0073b3e0) · [`0073b3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md#insn-0073b3e4)

~~~diff
- 0073b3dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0073b3dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0073b3dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 0073b3dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0073b3dc bytes fd7bbaa9
- 0073b3e0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0073b3e0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0073b3e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0073b3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073b3e0 bytes fc6f01a9
- 0073b3e4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0073b3e4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0073b3e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0073b3e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073b3e4 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b66ee006a592329d16c8c87d8bb97d4"></a>

### [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) → [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) FUN_00765ddc

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md) [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md) [`005742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md) [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md)
- 新版 呼出元 3件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 51.27% / 新版 51.27%

CFGの説明率　旧版 20.31% / 新版 19.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 41件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bb00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bb2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073bb00",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073bb20",
      "READ",
      [
        "storage",
        "0029f98d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0073bb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00765e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00765e2c",
      "READ",
      [
        "storage",
        "002afdab",
        null,
        "string"
      ]
    ],
    [
      "00765e34",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md#insn-0073bb00) · [`0073bb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md#insn-0073bb28) · [`0073bb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md#insn-0073bb2c)

~~~diff
- 0073bb00 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0073bb00 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0073bb00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0073bb00 bytes a8831ff8
- 0073bb28 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0073bb28 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 0073bb28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0073bb28 bytes e8830039
- 0073bb2c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0073bb2c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:31:8"]]
- 0073bb2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0073bb2c bytes ea130378
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6209814465152fe8fe21b1d60607323f"></a>

### [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) → [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) FUN_0076621c

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md)
- 新版 呼出元 1件 [`00769220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) · 呼出先 27件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.12% / 新版 63.12%

CFGの説明率　旧版 25.59% / 新版 25.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bf30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bf50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073bfbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073bf30",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073bf50",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073bf90",
      "DATA",
      [
        "storage",
        "003c34a4",
        null,
        "byte[39]"
      ]
    ]
  ],
  "added": [
    [
      "0076623c",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ],
    [
      "0076625c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0076629c",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "byte[15]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md#insn-0073bf30) · [`0073bf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md#insn-0073bf50) · [`0073bfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md#insn-0073bfbc)

~~~diff
- 0073bf30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:78:8"]]
- 0073bf30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 0073bf30 bytes e53f00f9
- 0073bf50 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0073bf50 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0073bf50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0073bf50 bytes a8831ef8
- 0073bfbc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0073bfbc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:100:8"]]
- 0073bfbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0073bfbc bytes e8030439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16265a1613dded2edd03cda00644849"></a>

### [`0073cac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cac4.md) → [`00766dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766dd0.md) FUN_00766dd0

採用 · 移動量 `+0x2a30c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0073f98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f98c.md) · 呼出先 8件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md) [`0052de54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052de54.md) [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 3件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00769c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769c98.md) · 呼出先 8件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) [`00550cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cec.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 59.26% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073cac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073cac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073cacc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073cac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073cacc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073cae0",
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
      "00766dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00766dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00766dec",
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

- 旧版 [`0073cac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cac4.md#insn-0073cac8) · [`0073cacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cac4.md#insn-0073cacc) · [`0073cae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cac4.md#insn-0073cae0)

~~~diff
- 0073cac8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0073cac8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0073cac8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0073cac8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073cac8 bytes fd7b06a9
- 0073cacc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0073cacc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0073cacc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0073cacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073cacc bytes f44f07a9
- 0073cae0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0073cae0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0073cae0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0073cae0 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b63b0a694547a0c04fddffd5fccccb"></a>

### [`0073ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md) → [`00766fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/00766fdc.md) FUN_00766fdc

採用 · 移動量 `+0x2a30c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005971dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.12% / 新版 69.12%

CFGの説明率　旧版 62.50% / 新版 52.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ccd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ccd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ccd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073ccd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073ccd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073ccd8",
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
      "00766fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00766fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00766fe4",
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

- 旧版 [`0073ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md#insn-0073ccd0) · [`0073ccd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md#insn-0073ccd4) · [`0073ccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md#insn-0073ccd8)

~~~diff
- 0073ccd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0073ccd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0073ccd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0073ccd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0073ccd0 bytes fd7bbba9
- 0073ccd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0073ccd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0073ccd4 bytes f90b00f9
- 0073ccd8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0073ccd8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0073ccd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0073ccd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073ccd8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52beb8740864f472f03c56724fe7f046"></a>

### [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) → [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) FUN_00767108

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00670f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md) · 呼出先 28件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md)
- 新版 呼出元 1件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) · 呼出先 28件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.45% / 新版 66.45%

CFGの説明率　旧版 11.05% / 新版 10.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件, `unresolved_branch_alignment` 23件, `unresolved_call_alignment` 16件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 50件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ce3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073cea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073ceac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073ce3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073ce7c",
      "DATA",
      [
        "storage",
        "003c34a4",
        null,
        "byte[39]"
      ]
    ],
    [
      "unmatched:0073ce84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073a8e0"
      ]
    ]
  ],
  "added": [
    [
      "00767148",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00767188",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "byte[15]"
      ]
    ],
    [
      "00767190",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764bec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073ce3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md#insn-0073ce3c) · [`0073cea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md#insn-0073cea4) · [`0073ceac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md#insn-0073ceac)

~~~diff
- 0073ce3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0073ce3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 0073ce3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0073ce3c bytes a8031ff8
- 0073cea4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0073cea4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:c8:8"]]
- 0073cea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0073cea4 bytes e8230339
- 0073ceac ["COPY", "tmp:0:4", ["const:0:4"]]
- 0073ceac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0073ceac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d1:8"]]
- 0073ceac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0073ceac bytes ff470339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f9bda655597ecefb7fe8b89be4c2ce"></a>

### [`0073de68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md) → [`00768174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md) FUN_00768174

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00851b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851b9c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00845f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f8c.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`00884b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 9件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00878278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 17.39% / 新版 16.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073deec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073def0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073def4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007681b0",
      "DATA",
      [
        "storage",
        "003c33d8",
        null,
        "dword"
      ]
    ],
    [
      "007681b4",
      "DATA",
      [
        "storage",
        "003c33e0",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:0073dedc",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007681b0",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "uleb128"
      ]
    ],
    [
      "007681b4",
      "DATA",
      [
        "storage",
        "003c76c0",
        null,
        "byte[11]"
      ]
    ],
    [
      "007681e8",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073deb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md#insn-0073deb0) · [`0073deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md#insn-0073deec) · [`0073def0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md#insn-0073def0)
- 新版 [`007681bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md#insn-007681bc)

~~~diff
- 0073deb0 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 007681bc ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 0073deb0 bytes 80080054
+ 007681bc bytes 80080054
- 0073deec ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0073deec ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 0073deec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0073deec bytes e8830039
- 0073def0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0073def0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0073def0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0073def0 bytes ea1302f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8321bcf82255e53b7a173f4ad25645"></a>

### [`0073e0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md) → [`007683d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md) FUN_007683d4

採用 · 移動量 `+0x2a30c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00adccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccc4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`009cc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc994.md) · 呼出先 8件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00b3c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c69c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.00% / 新版 68.00%

CFGの説明率　旧版 37.50% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073e0cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073e0cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073e0d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0073e0cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073e0d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0073e0d4",
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
      "007683d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "007683dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "007683e0",
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

- 旧版 [`0073e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md#insn-0073e0cc) · [`0073e0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md#insn-0073e0d0) · [`0073e0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md#insn-0073e0d4)

~~~diff
- 0073e0cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0073e0cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0073e0cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0073e0cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073e0cc bytes fd7b03a9
- 0073e0d0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0073e0d0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0073e0d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0073e0d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073e0d0 bytes f65704a9
- 0073e0d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0073e0d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0073e0d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0073e0d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0073e0d4 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94fb60061c2a9831b2b14cbd30bb293d"></a>

### [`0073ea18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md) → [`00768d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md) FUN_00768d24

採用 · 移動量 `+0x2a30c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073e89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e89c.md) · 呼出先 3件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) · 呼出先 3件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0073eaa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00768db0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0073ea98",
      "incomplete_value": true,
      "site": "0073eaa8",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0073eaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md#insn-0073eaa4) · [`0073eaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md#insn-0073eaa8)
- 新版 [`00768db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md#insn-00768db4) · [`00768db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md#insn-00768db0)

~~~diff
- 0073eaa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 0073eaa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0073eaa4 bytes 751600f9
- 0073eaa8 ["INT_ADD", "register:40f0:8", ["const:73eaa8:8", "const:4:8"]]
- 0073eaa8 ["CALL", null, ["callee:00c57c00:8"]]
+ 00768db4 ["INT_ADD", "register:40f0:8", ["const:768db4:8", "const:4:8"]]
+ 00768db4 ["CALL", null, ["callee:00c57c00:8"]]
- 0073eaa8 bytes c2711294
+ 00768db4 bytes 93bb1394
+ 00768db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
+ 00768db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00768db0 bytes 751600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f398ebc7ee9b0c62fe30f8a99d0218"></a>

### [`0073f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f3d4.md) → [`007696e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md) FUN_007696e0

採用 · 移動量 `+0x2a30c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 73.33% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00769730",
      "incomplete_value": true,
      "site": "00769734",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fffffffffffffff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0073f428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f3d4.md#insn-0073f428) · [`0073f3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f3d4.md#insn-0073f3e8) · [`0073f3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f3d4.md#insn-0073f3f4)
- 新版 [`00769734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md#insn-00769734) · [`007696f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md#insn-007696f4) · [`00769700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007696e0.md#insn-00769700)

~~~diff
- 0073f428 ["INT_ADD", "register:40f0:8", ["const:73f428:8", "const:4:8"]]
- 0073f428 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00769734 ["INT_ADD", "register:40f0:8", ["const:769734:8", "const:4:8"]]
+ 00769734 ["CALL", null, ["callee:00c57ab0:8"]]
- 0073f428 bytes 0e6f1294
+ 00769734 bytes dfb81394
- 0073f3e8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 0073f3e8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 007696f4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 007696f4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0073f3e8 bytes 48020034
+ 007696f4 bytes 48020034
- 0073f3f4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0073f3f4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00769700 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00769700 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0073f3f4 bytes f40100b4
+ 00769700 bytes f40100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0fff27335bea59556e351b78ffb7e6e"></a>

### [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) → [`007728a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md) FUN_007728a0

採用 · 移動量 `+0x2a340` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)
- 新版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.22% / 新版 81.22%

CFGの説明率　旧版 73.30% / 新版 80.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 1件, `store_value` 7件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00748570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00748570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00748574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00748570",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00748574",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00748598",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007728b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "007728b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007728d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md#insn-00748570) · [`00748574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md#insn-00748574) · [`00748598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md#insn-00748598)

~~~diff
- 00748570 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00748570 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00748570 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00748570 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00748570 bytes f65704a9
- 00748574 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00748574 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00748574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00748574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00748574 bytes f44f05a9
- 00748598 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00748598 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00748598 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00748598 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b22de638f973cf218dd46537a9935259"></a>

### [`0074931c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/0074931c.md) → [`0077365c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md) FUN_0077365c

採用 · 移動量 `+0x2a340` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 5件 [`007523a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523a8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 5件 [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.11% / 新版 85.11%

CFGの説明率　旧版 7.69% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0074931c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0074931c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00749320"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0074931c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00749320",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00749324",
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
      "0077365c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00773660",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00773664",
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

- 旧版 [`0074931c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/0074931c.md#insn-0074931c) · [`00749320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/0074931c.md#insn-00749320) · [`00749324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/0074931c.md#insn-00749324)

~~~diff
- 0074931c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0074931c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0074931c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0074931c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0074931c bytes fd7bbda9
- 00749320 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00749320 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00749320 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00749320 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00749320 bytes f65701a9
- 00749324 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00749324 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00749324 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00749324 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00749324 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad484e8b0d2963d0ec2f95ce4329f942"></a>

### [`00750888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750888.md) → [`0077acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077acec.md) FUN_0077acec

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ee758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ee/005ee758.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`0044ab84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab84.md)
- 新版 呼出元 1件 [`00613c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00613/00613c24.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.11% / 新版 88.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0075088c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0075088c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00750890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0075088c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00750890",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00750894",
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
      "0077acf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077acf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077acf8",
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

- 旧版 [`0075088c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750888.md#insn-0075088c) · [`00750890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750888.md#insn-00750890) · [`00750894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750888.md#insn-00750894)

~~~diff
- 0075088c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0075088c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0075088c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0075088c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0075088c bytes fd7b03a9
- 00750890 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00750890 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00750890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00750890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00750890 bytes fc6f04a9
- 00750894 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00750894 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00750894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00750894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00750894 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dbd4fb69a527035e2a42cd7df107ae5"></a>

### [`00750e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md) → [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md) FUN_0077b2cc

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0068f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068f/0068f070.md) [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) [`007507b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/007507b4.md) · 呼出先 11件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00702094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/00702094.md) [`0070219c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00702/0070219c.md)
- 新版 呼出元 3件 [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0077ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077ac18.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0072c194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c194.md) [`0072c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.04% / 新版 88.04%

CFGの説明率　旧版 57.53% / 新版 48.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b530",
      "incomplete_value": true,
      "site": "0077b544",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ac0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007510cc",
      "incomplete_value": true,
      "site": "007510e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b68c",
      "incomplete_value": true,
      "site": "0077b698",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751228",
      "incomplete_value": true,
      "site": "00751234",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 77,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751390"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077b318",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "0077b34c",
      "DATA",
      [
        "storage",
        "0032fda0",
        null,
        "dword"
      ]
    ],
    [
      "0077b350",
      "READ",
      [
        "storage",
        "00c1b6b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0077b318",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0077b34c",
      "DATA",
      [
        "storage",
        "00333de0",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0077b350",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00750eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md#insn-00750eb4) · [`00751264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md#insn-00751264) · [`0075127c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750e68.md#insn-0075127c)
- 新版 [`0077b318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md#insn-0077b318)

~~~diff
- 00750eb4 ["INT_ADD", "register:40f0:8", ["const:750eb4:8", "const:4:8"]]
- 00750eb4 ["CALL", null, ["ram:449aec:8"]]
+ 0077b318 ["INT_ADD", "register:40f0:8", ["const:77b318:8", "const:4:8"]]
+ 0077b318 ["CALL", null, ["ram:46c984:8"]]
- 00750eb4 bytes 0ee3f397
+ 0077b318 bytes 9bc5f397
- 00751264 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00751264 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00751264 ["CBRANCH", null, ["local:b45:8", "tmp:1:1"]]
- 00751264 bytes e8170054
- 0075127c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0075127c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0075127c ["COPY", "tmp:2:8", ["register:4050:8"]]
- 0075127c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0075127c bytes 4881889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-260dce577b2ccb92559c45ca43f7d8db"></a>

### [`0075171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md) → [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) FUN_0077bb80

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00751b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751b90.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`0072e2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0077bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md) · 呼出先 6件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`007584b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 67.44% / 新版 65.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0075171c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0075171c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0075171c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751720",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751724",
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
      "0077bb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0077bb84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077bb88",
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

- 旧版 [`0075171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md#insn-0075171c) · [`00751720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md#insn-00751720) · [`00751724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md#insn-00751724)

~~~diff
- 0075171c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0075171c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0075171c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0075171c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0075171c bytes fd7bbda9
- 00751720 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00751720 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00751720 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00751720 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00751720 bytes f65701a9
- 00751724 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00751724 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00751724 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00751724 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00751724 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6491db7bcead907a4b3cc4c0359fd05"></a>

### [`00751b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751b90.md) → [`0077bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md) FUN_0077bff4

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0075171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00751ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751b90.md#insn-00751ba0)
- 新版 [`0077c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md#insn-0077c004)

~~~diff
- 00751ba0 ["INT_ADD", "register:40f0:8", ["const:751ba0:8", "const:4:8"]]
- 00751ba0 ["CALL", null, ["callee:0077bb80:8"]]
+ 0077c004 ["INT_ADD", "register:40f0:8", ["const:77c004:8", "const:4:8"]]
+ 0077c004 ["CALL", null, ["callee:0077bb80:8"]]
- 00751ba0 bytes dffeff97
+ 0077c004 bytes dffeff97
~~~


<a id="compare-74312a03ccd480fa102fab9a07f53f0d"></a>

### [`00751bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751bb4.md) → [`0077c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c018.md) FUN_0077c018

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 16.67% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751bd0"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077c06c",
      "incomplete_value": false,
      "site": "0077c070",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751c08",
      "incomplete_value": false,
      "site": "00751c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0077c034"
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
      "unmatched:00751bd0",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00751be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c064"
      ]
    ],
    [
      "0077c070",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0077c034",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "0077c048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c064"
      ]
    ],
    [
      "0077c070",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00751bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751bb4.md#insn-00751bd0) · [`00751be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751bb4.md#insn-00751be4) · [`00751bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751bb4.md#insn-00751bf4)

~~~diff
- 00751bd0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00751bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00751bd0 bytes 080000f9
- 00751be4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00751be4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00751be4 bytes e00000b5
- 00751bf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00751bf4 ["INT_ADD", "register:40f0:8", ["const:751bf4:8", "const:4:8"]]
- 00751bf4 ["CALLIND", null, ["register:0:8"]]
- 00751bf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2eaee93ca499699a1bbfe5f67115d02"></a>

### [`00751c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751c4c.md) → [`0077c0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c0b0.md) FUN_0077c0b0

採用 · 移動量 `+0x2a464` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.00% / 新版 45.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751c50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00751c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751c50",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751c68",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0077c0b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077c0b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0077c0cc",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00751c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751c4c.md#insn-00751c4c) · [`00751c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751c4c.md#insn-00751c50) · [`00751c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751c4c.md#insn-00751c68)

~~~diff
- 00751c4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00751c4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00751c4c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00751c4c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00751c4c bytes fd7bbea9
- 00751c50 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00751c50 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00751c50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00751c50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00751c50 bytes f44f01a9
- 00751c68 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00751c68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00751c68 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf0e9ab804ef97106b17b3d9cdc5a32"></a>

### [`00751cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md) → [`0077c150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) FUN_0077c150

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 8件 [`006fbf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbf4c.md) [`006fbf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbf60.md) [`006fbfc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fb/006fbfc4.md) [`007520b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007520b8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 8件 [`0072604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/0072604c.md) [`00726060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726060.md) [`007260c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md) [`0077c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.59% / 新版 81.59%

CFGの説明率　旧版 36.71% / 新版 30.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 1件, `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00751d04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00751d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751d04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00751d24",
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
      "0077c164",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077c168",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0077c188",
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

- 旧版 [`00751d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md#insn-00751d00) · [`00751d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md#insn-00751d04) · [`00751d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751cec.md#insn-00751d24)

~~~diff
- 00751d00 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00751d00 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00751d00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00751d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00751d00 bytes f65709a9
- 00751d04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00751d04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00751d04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00751d04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00751d04 bytes f44f0aa9
- 00751d24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00751d24 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00751d24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00751d24 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b85f9595f9131297f1c19381de14e877"></a>

### [`007523bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523bc.md) → [`0077c820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md) FUN_0077c820

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00731710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/00731710.md) · 呼出先 2件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0075b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b8e4.md) · 呼出先 2件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 52.00% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00752418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0077c87c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077c880",
      "incomplete_value": true,
      "site": "0077c884",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
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
      "definition_site": "0075241c",
      "incomplete_value": true,
      "site": "00752420",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00752418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523bc.md#insn-00752418) · [`00752420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523bc.md#insn-00752420) · [`00752458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523bc.md#insn-00752458)
- 新版 [`0077c884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md#insn-0077c884) · [`0077c8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c820.md#insn-0077c8bc)

~~~diff
- 00752418 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00752418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00752418 bytes 090800f9
- 00752420 ["INT_ADD", "register:40f0:8", ["const:752420:8", "const:4:8"]]
- 00752420 ["CALL", null, ["callee:004945d0:8"]]
+ 0077c884 ["INT_ADD", "register:40f0:8", ["const:77c884:8", "const:4:8"]]
+ 0077c884 ["CALL", null, ["callee:004945d0:8"]]
- 00752420 bytes c67cf497
+ 0077c884 bytes 535ff497
- 00752458 ["INT_ADD", "register:40f0:8", ["const:752458:8", "const:4:8"]]
- 00752458 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0077c8bc ["INT_ADD", "register:40f0:8", ["const:77c8bc:8", "const:4:8"]]
+ 0077c8bc ["CALL", null, ["callee:00c57ab0:8"]]
- 00752458 bytes 02231294
+ 0077c8bc bytes 7d6c1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ba2e3a40411ed698520c5aeb614688"></a>

### [`0075246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md) → [`0077c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md) FUN_0077c8d0

採用 · 移動量 `+0x2a464` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007346b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/007346b0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0075e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e884.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 8.57% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00752470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00752470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00752474"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00752470",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00752474",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00752478",
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
      "0077c8d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077c8d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077c8dc",
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

- 旧版 [`00752470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md#insn-00752470) · [`00752474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md#insn-00752474) · [`00752478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md#insn-00752478)

~~~diff
- 00752470 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00752470 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00752470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00752470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00752470 bytes fd7b06a9
- 00752474 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00752474 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00752474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00752474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00752474 bytes fc6f07a9
- 00752478 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00752478 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00752478 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00752478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00752478 bytes fa6708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4b015126379695f3ea5fe5c9203af0"></a>

### [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) → [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) FUN_0077ca54

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0075246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md) [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md) [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.01% / 新版 92.01%

CFGの説明率　旧版 61.67% / 新版 54.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00752658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007527b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007527b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00752658",
      "WRITE",
      [
        "storage",
        "Stack[-0x178]",
        null,
        null
      ]
    ],
    [
      "unmatched:00752670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077cc20"
      ]
    ],
    [
      "unmatched:00752734",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077cbec"
      ]
    ]
  ],
  "added": [
    [
      "0077cabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x178]",
        null,
        null
      ]
    ],
    [
      "0077cad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077cc20"
      ]
    ],
    [
      "0077cb98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077cbec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00752658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md#insn-00752658) · [`00752664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md#insn-00752664) · [`00752668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md#insn-00752668)

~~~diff
- 00752658 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:78:8"]]
- 00752658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00752658 bytes e83f00f9
- 00752664 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00752664 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00752664 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00752664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00752664 bytes 9616809a
- 00752668 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00752668 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00752668 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00752668 ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00752668 bytes 35039a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a50c96be30bd350a539b7799492ae1f"></a>

### [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) → [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) FUN_0077d53c

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.54% / 新版 88.54%

CFGの説明率　旧版 59.57% / 新版 55.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00753770"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00753774"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007537ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00753194",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077d5d4"
      ]
    ],
    [
      "unmatched:007531b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077decc"
      ]
    ],
    [
      "0077d6b4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077d5f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077d5d4"
      ]
    ],
    [
      "0077d618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077decc"
      ]
    ],
    [
      "0077d6b4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00753194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md#insn-00753194) · [`007531b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md#insn-007531b4) · [`007531e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md#insn-007531e8)
- 新版 [`0077d64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md#insn-0077d64c)

~~~diff
- 00753194 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00753194 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00753194 bytes eafeff54
- 007531b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 007531b4 ["CBRANCH", null, ["local:b119:8", "tmp:0:1"]]
- 007531b4 bytes a3450054
- 007531e8 ["INT_ADD", "register:40f0:8", ["const:7531e8:8", "const:4:8"]]
- 007531e8 ["CALL", null, ["callee:00c57b40:8"]]
+ 0077d64c ["INT_ADD", "register:40f0:8", ["const:77d64c:8", "const:4:8"]]
+ 0077d64c ["CALL", null, ["callee:00c57b40:8"]]
- 007531e8 bytes c21f1294
+ 0077d64c bytes 3d691394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0b700c28f6e5cb070a90eadb0c70bdf"></a>

### [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) → [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) FUN_0077e0a4

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.61% / 新版 90.61%

CFGの説明率　旧版 68.67% / 新版 64.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00753c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00753c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00753c60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00753c58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00753c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x158]",
        null,
        null
      ]
    ],
    [
      "unmatched:00753c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x15c]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077e0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0077e0c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x158]",
        null,
        null
      ]
    ],
    [
      "0077e0d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x15c]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00753c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md#insn-00753c58) · [`00753c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md#insn-00753c60) · [`00753c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md#insn-00753c6c)

~~~diff
- 00753c58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00753c58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00753c58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00753c58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00753c58 bytes f44f18a9
- 00753c60 ["COPY", "tmp:0:4", ["register:4030:4"]]
- 00753c60 ["COPY", "tmp:1:4", ["register:4038:4"]]
- 00753c60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:38:8"]]
- 00753c60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:4"]]
- 00753c60 bytes e61f0729
- 00753c6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:34:8"]]
- 00753c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 00753c6c bytes e53700b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace604a13c61f87dd8abda005f0abfd8"></a>

### [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) → [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) FUN_0077ea50

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.01% / 新版 84.01%

CFGの説明率　旧版 55.56% / 新版 56.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754b28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00754630",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00754650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077ec8c"
      ]
    ],
    [
      "0077ebb8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077ea94",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0077eab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077ec8c"
      ]
    ],
    [
      "0077ebb8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00754630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md#insn-00754630) · [`00754644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md#insn-00754644) · [`00754648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md#insn-00754648)

~~~diff
- 00754630 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00754630 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00754630 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00754630 bytes a9831ef8
- 00754644 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00754644 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00754644 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00754644 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00754644 bytes b916809a
- 00754648 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00754648 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00754648 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00754648 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00754648 bytes 3c01949a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae37108d7fe17222dc66b77cd5999522"></a>

### [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) → [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) FUN_0077f3d4

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.78% / 新版 81.78%

CFGの説明率　旧版 45.61% / 新版 43.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_condition` 4件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00754f78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00754f74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00754f78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00754f7c",
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
      "0077f3d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0077f3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0077f3e0",
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

- 旧版 [`00754f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md#insn-00754f74) · [`00754f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md#insn-00754f78) · [`00754f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md#insn-00754f7c)

~~~diff
- 00754f74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00754f74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00754f74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00754f74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00754f74 bytes fd7b11a9
- 00754f78 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00754f78 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00754f78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00754f78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00754f78 bytes fc6f12a9
- 00754f7c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00754f7c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00754f7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00754f7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00754f7c bytes fa6713a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8d6e345e31b6be1248dab66c4b9412e"></a>

### [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) → [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) FUN_0077fd40

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.29% / 新版 88.29%

CFGの説明率　旧版 45.20% / 新版 50.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00755f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00755f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00755f70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00755a40",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0077fec8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00755b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007803f0"
      ]
    ]
  ],
  "added": [
    [
      "0077fea4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077fec8",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0077ff64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007803f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00755a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md#insn-00755a48) · [`00755a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md#insn-00755a70) · [`00755af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md#insn-00755af8)
- 新版 [`0077feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md#insn-0077feac) · [`0077fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md#insn-0077fed4)

~~~diff
- 00755a48 ["INT_ADD", "register:40f0:8", ["const:755a48:8", "const:4:8"]]
- 00755a48 ["CALL", null, ["callee:00441e54:8"]]
+ 0077feac ["INT_ADD", "register:40f0:8", ["const:77feac:8", "const:4:8"]]
+ 0077feac ["CALL", null, ["callee:00441e54:8"]]
- 00755a48 bytes 4326f397
+ 0077feac bytes ea07f397
- 00755a70 ["INT_ADD", "register:40f0:8", ["const:755a70:8", "const:4:8"]]
- 00755a70 ["CALL", null, ["callee:004427b4:8"]]
+ 0077fed4 ["INT_ADD", "register:40f0:8", ["const:77fed4:8", "const:4:8"]]
+ 0077fed4 ["CALL", null, ["callee:004427b4:8"]]
- 00755a70 bytes 9128f397
+ 0077fed4 bytes 380af397
- 00755af8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00755af8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00755af8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00755af8 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00755af8 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4772eb4e230b66eac405fa2b70302d98"></a>

### [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) → [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) FUN_007806ac

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 69.05% / 新版 72.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00756894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00756898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00780cf8"
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
      "0078080c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00780830",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00780964",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0078080c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00780830",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00780964",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007563b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md#insn-007563b0) · [`007563d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md#insn-007563d8) · [`00756508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md#insn-00756508)
- 新版 [`00780814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-00780814) · [`0078083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-0078083c) · [`0078096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-0078096c)

~~~diff
- 007563b0 ["INT_ADD", "register:40f0:8", ["const:7563b0:8", "const:4:8"]]
- 007563b0 ["CALL", null, ["callee:00441e54:8"]]
+ 00780814 ["INT_ADD", "register:40f0:8", ["const:780814:8", "const:4:8"]]
+ 00780814 ["CALL", null, ["callee:00441e54:8"]]
- 007563b0 bytes e923f397
+ 00780814 bytes 9005f397
- 007563d8 ["INT_ADD", "register:40f0:8", ["const:7563d8:8", "const:4:8"]]
- 007563d8 ["CALL", null, ["callee:004427b4:8"]]
+ 0078083c ["INT_ADD", "register:40f0:8", ["const:78083c:8", "const:4:8"]]
+ 0078083c ["CALL", null, ["callee:004427b4:8"]]
- 007563d8 bytes 3726f397
+ 0078083c bytes de07f397
- 00756508 ["INT_ADD", "register:40f0:8", ["const:756508:8", "const:4:8"]]
- 00756508 ["CALL", null, ["callee:00441e54:8"]]
+ 0078096c ["INT_ADD", "register:40f0:8", ["const:78096c:8", "const:4:8"]]
+ 0078096c ["CALL", null, ["callee:00441e54:8"]]
- 00756508 bytes 9323f397
+ 0078096c bytes 3a05f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6844b0670573cc47ddd5b95de98ab735"></a>

### [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) → [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) FUN_00781004

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) [`00a00ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00ce4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) [`00a5e2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e2cc.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.17% / 新版 90.17%

CFGの説明率　旧版 59.89% / 新版 68.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00756bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00756bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00756bc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00756bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00756bc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x160]",
        null,
        null
      ]
    ],
    [
      "unmatched:00756bcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x154]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0078101c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00781024",
      "WRITE",
      [
        "storage",
        "Stack[-0x160]",
        null,
        null
      ]
    ],
    [
      "00781030",
      "WRITE",
      [
        "storage",
        "Stack[-0x154]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00756bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md#insn-00756bb8) · [`00756bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md#insn-00756bc0) · [`00756bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md#insn-00756bcc)

~~~diff
- 00756bb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00756bb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00756bb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00756bb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00756bb8 bytes f44f16a9
- 00756bc0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00756bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:8"]]
- 00756bc0 bytes e40b00f9
- 00756bcc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:1c:8"]]
- 00756bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:4"]]
- 00756bcc bytes e31f00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b41b2365c5636266f415d6a428c95af"></a>

### [`00757514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757514.md) → [`00781978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md) FUN_00781978

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0078199c",
      "incomplete_value": false,
      "site": "0078199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757538",
      "incomplete_value": false,
      "site": "00757538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "0078199c",
      "DATA",
      [
        "storage",
        "00bfae78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078199c",
      "DATA",
      [
        "storage",
        "00c77fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757514.md#insn-00757528) · [`00757530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757514.md#insn-00757530) · [`00757534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757514.md#insn-00757534)
- 新版 [`0078198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-0078198c) · [`00781994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-00781994) · [`00781998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-00781998)

~~~diff
- 00757528 ["INT_ADD", "register:40f0:8", ["const:757528:8", "const:4:8"]]
- 00757528 ["CALL", null, ["callee:00c57a90:8"]]
+ 0078198c ["INT_ADD", "register:40f0:8", ["const:78198c:8", "const:4:8"]]
+ 0078198c ["CALL", null, ["callee:00c57a90:8"]]
- 00757528 bytes c60e1294
+ 0078198c bytes 41581394
- 00757530 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00781994 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 00757530 bytes 082500f0
+ 00781994 bytes a82700d0
- 00757534 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00757534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781998 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00781998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757534 bytes 08e13991
+ 00781998 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0360d36eedfacf329433602b0db4bd6a"></a>

### [`007575fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007575fc.md) → [`00781a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md) FUN_00781a60

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00781a84",
      "incomplete_value": false,
      "site": "00781a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757620",
      "incomplete_value": false,
      "site": "00757620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "00781a84",
      "DATA",
      [
        "storage",
        "00bfaef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781a84",
      "DATA",
      [
        "storage",
        "00c78020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007575fc.md#insn-00757610) · [`00757618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007575fc.md#insn-00757618) · [`0075761c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007575fc.md#insn-0075761c)
- 新版 [`00781a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md#insn-00781a74) · [`00781a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md#insn-00781a7c) · [`00781a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md#insn-00781a80)

~~~diff
- 00757610 ["INT_ADD", "register:40f0:8", ["const:757610:8", "const:4:8"]]
- 00757610 ["CALL", null, ["callee:00c57a90:8"]]
+ 00781a74 ["INT_ADD", "register:40f0:8", ["const:781a74:8", "const:4:8"]]
+ 00781a74 ["CALL", null, ["callee:00c57a90:8"]]
- 00757610 bytes 8c0e1294
+ 00781a74 bytes 07581394
- 00757618 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00781a7c ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00757618 bytes 082500f0
+ 00781a7c bytes a82700f0
- 0075761c ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 0075761c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781a80 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00781a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075761c bytes 08e13b91
+ 00781a80 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d7be5acb1919656e8025c0b1236951"></a>

### [`0075789c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075789c.md) → [`00781d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md) FUN_00781d00

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00781d24",
      "incomplete_value": false,
      "site": "00781d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007578c0",
      "incomplete_value": false,
      "site": "007578c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "00781d24",
      "DATA",
      [
        "storage",
        "00bfaff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781d24",
      "DATA",
      [
        "storage",
        "00c78120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007578b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075789c.md#insn-007578b0) · [`007578b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075789c.md#insn-007578b8) · [`007578bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075789c.md#insn-007578bc)
- 新版 [`00781d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md#insn-00781d14) · [`00781d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md#insn-00781d1c) · [`00781d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md#insn-00781d20)

~~~diff
- 007578b0 ["INT_ADD", "register:40f0:8", ["const:7578b0:8", "const:4:8"]]
- 007578b0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00781d14 ["INT_ADD", "register:40f0:8", ["const:781d14:8", "const:4:8"]]
+ 00781d14 ["CALL", null, ["callee:00c57a90:8"]]
- 007578b0 bytes e40d1294
+ 00781d14 bytes 5f571394
- 007578b8 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 00781d1c ["COPY", "register:4040:8", ["const:c78000:8"]]
- 007578b8 bytes 082500f0
+ 00781d1c bytes a82700f0
- 007578bc ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 007578bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781d20 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00781d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007578bc bytes 08e13f91
+ 00781d20 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b966b9e76d2ce4f60151ec4bbb4aa1"></a>

### [`007579a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579a4.md) → [`00781e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md) FUN_00781e08

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00781e2c",
      "incomplete_value": false,
      "site": "00781e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007579c8",
      "incomplete_value": false,
      "site": "007579c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00781e2c",
      "DATA",
      [
        "storage",
        "00bfb078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781e2c",
      "DATA",
      [
        "storage",
        "00c781a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007579b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579a4.md#insn-007579b8) · [`007579c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579a4.md#insn-007579c0) · [`007579c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579a4.md#insn-007579c4)
- 新版 [`00781e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md#insn-00781e1c) · [`00781e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md#insn-00781e24) · [`00781e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md#insn-00781e28)

~~~diff
- 007579b8 ["INT_ADD", "register:40f0:8", ["const:7579b8:8", "const:4:8"]]
- 007579b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00781e1c ["INT_ADD", "register:40f0:8", ["const:781e1c:8", "const:4:8"]]
+ 00781e1c ["CALL", null, ["callee:00c57a90:8"]]
- 007579b8 bytes a20d1294
+ 00781e1c bytes 1d571394
- 007579c0 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00781e24 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 007579c0 bytes 28250090
+ 00781e24 bytes a82700f0
- 007579c4 ["COPY", "tmp:0:8", ["const:78:8"]]
- 007579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781e28 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00781e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007579c4 bytes 08e10191
+ 00781e28 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c6756e68db787a040621466d9c61030"></a>

### [`007579f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579f4.md) → [`00781e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md) FUN_00781e58

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 86.35% / 新版 86.35%

CFGの説明率　旧版 90.41% / 新版 92.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_destination` 1件, `store_value` 6件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00781fb8",
      "incomplete_value": true,
      "site": "00781fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757b54",
      "incomplete_value": true,
      "site": "00757b5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
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
      "definition_site": "00781fc4",
      "incomplete_value": true,
      "site": "00781fc4",
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
            "const:3478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757b60",
      "incomplete_value": true,
      "site": "00757b60",
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
            "const:3388:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00781ff0",
      "incomplete_value": true,
      "site": "00781ff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a3a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757b8c",
      "incomplete_value": true,
      "site": "00757b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
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
      "00781e94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00757a54"
      ]
    ],
    [
      "00781e9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:00757a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00781e94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00781eb8"
      ]
    ],
    [
      "00781e9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781eb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579f4.md#insn-00757a38) · [`00757a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579f4.md#insn-00757a54) · [`00757ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579f4.md#insn-00757ab4)
- 新版 [`00781e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md#insn-00781e9c) · [`00781f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md#insn-00781f18)

~~~diff
- 00757a38 ["INT_ADD", "register:40f0:8", ["const:757a38:8", "const:4:8"]]
- 00757a38 ["CALL", null, ["ram:457e1c:8"]]
+ 00781e9c ["INT_ADD", "register:40f0:8", ["const:781e9c:8", "const:4:8"]]
+ 00781e9c ["CALL", null, ["ram:47acb4:8"]]
- 00757a38 bytes f900f497
+ 00781e9c bytes 86e3f397
- 00757a54 ["INT_ADD", "register:40f0:8", ["const:757a54:8", "const:4:8"]]
- 00757a54 ["CALL", null, ["ram:457e1c:8"]]
- 00757a54 bytes f200f497
- 00757ab4 ["INT_ADD", "register:40f0:8", ["const:757ab4:8", "const:4:8"]]
- 00757ab4 ["CALL", null, ["ram:73a8e0:8"]]
+ 00781f18 ["INT_ADD", "register:40f0:8", ["const:781f18:8", "const:4:8"]]
+ 00781f18 ["CALL", null, ["ram:764bec:8"]]
- 00757ab4 bytes 8b8bff97
+ 00781f18 bytes 358bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-356b96bdbfe36a84af0a4b5b20f3915e"></a>

### [`00757f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f30.md) → [`00782394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782394.md) FUN_00782394

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00782398",
      "incomplete_value": false,
      "site": "0078239c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757f34",
      "incomplete_value": false,
      "site": "00757f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0078239c",
      "DATA",
      [
        "storage",
        "00bfb0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078239c",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f30.md#insn-00757f30) · [`00757f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f30.md#insn-00757f34)
- 新版 [`00782394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782394.md#insn-00782394) · [`00782398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782394.md#insn-00782398)

~~~diff
- 00757f30 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782394 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00757f30 bytes 28250090
+ 00782394 bytes a82700d0
- 00757f34 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00757f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782398 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00782398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757f34 bytes 08a10391
+ 00782398 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ca951019034941910dbc7abe9718b4"></a>

### [`00757f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f48.md) → [`007823ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md) FUN_007823ac

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 64.71% / 新版 62.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00757ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00757ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00758000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007823e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:00757fc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007825d8"
      ]
    ],
    [
      "unmatched:00757ff0",
      "READ",
      [
        "storage",
        "002abac8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007823e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00782424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007825d8"
      ]
    ],
    [
      "00782454",
      "READ",
      [
        "storage",
        "002bc9eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f48.md#insn-00757f84) · [`00757fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f48.md#insn-00757fc0) · [`00757ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f48.md#insn-00757ff4)
- 新版 [`007823e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md#insn-007823e8)

~~~diff
- 00757f84 ["INT_ADD", "register:40f0:8", ["const:757f84:8", "const:4:8"]]
- 00757f84 ["CALL", null, ["ram:457e1c:8"]]
+ 007823e8 ["INT_ADD", "register:40f0:8", ["const:7823e8:8", "const:4:8"]]
+ 007823e8 ["CALL", null, ["ram:47acb4:8"]]
- 00757f84 bytes a6fff397
+ 007823e8 bytes 33e2f397
- 00757fc0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00757fc0 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00757fc0 bytes a10d0054
- 00757ff4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00757ff4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00757ff4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00757ff4 bytes e8630039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-028c0cbfb59ed1369091491f389de74d"></a>

### [`0075833c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075833c.md) → [`007827a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md) FUN_007827a0

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "007827b4",
      "incomplete_value": false,
      "site": "007827b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758350",
      "incomplete_value": false,
      "site": "00758354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
      "007827b8",
      "DATA",
      [
        "storage",
        "00bfb158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007827b8",
      "DATA",
      [
        "storage",
        "00c78280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075833c.md#insn-00758348) · [`0075834c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075833c.md#insn-0075834c) · [`00758350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075833c.md#insn-00758350)
- 新版 [`007827ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md#insn-007827ac) · [`007827b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md#insn-007827b0) · [`007827b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md#insn-007827b4)

~~~diff
- 00758348 ["INT_ADD", "register:40f0:8", ["const:758348:8", "const:4:8"]]
- 00758348 ["CALL", null, ["callee:00c57a90:8"]]
+ 007827ac ["INT_ADD", "register:40f0:8", ["const:7827ac:8", "const:4:8"]]
+ 007827ac ["CALL", null, ["callee:00c57a90:8"]]
- 00758348 bytes 3e0b1294
+ 007827ac bytes b9541394
- 0075834c ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 007827b0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0075834c bytes 082500f0
+ 007827b0 bytes a82700d0
- 00758350 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00758350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007827b4 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007827b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007827b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007827b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758350 bytes 08610591
+ 007827b4 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22bf7ef060d7d6cea1fdc1251eacd1f4"></a>

### [`00758360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758360.md) → [`007827c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827c4.md) FUN_007827c4

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007827c8",
      "incomplete_value": false,
      "site": "007827cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758364",
      "incomplete_value": false,
      "site": "00758368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "007827cc",
      "DATA",
      [
        "storage",
        "00bfb158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007827cc",
      "DATA",
      [
        "storage",
        "00c78280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758360.md#insn-00758360) · [`00758364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758360.md#insn-00758364)
- 新版 [`007827c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827c4.md#insn-007827c4) · [`007827c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827c4.md#insn-007827c8)

~~~diff
- 00758360 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 007827c4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00758360 bytes 082500f0
+ 007827c4 bytes a82700d0
- 00758364 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00758364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007827c8 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 007827c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007827c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007827c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758364 bytes 08610591
+ 007827c8 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09699d483a98b0e6748de280c20f12ea"></a>

### [`00758378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md) → [`007827dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827dc.md) FUN_007827dc

採用 · 移動量 `+0x2a464` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`007591f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/007591f4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 82.52% / 新版 82.52%

CFGの説明率　旧版 76.00% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 4件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00782888",
      "incomplete_value": true,
      "site": "00782898",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758424",
      "incomplete_value": true,
      "site": "00758434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dbe:8"
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
      "definition_site": "0078288c",
      "incomplete_value": true,
      "site": "0078289c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00758428",
      "incomplete_value": true,
      "site": "00758438",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00782890",
      "incomplete_value": true,
      "site": "007828a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075842c",
      "incomplete_value": true,
      "site": "0075843c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df0:8"
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
      "unmatched:007583c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f23b4"
      ]
    ],
    [
      "unmatched:007583c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:007583cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072f020"
      ]
    ]
  ],
  "added": [
    [
      "00782828",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "0078282c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00782830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007591f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007583c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md#insn-007583c4) · [`007583c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md#insn-007583c8) · [`007583cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md#insn-007583cc)

~~~diff
- 007583c4 ["INT_ADD", "register:40f0:8", ["const:7583c4:8", "const:4:8"]]
- 007583c4 ["CALL", null, ["ram:6f23b4:8"]]
- 007583c4 bytes fc67fe97
- 007583c8 ["INT_ADD", "register:40f0:8", ["const:7583c8:8", "const:4:8"]]
- 007583c8 ["CALL", null, ["callee:008514b8:8"]]
- 007583c8 bytes 6e1c0394
- 007583cc ["INT_ADD", "register:40f0:8", ["const:7583cc:8", "const:4:8"]]
- 007583cc ["CALL", null, ["ram:72f020:8"]]
- 007583cc bytes 155bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8370d64b1a86e20b6ce8e89d9a0c5dd7"></a>

### [`007585d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585d0.md) → [`00782a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md) FUN_00782a34

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00782a48",
      "incomplete_value": false,
      "site": "00782a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585e4",
      "incomplete_value": false,
      "site": "007585e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
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
      "00782a4c",
      "DATA",
      [
        "storage",
        "00bfb1c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782a4c",
      "DATA",
      [
        "storage",
        "00c782f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585d0.md#insn-007585dc) · [`007585e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585d0.md#insn-007585e0) · [`007585e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585d0.md#insn-007585e4)
- 新版 [`00782a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md#insn-00782a40) · [`00782a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md#insn-00782a44) · [`00782a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md#insn-00782a48)

~~~diff
- 007585dc ["INT_ADD", "register:40f0:8", ["const:7585dc:8", "const:4:8"]]
- 007585dc ["CALL", null, ["callee:00c57a90:8"]]
+ 00782a40 ["INT_ADD", "register:40f0:8", ["const:782a40:8", "const:4:8"]]
+ 00782a40 ["CALL", null, ["callee:00c57a90:8"]]
- 007585dc bytes 990a1294
+ 00782a40 bytes 14541394
- 007585e0 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782a44 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 007585e0 bytes 082500f0
+ 00782a44 bytes a82700d0
- 007585e4 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 007585e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782a48 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00782a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585e4 bytes 08210791
+ 00782a48 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055d5c31831b49f8235e58d4e20f9607"></a>

### [`007585f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585f4.md) → [`00782a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a58.md) FUN_00782a58

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00782a5c",
      "incomplete_value": false,
      "site": "00782a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585f8",
      "incomplete_value": false,
      "site": "007585fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00782a60",
      "DATA",
      [
        "storage",
        "00bfb1c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782a60",
      "DATA",
      [
        "storage",
        "00c782f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585f4.md#insn-007585f4) · [`007585f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585f4.md#insn-007585f8)
- 新版 [`00782a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a58.md#insn-00782a58) · [`00782a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a58.md#insn-00782a5c)

~~~diff
- 007585f4 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782a58 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 007585f4 bytes 082500f0
+ 00782a58 bytes a82700d0
- 007585f8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 007585f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782a5c ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00782a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585f8 bytes 08210791
+ 00782a5c bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e460cbc3750189ed0044bd0bb9cc8ffa"></a>

### [`007586cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586cc.md) → [`00782b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md) FUN_00782b30

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782b40",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007586dc",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00782b3c",
      "incomplete_value": false,
      "site": "00782b40",
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
    "old": {
      "definition_site": "007586d8",
      "incomplete_value": false,
      "site": "007586dc",
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
            "const:39d:8"
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
      "00782b3c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00782b40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00782b3c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00782b40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007586dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586cc.md#insn-007586dc) · [`007586d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586cc.md#insn-007586d4) · [`007586d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586cc.md#insn-007586d8)
- 新版 [`00782b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md#insn-00782b40) · [`00782b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md#insn-00782b38) · [`00782b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md#insn-00782b3c)

~~~diff
- 007586dc ["INT_ADD", "register:40f0:8", ["const:7586dc:8", "const:4:8"]]
- 007586dc ["CALL", null, ["ram:418c38:8"]]
+ 00782b40 ["INT_ADD", "register:40f0:8", ["const:782b40:8", "const:4:8"]]
+ 00782b40 ["CALL", null, ["ram:43b738:8"]]
- 007586dc bytes 5701f397
+ 00782b40 bytes fee2f297
- 007586d4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00782b38 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 007586d4 bytes 60dafff0
+ 00782b38 bytes a0d9ffb0
- 007586d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 007586d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00782b3c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00782b3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00782b3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00782b3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007586d8 bytes 00740e91
+ 00782b3c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a876e7bc75a6eba0d370b5035ed267b7"></a>

### [`007586e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586e4.md) → [`00782b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md) FUN_00782b48

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00782b6c",
      "incomplete_value": false,
      "site": "00782b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758708",
      "incomplete_value": false,
      "site": "00758708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00782b6c",
      "DATA",
      [
        "storage",
        "00bfb278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782b6c",
      "DATA",
      [
        "storage",
        "00c783a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007586f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586e4.md#insn-007586f8) · [`00758700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586e4.md#insn-00758700) · [`00758704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586e4.md#insn-00758704)
- 新版 [`00782b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md#insn-00782b5c) · [`00782b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md#insn-00782b64) · [`00782b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md#insn-00782b68)

~~~diff
- 007586f8 ["INT_ADD", "register:40f0:8", ["const:7586f8:8", "const:4:8"]]
- 007586f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00782b5c ["INT_ADD", "register:40f0:8", ["const:782b5c:8", "const:4:8"]]
+ 00782b5c ["CALL", null, ["callee:00c57a90:8"]]
- 007586f8 bytes 520a1294
+ 00782b5c bytes cd531394
- 00758700 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782b64 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00758700 bytes 082500f0
+ 00782b64 bytes a82700d0
- 00758704 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00758704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782b68 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00782b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758704 bytes 08e10991
+ 00782b68 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77325010cb29bc9a76868f8515a15373"></a>

### [`007587d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587d4.md) → [`00782c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md) FUN_00782c38

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00782c4c",
      "incomplete_value": false,
      "site": "00782c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007587e8",
      "incomplete_value": false,
      "site": "007587ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00782c50",
      "DATA",
      [
        "storage",
        "00bfb2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782c50",
      "DATA",
      [
        "storage",
        "00c78420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007587e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587d4.md#insn-007587e0) · [`007587e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587d4.md#insn-007587e4) · [`007587e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587d4.md#insn-007587e8)
- 新版 [`00782c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md#insn-00782c44) · [`00782c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md#insn-00782c48) · [`00782c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md#insn-00782c4c)

~~~diff
- 007587e0 ["INT_ADD", "register:40f0:8", ["const:7587e0:8", "const:4:8"]]
- 007587e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00782c44 ["INT_ADD", "register:40f0:8", ["const:782c44:8", "const:4:8"]]
+ 00782c44 ["CALL", null, ["callee:00c57a90:8"]]
- 007587e0 bytes 180a1294
+ 00782c44 bytes 93531394
- 007587e4 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782c48 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 007587e4 bytes 082500f0
+ 00782c48 bytes a82700d0
- 007587e8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007587e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782c4c ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00782c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007587e8 bytes 08e10b91
+ 00782c4c bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7986e0d8f08010168e528abe3a55d7aa"></a>

### [`00758810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758810.md) → [`00782c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md) FUN_00782c74

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "00782c98",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00758834",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00782c98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00782c98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758810.md#insn-00758834) · [`00758840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758810.md#insn-00758840)
- 新版 [`00782c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md#insn-00782c98) · [`00782ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md#insn-00782ca4)

~~~diff
- 00758834 ["INT_ADD", "register:40f0:8", ["const:758834:8", "const:4:8"]]
- 00758834 ["CALL", null, ["ram:457e1c:8"]]
+ 00782c98 ["INT_ADD", "register:40f0:8", ["const:782c98:8", "const:4:8"]]
+ 00782c98 ["CALL", null, ["ram:47acb4:8"]]
- 00758834 bytes 7afdf397
+ 00782c98 bytes 07e0f397
- 00758840 ["INT_ADD", "register:40f0:8", ["const:758840:8", "const:4:8"]]
- 00758840 ["CALL", null, ["callee:0047cd94:8"]]
+ 00782ca4 ["INT_ADD", "register:40f0:8", ["const:782ca4:8", "const:4:8"]]
+ 00782ca4 ["CALL", null, ["callee:0047cd94:8"]]
- 00758840 bytes af05f497
+ 00782ca4 bytes 3ce8f397
~~~


<a id="compare-5935c891db53c5e67d8a22bceda5837f"></a>

### [`00758884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758884.md) → [`00782ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md) FUN_00782ce8

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00782cfc",
      "incomplete_value": false,
      "site": "00782d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758898",
      "incomplete_value": false,
      "site": "0075889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00782d00",
      "DATA",
      [
        "storage",
        "00bfb378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782d00",
      "DATA",
      [
        "storage",
        "00c784a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758884.md#insn-00758890) · [`00758894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758884.md#insn-00758894) · [`00758898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758884.md#insn-00758898)
- 新版 [`00782cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md#insn-00782cf4) · [`00782cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md#insn-00782cf8) · [`00782cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md#insn-00782cfc)

~~~diff
- 00758890 ["INT_ADD", "register:40f0:8", ["const:758890:8", "const:4:8"]]
- 00758890 ["CALL", null, ["callee:00c57a90:8"]]
+ 00782cf4 ["INT_ADD", "register:40f0:8", ["const:782cf4:8", "const:4:8"]]
+ 00782cf4 ["CALL", null, ["callee:00c57a90:8"]]
- 00758890 bytes ec091294
+ 00782cf4 bytes 67531394
- 00758894 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782cf8 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00758894 bytes 082500f0
+ 00782cf8 bytes a82700d0
- 00758898 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00758898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782cfc ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00782cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758898 bytes 08e10d91
+ 00782cfc bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c233f3498a9434e54b2cd6d52285edc5"></a>

### [`007588c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007588c0.md) → [`00782d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md) FUN_00782d24

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

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
      "site": "00782d48",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007588e4",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00782d48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00782d48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007588e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007588c0.md#insn-007588e4) · [`007588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007588c0.md#insn-007588f0)
- 新版 [`00782d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md#insn-00782d48) · [`00782d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md#insn-00782d54)

~~~diff
- 007588e4 ["INT_ADD", "register:40f0:8", ["const:7588e4:8", "const:4:8"]]
- 007588e4 ["CALL", null, ["ram:457e1c:8"]]
+ 00782d48 ["INT_ADD", "register:40f0:8", ["const:782d48:8", "const:4:8"]]
+ 00782d48 ["CALL", null, ["ram:47acb4:8"]]
- 007588e4 bytes 4efdf397
+ 00782d48 bytes dbdff397
- 007588f0 ["INT_ADD", "register:40f0:8", ["const:7588f0:8", "const:4:8"]]
- 007588f0 ["CALL", null, ["callee:0047cd94:8"]]
+ 00782d54 ["INT_ADD", "register:40f0:8", ["const:782d54:8", "const:4:8"]]
+ 00782d54 ["CALL", null, ["callee:0047cd94:8"]]
- 007588f0 bytes 8305f497
+ 00782d54 bytes 10e8f397
~~~


<a id="compare-15556879b215d05498f56cfd4e25250d"></a>

### [`00758934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758934.md) → [`00782d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md) FUN_00782d98

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00782dac",
      "incomplete_value": false,
      "site": "00782db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758948",
      "incomplete_value": false,
      "site": "0075894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00782db0",
      "DATA",
      [
        "storage",
        "00bfb3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782db0",
      "DATA",
      [
        "storage",
        "00c78520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758934.md#insn-00758940) · [`00758944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758934.md#insn-00758944) · [`00758948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758934.md#insn-00758948)
- 新版 [`00782da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md#insn-00782da4) · [`00782da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md#insn-00782da8) · [`00782dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md#insn-00782dac)

~~~diff
- 00758940 ["INT_ADD", "register:40f0:8", ["const:758940:8", "const:4:8"]]
- 00758940 ["CALL", null, ["callee:00c57a90:8"]]
+ 00782da4 ["INT_ADD", "register:40f0:8", ["const:782da4:8", "const:4:8"]]
+ 00782da4 ["CALL", null, ["callee:00c57a90:8"]]
- 00758940 bytes c0091294
+ 00782da4 bytes 3b531394
- 00758944 ["COPY", "register:4040:8", ["const:bfb000:8"]]
+ 00782da8 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00758944 bytes 082500f0
+ 00782da8 bytes a82700d0
- 00758948 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00758948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782dac ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00782dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758948 bytes 08e10f91
+ 00782dac bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6592b228f94d9b00d9596238ad8ce2ed"></a>

### [`00758970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758970.md) → [`00782dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md) FUN_00782dd4

採用 · 移動量 `+0x2a464` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00782df8",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00758994",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "site": "00782e20",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007589bc",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00782df8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00782e20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00782df8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00782e20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758970.md#insn-00758994) · [`007589bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758970.md#insn-007589bc) · [`007589a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758970.md#insn-007589a0)
- 新版 [`00782df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782df8) · [`00782e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782e20) · [`00782e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782e04)

~~~diff
- 00758994 ["INT_ADD", "register:40f0:8", ["const:758994:8", "const:4:8"]]
- 00758994 ["CALL", null, ["ram:457e1c:8"]]
+ 00782df8 ["INT_ADD", "register:40f0:8", ["const:782df8:8", "const:4:8"]]
+ 00782df8 ["CALL", null, ["ram:47acb4:8"]]
- 00758994 bytes 22fdf397
+ 00782df8 bytes afdff397
- 007589bc ["INT_ADD", "register:40f0:8", ["const:7589bc:8", "const:4:8"]]
- 007589bc ["CALL", null, ["ram:457e1c:8"]]
+ 00782e20 ["INT_ADD", "register:40f0:8", ["const:782e20:8", "const:4:8"]]
+ 00782e20 ["CALL", null, ["ram:47acb4:8"]]
- 007589bc bytes 18fdf397
+ 00782e20 bytes a5dff397
- 007589a0 ["INT_ADD", "register:40f0:8", ["const:7589a0:8", "const:4:8"]]
- 007589a0 ["CALL", null, ["callee:0047cd94:8"]]
+ 00782e04 ["INT_ADD", "register:40f0:8", ["const:782e04:8", "const:4:8"]]
+ 00782e04 ["CALL", null, ["callee:0047cd94:8"]]
- 007589a0 bytes 5705f497
+ 00782e04 bytes e4e7f397
~~~


